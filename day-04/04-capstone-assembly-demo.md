# 4. تجميع مشروع بيان والعرض
# Bayan Assembly, Peer Review, and Demo

## لا نعيد البناء في الساعة الأخيرة

التجميع يعني ربط أدلة الأيام الأربعة في مسار يستطيع مراجع جديد تتبعه:

```text
problem → data boundary → preprocessing → tasks → search
→ evaluation → optimisation → service → limitations → reproduction
```

كل claim في README يجب أن يقود إلى ملف أو metric أو test، لا إلى وصف شفهي.

## خريطة الدليل | Evidence map

| السؤال الذي سيسأله المراجع | مكان الإجابة |
|---|---|
| ما المشكلة وما الذي لا يحله المشروع؟ | `README.md` + `MODEL_CARD.md` |
| ما مصدر البيانات وهل هي آمنة؟ | `DATA_CARD.md` |
| كيف مُنِع leakage؟ | split report + tests + `EVALUATION_REPORT.md` |
| لماذا هذا tokenizer/profile؟ | `DECISIONS.md` |
| ما جودة كل مهمة وشرائحها؟ | `EVALUATION_REPORT.md` |
| لماذا نثق برقم البحث؟ | relevance labels + Recall/MRR report |
| هل التحسين فعلي؟ | `BENCHMARKS.md` + JSON reports |
| هل الخدمة ترفض input السيئ؟ | service smoke report + tests |
| كيف يعاد التشغيل؟ | README Colab links + requirements + versions |
| ما النسخة المسلّمة؟ | `submission-v1.0` release |

## بنية المستودع النهائية

```text
bayan-nlp-YOUR-GITHUB-USERNAME/
├── README.md
├── STUDENT_PROFILE.md
├── PROGRESS.md
├── DECISIONS.md
├── BENCHMARKS.md
├── EVALUATION_REPORT.md
├── MODEL_CARD.md
├── DATA_CARD.md
├── PROJECT_SUMMARY.json
├── SUBMISSION.yml
├── notebooks/             # 00 إلى 08
├── src/bayan/             # وحدات مشتركة لا نسخ متكررة
├── tests/                 # golden + task + serving tests
├── reports/               # JSON/CSV صغيرة قابلة للمراجعة
└── sample_outputs/        # أمثلة آمنة وصغيرة فقط
```

الأوزان وONNX وcache وبيانات حساسة تبقى خارج GitHub. يوثق المصدر وhash وإعادة الإنتاج.

## مراجعة نظيرة من 8 دقائق

يتبادل كل متدربين المستودعين:

1. **دقيقتان:** افتح README في نافذة خاصة وتحقق من الروابط.
2. **دقيقتان:** تتبع metric واحدة إلى report وworkload.
3. **دقيقتان:** راجع limitation وprivacy boundary.
4. **دقيقتان:** شغّل validator أو راجع آخر run أخضر واكتب ملاحظة واحدة قابلة للتنفيذ.

استخدم [قالب المراجعة النظيرة](../templates/PEER_REVIEW_TEMPLATE.md). المراجع لا يغير ملفات زميله؛ يعطي دليلًا وملاحظة، وصاحب المشروع يقرر ويعمل commit.

## سيناريو العرض: 5 + 2 دقائق

| الزمن | ماذا تعرض؟ |
|---:|---|
| 0:00–0:30 | المشكلة والحدود والبيانات الاصطناعية |
| 0:30–2:00 | مثال عربي وإنجليزي من المسار الموحد |
| 2:00–3:00 | semantic search وحالة no-answer/limit |
| 3:00–4:00 | task metric + performance metric ومصدرهما |
| 4:00–5:00 | خطأ معروف وقرار هندسي والخطوة التالية |
| 5:00–7:00 | سؤالان؛ أحدهما: «لماذا نثق بهذا الرقم؟» |

لا تستهلك وقت العرض في تشغيل pip أو تدريب. افتح الروابط والتقارير مسبقًا، واحتفظ بمخرج آمن صغير إذا انقطع runtime.

## تنظيم العدد | Cohort-safe demo plan

| عدد المتدربين | التنظيم ضمن 12:40–13:30 مع تشغيل validator بالتوازي |
|---:|---|
| 1–4 | عروض 5+2 كاملة أمام الجميع؛ يبدأ فحص الملفات أثناء العرض |
| 5–10 | أزواج متوازية 3 دقائق لكل شخص + عرضين مختارين |
| 11–20 | محطات ثنائية/ثلاثية متوازية + rubric فردي للمستودع + عروض مختارة |

العرض الصفي المتوازي لا يحول المشروع إلى جماعي؛ المستودع والتقارير وشرح صاحبها فردية.

## تسميات الادعاءات

- `MEASURED`: قيس على artefact المشروع وبيئته وworkload موثق.
- `MEASURED_SMOKE`: عينة تعليمية صغيرة، مفيدة للتحقق لا للتعميم.
- `SYSTEMS_SMOKE`: يثبت سلامة الأنابيب التقنية فقط.
- `COURSE_FIXTURE`: بيانات/تنبؤات موزعة لأغراض التدريب.
- `TARGET`: budget كتب قبل القياس.
- `REFERENCE`: قيمة من مصدر منشور مع رابط.

لا تحول `SYSTEMS_SMOKE` إلى `MEASURED` بمجرد نسخه إلى README.

## تجميد النسخة | Release freeze

قبل tag:

1. أوقف إضافة features.
2. أصلح validator errors فقط.
3. أعد Run all في runtime نظيف.
4. تحقق من الروابط في نافذة خاصة.
5. اعمل commit: `release: complete Bayan submission v1.0`.
6. أنشئ tag/release المطلوب.
7. أعد validator بوضع `--require-tag`.

## English recap

Assembly connects every claim to inspectable evidence. Peer review follows one metric and one limitation, the demo is prepared rather than trained live, and cohort size is handled with parallel stations while repository grading remains individual. Freeze features before the final release.
