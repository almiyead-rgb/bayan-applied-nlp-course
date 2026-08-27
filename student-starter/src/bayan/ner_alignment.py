"""BIO alignment and entity-level evaluation helpers."""
from __future__ import annotations

from collections.abc import Sequence


IGNORE_INDEX = -100
LABELS = [
    "O",
    "B-SERVICE",
    "I-SERVICE",
    "B-LOCATION",
    "I-LOCATION",
    "B-DATE",
    "I-DATE",
    "B-REF_NUM",
    "I-REF_NUM",
    "B-ORG",
    "I-ORG",
]


def align_word_labels(
    word_ids: Sequence[int | None],
    word_labels: Sequence[int],
    *,
    ignore_index: int = IGNORE_INDEX,
) -> list[int]:
    """Label only the first subword; mask specials and continuations."""
    aligned: list[int] = []
    previous_word_id: int | None = None

    for word_id in word_ids:
        if word_id is None:
            aligned.append(ignore_index)
        else:
            if word_id < 0 or word_id >= len(word_labels):
                raise ValueError(f"word id out of range: {word_id}")
            if word_id != previous_word_id:
                aligned.append(int(word_labels[word_id]))
            else:
                aligned.append(ignore_index)
        previous_word_id = word_id

    return aligned


def bio_entities(tags: Sequence[str]) -> set[tuple[str, int, int]]:
    """Convert BIO tags into (type, start, end-exclusive) entity spans."""
    entities: set[tuple[str, int, int]] = set()
    current_type: str | None = None
    start = -1

    def close(end: int) -> None:
        nonlocal current_type, start
        if current_type is not None:
            entities.add((current_type, start, end))
        current_type, start = None, -1

    for index, tag in enumerate(list(tags) + ["O"]):
        if tag == "O":
            close(index)
            continue
        if "-" not in tag:
            raise ValueError(f"invalid BIO tag: {tag}")
        prefix, entity_type = tag.split("-", 1)
        if prefix not in {"B", "I"} or not entity_type:
            raise ValueError(f"invalid BIO tag: {tag}")

        if prefix == "B" or current_type != entity_type:
            close(index)
            current_type, start = entity_type, index

    return entities


def entity_f1(
    true_sequences: Sequence[Sequence[str]],
    predicted_sequences: Sequence[Sequence[str]],
) -> dict[str, float | int]:
    """Strict entity-level precision, recall, and F1."""
    if len(true_sequences) != len(predicted_sequences):
        raise ValueError("true and predicted sequence counts must match")

    gold: set[tuple[int, str, int, int]] = set()
    predicted: set[tuple[int, str, int, int]] = set()
    for sequence_id, (truth, guess) in enumerate(
        zip(true_sequences, predicted_sequences)
    ):
        if len(truth) != len(guess):
            raise ValueError("tag sequence lengths must match")
        gold |= {(sequence_id, *span) for span in bio_entities(truth)}
        predicted |= {(sequence_id, *span) for span in bio_entities(guess)}

    tp = len(gold & predicted)
    fp = len(predicted - gold)
    fn = len(gold - predicted)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall
        else 0.0
    )
    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "true_entities": len(gold),
        "predicted_entities": len(predicted),
    }
