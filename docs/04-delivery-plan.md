# رحلة بيان عبر أربعة أيام | Bayan four-day journey

تعرض هذه الصفحة التسلسل والموضوعات ومخرجات التعلم، دون تقسيم الساعة إلى فترات أو دقائق. تبقى مدة البرنامج الإجمالية 24 ساعة، وتعلن المدربة الترتيبات التشغيلية للدفعة منفصلة.

This page shows learning order, topics and outputs, not an hourly timetable. The course remains 24 hours; cohort logistics are announced separately.

## اليوم 1: من النص إلى المعنى | Day 1: From text to meaning

نبدأ بملاحظة واحدة، لا بصفحة مليئة بالمعادلات. نتتبع رحلتها: نص محمي، ثم وحدات ترميز، ثم تضمينات وانتباه. كل خطوة تجهّز جزءًا من بيان.

Start with one feedback message, not a wall of equations. Follow its journey through protected text, tokens, embeddings and attention. Every step prepares a piece of Bayan.

| Topic | English explanation | الشرح بالعربية |
|---|---|---|
| The Bayan problem / مشكلة بيان | Turn Arabic and English feedback into an inspectable analysis. Distinguish a teaching prototype from a service that makes real decisions. | نحوّل ملاحظات عربية وإنجليزية إلى تحليل يمكن فحصه. نحدد المستفيد وما ينتجه المشروع، ونفصل النموذج التعليمي عن خدمة تتخذ قرارات حقيقية. |
| Text, Unicode and privacy / النص وUnicode والخصوصية | Inspect text encoding, keep a safe display copy and create a model copy with documented masking and normalisation. | نفحص ترميز النص، ونحتفظ بنسخة عرض آمنة، وننشئ نسخة للنموذج مع إخفاء المعرّفات وتوثيق التطبيع. لا ننشر نصًا شخصيًا خامًا. |
| Tokens and embeddings / الترميز والتضمينات | Compare words and subwords; measure fragmentation and truncation. Token IDs are vocabulary positions, while embeddings are learned vectors. | نميّز الكلمات والوحدات الجزئية ونقيس التجزئة والقطع. رقم الرمز موضع في القاموس؛ أما التضمين فهو متجه عددي متعلّم. |
| Attention and Q/K/V / الانتباه وQ/K/V | Trace a small attention computation: queries compare with keys, and the resulting weights combine values. Check tensor shapes and masks. | نتتبع حسابًا صغيرًا: تقارن الاستعلامات بالمفاتيح، وتستخدم الأوزان الناتجة لدمج القيم. نفحص أبعاد المصفوفات وأقنعة الانتباه. |
| Transformer encoder / مشفر المحوّل | Connect multi-head attention, residual paths, normalisation and feed-forward layers; inspect a real forward pass and explain the limits of attention visualisation. | نربط الانتباه متعدد الرؤوس بالمسارات المتبقية والتطبيع والطبقات الأمامية، ونفحص تمريرًا فعليًا مع توضيح حدود تفسير خرائط الانتباه. |

**Architecture / المسار المعماري:** Synthetic AR/EN text → Privacy + profile → Tokens → vectors → Encoder + attention checks

**الأثر في المشروع:** اختبارات المعالجة + قرار الترميز + فحوص الانتباه + commit

[دليل اليوم وتطبيقاته](../day-01/README.md)

## اليوم 2: أعطِ النموذج مهمة | Day 2: Give the model a task

نبقى مع سياق بيان نفسه. نحدد المهمة وخط الأساس أولًا، ثم نفهم تقسيم البيانات ورأس المهمة والمقياس. يأتي التدريب بعد وضوح العقد.

Keep the same Bayan context. First define the task and a baseline; then inspect the data split, task head and metric. Training comes after the contract is clear.

| Topic | English explanation | الشرح بالعربية |
|---|---|---|
| Pretraining and task heads / التدريب المسبق ورؤوس المهام | Reuse a pretrained encoder and understand what changes during fine-tuning. Record whether the encoder is frozen in the CPU path. | نعيد استخدام مشفر مدرب مسبقًا ونفهم ما يتغير في الضبط الدقيق، ونسجل بصراحة هل جُمّد المشفر عند استخدام بديل CPU. |
| Baseline and honest splits / خط الأساس والتقسيم السليم | Create a TF-IDF baseline, keep groups separate across train/validation/test, then evaluate topic and sentiment with independent label contracts. | نبني خط أساس TF-IDF ونمنع تداخل المجموعات بين التدريب والتحقق والاختبار، ثم نقيس الموضوع والمشاعر بعقدي وسوم مستقلين. |
| NER and label alignment / الكيانات ومحاذاة الوسوم | Use BIO labels, align word labels to subwords and exclude special or ignored tokens from the loss as documented. Evaluate complete entities. | نستخدم وسوم BIO ونحاذي وسوم الكلمات مع الوحدات الجزئية ونستبعد الرموز الخاصة أو المهملة من حساب الخسارة وفق الدرس. نقيم الكيان كاملًا. |
| Extractive QA and no-answer / الأسئلة الاستخراجية وعدم وجود إجابة | Select an answer span from the supplied context. When the context does not support an answer, return no-answer instead of generating text. | نختار مقطع إجابة من السياق المقدم. عندما لا يدعم السياق الإجابة نعيد عدم وجود إجابة، ولا نولّد نصًا من خارج المصدر. |
| Arabic model choice / اختيار النموذج للعربية | Compare Arabic and multilingual checkpoint assumptions, tokenizer compatibility and sample coverage; justify the choice with evidence. | نقارن افتراضات النماذج العربية ومتعددة اللغات وتوافق المرمّز وتغطية العينة، ثم نبرر الاختيار بالدليل لا بالاسم الأشهر. |

**Architecture / المسار المعماري:** Protected, grouped data → Baseline + encoder → Topic / sentiment / NER / QA → Task metrics + Gate B

**الأثر في المشروع:** خط أساس + عدم تداخل المجموعات + أدلة التصنيف والكيانات والأسئلة + commit

[دليل اليوم وتطبيقاته](../day-02/README.md)

## اليوم 3: افهم العربية وابحث بالدليل | Day 3: Understand Arabic. Find evidence.

النتيجة المفيدة ليست مجرد كلمات مشتركة. نقارن المعنى، ونفحص الحالات المرتبة، ثم نقيس الاسترجاع ونحلل الأخطاء بدل الثقة برقم واحد.

A useful search result is more than shared words. Compare meaning, inspect the ranked cases, then measure retrieval and analyse errors rather than trusting a single score.

| Topic | English explanation | الشرح بالعربية |
|---|---|---|
| Arabic variation / تنوع العربية | Handle morphology, clitics, dialects and orthographic variation without treating all normalisation as harmless. | نتعامل مع الصرف واللواصق واللهجات والتنوع الإملائي دون افتراض أن كل تطبيع آمن. نحتفظ بالنص المحمي الذي يمكن الرجوع إليه. |
| CAMeL Tools and profiles / أدوات CAMeL وملفات المعالجة | Apply the documented Arabic profile and inspect the small Arabic-model comparison using the same evaluation contract. | نطبق ملف المعالجة العربي الموثق ونفحص المقارنة المصغرة بين النماذج مع تثبيت عقد التقييم وإظهار حدود العينة. |
| Sentence embeddings and FAISS / تضمينات الجمل وFAISS | Encode cases and queries with the same sentence model, normalise vectors and retrieve candidates using IndexFlatIP. | نرمّز الحالات والاستعلامات بنموذج جمل واحد، ونطبّع المتجهات ثم نسترجع المرشحين باستخدام IndexFlatIP. لا نخلط تضمين الجملة بمخرج المصنف. |
| Re-ranking and retrieval metrics / إعادة الترتيب ومقاييس البحث | Re-score the shortlist with a cross-encoder; compare Recall@k, MRR@k and latency. Tune no-answer on validation only. | نعيد تقييم المرشحين بالمشفر المشترك، ونقارن Recall@k وMRR@k والزمن. تضبط عتبة عدم الإجابة على التحقق فقط. |
| Error analysis and uncertainty / تحليل الأخطاء وعدم اليقين | Inspect language and task slices, sample sizes and confidence intervals. Classify errors and prioritise three evidence-backed fixes. | نفحص شرائح اللغة والمهمة وأحجام العينات وفترات الثقة، ونصنف الأخطاء ونرتب ثلاثة إصلاحات مدعومة بالدليل. |

**Architecture / المسار المعماري:** Arabic profile + case corpus → Sentence vectors → FAISS → Retrieve → re-rank → Slices + error report

**الأثر في المشروع:** ملف معالجة العربية + مقاييس البحث + تقرير الشرائح + ثلاثة إصلاحات مرتبة

[دليل اليوم وتطبيقاته](../day-03/README.md)

## اليوم 4: قِس، حسّن، ثم سلّم | Day 4: Measure. Improve. Deliver.

عمل النموذج في الدفتر بداية وليس نهاية. نثبت عبء العمل، ونقارن قبل التحسين وبعده، ونختبر الخدمة، ونجعل المستودع النهائي قابلًا للمراجعة.

A model running in a notebook is the beginning, not the finish. Freeze the workload, compare before and after, test the API and make the final repository reviewable.

| Topic | English explanation | الشرح بالعربية |
|---|---|---|
| Benchmark before changing / القياس قبل التغيير | Define the workload and performance budget; separate warm-up and record device, repetitions, latency, throughput and observed memory. | نحدد عبء العمل وميزانية الأداء، ونفصل الإحماء ونسجل الجهاز والتكرارات والزمن ومعدل المعالجة والذاكرة المرصودة. |
| ONNX and INT8 / ONNX وINT8 | Export, check numerical or prediction parity, and measure the quality and speed cost of quantisation. Keep a rollback path. | نصدّر النموذج ونفحص التكافؤ العددي أو التنبؤي، ثم نقيس أثر التكميم على الجودة والسرعة مع الاحتفاظ بمسار تراجع. |
| API contract and canaries / عقد الخدمة والاختبارات الحارسة | Connect project components through the documented service interface and test valid Arabic/English input, rejected input and preprocessing consistency. | نربط المكونات بواجهة الخدمة الموثقة، ونختبر طلبًا عربيًا وإنجليزيًا ومدخلًا مرفوضًا واتساق المعالجة مع النموذج. |
| Integration and measured extension / التكامل والامتداد المقاس | Assemble previous lab outputs, evaluate the actual project artifact and measure one bounded extension against a baseline. | نجمع مخرجات اللابات السابقة ونقيّم ناتج المشروع الفعلي ونقيس امتدادًا محدودًا واحدًا مقارنة بخط أساس. لا نبدأ مشروعًا جديدًا. |
| Evidence, presentation and submission / الأدلة والعرض والتسليم | Trace every number to a report, explain one limitation, practise the individual demo and validate the exact commit you will submit once. | نربط كل رقم بتقرير، ونشرح قيدًا معروفًا، ونتدرب على العرض الفردي ونفحص نسخة الـCommit التي سنرسلها مرة واحدة. |

**Architecture / المسار المعماري:** Actual project artifact → Benchmark → ONNX / INT8 → Parity + quality + API tests → Evidence → release

**الأثر في المشروع:** قياس المشروع + خدمة مختبرة + تقارير + فاحص ناجح + submission-v1.0

[دليل اليوم وتطبيقاته](../day-04/README.md)

## المشروع والتقييم | Project and assessment

اللابات تبني مشروع بيان نفسه تدريجيًا. التقييم 70 تقنية و20 إدارية و10 للعرض ضمن مجموع 100. العرض فردي والتصحيح مرة واحدة بعد التسليم.

The labs progressively build the same Bayan. Assessment is 70 technical, 20 administrative and 10 presentation within 100. The presentation and final review are individual.

[سيناريو المشروع ومعماريته](project-walkthrough.md) · [التقييم](policies/assessment-and-completion.md) · [خطوات العمل](learner-workflow.md)
