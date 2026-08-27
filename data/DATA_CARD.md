# بطاقة بيانات بيان | Bayan Data Card

## الغرض

مجموعة نصية اصطناعية صغيرة لتعليم المعالجة والترميز والمهام اللاحقة بالعربية والإنجليزية. لا تمثل خدمة حكومية أو مستخدمين حقيقيين.

## ملفات اليوم الأول | Day 1 files

`data/sample/bayan_day1_sample.csv`

| الحقل | المعنى |
|---|---|
| `case_id` | معرف تعليمي مصطنع |
| `language` | `ar` أو `en` |
| `text` | ملاحظة مصطنعة |
| `topic` | فئة تعليمية أولية |

## الخصوصية

- لا أسماء أو أرقام أو رسائل حقيقية.
- لا تستخدم هذه العينة لادعاء أداء إنتاجي.
- أي أمثلة PII داخل الاختبارات مصطنعة ومخصصة لاختبار masking.
- لا تخلط بيانات حقيقية مع هذا الملف.

## الحدود

12 سجلًا فقط؛ مناسب للشرح والـsmoke tests، وغير مناسب لتدريب نموذج أو استنتاجات إحصائية. الأرقام الناتجة منه توسم `EXAMPLE` إلا إذا قيس تشغيل محدد ووسم `MEASURED`.


## عينات اليوم الثاني | Day 2 samples

| الملف | الحجم | الغرض |
|---|---:|---|
| `data/sample/bayan_day2_classification.csv` | 40 سجلًا | topic classification + baseline + grouped splits |
| `data/sample/bayan_day2_ner.jsonl` | 12 جملة | BIO alignment + NER training smoke |
| `data/sample/bayan_day2_qa.json` | 10 أسئلة | extractive QA + حالتا no-answer |

- جميع النصوص والأرقام المرجعية مصطنعة.
- `group_id` معرف تعليمي لمنع تسرب الأمثلة المتقاربة، وليس معرف شخص.
- الأحجام مخصصة لاختبار صحة pipeline داخل الحصة، وليست لتقدير جودة إنتاجية.
- أي metric من هذه الملفات يجب أن تحمل الوسم `MEASURED_SMOKE`.

## عينات اليوم الثالث | Day 3 samples

| الملف | الحجم | الغرض | وسم الدليل |
|---|---:|---|---|
| `data/sample/bayan_day3_arabic.csv` | 20 سجلًا | profiles عربية + audit لـMSA/Gulf/Arabizi | `COURSE_FIXTURE` |
| `data/sample/bayan_day3_cases.csv` | 24 حالة | corpus بحث عربي/إنجليزي مع summary وresolution | `MEASURED_SMOKE` عند تشغيل النموذج |
| `data/sample/bayan_day3_queries.jsonl` | 18 استعلامًا | validation/test، mono/cross/no-answer، وrelevance labels | `MEASURED_SMOKE` عند تشغيل النموذج |
| `data/sample/bayan_day3_predictions.csv` | 36 تنبؤًا | تعليم Macro-F1 وCI والشرائح والمقارنة الزوجية | `COURSE_FIXTURE` دائمًا |

- `variant` وسم تعليمي يدوي في العينة، وليس مخرج dialect classifier.
- حالات البحث والتنبؤات مصطنعة ولا تمثل خدمة أو مستفيدين حقيقيين.
- يضبط no-answer threshold على validation فقط، ثم يثبت قبل test.
- صغر الشرائح يظهر كـ`SMALL_SLICE` ولا يسمح باستنتاجات سكانية أو إنتاجية.

## Workload اليوم الرابع | Day 4 workload

لا يضيف اليوم الرابع بيانات مواطنين أو dataset جديدة:

- `SYSTEMS_SMOKE` يستخدم ثمانية نصوص اصطناعية مدمجة في Notebook 08 لاختبار export والخدمة فقط؛ لا توجد لها task labels موثوقة.
- Gate D يعيد استخدام **validation الآمنة الخاصة بمشروع المتدرب** في ملف ثابت بأعمدة `example_id,split,language,text,label`.
- يحفظ التقرير عدد الأمثلة وتوزيع اللغات وأطوال tokens وSHA-256 لمحتوى workload.
- frozen test لا يستخدم لاختيار ONNX/INT8؛ يفتح بعد تثبيت القرار وفق عقد المشروع.
- لا يرفع ملف validation إذا كان يحوي بيانات غير عامة؛ دورة بيان تسمح بالبيانات الاصطناعية أو العامة الموثقة فقط.
