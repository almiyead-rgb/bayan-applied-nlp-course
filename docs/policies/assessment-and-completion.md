# تقييم بيان: 100 درجة | Bayan assessment: 100 points

**BAYAN-100-v2.1 · إعداد المدربة ميعاد المري · 24 سبتمبر 2026**

| English | العربية |
|---|---|
| One final individual assessment: **70 technical + 20 administrative + 10 presentation = 100**. The presentation is included, not an extra ten points. | تقييم فردي نهائي واحد: **70 تقنية + 20 إدارية + 10 للعرض = 100 درجة**. العرض داخل المئة، وليس عشر درجات إضافية. |
| This instructor-directed rubric replaces the previous 35/15/10/40 weighting for the cohort using this version. Practice quizzes and PA activities are formative, with no separate grade. It is not an announcement of new Academy accreditation. | يحل هذا السلم بتوجيه المدربة محل الأوزان السابقة للدفعة التي تستخدم هذا الإصدار. الاختبارات التدريبية والأنشطة العملية للممارسة دون درجة مستقلة. لا يمثل إعلان اعتماد جديد من الأكاديمية. |
| Each row names its evidence and subpoints. Evidence quality earns technical credit; file organisation earns administrative credit. Do not count the same defect twice without two distinct unmet criteria. | يوضح كل بند دليله ونقاطه الفرعية. جودة التنفيذ لها نقاط تقنية، وتنظيم الدليل له نقاط إدارية. لا يخصم العيب نفسه مرتين إلا إذا أخل بمعيارين مستقلين. |

## تقنية — 70 | Technical

| ID | Points | English requirement | المتطلب بالعربية | Evidence / الدليل |
|---|---:|---|---|---|
| T1 | 12 | **Text preparation and Arabic handling**<br>4: Protected text and consistent versioned preprocessing<br>4: Tokenisation, fertility and truncation evidence<br>4: Arabic profile / CAMeL use and golden tests | **المعالجة والتعامل مع العربية**<br>4: نص محمي ومعالجة موحدة ذات إصدار<br>4: أدلة الترميز وكثافته والقطع<br>4: معالجة عربية واستخدام CAMeL واختبارات مرجعية | notebooks/01 + 05; DECISIONS.md; tests |
| T2 | 6 | **Attention and architecture understanding**<br>3: Correct Q/K/V shapes, masks and attention checks<br>3: Explain encoder flow and limits of attention interpretation | **فهم الانتباه والمعمارية**<br>3: صحة أبعاد Q/K/V والأقنعة وفحوص الانتباه<br>3: شرح مسار المشفر وحدود تفسير الانتباه | notebooks/02; README architecture; DECISIONS.md |
| T3 | 18 | **Classification, NER and QA**<br>6: Topic + sentiment heads, baseline, grouped split and metrics<br>6: BIO/subword alignment, training and entity-level evaluation<br>6: Extractive spans, no-answer and boundary tests | **التصنيف والكيانات والأسئلة**<br>6: رأسا الموضوع والمشاعر وخط الأساس والتقسيم والمقاييس<br>6: محاذاة BIO والوحدات الجزئية والتدريب وتقييم الكيانات<br>6: المقاطع الاستخراجية وعدم الإجابة والاختبارات الحدية | notebooks/03 + 04; reports; tests |
| T4 | 10 | **Bilingual semantic search**<br>4: Sentence vectors, normalisation and FAISS index<br>3: Measured cross-encoder re-ranking<br>3: Recall/MRR, cross-lingual case and no-answer decision | **البحث الدلالي الثنائي**<br>4: متجهات الجمل والتطبيع وفهرس FAISS<br>3: إعادة ترتيب بالمشفر المشترك مع قياسها<br>3: Recall/MRR وحالة عبر اللغات وقرار عدم الإجابة | notebooks/06; retrieval reports |
| T5 | 10 | **Evaluation and error analysis**<br>4: Appropriate metrics, frozen split and traceable outputs<br>3: Slices, sample sizes and uncertainty<br>3: Error taxonomy and three prioritised fixes | **التقييم وتحليل الأخطاء**<br>4: مقاييس مناسبة وتقسيم مجمد ومخرجات قابلة للتتبع<br>3: الشرائح وأحجام العينات وعدم اليقين<br>3: تصنيف الأخطاء وثلاثة إصلاحات مرتبة | notebooks/07; EVALUATION_REPORT.md |
| T6 | 10 | **Optimisation and tested service**<br>4: Actual PROJECT_ARTIFACT benchmark before/after<br>3: ONNX/INT8 attempt, parity, quality tax and rollback decision<br>3: Unified service contract and AR/EN/invalid-input tests | **التحسين والخدمة المختبرة**<br>4: قياس PROJECT_ARTIFACT الفعلي قبل التحسين وبعده<br>3: تجربة ONNX/INT8 والتكافؤ وأثر الجودة وقرار التراجع<br>3: عقد خدمة موحد واختبارات العربية والإنجليزية والمدخل المرفوض | notebooks/08; BENCHMARKS.md; API tests |
| T7 | 4 | **One measured extension**<br>2: Implemented, bounded extension in the original scope<br>2: Baseline, benefit/cost and evidence | **امتداد واحد مقاس**<br>2: امتداد منفذ ومحدود ضمن نطاق المشروع<br>2: خط أساس وفائدة وتكلفة ودليل | PROJECT_SUMMARY.json extension; DECISIONS.md |

## إدارية — 20 | Administrative

| ID | Points | English requirement | المتطلب بالعربية | Evidence / الدليل |
|---|---:|---|---|---|
| A1 | 4 | **Repository organisation and safe publication**<br>2: Own accessible repository, main branch and required paths<br>2: No secrets, personal data or forbidden model artifacts | **تنظيم المستودع والنشر الآمن**<br>2: مستودع شخصي متاح وفرع main والمسارات المطلوبة<br>2: لا أسرار أو بيانات شخصية أو أوزان نموذج محظورة | repository tree; private-window check |
| A2 | 6 | **README and attribution**<br>2: Problem, scope, architecture and limitations<br>2: Own runnable links, result table and reproduction steps<br>2: Program code, SDAIA Academy, #SDAIAAcademy, trainer and sources | **README ونسب العمل**<br>2: المشكلة والنطاق والمعمارية والحدود<br>2: روابط تشغيل شخصية وجدول نتائج وخطوات إعادة التشغيل<br>2: رمز البرنامج وأكاديمية سدايا و#SDAIAAcademy والمدربة والمصادر | README.md |
| A3 | 4 | **Evidence package and documentation**<br>2: Required reports/cards/progress and real links to evidence<br>2: Valid summary/YAML and preflight reports | **حزمة الأدلة والتوثيق**<br>2: التقارير والبطاقات والتقدم وروابط الأدلة الفعلية<br>2: صحة الملخص وYAML وتقارير الفحص | required root files; reports/preflight.json |
| A4 | 4 | **Versioned final submission**<br>2: Meaningful progress history and declared commit SHA<br>2: submission-v1.0, complete hand-in and one-shot acknowledgement | **نسخة التسليم النهائية**<br>2: تاريخ تقدم مفهوم وبصمة Commit معلنة<br>2: وسم submission-v1.0 وتسليم مكتمل وإقرار التقييم الواحد | Git history; release; private hand-in |
| A5 | 2 | **Authorship and assistance disclosure**<br>1: Own contribution linked to a file/change/evidence<br>1: Honest source and AI/tool assistance disclosure or none | **المساهمة والإفصاح عن المساعدة**<br>1: مساهمة شخصية مربوطة بملف أو تغيير أو دليل<br>1: إفصاح صادق عن المصادر وأدوات المساعدة أو عدم استخدامها | README contribution and assistance sections |

## العرض — 10 | Presentation

| ID | Points | English requirement | المتطلب بالعربية | Evidence / الدليل |
|---|---:|---|---|---|
| P1 | 2 | **Problem and architecture**<br>2: Explain the user, scope and data flow accurately | **المشكلة والمعمارية**<br>2: شرح المستخدم والنطاق وتدفق البيانات بدقة | individual presentation |
| P2 | 3 | **Bilingual demonstration**<br>3: Own AR/EN examples with extraction/search and a no-answer or rejected case | **العرض التطبيقي الثنائي**<br>3: أمثلة شخصية بالعربية والإنجليزية مع استخراج أو بحث وحالة عدم إجابة أو رفض | own running project or documented fallback |
| P3 | 2 | **Evidence and limitations**<br>2: Trace one quality metric and one performance metric; state a limitation | **الدليل والحدود**<br>2: تتبع مقياس جودة ومقياس أداء وشرح قيد معروف | report links on screen |
| P4 | 2 | **Individual understanding**<br>2: Answer a code/decision question and a small input-change check | **الفهم الفردي**<br>2: إجابة عن الكود أو القرار وفحص تغيير صغير في المدخل | live instructor verification |
| P5 | 1 | **Clarity and delivery**<br>1: Readable visuals, clear sequence and prepared demo within the agreed slot | **الوضوح والالتزام**<br>1: عرض مقروء وتسلسل واضح وتجهيز مسبق والتزام بالمدة | maximum five slides or equivalent |

## كيف تمنح النقاط؟ | How credit is awarded

| English | العربية |
|---|---|
| For each listed subitem: full credit for correct, complete evidence; half credit for a meaningful but incomplete attempt; zero for missing, irrelevant or unverified evidence. Record the reason and file/line/output. | لكل بند فرعي: الدرجة كاملة لدليل صحيح ومكتمل؛ نصفها لمحاولة جوهرية ناقصة؛ وصفر للدليل الغائب أو غير ذي الصلة أو غير المتحقق. يسجل المصحح السبب والملف أو السطر أو المخرج. |
| A copied PASS string, checked browser box or self-declared tests_passed=true is not proof of successful execution. Automatic checks support review; they do not award a grade or conclusively detect plagiarism. | نسخ عبارة PASS أو تأشير مربع في المتصفح أو كتابة tests_passed=true ليس إثباتًا للتنفيذ. الفحوص الآلية تدعم المراجعة ولا تمنح درجة ولا تكشف الانتحال بصورة قطعية. |
| Completion requires at least **70/100**, mandatory project evidence, valid submission and no established integrity/privacy violation. Distinction starts at **90/100** after those conditions. No bonus is added outside these 100 points. | يتطلب الإكمال **70/100** على الأقل، وأدلة المتطلبات الأساسية وتسليمًا صحيحًا وعدم ثبوت مخالفة نزاهة أو خصوصية. يبدأ التميز من **90/100** بعد استيفاء الشروط. لا تضاف درجات مكافأة خارج المئة. |
| Published reference R1–R7 targets apply only with the announced frozen cohort data, suite and hardware. On small synthetic samples, report MEASURED_SMOKE honestly; missing organiser assets must not become surprise numerical penalties. | تطبق أهداف R1–R7 المرجعية فقط مع حزمة الدفعة المجمدة والاختبارات والعتاد المعلنة. تظل العينات الاصطناعية الصغيرة MEASURED_SMOKE؛ ولا تتحول موارد لم توفرها الجهة إلى خصومات رقمية مفاجئة. |
| This version does not authorise a second attempt. Improve and check as often as needed **before** final hand-in; after hand-in, the captured commit is assessed once. Later edits or moved tags do not replace it. | لا يجيز هذا الإصدار محاولة تصحيح ثانية. عدّل وافحص مرارًا **قبل** الإرسال النهائي؛ وبعده تقيم نسخة الـCommit المستلمة مرة واحدة. التعديلات اللاحقة أو نقل الوسم لا تستبدلها. |
| Attendance, administrative accommodations and certificate issuance remain organiser decisions. This rubric grades the project and presentation, not attendance. | تبقى إجراءات الحضور والتيسيرات الإدارية وإصدار الشهادة لدى الجهة المنظمة. يقيم هذا السلم المشروع والعرض، وليس الحضور. |

[مواصفات العرض | Presentation](../presentation-guide.md) · [التسليم النهائي | Hand-in](submission.md) · [النزاهة | Integrity](integrity-and-privacy.md)
