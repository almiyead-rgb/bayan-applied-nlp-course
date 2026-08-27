#!/usr/bin/env python3
"""Offline release gate for the public SDA-AIE-211 learner materials."""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
from urllib.parse import unquote
import csv
import json
import re
import subprocess
import sys
import zipfile


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_MARKERS = {
    "00_runtime_doctor.ipynb": "BAYAN_ENV_READY = True",
    "01_text_processing_tokenization.ipynb": "DAY1_NOTEBOOK1_CORE=PASS",
    "02_attention_transformers.ipynb": "DAY1_NOTEBOOK2_CORE=PASS",
    "03_text_classification.ipynb": "DAY2_NOTEBOOK3_CORE=PASS",
    "04_ner_and_qa.ipynb": "DAY2_NOTEBOOK4_CORE=PASS",
    "05_arabic_nlp.ipynb": "DAY3_NOTEBOOK5_CORE=PASS",
    "06_semantic_search.ipynb": "DAY3_NOTEBOOK6_CORE=PASS",
    "07_evaluation_error_analysis.ipynb": "DAY3_NOTEBOOK7_CORE=PASS",
    "08_optimization_serving.ipynb": "DAY4_NOTEBOOK8_CORE=PASS",
}
EXTRA_NOTEBOOK_EVIDENCE = {
    "01_text_processing_tokenization.ipynb": "SPACY_SENTENCE_PIPELINE=PASS",
    "02_attention_transformers.ipynb": "TWO_CHECKPOINT_PARAMETER_AUDIT=PASS",
    "05_arabic_nlp.ipynb": "ARABIC_MODEL_COMPARISON=MEASURED_SMOKE",
    "06_semantic_search.ipynb": "RERANKING_TRADEOFF=MEASURED_SMOKE",
    "08_optimization_serving.ipynb": "FASTAPI_TESTCLIENT=PASS",
}
REQUIRED_PUBLIC_FILES = {
    "README.md", "START_HERE.md", "COURSE_GUIDE.md",
    "docs/00-course-spec.md", "docs/01-outcomes-map.md",
    "docs/02-verified-runs.md", "docs/03-capstone-spec.md",
    "assessments/README.md", "assessments/pa-01/starter_buggy.py",
    "assessments/pa-01/check_pa1.py", "assessments/pa-02/rival-team-report.md",
    "assessments/quiz/README.md", "downloads/bayan-student-starter.zip",
    "downloads/SHA256SUMS.txt", "student-starter/GETTING_STARTED.md",
}
PRIVATE_DIRECTORIES = {"private", "internal", "instructor", "trainer", "solutions", "answer_keys"}
PRIVATE_PREFIXES = ("instructor_", "trainer_", "internal_")
TEXT_SUFFIXES = {".md", ".py", ".txt", ".yml", ".yaml", ".json", ".csv", ".ipynb"}
LINK_PATTERN = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def looks_internal(relative: str) -> bool:
    path = Path(relative)
    parts = {part.lower() for part in path.parts[:-1]}
    name = path.name.lower()
    return (
        bool(parts & PRIVATE_DIRECTORIES)
        or name.startswith(PRIVATE_PREFIXES)
        or "master_guide" in name
        or "answer_key" in name
    )


def collect_files() -> set[str]:
    return {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
        and "__pycache__" not in path.parts and ".pytest_cache" not in path.parts
    }


def validate_text_and_links(files: set[str], errors: list[str]) -> tuple[int, int]:
    markdown_count = 0
    link_count = 0
    for relative in sorted(files):
        path = ROOT / relative
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        data = path.read_bytes()
        controls = [byte for byte in data if byte < 32 and byte not in (9, 10, 13)]
        if controls:
            fail(errors, f"{relative}: forbidden control characters {sorted(set(controls))}")
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            fail(errors, f"{relative}: not valid UTF-8: {exc}")
            continue
        if relative != "scripts/validate_course.py":
            if "bayan-nlp-student-template" in text:
                fail(errors, f"{relative}: references the retired/nonexistent external template")
            if (
                "/develop/" in text
                or "branch=develop" in text
                or "blob/develop" in text
                or "bayan-applied-nlp-course/develop" in text
            ):
                fail(errors, f"{relative}: public link still targets develop instead of main")
            if any(token in text for token in ("/workspace/scratch/", "/tmp/bayan", "audit-run.")):
                fail(errors, f"{relative}: internal execution path exposed")
        if path.suffix.lower() != ".md":
            continue
        markdown_count += 1
        if text.count("```") % 2:
            fail(errors, f"{relative}: unbalanced fenced code block")
        for raw_target in LINK_PATTERN.findall(text):
            link_count += 1
            target = raw_target.strip().strip("<>")
            if not target or target.startswith("#") or re.match(r"^(https?:|mailto:|data:)", target):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            resolved = (path.parent / target).resolve()
            if ROOT not in resolved.parents and resolved != ROOT:
                fail(errors, f"{relative}: link escapes repository: {raw_target}")
            elif not resolved.exists():
                fail(errors, f"{relative}: missing local link target: {raw_target}")
    return markdown_count, link_count


def output_text(output: dict) -> str:
    if output.get("output_type") == "stream":
        value = output.get("text", "")
        return "".join(value) if isinstance(value, list) else str(value)
    if output.get("output_type") in {"display_data", "execute_result"}:
        value = output.get("data", {}).get("text/plain", "")
        return "".join(value) if isinstance(value, list) else str(value)
    return ""


def validate_notebooks(errors: list[str]) -> tuple[int, int, int]:
    paths = sorted((ROOT / "notebooks").glob("*.ipynb"))
    names = {path.name for path in paths}
    if names != set(NOTEBOOK_MARKERS):
        fail(errors, f"Notebook set mismatch: {sorted(names ^ set(NOTEBOOK_MARKERS))}")
    code_total = output_total = image_total = 0
    for path in paths:
        relative = path.relative_to(ROOT).as_posix()
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(errors, f"{relative}: invalid JSON: {exc}")
            continue
        if notebook.get("nbformat") != 4 or notebook.get("nbformat_minor", 0) < 5:
            fail(errors, f"{relative}: expected nbformat 4.5+")
        cells = notebook.get("cells")
        if not isinstance(cells, list) or not cells:
            fail(errors, f"{relative}: missing cells")
            continue
        ids = [cell.get("id") for cell in cells]
        if any(not value for value in ids) or len(ids) != len(set(ids)):
            fail(errors, f"{relative}: cell IDs are missing or duplicated")
        author = notebook.get("metadata", {}).get("authors", [{}])[0].get("name")
        if author != "Meaad Al-Marri":
            fail(errors, f"{relative}: author metadata must be Meaad Al-Marri")
        execution = notebook.get("metadata", {}).get("bayan_execution", {})
        expected = {
            "verified_at_utc": "2026-08-27", "python": "3.12.13", "device": "cpu",
            "mode": "isolated_sequential_reference_run", "outputs_saved": True,
            "errors": 0, "stderr_outputs": 0,
        }
        for key, value in expected.items():
            if execution.get(key) != value:
                fail(errors, f"{relative}: bayan_execution.{key} must be {value!r}")
        code_cells = [cell for cell in cells if cell.get("cell_type") == "code"]
        code_total += len(code_cells)
        counts = [cell.get("execution_count") for cell in code_cells]
        if counts != list(range(1, len(code_cells) + 1)):
            fail(errors, f"{relative}: execution counts are not sequential: {counts}")
        captured: list[str] = []
        for index, cell in enumerate(code_cells):
            try:
                compile("".join(cell.get("source", [])), f"{relative}:cell-{index}", "exec")
            except SyntaxError as exc:
                fail(errors, f"{relative}: syntax error in code cell {index}: {exc}")
            outputs = cell.get("outputs", [])
            output_total += bool(outputs)
            for output in outputs:
                if output.get("output_type") == "error":
                    fail(errors, f"{relative}: error output in code cell {index}")
                if output.get("output_type") == "stream" and output.get("name") == "stderr":
                    fail(errors, f"{relative}: stderr output in code cell {index}")
                if output.get("output_type") == "display_data" and "image/png" in output.get("data", {}):
                    image_total += 1
                captured.append(output_text(output))
        all_output = "\n".join(captured)
        for marker in (NOTEBOOK_MARKERS[path.name], EXTRA_NOTEBOOK_EVIDENCE.get(path.name)):
            if marker and marker not in all_output:
                fail(errors, f"{relative}: saved outputs do not contain {marker!r}")
        badge = (
            "https://colab.research.google.com/github/almiyead-rgb/"
            f"bayan-applied-nlp-course/blob/main/notebooks/{path.name}"
        )
        source_text = "\n".join("".join(cell.get("source", [])) for cell in cells)
        if badge not in source_text:
            fail(errors, f"{relative}: Colab badge does not target main")
    if image_total < 1:
        fail(errors, "Notebook 02 attention visualisation is not saved as an image output")
    return len(paths), code_total, output_total


def validate_data(errors: list[str]) -> None:
    expected_csv = {
        "data/sample/bayan_day1_sample.csv": 12,
        "data/sample/bayan_day2_classification.csv": 40,
        "data/sample/bayan_day3_arabic.csv": 20,
        "data/sample/bayan_day3_cases.csv": 24,
        "data/sample/bayan_day3_predictions.csv": 36,
    }
    for relative, expected in expected_csv.items():
        with (ROOT / relative).open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if len(rows) != expected:
            fail(errors, f"{relative}: expected {expected} rows, found {len(rows)}")
    json.loads((ROOT / "data/sample/bayan_day2_qa.json").read_text(encoding="utf-8"))
    for relative, expected in {
        "data/sample/bayan_day2_ner.jsonl": 12,
        "data/sample/bayan_day3_queries.jsonl": 18,
    }.items():
        lines = [line for line in (ROOT / relative).read_text(encoding="utf-8").splitlines() if line.strip()]
        if len(lines) != expected:
            fail(errors, f"{relative}: expected {expected} JSONL rows, found {len(lines)}")
        for index, line in enumerate(lines, start=1):
            try:
                json.loads(line)
            except json.JSONDecodeError as exc:
                fail(errors, f"{relative}:{index}: invalid JSON: {exc}")


def validate_starter(errors: list[str]) -> int:
    archive_path = ROOT / "downloads/bayan-student-starter.zip"
    digest_line = (ROOT / "downloads/SHA256SUMS.txt").read_text(encoding="utf-8").strip()
    expected_digest, expected_name = digest_line.split(maxsplit=1)
    if expected_name != archive_path.name or expected_digest != sha256(archive_path.read_bytes()).hexdigest():
        fail(errors, "Student starter SHA256 does not match SHA256SUMS.txt")
    directory_files = {
        path.relative_to(ROOT / "student-starter").as_posix(): path.read_bytes()
        for path in (ROOT / "student-starter").rglob("*") if path.is_file()
    }
    with zipfile.ZipFile(archive_path) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            fail(errors, "Student starter archive contains duplicate paths")
        if any(name.startswith("/") or ".." in Path(name).parts for name in names):
            fail(errors, "Student starter archive contains an unsafe path")
        if set(names) != set(directory_files):
            fail(errors, "Student starter directory and ZIP file lists differ")
        for name, expected_bytes in directory_files.items():
            if archive.read(name) != expected_bytes:
                fail(errors, f"Student starter ZIP content mismatch: {name}")
    required = {
        "README.md", "STUDENT_PROFILE.md", "PROGRESS.md", "DECISIONS.md",
        "BENCHMARKS.md", "EVALUATION_REPORT.md", "MODEL_CARD.md", "DATA_CARD.md",
        "PROJECT_SUMMARY.json", "SUBMISSION.yml", "GETTING_STARTED.md",
        "reports/README.md", "sample_outputs/README.md",
    } | {f"notebooks/{name}" for name in NOTEBOOK_MARKERS}
    missing = required - set(directory_files)
    if missing:
        fail(errors, f"Student starter missing required paths: {sorted(missing)}")
    if len(directory_files) != 75:
        fail(errors, f"Student starter file count changed: expected 75, found {len(directory_files)}")
    return len(directory_files)


def validate_assessment_fixture(errors: list[str]) -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "assessments/pa-01/check_pa1.py")],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    if result.returncode != 1:
        fail(errors, f"PA-1 starter must exit 1 before learner fixes; got {result.returncode}")
    if result.stdout.count(": FAIL") != 3 or "PA1_STARTER_EXPECTED=3_FAIL" not in result.stdout:
        fail(errors, "PA-1 starter no longer exposes the three documented defects")


def validate_accreditation_contract(errors: list[str]) -> None:
    required_fragments = {
        "docs/03-capstone-spec.md": [
            "≥8", "≥0.80", "≥17/20", "Recall@10", "MRR@10",
            "≥100", "≤40 ms", "16", "Required measured extension",
        ],
        "docs/policies/assessment-and-completion.md": [
            "90/100", "+5", "80/100", "08:30–08:45", "09:50–10:20",
        ],
        "day-04/README.md": [
            "08:30–08:45", "09:50–10:20", "تجميع بيان I", "عروض بيان",
        ],
        "templates/PROJECT_SUMMARY.template.json": [
            '"sentiment"', '"extension"', '"evidence"',
        ],
        "notebooks/03_text_classification.ipynb": [
            "Two independent classification heads", "bayan-sentiment-contract",
        ],
    }
    for relative, fragments in required_fragments.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for fragment in fragments:
            if fragment not in text:
                fail(errors, f"{relative}: missing accreditation contract fragment {fragment!r}")


def main() -> int:
    errors: list[str] = []
    files = collect_files()
    missing = REQUIRED_PUBLIC_FILES - files
    if missing:
        fail(errors, f"Missing required public files: {sorted(missing)}")
    exposed = sorted(relative for relative in files if looks_internal(relative))
    if exposed:
        fail(errors, f"Private/internal paths exposed: {exposed}")
    oversized = sorted(
        relative for relative in files if (ROOT / relative).stat().st_size > 10 * 1024 * 1024
    )
    if oversized:
        fail(errors, f"Files above the 10 MiB public limit: {oversized}")

    markdown_count, link_count = validate_text_and_links(files, errors)
    notebook_count, code_cells, output_cells = validate_notebooks(errors)
    validate_data(errors)
    starter_files = validate_starter(errors)
    validate_assessment_fixture(errors)
    validate_accreditation_contract(errors)

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    course_spec = (ROOT / "docs/00-course-spec.md").read_text(encoding="utf-8")
    for required_text in ("SDA-AIE-211", "Specialist", "SDA-AIE-112"):
        if required_text not in readme or required_text not in course_spec:
            fail(errors, f"Official identity text missing from README/course spec: {required_text}")

    if errors:
        print("COURSE_RELEASE_GATE=FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("COURSE_RELEASE_GATE=PASS", json.dumps({
        "public_files": len(files), "markdown_files": markdown_count,
        "links_checked": link_count, "notebooks": notebook_count,
        "executed_code_cells": code_cells, "code_cells_with_outputs": output_cells,
        "student_starter_files": starter_files,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
