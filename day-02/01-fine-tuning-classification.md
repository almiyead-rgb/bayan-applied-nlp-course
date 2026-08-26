# 1. Fine-tuning والتصنيف
# Fine-tuning and Text Classification

## الفكرة

**Pretraining** يعلم المشفر أنماطًا لغوية عامة من نصوص كبيرة.  
**Fine-tuning** يحدث أوزان النموذج ورأس المهمة على بيانات معنونة لمشكلة محددة.

في تصنيف بيان:

```text
"تعذر تسجيل الدخول إلى البوابة"
→ tokenizer
→ multilingual encoder
→ classification head
→ digital_service
```

رأس التصنيف طبقة صغيرة تحول تمثيل النص إلى logits بعدد الفئات. التدريب يستخدم labels لحساب loss ثم يحدث المعاملات.

## لماذا Baseline أولًا؟

نبدأ بـTF-IDF + مصنف خطي لأنه:

- يعمل بسرعة على CPU.
- يكشف labels المكسورة أو المهمة السهلة جدًا.
- يعطي خط أساس نقارن به تكلفة Transformer.
- يمنع عبارة «النموذج جيد» بلا مقام مقارنة.

لا يشترط أن يهزم Transformer الـbaseline في عينة Smoke الصغيرة. إذا لم يهزمه، نسجل النتيجة ونشرح أن التدريب والبيانات غير كافيين بدل تغيير test set.

## عقد التقسيم | Split contract

| Split | ماذا نفعل به؟ |
|---|---|
| Train | تحديث الأوزان |
| Validation | اختيار الإعدادات ومراقبة overfitting |
| Frozen test | قياس نهائي بعد تثبيت القرارات |

تطبق قاعدة **group isolation**: كل أمثلة `group_id` الواحد تبقى في split واحد. وجود نصين متشابهين من الحالة نفسها في train وtest يسمى leakage ويرفع الأرقام بصورة زائفة.

```python
import csv
from pathlib import Path
from bayan.splits import validate_predefined_splits

with Path("data/sample/bayan_day2_classification.csv").open(
    encoding="utf-8", newline=""
) as file:
    rows = list(csv.DictReader(file))

report = validate_predefined_splits(rows)
assert report["group_overlap"] == 0
print(report)
```

## لماذا Macro-F1؟

Accuracy تحسب نسبة الإجابات الصحيحة كلها. إذا كانت فئة كبيرة تهيمن، قد تبدو مرتفعة مع فشل الفئات الصغيرة.

لكل فئة:

- Precision: كم توقعًا لهذه الفئة كان صحيحًا؟
- Recall: كم مثالًا حقيقيًا لهذه الفئة اكتشفناه؟
- F1: المتوسط التوافقي بين Precision وRecall.
- Macro-F1: متوسط F1 للفئات بأوزان متساوية.

```python
from bayan.metrics import classification_report

report = classification_report(
    ["major", "major", "major", "minor"],
    ["major", "major", "major", "major"],
    labels=["major", "minor"],
)
print(report)
```

ستظهر Accuracy = 0.75، لكن F1 للفئة الصغيرة = 0. هذا هو الفرق الذي نريد رؤيته.

## الإعدادات التي تسجلها

| الإعداد | سؤال القرار |
|---|---|
| checkpoint | هل يغطي اللغات والمهمة؟ |
| learning rate | هل الخطوة صغيرة بما يحافظ على pretraining؟ |
| epochs | هل validation يتحسن أم بدأ الحفظ؟ |
| batch size | هل يناسب الذاكرة؟ |
| max length | كم نصًا سنقص؟ |
| seed | هل يمكن إعادة النتيجة؟ |
| frozen/full encoder | هل هذا CPU fallback أم full fine-tuning؟ |

في notebook نستخدم learning rate صغيرًا وتدريبًا قصيرًا. هذا إعداد تعليمي، وليس قيمة مثالية لكل مشروع.

## CPU وGPU

- GPU متاح: يحدث notebook المشفر والرأس معًا.
- CPU فقط: يجمد المشفر ويدرب الرأس لتبقى الحصة ضمن الوقت.
- كلا المسارين يستخدمان checkpoint مدربًا مسبقًا؛ لكن يجب تسجيل أيهما نُفذ.
- لا تقارن زمن CPU بزمن GPU كأن البيئة واحدة.

## علامات الخطر

| العرض | السبب المحتمل |
|---|---|
| train loss ينخفض وvalidation تسوء | overfitting |
| النتائج ممتازة بصورة غير منطقية | leakage أو labels سهلة |
| كل التوقعات فئة واحدة | imbalance أو mapping خاطئ |
| loss ثابتة | learning rate أو labels أو optimizer |
| النتيجة تتغير كثيرًا | عينة صغيرة أو seed variance |

## دليل الاكتمال

- baseline metric محفوظة.
- تقرير split يساوي `group_overlap=0`.
- training loss رقم finite.
- نوع التدريب `frozen_encoder` أو `full_finetune` موثق.
- النتائج موسومة `MEASURED_SMOKE`.
