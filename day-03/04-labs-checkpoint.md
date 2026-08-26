# 4. مختبرات اليوم الثالث وبوابة Gate C
# Day 3 Labs and Gate C

## الملفات | Files

1. [05 — Arabic NLP](../notebooks/05_arabic_nlp.ipynb)
2. [06 — Semantic Search](../notebooks/06_semantic_search.ipynb)
3. [07 — Evaluation and Error Analysis](../notebooks/07_evaluation_error_analysis.ipynb)
4. [عينة العربية](../data/sample/bayan_day3_arabic.csv)
5. [حالات البحث](../data/sample/bayan_day3_cases.csv)
6. [استعلامات التقييم](../data/sample/bayan_day3_queries.jsonl)
7. [تنبؤات COURSE_FIXTURE](../data/sample/bayan_day3_predictions.csv)

## Lab 4 — العربية

يلزم:

- تشغيل CAMeL Tools 1.6.0 في Core.
- حفظ display copy دون تغيير.
- إنتاج model copy بـprofile معروفة.
- نجاح golden cases للتشكيل والألف والياء المقصورة والتطويل.
- تسجيل توزيع `variant` وشرح لماذا لا يمثل dialect prediction.
- توثيق Arabizi كمسار يحتاج تقييمًا مستقلًا.

النجاح داخل الدفتر:

`DAY3_NOTEBOOK5_CORE=PASS`

Commit:

`feat: add Arabic NLP profiles and tests`

## Lab 5 — البحث الدلالي

يلزم:

- تحميل sentence-transformer متعدد اللغات من المصدر الرسمي.
- إنشاء embeddings فعلية، لا vectors مزروعة.
- التأكد من L2 norm على corpus وquery.
- بناء `FAISS IndexFlatIP` بعدد السجلات الصحيح.
- تشغيل monolingual وcross-lingual queries.
- حساب Recall@3 وMRR@3 بوصف `MEASURED_SMOKE`.
- ضبط threshold على validation فقط، ثم قياس test.
- حفظ manifest وmetrics؛ لا تحفظ weights أو cache في GitHub.

النجاح داخل الدفتر:

`DAY3_NOTEBOOK6_CORE=PASS`

Commit:

`feat: build bilingual semantic search`

## Lab 6 — التقييم وتحليل الأخطاء

يلزم:

- وصف `bayan_day3_predictions.csv` بأنه `COURSE_FIXTURE`.
- حساب Macro-F1 مع 95% bootstrap CI.
- paired comparison لـA وB وعدم ادعاء فرق إذا شملت CI الصفر.
- شرائح language وvariant وlength مع `SMALL_SLICE` حيث يلزم.
- حساب behavioural pass rate على أمثلة معلومة العقد.
- قراءة أخطاء validation ووضع taxonomy يدوية لعينة مختارة.
- كتابة ثلاثة إصلاحات مرتبة بدليل، لا عبارات عامة.

النجاح داخل الدفتر:

`DAY3_NOTEBOOK7_CORE=PASS`

Commit:

`docs: add evaluation and error analysis`

## Gate C — Search & Truth

حدّث مشروعك بهذه الملفات أو ما يعادلها:

```text
notebooks/05_arabic_nlp.ipynb
notebooks/06_semantic_search.ipynb
notebooks/07_evaluation_error_analysis.ipynb
src/bayan/arabic_profiles.py
src/bayan/retrieval.py
src/bayan/eval_stats.py
src/bayan/error_analysis.py
EVALUATION_REPORT.md
MODEL_CARD.md
DECISIONS.md
PROGRESS.md
reports/search_manifest.json
reports/retrieval_metrics.json
```

استخدم [قالب تقرير التقييم](../templates/EVALUATION_REPORT_TEMPLATE.md) و[قالب بطاقة النموذج](../templates/MODEL_CARD_TEMPLATE.md)، ثم استبدل جميع placeholders بقيمك.

## ما يضاف إلى DECISIONS.md

### Arabic profile

- profile + version + backend.
- ما الذي تغير وما الذي حُفظ؟
- لماذا لا تستخدم profile واحدة لكل checkpoints؟

### Semantic search

- embedding model + model card + license.
- index type ولماذا Flat مناسب للحجم الحالي.
- k وthreshold ومكان ضبطهما.
- Recall/MRR والشرائح بوصف `MEASURED_SMOKE`.

### Evaluation

- headline metric لكل مهمة.
- slices المختارة والسبب.
- CI verdict بلغة مهنية.
- top-3 fixes من الأخطاء.

## شروط عبور Gate C

- [ ] دفاتر 05 و06 و07 موجودة بالأسماء المطلوبة.
- [ ] علامات Core الثلاث ظاهرة بعد Run all.
- [ ] اختبارات المصدر خضراء.
- [ ] CAMeL Tools مستخدمة في موضع مفيد، وليست اسمًا في README فقط.
- [ ] corpus وquery vectors مطبعة L2.
- [ ] FAISS manifest يطابق عدد vectors وبعدها.
- [ ] Recall@k وMRR@k مقاسان على relevance labels.
- [ ] no-answer threshold لم يضبط على test.
- [ ] slices وCIs ظاهرة مع تحذير الحجم.
- [ ] error analysis على validation لا frozen test.
- [ ] النتائج موسومة `MEASURED_SMOKE` أو `COURSE_FIXTURE` بدقة.
- [ ] لا weights أو cache أو PII أو أسرار في GitHub.
- [ ] commits عامة وروابطها في `PROGRESS.md`.

## نقطة استعادة الطوارئ

| المشكلة | الإجراء الأول | البديل الآمن |
|---|---|---|
| فشل CAMeL Tools install | Runtime جديد وشغّل setup وحدها | أكمل الشرح؛ لا تعتبر stdlib بديل Gate C |
| تنزيل sentence model بطيء | محاولة واحدة ثم افحص الاتصال | انتقل إلى Notebook 07 وارجع للبحث لاحقًا |
| FAISS import fail | أعد تشغيل runtime بعد pip | استخدم exact NumPy oracle للتشخيص فقط، لا Gate PASS |
| لا GPU | لا تغيّر شيئًا | نموذج البحث يعمل على CPU |
| OOM | أغلِق نموذج اليوم الثاني وruntime قديم | batch أصغر؛ corpus اليوم 24 فقط |
| cross-encoder بطيء | أوقف Explore | Core لا يحتاج reranker |
| CI واسعة | لا تزد n_boot لإخفائها | وثق محدودية العينة واجمع بيانات أكثر |
| تأخر الصف 15 دقيقة | أوقف Explore/Distinction | حافظ على الدفاتر الثلاث وGate C |

## Exit ticket

أجب دون كود:

1. لماذا نحفظ display copy مستقلة؟
2. لماذا يجب تطبيع corpus وquery معًا؟
3. ما الفرق بين Recall@k وMRR@k؟
4. ماذا يعني أن CI للفرق تشمل الصفر؟
5. لماذا نجري error analysis على validation؟
6. ما الذي يجبرك على إعادة بناء FAISS index؟

## التالي

انتقل إلى [اليوم الرابع](../day-04/README.md): سنقيس latency والذاكرة، نقارن baseline وoptimized، نبني خدمة محلية مختبرة، ثم نجمع مشروع بيان ونجهزه للتسليم النهائي.
