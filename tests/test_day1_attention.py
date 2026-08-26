import numpy as np
import pytest

from bayan.attention import scaled_dot_product_attention


def test_attention_shapes_and_probabilities():
    q = np.eye(4)
    k = np.eye(4)
    v = np.arange(16, dtype=float).reshape(4, 4)
    output, weights = scaled_dot_product_attention(q, k, v)
    assert output.shape == (4, 4)
    assert weights.shape == (4, 4)
    assert np.allclose(weights.sum(axis=-1), 1.0)


def test_keep_mask_true_means_participate():
    q = k = np.eye(4)
    v = np.arange(16, dtype=float).reshape(4, 4)
    mask = np.tril(np.ones((4, 4), dtype=bool))
    _, weights = scaled_dot_product_attention(q, k, v, keep_mask=mask)
    assert np.allclose(weights[0, 1:], 0.0)


def test_all_masked_row_is_rejected():
    q = k = np.eye(2)
    v = np.ones((2, 2))
    with pytest.raises(ValueError, match="at least one key"):
        scaled_dot_product_attention(
            q, k, v, keep_mask=np.zeros((2, 2), dtype=bool)
        )
