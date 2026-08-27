import pytest

from bayan.arabic_profiles import arabizi_candidate, normalize_arabic_profile


def test_search_profile_preserves_display_and_normalises_model_copy():
    raw = "  إِدَارَةُ الهُدَى test@example.invalid  "
    record = normalize_arabic_profile(raw, profile="search", backend="stdlib")

    assert record.display_text == raw
    assert record.model_text == "ادارة الهدي [EMAIL]"
    assert record.profile == "search"
    assert record.backend == "stdlib"


def test_conservative_profile_keeps_diacritics_and_letter_variants():
    record = normalize_arabic_profile(
        "إِدَارَةُ الهُدَى", profile="conservative", backend="stdlib"
    )
    assert record.model_text == "إِدَارَةُ الهُدَى"


def test_unknown_profile_or_backend_is_rejected():
    with pytest.raises(ValueError, match="profile"):
        normalize_arabic_profile("نص", profile="universal", backend="stdlib")
    with pytest.raises(ValueError, match="backend"):
        normalize_arabic_profile("نص", profile="search", backend="auto")


def test_arabizi_flag_is_explicitly_a_heuristic():
    assert arabizi_candidate("mashkor 3la alkhidma") is True
    assert arabizi_candidate("الخدمة ممتازة") is False
    assert arabizi_candidate("service is good") is False
