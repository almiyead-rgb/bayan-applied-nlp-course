# ابدأ من هنا | START HERE

**إعداد وتقديم:** ميعاد المري · **Prepared and delivered by:** Meaad Al-Marri

هذه الصفحة هي نقطة البداية للمشارك في برنامج `SDA-AIE-211` التخصصي. يفترض البرنامج إكمال `SDA-AIE-112` أو امتلاك أساس مكافئ في Python وتعلم الآلة. اتبع الخطوات بالترتيب؛ لا تحتاج تثبيت Python محليًا لأن التطبيق الأساسي يتم داخل المتصفح باستخدام Google Colab.

This is the starting point for every learner. Follow it in order. The required path runs in the browser through Google Colab, so local Python installation is not required.

## قبل الدورة بـ24–48 ساعة | Before the course

- [ ] لدي حساب Google أستطيع فتح Drive وColab به.
- [ ] لدي حساب GitHub وبريد الحساب مؤكد.
- [ ] أعرف اسم مستخدم GitHub الخاص بي.
- [ ] أستطيع فتح `github.com` و`colab.research.google.com` و`drive.google.com`.
- [ ] أستخدم نسخة حديثة من Chrome أو Edge أو Firefox.
- [ ] أغلقت حظر النوافذ المنبثقة لهذه المواقع عند الحاجة فقط.
- [ ] لا أستخدم حسابًا مشتركًا مع شخص آخر.
- [ ] فعّلت 2FA في GitHub وحفظت recovery codes في مكان آمن — موصى به.
- [ ] أحضرت الشاحن، وسماعة عند الحاجة، ووسيلة دخول 2FA.
- [ ] قرأت [سياسة الخصوصية والنزاهة](docs/policies/integrity-and-privacy.md).

إذا لم يكن لديك حساب GitHub، اتبع [دليل GitHub](docs/setup/github.md). يتطلب GitHub بريدًا مؤكدًا لإتمام وظائف أساسية مثل إنشاء مستودع، وفق [وثائق GitHub الرسمية](https://docs.github.com/en/account-and-profile/how-tos/account-management/creating-an-account-on-github).

## أول 15 دقيقة | Your first 15 minutes

### 1. افتح فاحص البيئة

افتح [دفتر Runtime Doctor](notebooks/00_runtime_doctor.ipynb)، ثم استخدم زر **Open in Colab** الموجود داخله.

### 2. احفظ نسختك

من Colab اختر:

`File → Save a copy in Drive`

غيّر الاسم إلى:

`00_runtime_doctor_YOUR_GITHUB_USERNAME.ipynb`

### 3. شغّل بالترتيب

اختر:

`Runtime → Run all`

لا تعتبر الفحص ناجحًا إلا إذا ظهرت الرسالة:

`BAYAN_ENV_READY = True`

نجاح CPU كافٍ. ظهور `GPU unavailable` ليس خطأ؛ موارد Colab المجانية تتغير وليست مضمونة وفق [الأسئلة الرسمية الشائعة لـColab](https://research.google.com/colaboratory/faq.html).

### 4. احفظ تقرير البيئة

سينشئ الدفتر ملفًا صغيرًا باسم:

`runtime_report.json`

لا يحتوي التقرير كلمة مرور أو token. احتفظ به ضمن مخرجات التجهيز.

### 5. افتح خريطة البرنامج

اقرأ [دليل البرنامج](COURSE_GUIDE.md)، ثم اكتب في ملاحظاتك:

- المهارة التي تريد اكتسابها أكثر.
- المهمة التي تبدو جديدة عليك.
- مستوى المسار الذي ستبدأ به: 🟢 دائمًا أولًا.

## متى أصبحت جاهزًا؟ | Ready when

أنت جاهز عندما تستطيع:

- فتح notebook من GitHub في Colab.
- تشغيل خلية وقراءة مخرجها.
- حفظ نسخة في Drive.
- معرفة الفرق بين warning وerror.
- إنشاء مستودع GitHub عام باستخدام حزمة بداية الطالب.
- تنفيذ commit برسالة واضحة.
- نسخ **نص الخطأ الكامل** عند طلب المساعدة.

لا يشترط أن تكون قد درّبت Transformer أو BERT مسبقًا، لكن يلزم أن تستطيع قراءة Python الأساسية، وتشغيل notebook، وتفسير train/validation/test ومقياس بسيط. إن لم تتأكد، نفّذ [فحص الجاهزية](docs/setup/README.md#فحص-الجاهزية-العلمية--knowledge-readiness) قبل اليوم الأول واطلب مسار الدعم.

## إذا واجهت مشكلة | If something fails

لا تغيّر عدة أشياء مرة واحدة. استخدم هذه الصيغة عند طلب المساعدة:

```text
الخطوة | Step:
اسم الدفتر | Notebook:
رقم/عنوان الخلية | Cell:
نص الخطأ الكامل | Full error:
ما الذي جربته مرة واحدة؟ | One action tried:
CPU/GPU:
رابط المستودع أو لقطة لا تكشف بيانات حساسة:
```

ثم انتقل إلى [دليل استكشاف الأعطال](docs/setup/troubleshooting.md).

## قواعد الأمان السريعة | Safety rules

- لا تلصق password أو token أو recovery code في notebook.
- لا ترفع ملفات اعتماد أو بيانات أشخاص إلى GitHub.
- لا تشغّل notebook من مصدر لا تثق به.
- اقرأ صلاحية Google Drive قبل منحها؛ تركيب Drive يسمح للكود بالوصول إلى ملفات Drive.
- استخدم بيانات الدورة فقط.
- احفظ تقدمك في Drive وGitHub؛ ملفات runtime مؤقتة.

## المسار التالي | Next

1. [كيف تعمل الدورة؟](COURSE_GUIDE.md)
2. [إعداد GitHub](docs/setup/github.md)
3. [إعداد Colab وDrive](docs/setup/colab.md)
4. [الأدوات المجانية والاختيارية](docs/tools/free-tools.md)
5. [قاموس المصطلحات](docs/glossary/README.md)
6. [خريطة الأيام الأربعة](README.md#خريطة-الأيام--four-day-journey)
7. [طريقة التسليم النهائي](docs/policies/submission.md)
