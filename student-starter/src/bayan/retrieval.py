"""Dependency-light retrieval contracts and metrics for Bayan."""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

import numpy as np

SEARCH_MANIFEST_VERSION = "1.0.0"


def l2_normalize(matrix: np.ndarray) -> np.ndarray:
    """Return row-wise L2-normalised float32 vectors."""

    vectors = np.asarray(matrix, dtype=np.float32)
    if vectors.ndim != 2 or vectors.shape[0] == 0 or vectors.shape[1] == 0:
        raise ValueError("matrix must be a non-empty 2D array")
    if not np.isfinite(vectors).all():
        raise ValueError("matrix must contain only finite values")
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    if np.any(norms == 0):
        raise ValueError("zero vectors cannot be L2-normalised")
    return vectors / norms


def exact_inner_product_search(
    query_vectors: np.ndarray,
    corpus_vectors: np.ndarray,
    corpus_ids: Sequence[str],
    *,
    k: int,
) -> list[list[dict[str, float | str]]]:
    """Small exact-search oracle matching normalised IndexFlatIP semantics."""

    queries = np.asarray(query_vectors, dtype=np.float32)
    corpus = np.asarray(corpus_vectors, dtype=np.float32)
    if queries.ndim != 2 or corpus.ndim != 2:
        raise ValueError("query and corpus vectors must be 2D")
    if queries.shape[1] != corpus.shape[1]:
        raise ValueError("query and corpus dimensions must match")
    if corpus.shape[0] != len(corpus_ids):
        raise ValueError("corpus_ids length must match corpus rows")
    if k < 1:
        raise ValueError("k must be positive")

    width = min(k, len(corpus_ids))
    scores = queries @ corpus.T
    output: list[list[dict[str, float | str]]] = []
    for row in scores:
        order = np.argsort(-row, kind="stable")[:width]
        output.append(
            [
                {"case_id": str(corpus_ids[index]), "score": float(row[index])}
                for index in order
            ]
        )
    return output


def retrieval_metrics(
    ranked_ids: Sequence[Sequence[str]],
    relevant_ids: Sequence[Sequence[str]],
    *,
    k: int,
) -> dict[str, float | int]:
    """Compute hit-based Recall@k and MRR@k on answerable queries."""

    if len(ranked_ids) != len(relevant_ids):
        raise ValueError("ranked_ids and relevant_ids must have the same length")
    if k < 1:
        raise ValueError("k must be positive")

    hits: list[float] = []
    reciprocal_ranks: list[float] = []
    skipped_no_answer = 0
    for ranking, relevant in zip(ranked_ids, relevant_ids):
        relevant_set = {str(item) for item in relevant}
        if not relevant_set:
            skipped_no_answer += 1
            continue
        top = [str(item) for item in ranking[:k]]
        first_rank = next(
            (rank for rank, item in enumerate(top, start=1) if item in relevant_set),
            None,
        )
        hits.append(float(first_rank is not None))
        reciprocal_ranks.append(1.0 / first_rank if first_rank else 0.0)

    if not hits:
        raise ValueError("at least one answerable query is required")
    return {
        f"recall@{k}": float(np.mean(hits)),
        f"mrr@{k}": float(np.mean(reciprocal_ranks)),
        "answerable_queries": len(hits),
        "skipped_no_answer": skipped_no_answer,
    }


def tune_no_answer_threshold(
    best_scores: Sequence[float],
    has_relevant: Sequence[bool],
) -> dict[str, float]:
    """Tune score >= threshold => return results on validation data only."""

    if len(best_scores) != len(has_relevant) or not best_scores:
        raise ValueError("scores and labels must have the same non-zero length")
    scores = np.asarray(best_scores, dtype=float)
    if not np.isfinite(scores).all():
        raise ValueError("scores must be finite")

    unique = sorted(set(float(score) for score in scores))
    candidates = [unique[0] - 1e-6]
    candidates.extend((left + right) / 2 for left, right in zip(unique, unique[1:]))
    candidates.append(unique[-1] + 1e-6)

    labels = np.asarray(has_relevant, dtype=bool)
    best_threshold = candidates[0]
    best_accuracy = -1.0
    for threshold in candidates:
        predictions = scores >= threshold
        accuracy = float(np.mean(predictions == labels))
        if accuracy > best_accuracy or (
            accuracy == best_accuracy and threshold > best_threshold
        ):
            best_accuracy = accuracy
            best_threshold = threshold
    return {"threshold": float(best_threshold), "validation_accuracy": best_accuracy}


def validate_index_manifest(
    manifest: Mapping[str, Any],
    *,
    expected_vectors: int | None = None,
    expected_dimension: int | None = None,
) -> dict[str, Any]:
    """Validate the minimum reproducibility contract for a search index."""

    required = {
        "manifest_version",
        "model_id",
        "embedding_dimension",
        "normalization",
        "preprocessing_profile",
        "dataset_id",
        "vector_count",
    }
    missing = sorted(required - set(manifest))
    if missing:
        raise ValueError(f"manifest is missing keys: {missing}")
    if manifest["manifest_version"] != SEARCH_MANIFEST_VERSION:
        raise ValueError("unsupported manifest version")
    if manifest["normalization"] != "l2":
        raise ValueError("cosine/IndexFlatIP contract requires l2 normalization")
    if int(manifest["embedding_dimension"]) < 1 or int(manifest["vector_count"]) < 1:
        raise ValueError("dimension and vector_count must be positive")
    if expected_vectors is not None and int(manifest["vector_count"]) != expected_vectors:
        raise ValueError("manifest vector_count does not match the loaded index")
    if (
        expected_dimension is not None
        and int(manifest["embedding_dimension"]) != expected_dimension
    ):
        raise ValueError("manifest dimension does not match the loaded index")
    return dict(manifest)
