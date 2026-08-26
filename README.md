# معالجة اللغات الطبيعية التطبيقية  
# Applied Natural Language Processing

[![Quality checks](https://github.com/almiyead-rgb/bayan-applied-nlp-course/actions/workflows/quality.yml/badge.svg?branch=develop)](https://github.com/almiyead-rgb/bayan-applied-nlp-course/actions/workflows/quality.yml)

**إعداد وتقديم | Prepared and delivered by:** ميعاد المري · Meaad Al-Marri  
**السياق التدريبي | Training context:** أكاديمية سدايا · SDAIA Academy  
**المدة | Duration:** 4 أيام حضورية · 4 in-person days  
**البيئة | Environment:** Google Colab Free + GitHub

برنامج تطبيقي يبدأ من الصفر وينتقل بالمتدرب من معالجة النصوص إلى بناء مشروع **بيان**: نظام NLP ثنائي اللغة يجمع التصنيف، والتعرف على الكيانات، والإجابة الاستخراجية عن الأسئلة، والبحث الدلالي، والتقييم، وتحسين الاستدلال.

A beginner-friendly applied program that moves from text processing to **Bayan**, a bilingual NLP project combining classification, NER, extractive QA, semantic search, evaluation, and inference optimisation.

## ابدأ هنا | Start here

| وجهتك | متى تستخدمها؟ |
|---|---|
| [ابدأ من هنا · START HERE](START_HERE.md) | أول صفحة تفتحها قبل الدورة وفي صباح اليوم الأول |
| [دليل البرنامج · Course guide](COURSE_GUIDE.md) | الأهداف، الأيام، طريقة التعلم، والتقييم |
| [اليوم الأول · Day 1](day-01/README.md) | صفحة العرض المباشر: النص، الترميز، الانتباه، المختبرات، وبوابة المشروع |
| [اليوم الثاني · Day 2](day-02/README.md) | Fine-tuning للتصنيف وNER وQA وبوابة Gate B |
| [اليوم الثالث · Day 3](day-03/README.md) | العربية وCAMeL Tools والبحث الدلالي والتقييم وبوابة Gate C |
| [تجهيز البيئة · Setup hub](docs/setup/README.md) | GitHub وColab وفحص الجاهزية وحل الأعطال |
| [الأدوات المجانية · Free tools](docs/tools/free-tools.md) | ما هو إلزامي ومجاني، وما هو اختياري أو مدفوع |
| [قاموس المصطلحات · Glossary](docs/glossary/README.md) | تعريفات عربية/إنجليزية مبسطة وتقنية |
| [التقييم والاجتياز](docs/policies/assessment-and-completion.md) | الأوزان وشروط الشهادة |
| [طريقة التسليم](docs/policies/submission.md) | المستودع والملفات والـcommits والوسم النهائي |
| [النزاهة والخصوصية](docs/policies/integrity-and-privacy.md) | البيانات المسموحة والممنوعة |
| [مشروع بيان](docs/03-capstone-spec.md) | نطاق المشروع ومراحله ومخرجاته |
| [المصادر الرسمية](docs/references/official-sources.md) | الروابط الأولية المعتمدة للمحتوى والتجهيز |

## ماذا ستتعلم؟ | What will you learn?

1. بناء خط معالجة وترميز للنص العربي والإنجليزي.
2. فهم الانتباه ومعمارية المحولات.
3. Fine-tune نماذج BERT-family للتصنيف وNER وQA.
4. بناء بحث دلالي باستخدام sentence embeddings وFAISS.
5. تقييم كل مهمة بمقياسها الصحيح وتحليل الأخطاء.
6. قياس وتحسين latency والذاكرة للنشر.
7. تسليم مشروع عربي/إنجليزي موثق وقابل لإعادة التشغيل.

## خريطة الأيام | Four-day journey

| اليوم | السؤال الرئيس | ما تضيفه إلى بيان |
|---|---|---|
| [1](day-01/README.md) | كيف يتحول النص إلى أرقام يفهمها النموذج؟ | preprocessing + tokenizer decision + attention notebook |
| [2](day-02/README.md) | كيف نجعل النموذج يحل مهمة محددة؟ | classification + NER + QA |
| [3](day-03/README.md) | كيف نتعامل مع العربية ونثبت صحة النتائج؟ | CAMeL Tools + semantic search + evaluation report |
| 4 | كيف نجعل الحل أسرع وقابلًا للتسليم؟ | optimisation + tested API + final repository |

### ابدأ اليوم الأول | Start Day 1

1. افتح [صفحة اليوم الأول](day-01/README.md) واتبع الجدول بالترتيب.
2. نفّذ [مختبر معالجة النصوص والترميز](notebooks/01_text_processing_tokenization.ipynb) في Colab.
3. نفّذ [مختبر الانتباه والمحولات](notebooks/02_attention_transformers.ipynb) في Colab.
4. أكمل [بوابة مختبرات اليوم الأول وGate A](day-01/04-labs-checkpoint.md) واحفظ روابط الـcommits.

### ابدأ اليوم الثاني | Start Day 2

1. افتح [صفحة اليوم الثاني](day-02/README.md) وراجع شرط Gate A.
2. نفّذ [مختبر التصنيف](notebooks/03_text_classification.ipynb).
3. نفّذ [مختبر NER وQA](notebooks/04_ner_and_qa.ipynb) في runtime نفسه للاستفادة من cache.
4. أكمل [Gate B](day-02/05-labs-checkpoint.md) واحفظ رابط commit العام.

### ابدأ اليوم الثالث | Start Day 3

1. افتح [صفحة اليوم الثالث](day-03/README.md) وتحقق من اكتمال Gate B.
2. نفّذ [مختبر معالجة العربية](notebooks/05_arabic_nlp.ipynb) وأنشئ profile موثقة.
3. نفّذ [مختبر البحث الدلالي](notebooks/06_semantic_search.ipynb) وابنِ فهرس FAISS ثنائي اللغة.
4. نفّذ [مختبر التقييم وتحليل الأخطاء](notebooks/07_evaluation_error_analysis.ipynb).
5. أكمل [Gate C](day-03/04-labs-checkpoint.md) واحفظ التقارير وروابط الـcommits.


## مسارات التعلم | Learning lanes

- 🟢 **الأساسي · Core:** إلزامي للجميع، ومصمم ليبدأ من الصفر.
- 🔵 **الاستكشاف · Explore:** مقارنة أو تجربة إضافية بعد اكتمال الأساسي.
- 🟣 **التميّز · Distinction:** تحديات للمختصين ولا تعوض نقص Core.

## التكلفة | Cost

المسار الإلزامي مجاني: Google Colab Free، Google Drive، GitHub Public، ومكتبات Python مفتوحة المصدر. لا تحتاج اشتراك Colab Pro، أو خدمة API مدفوعة، أو جهازًا ببطاقة رسومية.

The required path is free. Paid services may be mentioned for comparison but are never required for completion.

## قبل تشغيل أي notebook

1. اقرأ الهدف والوقت المتوقع.
2. افتح النسخة من GitHub في Colab.
3. اختر **Save a copy in Drive**.
4. شغّل الخلايا بالترتيب.
5. لا تتجاوز خلية فاشلة.
6. احفظ الدليل المطلوب ثم اعمل commit إلى مستودعك.
7. قبل التسليم نفذ **Runtime → Restart session and run all**.

> لا تستخدم بيانات حقيقية أو أسرارًا. جميع تطبيقات بيان تستخدم بيانات تعليمية اصطناعية أو عامة موثقة.

---

© Meaad Al-Marri. Third-party libraries, datasets, references, and SDAIA Academy identity assets retain their respective rights and usage terms.
