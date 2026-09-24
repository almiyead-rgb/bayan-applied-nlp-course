# مواصفات البرنامج | Course Specification

**الإصدار | Version:** 2.0 — Instructor-directed delivery update; scientific scope unchanged

**مصدر الحقيقة | Source of truth:** هذا الملف يحكم المدة، النطاق، التقييم، والاجتياز. عند التعارض تُصحّح الملفات الأخرى لتطابقه.  
This file governs duration, scope, assessment, and completion requirements. Conflicting files must be corrected to match it.

> تحديث المدة بتوجيه المدربة بتاريخ 24 سبتمبر 2026؛ ليس ادعاء اعتماد جديد. الأهداف والأوزان ومتطلبات المشروع الأصلية محفوظة.
> Duration updated at the instructor’s request on 24 September 2026; no new accreditation is claimed. Original outcomes, weights and project requirements remain.

## الهوية | Identity

| البند | القيمة | Item | Value |
|---|---|---|---|
| اسم البرنامج | معالجة اللغات الطبيعية التطبيقية | Program | Applied Natural Language Processing |
| المدربة | ميعاد المري | Instructor | Meaad Al-Marri |
| رمز البرنامج | `SDA-AIE-211` | Program code | `SDA-AIE-211` |
| النمط | حضوري + Google Colab | Mode | In person + Google Colab |
| المدة | 4 أيام × 6 ساعات تعلم صافية = 24 ساعة | Duration | 4 days × 6 net learning hours = 24 hours |
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

## رحلة التعلم | Learning journey

أربعة أيام متدرجة، ولكل يوم مفاهيم وتطبيق ودليل. [افتح رحلة الأيام دون جدول زمني تفصيلي](04-delivery-plan.md).

Four progressive days, each with concepts, practice and evidence. Open the journey guide for topic summaries.

## خريطة الأيام | Four-day arc

| اليوم | المحور | ناتج بيان اليومي |
|---|---|---|
| [1](../day-01/README.md) | النص إلى Tensor: المعالجة، الترميز، التضمينات، الانتباه | وحدة معالجة عربية/إنجليزية + قرار tokenizer + اختبار ذهبي |
| [2](../day-02/README.md) | جعل النموذج متخصصًا: التصنيف، NER، QA، مدخل للعربية | نماذج/مسارات مهام قابلة للتشغيل مع تقييم أولي |
| [3](../day-03/README.md) | العمق العربي، البحث الدلالي، التقييم وتحليل الأخطاء | فهرس ثنائي اللغة + تقرير مقطّع + قائمة أخطاء |
| [4](../day-04/README.md) | التحسين، الخدمة، التجميع، العرض | API مختبرة + benchmark + مستودع تسليم كامل |

## التقييم | Assessment

**70 تقنية + 20 إدارية + 10 للعرض = 100 درجة إجمالًا.** العرض داخل المئة. تُقيّم نسخة التسليم مرة واحدة ولا تقبل نسخة معدلة بعد الإرسال. تبقى الأنشطة والاختبارات القصيرة للممارسة دون وزن مستقل.

**70 technical + 20 administrative + 10 presentation = 100 total.** The presentation is included. The submitted version is graded once; later replacements are not accepted. Practice activities and quizzes have no separate weight.

[سلم التقييم الكامل | Full rubric](policies/assessment-and-completion.md) · [متطلبات العرض | Presentation](presentation-guide.md)

## شروط الاجتياز | Completion requirements

الحد الأدنى **70/100** مع الأدلة الإلزامية والتسليم الصحيح وعدم ثبوت مخالفة نزاهة أو خصوصية. التميز من **90/100** بعد استيفاء الشروط، بلا نقاط خارج المئة. `submission-v1.0` وSHA النهائي يحددان النسخة التي ستصحح مرة واحدة.

A minimum of **70/100**, mandatory evidence, valid hand-in and no established integrity/privacy violation are required. Distinction starts at **90/100** after those conditions; no extra bonus is added. The final tag and recorded SHA identify the single assessed version.

إصدار الشهادة والحضور والتيسيرات الإدارية تخضع لإجراءات الجهة المنظمة. لا يُقدّم تعديل السلم باعتباره اعتمادًا جديدًا.

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
