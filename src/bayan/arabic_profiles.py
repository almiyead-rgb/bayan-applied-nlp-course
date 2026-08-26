"""Explicit Arabic normalisation profiles for Bayan.

The raw display text remains authoritative.  A separate model/search copy is
normalised with a named profile and a pinned backend so training, indexing,
evaluation, and serving cannot silently disagree.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable
import unicodedata

from .preprocessing import mask_pii, normalize_arabic, normalize_whitespace

ARABIC_PROFILE_VERSION = "1.0.0"
SUPPORTED_PROFILES = ("conservative", "search")


@dataclass(frozen=True)
class ArabicTextRecord:
    """Raw display text plus the derived model copy and its contract."""

    display_text: str
    model_text: str
    profile: str
    backend: str
    version: str = ARABIC_PROFILE_VERSION


def _camel_tools_steps() -> dict[str, Callable[[str], str]]:
    """Load CAMeL Tools utilities only when the pinned backend is requested."""

    try:
        from camel_tools.utils.dediac import dediac_ar
        from camel_tools.utils.normalize import (
            normalize_alef_ar,
            normalize_alef_maksura_ar,
            normalize_unicode,
        )
    except ImportError as exc:  # pragma: no cover - exercised in Colab
        raise RuntimeError(
            "CAMeL Tools is required for backend='camel'. "
            "Install the pinned Day 3 requirements first."
        ) from exc

    return {
        "unicode": lambda text: normalize_unicode(text, compatibility=False),
        "dediac": dediac_ar,
        "alef": normalize_alef_ar,
        "alef_maksura": normalize_alef_maksura_ar,
    }


def _stdlib_normalize(text: str, profile: str) -> str:
    """Dependency-light mirror used by automated correctness tests."""

    if profile == "conservative":
        return normalize_arabic(text)
    return normalize_arabic(
        text,
        remove_diacritics=True,
        normalize_alef=True,
        normalize_ya=True,
    )


def normalize_arabic_profile(
    text: str,
    *,
    profile: str = "search",
    backend: str = "camel",
) -> ArabicTextRecord:
    """Create a protected model/search copy while preserving the display copy.

    ``conservative`` performs Unicode normalisation, tatweel removal, PII
    masking, and whitespace cleanup. ``search`` additionally removes Arabic
    diacritics and folds Alef variants and Alef Maksura. Teh Marbuta is
    deliberately preserved because that extra fold can merge distinctions.

    The stdlib backend exists for dependency-light CI and must be recorded if
    selected. Course notebooks require ``backend='camel'`` for Gate C.
    """

    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")
    if profile not in SUPPORTED_PROFILES:
        raise ValueError(f"profile must be one of {SUPPORTED_PROFILES}")
    if backend not in {"camel", "stdlib"}:
        raise ValueError("backend must be 'camel' or 'stdlib'")

    display_text = text
    protected = mask_pii(text)

    if backend == "stdlib":
        model_text = _stdlib_normalize(protected, profile)
    else:
        steps = _camel_tools_steps()
        model_text = steps["unicode"](protected).replace("ـ", "")
        if profile == "search":
            model_text = steps["dediac"](model_text)
            model_text = steps["alef"](model_text)
            model_text = steps["alef_maksura"](model_text)
        model_text = normalize_whitespace(model_text)

    return ArabicTextRecord(
        display_text=display_text,
        model_text=model_text,
        profile=profile,
        backend=backend,
    )


def arabizi_candidate(text: str) -> bool:
    """Return a transparent heuristic flag, not a dialect classification."""

    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")
    latin = sum(character.isascii() and character.isalpha() for character in text)
    arabizi_digits = sum(character in "2356789" for character in text)
    arabic = sum("\u0600" <= character <= "\u06ff" for character in text)
    return latin >= 3 and arabizi_digits >= 1 and arabic == 0
