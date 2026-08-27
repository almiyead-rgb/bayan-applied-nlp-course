"""Intentionally defective PA-1 starter; fix in the learner's copy."""
from __future__ import annotations

import math
import re
import unicodedata


ALEF_TRANSLATION = str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ى": "ي"})


def training_model_text(text: str) -> str:
    """Reference training path used by the scenario."""
    normalised = unicodedata.normalize("NFC", text).translate(ALEF_TRANSLATION)
    normalised = "".join(char for char in normalised if not unicodedata.combining(char))
    return re.sub(r"\s+", " ", normalised).strip()


def serving_model_text(text: str) -> str:
    """BUG: serving must implement the same versioned text contract as training."""
    return text.strip()


def ner_entity_f1(gold_bio: list[str], predicted_bio: list[str]) -> float:
    """BUG: token agreement is not entity-level exact-span F1."""
    if len(gold_bio) != len(predicted_bio):
        raise ValueError("BIO sequences must have the same length")
    return sum(gold == predicted for gold, predicted in zip(gold_bio, predicted_bio)) / len(gold_bio)


def prepare_query_vector(vector: list[float]) -> list[float]:
    """BUG: IndexFlatIP cosine search requires an L2-normalised query too."""
    if not vector:
        raise ValueError("query vector cannot be empty")
    return list(vector)


def l2_norm(vector: list[float]) -> float:
    return math.sqrt(sum(value * value for value in vector))
