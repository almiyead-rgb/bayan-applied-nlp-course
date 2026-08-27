# BENCHMARKS — Bayan

> انسخ هذا الملف إلى جذر مشروعك باسم `BENCHMARKS.md`، ثم استبدل كل `FILL_ME`.  
> Copy this file to the project root as `BENCHMARKS.md`, then replace every `FILL_ME`.

## 1. Claim boundary | حدود الادعاء

- Artefact role: `PROJECT_ARTIFACT`
- Result label: `MEASURED`
- Task: FILL_ME
- Decision date: FILL_ME
- Author: FILL_ME

لا تستخدم `PROJECT_ARTIFACT` أو `MEASURED` إن كنت ما زلت تشغّل checkpoint مسار Systems Smoke.

## 2. Performance budget — written before candidates

| Constraint | TARGET | Why this matters |
|---|---:|---|
| p95 end-to-end latency | FILL_ME ms | FILL_ME |
| minimum throughput | FILL_ME items/s | FILL_ME |
| maximum quality tax | FILL_ME | FILL_ME |
| target device | FILL_ME | FILL_ME |

- Commit/time proving budget existed before candidate: FILL_ME

## 3. Reproduction contract

| Field | Value |
|---|---|
| Colab runtime/Python | FILL_ME |
| Device/provider | FILL_ME |
| CPU/GPU details | FILL_ME |
| Library versions | FILL_ME |
| Model ID/revision/hash | FILL_ME |
| Preprocessing version | FILL_ME |
| Label map version | FILL_ME |
| Workload path/hash | FILL_ME |
| Split | validation / frozen test: FILL_ME |
| Examples + AR/EN counts | FILL_ME |
| Length distribution | p50=FILL_ME, p95=FILL_ME, max=FILL_ME |
| Batch size | FILL_ME |
| Padding/max length | FILL_ME |
| Warm-up/repetitions | FILL_ME / FILL_ME |
| Measured boundary | model-only / end-to-end: FILL_ME |
| Memory method | process RSS observed peak / other: FILL_ME |

## 4. Controlled candidates

| ID | Runtime/precision | Only intended change | Artefact hash | Size MiB |
|---|---|---|---|---:|
| A | PyTorch FP32 reference | baseline | FILL_ME | FILL_ME |
| B | ONNX Runtime FP32 | runtime/export | FILL_ME | FILL_ME |
| C | ONNX Runtime dynamic INT8 | weight quantisation | FILL_ME | FILL_ME |

## 5. Parity

| Comparison | max abs logits diff | mean abs diff | prediction agreement | Verdict |
|---|---:|---:|---:|---|
| A vs B | FILL_ME | FILL_ME | FILL_ME | PASS/FAIL: FILL_ME |
| A vs C | FILL_ME | FILL_ME | FILL_ME | PASS/FAIL: FILL_ME |

- Tolerance chosen before inspection: FILL_ME
- Rationale: FILL_ME

## 6. Performance results

| ID | p50 ms | p95 ms | p99 ms | items/s | observed peak RSS MiB | speedup vs A |
|---|---:|---:|---:|---:|---:|---:|
| A | FILL_ME | FILL_ME | FILL_ME | FILL_ME | FILL_ME | 1.00× |
| B | FILL_ME | FILL_ME | FILL_ME | FILL_ME | FILL_ME | FILL_ME |
| C | FILL_ME | FILL_ME | FILL_ME | FILL_ME | FILL_ME | FILL_ME |

## 7. Quality results

- Primary task metric: FILL_ME
- Evaluation file/split: FILL_ME

| ID | Task quality | Quality tax = A − candidate | Small-sample/CI note |
|---|---:|---:|---|
| A | FILL_ME | 0 | FILL_ME |
| B | FILL_ME | FILL_ME | FILL_ME |
| C | FILL_ME | FILL_ME | FILL_ME |

## 8. Budget verdict and decision

| Candidate | latency OK | throughput OK | quality OK | Overall |
|---|---|---|---|---|
| B | FILL_ME | FILL_ME | FILL_ME | FILL_ME |
| C | FILL_ME | FILL_ME | FILL_ME | FILL_ME |

- Selected runtime: FILL_ME
- Decision: **ADOPT / REJECT / KEEP FP32** — FILL_ME
- Evidence-based reason: FILL_ME
- Known limitation/noise source: FILL_ME
- FP32 rollback/reproduction path: FILL_ME
- Generated JSON report: `reports/benchmark_results.json`

## 9. Reproduction commands

```bash
# FILL_ME: exact setup and benchmark commands without tokens or secrets
```

## 10. Integrity check

- [ ] Budget predates candidate results.
- [ ] Same workload/device/batch/boundary used.
- [ ] Warm-up excluded.
- [ ] At least 30 measured repetitions or limitation explained.
- [ ] p50/p95/p99 and throughput included.
- [ ] Memory wording matches measurement method.
- [ ] Quality tax uses the same examples.
- [ ] Failed/slower candidates were not hidden.
- [ ] Numbers are `MEASURED`, not copied references.
- [ ] No weights, ONNX artefacts, cache, secrets, or PII committed.
