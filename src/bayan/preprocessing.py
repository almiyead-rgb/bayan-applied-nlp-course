"""Safe, course-sized preprocessing utilities for Bayan.

The functions preserve an untouched display copy and create a separate model copy.
They are educational defaults, not a production PII detection service.
"""
from __future__ import annotations

from dataclasses import dataclass
import re
import unicodedata

_EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
_SAUDI_MOBILE_RE = re.compile(r"(?<!\d)(?:\+?966[\s-]?|0)?5(?:[\s-]?\d){8}(?!\d)")
_WHITESPACE_RE = re.compile(r"\s+")
_ARABIC_DIACRITICS_RE = re.compile(
    "[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]"
)
_ALEF_VARIANTS_RE = re.compile("[إأآٱ]")


@dataclass(frozen=True)
class TextRecord:
    """Two-copy contract: original safe display text and model input text."""

    display_text: str
    model_text: str


def _require_text(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")
    return text


def normalize_whitespace(text: str) -> str:
    """Collapse Unicode whitespace and trim both ends."""

    return _WHITESPACE_RE.sub(" ", _require_text(text)).strip()


def mask_pii(text: str) -> str:
    """Mask course-supported email and Saudi mobile patterns.

    This is deliberately narrow and must not be presented as a complete
    production PII detector.
    """

    text = _require_text(text)
    text = _EMAIL_RE.sub("[EMAIL]", text)
    text = _SAUDI_MOBILE_RE.sub("[PHONE]", text)
    return text


def normalize_arabic(
    text: str,
    *,
    unicode_form: str = "NFC",
    remove_tatweel: bool = True,
    remove_diacritics: bool = False,
    normalize_alef: bool = False,
    normalize_ya: bool = False,
) -> str:
    """Apply an explicit Arabic normalisation profile.

    Conservative defaults preserve diacritics, alef variants, ya/alef maqsura,
    and ta marbuta. Enable a transformation only when the task and checkpoint
    justify it.
    """

    text = unicodedata.normalize(unicode_form, _require_text(text))
    if remove_tatweel:
        text = text.replace("ـ", "")
    if remove_diacritics:
        text = _ARABIC_DIACRITICS_RE.sub("", text)
    if normalize_alef:
        text = _ALEF_VARIANTS_RE.sub("ا", text)
    if normalize_ya:
        text = text.replace("ى", "ي")
    return normalize_whitespace(text)


def build_text_record(
    text: str,
    *,
    language: str,
    remove_diacritics: bool = False,
    normalize_alef: bool = False,
    normalize_ya: bool = False,
) -> TextRecord:
    """Create the display/model copies used by Bayan."""

    display_text = _require_text(text)
    masked = mask_pii(display_text)
    if language.lower() == "ar":
        model_text = normalize_arabic(
            masked,
            remove_diacritics=remove_diacritics,
            normalize_alef=normalize_alef,
            normalize_ya=normalize_ya,
        )
    elif language.lower() == "en":
        model_text = normalize_whitespace(
            unicodedata.normalize("NFC", masked)
        )
    else:
        raise ValueError("language must be 'ar' or 'en'")
    return TextRecord(display_text=display_text, model_text=model_text)
