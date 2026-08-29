# قاموس اليوم الثالث | Day 3 Glossary

**العربية، البحث، والحقيقة | Arabic, Search, and Truth**  
**إعداد وتقديم | Prepared and delivered by:** ميعاد المري · Meaad Al-Marri

يشرح هذا القاموس مصطلحات العربية وCAMeL Tools والبحث الدلالي والتقييم وتحليل الأخطاء كما تظهر في صفحات اليوم الثالث ودفاتره 05–07. يبدأ كل صف بالمصطلح الإنجليزي، ثم النطق التقريبي، والتعريف بالإنجليزية، والشرح بالعربية، ومثال تطبيقي.

> لا تعني المصطلحات الخاصة باللهجة أو Arabizi أن النظام «يفهم كل العربية»؛ الادعاء المقبول هو ما تدعمه الشرائح والاختبارات الموثقة فقط.

## A. Arabic NLP and CAMeL Tools

مرتبط بـ[معالجة العربية باستخدام CAMeL Tools](01-arabic-nlp-camel-tools.md) و[Notebook 05](../notebooks/05_arabic_nlp.ipynb).

| English term | Pronunciation | English explanation | الشرح بالعربية | Example |
|---|---|---|---|---|
| Arabic morphology | آرابِك مورفولوجي | The study and computational analysis of how Arabic words are formed from roots, patterns, and affixes. | دراسة بنية الكلمة العربية وكيف تتكون من جذور وأوزان وزوائد ولواصق. | «وبالمدرسة» تجمع أكثر من عنصر صرفي في كلمة مكتوبة واحدة. |
| Clitic | كْلِتِك | A short grammatical element pronounced with and written attached to a neighbouring word. | عنصر لغوي قصير يلتصق بالكلمة كتابةً مثل الواو والباء واللام. | في «وبالرياض» تظهر الواو والباء ملتصقتين باسم الموقع. |
| Affix | أفِكس | A morpheme attached to a word stem, including prefixes and suffixes. | جزء يضاف إلى أول الكلمة أو آخرها لتغيير معناها أو وظيفتها. | «الـ» في «الخدمة» prefix و«ها» في «طلبها» suffix. |
| Morphological segmentation | مورفولوجِك سيغمِنتيشن | Splitting a word into meaningful morphological components. | تقسيم الكلمة إلى مكوناتها الصرفية ذات المعنى أو الوظيفة. | قد تُحلل «وبالرياض» إلى `و + ب + الرياض`. |
| Root | روت | A consonantal base associated with a family of Arabic words. | جذر غالبًا صامت يربط مجموعة كلمات متقاربة اشتقاقيًا. | «كتب» جذر «كتاب» و«كاتب» و«مكتوب». |
| Stem | ستِم | A reduced word form produced by removing selected affixes, not necessarily a dictionary word. | شكل مختصر ينتج من إزالة بعض الزوائد وقد لا يكون كلمة معجمية صحيحة. | قد يحول stemmer «والطلبات» إلى شكل أقصر بحسب قواعده. |
| Stemming | ستِمِنغ | Applying rules or an algorithm to reduce words to stems. | عملية اختزال الكلمات إلى stems، وقد تنتج شكلًا غير معجمي. | يستخدم البحث stemming فقط إذا أثبت القياس فائدته للمهمة. |
| Lemma | لِمَّا | The canonical dictionary form selected for an inflected word in context. | الصيغة المعجمية الأساسية للكلمة، وقد تحتاج سياقًا وتحليلًا صرفيًا. | Lemma «ذهبوا» هي «ذهب». |
| Diacritic | داياكريتِك | A mark added to a letter to indicate pronunciation or grammatical information. | علامة مثل الفتحة والضمة والكسرة والشدة. | «عَلَم» و«عِلْم» يختلفان بالتشكيل. |
| Diacritic removal | داياكريتِك رِموفَل | Removing Arabic diacritics under an explicit task-specific policy. | حذف التشكيل وفق قرار موثق، وليس خطوة آمنة دائمًا. | حذف الحركة قد يحسن المطابقة لكنه يزيل الفرق بين «عَلَم» و«عِلْم». |
| Tatweel | تطويل | The Arabic elongation character used for visual stretching rather than lexical meaning. | محرف الكشيدة المستخدم للشكل البصري غالبًا. | يتحول «الخدمــــة» إلى «الخدمة» إذا نص profile على إزالة التطويل. |
| Orthographic variation | أورثوغرافِك فِرييشن | Multiple written forms that may represent related or equivalent linguistic content. | اختلافات الكتابة مثل أشكال الألف والياء والتاء المربوطة. | `أ/إ/آ/ا` اختلاف يجب قياس أثر توحيده. |
| Modern Standard Arabic (MSA) | مودرن ستاندرد آرابِك | The formal standard variety used across much Arabic writing and media. | العربية الفصحى المعاصرة المستخدمة في الخطاب الرسمي والإعلامي. | «لم يصلني رمز التحقق» مثال أقرب إلى MSA. |
| Dialect | دايَلِكت | A regional or social language variety with its own vocabulary and patterns. | تنوع لغوي محلي له مفرداته وصيغه، وليس «خطأً» يجب تنظيفه. | «ما وصلني الكود» صياغة لهجية مقارنة بـ«لم يصلني الرمز». |
| Gulf Arabic | غَلف آرابِك | A group of Arabic dialect varieties used in the Gulf region. | مجموعة لهجات خليجية لها مفردات وتراكيب متباينة داخلها أيضًا. | شريحة `Gulf` في المختبر تُقاس منفصلة ولا تمثل كل متحدث خليجي. |
| Arabic variant | آرابِك فِريَنت | A labelled language form such as MSA, Gulf, or Arabizi used for slicing or routing. | وسم يصف شكل النص لأغراض التحليل، ولا يعني أن النظام تنبأ باللهجة آليًا. | يحمل المثال `variant=Gulf` إذا كان الوسم مقدمًا في البيانات. |
| Arabizi | آرابيزي | Arabic language written using Latin letters, often with digits for Arabic sounds. | كتابة العربية بحروف لاتينية وأرقام. | `ma wasalni code 3al jawal` مثال Arabizi. |
| Transliteration | ترانزْلِتِريشن | Converting text from one writing system to another while approximating spelling or sound. | تحويل الكتابة بين نظامين مثل Latin والعربية، وقد ينتج أكثر من احتمال. | تحويل `3al` إلى «على» يحتاج قواعد واختبارًا مستقلًا. |
| Heuristic | هيوريستِك | A practical rule that may work often but does not guarantee a correct prediction. | قاعدة تقريبية تساعد في بعض الحالات ولا تعادل نموذجًا مقاسًا. | وجود الرقم `3` قد يشير إلى Arabizi لكنه ليس مصنف لهجة موثوقًا وحده. |
| CAMeL Tools | كامِل تولز | An open-source Python toolkit for Arabic natural language processing. | مكتبة Python مفتوحة المصدر توفر أدوات لمعالجة العربية وتحليلها. | يستخدم Notebook 05 أدوات تطبيع عربية واختبارات سلوك محددة. |
| Normalisation profile | نورمَلايزيشن بروفايل | A named and versioned contract describing exactly which text transformations are applied. | عقد مسمى ومرقم يحدد تحويلات النص بالتفصيل. | `conservative-v1` يطبق في التدريب والتقييم والاستدلال. |
| Golden test | غولدِن تِست | A fixed input-output example used to detect an unintended behavioural change. | مثال ثابت نعرف نتيجته المتوقعة ويكشف تغير المعالجة. | يجب أن تعطي `الخدمــــة` النتيجة المتفق عليها في profile. |
| Train–inference consistency | ترين إنفِرَنس كَنسِستِنسي | Applying the same transformation contract during training and inference. | استخدام المعالجة نفسها عند التدريب وعند تشغيل النموذج لاحقًا. | لا نطبّع الألف في التدريب ثم نتركها دون تطبيع في الخدمة. |
| CAMeLBERT-DA | كامِل بِرت دي إيه | An Arabic BERT-family checkpoint pretrained with a focus on dialectal Arabic. | checkpoint من عائلة BERT للعربية وله تركيز على بيانات لهجية. | نقارنه بنموذج متعدد اللغات على شريحة خليجية مجمدة، ولا نفترض تفوقه مسبقًا. |
| Model comparison | مودِل كَمبارِسَن | A controlled evaluation of candidate models on the same data, metric, and decision rules. | مقارنة منضبطة بين نموذجين باستخدام البيانات والمقياس والقواعد نفسها. | نثبت الشريحة والبذرة ثم نقارن Macro-F1 والزمن. |
| Symmetric preprocessing | سِمِترِك بري بروسِسِنغ | Applying the same compatible text-processing contract to both indexed documents and incoming queries. | تطبيق عقد معالجة متوافق على وثائق الفهرس والاستعلامات معًا. | لا نطبّع corpus ونترك query بصيغة مختلفة. |

## B. Semantic search and sentence embeddings

مرتبط بـ[البحث الدلالي بتضمينات الجمل](02-semantic-search.md) و[Notebook 06](../notebooks/06_semantic_search.ipynb).

| English term | Pronunciation | English explanation | الشرح بالعربية | Example |
|---|---|---|---|---|
| Semantic search | سِمانتِك سيرتش | Retrieval based on meaning rather than exact keyword overlap alone. | استرجاع يعتمد على تقارب المعنى لا على تطابق الكلمات حرفيًا فقط. | يبحث «لم يصل رمز الدخول» فيجد حالة «مشكلة كود التحقق». |
| Information retrieval | إنفورميشن ريتريفَل | Finding and ranking relevant items from a collection in response to a query. | العثور على العناصر المناسبة من مجموعة وترتيبها استجابةً لاستعلام. | يسترجع «بيان» الحالات الأقرب لسؤال المستخدم. |
| Corpus | كوربَس | The collection of documents or cases available for search or analysis. | مجموعة النصوص أو الحالات التي نبني عليها البحث. | 24 حالة خدمة اصطناعية تمثل corpus المختبر. |
| Query | كويري | The text expressing what a search user wants to find. | نص الاستعلام الذي يصف حاجة الباحث. | «كيف أسترجع رقم الطلب؟». |
| Document | دوكيومِنت | An item in the searchable collection. | عنصر داخل مجموعة البحث وقد يكون حالة أو فقرة أو صفحة. | وصف إجراء استرجاع الرقم document قابل للاسترجاع. |
| Sentence embedding | سِنتِنس إمبِدِنغ | A dense vector representing the meaning of a sentence or short passage. | متجه رقمي يمثل معنى جملة أو مقطع كامل. | يحول المشفر سؤالًا عربيًا إلى متجه من 384 قيمة. |
| Token embedding | توكِن إمبِدِنغ | A vector representing one token, often in context. | متجه يمثل token واحدة، ولا يساوي تلقائيًا تمثيل الجملة كاملة. | مخرجات كل موضع في BERT هي token embeddings سياقية. |
| Bi-encoder | باي إنكودر | A model that encodes queries and documents separately into comparable vectors. | نموذج يشفّر الاستعلام والوثيقة بصورة منفصلة، فيسمح بحساب الوثائق مسبقًا. | نحسب embeddings للحالات مرة، ثم نشفّر كل query عند البحث. |
| Cross-encoder | كروس إنكودر | A model that jointly reads a query-document pair and predicts a relevance score. | نموذج يقرأ الاستعلام والمرشح معًا ليعطي درجة صلة أدق غالبًا وأغلى. | نمرر query مع أفضل خمسة مرشحين فقط لإعادة ترتيبهم. |
| Re-ranking | ري رانكِنغ | Reordering an initial candidate list using a more expensive scoring model. | إعادة ترتيب نتائج أولية باستخدام نموذج أدق. | يسترجع bi-encoder أفضل 10 ثم يعيد cross-encoder ترتيبها. |
| Candidate | كاندِديت | An item selected by the first retrieval stage for possible final ranking. | نتيجة مرشحة من المرحلة الأولى قد تصبح ضمن الإجابات النهائية. | أفضل 10 حالات من FAISS هي candidates. |
| Dense vector | دِنس فِكتور | A numeric vector in which most components carry values. | متجه رقمي كثيف أغلب قيمه غير صفرية. | sentence embedding بطول 384 متجه كثيف. |
| Cosine similarity | كوساين سِمِلاريتي | A measure of the angle between two vectors, independent of their magnitudes. | مقياس يقارن اتجاه متجهين ويستخدم كثيرًا للتشابه الدلالي. | كلما اقترب الاتجاهان من بعضهما ارتفعت درجة التشابه. |
| L2 normalisation | إل تو نورمَلايزيشن | Scaling a vector so its Euclidean length becomes one. | تقسيم المتجه على طوله ليصبح طوله واحدًا. | نطبع corpus وquery قبل استخدام inner product لمحاكاة cosine ranking. |
| Inner product | إنَر برودَكت | The sum of pairwise products between vector components. | مجموع حاصل ضرب القيم المتقابلة في متجهين. | بعد L2 normalisation يساوي inner product تشابه cosine. |
| Vector index | فِكتور إندكس | A data structure that stores vectors and supports nearest-neighbour search. | بنية تخزن المتجهات وتبحث عن الأقرب منها. | يحتوي فهرس «بيان» embeddings الحالات ومعرفاتها. |
| FAISS | فايس | A library for efficient similarity search and clustering of dense vectors. | مكتبة للبحث السريع في المتجهات الكثيفة وتجميعها. | يستخدم المختبر نسخة CPU من FAISS بلا خدمة مدفوعة. |
| IndexFlatIP | إندكس فلات آي بي | An exact FAISS index that ranks vectors by inner product without approximation. | فهرس FAISS دقيق يقارن الاستعلام بجميع المتجهات وفق inner product. | نستخدمه baseline لأن بيانات الدورة صغيرة. |
| Exact search | إكزاكت سيرتش | Search that evaluates every indexed vector under the chosen similarity measure. | بحث دقيق لا يستخدم تقريبًا، لكنه قد يصبح مكلفًا مع الملايين. | `IndexFlatIP` يعيد الترتيب الدقيق على corpus الصغير. |
| Approximate Nearest Neighbour (ANN) | أبروكسِمِت نيرِست نيبر | Search that trades some exactness for speed or memory at large scale. | بحث تقريبي يضحي بجزء محتمل من الاستدعاء مقابل سرعة أو حجم أفضل. | HNSW امتداد Explore ولا يلزم للـCore الصغير. |
| Top-k | توب كي | The first k items in a ranked result list. | أعلى عدد `k` من النتائج المرتبة. | `top_k=3` يعيد أفضل ثلاث حالات. |
| Bilingual search | باي لِنغوَل سيرتش | Search supporting two languages in queries, documents, or both. | بحث يدعم لغتين مثل العربية والإنجليزية. | استعلام عربي قد يبحث في حالات عربية وإنجليزية. |
| Cross-lingual retrieval | كروس لِنغوَل ريتريفَل | Retrieval where a relevant document may be written in a different language from the query. | استرجاع يمكن أن تكون فيه لغة النتيجة مختلفة عن لغة السؤال. | سؤال عربي يسترجع إجراءً إنجليزيًا ذا معنى مطابق. |
| Relevant document | رِلِفَنت دوكيومِنت | A document labelled as satisfying the information need of a query. | وثيقة مصنفة بأنها مناسبة لحاجة الاستعلام. | يحوي `relevant_ids` معرف الحالة الصحيحة لكل query. |
| Recall@k | ريكول أت كي | The fraction of queries for which at least one relevant item appears in the top k. | نسبة الاستعلامات التي ظهر لها عنصر صحيح ضمن أول `k` نتائج. | إذا ظهر الصحيح ضمن أول 3 في 8 من 10 استعلامات فـRecall@3 تساوي 0.8. |
| Reciprocal rank | رِسِبرُكَل رانك | The inverse of the rank of the first relevant result. | مقلوب ترتيب أول نتيجة صحيحة. | الصحيح في المرتبة 2 يعطي reciprocal rank تساوي 0.5. |
| Mean Reciprocal Rank (MRR@k) | مين رِسِبرُكَل رانك | The average reciprocal rank of the first relevant result, limited to the top k. | متوسط مقلوب رتبة أول نتيجة صحيحة ضمن أول `k`. | الصحيح في المرتبة الأولى يكافأ أكثر من ظهوره في الثالثة. |
| MRR | إم آر آر | The common abbreviation for Mean Reciprocal Rank. | الاختصار الشائع لمتوسط الرتبة المقلوبة. | يعرض التقرير `MRR@3` عندما نحصر القياس في أول ثلاث نتائج. |
| Similarity threshold | سِمِلاريتي ثرِشولد | A score boundary used to accept or reject a retrieved result. | حد للدرجة نقرر بعده قبول النتيجة أو الامتناع. | إذا كانت أفضل درجة أقل من `min_score` نرجع no-answer. |
| No-answer retrieval | نو آنسَر ريتريفَل | A search outcome that declines to return an unsupported result. | قرار بحث يمتنع عن تقديم نتيجة عندما لا توجد صلة كافية. | سؤال خارج نطاق corpus يجب ألا يُجبر على أقرب حالة ضعيفة. |
| Index manifest | إندكس مانِفِست | Metadata recording how a vector index was built and what it is compatible with. | ملف يسجل النموذج وprofile والبيانات والبعد وعدد المتجهات. | يمنع تشغيل query encoder مختلف على فهرس قديم بصمت. |
| Embedding dimension | إمبِدِنغ دِمِنشن | The number of components in each indexed embedding. | عدد القيم في كل متجه، ويجب أن يطابق الفهرس والاستعلام. | النموذج المستخدم في المختبر ينتج بعدًا مثل 384. |
| Vector count | فِكتور كاونت | The number of vectors stored in an index. | عدد المتجهات المسجلة في الفهرس. | فهرس 24 حالة يجب أن يسجل `vector_count=24`. |

## C. Evaluation and error analysis

مرتبط بـ[التقييم وتحليل الأخطاء](03-evaluation-error-analysis.md) و[Notebook 07](../notebooks/07_evaluation_error_analysis.ipynb).

| English term | Pronunciation | English explanation | الشرح بالعربية | Example |
|---|---|---|---|---|
| Evaluation | إفاليويشن | A defined process for measuring a system against labelled data and stated criteria. | عملية مقننة تقيس النظام على بيانات ومعايير معلنة. | نحسب Recall@3 على queries مجمدة ذات إجابات معروفة. |
| Aggregate metric | أغريغِت مِترك | A single score summarising performance over many examples. | رقم إجمالي يلخص الأداء وقد يخفي اختلاف الشرائح. | Recall الكلي قد يبدو جيدًا رغم ضعف Arabizi. |
| Evaluation slice | إفاليويشن سلايس | A meaningful subset evaluated separately to expose uneven performance. | شريحة بيانات تُقاس منفصلة مثل اللغة أو اللهجة أو الطول. | نقارن نتائج MSA وGulf وArabizi. |
| Sliced evaluation | سلايست إفاليويشن | Reporting metrics across predefined evaluation slices. | عرض المقاييس على شرائح محددة بدل الاكتفاء بمتوسط واحد. | جدول يبين F1 لكل `variant` و`language`. |
| Confidence interval (CI) | كونفِدِنس إنتِرفَل | A range that expresses sampling uncertainty around an estimated metric. | نطاق يعبر عن عدم اليقين حول المقياس بسبب محدودية العينة. | `0.72–0.86` أوضح من رقم `0.79` وحده. |
| Bootstrap | بوتستراب | Resampling examples with replacement to estimate uncertainty. | إعادة سحب أمثلة مع الإرجاع مرات عديدة لتقدير تذبذب المقياس. | نحسب Recall على 1,000 resamples من مجموعة التقييم. |
| Paired bootstrap | بيرد بوتستراب | Bootstrap comparison that resamples the same example indices for both systems. | مقارنة تعيد أخذ الفهارس نفسها للنموذجين حتى نحافظ على اقتران الأمثلة. | نحسب CI لفرق MRR بين baseline وreranker. |
| Paired comparison | بيرد كَمبارِسَن | A comparison in which two systems are evaluated on the same examples. | مقارنة نموذجين على الأمثلة نفسها حتى لا يكون الفرق ناتجًا من عينات مختلفة. | نقارن baseline وcandidate لكل query قبل تلخيص الفرق. |
| Macro-F1 | ماكرو إف وَن | The unweighted mean of F1 scores computed separately for each class. | متوسط F1 للفئات بعد منحها وزنًا متساويًا. | يعرض Notebook 07 Macro-F1 مع CI بدل Accuracy وحدها. |
| Behavioural test | بِهيفيورَل تِست | A targeted example that checks a specific linguistic or system behaviour. | اختبار مركز يفحص سلوكًا بعينه بدل متوسط عام. | مثال نفي يتأكد أن «لم يتم الحل» لا يعامل مثل «تم الحل». |
| Regression test | ريغريشن تِست | A test that ensures a previously fixed behaviour does not break again. | اختبار يمنع عودة خطأ سبق إصلاحه. | بعد إصلاح Arabizi نثبت المثال كاختبار دائم. |
| Error analysis | إيرَر أنالِسِس | Systematic inspection and grouping of failures to guide improvements. | قراءة الأخطاء وتصنيفها لاختيار إصلاحات مفيدة. | نفحص queries الفاشلة ونحدد هل السبب preprocessing أو ranking. |
| Error taxonomy | إيرَر تاكسونَمي | A controlled set of labels used to categorise error causes or symptoms. | قائمة تصنيفات منظمة للأخطاء، وتمثل فرضيات بشرية قابلة للمراجعة. | `dialect_gap` و`negation` و`class_confusion`. |
| Label noise | لايبل نويز | Incorrect, inconsistent, or ambiguous ground-truth annotations. | أخطاء أو تناقضات في labels الصحيحة نفسها. | وثيقة مناسبة وُسمت خطأ على أنها غير ذات صلة. |
| Class confusion | كلاس كونفيوجن | A repeated pattern in which one class is predicted as another. | نمط يخلط فيه النموذج بين فئتين. | يخلط بين «شكوى» و«طلب خدمة». |
| Dialect gap | دايَلِكت غاب | A performance gap associated with dialectal language not well covered by the system. | ضعف مرتبط بصيغ لهجية لا يغطيها النموذج أو البيانات جيدًا. | تنجح MSA ويفشل تعبير خليجي يؤدي المعنى نفسه. |
| Entity-boundary error | إنتِتي باوندري إيرَر | A NER failure caused by an incorrect entity start or end. | خطأ في بداية الكيان أو نهايته. | استخراج «وزارة» بدل «وزارة الصحة». |
| Negation error | نِغيشن إيرَر | A failure to preserve or interpret a negation cue correctly. | خطأ يجعل النظام يتجاهل النفي أو يعكس المعنى. | يساوي بين «تم الحل» و«لم يتم الحل». |
| Truncation error | ترانكيشن إيرَر | A failure caused by removing a relevant part of an overlength input. | خطأ سببه قطع الجزء الذي يحمل المعلومة المطلوبة. | تقع الإجابة بعد `max_length` فلا تصل إلى النموذج. |
| Hard or ambiguous case | هارد أور أمبيغيوَس كيس | An example with genuinely difficult or multiple plausible interpretations. | مثال صعب أو يحتمل أكثر من تفسير معقول. | طلب قصير مثل «ما اشتغل» من دون ذكر الخدمة. |
| Small slice | سمول سلايس | An evaluation slice too small for a stable strong conclusion. | شريحة قليلة الأمثلة يجب تفسيرها بحذر. | شريحة من ثلاثة أمثلة توسم `SMALL_SLICE`. |
| Validation wall | فالِديشن وول | A strict separation that keeps tuning decisions on validation and reserves test for final evaluation. | حاجز يمنع ضبط القرارات على الاختبار النهائي. | نضبط `min_score` على validation ثم نثبت القيمة قبل test. |
| Model card | مودِل كارد | A report describing model use, evaluation, limitations, and risks. | وثيقة تلخص استخدام النموذج ونتائجه وحدوده ومخاطره. | توضح البطاقة ضعف Arabizi وعدم ملاءمة النموذج لقرار حساس مستقل. |
| Data card | داتا كارد | Documentation of dataset sources, fields, licence, privacy, construction, and limitations. | وثيقة تشرح مصدر البيانات وترخيصها وحقولها وخصوصيتها وحدودها. | تذكر أن بيانات الدورة اصطناعية ولا تحتوي بيانات مستفيدين حقيقية. |
| Course fixture | كورس فِكستشر | A provided deterministic dataset or output used for instruction and testing. | ملف ثابت مقدم ضمن الدورة لتشغيل التمارين واختبارها. | `bayan_day3_predictions.csv` يحمل الوسم `COURSE_FIXTURE`. |
| Evidence provenance | إفِدِنس بروفِنَنس | Traceable information showing where a metric, prediction, or artefact came from. | معلومات توضح مصدر النتيجة أو التنبؤ وكيف أُنشئ. | يذكر التقرير هل التنبؤ `COURSE_FIXTURE` أم ناتج تشغيل نموذج فعلي. |
| Threshold tuning | ثرِشولد تيونِنغ | Selecting a decision threshold using validation data only. | اختيار حد القرار على validation فقط ثم تثبيته قبل test. | نضبط `min_score` للـno-answer ثم لا نغيره بعد فتح الاختبار. |
| `MEASURED_SMOKE` | ميجَرد سموك | A real measured result from a small instructional workload, insufficient for production claims. | نتيجة حقيقية مقاسة على عينة تعليمية صغيرة ولا تثبت الجاهزية الإنتاجية. | نتيجة Notebook 06 تعرض بهذا الوسم. |
| `SMALL_SLICE` | سمول سلايس | A warning label showing that a slice contains too few examples for a stable claim. | تنبيه صريح بأن حجم الشريحة صغير ولا يدعم تعميمًا قويًا. | يظهر بجانب CI شريحة Arabizi قليلة الأمثلة. |
| Gate C | غيت سي | The Day 3 checkpoint for Arabic processing, retrieval, evaluation, and documented decisions. | بوابة اليوم الثالث التي تربط البحث بالأدلة وتحليل الأخطاء. | تتطلب manifest وRecall/MRR وsliced report وقرارات موثقة. |

## مراجعة سريعة | Quick review

قبل Gate C يجب أن يستطيع المتدرب شرح الفرق بين:

1. `Root` و`Stem` و`Lemma`.
2. `MSA` و`Dialect` و`Arabizi`.
3. `Token embedding` و`Sentence embedding`.
4. `Bi-encoder` و`Cross-encoder` و`Re-ranking`.
5. `Cosine similarity` و`L2 normalisation` و`Inner product`.
6. `Recall@k` و`MRR@k`.
7. `Aggregate metric` و`Evaluation slice`.
8. `Bootstrap` و`Paired bootstrap`.
9. `Error taxonomy` وسبب الخطأ المؤكد.

[العودة إلى صفحة اليوم الثالث](README.md) · [قاموس الدورة الكامل](../docs/glossary/README.md) · [مراجع اليوم الثالث](REFERENCES.md)
