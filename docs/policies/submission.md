# طريقة تسليم مشروع بيان | Bayan Submission

## قاعدة التسليم

يسلّم كل متدرب **مستودع GitHub عامًا بحسابه الشخصي**، حتى عند التعاون في الأنشطة الصفية. الرابط هو دليل المشروع؛ ملفات Drive وحدها ليست تسليمًا.

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
PRESENTATION.md
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
- [ ] نتائجك موسومة وفق حقيقتها: `MEASURED_SMOKE` للعينة المصغرة وقياس المشروع الفعلي موثق؛ لا تنسخ نتائج مرجعية.
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

## سياسة التقييم مرة واحدة | One final assessment

**يسلّم المتدرب مرة واحدة للتصحيح. لا تقبل تعديلات أو إعادة تسليم بعد إرسال الرابط النهائي إلى المدربة.** قبل الإرسال يجوز الفحص والإصلاح والتجربة؛ لا ترسل نسخة تجريبية للتقييم ثم تطلب استبدالها.

**One final submission is assessed once. No edited replacement or resubmission is accepted after the final hand-in.** Before sending, test and correct your work as needed.

أرسل عبر قناة التسليم الخاصة المعلنة: رابط المستودع، ورابط إصدار `submission-v1.0`، وبصمة **Commit SHA الكاملة** التي يشير إليها الوسم، ورابط `PRESENTATION.md` أو العرض. لا ترسل رابط `file:///C:/...` أو رابط المدربة أو رابطًا خاصًا يتطلب طلب صلاحية.

Send the repository URL, `submission-v1.0` release URL, the full commit SHA resolved by the tag, and the presentation link through the announced private hand-in route. Do not submit a local computer path, the instructor's URL or an inaccessible private share.

تثبت المدربة نسخة SHA المستلمة وقت التسليم. قد يسمح GitHub تقنيًا بتعديل `main` أو نقل الوسم، لكن التعديل اللاحق **لا يدخل في التصحيح**؛ المرجع هو SHA المسجل لا رأس الفرع المتغير. حفظ الإقرار ليس قفلًا تقنيًا للمستودع.

The instructor captures the received SHA. GitHub may technically allow branch changes or tag moves, but later changes are outside assessment. The recorded commit, not the moving branch head, defines the assessed version. An acknowledgement is not a technical repository lock.

إقرار التسليم: «راجعت المتطلبات الإدارية والتقنية والعرض، وهذه نسختي النهائية التي تُقيّم مرة واحدة، وأفهم أنه لا يسمح باستبدالها أو تعديلها لأغراض إعادة التصحيح بعد الإرسال».

Acknowledgement: “I reviewed the administrative, technical and presentation requirements. This is my final version for one assessment; I understand that no replacement or amendment for regrading is accepted after hand-in.”

## تحقق من أن الوسم يطابق نسختك | Verify the tag target

في نسخة Git المستنسخة حديثًا من مستودعك، وبعد نشر الإصدار:

```bash
git fetch origin --tags
python scripts/preflight_submission.py . --require-tag
python scripts/validate_submission.py . --require-tag
git rev-parse HEAD
git rev-parse 'submission-v1.0^{commit}'
```

يجب أن تتطابق البصمتان عند تثبيت النسخة النهائية. لا تعِد كتابة نتيجة الفحص النهائية داخل الوسم نفسه بعد إنشائه؛ أرسل SHA والروابط الصحيحة. الفاحص يفحص النسخة المحلية؛ راجع الإصدار العام أيضًا.

Both SHAs must match for the final frozen version. Do not mutate the release to insert a post-tag report; hand in the verified SHA and links. Local checks do not replace a public release check.

[دليل المبتدئ للتشغيل والحفظ](../learner-workflow.md) · [قائمة الفحص](../pre-submission-checklist.md) · [سُلّم 100 درجة](assessment-and-completion.md) · [العرض](../presentation-guide.md)
