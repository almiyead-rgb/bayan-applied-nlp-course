# 5. Lab 7 وبوابتا Gate D وGate E
# Lab 7, Gate D, and Gate E

## الملفات | Files

1. [08 — Optimisation and Serving](../notebooks/08_optimization_serving.ipynb)
2. [قالب BENCHMARKS](../templates/BENCHMARKS_TEMPLATE.md)
3. [قالب القرارات](../templates/DECISIONS_TEMPLATE.md)
4. [قالب التقدم](../templates/PROGRESS_TEMPLATE.md)
5. [قالب ملخص JSON](../templates/PROJECT_SUMMARY.template.json)
6. [قالب SUBMISSION.yml](../templates/SUBMISSION.template.yml)
7. [فاحص التسليم](../scripts/validate_submission.py)

## Lab 7 — تحسين الاستدلال والخدمة

يلزم في Notebook 08:

- تسجيل environment وdevice والإصدارات.
- كتابة budget قبل قياس candidate.
- فصل `SYSTEMS_SMOKE` عن `PROJECT_ARTIFACT`.
- baseline بعد warm-up وبـ30 تكرارًا على الأقل.
- p50/p95/p99 وthroughput وRSS observed peak.
- length audit وdynamic padding/batching rationale.
- ONNX checker + ORT session + numerical/prediction parity.
- dynamic INT8 candidate أو فشل موثق لا يخفى.
- quality tax على الأمثلة نفسها.
- FastAPI `/health` و`/v1/classify`.
- TestClient لطلب عربي وإنجليزي وطلب invalid.
- canaries وmanifest/version check.
- حفظ تقارير نصية/JSON صغيرة فقط، لا artefacts.

نجاح مسار المختبر داخل الدفتر:

`DAY4_NOTEBOOK8_CORE=PASS`

Commit:

`perf: add optimized serving benchmark`

هذه العلامة تثبت Core systems path. لا تكفي وحدها لعبور Gate D؛ يجب استبدال مصدر الاختبار بنموذج بيان الفعلي وتحديث التقارير.

## Gate D — Ship

### أدلة artefact المشروع

- [ ] `artefact_role = PROJECT_ARTIFACT` في BENCHMARKS.
- [ ] model/revision وpreprocessing version وlabel map موثقة.
- [ ] workload ثنائي اللغة ثابت وله IDs.
- [ ] baseline وcandidate قيسا على الجهاز والعمل نفسيهما.
- [ ] metric المهمة قبل/بعد وquality tax ظاهرة.
- [ ] القرار Adopt/Reject/Rollback يطابق budget.
- [ ] FP32 reference أو reproduction path محفوظ خارج GitHub.
- [ ] API smoke يستخدم artefact المختار لا fixture مجهولة.
- [ ] canaries عربية وإنجليزية تمر.
- [ ] الاختبارات كلها خضراء.

ملفات Gate D المقترحة:

```text
notebooks/08_optimization_serving.ipynb
src/bayan/benchmarking.py
src/bayan/serving.py
tests/test_benchmarking.py
tests/test_serving.py
reports/benchmark_results.json
reports/service_smoke.json
BENCHMARKS.md
DECISIONS.md
PROGRESS.md
```

لا ترفع ملفات `.onnx` أو weights. ارفع report وhash وطريقة إعادة الإنشاء.

## Gate E — Submit

### 1) جهز ملفات العقد

انسخ القوالب إلى الأسماء النهائية واستبدل كل `FILL_ME`/`YOUR_USERNAME`:

```bash
cp templates/PROJECT_SUMMARY.template.json PROJECT_SUMMARY.json
cp templates/SUBMISSION.template.yml SUBMISSION.yml
```

إذا كان مستودعك لا يحتوي مجلد `templates`، انسخ محتوى القالب من مستودع الدورة يدويًا.

في `PROJECT_SUMMARY.json` يجب أن تكون:

```json
"benchmark_mode": "PROJECT_ARTIFACT"
```

### 2) شغّل الفاحص قبل tag

```bash
PYTHONPATH=src python scripts/validate_submission.py . \
  --json-report reports/submission_validation.json
```

النجاح:

`BAYAN_SUBMISSION_VALIDATOR=PASS`

سيبقى تحذيران يدويان: التحقق من visibility/links في نافذة خاصة، وإعادة الفحص بعد tag.

### 3) تحقق يدويًا

- [ ] نسبة الحضور مستوفاة وفق الجهة المنظمة.
- [ ] الدرجة/التقييمات المطلوبة مكتملة.
- [ ] المستودع عام ويفتح دون تسجيل دخول خاص.
- [ ] روابط Colab التسعة تعمل.
- [ ] Runtime نظيف: Restart session and run all.
- [ ] لا secrets أو PII أو بريد شخصي غير لازم.
- [ ] نتائج test لم تستخدم للتعديل المتكرر.
- [ ] limitations صريحة.
- [ ] المراجعة النظيرة عولجت أو رُفضت بسبب موثق.

### 4) جمّد الإصدار

Commit النهائي:

```text
release: complete Bayan submission v1.0
```

ثم أنشئ GitHub Release/tag باسم دقيق:

`submission-v1.0`

العنوان:

`Bayan NLP Final Submission`

### 5) أعد الفحص النهائي

بعد pull/clone يشمل tag:

```bash
PYTHONPATH=src python scripts/validate_submission.py . --require-tag
```

احتفظ برابط الـrelease ورابط commit النهائي ونتيجة الفاحص.

## شروط عبور Gate E

- [ ] جميع ملفات التسليم الإلزامية موجودة وغير فارغة.
- [ ] notebooks التسعة بأسمائها وعلامات Core.
- [ ] `PROJECT_SUMMARY.json` JSON صالح و`benchmark_mode` نهائي.
- [ ] `SUBMISSION.yml` flat YAML صالح بلا tabs.
- [ ] لا placeholders أو weights أو secrets أو ملف أكبر من حد الدورة.
- [ ] فاحص pre-tag ناجح.
- [ ] demo/review مكتمل وفق تنظيم المجموعة.
- [ ] commit الإصدار موجود.
- [ ] tag `submission-v1.0` موجود.
- [ ] فاحص `--require-tag` ناجح.
- [ ] رابط GitHub العام سلّم بالطريقة المعلنة.

## نقطة استعادة الطوارئ

| المشكلة | الإجراء الأول | البديل الآمن |
|---|---|---|
| export فشل | اقرأ أول error وافحص opset/input names | استخدم FP32 وأوثق blocker؛ لا ترفع PASS مزيفًا |
| INT8 أبطأ | ثبّت workload وأعد warm-up | ارفض INT8 واحتفظ بـFP32 |
| parity فشلت | نفس encoded inputs و`eval()` | أوقف قرار النشر حتى تتطابق المخرجات |
| Colab OOM | أعد runtime وأغلق نماذج الأيام السابقة | checkpoint أصغر لمسار Systems Smoke ثم المشروع على batches أصغر |
| TestClient import fail | ثبت `requirements-day4.txt` ثم restart | اختبر دالة العقد مؤقتًا، لكن Gate D يحتاج HTTP smoke |
| validator: placeholder | افتح الملف المذكور واستبدل القيمة | لا تعطل الفحص ولا تغير قواعده |
| validator: artefact | احذف الوزن من Git history قبل tag ووثق hash | اطلب مساعدة قبل أي rewrite إن كان push تم |
| رابط لا يعمل | افتح نافذة خاصة وصحح المسار/case | ضع رابط commit ثابتًا مؤقتًا ثم أصلح README |
| انقطع runtime قبل العرض | استخدم sample output آمنًا + آخر report | اشرح أنه evidence محفوظ، ولا تختلق تشغيلًا حيًا |
| تأخر الصف 15 دقيقة | أوقف Explore والعروض العامة الكاملة | مراجعة متوازية + validator + tag أولًا |

## Exit ticket

أجب دون كود:

1. لماذا لا يكفي المتوسط لقياس latency؟
2. كيف يمكن أن تزيد throughput بينما تسوء latency الفردية؟
3. ما الفرق بين ONNX وONNX Runtime؟
4. لماذا لا يعني ملف INT8 أصغر أنه أفضل؟
5. ما الذي تكشفه startup canary؟
6. لماذا لا يكفي `SYSTEMS_SMOKE` للتسليم؟
7. ما الدليل الذي يجعلك تثق بأهم رقم في مشروعك؟

## اكتمل المسار

بعد Gate E تكون قد بنيت مشروعًا ثنائي اللغة، قسته، اختبرته، وثقته، وأصدرته من مستودع عام قابل للمراجعة—وهو الدليل النهائي على نواتج البرنامج السبعة.
