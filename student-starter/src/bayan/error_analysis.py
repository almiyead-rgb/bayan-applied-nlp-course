"""Human error-analysis and behavioural-test bookkeeping."""
from __future__ import annotations

from collections import Counter
from collections.abc import Mapping, Sequence
from typing import Any

DEFAULT_TAXONOMY = {
    "label_noise",
    "class_confusion",
    "dialect_gap",
    "negation",
    "truncation",
    "preprocessing",
    "entity_boundary",
    "hard_or_ambiguous",
}


def summarise_taxonomy(
    tagged_errors: Sequence[Mapping[str, Any]],
    *,
    allowed_tags: set[str] | None = None,
) -> list[dict[str, int | str]]:
    """Validate hand-written tags and count them from most frequent to least."""

    if not tagged_errors:
        raise ValueError("tagged_errors must not be empty")
    allowed = allowed_tags or DEFAULT_TAXONOMY
    counts: Counter[str] = Counter()
    seen_ids: set[str] = set()
    for row in tagged_errors:
        identifier = str(row.get("example_id", "")).strip()
        tag = str(row.get("taxonomy_tag", "")).strip()
        if not identifier or identifier in seen_ids:
            raise ValueError("each tagged error needs a unique example_id")
        if tag not in allowed:
            raise ValueError(f"unknown or blank taxonomy tag: {tag!r}")
        seen_ids.add(identifier)
        counts[tag] += 1
    return [
        {"taxonomy_tag": tag, "count": count}
        for tag, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    ]


def behavioural_pass_rate(
    rows: Sequence[Mapping[str, Any]],
    *,
    passed_key: str = "passed",
) -> dict[str, float | int]:
    """Return a transparent pass rate for generated behavioural cases."""

    if not rows:
        raise ValueError("behavioural rows must not be empty")
    passed = sum(bool(row[passed_key]) for row in rows)
    return {
        "passed": passed,
        "total": len(rows),
        "pass_rate": passed / len(rows),
    }
