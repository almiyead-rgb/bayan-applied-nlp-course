# مواصفات البرنامج | Course Specification

**الإصدار | Version:** 1.1 — Final accreditation alignment

**مصدر الحقيقة | Source of truth:** هذا الملف يحكم المدة، النطاق، التقييم، والاجتياز. عند التعارض تُصحّح الملفات الأخرى لتطابقه.  
This file governs duration, scope, assessment, and completion requirements. Conflicting files must be corrected to match it.

## الهوية | Identity

| البند | القيمة | Item | Value |
|---|---|---|---|
| اسم البرنامج | معالجة اللغات الطبيعية التطبيقية | Program | Applied Natural Language Processing |
| المدربة | ميعاد المري | Instructor | Meaad Al-Marri |
| رمز البرنامج | `SDA-AIE-211` | Program code | `SDA-AIE-211` |
| النمط | حضوري + Google Colab | Mode | In person + Google Colab |
| المدة | 4 أيام × 5 ساعات تدريبية اسمية = 20 ساعة | Duration | 4 days × 5 nominal learning hours = 20 hours |
| السعة | حتى 20 متدربًا | Capacity | Up to 20 learners |
| المستوى | تخصصي | Level | Specialist |
| المتطلب السابق | `SDA-AIE-112` أو ما يعادله | Prerequisite | `SDA-AIE-112` or equivalent foundations |
| المشروع | بيان — نظام NLP ثنائي اللغة | Capstone | Bayan — bilingual NLP system |
| التسليم | مستودع GitHub عام إلزامي | Submission | Mandatory public GitHub repository |

## الفلسفة التعليمية | Learning design

كل درس يبدأ بالمفهوم، ثم مثال صغير، ثم تطبيق موجّه، ثم دليل قابل للتقييم. تخدم السقالات تفاوت الثقة العملية داخل المستوى التخصصي، ولا يعتمد الاجتياز على مهام التوسع.

Every lesson moves from concept to a small example, guided practice, and assessable evidence. Scaffolding supports varied practical confidence within the specialist level. Explore/Distinction lane work is optional; the capstone's single measured extension is a separate official R7 requirement.

- 🟢 **أساسي | Core:** إلزامي للجميع ويغطي نواتج التعلم.
- 🔵 **استكشاف | Explore:** للمتوسطين أو لمن ينتهي مبكرًا.
- 🟣 **تميّز | Distinction:** تحديات للمختصين، ولا تعوّض نقص المتطلبات الأساسية.

مسارات المستوى السابقة تخص أنشطة الدروس؛ أما المشروع الختامي فيتطلب امتدادًا واحدًا مقاسًا وفق [مواصفات بيان](03-capstone-spec.md).

## نواتج التعلم الرسمية | Official learning outcomes

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

### متطلب التكامل الختامي | Capstone integration requirement

يُثبت المتدرب النواتج الرسمية الستة من خلال مشروع «بيان» التطبيقي ثنائي اللغة. المشروع متطلب تكاملي إلزامي في التقييم، وليس `LO7` إضافيًا في الحزمة المرجعية.

The learner demonstrates the six official outcomes through the bilingual Bayan capstone. The capstone is a mandatory integration and assessment requirement, not an additional `LO7` in the source package.

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

إجمالي اليوم: **5 فترات تدريبية اسمية**؛ كل فترة `50` دقيقة تعلم و`10` دقائق مرونة، أي **250 دقيقة تعلم مباشر + 50 دقيقة انتقال/استراحة = 5 ساعات اسمية**.<br>
Daily total: **5 nominal learning periods** of `50` learning minutes plus `10` buffer minutes: **250 direct learning minutes + 50 transition/break minutes = 5 nominal hours**.

## خريطة الأيام | Four-day arc

| اليوم | المحور | ناتج بيان اليومي |
|---|---|---|
| [1](../day-01/README.md) | النص إلى Tensor: المعالجة، الترميز، التضمينات، الانتباه | وحدة معالجة عربية/إنجليزية + قرار tokenizer + اختبار ذهبي |
| [2](../day-02/README.md) | جعل النموذج متخصصًا: التصنيف، NER، QA، مدخل للعربية | نماذج/مسارات مهام قابلة للتشغيل مع تقييم أولي |
| [3](../day-03/README.md) | العمق العربي، البحث الدلالي، التقييم وتحليل الأخطاء | فهرس ثنائي اللغة + تقرير مقطّع + قائمة أخطاء |
| [4](../day-04/README.md) | التحسين، الخدمة، التجميع، العرض | API مختبرة + benchmark + مستودع تسليم كامل |

## التقييم | Assessment

| المكوّن | الوزن | الدليل |
|---|---:|---|
| المختبرات 1–7 | 35% | commits، اختبارات، ومخرجات متوقعة |
| تقويمان عمليان | 15% | تشخيص وإصلاح/مراجعة مدعومة بالدليل |
| اختبار قصير | 10% | 10 أسئلة موضوعية |
| مشروع بيان | 40% | rubric + مستودع + عرض |

مواد المتدرب للتقييمين العمليين وتعليمات الاختبار في [حزمة التقييم](../assessments/README.md). مفاتيح الإجابة والتصحيح التفصيلي لا تُنشر في المستودع العام.

## شروط الاجتياز | Completion requirements

تتحقق **الأهلية الأكاديمية للاجتياز** عند استيفاء الشروط المثبتة في الحزمة المرجعية ومتطلبات التسليم التقنية لهذه النسخة:

1. الدرجة النهائية **70/100 فأعلى**.
2. درجة المشروع الختامي **70/100 فأعلى**.
3. عدم وجود مخالفة للنزاهة الأكاديمية.
4. مستودع GitHub عام ومكتمل، ورابطه مسلّم في الموعد بوصفه دليل هذه النسخة.
5. اجتياز فاحص التسليم ووجود الأدلة الإلزامية.
6. عدم نشر بيانات شخصية أو أسرار.
7. وسم الإصدار النهائي `submission-v1.0`.

الحضور، والتيسيرات، وإعادة المحاولة، وآلية إصدار الشهادة/الشارة تحددها الجهة المنظمة وتعلنها للدفعة؛ لا يضع هذا المستودع نسبة حضور غير واردة في المصدر المرجعي.

**مسار التميّز | Distinction lane:** التميّز عند `90/100` فأعلى بعد استيفاء شروط الاجتياز. مهام bonus تضيف حتى `+5` نقاط (بحد أقصى `100`) فقط عندما تبلغ المتطلبات الإلزامية للمشروع `80/100` على الأقل؛ ولا تعوض نقص Core أو الامتداد الإلزامي المقاس.

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
- `MEASURED_SMOKE`: قياس فعلي على عينة تعليمية صغيرة لا يسمح بالتعميم.
- `SYSTEMS_SMOKE`: تحقق فعلي من البنية التقنية، لا من جودة المهمة.
- `COURSE_FIXTURE`: قيمة أو تنبؤ تعليمي موزع مع الدورة وليس ناتج model run للمتدرب.
- `TARGET`: حد نجاح تدريبي.
- `EXAMPLE`: رقم توضيحي غير صالح كادعاء.

## نقاط الاستعادة | Recovery checkpoints

في نهاية كل جلسة: حفظ notebook، تصدير النتائج الصغيرة إلى Drive، تنفيذ commit، تحديث `PROGRESS.md`، ثم التأكد من رابط Colab. عند تعطل GPU ينتقل الصف فورًا إلى مسار CPU المصغر دون تغيير نواتج التعلم.
