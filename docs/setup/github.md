# GitHub من الصفر | GitHub from Zero

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

## 3. إنشاء مستودعك من قالب الطالب

عند نشر قالب الدورة:

1. افتح مستودع `bayan-nlp-student-template`.
2. اضغط **Use this template**.
3. اختر **Create a new repository**.
4. اختر حسابك مالكًا.
5. استخدم الاسم:
   `bayan-nlp-YOUR-GITHUB-USERNAME`
6. اختر **Public**.
7. لا تختر Include all branches.
8. اضغط **Create repository**.

إنشاء مستودع من template يبدأ تاريخًا جديدًا بدل نسخ تاريخ المستودع الأصلي، وفق [دليل GitHub الرسمي](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

## 4. أول تعديل وCommit

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

## 5. حفظ notebook من Colab إلى GitHub

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

## 6. النسخة النهائية

بعد اجتياز فاحص التسليم:

1. افتح **Releases** في مستودعك.
2. اختر **Draft a new release**.
3. أنشئ tag باسم:
   `submission-v1.0`
4. اجعل target هو `main`.
5. اكتب عنوانًا: `Bayan NLP Final Submission`.
6. انشر الإصدار ثم انسخ رابطه.

GitHub Releases مبنية على tags التي تحدد نقطة في تاريخ المستودع، وفق [الوثائق الرسمية](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases).

## فحص سريع

- [ ] المستودع Public.
- [ ] الاسم صحيح.
- [ ] README يظهر في الصفحة الرئيسية.
- [ ] لا secrets أو ملفات ضخمة.
- [ ] يوجد commit بعد كل مختبر.
- [ ] روابط Colab تفتح.
- [ ] الإصدار النهائي يشير إلى `main`.
