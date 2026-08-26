# 5. مختبرات اليوم الثاني وبوابة Gate B
# Day 2 Labs and Gate B

## الملفات

1. [03 — Text Classification](../notebooks/03_text_classification.ipynb)
2. [04 — NER and QA](../notebooks/04_ner_and_qa.ipynb)
3. [بيانات التصنيف](../data/sample/bayan_day2_classification.csv)
4. [بيانات NER](../data/sample/bayan_day2_ner.jsonl)
5. [بيانات QA](../data/sample/bayan_day2_qa.json)

## Lab 3A — التصنيف

يلزم:

- تشغيل split validation وإثبات zero overlap.
- تشغيل TF-IDF baseline.
- تنفيذ Transformer optimizer step فعلية.
- تسجيل device وfrozen/full وseed.
- تسجيل validation وtest metrics بوصف `MEASURED_SMOKE`.
- تفسير فئة واحدة أخطأ بها النموذج أو baseline.

النجاح داخل الدفتر:

`DAY2_NOTEBOOK3_CORE=PASS`

## Lab 3B — NER وQA

يلزم:

- محاذاة labels مع `word_ids()`.
- `-100` عند special/continuation tokens.
- تنفيذ NER optimizer step.
- قياس entity-level لا token accuracy فقط.
- تجهيز QA start/end positions.
- تنفيذ QA optimizer step.
- نجاح valid-span وno-answer tests.

النجاح داخل الدفتر:

`DAY2_NOTEBOOK4_CORE=PASS`

## Gate B — Tasks

حدّث مشروعك:

```text
notebooks/03_text_classification.ipynb
notebooks/04_ner_and_qa.ipynb
src/bayan/splits.py
src/bayan/metrics.py
src/bayan/ner_alignment.py
src/bayan/qa_postprocess.py
DECISIONS.md
PROGRESS.md
```

أضف إلى `DECISIONS.md`:

- checkpoint والسبب.
- نوع التنفيذ: frozen أو full.
- split strategy ودليل عدم التسرب.
- baseline وTransformer metric.
- NER alignment policy.
- QA null policy.
- ما الذي لا تستطيع العينة الصغيرة إثباته.

## Commit المطلوب

`feat: add classification ner and qa pipelines`

ثم ضع رابط commit في `PROGRESS.md` عند Gate B.

## شروط عبور Gate B

- [ ] الدفتران موجودان بالاسم المطلوب.
- [ ] علامتا PASS ظاهرتان بعد Run all.
- [ ] 13 اختبار Day 2 خضراء.
- [ ] zero group overlap.
- [ ] baseline موجودة.
- [ ] classification/NER/QA training smoke تعمل.
- [ ] no-answer يعيد `None`.
- [ ] النتائج موسومة `MEASURED_SMOKE`.
- [ ] لا weights أو cache أو PII في GitHub.
- [ ] commit عام ورابط صالح.

## إذا نفد الوقت

لا تحذف مهمة:

1. Core فقط.
2. CPU: encoder مجمد.
3. خطوة تدريب واحدة بدل epochs إضافية.
4. أوقف Explore وDistinction.
5. احفظ Drive ثم commit.

## Exit ticket

أجب دون كود:

1. لماذا baseline قبل Transformer؟
2. ماذا يمنع `group_id`؟
3. لماذا نستخدم `-100` في NER؟
4. لماذا لا يجوز أن يستخرج QA جوابًا دائمًا؟
5. ما الفرق بين `MEASURED_SMOKE` ونتيجة إنتاجية؟

## التالي

في [اليوم الثالث](../COURSE_GUIDE.md#اليوم-3--العربية-البحث-والحقيقة) سنعمق العربية، ونبني البحث الدلالي، ثم نقيم النتائج حسب الشرائح ونحلل الأخطاء.
