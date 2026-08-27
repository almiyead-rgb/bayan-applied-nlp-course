import pytest

from bayan.metrics import classification_report, macro_f1


def test_perfect_macro_f1():
    assert macro_f1(["a", "b", "a"], ["a", "b", "a"]) == 1.0


def test_macro_f1_does_not_hide_minority_failure():
    report = classification_report(
        ["major", "major", "major", "minor"],
        ["major", "major", "major", "major"],
        labels=["major", "minor"],
    )
    assert report["accuracy"] == 0.75
    assert report["per_label"]["minor"]["f1"] == 0.0
    assert report["macro_f1"] < report["accuracy"]


def test_metric_length_mismatch_is_rejected():
    with pytest.raises(ValueError, match="same length"):
        macro_f1(["a"], ["a", "b"])
