# طريقة تسليم مشروع بيان | Bayan Submission

## قاعدة التسليم

يسلّم كل متدرب **مستودع GitHub عامًا باسمه**، حتى عند التعاون في الأنشطة الصفية. الرابط هو دليل المشروع؛ ملفات Drive وحدها ليست تسليمًا.

## اسم المستودع

`bayan-nlp-YOUR-GITHUB-USERNAME`

مثال:

`bayan-nlp-meaad-example`

## الملفات الإلزامية

```text
README.md
STUDENT_PROFILE.md
PROGRESS.md
DECISIONS.md
BENCHMARKS.md
EVALUATION_REPORT.md
MODEL_CARD.md
DATA_CARD.md
PROJECT_SUMMARY.json
SUBMISSION.yml
notebooks/
src/bayan/
tests/
reports/
sample_outputs/
```

### دفاتر Colab التسعة

```text
00_runtime_doctor.ipynb
01_text_processing_tokenization.ipynb
02_attention_transformers.ipynb
03_text_classification.ipynb
04_ner_and_qa.ipynb
05_arabic_nlp.ipynb
06_semantic_search.ipynb
07_evaluation_error_analysis.ipynb
08_optimization_serving.ipynb
```

لا تغيّر أسماء الملفات؛ يستخدم فاحص التسليم هذه المسارات.

## الـCommits المطلوبة

| البوابة | الرسالة المقترحة |
|---|---|
| تجهيز البيئة | `chore: pass runtime doctor` |
| Lab 1 | `feat: complete preprocessing and tokenization` |
| Lab 2 | `feat: explain attention and transformer flow` |
| Lab 3 | `feat: add classification ner and qa pipelines` |
| Lab 4 | `feat: add Arabic NLP profiles and tests` |
| Lab 5 | `feat: build bilingual semantic search` |
| Lab 6 | `docs: add evaluation and error analysis` |
| Lab 7 | `perf: add optimized serving benchmark` |
| المشروع النهائي | `release: complete Bayan submission v1.0` |

يجوز وجود commits إضافية. المطلوب أن يظهر تقدم حقيقي، لا رفع كل شيء مرة واحدة في النهاية.

## ما يوضع في Drive ولا يوضع في GitHub

- أوزان النماذج الكبيرة.
- checkpoints المؤقتة.
- caches والبيانات الخام الثقيلة.
- artefacts يمكن إعادة إنتاجها.

وثق داخل README: اسم النموذج، المصدر، hash/نسخة checkpoint، وخطوات إعادة الإنتاج. لا تضع رابط Drive عامًا إذا كان يكشف ملفات أخرى.

## PROJECT_SUMMARY.json

يجب أن يكون JSON صالحًا ويحتوي على الأقل:

```json
{
  "student_github": "YOUR_USERNAME",
  "repository_url": "https://github.com/YOUR_USERNAME/bayan-nlp-YOUR_USERNAME",
  "languages": ["ar", "en"],
  "tasks": ["classification", "sentiment", "ner", "qa", "semantic_search"],
  "extension": {
    "name": "batch endpoint",
    "evidence": "BENCHMARKS.md#batch-endpoint"
  },
  "benchmark_mode": "PROJECT_ARTIFACT",
  "final_tag": "submission-v1.0",
  "privacy_check": true,
  "tests_passed": true
}
```

استبدل القيم بمشروعك. لا تكتب `true` ما لم يتحقق الشرط.

`benchmark_mode` لا يصبح `PROJECT_ARTIFACT` إلا بعد إعادة Notebook 08 على checkpoint بيان المضبوط وworkload المشروع. مسار `SYSTEMS_SMOKE` يثبت البنية فقط ويرفضه الفاحص في التسليم النهائي.

## SUBMISSION.yml

```yaml
course: bayan-applied-nlp
student_github: YOUR_USERNAME
repository: https://github.com/YOUR_USERNAME/bayan-nlp-YOUR_USERNAME
default_branch: main
final_tag: submission-v1.0
runtime: google-colab
visibility: public
```

استخدم spaces لا tabs.

## الفحص قبل الوسم النهائي

انسخ [قالب PROJECT_SUMMARY](../../templates/PROJECT_SUMMARY.template.json) و[قالب SUBMISSION](../../templates/SUBMISSION.template.yml)، ثم شغّل:

```bash
PYTHONPATH=src python scripts/validate_submission.py . \
  --json-report reports/submission_validation.json
```

يجب أن تظهر `BAYAN_SUBMISSION_VALIDATOR=PASS`. الفاحص محلي ولا يستطيع إثبات visibility؛ افتح الروابط في نافذة خاصة أيضًا.

- [ ] جميع الروابط تعمل في نافذة خاصة بلا صلاحيات إضافية.
- [ ] README يشرح التشغيل من الصفر.
- [ ] notebooks تفتح وتعمل بالترتيب.
- [ ] نتائجك موسومة `MEASURED`.
- [ ] لا password أو token أو email شخصي أو PII.
- [ ] الاختبارات خضراء.
- [ ] `PROJECT_SUMMARY.json` صالح.
- [ ] `SUBMISSION.yml` صالح.
- [ ] لم تُرفع أوزان كبيرة.
- [ ] frozen test لم يستخدم في tuning.
- [ ] limitations مكتوبة بوضوح.

## إنشاء الوسم النهائي

1. افتح Releases.
2. اختر Draft a new release.
3. أنشئ tag `submission-v1.0` على `main`.
4. العنوان: `Bayan NLP Final Submission`.
5. انشر الإصدار.
6. سلّم رابط الـrelease بالطريقة التي تعلنها الجهة المنظمة.

بعد إنشاء tag، اسحب النسخة النهائية ثم أعد الفحص:

```bash
PYTHONPATH=src python scripts/validate_submission.py . --require-tag
```

بعد الوسم لا تعدّل النتائج وتدّعي أنها النسخة نفسها؛ أي تصحيح لاحق يحتاج tag جديدًا إذا سُمح بإعادة التسليم.
