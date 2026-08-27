# 3. التقييم وتحليل الأخطاء
# Evaluation and Error Analysis

## الرقم ليس النتيجة كاملة

كل مهمة تحتاج مقياسًا يناسب شكل خطئها:

| المهمة | المقاييس الأساسية | ما يجب عرضه معها |
|---|---|---|
| Classification | Macro-F1 | per-class precision/recall + confusion |
| NER | strict entity-level F1 | per-entity type + boundary errors |
| Extractive QA | EM وtoken F1 | no-answer curve/threshold |
| Retrieval | Recall@k وMRR@k | language/mode slices + no-answer |

Accuracy وحدها قد تخفي الفئات الصغيرة، وtoken accuracy قد تخفي حدود NER، وRecall@50 لا يصف شاشة تعرض ثلاث نتائج.

## Sliced evaluation

المتوسط يضغط مجموعات مختلفة في رقم واحد. نبدأ بمجموعة شرائح ثابتة:

- `language`: ar / en؛
- `variant`: Gulf / MSA / English؛
- `length_bucket`: short / long؛
- class أو entity type؛
- retrieval mode: mono / cross / no-answer.

لا نحذف slice صغيرة. نضع `SMALL_SLICE` ونقول إن الدليل غير كافٍ. عدم القدرة على التقييم نتيجة يجب توثيقها.

## Bootstrap confidence interval

الفكرة مبسطة:

1. اسحب من أمثلة validation مع الإرجاع.
2. احسب metric.
3. كرر مئات أو آلاف المرات.
4. خذ percentiles المناسبة لـ95% CI.

CI واسع يعني أن العينة لا تثبت رقمًا دقيقًا. زيادة عدد مرات bootstrap لا تعوض نقص البيانات؛ هي تعيد استخدام البيانات نفسها.

## مقارنة نموذجين: paired bootstrap

يجب مقارنة النموذجين على **الأمثلة نفسها** وبنفس preprocessing:

```text
diff = metric(model B on sample) - metric(model A on same sample)
```

إذا شملت CI الصفر، فالنتيجة لا تدعم اتجاه فرق ثابت على هذه العينة. الصياغة المهنية:

> الفرق المرصود صغير، وفاصل الفرق المقترن يشمل الصفر؛ لا ندعي تفوق B بعد، ونحتاج بيانات أو تكرارات إضافية.

لا تعني statistical significance أن الفرق مهم عمليًا؛ يجب كذلك مقارنة تكلفة التغيير وتأثيره على المستخدم.

## Behavioural tests

تسأل عن سلوك محدد لا يظهر في المتوسط:

- **Invariance:** إضافة `السلام عليكم` لا تغير topic.
- **Directional:** `تم الحل` مقابل `لم يتم الحل` يجب ألا يجعل unresolved أكثر إيجابية.
- **Minimum functionality:** اسم خدمة واضح داخل قالب يجب أن يستخرج كـSERVICE.

كل اختبار يحمل نصًا متوقع السلوك ونسبة نجاح. إذا ارتفع F1 وانخفض negation pass rate، فهذا regression يحتاج قرارًا قبل النشر.

## Error analysis: اقرأ الأخطاء

الخطوات:

1. اجمع أخطاء validation وbehavioural failures.
2. اقرأ العينة يدويًا؛ لا تستخدم frozen test للتشخيص.
3. ضع taxonomy tag قابلة للتفسير.
4. احسب التكرار والتقاطعات.
5. اربط كل فئة خطأ بإصلاح وتجربة.
6. حول الخطأ المتكرر إلى regression test.

Taxonomy البداية في بيان:

| الوسم | المعنى | إصلاح محتمل |
|---|---|---|
| `label_noise` | الحقيقة نفسها مشكوك فيها | مراجعة annotation guide |
| `class_confusion` | حد الفئات غير واضح | تعريفات/أمثلة أو data |
| `dialect_gap` | ضعف مرتبط بالسجل/اللهجة | بيانات ممثلة أو نموذج مناسب |
| `negation` | سوء فهم النفي | hard examples + behavioural tests |
| `truncation` | معلومة المهمة قُطعت | chunk/length policy |
| `preprocessing` | profile أزال أو غيّر إشارة | تعديل العقد وإعادة الاختبار |
| `entity_boundary` | نوع الكيان صحيح وحدوده خاطئة | alignment/annotation review |
| `hard_or_ambiguous` | أكثر من تفسير معقول | abstention أو policy |

الوسم ليس الحقيقة النهائية؛ هو hypothesis قابلة للاختبار.

## من الأخطاء إلى أولويات

لا يكفي قول «نحتاج نموذجًا أقوى». اكتب:

| الدليل | الفرضية | الإجراء | المقياس المتوقع تحريكه | الكلفة |
|---|---|---|---|---|
| Gulf slice منخفض | بيانات اللهجة غير ممثلة | أضف عينة لهجية متوازنة | Gulf macro-F1 | annotation |
| long أقل من short | truncation/تشتيت | افحص length policy | long slice | compute |
| permit↔digital | تعريف labels متداخل | راجع guide والأمثلة | per-class recall | product/data |

اختر ثلاثة إصلاحات حسب التكرار × أثر الخطأ × كلفة التنفيذ.

## Model card وتقرير التقييم

بطاقة النموذج تحمل:

- intended use وout-of-scope؛
- model/data/preprocessing versions؛
- aggregate وslices وCIs؛
- behavioural rates؛
- known limitations؛
- تاريخ التقييم والمالك.

`EVALUATION_REPORT.md` يجمع الأدلة عبر مكونات بيان ويشرح لماذا نثق أو لا نثق بكل رقم.

## أخطاء شائعة

1. تحليل frozen test ثم تعديل النموذج.
2. مقارنة نموذجين على بيانات أو preprocessing مختلف.
3. عرض delta بلا paired interval.
4. إخفاء slice صغيرة أو ضعيفة.
5. إنشاء taxonomy آليًا بالكامل ثم تسميتها تحليلًا بشريًا.
6. إصلاح الخطأ من دون test يمنع عودته.
7. تقديم `COURSE_FIXTURE` كأنه مخرج نموذج حقيقي.

## التطبيق

نفّذ [Notebook 07 — Evaluation and Error Analysis](../notebooks/07_evaluation_error_analysis.ipynb)، ثم انسخ ناتجك إلى [قالب تقرير التقييم](../templates/EVALUATION_REPORT_TEMPLATE.md) و[قالب بطاقة النموذج](../templates/MODEL_CARD_TEMPLATE.md).

## English recap

Use task-shaped metrics, report meaningful slices, attach uncertainty, compare models on identical examples, probe language behaviours, and read validation errors by hand. Every observed failure should become a testable improvement hypothesis and, when recurring, a regression test.
