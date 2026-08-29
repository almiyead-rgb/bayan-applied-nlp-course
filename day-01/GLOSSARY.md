# قاموس اليوم الأول | Day 1 Glossary

**من النص إلى Tensor | From Text to Tensor**  
**إعداد وتقديم | Prepared and delivered by:** ميعاد المري · Meaad Al-Marri

استخدم هذا القاموس أثناء قراءة صفحات اليوم الأول وتشغيل الدفترين 01 و02. يبدأ كل صف بالمصطلح الإنجليزي كما يظهر في الكود أو التوثيق، ثم نطقه التقريبي، وتعريف دقيق بالإنجليزية، وشرح عربي مبسط، ومثال مرتبط بمشروع «بيان».

> النطق بالعربية تقريبي للمساعدة داخل القاعة، أما الكتابة الإنجليزية في العمود الأول فهي الصيغة التي يُبحث بها في التوثيق.

## A. Text, Unicode, and preprocessing

مرتبط بـ[النص وUnicode والمعالجة](01-text-preprocessing.md).

| English term | Pronunciation | English explanation | الشرح بالعربية | Example |
|---|---|---|---|---|
| Natural Language Processing (NLP) | ناتشرَل لانغوِج بروسِسِنغ | A field that enables computers to analyse, understand, or generate human language. | مجال يمكّن الحاسوب من تحليل اللغة البشرية أو فهمها أو إنتاجها. | يصنّف «بيان» طلبًا عربيًا، ويستخرج كيانًا منه، ثم يبحث عن حالة مشابهة. |
| Raw text | رو تِكست | Text exactly as received before any transformation. | النص كما وصل قبل التنظيف أو التطبيع، ويُحتفظ به للرجوع والتدقيق وفق سياسة الخصوصية. | `"  أحتاجُ متابعة الطلب  "` هو النص الخام قبل إزالة المسافات الزائدة. |
| Character | كارَكتر | A unit of written text as handled by software; one visible symbol may involve more than one Unicode code point. | محرف في النص، وقد يتكون الشكل المرئي الواحد من أكثر من نقطة Unicode. | الحرف المشكّل «حُ» قد يتكون من حرف وحركة منفصلين برمجيًا. |
| Unicode | يونيكود | The standard that assigns code points to characters across writing systems. | معيار عالمي يمنح الحروف والرموز أرقامًا موحدة، بما فيها العربية. | يمثّل Unicode الحرف «م» بطريقة يمكن للأنظمة المختلفة تبادلها. |
| Code point | كود بوينت | A numeric value assigned to a Unicode character. | الرقم المعياري الذي يعرّف محرفًا في Unicode. | يمكن فحص النقطة البرمجية باستخدام `ord("م")`. |
| Encoding | إنكودِنغ | A rule for converting characters or other information into a storable or transferable representation. | قاعدة تحول المحارف أو المعلومات إلى تمثيل قابل للحفظ أو النقل. | يحول UTF-8 نقاط Unicode إلى bytes داخل الملف. |
| UTF-8 | يو تي إف إيت | A variable-length encoding that stores Unicode code points as bytes. | ترميز شائع يحوّل رموز Unicode إلى بايتات للحفظ والنقل. | يُحفظ ملف CSV العربي بترميز UTF-8 حتى لا تظهر الحروف مشوّهة. |
| Unicode normalisation | يونيكود نورمَلايزيشن | A process that converts canonically equivalent character sequences into a consistent form. | توحيد التمثيلات البرمجية المتكافئة للحروف، وليس حذف خصائص اللغة عشوائيًا. | يحوّل `NFC` حرفًا وحركة منفصلين إلى الصيغة المركبة عندما توجد. |
| Normalisation | نورمَلايزيشن | Applying declared transformations to make selected text forms consistent for a task. | تطبيق تحويلات معلنة لتوحيد أشكال مختارة من النص وفق المهمة. | توحيد المسافات قرار Normalisation، أما حذف التشكيل فيحتاج قياسًا مستقلًا. |
| NFC | إن إف سي | A Unicode normalisation form that prefers composed character representations. | أحد أشكال تطبيع Unicode ويهدف إلى تمثيل متسق مع تفضيل الصيغ المركبة. | نطبق `unicodedata.normalize("NFC", text)` قبل المقارنة الحرفية. |
| Whitespace | وايت سبيس | Spaces, tabs, and line breaks that separate or format text. | المسافات وعلامات الجدولة والأسطر الجديدة، وقد تتكرر أو تكون غير مرئية. | تتحول المسافات المتعددة في `"طلب   جديد"` إلى مسافة واحدة في نسخة النموذج. |
| Personally Identifiable Information (PII) | بيرسَنَلي آيدِنتِفايَبُل إنفورميشن | Information that can identify or contact a person directly or indirectly. | بيانات قد تكشف هوية شخص أو وسيلة التواصل معه مثل البريد والهاتف. | `user@example.invalid` و`0500000000` أمثلة يجب حمايتها قبل السجل أو النشر. |
| PII masking | بي آي آي ماسكِنغ | Replacing sensitive values with safe placeholders before logging, sharing, or modelling. | استبدال البيانات الحساسة بعلامات آمنة قبل التسجيل أو المشاركة أو التدريب. | يصبح البريد `[EMAIL]` ورقم الهاتف `[PHONE]`. |
| Placeholder | بليس هولدر | A visible marker that replaces hidden or unavailable content while preserving its role. | علامة بديلة تحفظ نوع المعلومة دون كشف قيمتها الأصلية. | تشير `[PHONE]` إلى وجود هاتف من دون الاحتفاظ بالرقم. |
| Logging | لوغِنغ | Recording events, inputs, errors, or outputs for monitoring and debugging. | تسجيل أحداث النظام لتتبع التشغيل والأخطاء، ويجب ألا يسبق حماية البيانات الحساسة. | نسجل طول النص ووقت المعالجة بعد إخفاء البريد والهاتف. |
| Preprocessing | بري بروسِسِنغ | Deterministic preparation applied to data before tokenisation, training, or inference. | خطوات ثابتة تُجهّز النص قبل التجزئة أو التدريب أو الاستدلال. | حماية PII ثم Unicode NFC ثم ضبط المسافات وفق profile موثق. |
| Normalisation profile | نورمَلايزيشن بروفايل | A named and versioned specification of text transformations. | وصف مسمّى ومرقّم يحدد بالضبط التحويلات المطبقة على النص. | `conservative-v1` يوثق NFC وضبط المسافات من دون حذف التشكيل. |
| Conservative normalisation | كونسيرفَتِف نورمَلايزيشن | A minimal transformation policy designed to preserve potentially meaningful information. | تطبيع محافظ يغيّر أقل قدر ممكن حتى لا يفقد النص معلومة مهمة. | نوحّد المسافات لكن لا نحذف الهمزات قبل قياس أثر ذلك. |
| Aggressive normalisation | أغريسِف نورمَلايزيشن | A stronger transformation policy that may improve matching but can remove distinctions. | تطبيع واسع قد يساعد المطابقة لكنه قد يمحو فروقًا مهمة، لذلك يُعامل كتجربة مقاسة. | تحويل `أ` و`إ` و`آ` إلى `ا` يحتاج مقارنة قبل اعتماده. |
| Display copy | دِسبلاي كوبي | A protected text version kept readable for people and reports. | نسخة محمية وواضحة للعرض والمراجعة البشرية. | يحتفظ `display_text` بصياغة الطلب بعد إخفاء PII. |
| Model copy | مودِل كوبي | A derived text version prepared under the exact contract expected by the model. | نسخة مشتقة تُطبق عليها معالجة النموذج الموثقة. | يحمل `model_text` النص بعد profile التطبيع المختار. |
| Two-copy contract | تو كوبي كونتراكت | A rule that separates the human-readable protected copy from the model-specific transformed copy. | قاعدة تمنع خلط نسخة العرض بنسخة النموذج حتى تبقى التحويلات قابلة للتتبع. | نعرض `display_text` للمراجع وندخل `model_text` إلى tokenizer. |
| Sentence segmentation | سِنتِنس سيغمِنتيشن | Dividing a document into sentence units using linguistic or rule-based boundaries. | تقسيم المستند إلى جمل مع مراعاة أن النقطة قد تكون اختصارًا لا نهاية جملة. | `د. أحمد راجع الطلب. تم الحل.` يجب ألا تنقسم بعد `د.` بطريقة خاطئة. |
| spaCy sentencizer | سبيسي سِنتِنسايزر | A lightweight spaCy pipeline component that assigns sentence boundaries without a statistical parser. | مكوّن خفيف في spaCy يحدد حدود الجمل بقواعد علامات الترقيم. | يضيف `sentencizer` إلى `spacy.blank("xx")` لتقسيم أمثلة المختبر. |
| Deterministic transformation | دِتِرمِنِستِك ترانسفورميشن | A transformation that returns the same output for the same input and configuration. | تحويل يعطي النتيجة نفسها كل مرة عند ثبات المدخل والإعدادات. | profile نفسه يحول النص نفسه إلى `model_text` مطابق في التدريب والخدمة. |
| Runtime | رَن تايم | The active execution environment in which code, libraries, and models run. | بيئة التنفيذ الحالية التي تعمل داخلها الشفرة والمكتبات والنماذج. | قد يعاد تشغيل Colab runtime فتُفقد الملفات المؤقتة. |
| Dependency | دِبِندِنسي | A library or component required by another piece of software. | مكتبة أو مكوّن يعتمد عليه المشروع ليعمل. | `transformers` و`torch` من dependencies الدفاتر. |
| Package version | باكِج فِرجِن | The specific released version of an installed software package. | رقم إصدار الحزمة المثبتة. | نسجل إصدار `transformers` حتى نفهم اختلاف السلوك بين التشغيلات. |
| Version pinning | فِرجِن بِنِنغ | Requiring exact or bounded dependency versions for repeatable behaviour. | تثبيت إصدارات محددة أو نطاقات مضبوطة للحزم لتحسين قابلية إعادة التشغيل. | يحدد ملف المتطلبات إصدارًا مجربًا بدل تحميل أحدث إصدار بلا مراجعة. |

## B. Tokenisation and tensors

مرتبط بـ[Tokenisation وEmbeddings](02-tokenization-embeddings.md) و[Notebook 01](../notebooks/01_text_processing_tokenization.ipynb).

| English term | Pronunciation | English explanation | الشرح بالعربية | Example |
|---|---|---|---|---|
| Token | توكِن | A unit produced by a tokenizer for model processing. | وحدة نصية يعالجها النموذج، وقد تكون كلمة أو جزء كلمة أو رمزًا. | قد تصبح «وبالخدمة» عدة tokens بدل token واحدة. |
| Tokenisation | توكِنايزيشن | Splitting text into tokens and mapping them to model vocabulary entries. | تقسيم النص إلى وحدات ثم ربطها بمفردات النموذج. | يحول tokenizer جملة عربية إلى tokens ثم إلى أرقام. |
| Tokenizer | توكِنايزر | The component that applies tokenisation rules and returns model inputs. | الأداة المرتبطة بالنموذج التي تنفذ التجزئة وتنتج المدخلات. | يجب تحميل tokenizer من checkpoint المتوافق نفسه. |
| Vocabulary | فوكابيولَري | The fixed set of tokens known by a tokenizer, each with an identifier. | قائمة الوحدات التي يعرفها tokenizer ولكل وحدة رقم. | إذا كانت الوحدة موجودة في vocabulary تحصل على `token_id` محدد. |
| Token ID | توكِن آي دي | The integer index assigned to a token in a tokenizer vocabulary. | رقم الوحدة داخل قاموس tokenizer، وليس معنى الكلمة نفسه. | قد تمثل `[CLS]` بالرقم `101` في checkpoint معين فقط. |
| Special tokens | سبيشَل توكِنز | Reserved tokens used for structure, padding, or task control. | وحدات خاصة تضيف معنى بنيويًا مثل بداية التسلسل أو نهايته أو الحشو. | `[CLS]` و`[SEP]` و`[PAD]` أمثلة شائعة. |
| Subword | سَب وورد | A token that represents part of a word rather than the whole word. | جزء من كلمة يسمح للنموذج بتمثيل كلمات نادرة أو مركبة. | قد تنقسم «وبالخدمة» إلى الواو والباء وجزء يمثل «الخدمة». |
| Out-of-vocabulary (OOV) | آوت أُف فوكابيولَري | A word not represented as one complete item in a vocabulary. | كلمة غير موجودة كوحدة كاملة؛ تعالجها tokenizers الحديثة غالبًا بأجزاء تحت كلمية. | اسم جديد قد ينقسم إلى subwords بدل التحول إلى كلمة مجهولة واحدة. |
| Token fertility | توكِن فِرتِلِتي | The average number of model tokens produced per whitespace-delimited word. | متوسط عدد tokens الناتجة عن كل كلمة محسوبة بالمسافات. | 20 token من 10 كلمات تعني fertility تساوي `2.0`. |
| Sequence length | سيكوانس لِنث | The number of tokens in one model input after tokenisation. | عدد الوحدات في المدخل بعد التجزئة، بما في ذلك الرموز الخاصة عند إضافتها. | النص الطويل قد يصل إلى `128` token بعد التجزئة. |
| Maximum length | ماكسِمَم لِنث | The configured upper limit on tokens accepted for one input. | الحد الأعلى لطول التسلسل الذي نسمح به في التشغيل. | نضبط `max_length=128` بعد قياس أطوال بياناتنا. |
| Truncation | ترانكيشن | Removing tokens that exceed the configured maximum sequence length. | حذف الوحدات الزائدة عن الحد، وقد يحذف معلومة مهمة. | `truncation=True` يقطع نهاية النص إذا تجاوز `max_length`. |
| Padding | بادِنغ | Adding padding tokens so sequences can share one tensor shape. | إضافة وحدات حشو لتتساوى أطوال الأمثلة داخل الدفعة. | يُضاف `[PAD]` إلى النص الأقصر حتى يساوي الأطول. |
| Dynamic padding | داينامِك بادِنغ | Padding each batch only to its longest sequence. | حشو كل دفعة إلى طول أطول مثال فيها بدل حد ثابت كبير. | دفعة أطوالها 12 و18 و20 تُحشى إلى 20 لا إلى 512. |
| Input attention mask | إنبُت أتنشن ماسك | A binary model input that identifies real-token positions rather than padding positions. | مدخل ثنائي يميز مواضع النص الحقيقي عن مواضع الحشو. | القيمة `1` للنص الحقيقي و`0` عادةً لمواضع `[PAD]`. |
| Input IDs | إنبُت آي ديز | The tensor of vocabulary identifiers supplied to a language model. | Tensor تحتوي أرقام tokens التي تدخل إلى النموذج. | يعيد tokenizer الحقل `input_ids` بالشكل `[batch, sequence]`. |
| Tensor | تِنسَر | A multidimensional array used to store numeric model inputs, parameters, or outputs. | مصفوفة رقمية متعددة الأبعاد تمثل المدخلات أو الأوزان أو النتائج. | `input_ids` لدفعة من النصوص قد يكون Tensor بالشكل `[batch, sequence]`. |
| Batch | باتش | A group of examples processed together in one model operation. | مجموعة أمثلة تُعالج معًا لتسريع الاستفادة من العتاد. | `batch_size=8` يعني تشغيل ثمانية نصوص في الخطوة. |
| Embedding | إمبِدِنغ | A learned dense vector that represents a token, sentence, or other item. | متجه أرقام كثيف يتعلم تمثيل وحدة لغوية أو نص. | يتحول token ID إلى متجه مثل `[0.12, -0.44, ...]`. |
| Embedding dimension | إمبِدِنغ دِمِنشن | The number of numeric components in an embedding vector. | عدد القيم داخل متجه التضمين. | إذا كان `d_model=768` فلكل موضع 768 قيمة في hidden state. |
| Contextual embedding | كونتِكستشُوَل إمبِدِنغ | A representation whose value changes according to surrounding tokens. | تمثيل يتغير بحسب سياق الكلمة داخل الجملة. | تمثيل «عين» يختلف بين «عين الماء» و«ألم في العين». |
| Hidden state | هِدِن ستيت | The internal vector representation produced for each position by a model layer. | التمثيل الداخلي لكل موضع بعد إحدى طبقات النموذج. | يخرج encoder مصفوفة بالشكل `[batch, sequence, hidden_size]`. |
| Shape | شيب | The ordered sizes of a tensor's dimensions. | أحجام أبعاد Tensor بالترتيب. | الشكل `[2, 12, 768]` يعني دفعتين و12 موضعًا و768 خاصية. |
| Checkpoint | تشِك بوينت | Saved model weights plus configuration, usually tied to a compatible tokenizer. | أوزان وإعدادات محفوظة لنموذج، ويجب استخدام tokenizer المتوافق معها. | لا نخلط tokenizer من نموذج مع أوزان checkpoint آخر. |

## C. Attention and Transformers

مرتبط بـ[Attention وTransformer](03-attention-transformers.md) و[Notebook 02](../notebooks/02_attention_transformers.ipynb).

| English term | Pronunciation | English explanation | الشرح بالعربية | Example |
|---|---|---|---|---|
| Attention | أتنشن | A mechanism that computes weighted combinations of information from other positions. | آلية تمنح المواضع أوزانًا مختلفة ثم تجمع معلوماتها وفق هذه الأوزان. | عند معالجة «الطلب لم يصل»، قد يركز تمثيل «يصل» على «لم». |
| Self-attention | سِلف أتنشن | Attention in which queries, keys, and values come from the same sequence. | انتباه تكون فيه Q وK وV مشتقة من التسلسل نفسه. | كلمات جملة الطلب تنتبه إلى كلمات أخرى داخل الجملة نفسها. |
| Query (Q) | كويري | A vector describing what information the current position is looking for. | متجه يعبّر عما يبحث عنه الموضع الحالي. | موضع «وصل» يرسل Query للعثور على ما يغير معناه مثل «لم». |
| Key (K) | كي | A vector describing what information a position offers for matching. | متجه يصف ما يعلنه كل موضع حتى تتم مقارنته مع Query. | Key الخاصة بـ«لم» قد تحقق score مرتفعة مع Query الفعل. |
| Value (V) | فاليو | A vector containing the information mixed into the attention output. | متجه يحمل المعلومة التي تُجمع فعليًا بعد حساب الأوزان. | وزن الانتباه يحدد مقدار Value الخاصة بكل كلمة في الناتج. |
| Attention score | أتنشن سكور | A compatibility value computed between a query and a key. | قيمة تقيس مدى ارتباط Query بــKey قبل تحويلها إلى أوزان. | يُحسب score أساسيًا من الضرب النقطي بين `Q` و`K`. |
| Scaled dot-product attention | سكيلد دوت برودَكت أتنشن | Attention computed from scaled query-key dot products, softmax weights, and values. | انتباه يحسب تشابه Q وK، يقسمه على جذر البعد، ثم يطبق Softmax ويجمع V. | `softmax(QKᵀ / sqrt(d_k))V` هي الصيغة الأساسية. |
| Softmax | سوفت ماكس | A function that converts scores into non-negative weights that sum to one. | دالة تحول الدرجات إلى أوزان موجبة مجموعها واحد. | الدرجات `[1, 2]` تتحول إلى وزن أصغر للأولى وأكبر للثانية. |
| Attention mask | أتنشن ماسك | A constraint that prevents selected positions from receiving attention weight. | قناع يمنع النموذج من الانتباه إلى مواضع مثل الحشو أو المستقبل في decoder. | تُمنع مواضع `[PAD]` من التأثير في ناتج الانتباه. |
| Multi-head attention | ملتي هِد أتنشن | Multiple attention heads operating in parallel over different learned projections. | عدة رؤوس انتباه تعمل بالتوازي لتتعلم أنواع علاقات مختلفة. | رأس قد يلتقط النفي وآخر قد يلتقط علاقة الكيان بالموقع. |
| Attention head | أتنشن هِد | One independent set of query, key, and value projections inside multi-head attention. | مسار انتباه مستقل داخل Multi-head Attention. | مع `num_heads=3` توجد ثلاثة رؤوس متوازية. |
| Head dimension | هِد دِمِنشن | The feature width allocated to one attention head. | عدد القيم التي يعالجها الرأس الواحد. | إذا كان `d_model=12` و`num_heads=3` فإن `head_dim=4`. |
| Model dimension | مودِل دِمِنشن | The width of token representations throughout a Transformer block. | عرض تمثيل كل موضع داخل كتلة Transformer. | يجب أن يقبل `d_model` القسمة على عدد الرؤوس في البنية المعتادة. |
| Positional encoding | بوزيشنَل إنكودِنغ | Information added or learned so the model can represent token order. | معلومات تمكّن Transformer من معرفة ترتيب الوحدات. | يختلف تمثيل «الطالب شرح النموذج» عن «النموذج شرح الطالب». |
| Transformer | ترانسفورمر | A neural architecture built from attention, feed-forward layers, residual paths, and normalisation. | معمارية عصبية تعتمد على الانتباه وطبقات أخرى لمعالجة التسلسلات. | BERT نموذج Transformer من نوع encoder. |
| Encoder | إنكودر | A Transformer component that builds contextual representations of an input sequence. | جزء يقرأ المدخل كاملًا ويبني تمثيلًا سياقيًا لكل موضع. | نستخدم encoder للتصنيف وNER في اليوم الثاني. |
| Decoder | ديكودر | A Transformer component commonly used to generate outputs token by token. | جزء يُستخدم غالبًا لتوليد وحدات جديدة تدريجيًا. | نماذج توليد النص تتنبأ بالوحدة التالية باستخدام decoder. |
| BERT | بِرت | A bidirectional Transformer encoder pretrained to build contextual language representations. | مشفر Transformer ثنائي الاتجاه مدرّب مسبقًا لتمثيل اللغة. | نضيف task head فوق BERT في التصنيف وNER. |
| Forward pass | فوروَرد باس | Computing model outputs from inputs without performing an optimisation update. | تمرير المدخلات عبر طبقات النموذج لإنتاج المخرجات من دون تحديث الأوزان. | يشغل Notebook 02 forward pass فعليًا ويعرض shapes. |
| Model parameter | مودِل بَرامِتر | A learned numeric value, such as a weight or bias, stored by a model. | قيمة رقمية متعلمة داخل النموذج مثل weight أو bias. | يحتوي checkpoint على ملايين parameters قابلة للعد. |
| Parameter count | بَرامِتر كاونت | The number of learned parameters in a model. | عدد القيم المتعلمة داخل النموذج ويعطي مؤشرًا للحجم لا للجودة وحدها. | يقارن الدفتر عدد معاملات checkpointين من دون الادعاء أن الأكبر أفضل. |
| Feed-forward network (FFN) | فيد فوروَرد نِتوورك | A position-wise neural network applied after attention inside a Transformer block. | شبكة عصبية تُطبق على كل موضع بعد طبقة الانتباه. | تمر مخرجات الانتباه عبر FFN قبل إخراج كتلة encoder. |
| Residual connection | رِزيدجُوَل كَنِكشن | A shortcut that adds a block input to its transformed output. | مسار يضيف مدخل الطبقة إلى ناتجها لدعم استقرار التدريب. | `output = input + attention_output` تمثيل مبسط للفكرة. |
| Layer normalisation | لايَر نورمَلايزيشن | A normalisation operation applied across hidden features for each example position. | تطبيع على خصائص hidden state يساعد استقرار الشبكة. | توجد LayerNorm حول مكونات كتلة Transformer بحسب المعمارية. |
| Quadratic complexity | كوادراتِك كومبلكسِتي | Growth proportional to the square of sequence length. | تكلفة تزداد تقريبًا مع مربع طول التسلسل في self-attention الكامل. | مضاعفة الطول من 128 إلى 256 قد تجعل مصفوفة الانتباه أكبر أربع مرات. |
| Attention visualisation | أتنشن فيجوالايزيشن | A display of attention weights for inspection, not proof of causal explanation. | عرض لأوزان الانتباه يساعد الاستكشاف لكنه ليس دليلًا سببيًا على قرار النموذج. | Heatmap توضح أن وزنًا مرتفعًا ظهر بين كلمتين، ولا تثبت وحدها سبب التنبؤ. |

## D. Learning path and evidence

مرتبط بـ[المختبرين وبوابة بيان A](04-labs-checkpoint.md).

| English term | Pronunciation | English explanation | الشرح بالعربية | Example |
|---|---|---|---|---|
| Core | كور | The required learning path that every learner must complete. | المسار الأساسي الإلزامي لجميع المتدربين. | نجاح الدفترين وعلامات `PASS` جزء من Core. |
| Explore | إكسبلور | An optional extension attempted after Core succeeds. | مسار اختياري للاستكشاف بعد إكمال الأساسيات. | مقارنة profile تطبيع إضافي بعد نجاح الاختبارات. |
| Distinction | دِستِنكشن | An advanced evidence-based extension for learners seeking deeper mastery. | مسار تميز متقدم يحتاج دليلًا وقياسًا، ولا يعوض نقص Core. | مقارنة checkpoint ثانية مع توثيق النتائج والحدود. |
| Gate | غيت | A defined checkpoint with evidence that must pass before moving forward. | بوابة اجتياز تربط الانتقال بأدلة واضحة لا بمجرد انتهاء الوقت. | Gate A تتطلب معالجة ناجحة وقرار tokenizer موثقًا. |
| Smoke test | سموك تِست | A small, fast check that proves a path runs without claiming full quality. | اختبار سريع يثبت أن المسار يعمل دون ادعاء جودة نهائية. | تشغيل عينة صغيرة حتى تظهر علامة `PASS`. |
| Golden test | غولدِن تِست | A test with a deliberately chosen input and known expected output. | اختبار بمدخل ونتيجة متوقعة معروفة لكشف تغير السلوك. | يجب أن يتحول البريد إلى `[EMAIL]` في كل تشغيل. |
| Evidence | إفِدِنس | A saved artefact that supports a technical claim. | دليل محفوظ يثبت ادعاء مثل نتيجة اختبار أو قرار موثق. | مخرجات الاختبار ورابط commit دليلان على إكمال المهمة. |
| Reproducibility | ريبْروديوسِبِلِتي | The ability to repeat a result using documented data, code, versions, and settings. | إمكانية إعادة النتيجة عند توفر البيانات والكود والإصدارات والإعدادات نفسها. | يسجل الطالب checkpoint وprofile وseed وإصدارات الحزم. |
| Git commit | غِت كَمِت | A named snapshot of repository changes in version history. | لقطة موثقة للتغييرات داخل تاريخ Git. | `feat: complete day 1 preprocessing tokenization and attention`. |
| Decision log | دِسيجِن لوج | A record of a choice, its evidence, alternatives, and limitations. | سجل يشرح القرار وسببه والبدائل وحدوده. | يسجل `DECISIONS.md` لماذا اختير tokenizer معين. |

## مراجعة سريعة | Quick review

قبل Gate A يجب أن يستطيع المتدرب شرح الفرق بين:

1. `Raw text` و`display_text` و`model_text`.
2. `Token` و`Token ID` و`Embedding`.
3. `Padding` و`Truncation` و`Attention mask`.
4. `Query` و`Key` و`Value`.
5. `Encoder` و`Decoder`.
6. `Smoke test` وقياس الجودة الكامل.

[العودة إلى صفحة اليوم الأول](README.md) · [قاموس الدورة الكامل](../docs/glossary/README.md) · [مراجع اليوم الأول](REFERENCES.md)
