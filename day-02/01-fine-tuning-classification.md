# 1. Fine-tuning والتصنيف
# Fine-tuning and Text Classification

<!-- BAYAN_YOUTUBE_START -->
### شاهد الفكرة ثم طبّقها | Video companions

<div class="card youtube-topic youtube-t09"><h3 class="pair"><span class="en" lang="en" dir="ltr">BERT and transfer learning</span><span class="ar" lang="ar" dir="rtl">BERT والتعلم بالنقل</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Understand the encoder and why we adapt a pretrained model.</p><p class="ar" lang="ar" dir="rtl">افهم المشفر ولماذا نكيّف نموذجًا مدربًا مسبقًا.</p></div><p><strong lang="en" dir="ltr">Encoder Models</strong><br><span class="micro">Hugging Face · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=zsfR7eY9Uho" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><p><strong lang="en" dir="ltr">What Is Transfer Learning?</strong><br><span class="micro">Hugging Face · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=BqqfQnyjmgg" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">Which parameters change when the encoder is frozen?</p><p class="ar" lang="ar" dir="rtl">أي المعاملات تتغير عند تجميد المشفر؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<div class="card youtube-topic youtube-t10"><h3 class="pair"><span class="en" lang="en" dir="ltr">Baseline and honest evaluation</span><span class="ar" lang="ar" dir="rtl">خط الأساس والتقييم السليم</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Watch TF-IDF for a baseline, then revisit data splitting and evaluation.</p><p class="ar" lang="ar" dir="rtl">شاهد TF-IDF لخط الأساس ثم راجع تقسيم البيانات والتقييم.</p></div><p><strong lang="en" dir="ltr">3 Vector-based Methods: TF-IDF, BM25, SBERT</strong><br><span class="micro">James Briggs · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=ziiF1eFM3_4" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><details><summary>شرح إضافي عند الحاجة · More explanation when needed</summary><p><strong lang="en" dir="ltr">Machine Learning Fundamentals: Cross Validation</strong><br><span class="micro">StatQuest · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=fSytzGwwBVw" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p></details><div class="callout warning"><div class="pair"><p class="en" lang="en" dir="ltr">Focus on TF-IDF, not a new BM25 task. Cross-validation is background: keep Bayan’s fixed grouped split; do not replace it with random folds.</p><p class="ar" lang="ar" dir="rtl">ركز على TF-IDF؛ لا يُضاف تكليف BM25. التحقق المتقاطع خلفية للفهم؛ حافظ على تقسيم بيان المجمد حسب المجموعات ولا تستبدله بطيات عشوائية.</p></div></div><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">Can the same case group appear in training and test?</p><p class="ar" lang="ar" dir="rtl">هل يجوز ظهور مجموعة الحالة نفسها في التدريب والاختبار؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<div class="card youtube-topic youtube-t11"><h3 class="pair"><span class="en" lang="en" dir="ltr">Fine-tuning with Trainer</span><span class="ar" lang="ar" dir="rtl">الضبط الدقيق باستخدام Trainer</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Recognise the model, datasets, training arguments and evaluation in one training path.</p><p class="ar" lang="ar" dir="rtl">تعرف إلى النموذج والبيانات وإعدادات التدريب والتقييم في مسار واحد.</p></div><p><strong lang="en" dir="ltr">The Trainer API</strong><br><span class="micro">Hugging Face · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=nvBXf7s7vTI" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><div class="callout warning"><div class="pair"><p class="en" lang="en" dir="ltr">APIs may differ by version. Use the notebook’s installation and code, not an older video environment.</p><p class="ar" lang="ar" dir="rtl">قد تختلف الواجهات حسب الإصدار؛ استخدم إعدادات وكود الدفتر لا بيئة الفيديو القديمة.</p></div></div><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">What is the difference between training a task head and inference?</p><p class="ar" lang="ar" dir="rtl">ما الفرق بين تدريب رأس المهمة والاستدلال؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<!-- BAYAN_YOUTUBE_END -->

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
