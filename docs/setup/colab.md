# Google Colab وDrive | Colab and Drive

## ما هو Colab؟

Google Colab خدمة Jupyter Notebook مستضافة تعمل في المتصفح ومناسبة للتعلم الآلي. يمكن استخدامها مجانًا دون إعداد محلي.

> الموارد المجانية ليست ثابتة أو مضمونة: نوع GPU، مدة الجلسة، timeout، والحصص قد تتغير. تؤكد [الأسئلة الرسمية الشائعة](https://research.google.com/colaboratory/faq.html) أن حدود الاستخدام ديناميكية ولا تنشر كقيم ثابتة.

### بيئة Colab المرجعية الحالية | Current reference runtime

بتاريخ **26 أغسطس 2026** تعرض Google البيئة السابقة القابلة للتثبيت `2026.07` وفيها `Python 3.12.13` و`NumPy 2.0.2` و`PyTorch 2.11.0`. هذه قيم `REFERENCE` من [صفحة Runtime Versions الرسمية](https://research.google.com/colaboratory/runtime-version-faq.html)، وليست افتراضًا بأن كل جلسة ستبقى مطابقة. شغّل Runtime Doctor وسجل ما توفر فعليًا بوصفه `MEASURED`.

توضح Google أن الإصدارات السابقة تبقى متاحة حاليًا لمدة سنة، وأن اختيارها قد يزيد وقت الاتصال؛ لذلك نستخدم أحدث runtime افتراضيًا ونلجأ إلى النسخة المرجعية فقط إذا ظهر تعارض موثق.

لذلك نجاح CPU هو الأساس، ولكل مختبر مسار مصغر.

## 1. فتح notebook من GitHub

1. افتح ملف `.ipynb` في مستودع الدورة.
2. اضغط **Open in Colab**.
3. تأكد أن الرابط يبدأ بـ:
   `https://colab.research.google.com/`
4. لا تشغّل نسخة من مصدر مجهول.

## 2. احفظ نسخة قبل التشغيل

اختر:

`File → Save a copy in Drive`

لا تعمل ساعات على نسخة مؤقتة فقط. جميع notebooks تحفظ بصيغة Jupyter المفتوحة `.ipynb`.

## 3. افهم أجزاء الواجهة

- **Text cell:** شرح، سؤال، أو تعليمات.
- **Code cell:** كود Python يمكن تشغيله بزر ▶.
- **Runtime:** الجهاز المؤقت الذي ينفذ الكود.
- **Files:** ملفات runtime؛ قد تختفي عند إنهاء الجلسة.
- **Drive:** تخزين دائم بعد منح الصلاحية.

## 4. CPU وGPU

افتح:

`Runtime → Change runtime type`

- اختر CPU إذا كان GPU غير متاح.
- اختر T4/GPU إن ظهر ضمن المجاني؛ لا تفترض أنه سيظهر دائمًا.
- لا تغيّر الجهاز أثناء التدريب دون حفظ checkpoint.

تشغيل الخلية التالية يكشف الجهاز:

```python
import torch
device = "cuda" if torch.cuda.is_available() else "cpu"
print("device =", device)
```

## 5. تركيب Google Drive

نستخدم Drive فقط عندما نحتاج حفظ checkpoint أو نتيجة بعد انتهاء runtime:

```python
from google.colab import drive
drive.mount("/content/drive")
```

اقرأ شاشة الصلاحية قبل الموافقة. توضح [وثائق Colab الرسمية](https://research.google.com/colaboratory/faq.html) أن تركيب Drive يسمح لكود notebook بالوصول إلى ملفات Drive؛ لذلك لا تمنح الصلاحية لدفتر لا تثق بمصدره.

أنشئ مجلدًا:

```text
MyDrive/bayan-nlp/
├── checkpoints/
├── reports/
└── recovery/
```

لا تقرأ وتكتب آلاف الملفات الصغيرة مباشرة من Drive أثناء التدريب؛ اعمل في `/content` ثم انسخ checkpoint المقصودة.

## 6. ترتيب التشغيل الصحيح

1. Runtime Doctor.
2. خلية الإعداد.
3. imports.
4. البيانات.
5. المعالجة.
6. النموذج.
7. التدريب/الاستدلال.
8. التقييم.
9. الحفظ.
10. الاختبارات النهائية.

إذا شغّلت الخلايا خارج الترتيب، أعد:

`Runtime → Restart session and run all`

## 7. ماذا يختفي؟

| العنصر | يبقى بعد انتهاء runtime؟ |
|---|---|
| ملف في `/content` | لا |
| متغير Python | لا |
| GPU memory | لا |
| notebook محفوظ في Drive | نعم |
| ملف نُسخ إلى Drive | نعم |
| commit على GitHub | نعم |

## 8. حفظ إلى GitHub

بعد نجاح notebook:

`File → Save a copy in GitHub`

اختر مستودعك وcommit message واضحة. لا تجعل GitHub هو النسخة الوحيدة قبل التأكد من الحفظ؛ احتفظ بنسخة Drive أيضًا. راجع [دليل GitHub](github.md).

## 9. متى أستخدم Colab المدفوع؟

ليس مطلوبًا في الدورة. قد يوفر compute units أو وصولًا أوسع لبعض الموارد، لكنه لا يلغي ديناميكية التوفر. لا تشترِ اشتراكًا لأجل الاجتياز؛ استخدم reduced path وcheckpoints المجانية.
