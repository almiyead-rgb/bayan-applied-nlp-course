"""Tokenisation measurements used in Day 1."""
from __future__ import annotations

from collections.abc import Callable, Iterable
from statistics import mean
import re

_NONSPACE_RE = re.compile(r"\S+")


def whitespace_tokens(text: str) -> list[str]:
    if not isinstance(text, str):
        raise TypeError("text must be str")
    return _NONSPACE_RE.findall(text)


def token_fertility(text: str, tokenize: Callable[[str], list[str]]) -> float:
    """Return model tokens divided by whitespace words for one text."""

    words = whitespace_tokens(text)
    if not words:
        return 0.0
    tokens = list(tokenize(text))
    return len(tokens) / len(words)


def corpus_fertility(
    texts: Iterable[str], tokenize: Callable[[str], list[str]]
) -> float:
    values = [token_fertility(text, tokenize) for text in texts if text.strip()]
    return mean(values) if values else 0.0


def truncation_rate(
    texts: Iterable[str],
    tokenize: Callable[[str], list[str]],
    *,
    max_length: int,
    special_tokens: int = 2,
) -> float:
    """Fraction of texts that exceed the usable token budget."""

    if max_length <= special_tokens:
        raise ValueError("max_length must be greater than special_tokens")
    texts = list(texts)
    if not texts:
        return 0.0
    usable = max_length - special_tokens
    truncated = sum(len(tokenize(text)) > usable for text in texts)
    return truncated / len(texts)
