"""Honest, dependency-light inference benchmarking utilities for Bayan."""
from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from time import perf_counter, perf_counter_ns
from typing import Any
import math


def _finite_non_negative(value: float, name: str) -> float:
    number = float(value)
    if not math.isfinite(number) or number < 0:
        raise ValueError(f"{name} must be finite and non-negative")
    return number


def percentile(values: Sequence[float], q: float) -> float:
    """Return a linearly interpolated percentile for a non-empty sequence."""

    if not values:
        raise ValueError("values must not be empty")
    if not 0 <= q <= 100:
        raise ValueError("q must be between 0 and 100")
    ordered = sorted(_finite_non_negative(value, "latency") for value in values)
    position = (len(ordered) - 1) * q / 100
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def summarise_latencies(
    latencies_ms: Sequence[float], *, items_per_call: int = 1
) -> dict[str, float | int]:
    """Summarise measured calls with latency percentiles and throughput."""

    if not latencies_ms:
        raise ValueError("latencies_ms must not be empty")
    if items_per_call < 1:
        raise ValueError("items_per_call must be positive")
    values = [_finite_non_negative(value, "latency") for value in latencies_ms]
    total_seconds = sum(values) / 1000
    throughput = len(values) * items_per_call / total_seconds if total_seconds else math.inf
    return {
        "repetitions": len(values),
        "items_per_call": items_per_call,
        "p50_ms": percentile(values, 50),
        "p95_ms": percentile(values, 95),
        "p99_ms": percentile(values, 99),
        "mean_ms": sum(values) / len(values),
        "min_ms": min(values),
        "max_ms": max(values),
        "throughput_items_s": throughput,
    }


def benchmark_callable(
    function: Callable[[], Any],
    *,
    warmup: int = 5,
    repetitions: int = 30,
    items_per_call: int = 1,
    memory_reader: Callable[[], int] | None = None,
) -> dict[str, float | int]:
    """Benchmark a zero-argument inference closure after unmeasured warm-up calls.

    ``memory_reader`` may return current process bytes. RSS is an approximation, so
    the report preserves start and observed peak instead of claiming exact tensor
    allocation.
    """

    if warmup < 0 or repetitions < 1:
        raise ValueError("warmup must be non-negative and repetitions must be positive")
    if items_per_call < 1:
        raise ValueError("items_per_call must be positive")

    for _ in range(warmup):
        function()

    rss_start = memory_reader() if memory_reader else None
    rss_peak = rss_start
    durations = []
    for _ in range(repetitions):
        start = perf_counter_ns()
        function()
        durations.append((perf_counter_ns() - start) / 1_000_000)
        if memory_reader:
            current = memory_reader()
            rss_peak = current if rss_peak is None else max(rss_peak, current)

    report = {"warmup": warmup, **summarise_latencies(durations, items_per_call=items_per_call)}
    if rss_start is not None and rss_peak is not None:
        report.update(
            {
                "rss_start_mb": rss_start / (1024**2),
                "rss_peak_observed_mb": rss_peak / (1024**2),
                "rss_observed_delta_mb": max(0, rss_peak - rss_start) / (1024**2),
            }
        )
    return report


def benchmark_concurrent(
    function: Callable[[], Any],
    *,
    warmup_requests: int = 16,
    requests: int = 160,
    concurrency: int = 16,
) -> dict[str, float | int]:
    """Measure one closed-loop concurrent request workload.

    Each worker issues one request at a time; latency is measured inside the worker,
    while throughput uses wall time for the complete measured request set. The caller
    owns the HTTP client and must assert the response contract inside ``function``.
    """

    if warmup_requests < 0:
        raise ValueError("warmup_requests must be non-negative")
    if requests < 1 or concurrency < 1:
        raise ValueError("requests and concurrency must be positive")
    if concurrency > requests:
        raise ValueError("concurrency cannot exceed measured requests")

    def measured_call() -> float:
        started = perf_counter_ns()
        function()
        return (perf_counter_ns() - started) / 1_000_000

    if warmup_requests:
        with ThreadPoolExecutor(max_workers=min(concurrency, warmup_requests)) as pool:
            for future in as_completed(
                [pool.submit(function) for _ in range(warmup_requests)]
            ):
                future.result()

    wall_started = perf_counter()
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        latencies = [
            future.result()
            for future in as_completed([pool.submit(measured_call) for _ in range(requests)])
        ]
    wall_seconds = perf_counter() - wall_started
    report = summarise_latencies(latencies)
    wall_throughput = requests / wall_seconds if wall_seconds else math.inf
    report.update(
        {
            "warmup_requests": warmup_requests,
            "requests": requests,
            "concurrency": concurrency,
            "wall_time_s": wall_seconds,
            "throughput_items_s": wall_throughput,
            "throughput_requests_s": wall_throughput,
        }
    )
    return report


def quality_tax(baseline_score: float, candidate_score: float) -> float:
    """Return baseline minus candidate; a positive value means quality dropped."""

    baseline = _finite_non_negative(baseline_score, "baseline_score")
    candidate = _finite_non_negative(candidate_score, "candidate_score")
    return baseline - candidate


def speedup(baseline_ms: float, candidate_ms: float) -> float:
    """Return baseline latency divided by candidate latency."""

    baseline = _finite_non_negative(baseline_ms, "baseline_ms")
    candidate = _finite_non_negative(candidate_ms, "candidate_ms")
    if candidate == 0:
        raise ValueError("candidate_ms must be greater than zero")
    return baseline / candidate


def artifact_size_mb(path: str | Path) -> float:
    """Return the size of one file or all files below a directory in MiB."""

    target = Path(path)
    if not target.exists():
        raise FileNotFoundError(target)
    if target.is_file():
        total = target.stat().st_size
    else:
        total = sum(item.stat().st_size for item in target.rglob("*") if item.is_file())
    return total / (1024**2)


def assess_budget(
    benchmark: Mapping[str, float | int],
    *,
    quality_tax_value: float,
    max_p95_ms: float,
    max_quality_tax: float,
    min_throughput_items_s: float | None = None,
    latency_key: str = "p95_ms",
) -> dict[str, bool]:
    """Evaluate a budget chosen before measurement; never invent course targets."""

    if latency_key not in {"p50_ms", "p95_ms", "p99_ms"}:
        raise ValueError("latency_key must be p50_ms, p95_ms, or p99_ms")
    latency = _finite_non_negative(float(benchmark[latency_key]), latency_key)
    throughput = _finite_non_negative(
        float(benchmark["throughput_items_s"]), "throughput_items_s"
    )
    latency_ok = latency <= _finite_non_negative(max_p95_ms, "max_p95_ms")
    quality_ok = quality_tax_value <= _finite_non_negative(
        max_quality_tax, "max_quality_tax"
    )
    throughput_ok = True
    if min_throughput_items_s is not None:
        throughput_ok = throughput >= _finite_non_negative(
            min_throughput_items_s, "min_throughput_items_s"
        )
    return {
        "latency_ok": latency_ok,
        "quality_ok": quality_ok,
        "throughput_ok": throughput_ok,
        "budget_met": latency_ok and quality_ok and throughput_ok,
    }
