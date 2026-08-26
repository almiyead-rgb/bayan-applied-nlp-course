"""Small dependency-light metrics used by the Bayan smoke path."""
from __future__ import annotations

from collections.abc import Hashable, Sequence
from typing import Any


def classification_report(
    y_true: Sequence[Hashable],
    y_pred: Sequence[Hashable],
    labels: Sequence[Hashable] | None = None,
) -> dict[str, Any]:
    """Return per-label precision/recall/F1 and macro-F1."""
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")
    if len(y_true) == 0:
        raise ValueError("labels must not be empty")

    if labels is None:
        labels = sorted(set(y_true) | set(y_pred), key=str)
    else:
        labels = list(labels)
    if not labels:
        raise ValueError("labels must not be empty")

    per_label: dict[str, dict[str, float | int]] = {}
    f1_values: list[float] = []
    for label in labels:
        tp = sum(t == label and p == label for t, p in zip(y_true, y_pred))
        fp = sum(t != label and p == label for t, p in zip(y_true, y_pred))
        fn = sum(t == label and p != label for t, p in zip(y_true, y_pred))
        support = sum(t == label for t in y_true)

        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0
        f1 = (
            2 * precision * recall / (precision + recall)
            if precision + recall
            else 0.0
        )
        per_label[str(label)] = {
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "support": support,
        }
        f1_values.append(f1)

    return {
        "per_label": per_label,
        "macro_f1": sum(f1_values) / len(f1_values),
        "accuracy": sum(t == p for t, p in zip(y_true, y_pred)) / len(y_true),
    }


def macro_f1(
    y_true: Sequence[Hashable],
    y_pred: Sequence[Hashable],
    labels: Sequence[Hashable] | None = None,
) -> float:
    """Return unweighted mean F1 across labels."""
    return float(classification_report(y_true, y_pred, labels)["macro_f1"])
