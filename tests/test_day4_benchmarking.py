from pathlib import Path

import pytest

from bayan.benchmarking import (
    artifact_size_mb,
    assess_budget,
    benchmark_callable,
    percentile,
    quality_tax,
    speedup,
    summarise_latencies,
)


def test_percentile_uses_linear_interpolation():
    assert percentile([1, 2, 3, 4], 50) == 2.5
    assert percentile([4, 1, 3, 2], 95) == pytest.approx(3.85)


def test_latency_summary_reports_tail_and_throughput():
    report = summarise_latencies([10, 20, 30, 40], items_per_call=2)
    assert report["repetitions"] == 4
    assert report["p50_ms"] == 25
    assert report["p95_ms"] > report["p50_ms"]
    assert report["throughput_items_s"] == pytest.approx(80)


def test_benchmark_keeps_warmup_out_of_measured_repetitions():
    calls = []

    def operation():
        calls.append(len(calls))

    report = benchmark_callable(operation, warmup=3, repetitions=5, items_per_call=2)
    assert len(calls) == 8
    assert report["warmup"] == 3
    assert report["repetitions"] == 5
    assert report["throughput_items_s"] > 0


def test_benchmark_preserves_observed_rss_contract():
    readings = iter([100, 120, 110, 140])
    report = benchmark_callable(
        lambda: None,
        warmup=0,
        repetitions=3,
        memory_reader=lambda: next(readings),
    )
    assert report["rss_start_mb"] == 100 / (1024**2)
    assert report["rss_peak_observed_mb"] == 140 / (1024**2)
    assert report["rss_observed_delta_mb"] == 40 / (1024**2)


def test_quality_tax_and_speedup_have_explicit_direction():
    assert quality_tax(0.91, 0.89) == pytest.approx(0.02)
    assert quality_tax(0.91, 0.93) == pytest.approx(-0.02)
    assert speedup(20, 10) == 2


def test_budget_is_chosen_by_caller_and_all_constraints_must_pass():
    report = {"p95_ms": 42.0, "throughput_items_s": 30.0}
    verdict = assess_budget(
        report,
        quality_tax_value=0.01,
        max_p95_ms=50,
        max_quality_tax=0.02,
        min_throughput_items_s=25,
    )
    assert verdict == {
        "latency_ok": True,
        "quality_ok": True,
        "throughput_ok": True,
        "budget_met": True,
    }


def test_artifact_size_supports_file_and_directory(tmp_path: Path):
    (tmp_path / "a.bin").write_bytes(b"a" * 1024)
    nested = tmp_path / "nested"
    nested.mkdir()
    (nested / "b.bin").write_bytes(b"b" * 1024)
    assert artifact_size_mb(tmp_path / "a.bin") == pytest.approx(1024 / 1024**2)
    assert artifact_size_mb(tmp_path) == pytest.approx(2048 / 1024**2)


@pytest.mark.parametrize(
    "function,args",
    [
        (percentile, ([], 50)),
        (summarise_latencies, ([],)),
        (speedup, (1, 0)),
        (quality_tax, (float("nan"), 0.5)),
    ],
)
def test_invalid_measurements_fail_closed(function, args):
    with pytest.raises(ValueError):
        function(*args)
