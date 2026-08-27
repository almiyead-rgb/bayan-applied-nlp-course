# نتائج التشغيل الموثقة | Verified Runs

**آخر تدقيق:** 27 أغسطس 2026 (UTC)<br>
**البيئة المرجعية:** Linux CPU، Python `3.12.13`، PyTorch `2.13.0`، Transformers `5.15.1`<br>
**النطاق:** تشغيل خلايا Python بالترتيب في عملية معزولة نظيفة، وحفظ المخرجات داخل الدفاتر المنشورة.

هذه الصفحة تجيب عن سؤالين مختلفين:

1. **هل الكود يعمل؟** نعم؛ الدفاتر التسعة نُفذت بالترتيب، بلا Error outputs أو `stderr` محفوظ، وظهرت علامات النجاح الخاصة بكل دفتر.
2. **هل الأرقام أداء إنتاجي؟** لا؛ بيانات الدورة اصطناعية ومصغرة. الأرقام موسومة `MEASURED_SMOKE` أو `SYSTEMS_SMOKE` ولا يجوز تعميمها.

> تستطيع المدربة عرض المخرجات المحفوظة مباشرةً أثناء الشرح، فلا يلزم انتظار تنزيل نموذج أو تدريب حي. ينفذ المتدرب نسخته لاحقًا لإنتاج دليله الشخصي، وقد تختلف أزمنة CPU/Colab مع العتاد والحمل.

## لوحة النتائج | Evidence board

| # | الدفتر | دليل التنفيذ المحفوظ | حد الادعاء |
|---:|---|---|---|
| 00 | [Runtime Doctor](../notebooks/00_runtime_doctor.ipynb) | `BAYAN_ENV_READY = True`؛ وفحوص GitHub Raw وPyPI وHugging Face نجحت | فحص البيئة، لا جودة نموذج |
| 01 | [Text Processing & Tokenisation](../notebooks/01_text_processing_tokenization.ipynb) | Unicode، عقد النسختين، PII masking، spaCy segmentation، WordPiece، fertility، embeddings؛ `DAY1_NOTEBOOK1_CORE=PASS` | أمثلة تعليمية واختبارات عقود |
| 02 | [Attention & Transformers](../notebooks/02_attention_transformers.ipynb) | تدقيق mBERT=`177,853,440` وCAMeLBERT‑DA=`109,081,344` معاملًا؛ NumPy/PyTorch parity؛ forward pass حقيقي بـ`134,734,080` معاملًا؛ attention shape `(2, 12, 10, 10)`؛ خريطة رأس محفوظة | التدقيقان الأولان معماريان من config الرسمية؛ والخريطة وصف weights وليست تفسيرًا سببيًا |
| 03 | [Text Classification](../notebooks/03_text_classification.ipynb) | `72` خطوة تدريب؛ epoch مختار=`9`؛ test Macro‑F1: TF‑IDF=`0.7333`، Transformer=`0.8667` | `MEASURED_SMOKE` على بيانات اصطناعية صغيرة |
| 04 | [NER & QA](../notebooks/04_ner_and_qa.ipynb) | NER: `48` خطوة وentity F1=`0.5714`؛ QA: `3` خطوات؛ alignment و`-100` وstrict boundaries وspan/no-answer اختبارات ناجحة | جودة NER/QA ليست تقديرًا إنتاجيًا؛ QA model span smoke فقط |
| 05 | [Arabic NLP](../notebooks/05_arabic_nlp.ipynb) | CAMeL Tools golden tests؛ نموذجان × `40` خطوة؛ Gulf test Macro‑F1: multilingual=`0.0000`، CAMeLBERT‑DA=`0.6667` | أربع حالات Gulf وبذرة واحدة؛ اتجاه وصفي فقط |
| 06 | [Semantic Search](../notebooks/06_semantic_search.ipynb) | FAISS + embeddings حقيقية؛ Recall@3=`1.0000`؛ MRR@3 قبل/بعد rerank=`0.6667 → 0.7222`؛ no-answer=`1.0000` | ستة استعلامات test قابلة للإجابة؛ `MEASURED_SMOKE` |
| 07 | [Evaluation & Error Analysis](../notebooks/07_evaluation_error_analysis.ipynb) | slices وbootstrap وbehavioural tests وtaxonomy؛ paired CI=`[-0.1047, 0.0996]` يرفض ادعاء اتجاهي | التنبؤات `COURSE_FIXTURE` لتعليم المنهج |
| 08 | [Optimisation & Serving](../notebooks/08_optimization_serving.ipynb) | ONNX checker؛ FP32 agreement=`1.0`؛ حجم `16.788 MiB → 4.272 MiB` INT8؛ p95 model-only `9.91 → 6.42 → 1.73 ms`؛ FastAPI/canaries PASS | `SYSTEMS_SMOKE` برأس عشوائي English-only؛ ليس قرار Gate D لمشروع الطالب |

## كيف تقرأ الأرقام؟

- `MEASURED_SMOKE`: قياس فعلي على fixture صغيرة؛ يثبت أن pipeline والمقياس يعملان، لا أنهما يمثلان جمهورًا أو خدمة حقيقية.
- `SYSTEMS_SMOKE`: يثبت export/quantisation/API والعقود التقنية فقط، ولا يقيس جودة مهمة بيان.
- `COURSE_FIXTURE`: بيانات أو تنبؤات موزعة لتعليم التقييم، وليست مخرجات model run خفي.
- أي نتيجة latency مرتبطة بالبيئة والعمل المحددين؛ لا تُقارن بأرقام جهاز آخر من دون workload وwarm-up وrepetitions نفسها.

## سياسة العرض داخل الدرس

1. افتح الدفتر من GitHub واعرض المخرج المحفوظ أولًا.
2. اشرح ما يثبته المخرج وما لا يثبته.
3. شغّل خلية قصيرة فقط إذا كان ذلك يخدم سؤالًا تعليميًا؛ لا تنتظر تنزيل checkpoint أمام الصف.
4. إذا تعطل اتصال الطالب، يستخدم المخرج المرجعي لفهم الخطوة، ثم يعيد التشغيل في نسخته عند عودة الاتصال.
5. لا ينسخ الطالب الرقم المرجعي إلى تقريره على أنه قياسه؛ يجب أن يسجل بيئته وcommit ونتيجته.

## فحوص النزاهة التقنية

- كل code cell يحمل `execution_count` متسلسلًا.
- كل cell يحمل معرفًا فريدًا متوافقًا مع nbformat 4.5+.
- لا توجد Error outputs أو tracebacks أو `stderr` محفوظة.
- اسم المؤلفة في metadata لجميع الدفاتر: `Meaad Al-Marri`.
- لا توجد مفاتيح API أو بيانات اعتماد أو أوزان نماذج ضمن المستودع.
- يفشل GitHub Actions إذا حُذفت النتائج أو اختفت علامة النجاح أو ظهر Error output.

## تشغيل Colab للمتدرب

روابط **Open in Colab** داخل كل دفتر تشير إلى فرع `main`. أول تشغيل قد يحتاج تنزيل checkpoints مفتوحة المصدر؛ لا يحتاج API key أو خدمة مدفوعة. نجاح الدفتر في البيئة المرجعية لا يضمن توفر GPU مجاني، وCPU هو مسار الاستمرارية المعتمد.
