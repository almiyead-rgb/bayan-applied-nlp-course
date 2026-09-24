# 3. التقييم وتحليل الأخطاء
# Evaluation and Error Analysis

<!-- BAYAN_YOUTUBE_START -->
### شاهد الفكرة ثم طبّقها | Video companions

<div class="card youtube-topic youtube-t18"><h3 class="pair"><span class="en" lang="en" dir="ltr">Task metrics and retrieval ranking</span><span class="ar" lang="ar" dir="rtl">مقاييس المهام وترتيب البحث</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Separate classification quality from retrieval and ranking quality.</p><p class="ar" lang="ar" dir="rtl">افصل جودة التصنيف عن جودة الاسترجاع والترتيب.</p></div><p><strong lang="en" dir="ltr">Precision, Recall and F1 Score</strong><br><span class="micro">codebasics · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=2osIZ-dSPGE" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><p><strong lang="en" dir="ltr">Evaluation Measures for Search and Recommender Systems</strong><br><span class="micro">James Briggs · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=BD9TkvEsKwM" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><div class="callout warning"><div class="pair"><p class="en" lang="en" dir="ltr">Recall@k and MRR are the focus. Additional ranking metrics shown are enrichment only.</p><p class="ar" lang="ar" dir="rtl">التركيز على Recall@k وMRR؛ المقاييس الإضافية للتوسع فقط.</p></div></div><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">How can Recall@k stay the same while MRR changes?</p><p class="ar" lang="ar" dir="rtl">كيف يبقى Recall@k ثابتًا بينما يتغير MRR؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<div class="card youtube-topic youtube-t19"><h3 class="pair"><span class="en" lang="en" dir="ltr">Errors, slices and uncertainty</span><span class="ar" lang="ar" dir="rtl">الأخطاء والشرائح وعدم اليقين</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Start with error analysis; use the support clips for bootstrap and confidence intervals.</p><p class="ar" lang="ar" dir="rtl">ابدأ بتحليل الأخطاء واستعن بالمقاطع الداعمة لإعادة أخذ العينات وفترات الثقة.</p></div><p><strong lang="en" dir="ltr">Carrying Out Error Analysis</strong><br><span class="micro">DeepLearning.AI · Andrew Ng · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=JoAxZsdw_3w" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><details><summary>شرح إضافي عند الحاجة · More explanation when needed</summary><p><strong lang="en" dir="ltr">Bootstrapping: Main Ideas</strong><br><span class="micro">StatQuest · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=Xz0x-8-cgaQ" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><p><strong lang="en" dir="ltr">Confidence Intervals, Clearly Explained!</strong><br><span class="micro">StatQuest · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=TqOeMYtOc1w" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p></details><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">Which three errors would you investigate first, and what evidence supports that order?</p><p class="ar" lang="ar" dir="rtl">ما الأخطاء الثلاثة التي تفحصها أولًا، وما دليل ترتيبها؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<!-- BAYAN_YOUTUBE_END -->

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
