import pytest

from bayan.splits import validate_predefined_splits


ROWS = [
    {"group_id": "a", "split": "train", "topic": "x"},
    {"group_id": "b", "split": "train", "topic": "y"},
    {"group_id": "c", "split": "validation", "topic": "x"},
    {"group_id": "d", "split": "validation", "topic": "y"},
    {"group_id": "e", "split": "test", "topic": "x"},
    {"group_id": "f", "split": "test", "topic": "y"},
]


def test_valid_split_has_no_group_overlap():
    report = validate_predefined_splits(ROWS)
    assert report["group_overlap"] == 0
    assert report["rows_per_split"] == {"train": 2, "validation": 2, "test": 2}


def test_group_leakage_is_rejected():
    broken = ROWS + [{"group_id": "a", "split": "test", "topic": "x"}]
    with pytest.raises(ValueError, match="group leakage"):
        validate_predefined_splits(broken)


def test_missing_label_coverage_is_rejected():
    broken = [row for row in ROWS if not (row["split"] == "test" and row["topic"] == "y")]
    with pytest.raises(ValueError, match="missing labels"):
        validate_predefined_splits(broken)
