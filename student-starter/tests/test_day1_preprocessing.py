from bayan.preprocessing import build_text_record, mask_pii, normalize_arabic, normalize_whitespace


def test_whitespace_and_tatweel_defaults():
    assert normalize_whitespace("  خدمة\n\t ممتازة  ") == "خدمة ممتازة"
    assert normalize_arabic("  الخـدمةُ   ممتازة  ") == "الخدمةُ ممتازة"


def test_optional_arabic_profile_is_explicit():
    assert normalize_arabic("إدارة آمنة", normalize_alef=True) == "ادارة امنة"
    assert normalize_arabic("هدى", normalize_ya=True) == "هدي"
    assert normalize_arabic("مدرسة") == "مدرسة"


def test_course_pii_patterns():
    text = "راسل test@example.invalid أو اتصل 0500000000"
    assert mask_pii(text) == "راسل [EMAIL] أو اتصل [PHONE]"


def test_display_copy_is_untouched():
    raw = "  الخـدمة test@example.invalid  "
    record = build_text_record(raw, language="ar")
    assert record.display_text == raw
    assert record.model_text == "الخدمة [EMAIL]"
