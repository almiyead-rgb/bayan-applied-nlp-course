# GitHub خطوة بخطوة | GitHub Setup

<!-- BAYAN_YOUTUBE_START -->
### شاهد الفكرة ثم طبّقها | Video companions

<div class="card youtube-topic youtube-t02"><h3 class="pair"><span class="en" lang="en" dir="ltr">Your repository and README</span><span class="ar" lang="ar" dir="rtl">مستودعك وملف README</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Create your own repository and recognise the role of README and gitignore.</p><p class="ar" lang="ar" dir="rtl">أنشئ مستودعك وافهم دور README وملف gitignore.</p></div><p><strong lang="en" dir="ltr">GitHub for Beginners #1: Create Your First Repository</strong><br><span class="micro">Ben Day · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=5A9oLJRLVl4" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">Where will your own notebook, code and evidence be stored?</p><p class="ar" lang="ar" dir="rtl">أين ستحفظ دفترك وكودك وأدلتك الشخصية؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<!-- BAYAN_YOUTUBE_END -->

## ما هو المستودع؟ | Repository

المستودع (Repository) مجلد مشروع يحتفظ بالملفات وتاريخ تغييراتها. الـCommit لقطة موثقة لحالة المشروع في لحظة معينة. يوضح [دليل GitHub الرسمي](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories) أن README يظهر تلقائيًا في واجهة المستودع ويشرح المشروع.

## 1. إنشاء الحساب

1. افتح [github.com/signup](https://github.com/signup).
2. أنشئ حسابًا شخصيًا مجانيًا.
3. اختر username مهنيًا؛ سيظهر في رابط مشروعك.
4. أكد بريدك الإلكتروني.
5. سجّل دخولك من المتصفح الذي ستستخدمه في الدورة.

وفق [وثائق GitHub الرسمية](https://docs.github.com/en/account-and-profile/how-tos/account-management/creating-an-account-on-github)، البريد المؤكد مطلوب لبعض الوظائف الأساسية مثل إنشاء المستودع.

## 2. حماية الحساب

فعّل 2FA من Settings واحفظ recovery codes خارج GitHub. توصي [وثائق GitHub](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication) بتطبيق TOTP بدل SMS عندما يتوفر.

**ممنوع:** تصوير recovery codes، إرسالها، أو وضعها في Colab/README.

## 3. تنزيل حزمة بداية الطالب

1. نزّل [حزمة بداية الطالب الرسمية](../../downloads/bayan-student-starter.zip).
2. افتح [SHA256SUMS](../../downloads/SHA256SUMS.txt) إذا أردت التحقق من سلامة التنزيل.
3. فك الضغط. يجب أن تجد `GETTING_STARTED.md` وتسعة دفاتر ومجلدات `src` و`tests` و`reports` و`sample_outputs`.
4. لا ترفع ملف ZIP نفسه إلى مشروعك؛ ارفع **محتوياته بعد فك الضغط**.

لا تعتمد على قالب خارجي منفصل؛ الحزمة المرفقة هنا هي المصدر الرسمي وتمنع اعتماد الطلاب على رابط غير منشور.

## 4. إنشاء مستودعك العام ورفع الحزمة

1. افتح [github.com/new](https://github.com/new).
2. اختر حسابك مالكًا واستخدم الاسم `bayan-nlp-YOUR-GITHUB-USERNAME`.
3. اختر **Public**، ولا تضف README أو `.gitignore` جديدين؛ فهما موجودان في الحزمة.
4. أنشئ المستودع، ثم اختر **uploading an existing file**.
5. اسحب محتويات الحزمة بعد فكها، بما فيها المجلدات. الحزمة `78` ملفًا، وهي دون حد GitHub الحالي البالغ `100` ملف لكل عملية رفع من المتصفح، ولا تحتوي أوزان نماذج.
6. استخدم رسالة commit: `chore: initialise Bayan student workspace`.
7. افتح المستودع في نافذة خاصة وتأكد أن README والدفاتر تظهر بلا تسجيل دخول.

يوضح [دليل GitHub الرسمي](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository) رفع الملفات من المتصفح. إذا منعت جهة العمل رفع مجلد كامل، استخدم مسار Git المحلي الاختياري في الدليل الرسمي أو اطلب مساعدة المدربة؛ لا تنشئ token داخل notebook.

## 5. أول تعديل وCommit

1. افتح `STUDENT_PROFILE.md`.
2. اضغط رمز القلم.
3. اكتب الاسم الذي تسمح بعرضه، وGitHub username، ومستواك الذاتي.
4. اختر **Commit changes**.
5. استخدم الرسالة:
   `docs: complete student profile`

الـCommit الجيد يصف تغييرًا واحدًا:

```text
docs: update day 1 reflection
feat: add bilingual preprocessing
test: add Arabic normalization cases
fix: correct NER label alignment
perf: record ONNX benchmark
```

لا تستخدم `update` أو `final` وحدهما؛ فهما لا يشرحان ما تغير.

## 6. حفظ notebook من Colab إلى GitHub

الطريقة الأساسية:

1. احفظ نسخة العمل أولًا في Drive.
2. بعد نجاح الاختبارات اختر في Colab:
   `File → Save a copy in GitHub`
3. امنح الصلاحية من نافذة Google/GitHub الرسمية فقط.
4. اختر مستودعك والفرع `main`.
5. اكتب commit message محددة.
6. تأكد من مسار الملف قبل الحفظ.

هذا المسار موضح في [دفتر Colab الرسمي للتكامل مع GitHub](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb).

إذا لم يظهر الخيار أو فشل OAuth، اتبع [استكشاف الأعطال](troubleshooting.md) ولا تنشئ token علنيًا.

## 7. النسخة النهائية

شغّل فاحص ما قبل tag أولًا:

```bash
PYTHONPATH=src python scripts/validate_submission.py . \
  --json-report reports/submission_validation.json
```

بعد ظهور `BAYAN_SUBMISSION_VALIDATOR=PASS` والتحقق من الروابط في نافذة خاصة:

1. افتح **Releases** في مستودعك.
2. اختر **Draft a new release**.
3. أنشئ tag باسم:
   `submission-v1.0`
4. اجعل target هو `main`.
5. اكتب عنوانًا: `Bayan NLP Final Submission`.
6. انشر الإصدار ثم انسخ رابطه.

ثم اسحب أو افتح النسخة التي تحتوي tag وأعد:

```bash
PYTHONPATH=src python scripts/validate_submission.py . --require-tag
```

GitHub Releases مبنية على tags التي تحدد نقطة في تاريخ المستودع، وفق [الوثائق الرسمية](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases).

## فحص سريع

- [ ] المستودع Public.
- [ ] الاسم صحيح.
- [ ] ملفات حزمة البداية في الحزمة ظهرت، بما فيها المجلدات المتداخلة.
- [ ] README يظهر في الصفحة الرئيسية.
- [ ] لا secrets أو ملفات ضخمة.
- [ ] يوجد commit بعد كل مختبر.
- [ ] روابط Colab تفتح.
- [ ] الإصدار النهائي يشير إلى `main`.
