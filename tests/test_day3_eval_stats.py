import pytest
import numpy as np

from bayan.eval_stats import (
    bootstrap_ci,
    paired_bootstrap_difference,
    sliced_metric_report,
)
from bayan.metrics import macro_f1


def test_bootstrap_interval_contains_perfect_score():
    report = bootstrap_ci(
        ["a", "b", "a", "b"],
        ["a", "b", "a", "b"],
        macro_f1,
        n_boot=50,
        seed=7,
    )
    assert report["estimate"] == 1.0
    assert report["ci_low"] == 1.0
    assert report["ci_high"] == 1.0


def test_paired_bootstrap_detects_clear_directional_gain():
    truth = ["a", "b"] * 20
    first = ["a"] * 40
    second = truth.copy()
    report = paired_bootstrap_difference(
        truth, first, second, macro_f1, n_boot=200, seed=9
    )
    assert report["difference_b_minus_a"] > 0
    assert report["ci_low"] > 0
    assert report["supports_directional_claim"] is True


def test_small_noisy_difference_does_not_force_a_claim():
    truth = ["a", "b"] * 10
    first = truth.copy()
    second = truth.copy()
    first[0] = "b"
    second[1] = "a"
    report = paired_bootstrap_difference(
        truth, first, second, macro_f1, n_boot=300, seed=4
    )
    assert report["ci_low"] <= 0 <= report["ci_high"]
    assert report["supports_directional_claim"] is False


def test_sliced_report_flags_small_slices_instead_of_hiding_them():
    rows = [
        {"language": "ar", "truth": "x", "prediction": "x"},
        {"language": "ar", "truth": "y", "prediction": "x"},
        {"language": "en", "truth": "x", "prediction": "x"},
    ]
    report = sliced_metric_report(
        rows,
        true_key="truth",
        pred_key="prediction",
        slice_keys=["language"],
        metric_fn=macro_f1,
        min_slice_size=3,
        n_boot=30,
    )
    english = next(row for row in report if row["slice"] == "language=en")
    assert english["n"] == 1
    assert english["flag"] == "SMALL_SLICE"


def test_bootstrap_rejects_mismatched_or_empty_inputs():
    with pytest.raises(ValueError, match="same non-zero length"):
        bootstrap_ci(["a"], [], macro_f1)


def test_bootstrap_accepts_numpy_arrays_without_truth_value_ambiguity():
    report = bootstrap_ci(
        np.array(["a", "b"]),
        np.array(["a", "b"]),
        macro_f1,
        n_boot=20,
        seed=3,
    )
    assert report["estimate"] == 1.0
