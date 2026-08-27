# Rival Team Evaluation Report — COURSE FIXTURE

> هذا تقرير منافس اصطناعي صُمم للتقييم. لا يمثل نظامًا أو جهة حقيقية.

## Executive claim

The classifier is ready to ship. Accuracy is **91.2%**, higher than the current system's **89.4%**.

## Method notes

- Dataset: `feedback_latest.csv`; owner, row count, licence, hash, and collection window not recorded.
- Split: random rows; no grouping key was retained.
- Metric: aggregate accuracy only.
- Threshold: tried `0.30`, `0.40`, `0.50`, and `0.60` on the test set; `0.40` gave the best score above.
- Training: seed `42`; no repeated run or paired comparison.
- Slices: not reported. The team states Arabic fairness is covered because a language detector runs before classification.

## Behavioural checks

| Check | Passed |
|---|---:|
| punctuation invariance | 5/5 |
| whitespace invariance | 5/5 |
| negated-resolution direction | 3/5 |

The two negation regressions were excluded from the release summary because the aggregate score stayed above 90%.

## Serving note

Median latency is **28 ms** from five warm requests on a developer laptop. Batch size, sequence-length distribution, p95/p99, memory, model version, and preprocessing version were not recorded.

## Proposed release

Replace the current model on Friday and monitor complaints after deployment.
