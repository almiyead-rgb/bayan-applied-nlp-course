import pytest

from bayan.error_analysis import behavioural_pass_rate, summarise_taxonomy


def test_taxonomy_counts_sorted_and_validated():
    report = summarise_taxonomy(
        [
            {"example_id": "e1", "taxonomy_tag": "dialect_gap"},
            {"example_id": "e2", "taxonomy_tag": "class_confusion"},
            {"example_id": "e3", "taxonomy_tag": "dialect_gap"},
        ]
    )
    assert report[0] == {"taxonomy_tag": "dialect_gap", "count": 2}


def test_blank_or_unknown_tags_do_not_pass_as_analysis():
    with pytest.raises(ValueError, match="unknown or blank"):
        summarise_taxonomy([{"example_id": "e1", "taxonomy_tag": ""}])


def test_behavioural_pass_rate_is_not_a_model_accuracy_alias():
    report = behavioural_pass_rate(
        [{"passed": True}, {"passed": False}, {"passed": True}]
    )
    assert report == {"passed": 2, "total": 3, "pass_rate": 2 / 3}
