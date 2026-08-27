"""Bootstrap uncertainty and sliced evaluation for small NLP experiments."""
from __future__ import annotations

from collections.abc import Callable, Hashable, Mapping, Sequence
from typing import Any

import numpy as np


MetricFunction = Callable[[Sequence[Hashable], Sequence[Hashable]], float]


def _validate_pairs(
    y_true: Sequence[Hashable], y_pred: Sequence[Hashable]
) -> tuple[np.ndarray, np.ndarray]:
    if len(y_true) != len(y_pred) or len(y_true) == 0:
        raise ValueError("y_true and y_pred must have the same non-zero length")
    return np.asarray(y_true, dtype=object), np.asarray(y_pred, dtype=object)


def bootstrap_ci(
    y_true: Sequence[Hashable],
    y_pred: Sequence[Hashable],
    metric_fn: MetricFunction,
    *,
    n_boot: int = 1000,
    alpha: float = 0.05,
    seed: int = 42,
) -> dict[str, float]:
    """Percentile bootstrap CI over paired examples."""

    truth, prediction = _validate_pairs(y_true, y_pred)
    if n_boot < 1 or not 0 < alpha < 1:
        raise ValueError("n_boot must be positive and alpha must be between 0 and 1")

    rng = np.random.default_rng(seed)
    stats = np.empty(n_boot, dtype=float)
    for iteration in range(n_boot):
        indexes = rng.integers(0, len(truth), len(truth))
        stats[iteration] = metric_fn(truth[indexes], prediction[indexes])
    low, high = np.percentile(stats, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    return {
        "estimate": float(metric_fn(truth, prediction)),
        "bootstrap_mean": float(np.mean(stats)),
        "ci_low": float(low),
        "ci_high": float(high),
    }


def paired_bootstrap_difference(
    y_true: Sequence[Hashable],
    prediction_a: Sequence[Hashable],
    prediction_b: Sequence[Hashable],
    metric_fn: MetricFunction,
    *,
    n_boot: int = 1000,
    alpha: float = 0.05,
    seed: int = 42,
) -> dict[str, float | bool]:
    """Bootstrap B-A on identical resamples; CI crossing zero means no claim."""

    truth, first = _validate_pairs(y_true, prediction_a)
    if len(prediction_b) != len(truth):
        raise ValueError("all prediction arrays must have the same length")
    second = np.asarray(prediction_b, dtype=object)
    if n_boot < 1 or not 0 < alpha < 1:
        raise ValueError("n_boot must be positive and alpha must be between 0 and 1")

    rng = np.random.default_rng(seed)
    differences = np.empty(n_boot, dtype=float)
    for iteration in range(n_boot):
        indexes = rng.integers(0, len(truth), len(truth))
        differences[iteration] = metric_fn(truth[indexes], second[indexes]) - metric_fn(
            truth[indexes], first[indexes]
        )
    low, high = np.percentile(
        differences, [100 * alpha / 2, 100 * (1 - alpha / 2)]
    )
    observed = metric_fn(truth, second) - metric_fn(truth, first)
    return {
        "difference_b_minus_a": float(observed),
        "ci_low": float(low),
        "ci_high": float(high),
        "supports_directional_claim": bool(low > 0 or high < 0),
    }


def sliced_metric_report(
    rows: Sequence[Mapping[str, Any]],
    *,
    true_key: str,
    pred_key: str,
    slice_keys: Sequence[str],
    metric_fn: MetricFunction,
    min_slice_size: int = 10,
    n_boot: int = 300,
    seed: int = 42,
) -> list[dict[str, Any]]:
    """Return aggregate and single-column slice metrics with CIs."""

    if not rows:
        raise ValueError("rows must not be empty")
    if min_slice_size < 1:
        raise ValueError("min_slice_size must be positive")

    groups: list[tuple[str, Sequence[Mapping[str, Any]]]] = [("ALL", rows)]
    for key in slice_keys:
        values = sorted({str(row[key]) for row in rows})
        groups.extend(
            (f"{key}={value}", [row for row in rows if str(row[key]) == value])
            for value in values
        )

    report = []
    for offset, (name, group) in enumerate(groups):
        interval = bootstrap_ci(
            [row[true_key] for row in group],
            [row[pred_key] for row in group],
            metric_fn,
            n_boot=n_boot,
            seed=seed + offset,
        )
        report.append(
            {
                "slice": name,
                "n": len(group),
                **interval,
                "flag": "SMALL_SLICE" if len(group) < min_slice_size else "",
            }
        )
    return report
