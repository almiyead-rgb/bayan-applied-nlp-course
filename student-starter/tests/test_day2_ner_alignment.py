import pytest

from bayan.ner_alignment import align_word_labels, bio_entities, entity_f1


def test_specials_and_continuation_subwords_are_masked():
    word_ids = [None, 0, 1, 1, 2, None]
    word_labels = [0, 3, 0]
    assert align_word_labels(word_ids, word_labels) == [-100, 0, 3, -100, 0, -100]


def test_word_id_out_of_range_is_rejected():
    with pytest.raises(ValueError, match="out of range"):
        align_word_labels([0, 2], [0, 1])


def test_bio_entities_use_strict_boundaries():
    tags = ["O", "B-ORG", "I-ORG", "O", "B-LOCATION"]
    assert bio_entities(tags) == {("ORG", 1, 3), ("LOCATION", 4, 5)}


def test_entity_f1_penalises_boundary_errors():
    truth = [["B-ORG", "I-ORG", "O"]]
    guess = [["B-ORG", "O", "O"]]
    report = entity_f1(truth, guess)
    assert report["f1"] == 0.0
    assert report["true_entities"] == 1
    assert report["predicted_entities"] == 1
