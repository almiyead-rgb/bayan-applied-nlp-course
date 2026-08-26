"""Serving-contract and startup-canary helpers without a web-framework dependency."""
from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import asdict, dataclass
from typing import Any
import hashlib
import math
import re


_ARABIC_RE = re.compile(r"[\u0600-\u06ff]")
SUPPORTED_LANGUAGES = {"ar", "en", "auto"}


@dataclass(frozen=True)
class ServingManifest:
    """Versions that must travel with a served model artifact."""

    model_id: str
    model_version: str
    preprocessing_version: str
    runtime: str
    label_map: Mapping[int, str]
    artifact_sha256: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["label_map"] = {str(key): value for key, value in self.label_map.items()}
        return data


def sha256_file(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def infer_language(text: str) -> str:
    """Return ``ar`` when Arabic-script text exists, otherwise ``en``."""

    return "ar" if _ARABIC_RE.search(text) else "en"


def validate_request_text(text: Any, *, max_chars: int = 1000) -> str:
    """Validate and trim service input before preprocessing or tokenisation."""

    if not isinstance(text, str):
        raise ValueError("text must be a string")
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("text must not be empty")
    if len(cleaned) > max_chars:
        raise ValueError(f"text exceeds max_chars={max_chars}")
    return cleaned


def resolve_language(text: str, language: str) -> str:
    if language not in SUPPORTED_LANGUAGES:
        raise ValueError(f"language must be one of {sorted(SUPPORTED_LANGUAGES)}")
    return infer_language(text) if language == "auto" else language


def validate_manifest(
    manifest: ServingManifest,
    *,
    expected_preprocessing_version: str,
    expected_model_version: str | None = None,
) -> None:
    """Fail closed when model and serving contracts do not match."""

    if manifest.preprocessing_version != expected_preprocessing_version:
        raise RuntimeError("preprocessing version mismatch")
    if expected_model_version and manifest.model_version != expected_model_version:
        raise RuntimeError("model version mismatch")
    if not manifest.label_map:
        raise RuntimeError("label_map must not be empty")
    if not all(
        value.strip()
        for value in (
            manifest.model_id,
            manifest.model_version,
            manifest.preprocessing_version,
            manifest.runtime,
        )
    ):
        raise RuntimeError("manifest identity/version fields must not be empty")
    if not re.fullmatch(r"[0-9a-f]{64}", manifest.artifact_sha256):
        raise RuntimeError("artifact_sha256 must be a lowercase SHA-256 digest")


def build_prediction_response(
    *,
    request_id: str,
    text: str,
    language: str,
    label: str,
    confidence: float,
    latency_ms: float,
    manifest: ServingManifest,
) -> dict[str, Any]:
    """Build the stable JSON envelope used by the Bayan classification endpoint."""

    if not request_id.strip():
        raise ValueError("request_id must not be empty")
    if label not in manifest.label_map.values():
        raise ValueError("label is not present in manifest.label_map")
    if not 0 <= confidence <= 1:
        raise ValueError("confidence must be between 0 and 1")
    if not math.isfinite(latency_ms) or latency_ms < 0:
        raise ValueError("latency_ms must be finite and non-negative")
    return {
        "request_id": request_id,
        "language": resolve_language(validate_request_text(text), language),
        "prediction": {"label": label, "confidence": float(confidence)},
        "latency_ms": float(latency_ms),
        "model": {
            "id": manifest.model_id,
            "version": manifest.model_version,
            "runtime": manifest.runtime,
            "preprocessing_version": manifest.preprocessing_version,
        },
    }


def run_canaries(
    predict: Callable[[str, str], Mapping[str, Any]],
    cases: Sequence[Mapping[str, str]],
) -> list[dict[str, Any]]:
    """Run startup cases and fail on contract drift or an expected-label change."""

    if not cases:
        raise ValueError("canary cases must not be empty")
    reports = []
    for case in cases:
        name = case.get("name", "unnamed")
        text = validate_request_text(case.get("text"))
        language = case.get("language", "auto")
        response = dict(predict(text, language))
        prediction = response.get("prediction")
        if not isinstance(prediction, Mapping):
            raise RuntimeError(f"canary {name}: missing prediction object")
        label = prediction.get("label")
        confidence = prediction.get("confidence")
        if not isinstance(label, str) or not isinstance(confidence, (int, float)):
            raise RuntimeError(f"canary {name}: invalid prediction contract")
        if not 0 <= float(confidence) <= 1:
            raise RuntimeError(f"canary {name}: confidence outside [0, 1]")
        expected = case.get("expected_label")
        if expected is not None and label != expected:
            raise RuntimeError(
                f"canary {name}: expected label {expected!r}, received {label!r}"
            )
        reports.append({"name": name, "status": "PASS", "label": label})
    return reports
