# قاموس اليوم الرابع | Day 4 Glossary

**قِس، حسّن، اختبر، وسلّم | Measure, Optimise, Test, and Ship**  
**إعداد وتقديم | Prepared and delivered by:** ميعاد المري · Meaad Al-Marri

يجمع هذا القاموس مصطلحات القياس والتحسين وONNX والتكميم والخدمة والتسليم كما تظهر في صفحات اليوم الرابع وNotebook 08. يبدأ كل صف بالمصطلح الإنجليزي، ثم نطقه التقريبي، وتعريفه بالإنجليزية، وشرحه بالعربية، ومثال من مشروع «بيان».

> لا توجد تقنية تحسين أسرع دائمًا. قرار الشحن أو الرفض يعتمد على قياس workload المشروع نفسه مع ثبات العقد والبيئة.

## A. Benchmarking and performance

مرتبط بـ[Benchmark قبل التحسين](01-benchmark-before-optimization.md) و[Notebook 08](../notebooks/08_optimization_serving.ipynb).

| English term | Pronunciation | English explanation | الشرح بالعربية | Example |
|---|---|---|---|---|
| Inference | إنفِرَنس | Running a trained model to produce predictions without updating its parameters. | تشغيل نموذج مدرّب لإنتاج توقعات من دون تحديث أوزانه. | تمرير طلب جديد إلى classifier بعد `model.eval()`. |
| Benchmark | بِنش مارك | A controlled measurement of performance under a documented workload and environment. | قياس منضبط للأداء على مدخلات وبيئة موثقتين. | نقيس FP32 وINT8 على النصوص نفسها وعدد التكرارات نفسه. |
| Baseline benchmark | بيس لاين بِنش مارك | The reference measurement taken before an optimisation candidate is introduced. | القياس المرجعي قبل تطبيق التحسين. | زمن PyTorch FP32 هو baseline الذي نقارن به ONNX. |
| Workload | وِرك لود | The exact set and pattern of inputs used during a performance test. | مجموعة المدخلات وطريقة تشغيلها في القياس. | 40 طلبًا عربيًا وإنجليزيًا بأطوال موثقة و`batch_size=1`. |
| Frozen workload | فروزِن وِرك لود | A workload kept unchanged across candidate comparisons. | مدخلات ثابتة لا تتغير عند مقارنة البدائل. | لا نقيس INT8 على نصوص أقصر من FP32. |
| Measurement contract | ميجَرمِنت كونتراكت | A specification of device, versions, workload, warm-up, repetitions, batching, and metrics. | عقد يحدد البيئة والمدخلات والإحماء والتكرارات والدفعات والمقاييس. | نسجل CPU وإصدار ORT و30 تكرارًا وp95 قبل عرض النتيجة. |
| Performance budget | برفورمَنس بَجِت | A predefined acceptable limit for latency, throughput, memory, size, and quality. | حدود أداء مقبولة تُكتب قبل رؤية نتائج المرشحين. | الهدف p95 أقل من 40 ms مع quality tax ضمن الحد المعلن. |
| Warm-up | وورم أب | Initial runs excluded from measurement to initialise caches, kernels, or runtime state. | تشغيلات أولية لا تدخل في النتيجة لأنها تهيئ النموذج أو المحرك. | ننفذ خمس طلبات warm-up قبل تسجيل الأزمنة. |
| Repetition | رِبِتيشن | One repeated execution of the measured operation. | مرة واحدة من تشغيل العملية المقاسة. | نستخدم 30 تكرارًا على الأقل بدل زمن طلب واحد. |
| Latency | ليتِنسي | The elapsed time required to complete one request or batch. | الزمن من بداية الطلب حتى اكتمال النتيجة. | يستغرق الطلب 25 millisecond في بيئة موثقة. |
| p50 latency | بي فِفتي ليتِنسي | The median latency; half the measurements are at or below it. | وسيط زمن الاستجابة؛ نصف الطلبات أسرع منه أو تساويه. | `p50=22 ms` يصف السلوك المعتاد. |
| p95 latency | بي ناينتي فايف ليتِنسي | The latency value at or below which 95 percent of measurements fall. | قيمة لا يتجاوزها 95% من الطلبات وتكشف بطء الذيل. | `p95=39 ms` يحقق ميزانية 40 ms. |
| p99 latency | بي ناينتي ناين ليتِنسي | The latency value at or below which 99 percent of measurements fall. | زمن قريب من أسوأ الطلبات ويحتاج عددًا كافيًا من القياسات. | لا نفسر p99 بقوة من عشرة تكرارات فقط. |
| Tail latency | تيل ليتِنسي | The slower end of the latency distribution, commonly represented by p95 or p99. | أزمنة الطلبات الأبطأ التي قد يخفيها المتوسط. | p50 جيد لكن p99 مرتفع بسبب حالات طويلة. |
| Percentile | بَرسِنتايل | A value below which a stated percentage of observations falls. | قيمة يقع تحتها أو عندها جزء محدد من القياسات. | p95 هو percentile الخامس والتسعون. |
| Throughput | ثرو بوت | The number of items or requests completed per unit of time. | عدد العناصر أو الطلبات المنجزة في وحدة الزمن. | `120 items/s` عند `batch_size=8`. |
| Concurrency | كَنكَرِنسي | The number of requests that are in progress during the same test interval. | عدد الطلبات الجاري تنفيذها في الوقت نفسه خلال الاختبار. | البوابة الرسمية تستخدم `concurrency=16`. |
| Model-only latency | مودِل أونلي ليتِنسي | Latency measured only around model execution, excluding surrounding processing. | زمن تشغيل النموذج وحده من دون المعالجة القبلية والبعدية وHTTP. | نقيس `session.run()` وحدها لتشخيص المحرك. |
| End-to-end latency | إند تو إند ليتِنسي | Latency measured across the complete request path within a declared boundary. | زمن المسار الكامل ضمن حدود معلنة مثل التحقق والمعالجة والنموذج والاستجابة. | قياس TestClient يشمل عقد التطبيق داخل العملية ولا يشمل شبكة خارجية. |
| Overhead | أوفر هِد | Extra time or resources introduced by orchestration, conversion, communication, or setup. | تكلفة إضافية لا تمثل حساب النموذج الأساسي وحده. | قد يجعل overhead التكميم أبطأ على workload صغير. |
| Batch size | باتش سايز | The number of examples processed together in one operation. | عدد الأمثلة التي تُعالج معًا. | زيادة batch قد ترفع throughput لكنها قد ترفع latency لطلب منفرد. |
| Resident Set Size (RSS) | رِزِدَنت سِت سايز | The portion of a process's memory currently held in physical RAM. | مقدار ذاكرة RAM التي يشغلها process أثناء التشغيل. | يسجل التقرير `RSS observed peak` أثناء benchmark. |
| Observed peak memory | أوبزِرفد بيك مِمُري | The highest memory value observed by the chosen measurement method. | أعلى قيمة ذاكرة رُصدت بأداة القياس، وليست بالضرورة الحد المطلق الحقيقي. | نكتب اسم الأداة وفاصل أخذ العينات بجانب القيمة. |
| Artefact size | آرتِفاكت سايز | The storage size of a saved model or deployment file. | حجم ملف النموذج أو حزمة التشغيل على القرص. | نقارن حجم `.onnx` بحجم أوزان FP32. |
| Cold start | كولد ستارت | The first request after loading or initialising a service or model. | الطلب الأول بعد تحميل النموذج أو بدء الخدمة وقد يكون أبطأ. | لا نخلطه مع latency المستقرة بعد warm-up. |
| Inference mode | إنفِرَنس مود | A PyTorch context that disables gradient tracking and related overhead during inference. | وضع PyTorch يوقف حساب gradients لأنه غير مطلوب عند التنبؤ. | نستخدم `torch.inference_mode()` حول تشغيل النموذج. |
| Autograd | أوتو غراد | PyTorch's automatic differentiation system for recording operations and computing gradients. | نظام PyTorch لتتبع العمليات وحساب gradients أثناء التدريب. | يوقف `inference_mode()` تتبع Autograd في الاستدلال. |
| Evaluation mode | إفاليويشن مود | A model state that changes training-specific layers to inference behaviour. | حالة تضبط طبقات مثل Dropout على سلوك التقييم. | نستدعي `model.eval()` قبل benchmark. |
| Dropout | دروب آوت | A regularisation layer that randomly drops activations during training and is disabled in evaluation mode. | طبقة تسقط قيمًا عشوائيًا في التدريب وتُوقف في وضع التقييم. | نسيان `model.eval()` قد يجعل نتائج inference غير ثابتة. |
| Dynamic padding | داينامِك بادِنغ | Padding each batch only to its longest input rather than a fixed global maximum. | حشو الدفعة إلى أطول مدخل فيها فقط. | نصوص أطوالها 20 و30 تُحشى إلى 30 لا إلى 512. |
| Length bucketing | لِنث بَكِتِنغ | Grouping inputs of similar lengths into batches to reduce padding waste. | تجميع النصوص المتقاربة في الطول لتقليل الحشو. | توضع النصوص القصيرة معًا والطويلة معًا ثم تعاد النتائج إلى ترتيب IDs. |

## B. ONNX, INT8, and the ship decision

مرتبط بـ[ONNX وINT8 وقرار النشر](02-onnx-int8-decision.md).

| English term | Pronunciation | English explanation | الشرح بالعربية | Example |
|---|---|---|---|---|
| Open Neural Network Exchange | أوبِن نيورَل نِتوورك إكستشينج | The full name of the open model format commonly abbreviated as ONNX. | الاسم الكامل لصيغة ONNX المفتوحة لتبادل نماذج التعلم الآلي. | يحفظ التصدير graph في ملف امتداده `.onnx`. |
| ONNX | أونِكس | The abbreviation for the Open Neural Network Exchange model format. | الاختصار المستخدم لصيغة تمثيل graph النموذج ونقله بين الأدوات. | نصدر Transformer من PyTorch إلى ملف ONNX. |
| Computation graph | كومبيوتيشن غراف | A graph of operations and tensors that defines a model's computation. | مخطط يحدد العمليات الرقمية وتدفق tensors داخل النموذج. | يفحص `onnx.checker` صحة بنية graph المصدرة. |
| ONNX Runtime (ORT) | أونِكس رَن تايم | An inference engine that executes ONNX models using available execution providers. | محرك يشغل نماذج ONNX على CPU أو مزود آخر. | نفتح الملف باستخدام `onnxruntime.InferenceSession`. |
| Execution provider | إكزِكيوشن بروفايدر | A backend that implements ONNX Runtime operations for specific hardware. | مزود ينفذ عمليات ORT على عتاد معين. | `CPUExecutionProvider` يشغل النموذج على CPU. |
| FP32 | إف بي ثيرتي تو | Thirty-two-bit floating-point numerical representation. | تمثيل عشري بدقة 32 بت ويستخدم كخط أساس شائع. | نحفظ نموذج ONNX FP32 قبل تجربة INT8. |
| INT8 | إنت إيت | Eight-bit integer numerical representation used to reduce model size or computation cost. | تمثيل أعداد صحيحة بدقة 8 بت قد يقلل الحجم أو الزمن. | تصبح بعض أوزان الطبقات من FP32 إلى INT8 بعد التكميم. |
| Quantisation | كوانتِزَيشن | Converting model values or computations to lower numerical precision. | تحويل الأوزان أو الحسابات إلى دقة أقل مع ضرورة إعادة قياس الجودة. | نجرب INT8 ثم نحسب quality tax. |
| Dynamic INT8 quantisation | داينامِك إنت إيت كوانتِزَيشن | Quantisation in which weights are stored as INT8 and activation scales are determined at runtime. | تكميم يخزن الأوزان بدقة INT8 ويحسب معاملات activations وقت التشغيل. | قد يصغر الملف على CPU لكنه لا يضمن تسريع كل workload. |
| Dynamic INT8 | داينامِك إنت إيت | A shorthand name for the dynamic INT8 quantisation candidate used in this course. | الاسم المختصر لمرشح التكميم الديناميكي بدقة 8 بت. | نقارن ONNX INT8 بـONNX FP32 على workload نفسها. |
| Candidate model | كاندِديت مودِل | A proposed alternative being compared with the accepted baseline. | نموذج مرشح للتحسين قبل اعتماده. | ONNX INT8 هو candidate وFP32 هو baseline. |
| Graph validation | غراف فالِديشن | Checking whether an exported model graph is structurally valid. | التحقق من أن graph المصدرة صحيحة وقابلة للقراءة. | يمر الملف على `onnx.checker.check_model`. |
| Exporter | إكسبورتر | A tool or code path that converts a model from its source framework into another format. | أداة أو مسار يحول النموذج من إطاره الأصلي إلى صيغة أخرى. | يستخدم Core مصدّرًا متوافقًا ويترك `dynamo` للمقارنة في Explore. |
| Operator | أوبِريتر | A computation primitive represented as a node in a model graph. | عملية حسابية أساسية داخل graph مثل Matrix Multiply. | قد لا يدعم runtime أو التكميم operator معينة. |
| Opset | أوب سِت | A versioned set of ONNX operator specifications used by a graph. | إصدار مجموعة عمليات ONNX التي تعتمد عليها graph. | يجب تسجيل opset لأن تغييره قد يغير التوافق. |
| Dynamic axes | داينامِك أكسِز | Export metadata that permits selected tensor dimensions to vary at runtime. | إعداد يسمح لأبعاد مثل batch أو sequence أن تتغير عند التشغيل. | نجعل محورَي batch والطول ديناميكيين عند الحاجة. |
| Data type (dtype) | داتا تايب | The numerical type used to store tensor values. | نوع القيم الرقمية في Tensor مثل `int64` أو `float32`. | عدم تطابق dtype في `input_ids` يسبب خطأ تشغيل. |
| Numerical parity | نيومِرِكَل بارِتي | Agreement between numeric outputs of two implementations within defined tolerances. | تقارب النتائج الرقمية بين الإصدارين ضمن حدود معلنة. | نقارن logits الخاصة بـPyTorch وONNX. |
| Maximum absolute difference | ماكسِمَم أبسولوت دِفِرِنس | The largest absolute element-wise difference between two output arrays. | أكبر فرق مطلق بين قيمتين متقابلتين في المخرجات. | يسجل التقرير `max_abs_diff` بين logits. |
| Mean absolute difference | مين أبسولوت دِفِرِنس | The average absolute element-wise difference between two output arrays. | متوسط الفروق المطلقة بين المخرجات المتقابلة. | قيمة صغيرة تدعم التقارب العددي ولا تكفي وحدها للجودة. |
| Prediction parity | برِدِكشن بارِتي | Agreement between the final predictions produced by two model versions. | تطابق القرارات النهائية مثل الفئات بين إصدارين. | يعطي FP32 وONNX `argmax` نفسه لكل مثال canary. |
| Argmax | آرغ ماكس | The index of the largest value in an array. | موضع أعلى قيمة، ويستخدم غالبًا لاختيار الفئة. | `argmax(logits)` يعيد رقم label المتوقعة. |
| Logits | لوجِتس | Raw output scores from a model before probability conversion. | الدرجات الخام التي ينتجها النموذج قبل Softmax. | نقارن logits بين PyTorch وORT في numerical parity. |
| Task quality | تاسك كوالِتي | Performance on the actual task metric and labelled examples. | جودة النموذج وفق مقياس المهمة وبياناتها الصحيحة. | نعيد حساب Macro-F1 بعد التكميم. |
| Quality tax | كوالِتي تاكس | Baseline quality minus candidate quality under the same evaluation contract. | مقدار خسارة الجودة من baseline إلى candidate على المقياس نفسه. | `0.84 - 0.82 = 0.02` quality tax. |
| Tolerance | تولِرَنس | A predefined acceptable numerical or quality difference. | حد مقبول للفرق يُكتب قبل اتخاذ القرار. | نقبل `max_abs_diff` إذا بقي تحت الحد الموثق. |
| Ship decision | شِب دِسيجن | A documented decision to deploy, reject, or defer a candidate based on evidence and budget. | قرار موثق باعتماد المرشح أو رفضه أو تأجيله وفق القياس. | نرفض INT8 إذا لم يحقق الزمن أو تجاوز quality tax. |
| Rollback | رول باك | Returning to a known working model or service version after a candidate fails. | الرجوع إلى نسخة مستقرة معروفة عند فشل الإصدار الجديد. | نبقي FP32 متاحًا ونوثق خطوات الرجوع إليه. |
| Fallback | فول باك | A predefined alternative used when the preferred path is unavailable or rejected. | بديل محدد مسبقًا نستخدمه عند تعذر المسار المفضل أو رفضه. | إذا فشل INT8 تخدم API بإصدار ONNX FP32 أو PyTorch FP32 الموثق. |
| Versioning | فِرجِنِنغ | Assigning traceable identifiers to code, models, data, and contracts. | منح الإصدارات معرفات يمكن تتبعها. | يربط serving manifest إصدار النموذج بإصدار preprocessing. |
| Model artefact | مودِل آرتِفاكت | A saved file or bundle required to execute a trained model. | ملف أو حزمة تمثل النموذج القابل للتشغيل. | ملف ONNX وlabels وtokenizer artefacts تشكل حزمة التشغيل. |
| Hash | هاش | A deterministic digest used to identify exact file content. | بصمة رقمية تكشف تغير محتوى الملف. | نسجل SHA-256 لملف النموذج في manifest. |

## C. FastAPI, service contracts, and canaries

مرتبط بـ[FastAPI وعقد الخدمة وCanaries](03-fastapi-serving-canaries.md).

| English term | Pronunciation | English explanation | الشرح بالعربية | Example |
|---|---|---|---|---|
| Application Programming Interface (API) | أبلكيشن بروغرامِنغ إنترفيس | A defined interface through which software sends requests and receives responses. | عقد تتواصل من خلاله البرامج عبر طلبات واستجابات محددة. | يرسل العميل نصًا إلى `/v1/classify` ويستقبل label وscore. |
| API | إيه بي آي | The common abbreviation for Application Programming Interface. | الاختصار الشائع للواجهة البرمجية. | تغلف FastAPI دالة التنبؤ داخل API مختبرة. |
| FastAPI | فاست إيه بي آي | A Python framework for building typed web APIs with automatic schema documentation. | إطار Python لبناء APIs بعقود أنواع وتوثيق تلقائي. | ينشئ المختبر خدمة تصنيف ويعرض `/docs`. |
| Endpoint | إند بوينت | A named API route that exposes one operation. | مسار محدد في API يقدم وظيفة واحدة. | `/health` و`/v1/classify` endpointان مختلفان. |
| HTTP | إتش تي تي بي | The protocol used to exchange web requests and responses. | بروتوكول تبادل الطلبات والاستجابات عبر الويب. | يستخدم TestClient طلبات HTTP داخل العملية نفسها. |
| GET | غِت | An HTTP method commonly used to retrieve status or resources. | طريقة HTTP تُستخدم غالبًا للقراءة أو فحص الحالة. | `GET /health` يعيد حالة الخدمة. |
| POST | بوست | An HTTP method commonly used to submit data for processing. | طريقة HTTP ترسل بيانات لتنفيذ عملية. | `POST /v1/classify` يرسل نص الطلب. |
| Request schema | ريكوِست سكيما | A typed definition of fields accepted by an API operation. | تعريف الحقول وأنواعها وشروطها في الطلب. | الحقل `text` مطلوب ومن نوع `str` وغير فارغ. |
| Pydantic | باي دانتِك | A Python validation library used by FastAPI to define and validate typed data models. | مكتبة Python يستخدمها FastAPI للتحقق من بيانات الطلب والاستجابة. | يرفض نموذج Pydantic نصًا فارغًا أو لغة غير مدعومة. |
| Response schema | رِسبونس سكيما | A typed definition of fields returned by an API operation. | تعريف شكل الاستجابة وأنواع حقولها. | تعيد الخدمة `label` و`score` و`model_version`. |
| Validation error | فالِديشن إيرَر | An error returned when request data violates the declared schema. | خطأ يحدث عندما لا يطابق الطلب العقد. | النص الفارغ يجب أن يُرفض بدل دخوله إلى النموذج. |
| HTTP status code | إتش تي تي بي ستاتَس كود | A numeric code describing the outcome of an HTTP request. | رقم يوضح نجاح الطلب أو نوع فشله. | `200` نجاح و`422` خطأ تحقق في المدخلات. |
| TestClient | تِست كلاينت | An in-process client used to test FastAPI or Starlette routes without public hosting. | عميل اختبار يشغل الطلبات داخل العملية من دون نشر الخدمة على الإنترنت. | نختبر طلبًا عربيًا وإنجليزيًا وطلبًا مرفوضًا داخل Colab. |
| OpenAPI | أوبِن إيه بي آي | A machine-readable specification describing API operations and schemas. | مواصفة تصف مسارات API وحقولها وتدعم التوثيق التفاعلي. | ينشئ FastAPI صفحة `/docs` من OpenAPI schema. |
| Service contract | سِرفِس كونتراكت | The stable agreement covering request fields, response fields, errors, and version behaviour. | عقد ثابت يحدد المدخلات والمخرجات والأخطاء والإصدارات. | لا نغير اسم `text` إلى `input` من دون إصدار وتحديث العملاء. |
| Serving manifest | سِرفِنغ مانِفِست | Metadata binding model, labels, tokenizer, preprocessing, runtime, and versions for service use. | ملف يربط النموذج والlabels والtokenizer والمعالجة والمحرك وإصداراتها. | ترفض الخدمة startup إذا لم يطابق label hash ملف النموذج. |
| Health check | هِلث تْشِك | A lightweight check that reports whether the process is running. | فحص بسيط يبين أن عملية الخدمة تعمل. | `GET /health` قد يعيد `status=ok`. |
| Readiness check | رِدِينِس تْشِك | A check that confirms the service can safely handle real requests. | فحص يؤكد أن الخدمة جاهزة فعليًا بعد تحميل مكوناتها واختبارها. | لا تصبح readiness ناجحة إذا فشل model canary. |
| Canary test | كَناري تِست | A small known case executed to detect a broken or incompatible release. | حالة معروفة وسريعة تكشف انكسار الإصدار أو عدم توافق مكوناته. | طلب عربي معروف يجب أن يعيد label متفقًا عليه. |
| Startup canary | ستارت أب كَناري | A canary executed during service startup before readiness is granted. | اختبار كناري يعمل عند بدء الخدمة قبل إعلان الجاهزية. | يفشل startup إذا تغير preprocessing وأفسد التوقع المتوقع. |
| Fail closed | فيل كلوزد | A safety behaviour that denies readiness or access when a required check fails. | سلوك آمن يمنع الجاهزية أو الطلب عند فشل تحقق إلزامي. | تبقى الخدمة غير جاهزة إذا فشل startup canary. |
| Train–serve skew | ترين سِرف سكيو | A mismatch between training-time and serving-time data processing or contracts. | اختلاف بين المعالجة أو labels أو الإصدارات في التدريب والخدمة. | طبّعنا الألف في التدريب ولم نطبق ذلك في API. |
| Model version | مودِل فِرجِن | A traceable identifier for the exact model used by a response. | معرف يحدد نسخة النموذج التي أنتجت الاستجابة. | تعيد API `model_version="bayan-fp32-v1"`. |
| Confidence score | كونفِدِنس سكور | A model-reported score associated with a prediction, not automatically a calibrated probability. | درجة يرفقها النموذج بالتوقع ولا تعد احتمالًا معايرًا تلقائيًا. | تتحقق canary أن القيمة داخل `[0, 1]` من دون ادعاء أنها يقين. |
| Authentication | أوثِنتِكيشن | Verifying the identity of a user or client before granting access. | التحقق من هوية المستخدم أو النظام قبل السماح بالوصول. | ليست مطلوبة في smoke داخل Colab لكنها لازمة غالبًا في نشر حقيقي. |
| Transport Layer Security (TLS) | ترانسبورت لايَر سِكيورِتي | Encryption that protects network traffic in transit. | تشفير يحمي البيانات أثناء انتقالها عبر الشبكة. | خدمة HTTPS الإنتاجية تستخدم TLS، بينما TestClient لا يثبت ذلك. |
| Rate limiting | ريت لِمِتِنغ | Restricting request frequency to protect service capacity and reduce abuse. | تحديد عدد الطلبات خلال مدة لحماية الخدمة من الإساءة أو الحمل الزائد. | يُضاف عند النشر العام ولا يختبره مختبر Core. |
| Load testing | لود تِستِنغ | Testing a deployed or realistic service under controlled levels of traffic. | اختبار الخدمة تحت أحمال محددة لمعرفة قدرتها وسلوكها. | TestClient الوظيفي لا يعوض load test إنتاجيًا. |
| Monitoring | مونِترِنغ | Continuous collection of operational signals such as errors, latency, and resource use. | متابعة مستمرة للأخطاء والزمن والموارد بعد التشغيل. | يراقب النظام p95 ونسبة الأخطاء من دون تسجيل PII خام. |

## D. Evidence, review, and final submission

مرتبط بـ[تجميع مشروع بيان والعرض](04-capstone-assembly-demo.md) و[Gate D وGate E](05-lab-gates-submission.md).

| English term | Pronunciation | English explanation | الشرح بالعربية | Example |
|---|---|---|---|---|
| `SYSTEMS_SMOKE` | سِستِمز سموك | A small technical run proving that export, runtime, and API mechanics work. | تشغيل تقني صغير يثبت أن مسار التصدير والمحرك والخدمة يعمل، ولا يثبت أداء المشروع. | checkpoint مصغر يمر عبر PyTorch ثم ONNX ثم INT8 وTestClient. |
| `PROJECT_ARTIFACT` | بروجِكت آرتِفاكت | The learner's actual Bayan model and workload used for final measured evidence. | نموذج مشروع «بيان» الفعلي ومدخلاته المستخدمة في دليل التسليم النهائي. | يجب أن يحمل `benchmark_mode` هذه القيمة عند Gate E. |
| Evidence map | إفِدِنس ماب | A mapping from each claim or requirement to a file, metric, test, or commit that supports it. | خريطة تربط كل ادعاء أو متطلب بدليل قابل للفحص. | Claim البحث يربط بـ`EVALUATION_REPORT.md` ونتيجة Recall@k. |
| Claim | كليم | A statement presented as true and expected to be supported by evidence. | ادعاء يجب أن يكون محدودًا بما تثبته البيانات والقياسات. | «حقق p95 قدره 38 ms على CPU الموثق» claim قابل للمراجعة. |
| Peer review | بِير ريفيو | Structured review of a project by another learner using defined criteria. | مراجعة منظمة ينفذها زميل وفق قائمة تحقق. | يفحص زميل جديد README وإعادة التشغيل والادعاءات خلال ثماني دقائق. |
| Cold clone | كولد كلون | Testing a repository from a fresh clone without relying on the author's local state. | تجربة المستودع من نسخة جديدة للتأكد من أن الملفات والتعليمات كافية. | ينسخ المراجع repo إلى مجلد جديد ويتبع `GETTING_STARTED.md`. |
| Repository | ريبوزِتوري | A version-controlled collection of project files and history. | مستودع يحفظ الكود والوثائق وتاريخ التغييرات. | يسلم الطالب رابط GitHub public لمشروعه. |
| README | ريد مي | The primary project document explaining purpose, setup, use, evidence, and limitations. | الصفحة الرئيسية التي تشرح فكرة المشروع وتشغيله واستخدامه وأدلته وحدوده. | يبدأ المراجع بـ`README.md` قبل فتح notebooks. |
| Technical documentation | تِكنِكَل دوكيومِنتيشن | Documentation of architecture, interfaces, data, decisions, tests, and operational limits. | توثيق يشرح البنية والعقود والبيانات والقرارات والاختبارات والحدود التشغيلية. | تشمل الوثائق Model Card وData Card وBenchmark report. |
| Git | غِت | A distributed version-control system that records project history. | نظام لإدارة الإصدارات وتتبع التغييرات والرجوع إليها. | يستخدم الطالب commits صغيرة بأسماء واضحة. |
| Branch | برانتش | An independent line of development in Git. | مسار تطوير مستقل يسمح بالعمل قبل الدمج. | ينشئ feature branch ثم يراجع التغيير. |
| Pull request (PR) | بُل ريكوِست | A request to review and merge changes from one branch into another. | طلب مراجعة ودمج التغييرات مع نقاش واختبارات. | يفتح الطالب PR بدل تعديل `main` بلا مراجعة. |
| Issue | إشيو | A tracked item for a bug, task, question, or improvement. | بطاقة لتوثيق مشكلة أو مهمة أو اقتراح. | يسجل خطأ Arabizi كـIssue مع خطوات إعادة المشكلة. |
| Continuous Integration (CI) | كونتِنيوس إنتِغريشن | Automated checks run when code changes are pushed or proposed. | فحوص آلية تعمل عند دفع التغييرات أو فتح PR. | يشغل GitHub Actions الاختبارات وفحص الروابط. |
| GitHub Actions | غِت هَب أكشنز | GitHub's automation service for CI and repository workflows. | خدمة GitHub لتشغيل الاختبارات والفحوص تلقائيًا. | تظهر علامة خضراء بعد نجاح `pytest` وrelease gate. |
| Validator | فالِديتور | A tool that checks whether files and values satisfy a defined submission contract. | فاحص آلي يتحقق من اكتمال الملفات والقيم والعقود. | `validate_submission.py` يرفض placeholders وSystems Smoke النهائي. |
| YAML | يامِل | A human-readable structured-data format often used for configuration. | صيغة بيانات منظمة وسهلة القراءة تستخدم للإعدادات. | يحتوي `SUBMISSION.yml` معرف المتدرب وbenchmark mode. |
| JSON | جَيْسَن | A structured text format based on objects, arrays, and primitive values. | صيغة نصية منظمة لتبادل البيانات بين البرامج. | يلخص `PROJECT_SUMMARY.json` مكونات المشروع وروابط الأدلة. |
| Release freeze | رِليس فريز | A point after which only critical, reviewed fixes are allowed before submission. | تجميد النسخة قبل التسليم ومنع الإضافات غير الضرورية. | بعد نجاح Gate D نصلح العيوب الحرجة فقط. |
| Release tag | رِليس تاغ | A stable Git label pointing to a specific release commit. | علامة ثابتة تشير إلى commit النسخة المسلمة. | يستخدم المشروع `submission-v1.0`. |
| Rollback path | رول باك باث | A documented route back to a previously accepted version. | خطوات ونسخة معروفتان للعودة عند فشل المرشح. | يشير `DECISIONS.md` إلى FP32 وcommit المستقر. |
| Reproducibility | ريبْروديوسِبِلِتي | The ability for another person to repeat the result from documented inputs, code, versions, and steps. | قدرة مراجع جديد على إعادة النتيجة باستخدام تعليمات وإصدارات موثقة. | ينجح cold clone من دون ملفات موجودة فقط في جهاز المؤلف. |
| Random seed | راندم سيد | A value used to initialise pseudo-random operations for more repeatable measurements or training. | قيمة تبدأ العمليات شبه العشوائية وتُسجل لدعم إعادة التجربة. | يسجل التقرير seed المستخدمة عند تقييم المرشح. |
| Model card | مودِل كارد | Documentation of model purpose, metrics, limitations, risks, and appropriate use. | وثيقة استخدام النموذج ونتائجه وحدوده ومخاطره. | توضح أن البيانات اصطناعية وأن النتيجة ليست اعتمادًا إنتاجيًا. |
| Data card | داتا كارد | Documentation of dataset sources, construction, licence, privacy, splits, and limitations. | وثيقة مصادر البيانات وبنائها وترخيصها وخصوصيتها وتقسيمها وحدودها. | تذكر مصدر dataset أو طريقة إنشاء البيانات الاصطناعية. |
| Decision log | دِسيجن لوج | A traceable record of decisions, evidence, alternatives, and consequences. | سجل قابل للتتبع يوضح القرار ودليله والبدائل وأثره. | يسجل لماذا رُفض INT8 رغم أن حجمه أصغر. |
| Gate D | غيت دي | The Day 4 shipping checkpoint for measured project inference, parity, quality, and service evidence. | بوابة قرار التشغيل التي تتطلب benchmark المشروع والتقارب والجودة والخدمة. | لا يكفي `SYSTEMS_SMOKE` لعبور Gate D النهائي. |
| Gate E | غيت إي | The final submission checkpoint for repository completeness, validation, evidence, and release tag. | بوابة التسليم النهائية التي تفحص المستودع والوثائق والأدلة وtag. | ينجح الفاحص ثم يُنشأ `submission-v1.0`. |
| Core | كور | The mandatory path required for completion. | المسار الإلزامي للاجتياز. | benchmark صحيح وONNX وTestClient وvalidator. |
| Explore | إكسبلور | An optional extension after the required path succeeds. | امتداد اختياري بعد نجاح Core. | مقارنة batch sizes أو length bucketing. |
| Distinction | دِستِنكشن | An advanced measured extension demonstrating deeper engineering judgement. | شرط تميز متقدم مبني على قياس وقرار موثق. | مقارنة نموذج distilled أو benchmark متزامن منضبط. |

## مراجعة سريعة | Quick review

قبل التسليم يجب أن يستطيع المتدرب شرح الفرق بين:

1. `Latency` و`Throughput`.
2. `p50` و`p95` و`p99`.
3. `Warm-up` والتكرارات المقاسة.
4. `FP32` و`ONNX` و`ONNX Runtime` و`INT8`.
5. `Numerical parity` و`Prediction parity` و`Task quality`.
6. `Health check` و`Readiness check` و`Canary test`.
7. `SYSTEMS_SMOKE` و`PROJECT_ARTIFACT`.
8. `Commit` و`Branch` و`Pull request` و`Release tag`.
9. `Gate D` و`Gate E`.

[العودة إلى صفحة اليوم الرابع](README.md) · [قاموس الدورة الكامل](../docs/glossary/README.md) · [مراجع اليوم الرابع](REFERENCES.md)
