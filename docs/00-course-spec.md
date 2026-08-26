# مواصفات البرنامج | Course Specification

**الإصدار | Version:** 0.1 — Foundation  
**مصدر الحقيقة | Source of truth:** هذا الملف يحكم المدة، النطاق، التقييم، والاجتياز. عند التعارض تُصحّح الملفات الأخرى لتطابقه.  
This file governs duration, scope, assessment, and completion requirements. Conflicting files must be corrected to match it.

## الهوية | Identity

| البند | القيمة | Item | Value |
|---|---|---|---|
| اسم البرنامج | معالجة اللغات الطبيعية التطبيقية | Program | Applied Natural Language Processing |
| المدربة | ميعاد المري | Instructor | Meaad Al-Marri |
| النمط | حضوري + Google Colab | Mode | In person + Google Colab |
| المدة | 4 أيام × 5 ساعات صباحية | Duration | 4 days × 5 morning hours |
| السعة | حتى 20 متدربًا | Capacity | Up to 20 learners |
| المستويات | مبتدئ، متوسط، مختص | Levels | Beginner, intermediate, specialist |
| المشروع | بيان — نظام NLP ثنائي اللغة | Capstone | Bayan — bilingual NLP system |
| التسليم | مستودع GitHub عام إلزامي | Submission | Mandatory public GitHub repository |

## الفلسفة التعليمية | Learning design

كل درس يبدأ بالمفهوم، ثم مثال صغير، ثم تطبيق موجّه، ثم دليل قابل للتقييم. ولا يعتمد نجاح المبتدئ على إنهاء مهام التوسع.

Every lesson moves from concept to a small example, guided practice, and assessable evidence. A beginner can pass without completing extension work.

- 🟢 **أساسي | Core:** إلزامي للجميع ويغطي نواتج التعلم.
- 🔵 **استكشاف | Explore:** للمتوسطين أو لمن ينتهي مبكرًا.
- 🟣 **تميّز | Distinction:** تحديات للمختصين، ولا تعوّض نقص المتطلبات الأساسية.

## الأهداف الرسمية | Official learning outcomes

بنهاية البرنامج يكون المتدرب قادرًا على:

1. بناء خطوط معالجة النصوص والترميز، بما يشمل المعالجة الخاصة باللغة العربية.  
   Build text-processing and tokenisation pipelines, including Arabic-specific processing.
2. شرح آليات الانتباه ومعمارية المحولات.  
   Explain attention mechanisms and Transformer architecture.
3. الضبط الدقيق لنماذج محولات مدرّبة مسبقًا للتصنيف وNER والإجابة عن الأسئلة.  
   Fine-tune pretrained Transformers for classification, NER, and question answering.
4. تطوير البحث الدلالي والتشابه باستخدام التضمينات.  
   Build embedding-based semantic search and similarity applications.
5. تقييم النماذج بالمقاييس المناسبة وتحليل الأخطاء.  
   Evaluate NLP models with task-appropriate metrics and error analysis.
6. تحسين سرعة الاستدلال واستهلاك الذاكرة للنشر.  
   Improve inference speed and memory use for deployment.
7. إنجاز مشروع تطبيقي ثنائي اللغة بالعربية والإنجليزية.  
   Deliver a bilingual Arabic–English NLP capstone.

## النطاق | Scope

**داخل المسار الإلزامي:** Python fundamentals needed by the labs, Unicode and regex, tokenisation, embeddings, attention, encoder Transformers, BERT-family fine-tuning, classification, NER, extractive QA, Arabic normalisation and CAMeL Tools, sentence embeddings, FAISS, evaluation, error analysis, ONNX/INT8 concepts, FastAPI testing, Git/GitHub evidence.

**خارج النطاق:** تدريب نموذج لغوي من الصفر، واجهة سحابية مدفوعة، استضافة إنتاجية دائمة، تدريب موزّع، RLHF، أو بناء تطبيق LLM عام. تُذكر هذه الموضوعات كامتدادات فقط.

## الجدول اليومي الثابت | Fixed daily timetable

| الوقت | المدة | الاستخدام |
|---|---:|---|
| 08:30–09:20 | 50 دقيقة | مفهوم + عرض عملي |
| 09:20–09:30 | 10 دقائق | استراحة |
| 09:30–10:20 | 50 دقيقة | ممارسة موجّهة |
| 10:20–10:30 | 10 دقائق | استراحة |
| 10:30–11:20 | 50 دقيقة | مختبر |
| 11:20–11:30 | 10 دقائق | استراحة |
| 11:30–12:20 | 50 دقيقة | مختبر/مشروع |
| 12:20–12:40 | 20 دقيقة | استراحة طويلة/صلاة |
| 12:40–13:30 | 50 دقيقة | بوابة إنجاز + حفظ نقطة الاستعادة |

إجمالي اليوم: **250 دقيقة تعلم + 50 دقيقة استراحات = 5 ساعات**.  
Daily total: **250 learning minutes + 50 break minutes = 5 hours**.

## خريطة الأيام | Four-day arc

| اليوم | المحور | ناتج بيان اليومي |
|---|---|---|
| 1 | النص إلى Tensor: المعالجة، الترميز، التضمينات، الانتباه | وحدة معالجة عربية/إنجليزية + قرار tokenizer + اختبار ذهبي |
| 2 | جعل النموذج متخصصًا: التصنيف، NER، QA، مدخل للعربية | نماذج/مسارات مهام قابلة للتشغيل مع تقييم أولي |
| 3 | العمق العربي، البحث الدلالي، التقييم وتحليل الأخطاء | فهرس ثنائي اللغة + تقرير مقطّع + قائمة أخطاء |
| 4 | التحسين، الخدمة، التجميع، العرض | API مختبرة + benchmark + مستودع تسليم كامل |

## التقييم | Assessment

| المكوّن | الوزن | الدليل |
|---|---:|---|
| المختبرات 1–7 | 35% | commits، اختبارات، ومخرجات متوقعة |
| تقويمان عمليان | 15% | تشخيص وإصلاح/مراجعة مدعومة بالدليل |
| اختبار قصير | 10% | 10 أسئلة موضوعية |
| مشروع بيان | 40% | rubric + مستودع + عرض |

## شروط الاجتياز | Completion requirements

يستحق المتدرب **شهادة/إثبات الاجتياز وفق إجراءات الأكاديمية** عند تحقق جميع الشروط:

1. الدرجة النهائية **70/100 فأعلى**.
2. درجة المشروع الختامي **70/100 فأعلى**.
3. حضور **80% على الأقل**؛ وإذا كانت سياسة الأكاديمية أشد فهي المقدّمة.
4. مستودع GitHub عام ومكتمل، ورابطه مسلّم في الموعد.
5. اجتياز فاحص التسليم ووجود الأدلة الإلزامية.
6. عدم وجود مخالفة للنزاهة الأكاديمية أو نشر لبيانات شخصية/أسرار.
7. وسم الإصدار النهائي `submission-v1.0`.

**التميّز | Distinction:** 90/100 فأعلى، مع استيفاء جميع المتطلبات الأساسية. مهام التوسع تضيف حتى 5 نقاط، بسقف نهائي 100، ولا تُحسب إذا كان نطاق المشروع الإلزامي أقل من 80%.

## سياسة الأدوات | Tooling policy

المسار الإلزامي يستخدم خدمات مجانية: **Google Colab Free، Google Drive، GitHub Public، Python، Hugging Face open-source libraries، CAMeL Tools، FAISS CPU، ONNX Runtime، FastAPI**. لا يلزم Colab Pro أو GitHub Copilot أو واجهة API مدفوعة.

موارد Colab المجانية ديناميكية وغير مضمونة؛ لذلك لكل مختبر مسار CPU، حجم بيانات مصغر، checkpoint قابل للاستئناف، وخيار نموذج صغير. تُذكر الخيارات المدفوعة للمقارنة فقط وتوسم بوضوح بأنها غير مطلوبة.

## الخصوصية والنزاهة | Privacy and integrity

- استخدم بيانات الدورة الاصطناعية أو العامة المرخّصة فقط.
- لا ترفع أسماء حقيقية، أرقام هوية، هواتف، بريدًا شخصيًا، مفاتيح API، أو ملفات اعتماد.
- لا ترفع أوزان النماذج الكبيرة؛ تحفظ في Drive وتوثّق طريقة إعادة إنتاجها.
- يجوز الاستفادة من المراجع والمساعدة البرمجية مع ذكرها؛ ويجب أن يفهم المتدرب كل claim وكل سطر جوهري يقدمه.
- النسخ المطابق للنتائج الرقمية أو العبث بمجموعة الاختبار مخالفة.

## قاعدة القياسات | Metrics truth rule

كل قيمة رقمية توسم بواحد من:

- `REFERENCE`: من مصدر موثوق مع رابط.
- `MEASURED`: قاسها المتدرب مع البيئة والبذرة والتاريخ.
- `TARGET`: حد نجاح تدريبي.
- `EXAMPLE`: رقم توضيحي غير صالح كادعاء.

## نقاط الاستعادة | Recovery checkpoints

في نهاية كل جلسة: حفظ notebook، تصدير النتائج الصغيرة إلى Drive، تنفيذ commit، تحديث `PROGRESS.md`، ثم التأكد من رابط Colab. عند تعطل GPU ينتقل الصف فورًا إلى مسار CPU المصغر دون تغيير نواتج التعلم.
