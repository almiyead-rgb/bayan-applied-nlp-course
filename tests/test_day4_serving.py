import pytest

from bayan.serving import (
    ServingManifest,
    build_prediction_response,
    infer_language,
    resolve_language,
    run_canaries,
    validate_manifest,
    validate_request_text,
)


def manifest():
    return ServingManifest(
        model_id="bayan-classifier",
        model_version="1.0.0",
        preprocessing_version="ar-en-v1",
        runtime="onnxruntime-cpu",
        label_map={0: "negative", 1: "neutral", 2: "positive"},
        artifact_sha256="a" * 64,
    )


def test_language_detection_and_explicit_override():
    assert infer_language("الخدمة سريعة") == "ar"
    assert infer_language("The service is fast") == "en"
    assert resolve_language("الخدمة سريعة", "auto") == "ar"
    assert resolve_language("الخدمة سريعة", "en") == "en"


@pytest.mark.parametrize("value", ["", "   ", None, 42])
def test_invalid_text_is_rejected(value):
    with pytest.raises(ValueError):
        validate_request_text(value)


def test_manifest_fails_closed_on_train_serve_skew():
    validate_manifest(manifest(), expected_preprocessing_version="ar-en-v1")
    with pytest.raises(RuntimeError, match="preprocessing version mismatch"):
        validate_manifest(manifest(), expected_preprocessing_version="ar-en-v2")


def test_manifest_rejects_empty_identity_fields():
    invalid = ServingManifest(
        model_id="",
        model_version="1.0.0",
        preprocessing_version="ar-en-v1",
        runtime="onnxruntime-cpu",
        label_map={0: "negative"},
        artifact_sha256="a" * 64,
    )
    with pytest.raises(RuntimeError, match="must not be empty"):
        validate_manifest(invalid, expected_preprocessing_version="ar-en-v1")


def test_response_exposes_traceable_model_metadata():
    response = build_prediction_response(
        request_id="req-1",
        text="الخدمة سريعة",
        language="auto",
        label="positive",
        confidence=0.9,
        latency_ms=12.5,
        manifest=manifest(),
    )
    assert response["language"] == "ar"
    assert response["prediction"] == {"label": "positive", "confidence": 0.9}
    assert response["model"]["preprocessing_version"] == "ar-en-v1"


def test_response_rejects_non_finite_latency():
    with pytest.raises(ValueError, match="finite"):
        build_prediction_response(
            request_id="req-1",
            text="valid text",
            language="en",
            label="positive",
            confidence=0.9,
            latency_ms=float("nan"),
            manifest=manifest(),
        )


def test_canaries_detect_label_drift():
    def predict(text, language):
        return {"prediction": {"label": "positive", "confidence": 0.8}}

    cases = [
        {
            "name": "arabic-positive",
            "text": "الخدمة سريعة",
            "language": "ar",
            "expected_label": "positive",
        }
    ]
    assert run_canaries(predict, cases)[0]["status"] == "PASS"
    cases[0]["expected_label"] = "negative"
    with pytest.raises(RuntimeError, match="expected label"):
        run_canaries(predict, cases)
