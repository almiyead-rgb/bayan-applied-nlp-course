#!/usr/bin/env python3
"""Command-line entry point for the Bayan final-submission validator."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from bayan.submission import format_result, validate_project  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Bayan learner repository")
    parser.add_argument("project", nargs="?", default=".", help="repository root")
    parser.add_argument(
        "--require-tag",
        action="store_true",
        help="also require the local Git tag submission-v1.0",
    )
    parser.add_argument("--json-report", help="optional JSON report path")
    args = parser.parse_args()

    result = validate_project(args.project, require_git_tag=args.require_tag)
    print(format_result(result))
    if args.json_report:
        report_path = Path(args.json_report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            json.dumps(result.to_dict(), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return 0 if result.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
