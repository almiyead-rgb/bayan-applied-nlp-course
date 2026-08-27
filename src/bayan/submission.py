"""Offline validator for the final public Bayan learner repository."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
import json
import re
import subprocess


REQUIRED_FILES = (
    "README.md",
    "STUDENT_PROFILE.md",
    "PROGRESS.md",
    "DECISIONS.md",
    "BENCHMARKS.md",
    "EVALUATION_REPORT.md",
    "MODEL_CARD.md",
    "DATA_CARD.md",
    "PROJECT_SUMMARY.json",
    "SUBMISSION.yml",
)
REQUIRED_DIRECTORIES = ("notebooks", "src/bayan", "tests", "reports", "sample_outputs")
REQUIRED_NOTEBOOKS = (
    "00_runtime_doctor.ipynb",
    "01_text_processing_tokenization.ipynb",
    "02_attention_transformers.ipynb",
    "03_text_classification.ipynb",
    "04_ner_and_qa.ipynb",
    "05_arabic_nlp.ipynb",
    "06_semantic_search.ipynb",
    "07_evaluation_error_analysis.ipynb",
    "08_optimization_serving.ipynb",
)
REQUIRED_MARKERS = {
    "01_text_processing_tokenization.ipynb": "DAY1_NOTEBOOK1_CORE=PASS",
    "02_attention_transformers.ipynb": "DAY1_NOTEBOOK2_CORE=PASS",
    "03_text_classification.ipynb": "DAY2_NOTEBOOK3_CORE=PASS",
    "04_ner_and_qa.ipynb": "DAY2_NOTEBOOK4_CORE=PASS",
    "05_arabic_nlp.ipynb": "DAY3_NOTEBOOK5_CORE=PASS",
    "06_semantic_search.ipynb": "DAY3_NOTEBOOK6_CORE=PASS",
    "07_evaluation_error_analysis.ipynb": "DAY3_NOTEBOOK7_CORE=PASS",
    "08_optimization_serving.ipynb": "DAY4_NOTEBOOK8_CORE=PASS",
}
FORBIDDEN_SUFFIXES = {
    ".pt",
    ".pth",
    ".ckpt",
    ".safetensors",
    ".onnx",
    ".bin",
    ".pem",
    ".key",
}
FORBIDDEN_NAMES = {".env", "credentials.json", "service-account.json"}
FORBIDDEN_DIRECTORY_NAMES = {"secrets", "credentials"}
PLACEHOLDER_PATTERNS = (
    re.compile(r"YOUR_USERNAME", re.IGNORECASE),
    re.compile(r"\bFILL_ME\b", re.IGNORECASE),
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"REPLACE[_ -]?ME", re.IGNORECASE),
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"\[FILL[^]]*\]", re.IGNORECASE),
)


@dataclass
class ValidationResult:
    checks: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.errors

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": "PASS" if self.passed else "FAIL",
            "checks": self.checks,
            "warnings": self.warnings,
            "errors": self.errors,
        }


def parse_flat_yaml(text: str) -> dict[str, str]:
    """Parse the flat key/value subset required by ``SUBMISSION.yml``."""

    result: dict[str, str] = {}
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "\t" in raw_line or ":" not in line:
            raise ValueError(f"invalid flat YAML on line {line_number}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"\'')
        if not key or not value:
            raise ValueError(f"empty YAML key/value on line {line_number}")
        if key in result:
            raise ValueError(f"duplicate YAML key {key!r}")
        result[key] = value
    return result


def _contains_placeholder(text: str) -> bool:
    return any(pattern.search(text) for pattern in PLACEHOLDER_PATTERNS)


def _validate_structure(root: Path, result: ValidationResult) -> None:
    missing_files = [name for name in REQUIRED_FILES if not (root / name).is_file()]
    missing_directories = [name for name in REQUIRED_DIRECTORIES if not (root / name).is_dir()]
    if missing_files:
        result.errors.append(f"Missing required files: {missing_files}")
    if missing_directories:
        result.errors.append(f"Missing required directories: {missing_directories}")
    if not missing_files and not missing_directories:
        result.checks.append("Required project structure")


def _validate_notebooks(root: Path, result: ValidationResult) -> None:
    notebook_root = root / "notebooks"
    missing = [name for name in REQUIRED_NOTEBOOKS if not (notebook_root / name).is_file()]
    if missing:
        result.errors.append(f"Missing required notebooks: {missing}")
        return
    for name in REQUIRED_NOTEBOOKS:
        path = notebook_root / name
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            result.errors.append(f"Invalid notebook {name}: {exc}")
            continue
        if not isinstance(notebook.get("cells"), list):
            result.errors.append(f"Invalid notebook structure: {name}")
        marker = REQUIRED_MARKERS.get(name)
        if marker and marker not in path.read_text(encoding="utf-8"):
            result.errors.append(f"Missing Core marker in {name}: {marker}")
    if not any("notebook" in error.lower() or "core marker" in error.lower() for error in result.errors):
        result.checks.append("Nine valid notebooks and Core markers")


def _validate_summary(root: Path, result: ValidationResult) -> None:
    path = root / "PROJECT_SUMMARY.json"
    if not path.is_file():
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        result.errors.append(f"PROJECT_SUMMARY.json is invalid JSON: {exc}")
        return
    if not isinstance(data, dict):
        result.errors.append("PROJECT_SUMMARY.json must contain one JSON object")
        return
    required = {
        "student_github",
        "repository_url",
        "languages",
        "tasks",
        "extension",
        "final_tag",
        "privacy_check",
        "tests_passed",
        "benchmark_mode",
    }
    missing = sorted(required - set(data))
    if missing:
        result.errors.append(f"PROJECT_SUMMARY.json missing keys: {missing}")
        return
    if _contains_placeholder(json.dumps(data, ensure_ascii=False)):
        result.errors.append("PROJECT_SUMMARY.json still contains placeholders")
    languages = data.get("languages")
    if not isinstance(languages, list) or not {"ar", "en"}.issubset(set(languages)):
        result.errors.append("PROJECT_SUMMARY.json must include ar and en")
    required_tasks = {"classification", "sentiment", "ner", "qa", "semantic_search"}
    tasks = data.get("tasks")
    if not isinstance(tasks, list) or not required_tasks.issubset(set(tasks)):
        result.errors.append("PROJECT_SUMMARY.json is missing required NLP tasks")
    extension = data.get("extension")
    if (
        not isinstance(extension, dict)
        or not isinstance(extension.get("name"), str)
        or not extension.get("name", "").strip()
        or not isinstance(extension.get("evidence"), str)
        or not extension.get("evidence", "").strip()
    ):
        result.errors.append("PROJECT_SUMMARY.json must name one measured extension and its evidence")
    if data.get("final_tag") != "submission-v1.0":
        result.errors.append("final_tag must be submission-v1.0")
    if data.get("privacy_check") is not True or data.get("tests_passed") is not True:
        result.errors.append("privacy_check and tests_passed must be JSON true after verification")
    if data.get("benchmark_mode") != "PROJECT_ARTIFACT":
        result.errors.append("benchmark_mode must be PROJECT_ARTIFACT for final submission")
    if not re.fullmatch(r"https://github\.com/[^/]+/[^/]+/?", str(data.get("repository_url"))):
        result.errors.append("repository_url must be a public GitHub repository URL")
    if not any(error.startswith("PROJECT_SUMMARY") or error.startswith("final_tag") or error.startswith("privacy_check") or error.startswith("benchmark_mode") or error.startswith("repository_url") for error in result.errors):
        result.checks.append("PROJECT_SUMMARY.json contract")


def _validate_submission_yaml(root: Path, result: ValidationResult) -> None:
    path = root / "SUBMISSION.yml"
    if not path.is_file():
        return
    try:
        data = parse_flat_yaml(path.read_text(encoding="utf-8"))
    except ValueError as exc:
        result.errors.append(f"SUBMISSION.yml is invalid: {exc}")
        return
    expected = {
        "course": "bayan-applied-nlp",
        "default_branch": "main",
        "final_tag": "submission-v1.0",
        "runtime": "google-colab",
        "visibility": "public",
    }
    for key, value in expected.items():
        if data.get(key) != value:
            result.errors.append(f"SUBMISSION.yml: {key} must be {value}")
    for key in ("student_github", "repository"):
        if key not in data:
            result.errors.append(f"SUBMISSION.yml missing {key}")
    if "repository" in data and not re.fullmatch(
        r"https://github\.com/[^/]+/[^/]+/?", data["repository"]
    ):
        result.errors.append("SUBMISSION.yml: repository must be a public GitHub URL")
    if _contains_placeholder(path.read_text(encoding="utf-8")):
        result.errors.append("SUBMISSION.yml still contains placeholders")
    if not any(error.startswith("SUBMISSION.yml") for error in result.errors):
        result.checks.append("SUBMISSION.yml contract")


def _validate_public_files(root: Path, result: ValidationResult) -> None:
    forbidden = []
    too_large = []
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        relative = path.relative_to(root).as_posix()
        if (
            path.suffix.lower() in FORBIDDEN_SUFFIXES
            or path.name.lower() in FORBIDDEN_NAMES
            or any(part.lower() in FORBIDDEN_DIRECTORY_NAMES for part in path.parts)
        ):
            forbidden.append(relative)
        if path.stat().st_size > 10 * 1024 * 1024:
            too_large.append(relative)
    if forbidden:
        result.errors.append(f"Forbidden model/secret artefacts: {forbidden}")
    if too_large:
        result.errors.append(f"Files above the 10 MiB course limit: {too_large}")
    for name in REQUIRED_FILES:
        path = root / name
        if path.is_file() and path.stat().st_size == 0:
            result.errors.append(f"Required file is empty: {name}")
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".yml"}:
            if _contains_placeholder(path.read_text(encoding="utf-8")):
                result.errors.append(f"Required file still contains a placeholder: {name}")
    if not forbidden and not too_large:
        result.checks.append("No forbidden or oversized tracked artefacts")


def _validate_tag(root: Path, result: ValidationResult) -> None:
    try:
        completed = subprocess.run(
            ["git", "-C", str(root), "tag", "--list", "submission-v1.0"],
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        result.errors.append(f"Could not inspect Git tag: {exc}")
        return
    if completed.stdout.strip() != "submission-v1.0":
        result.errors.append("Git tag submission-v1.0 is missing")
    else:
        result.checks.append("Final Git tag submission-v1.0")


def validate_project(root: str | Path, *, require_git_tag: bool = False) -> ValidationResult:
    """Validate a Bayan repository locally without network access."""

    project_root = Path(root).resolve()
    result = ValidationResult()
    if not project_root.is_dir():
        result.errors.append(f"Project root does not exist: {project_root}")
        return result
    _validate_structure(project_root, result)
    _validate_notebooks(project_root, result)
    _validate_summary(project_root, result)
    _validate_submission_yaml(project_root, result)
    _validate_public_files(project_root, result)
    if require_git_tag:
        _validate_tag(project_root, result)
    else:
        result.warnings.append(
            "Run again with --require-tag after creating submission-v1.0."
        )
    result.warnings.append(
        "Open the repository and Colab links in a private browser window; visibility is not verifiable offline."
    )
    return result


def format_result(result: ValidationResult) -> str:
    lines = [f"BAYAN_SUBMISSION_VALIDATOR={'PASS' if result.passed else 'FAIL'}"]
    lines.extend(f"[PASS] {item}" for item in result.checks)
    lines.extend(f"[WARN] {item}" for item in result.warnings)
    lines.extend(f"[ERROR] {item}" for item in result.errors)
    return "\n".join(lines)
