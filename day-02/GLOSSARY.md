# قاموس اليوم الثاني | Day 2 Glossary

**اجعل النموذج متخصصًا | Make the Model Yours**  
**إعداد وتقديم | Prepared and delivered by:** ميعاد المري · Meaad Al-Marri

يجمع هذا القاموس المصطلحات التي تظهر في صفحات اليوم الثاني ودفترَي التصنيف وNER/QA. يبدأ كل صف بالمصطلح الإنجليزي، ثم النطق التقريبي، وشرح بالإنجليزية، وشرح عربي مبسط، ومثال من مسار «بيان».

> نتائج العينات الصغيرة في هذا اليوم تثبت سلامة التنفيذ فقط، وتسمى `MEASURED_SMOKE` ولا تمثل جودة إنتاجية.

## A. Fine-tuning and classification

مرتبط بـ[Fine-tuning والتصنيف](01-fine-tuning-classification.md) و[Notebook 03](../notebooks/03_text_classification.ipynb).

| English term | Pronunciation | English explanation | الشرح بالعربية | Example |
|---|---|---|---|---|
| Pretraining | بري ترينِنغ | General-purpose training on a large corpus before adaptation to a specific task. | تدريب عام واسع يسبق تخصيص النموذج لمهمة محددة. | يتعلم BERT أنماط اللغة قبل أن ندرّبه على فئات طلبات «بيان». |
| Fine-tuning | فاين تيونِنغ | Updating pretrained model parameters using labelled data for a target task. | تحديث أوزان نموذج مدرّب مسبقًا باستخدام بيانات المهمة وتصنيفاتها. | نضبط المشفر ورأس التصنيف على موضوع الطلب. |
| Task head | تاسك هِد | A task-specific output layer placed on top of a shared encoder. | طبقة إخراج خاصة بالمهمة تُضاف فوق المشفر العام. | رأس تصنيف للموضوع، ورأس مستقل للمشاعر، ورأس token classification لـNER. |
| Text classification | تِكست كلاسِفِكيشن | Assigning one label or a set of labels to a complete text. | إسناد فئة واحدة أو أكثر إلى النص كاملًا. | تصنيف الطلب إلى خدمة أو شكوى أو استفسار. |
| Label | لايبل | The target category or annotation associated with a training example. | التصنيف الصحيح المرتبط بالمثال. | `service_request` هو label لنص يطلب خدمة. |
| Sentiment | سِنتِمِنت | The expressed attitude or polarity in a text, modelled as a separate target when required. | الانطباع أو النبرة مثل إيجابي أو سلبي، ويُعامل كرأس مستقل إذا كانت المهمة تطلبه. | نص شكوى قد يكون موضوعه «خدمة» ومشاعره «سلبي». |
| Logit | لوجِت | A raw model output score produced before conversion to probabilities. | درجة خام ينتجها النموذج قبل تحويلها إلى احتمالات. | يطبق `argmax` على logits لاختيار الفئة الأعلى. |
| Probability | برُبابِلِتي | A normalised value between zero and one representing model confidence under its output rule. | قيمة بين صفر وواحد تمثل ثقة النموذج وفق طريقة التحويل. | يحول Softmax logits إلى probabilities مجموعها واحد. |
| Baseline | بيس لاين | A simple reference system used to judge whether added complexity provides value. | حل مرجعي بسيط نقارن به النموذج المعقد. | نقارن Transformer بخط أساس TF-IDF مع مصنف خطي. |
| TF-IDF | تي إف آي دي إف | A sparse text representation that weights terms by local frequency and corpus rarity. | تمثيل يعطي الكلمة وزنًا أعلى إذا تكررت في نص وقل انتشارها في بقية النصوص. | قد تحصل «فاتورة» على وزن مفيد لتمييز فئة الفوترة. |
| Sparse vector | سبارس فِكتور | A vector in which most values are zero. | متجه معظم قيمه أصفار، وهو شائع في TF-IDF. | نص قصير يستخدم عددًا قليلًا من مفردات القاموس الكبير. |
| Linear classifier | لينيَر كلاسِفاير | A classifier that separates classes using weighted linear combinations of features. | مصنف يتعلم أوزانًا للخصائص ويستخدم حدًا خطيًا للفصل. | Logistic Regression فوق TF-IDF خط أساس مناسب. |
| Frozen encoder | فروزِن إنكودر | An encoder whose pretrained weights are not updated during task training. | مشفر تبقى أوزانه ثابتة وندرب الرأس فقط. | عند غياب GPU ندرّب `task head` على CPU مع تجميد encoder. |
| Full fine-tuning | فُل فاين تيونِنغ | Updating both the encoder and the task head during training. | تحديث أوزان المشفر والرأس معًا. | يستخدم `full_finetune` عندما تتوفر الموارد ونريد تكييفًا أعمق. |
| Training set | ترينِنغ سِت | Data used to update model parameters. | البيانات التي يتعلم منها النموذج وتُحدث عليها الأوزان. | أمثلة الطلبات المخصصة للتدريب فقط. |
| Validation set | فالِديشن سِت | Held-out data used to select settings and make development decisions. | بيانات لا تدرب عليها الأوزان، وتستخدم لاختيار الإعدادات والقرارات. | نختار epoch الأفضل وفق Macro-F1 على validation. |
| Frozen test set | فروزِن تِست سِت | A final held-out set that must not guide model selection or tuning. | مجموعة اختبار نهائية لا تُفتح لاتخاذ قرارات التطوير. | نقيّمها مرة بعد تثبيت النموذج والthreshold. |
| Split contract | سبليت كونتراكت | A documented rule defining how examples are assigned to train, validation, and test. | عقد يحدد طريقة التقسيم ويمنع التداخل بين المجموعات. | يقسم المشروع حسب `group_id` لا حسب الصفوف عشوائيًا فقط. |
| Group ID | غروب آي دي | An identifier linking related examples that must remain in the same split. | معرف يجمع الأمثلة المرتبطة حتى لا تتوزع على التدريب والاختبار. | رسائل القضية نفسها تحمل `group_id` واحدًا. |
| Data leakage | داتا ليكِج | Information from validation or test improperly influencing training or model selection. | وصول معلومة من التحقق أو الاختبار إلى التدريب، فتظهر نتيجة مضللة. | وجود رسالتين من القضية نفسها في train وtest تسرب بيانات. |
| Group overlap | غروب أوفرلاب | The presence of the same group identifier in more than one data split. | ظهور المجموعة نفسها في أكثر من تقسيم، ويجب أن يساوي صفرًا. | `group_overlap=0` شرط صحة قبل التدريب. |
| Epoch | إيبُك | One complete pass through the training set. | مرور كامل على بيانات التدريب. | ثلاث epochs تعني مشاهدة مجموعة التدريب ثلاث مرات. |
| Batch | باتش | A subset of examples processed before one optimisation update. | مجموعة صغيرة من الأمثلة تُعالج قبل تحديث الأوزان. | `batch_size=8` يشغّل ثمانية نصوص في الخطوة. |
| Learning rate | ليرنِنغ ريت | The step size used when updating model parameters. | حجم خطوة تحديث الأوزان؛ الكبير قد يزعزع التدريب والصغير قد يبطئه. | نسجل `2e-5` مع بقية إعدادات التجربة. |
| Hyperparameter | هايبر بَرامِتر | A training or model setting chosen rather than learned directly from data. | إعداد نختاره نحن ولا يتعلمه النموذج مباشرة. | Learning rate وbatch size وعدد epochs hyperparameters. |
| Optimiser | أوبتِمايزر | An algorithm that updates parameters using computed gradients. | خوارزمية تستخدم gradients لتعديل أوزان النموذج. | `AdamW` شائع في Fine-tuning نماذج Transformer. |
| Gradient | غريديَنت | The derivative signal indicating how parameters should change to reduce loss. | إشارة رياضية توضح اتجاه تعديل الأوزان لتقليل الخطأ. | يحسب Backpropagation gradients بعد loss. |
| Backpropagation | باك بروبَغيشن | The algorithm that propagates loss derivatives backward through a network to compute gradients. | خوارزمية تمرر أثر الخطأ عكسيًا عبر الشبكة لحساب gradients. | بعد forward pass نحسب loss ثم Backpropagation. |
| Loss | لوس | A differentiable training objective that quantifies prediction error. | دالة رقمية يستخدمها التدريب لقياس الخطأ وتحديث الأوزان. | انخفاض loss علامة صحة أولية، وليس دليل جودة كافيًا. |
| Weight decay | ويت دِكاي | A regularisation term that discourages excessively large parameter values during optimisation. | أسلوب تنظيم يحد من تضخم الأوزان أثناء التدريب. | نسجل قيمة weight decay ضمن إعدادات AdamW. |
| Random seed | راندم سيد | A value used to initialise pseudo-random operations for more repeatable experiments. | قيمة تبدأ العمليات شبه العشوائية لتحسين قابلية إعادة التجربة. | نستخدم seed ثابتة عند التقسيم والتدريب، مع معرفة أنها لا تضمن تطابق كل GPU. |
| Overfitting | أوفر فِتِنغ | Learning the training data too specifically and failing to generalise. | حفظ تفاصيل التدريب على حساب الأداء على بيانات جديدة. | تتحسن train loss بينما تتراجع validation Macro-F1. |
| Class imbalance | كلاس إمبالَنس | A dataset condition in which some labels have many more examples than others. | عدم توازن عدد الأمثلة بين الفئات. | وجود 80 طلب خدمة مقابل 10 شكاوى قد يجعل Accuracy مضللة. |
| Accuracy | أكيورَسي | The proportion of predictions that exactly match their labels. | نسبة التوقعات الصحيحة من جميع الأمثلة. | 90 توقعًا صحيحًا من 100 تعني Accuracy تساوي 0.90. |
| Precision | بريسيجن | The proportion of predicted positives that are truly positive. | من الحالات التي توقعها النموذج كفئة معينة، كم حالة كانت صحيحة؟ | إذا توقع 10 شكاوى وكانت 8 صحيحة فـPrecision تساوي 0.8. |
| Recall | ريكول | The proportion of true positives that the model successfully retrieves. | من جميع الحالات الحقيقية لفئة معينة، كم حالة اكتشفها النموذج؟ | إذا كانت 10 شكاوى حقيقية واكتشف 7 فـRecall تساوي 0.7. |
| F1 score | إف وَن سكور | The harmonic mean of precision and recall. | متوسط توافقي يوازن بين Precision وRecall. | عندما يساوي كلاهما 0.8 تصبح F1 تساوي 0.8. |
| Macro-F1 | ماكرو إف وَن | The unweighted mean of per-class F1 scores. | نحسب F1 لكل فئة ثم نعطي جميع الفئات وزنًا متساويًا. | لا تستطيع الفئة الكبيرة إخفاء ضعف النموذج في فئة صغيرة. |
| Confusion matrix | كونفيوجن ميتريكس | A table comparing true classes with predicted classes. | جدول يوضح الفئات التي يخلط النموذج بينها. | يكشف أن «شكوى» تُصنف كثيرًا على أنها «استفسار». |
| True Positive (TP) | ترو بوزِتِف | A positive prediction that matches a positive reference label. | حالة إيجابية توقعها النموذج بطريقة صحيحة. | توقع شكوى وكانت الحقيقة شكوى. |
| False Positive (FP) | فولس بوزِتِف | A positive prediction made for a reference that is not positive. | حالة توقعها النموذج إيجابية بينما الحقيقة ليست كذلك. | توقع شكوى لحالة استفسار. |
| False Negative (FN) | فولس نيغَتِف | A positive reference case that the model fails to identify. | حالة إيجابية حقيقية لم يكتشفها النموذج. | كانت الحالة شكوى لكن النموذج صنفها استفسارًا. |
| Support | سَبورت | The number of true examples belonging to a class in an evaluation set. | عدد الأمثلة الحقيقية لكل فئة داخل التقييم. | إذا احتوى test على 12 شكوى فـsupport فئة الشكوى يساوي 12. |
| CPU | سي بي يو | A general-purpose processor that can run training and inference, usually more slowly for large neural workloads. | المعالج العام؛ يمكنه تشغيل المسار المصغر لكن تدريب Transformer الكامل قد يكون أبطأ. | عند عدم توفر GPU نستخدم frozen encoder ومسار CPU. |
| GPU | جي بي يو | A parallel processor well suited to tensor operations in neural networks. | معالج متوازٍ يسرع عمليات الشبكات العصبية، لكنه غير مضمون في Colab المجاني. | يختار الدفتر GPU تلقائيًا إذا كان متاحًا. |
| Smoke training | سموك ترينِنغ | A deliberately small training run that checks the pipeline without establishing final model quality. | تدريب مصغر يثبت سلامة البيانات وloss والتحديث، ولا يثبت الجاهزية الإنتاجية. | خطوة أو epoch صغيرة تنتهي بعلامة `MEASURED_SMOKE`. |

## B. Named Entity Recognition and BIO alignment

مرتبط بـ[NER ومحاذاة BIO](02-ner-label-alignment.md) و[Notebook 04](../notebooks/04_ner_and_qa.ipynb).

| English term | Pronunciation | English explanation | الشرح بالعربية | Example |
|---|---|---|---|---|
| Named Entity Recognition (NER) | نيمد إنتِتي ريكَغنِشن | Identifying spans of text and assigning entity types to them. | اكتشاف مقاطع تمثل كيانات وتسميتها مثل مؤسسة أو موقع أو تاريخ. | في «راجعت وزارة الصحة أمس» نستخرج «وزارة الصحة» كـORG و«أمس» كـDATE. |
| Named Entity | نيمد إنتِتي | A real or conceptual item mentioned by a text span and assigned a type. | اسم أو معلومة محددة داخل النص تُعطى نوعًا. | «الرياض» كيان من نوع LOCATION. |
| Span | سبان | A contiguous region of text defined by start and end boundaries. | مقطع متصل من النص له بداية ونهاية. | «وزارة الصحة» Span من كلمتين. |
| Entity boundary | إنتِتي باوندري | The exact start and end positions of an entity span. | الحدود الدقيقة لبداية الكيان ونهايته. | توقع «وزارة» بدل «وزارة الصحة» خطأ حدود. |
| BIO scheme | بي آي أو سْكيم | A tagging scheme using B for beginning, I for inside, and O for outside an entity. | مخطط وسم يستخدم B للبداية وI للداخل وO لخارج الكيان. | `B-ORG I-ORG O` يمثل مؤسسة من كلمتين ثم كلمة خارجها. |
| B tag | بي تاغ | A label marking the first token of an entity. | وسم بداية الكيان. | «وزارة» تحمل `B-ORG`. |
| I tag | آي تاغ | A label marking a continuation token inside the same entity. | وسم استمرار داخل الكيان نفسه. | «الصحة» تحمل `I-ORG`. |
| O tag | أو تاغ | A label marking a token outside every entity. | وسم كلمة لا تنتمي إلى كيان. | «راجعت» تحمل `O`. |
| Subword continuation | سَب وورد كونتِنيويشن | A tokenizer piece that continues a word already represented by an earlier piece. | جزء tokenizer يكمل الكلمة نفسها بعد الجزء الأول. | الأجزاء اللاحقة من كلمة مقسمة لا تحصل على بداية كيان جديدة. |
| Label alignment | لايبل ألاينمِنت | Mapping word-level labels to the tokenised subword sequence. | ربط وسوم الكلمات بالتسلسل الجديد بعد تقسيم الكلمات إلى subwords. | نعطي أول subword وسم الكلمة ونتجاهل بقية أجزائها في loss. |
| `word_ids()` | وورد آي ديز | A fast-tokenizer mapping from token positions back to original word indices. | خريطة تعيد كل token إلى رقم الكلمة الأصلية أو `None` للرموز الخاصة. | القيم `[None, 0, 1, 1, None]` تكشف أن الموضعين 2 و3 للكلمة نفسها. |
| Ignore index (`-100`) | إغنور إندكس | A target value conventionally ignored by PyTorch cross-entropy loss. | قيمة تجعل loss يتجاوز مواضع الرموز الخاصة والأجزاء اللاحقة. | `[CLS]` و`[SEP]` وcontinuation subwords تحصل على `-100`. |
| `label2id` | لايبل تو آي دي | A mapping from readable label names to numeric model identifiers. | قاموس يحول اسم الوسم إلى رقم يفهمه النموذج. | يحول `B-ORG` إلى رقم ثابت موثق. |
| `id2label` | آي دي تو لايبل | The inverse mapping from numeric identifiers to readable label names. | قاموس يعيد رقم التوقع إلى اسم الوسم. | يحول رقم التوقع إلى `B-LOCATION` عند التقرير. |
| Strict entity-level F1 | ستريكت إنتِتي لِفِل إف وَن | F1 computed from entities that match exactly in type, start, and end. | F1 صارمة لا تحتسب الكيان صحيحًا إلا إذا تطابق نوعه وبدايته ونهايته. | الحقيقة «وزارة الصحة» والتوقع «وزارة» يعطيان strict F1 صفرًا لهذا الكيان. |
| Token accuracy | توكِن أكيورَسي | Accuracy computed independently over token labels. | دقة وسوم الكلمات منفردة، وقد تخفي فشل الحدود بسبب كثرة `O`. | توقع `O` لمعظم الكلمات قد يعطي دقة مرتفعة مع Recall كيانات يساوي صفرًا. |
| End-exclusive index | إند إكسكلوسِف إندكس | An end position that points immediately after the final included item. | فهرس نهاية يشير إلى الموضع التالي لآخر عنصر داخل span. | الكيان في الفهرسين 1 و2 يمثّل بالحدود `(1, 3)`. |
| Arabic clitic | آرابِك كْلِتِك | A short grammatical element attached to a word in Arabic writing. | حرف أو أداة قصيرة تلتصق بالكلمة مثل الواو والباء. | «وبالرياض» تضم الواو والباء واسم الموقع في كتابة واحدة. |

## C. Extractive question answering

مرتبط بـ[الإجابة الاستخراجية عن الأسئلة](03-extractive-qa.md) و[Notebook 04](../notebooks/04_ner_and_qa.ipynb).

| English term | Pronunciation | English explanation | الشرح بالعربية | Example |
|---|---|---|---|---|
| Question Answering (QA) | كويستشن آنسَرِنغ | A task in which a system produces or selects an answer to a question. | مهمة يجيب فيها النظام عن سؤال بالاعتماد على سياق أو معرفة محددة. | سؤال: «أين قُدم الطلب؟» والإجابة من سياق الحالة. |
| Extractive QA | إكستراكتِف كيو إيه | QA that selects an answer span directly from the supplied context. | إجابة استخراجيّة تختار مقطعًا موجودًا حرفيًا في السياق. | يستخرج النظام «الرياض» من النص بدل كتابة إجابة جديدة. |
| Context | كونتِكست | The passage supplied to the QA model as the source of a possible answer. | النص المرجعي الذي يبحث النموذج داخله عن الإجابة. | وصف حالة الدعم هو `context`. |
| Question | كويستشن | The information request paired with a context. | السؤال الذي نريد العثور على إجابته داخل السياق. | «متى تم إغلاق الطلب؟». |
| Answer text | آنسَر تِكست | The exact text span used as the labelled answer. | النص الحرفي للإجابة الصحيحة. | `answer_text="أمس"`. |
| Answer start | آنسَر ستارت | The character offset at which the labelled answer begins in the context. | رقم المحرف الذي تبدأ عنده الإجابة داخل السياق. | إذا بدأت «الرياض» عند المحرف 18 فالقيمة `answer_start=18`. |
| Character offset | كارَكتر أوفست | A position measured in characters within the original string. | موضع محسوب بعدد المحارف في النص الأصلي. | البداية 18 والنهاية 24 تحددان موضع «الرياض». |
| Offset mapping | أوفست مابِنغ | A mapping from each token to its character start and end positions in the original text. | خريطة تربط كل token بحدود المحارف التي جاء منها. | نستخدم `offset_mapping` لتحويل موضع الإجابة من محارف إلى tokens. |
| `sequence_ids()` | سيكوانس آي ديز | A tokenizer mapping that identifies whether a token belongs to the question, context, or neither. | خريطة تميز tokens السؤال عن Tokens السياق والرموز الخاصة. | نقبل بداية الإجابة فقط في المواضع التابعة للسياق. |
| Long context | لونغ كونتِكست | A context whose tokenised length exceeds the model input limit. | سياق يتجاوز بعد التجزئة الحد الذي يستطيع النموذج إدخاله مرة واحدة. | تقرير طويل يتجاوز 384 token يحتاج نوافذ متداخلة. |
| Sliding window | سلايدِنغ وِندو | Splitting a long context into overlapping token windows. | تقسيم السياق الطويل إلى نوافذ متداخلة حتى لا تضيع الإجابة قرب القطع. | نوافذ طولها 384 مع تداخل `stride=128`. |
| Stride | سترايد | The overlap retained between consecutive windows of a long context. | مقدار التداخل بين نافذتين متتاليتين. | آخر 128 token من نافذة تظهر أيضًا في التالية. |
| `truncation="only_second"` | ترانكيشن أونلي سِكند | A paired-input rule that truncates only the second sequence, normally the context. | قاعدة تقطع السياق عند الحاجة وتحافظ على السؤال. | في زوج السؤال والسياق لا نريد حذف كلمات السؤال. |
| Start logits | ستارت لوجِتس | Raw model scores for each token being the answer start. | درجات خام لاحتمال أن يكون كل token بداية الإجابة. | نرشح مواضع البداية ذات الدرجات الأعلى. |
| End logits | إند لوجِتس | Raw model scores for each token being the answer end. | درجات خام لاحتمال أن يكون كل token نهاية الإجابة. | نختار نهاية تأتي بعد البداية وضمن الطول المسموح. |
| Valid span | فالِد سبان | A candidate answer whose start, end, sequence, and length obey all constraints. | إجابة مرشحة ذات بداية ونهاية صالحتيْن داخل السياق وبطول مقبول. | نرفض span نهايتها قبل بدايتها أو تقع داخل السؤال. |
| Maximum answer length | ماكسِمَم آنسَر لِنث | The largest token length allowed for a candidate answer. | الحد الأعلى لطول الإجابة المرشحة. | `max_answer_length=30` يمنع اختيار فقرة كاملة كإجابة قصيرة. |
| No-answer | نو آنسَر | A supported outcome indicating that the context does not contain a justified answer. | قرار صريح بأن السياق لا يحتوي إجابة موثوقة. | إذا سألنا عن رقم مرجع غير موجود نرجع «لا توجد إجابة». |
| Null score | نَل سكور | A score representing the model's preference for returning no answer. | درجة تمثل تفضيل النموذج للامتناع عن استخراج إجابة. | نقارن أفضل span بدرجة null باستخدام threshold مضبوط على validation. |
| Exact Match (EM) | إكزاكت ماتش | A metric that checks whether the normalised predicted answer exactly matches the reference. | مقياس يساوي 1 عند التطابق الكامل بعد قواعد التطبيع المحددة وإلا 0. | «الرياض» مقابل «الرياض» يعطي EM تساوي 1. |
| Token-overlap F1 | توكِن أوفرلاب إف وَن | F1 based on overlapping answer tokens between prediction and reference. | F1 تقيس الكلمات المشتركة بين الإجابة المتوقعة والصحيحة. | «وزارة الصحة» مقابل «الصحة» يعطي تطابقًا جزئيًا لا EM كاملًا. |

## D. Model selection and evidence

مرتبط بـ[مقدمة اختيار نموذج للعربية](04-arabic-models-intro.md) و[Gate B](05-labs-checkpoint.md).

| English term | Pronunciation | English explanation | الشرح بالعربية | Example |
|---|---|---|---|---|
| Multilingual model | ملتي لِنغوَل مودِل | A model trained to represent or process multiple languages. | نموذج دُرّب على لغات متعددة ويعطي نقطة بداية موحدة. | نبدأ بنموذج يدعم العربية والإنجليزية لمسار «بيان». |
| Arabic-specific model | آرابِك سْبِسِفِك مودِل | A model pretrained mainly or exclusively on Arabic data. | نموذج ركز تدريبه المسبق على العربية أو أحد تنوعاتها. | نجرب نموذجًا عربيًا عندما تُظهر الشرائح العربية ضعف baseline متعدد اللغات. |
| Model card | مودِل كارد | Documentation describing a model's training, intended use, evaluation, licence, and limitations. | بطاقة توثق بيانات النموذج واستخدامه وترخيصه ونتائجه وحدوده. | نراجع لغة التدريب والترخيص قبل تحميل checkpoint. |
| Checkpoint selection | تشِك بوينت سِلكشن | Choosing a saved model version using task, data, licence, cost, and measured evidence. | اختيار نموذج محفوظ وفق المهمة والبيانات والترخيص والتكلفة والقياس. | لا نختار نموذجًا لمجرد أن اسمه يحتوي كلمة Arabic. |
| In-domain data | إن دومين داتا | Data that resembles the target application's language, topics, and conditions. | بيانات تشبه بيئة الاستخدام الحقيقية في المجال واللغة. | طلبات خدمات اصطناعية أقرب للمهمة من مراجعات أفلام. |
| Per-language evaluation | بِر لانغوِج إفاليويشن | Reporting performance separately for each language. | قياس الأداء لكل لغة بدل إخفائه في متوسط واحد. | نعرض Macro-F1 للعربية والإنجليزية كلًا على حدة. |
| `MEASURED_SMOKE` | ميجَرد سموك | A measured result from a small instructional run that validates mechanics, not production quality. | نتيجة مقاسة من تجربة تعليمية صغيرة تثبت التنفيذ فقط. | نتيجة 12 مثالًا توسم `MEASURED_SMOKE` ولا تسمى دقة نهائية. |
| Gate B | غيت بي | The Day 2 evidence checkpoint for classification, NER, QA, and model-selection decisions. | بوابة اليوم الثاني التي تتطلب أدلة المسارات الثلاثة وقرار النموذج. | لا يعبر الطالب Gate B قبل `group_overlap=0` واختبارات alignment وQA. |

## مراجعة سريعة | Quick review

قبل Gate B يجب أن يستطيع المتدرب شرح الفرق بين:

1. `Pretraining` و`Fine-tuning` و`Task head`.
2. `Baseline` وTransformer المدرب.
3. `Training` و`Validation` و`Frozen test`.
4. `Accuracy` و`Macro-F1`.
5. `Token accuracy` و`Strict entity-level F1`.
6. `Character offset` و`Token position`.
7. `Valid span` و`No-answer`.
8. `MEASURED_SMOKE` ونتيجة إنتاجية.

[العودة إلى صفحة اليوم الثاني](README.md) · [قاموس الدورة الكامل](../docs/glossary/README.md) · [مراجع اليوم الثاني](REFERENCES.md)
