import pytest

from bayan.qa_postprocess import best_span


def test_best_span_returns_context_substring():
    context = "الخدمة متاحة في الرياض"
    offsets = [None, (0, 6), (7, 12), (13, 15), (16, 22)]
    result = best_span(
        [0.0, 0.1, 0.1, 0.2, 4.0],
        [0.0, 0.1, 0.1, 0.2, 4.5],
        offsets,
        context,
    )
    assert result["answer"] == "الرياض"
    assert result["start"] == 16


def test_null_score_can_reject_a_plausible_span():
    context = "الخدمة متاحة"
    offsets = [None, (0, 6), (7, 12)]
    result = best_span(
        [5.0, 1.0, 2.0],
        [5.0, 1.0, 2.0],
        offsets,
        context,
        null_threshold=0.0,
    )
    assert result["answer"] is None
    assert result["reason"] == "no_answer_in_context"


def test_invalid_shapes_are_rejected():
    with pytest.raises(ValueError, match="same non-zero length"):
        best_span([1.0], [1.0, 2.0], [None], "x")
