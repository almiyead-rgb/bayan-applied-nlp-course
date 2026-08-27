# 2. ONNX وINT8 وقرار النشر
# ONNX, INT8, and the Ship Decision

## ما هو ONNX؟

**ONNX** صيغة مفتوحة لتمثيل graph النموذج. **ONNX Runtime (ORT)** محرك استدلال يشغل graph على مزود تنفيذ مثل CPU. الصيغة والمحرك شيئان مختلفان.

```text
PyTorch model
→ export
→ ONNX graph
→ ONNX checker
→ ORT session
→ parity test
→ benchmark
```

التصدير الناجح لا يثبت أن المخرجات صحيحة، وفتح الجلسة لا يثبت أنها أسرع.

يستخدم Notebook 08 مسار TorchScript exporter صراحةً للتوافق مع تجربة dynamic INT8 في ONNX Runtime. قد يعرض PyTorch تحذير deprecation أو tracing؛ التحذير ليس PASS ولا FAIL. بوابات Core الحاسمة هي `onnx.checker` ثم numerical/prediction parity. جرّب المصدّر `dynamo` الحديث في Explore فقط، ثم أعد جميع البوابات لأن graph مختلف وقد لا يقبل التكميم الحالي.

## ما هو Dynamic INT8؟

**التكميم** يمثل بعض القيم بعدد بتات أقل. في dynamic quantisation تُحسب معاملات activations أثناء الاستدلال بينما تكمم weights المناسبة. توصي وثائق ONNX Runtime عمومًا بتجربته مع نماذج Transformer، لكنها لا تضمن سرعة أو جودة محددة.

قد تكون النتيجة:

- artefact أصغر وأسرع؛
- أصغر ولكن latency مشابهة؛
- أبطأ بسبب overhead/حجم workload/العتاد؛
- انخفاض جودة غير مقبول؛
- operator غير مدعوم في graph الحالي.

كلها نتائج صالحة إذا وثقت بصدق.

## تسلسل التحقق الإلزامي

### 1) صحة graph

```python
import onnx

graph = onnx.load("model_fp32.onnx")
onnx.checker.check_model(graph)
```

### 2) نفس المدخلات

استخدم `input_ids` و`attention_mask` نفسيهما في PyTorch وORT. لا تعِد tokenisation بإعدادات مختلفة داخل أحد المسارين.

### 3) Numerical parity

قارن logits بـ`max_abs_diff` و`mean_abs_diff` مع tolerance تذكرها. الاختلاف العشري الصغير قد يكون طبيعيًا؛ الاختلاف الكبير يحتاج تشخيصًا.

### 4) Prediction parity

قارن `argmax` لكل مثال، لا مثالًا واحدًا فقط. اختلاف labels مهم حتى لو بدا متوسط logits قريبًا.

### 5) Task quality

احسب metric المهمة على validation نفسها لكل من:

- PyTorch FP32 reference؛
- ONNX FP32؛
- ONNX INT8 candidate.

ثم:

```python
quality_tax = baseline_metric - candidate_metric
```

قيمة موجبة تعني انخفاضًا، وسالبة تعني أن candidate أعلى على العينة؛ لا تحول فرقًا صغيرًا على عينة صغيرة إلى ادعاء عام.

### 6) Benchmark والحجم

قارن p50/p95/p99 وthroughput وRSS observed peak وMiB على الجهاز نفسه. أعد warm-up لكل runtime.

## قرار قابل للدفاع

| الحالة | القرار المهني المحتمل |
|---|---|
| يحقق latency والجودة | اعتمد candidate وسجل الدليل |
| أسرع لكن quality tax تتجاوز الحد | احتفظ بـFP32 أو عدّل المسار ثم أعد validation |
| أصغر لكن أبطأ | استخدمه فقط إذا كانت المساحة أهم ومبررة، وإلا ارفضه |
| فرق السرعة داخل ضوضاء القياس | لا تدّع تحسنًا؛ زد القياسات واضبط العوامل |
| فشل export/operator | سجل السبب وارجع إلى FP32؛ لا تمنح PASS مزيفًا |

الـfallback قرار صالح. الهدف اختيار إصدار موثوق، لا إجبار INT8 على الفوز.

## Rollback وversioning

احتفظ بالمعلومات التالية، لا بالأوزان داخل GitHub:

```text
model_id
model_version / revision
preprocessing_version
label_map
runtime + provider
artifact SHA-256
data/workload version
benchmark report path
FP32 rollback path or reproduction command
```

لا ترفع `.onnx` أو `.safetensors` أو checkpoints إلى مستودع الدورة. ضع خطوات إعادة الإنتاج وhash فقط؛ واحفظ artefacts في Drive الخاص إن احتجت.

## أخطاء شائعة

| العرض | افحص أولًا |
|---|---|
| ORT input missing | أسماء inputs في `session.get_inputs()` |
| shape mismatch | dynamic axes وdtype وbatch/sequence dimensions |
| labels تغيرت | tokenizer، padding، opset، output mapping |
| quantisation لم تصغّر الملف | operators التي كُممت فعلًا ونوع weights |
| INT8 أبطأ | batch، طول النص، CPU instruction set، warm-up |
| FP32 وONNX مختلفان كثيرًا | `eval()`، نفس inputs، unsupported/export semantics |

## Explore: Optimum ONNX

يوفر Hugging Face حزمة `optimum-onnx` الرسمية للتصدير والتحسين والتكميم. هي خيار Explore بعد نجاح Core. لا تخلط تعليمات الإصدارات القديمة من `optimum` مع الحزمة المنفصلة الحالية؛ اتبع [مراجع اليوم](REFERENCES.md).

## English recap

ONNX export is a format conversion, ORT is the runtime, and INT8 is only a candidate. Check the graph, numerical parity, prediction parity, task quality, latency, memory method, and artefact size. Keep an FP32 rollback path and let the pre-declared budget decide.
