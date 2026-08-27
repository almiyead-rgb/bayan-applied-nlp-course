"""Acceptance canaries for PA-1. Learners must not edit this file."""
from __future__ import annotations

from starter_buggy import l2_norm, ner_entity_f1, prepare_query_vector, serving_model_text, training_model_text


def main() -> int:
    checks = {
        "train_serve_text_contract": (
            serving_model_text("إدارةُ الخِدمة") == training_model_text("إدارةُ الخِدمة")
        ),
        "ner_exact_entity_f1": (
            ner_entity_f1(
                ["O", "B-LOC", "I-LOC", "O"],
                ["O", "B-LOC", "O", "O"],
            ) == 0.0
        ),
        "query_l2_contract": abs(l2_norm(prepare_query_vector([3.0, 4.0])) - 1.0) < 1e-9,
    }
    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    if all(checks.values()):
        print("PA1_CANARIES=PASS")
        return 0
    print(f"PA1_STARTER_EXPECTED={sum(not value for value in checks.values())}_FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
