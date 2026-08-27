"""Constrained extractive-QA span selection with honest null handling."""
from __future__ import annotations

from collections.abc import Sequence
from math import inf


def best_span(
    start_logits: Sequence[float],
    end_logits: Sequence[float],
    offsets: Sequence[tuple[int, int] | None],
    context: str,
    *,
    null_threshold: float = 0.0,
    max_answer_length: int = 48,
    top_k: int = 20,
) -> dict[str, float | int | str | None]:
    """Return the best valid context span or an explicit no-answer result."""
    size = len(start_logits)
    if size == 0 or len(end_logits) != size or len(offsets) != size:
        raise ValueError("logits and offsets must have the same non-zero length")
    if max_answer_length < 1 or top_k < 1:
        raise ValueError("max_answer_length and top_k must be positive")

    null_score = float(start_logits[0]) + float(end_logits[0])
    start_indexes = sorted(range(size), key=lambda i: start_logits[i], reverse=True)[:top_k]
    end_indexes = sorted(range(size), key=lambda i: end_logits[i], reverse=True)[:top_k]

    best_score = -inf
    best_start = best_end = -1
    for start in start_indexes:
        for end in end_indexes:
            if start == 0 or end == 0 or end < start:
                continue
            if end - start + 1 > max_answer_length:
                continue
            start_offset, end_offset = offsets[start], offsets[end]
            if start_offset is None or end_offset is None:
                continue
            char_start, char_end = start_offset[0], end_offset[1]
            if char_start < 0 or char_end <= char_start or char_end > len(context):
                continue
            score = float(start_logits[start]) + float(end_logits[end])
            if score > best_score:
                best_score = score
                best_start, best_end = char_start, char_end

    if best_start < 0:
        return {
            "answer": None,
            "reason": "no_valid_span",
            "margin": inf,
        }

    margin = null_score - best_score
    if margin > null_threshold:
        return {
            "answer": None,
            "reason": "no_answer_in_context",
            "margin": margin,
        }

    return {
        "answer": context[best_start:best_end],
        "start": best_start,
        "end": best_end,
        "score": best_score,
        "null_margin": margin,
    }
