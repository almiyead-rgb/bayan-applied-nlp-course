# 1. Benchmark قبل التحسين
# Benchmark Before Optimisation

## الفكرة

**التحسين بلا baseline تخمين.** نثبت workload والبيئة والميزانية أولًا، ثم نغيّر عاملًا واحدًا ونقارن.

```text
same model task + same texts + same batch + same device
→ baseline
→ one controlled change
→ candidate
→ latency + throughput + memory + quality
→ decision
```

## تعريفات أساسية

| المصطلح | التعريف | سؤال التحقق |
|---|---|---|
| Latency | زمن إكمال طلب/دفعة | هل يشمل preprocessing وpostprocessing؟ |
| p50 | الوسيط؛ نصف القياسات أسرع منه | هل يمثل الطلب المعتاد؟ |
| p95/p99 | زمن الذيل للطلبات الأبطأ | هل تخفي المتوسطات تأخيرًا مهمًا؟ |
| Throughput | العناصر المكتملة في الثانية | ما batch size المستخدم؟ |
| Warm-up | تشغيلات لا تدخل في القياس | هل أُخرج التحميل/التهيئة الأولى؟ |
| RSS observed peak | أعلى ذاكرة عملية شوهدت أثناء النافذة | هل وُصفت بأنها تقريبية؟ |
| Quality tax | `baseline quality − candidate quality` | هل قيس على الأمثلة نفسها؟ |

قد يزيد batching الإنتاجية مع زيادة latency للطلب الفردي. لذلك لا تختزل الأداء في رقم واحد.

## عقد القياس | Measurement contract

اكتب هذه القيم قبل التشغيل:

| الحقل | مثال وصفي |
|---|---|
| task | bilingual topic classification |
| artefact role | `SYSTEMS_SMOKE` أو `PROJECT_ARTIFACT` |
| model/checkpoint/version | الاسم + commit/revision أو hash |
| preprocessing version | نفس الوحدة المستخدمة في التقييم والخدمة |
| workload | ملف ثابت + عدد الأمثلة + توزيع اللغات والأطوال |
| split | validation للقرارات؛ frozen test مرة بعد التثبيت |
| batch size | 1 أو قيمة موثقة |
| max length/padding | مدعوم بتوزيع الأطوال |
| device/runtime | CPU/GPU + Colab runtime + نسخ المكتبات |
| warm-up/repetitions | 5 و30 على الأقل عندما يسمح الوقت |
| measured boundary | model-only أو end-to-end؛ الأفضل عرض كليهما |

لا تقارن زمن GPU بزمن CPU أو batch 1 بـbatch 16 وتسمي الفرق أثر التكميم.

## اكتب الميزانية قبل رؤية النتيجة

ميزانية الأداء **TARGET خاص بالمشروع**، وليست رقمًا موحدًا للدورة:

```yaml
max_p95_ms: قيمة يحددها المتدرب قبل القياس
min_throughput_items_s: قيمة يحددها المتدرب
max_quality_tax: فرق مقبول يبرره أثر المهمة
target_device: colab-cpu أو البيئة المقصودة
```

يُسمح أن تكون النتيجة «لم تتحقق الميزانية». هذا أفضل من تغيير الهدف بعد ظهور الرقم.

## كود قياس قابل لإعادة الاستخدام

```python
import os
import psutil
from bayan.benchmarking import benchmark_callable

process = psutil.Process(os.getpid())

report = benchmark_callable(
    lambda: predict(batch_texts),
    warmup=5,
    repetitions=30,
    items_per_call=len(batch_texts),
    memory_reader=lambda: process.memory_info().rss,
)

print(report["p50_ms"], report["p95_ms"], report["p99_ms"])
print(report["throughput_items_s"], report["rss_peak_observed_mb"])
```

RSS قد لا يرى تخصيصًا حدث قبل نافذة القياس، ولا يساوي ذاكرة tensor الدقيقة. لذلك نسميه `observed` ونسجل طريقة القياس.

## Free wins قبل تغيير الصيغة

### 1) Inference mode

```python
model.eval()
with torch.inference_mode():
    logits = model(**encoded).logits
```

`eval()` يغير سلوك dropout ونحوه، و`inference_mode()` يوقف تتبع autograd. نحتاج الاثنين.

### 2) قِس الطول

احسب percentiles لأطوال tokens. لا تختر `max_length=512` لأن النموذج يقبله فقط؛ قد تدفع كلفة padding لا تحتاجها أو تقص نصوصًا مهمة.

### 3) Dynamic padding

`padding=True` يجعل الدفعة إلى طول أطول عنصر فيها. أما `padding="max_length"` فيحشو إلى طول ثابت. قارنهما على توزيع حقيقي.

### 4) Length buckets

عند وجود batches، جمع الأطوال المتقاربة يقلل padding. لا يغير label؛ لكنه يغير ترتيب المعالجة، لذلك أعد النتائج إلى ترتيب IDs الأصلي.

## ما الذي يجعل Benchmark غير صالح؟

- قياس أول تشغيل فقط.
- تغيير workload بين baseline وcandidate.
- عدم تسجيل batch أو sequence length.
- عرض المتوسط وحده.
- مقارنة model-only بإصدار end-to-end.
- ضبط budget بعد ظهور النتائج.
- حذف candidate الأبطأ من التقرير.
- قياس الجودة على test ثم تعديل القرار مرارًا.

## تحقق قبل المتابعة

- [ ] artefact role مكتوب.
- [ ] workload ثابت وله IDs.
- [ ] الميزانية كتبت قبل candidate.
- [ ] warm-up خارج القياس.
- [ ] 30 تكرارًا أو سبب تقليلها موثق.
- [ ] p50/p95/p99 وthroughput ظاهرة.
- [ ] memory method موصوفة بأنها تقريبية.
- [ ] frozen test لم يستخدم في اختيار البديل.

## English recap

A valid benchmark fixes the artefact, workload, environment, measured boundary, and budget before testing candidates. Warm-up is excluded, tail latency and throughput are both reported, memory is labelled by method, and every optimisation is compared on the same examples.
