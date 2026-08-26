import numpy as np
import pytest

from bayan.retrieval import (
    SEARCH_MANIFEST_VERSION,
    exact_inner_product_search,
    l2_normalize,
    retrieval_metrics,
    tune_no_answer_threshold,
    validate_index_manifest,
)


def test_l2_normalize_returns_unit_float32_rows():
    vectors = l2_normalize(np.array([[3.0, 4.0], [0.0, 2.0]]))
    assert vectors.dtype == np.float32
    assert np.allclose(np.linalg.norm(vectors, axis=1), 1.0)


def test_l2_normalize_rejects_zero_vectors():
    with pytest.raises(ValueError, match="zero vectors"):
        l2_normalize(np.array([[0.0, 0.0]]))


def test_exact_search_matches_cosine_ranking_after_normalization():
    corpus = l2_normalize(np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]))
    query = l2_normalize(np.array([[0.9, 0.1]]))
    results = exact_inner_product_search(query, corpus, ["a", "b", "c"], k=2)
    assert [item["case_id"] for item in results[0]] == ["a", "c"]


def test_recall_and_mrr_skip_no_answer_queries():
    report = retrieval_metrics(
        [["x", "a", "b"], ["z"], ["none"]],
        [["a"], ["z"], []],
        k=3,
    )
    assert report["recall@3"] == 1.0
    assert report["mrr@3"] == 0.75
    assert report["skipped_no_answer"] == 1


def test_threshold_is_tuned_only_from_supplied_validation_labels():
    result = tune_no_answer_threshold([0.82, 0.75, 0.20, 0.18], [True, True, False, False])
    assert 0.20 < result["threshold"] < 0.75
    assert result["validation_accuracy"] == 1.0


def test_manifest_pins_model_profile_dimension_and_count():
    manifest = {
        "manifest_version": SEARCH_MANIFEST_VERSION,
        "model_id": "sentence-transformers/example",
        "embedding_dimension": 3,
        "normalization": "l2",
        "preprocessing_profile": "search@1.0.0/camel",
        "dataset_id": "bayan-day3-synthetic-v1",
        "vector_count": 4,
    }
    assert validate_index_manifest(
        manifest, expected_vectors=4, expected_dimension=3
    )["model_id"] == "sentence-transformers/example"
    broken = dict(manifest, normalization="none")
    with pytest.raises(ValueError, match="requires l2"):
        validate_index_manifest(broken)
