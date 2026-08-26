"""Leakage checks for predefined train/validation/test splits."""
from __future__ import annotations

from collections import Counter, defaultdict
from collections.abc import Iterable, Mapping
from typing import Any


def validate_predefined_splits(
    rows: Iterable[Mapping[str, Any]],
    *,
    group_key: str = "group_id",
    split_key: str = "split",
    label_key: str = "topic",
    required_splits: tuple[str, ...] = ("train", "validation", "test"),
    require_all_labels: bool = True,
) -> dict[str, Any]:
    """Validate split names, group isolation, and optional label coverage."""
    rows = list(rows)
    if not rows:
        raise ValueError("rows must not be empty")

    required = set(required_splits)
    counts: Counter[str] = Counter()
    group_owner: dict[str, str] = {}
    labels_by_split: dict[str, set[str]] = defaultdict(set)

    for index, row in enumerate(rows):
        missing = [key for key in (group_key, split_key, label_key) if key not in row]
        if missing:
            raise ValueError(f"row {index} is missing keys: {missing}")

        split = str(row[split_key])
        group = str(row[group_key])
        label = str(row[label_key])
        if split not in required:
            raise ValueError(f"unknown split: {split}")
        if not group or not label:
            raise ValueError("group and label values must be non-empty")

        previous = group_owner.setdefault(group, split)
        if previous != split:
            raise ValueError(
                f"group leakage: {group!r} appears in {previous!r} and {split!r}"
            )

        counts[split] += 1
        labels_by_split[split].add(label)

    empty_splits = sorted(split for split in required if counts[split] == 0)
    if empty_splits:
        raise ValueError(f"empty required splits: {empty_splits}")

    all_labels = set().union(*labels_by_split.values())
    if require_all_labels:
        for split in required:
            missing_labels = sorted(all_labels - labels_by_split[split])
            if missing_labels:
                raise ValueError(
                    f"split {split!r} is missing labels: {missing_labels}"
                )

    return {
        "rows_per_split": {split: counts[split] for split in required_splits},
        "groups": len(group_owner),
        "labels": sorted(all_labels),
        "group_overlap": 0,
    }
