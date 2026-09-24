# 4. مقدمة اختيار نموذج للعربية
# Arabic Model Selection — Introduction

<!-- BAYAN_YOUTUBE_START -->
### شاهد الفكرة ثم طبّقها | Video companions

<div class="card youtube-topic youtube-t14"><h3 class="pair"><span class="en" lang="en" dir="ltr">Arabic variation and CAMeL context</span><span class="ar" lang="ar" dir="rtl">تنوع العربية ومدخل أدوات CAMeL</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Understand Arabic morphology, clitics and dialect variation before selecting a profile.</p><p class="ar" lang="ar" dir="rtl">افهم الصرف واللواصق واللهجات قبل اختيار ملف المعالجة.</p></div><p><strong lang="en" dir="ltr">A Short Introduction to Arabic Natural Language Processing</strong><br><span class="micro">Nizar Habash · JSALT · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=vQL5CUlbw0k" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><div class="callout warning"><div class="pair"><p class="en" lang="en" dir="ltr">A conceptual lecture, not a step-by-step CAMeL Tools tutorial. The CAMeL implementation remains in Notebook 05.</p><p class="ar" lang="ar" dir="rtl">محاضرة مفاهيمية وليست شرحًا تنفيذيًا كاملًا لأدوات CAMeL. التنفيذ في الدفتر 05.</p></div></div><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">Which Arabic variation could change your tokenizer’s behaviour?</p><p class="ar" lang="ar" dir="rtl">أي اختلاف في العربية قد يغير سلوك المرمّز؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<!-- BAYAN_YOUTUBE_END -->

## لا يوجد نموذج «أفضل» مطلقًا

الاختيار يعتمد على:

- اللغات المطلوبة: عربية فقط أم عربية/إنجليزية.
- MSA أو لهجات أو نصوص تاريخية.
- المهمة: تصنيف أو NER أو QA.
- طول النص وسرعة الاستدلال والذاكرة.
- tokenizer وpreprocessing المستخدمين في pretraining.
- الترخيص وبطاقة النموذج وحدود البيانات.

## خيارات اليوم

| النموذج | التغطية | استخدامه في البرنامج |
|---|---|---|
| DistilmBERT multilingual cased | متعدد اللغات ومنها العربية والإنجليزية | Core ثنائي اللغة في اليوم الثاني |
| CAMeLBERT Mix | عربي؛ مزيج من MSA ولهجات وعربية كلاسيكية وفق بطاقته | مقارنة عربية في اليوم الثالث |
| AraBERT v02 | نموذج BERT عربي مع تعليمات preprocessing خاصة بعائلته | مثال على ضرورة مطابقة preprocessing |

لا تعني القائمة ترتيب جودة. يجب تقييم checkpoint الفعلي على بيانات المهمة.

## لماذا نبدأ بمتعدد اللغات؟

مشروع بيان ثنائي اللغة، ونحتاج في خمس ساعات إلى خط أساس موحد ومفهوم. DistilmBERT يقلل عدد الطبقات مقارنة بـmBERT، لكنه ما يزال نموذجًا كبيرًا نسبيًا بسبب vocabulary متعددة اللغات. نستخدم عينة قصيرة وCPU fallback.

## متى أجرب نموذجًا عربيًا؟

- عندما تكون العربية أغلب الحمل.
- عند وجود فجوة واضحة في Arabic slice.
- عندما تتطابق بيانات pretraining مع MSA/اللهجة المطلوبة.
- عندما يمكن تشغيل نفس preprocessing في train وserve.
- عندما تقارن metric المهمة لا الانطباع.

اليوم الثالث يضيف CAMeL Tools ويقارن النتائج بدليل، وليس بمجرد اسم النموذج.

## مجاني ومدفوع

### المسار المجاني الإلزامي

- تنزيل checkpoint عام من Hugging Face Hub.
- تشغيل محلي داخل Colab.
- حفظ config وmetrics الصغيرة في GitHub.
- عدم رفع weights الكبيرة.

### اختياري وقد يكون مدفوعًا

- Colab Pro للحصول على موارد أكثر؛ غير مضمون وغير مطلوب.
- Hugging Face hosted inference أو endpoints؛ ليست مطلوبة.
- منصات experiment tracking؛ لا نستخدمها في Core.

نحفظ metrics في JSON/Markdown محليًا، لذلك لا يلزم حساب إضافي أو token.

## بطاقة قرار مختصرة

| السؤال | إجابتي |
|---|---|
| اللغات المطلوبة |  |
| نوع العربية |  |
| المهمة |  |
| checkpoint الأول |  |
| CPU/GPU |  |
| preprocessing المتوافق |  |
| metric القرار |  |
| القيد أو الخطر |  |

## قاعدة اليوم

اختيار النموذج فرضية قابلة للاختبار. اكتب:

> اخترت X كبداية لأن… وسأستبدله إذا أظهر Slice Y أن Metric Z أقل من الحد الذي حددته.
