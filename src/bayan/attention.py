"""NumPy reference implementation of scaled dot-product attention."""
from __future__ import annotations

import math
import numpy as np


def _softmax(values: np.ndarray, axis: int = -1) -> np.ndarray:
    shifted = values - np.max(values, axis=axis, keepdims=True)
    exp = np.exp(shifted)
    return exp / exp.sum(axis=axis, keepdims=True)


def scaled_dot_product_attention(
    query: np.ndarray,
    key: np.ndarray,
    value: np.ndarray,
    *,
    keep_mask: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Compute softmax(QKᵀ/√d_k)V.

    keep_mask follows PyTorch SDPA semantics: True means the position may
    participate. It must broadcast to the attention score shape.
    """

    q = np.asarray(query, dtype=np.float64)
    k = np.asarray(key, dtype=np.float64)
    v = np.asarray(value, dtype=np.float64)
    if q.ndim < 2 or k.ndim < 2 or v.ndim < 2:
        raise ValueError("query, key, and value must have at least 2 dimensions")
    if q.shape[-1] != k.shape[-1]:
        raise ValueError("query and key feature dimensions must match")
    if k.shape[-2] != v.shape[-2]:
        raise ValueError("key and value sequence lengths must match")

    scores = q @ np.swapaxes(k, -1, -2)
    scores = scores / math.sqrt(q.shape[-1])

    if keep_mask is not None:
        mask = np.asarray(keep_mask, dtype=bool)
        try:
            mask = np.broadcast_to(mask, scores.shape)
        except ValueError as exc:
            raise ValueError("keep_mask cannot broadcast to score shape") from exc
        if np.any(~mask.any(axis=-1)):
            raise ValueError("every query row must keep at least one key")
        scores = np.where(mask, scores, -np.inf)

    weights = _softmax(scores, axis=-1)
    output = weights @ v
    return output, weights
