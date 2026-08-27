import json
import subprocess
from pathlib import Path

import pytest

from bayan.submission import (
    REQUIRED_DIRECTORIES,
    REQUIRED_FILES,
    REQUIRED_MARKERS,
    REQUIRED_NOTEBOOKS,
    format_result,
    parse_flat_yaml,
    validate_project,
)


def build_valid_project(root: Path) -> None:
    for directory in REQUIRED_DIRECTORIES:
        (root / directory).mkdir(parents=True, exist_ok=True)
    for name in REQUIRED_FILES:
        (root / name).write_text("Completed evidence\n", encoding="utf-8")
    summary = {
        "student_github": "student-one",
        "repository_url": "https://github.com/student-one/bayan-nlp-student-one",
        "languages": ["ar", "en"],
        "tasks": ["classification", "sentiment", "ner", "qa", "semantic_search"],
        "extension": {
            "name": "batch endpoint",
            "evidence": "BENCHMARKS.md#batch-endpoint",
        },
        "final_tag": "submission-v1.0",
        "privacy_check": True,
        "tests_passed": True,
        "benchmark_mode": "PROJECT_ARTIFACT",
    }
    (root / "PROJECT_SUMMARY.json").write_text(
        json.dumps(summary), encoding="utf-8"
    )
    (root / "SUBMISSION.yml").write_text(
        "\n".join(
            [
                "course: bayan-applied-nlp",
                "student_github: student-one",
                "repository: https://github.com/student-one/bayan-nlp-student-one",
                "default_branch: main",
                "final_tag: submission-v1.0",
                "runtime: google-colab",
                "visibility: public",
            ]
        ),
        encoding="utf-8",
    )
    for name in REQUIRED_NOTEBOOKS:
        marker = REQUIRED_MARKERS.get(name, "")
        notebook = {
            "cells": [{"cell_type": "markdown", "metadata": {}, "source": [marker]}],
            "metadata": {},
            "nbformat": 4,
            "nbformat_minor": 5,
        }
        (root / "notebooks" / name).write_text(json.dumps(notebook), encoding="utf-8")


def test_flat_yaml_parser_accepts_course_contract():
    parsed = parse_flat_yaml("course: bayan-applied-nlp\nvisibility: public\n")
    assert parsed == {"course": "bayan-applied-nlp", "visibility": "public"}


def test_flat_yaml_parser_rejects_tabs_duplicates_and_nesting():
    with pytest.raises(ValueError):
        parse_flat_yaml("\tcourse: x")
    with pytest.raises(ValueError):
        parse_flat_yaml("course: x\ncourse: y")
    with pytest.raises(ValueError):
        parse_flat_yaml("not-a-pair")
    with pytest.raises(ValueError):
        parse_flat_yaml("course:\tbayan")


def test_valid_project_passes_with_manual_online_warnings(tmp_path: Path):
    build_valid_project(tmp_path)
    result = validate_project(tmp_path)
    assert result.passed is True
    assert len(result.warnings) == 2
    assert "BAYAN_SUBMISSION_VALIDATOR=PASS" in format_result(result)


def test_missing_file_marker_and_placeholder_fail(tmp_path: Path):
    build_valid_project(tmp_path)
    (tmp_path / "BENCHMARKS.md").unlink()
    notebook_path = tmp_path / "notebooks" / "08_optimization_serving.ipynb"
    notebook_path.write_text(
        json.dumps({"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}),
        encoding="utf-8",
    )
    (tmp_path / "SUBMISSION.yml").write_text(
        "course: bayan-applied-nlp\nstudent_github: YOUR_USERNAME\n",
        encoding="utf-8",
    )
    result = validate_project(tmp_path)
    assert result.passed is False
    assert any("BENCHMARKS.md" in error for error in result.errors)
    assert any("DAY4_NOTEBOOK8_CORE=PASS" in error for error in result.errors)
    assert any("placeholder" in error.lower() for error in result.errors)


def test_systems_smoke_cannot_claim_final_project_benchmark(tmp_path: Path):
    build_valid_project(tmp_path)
    summary_path = tmp_path / "PROJECT_SUMMARY.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    summary["benchmark_mode"] = "SYSTEMS_SMOKE"
    summary_path.write_text(json.dumps(summary), encoding="utf-8")
    result = validate_project(tmp_path)
    assert any("PROJECT_ARTIFACT" in error for error in result.errors)


def test_missing_measured_extension_fails(tmp_path: Path):
    build_valid_project(tmp_path)
    summary_path = tmp_path / "PROJECT_SUMMARY.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    summary["extension"] = {"name": "", "evidence": ""}
    summary_path.write_text(json.dumps(summary), encoding="utf-8")
    result = validate_project(tmp_path)
    assert any("measured extension" in error for error in result.errors)


def test_sentiment_task_is_required(tmp_path: Path):
    build_valid_project(tmp_path)
    summary_path = tmp_path / "PROJECT_SUMMARY.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    summary["tasks"].remove("sentiment")
    summary_path.write_text(json.dumps(summary), encoding="utf-8")
    result = validate_project(tmp_path)
    assert any("required NLP tasks" in error for error in result.errors)


@pytest.mark.parametrize("placeholder", ["FILL_ME", "TODO", "REPLACE_ME", "TBD"])
def test_required_files_reject_plain_placeholders(tmp_path: Path, placeholder: str):
    build_valid_project(tmp_path)
    (tmp_path / "BENCHMARKS.md").write_text(
        f"Evidence still pending: {placeholder}\n", encoding="utf-8"
    )
    result = validate_project(tmp_path)
    assert any("BENCHMARKS.md" in error and "placeholder" in error for error in result.errors)


def test_forbidden_weights_and_oversized_files_fail(tmp_path: Path):
    build_valid_project(tmp_path)
    (tmp_path / "model.onnx").write_bytes(b"unsafe")
    result = validate_project(tmp_path)
    assert any("Forbidden" in error for error in result.errors)


def test_malformed_summary_types_fail_without_crashing(tmp_path: Path):
    build_valid_project(tmp_path)
    summary_path = tmp_path / "PROJECT_SUMMARY.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    summary["languages"] = None
    summary["tasks"] = "classification"
    summary_path.write_text(json.dumps(summary), encoding="utf-8")
    result = validate_project(tmp_path)
    assert result.passed is False
    assert any("include ar and en" in error for error in result.errors)
    assert any("required NLP tasks" in error for error in result.errors)


def test_final_mode_checks_local_git_tag(tmp_path: Path):
    build_valid_project(tmp_path)
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    subprocess.run(["git", "-C", str(tmp_path), "add", "."], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(tmp_path),
            "-c",
            "user.name=Bayan Test",
            "-c",
            "user.email=bayan-test@example.invalid",
            "commit",
            "-qm",
            "test fixture",
        ],
        check=True,
    )
    missing = validate_project(tmp_path, require_git_tag=True)
    assert any("tag submission-v1.0 is missing" in error for error in missing.errors)
    subprocess.run(["git", "-C", str(tmp_path), "tag", "submission-v1.0"], check=True)
    present = validate_project(tmp_path, require_git_tag=True)
    assert present.passed is True
