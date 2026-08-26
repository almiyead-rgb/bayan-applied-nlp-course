# استكشاف الأعطال | Troubleshooting

## القاعدة الذهبية

اقرأ **أول رسالة خطأ ذات معنى**، ثم غيّر شيئًا واحدًا فقط وأعد الاختبار. تكرار Run دون تشخيص لا يصلح الخطأ.

## مسار القرار

```mermaid
flowchart TD
    A["ظهرت مشكلة"] --> B{"هل توجد رسالة خطأ؟"}
    B -- "نعم" --> C["انسخ النص الكامل وحدد الخلية"]
    B -- "لا" --> D["افحص هل الخلية ما زالت تعمل"]
    C --> E{"إعداد/Package أم ذاكرة/Runtime؟"}
    E -- "إعداد" --> F["Runtime جديد ثم خلية التثبيت"]
    E -- "ذاكرة" --> G["CPU/دفعة أصغر/طول أقصر"]
    D --> H["تحقق من رمز التشغيل والـRAM"]
```

## مشاكل شائعة

### `ModuleNotFoundError`

**السبب المعتاد:** لم تُشغّل خلية التثبيت، أو أُعيد تشغيل runtime.

**نفذ:**

1. ارجع إلى خلية Setup.
2. شغّلها مرة واحدة.
3. إذا طلبت restart، أعد الجلسة.
4. شغّل من الأعلى.

لا تضف إصدارًا عشوائيًا من الإنترنت؛ استخدم إصدار notebook.

### `CUDA out of memory`

**ليست مشكلة في إجابتك بالضرورة.**

1. احفظ checkpoint.
2. خفّض `batch_size`.
3. خفّض `max_length`.
4. استخدم reduced dataset.
5. انتقل إلى CPU/tiny model إذا وجهتك الصفحة.

بعد OOM قد تبقى الذاكرة محجوزة؛ أعد runtime عند الحاجة.

### GPU غير متاح

هذا متوقع أحيانًا في Colab Free. لا تنتظر أكثر من تعليمات الجلسة. اختر CPU وشغّل المسار 🟢 المصغر. [Colab يوضح رسميًا](https://research.google.com/colaboratory/faq.html) أن أنواع الموارد وحدودها تتغير.

### انقطع runtime أو اختفت الملفات

- أعد الاتصال.
- شغّل Runtime Doctor.
- استعد آخر checkpoint من Drive.
- لا تتوقع بقاء `/content`.
- راجع آخر commit و`PROGRESS.md`.

### Drive لا يركب

- تأكد أنك سجلت دخول الحساب الصحيح.
- اقرأ نافذة الصلاحية وأكملها.
- اسمح بالنوافذ المنبثقة لموقع Colab عند الحاجة.
- جرّب runtime جديدًا مرة واحدة.
- لا تشغّل أكواد mount متكررة داخل loop.

### فشل Save a copy in GitHub

- تأكد أن GitHub مفتوح ومسجل في المتصفح نفسه.
- اسمح لنافذة OAuth الرسمية.
- تأكد أنك تملك المستودع وأنه ليس read-only.
- اختر مسارًا لا يستبدل ملفًا آخر بالخطأ.
- احفظ/download ملف `.ipynb` مؤقتًا ثم ارفعه من GitHub web إن تعذر التكامل.

### `FileNotFoundError`

اطبع المكان الحالي والملفات:

```python
from pathlib import Path
print("cwd:", Path.cwd())
print("files:", [p.name for p in Path.cwd().iterdir()][:30])
```

لا تكتب مسار Drive من الذاكرة؛ انسخه من Files بعد mount.

### العربية تظهر مفصولة أو باتجاه غريب

قد يكون العرض فقط، لا البيانات. افحص:

```python
text = "مرحبًا بكم في بيان"
print(repr(text))
print(text.encode("utf-8"))
assert text.encode("utf-8").decode("utf-8") == text
```

لا تقلب الأحرف يدويًا ولا تحفظ نصًا معكوسًا.

### الاختبار فشل رغم أن المخرج “يشبه” الصحيح

الاختبار قد يفحص مسافة، Unicode code point، type، shape، أو ترتيبًا. اطبع `repr(value)` و`type(value)` و`shape` إن وجدت. لا تعدّل الاختبار ليصبح أخضر.

### فشل ONNX export أو `onnx.checker`

1. تأكد أن `model.eval()` استُدعيت وأن inputs tensors فعلية.
2. افحص أسماء `input_ids` و`attention_mask` وdtype `int64`.
3. استخدم opset المحددة في Notebook 08، ولا تغيّر عدة إعدادات معًا.
4. لا تعتبر وجود ملف `.onnx` نجاحًا إذا فشل checker أو parity.
5. احتفظ بـPyTorch FP32 وسجل أول error إن بقي operator غير مدعوم.

### ONNX Runtime: input أو shape mismatch

```python
print([(item.name, item.shape, item.type) for item in session.get_inputs()])
```

قارنها بالمفاتيح والأشكال المرسلة. لا تضف input غير موجود ولا تحذف `attention_mask` لأن النموذج أعطى نتيجة مرة واحدة.

### INT8 أبطأ أو خفّض الجودة

هذه نتيجة ممكنة وليست خطأ في المختبر:

- أعد warm-up وثبت workload والجهاز والbatch.
- احسب quality tax على الأمثلة نفسها.
- إذا لم يحقق candidate الميزانية فاختر `KEEP_PYTORCH_FP32` أو ONNX FP32 الموثق.
- لا تغيّر budget بعد رؤية النتيجة.

### FastAPI/TestClient يعيد 422

422 متوقع للطلب الفارغ أو اللغة غير المدعومة. إذا ظهر لطلب صالح، اطبع `response.json()` وافحص أسماء حقول JSON وأن `text` string و`language` واحدة من `ar/en/auto`.

### فاحص التسليم يعيد FAIL

اقرأ كل سطر `[ERROR]` وأصلح الملف المذكور؛ لا تعدّل `scripts/validate_submission.py` لتجاوز الشرط. الأخطاء المعتادة:

- placeholder مثل `YOUR_USERNAME` أو `FILL_ME`.
- notebook مفقود أو علامة Core غير موجودة.
- `benchmark_mode` ما زال `SYSTEMS_SMOKE`.
- وزن/ONNX/secret أو ملف أكبر من حد الدورة.
- tag النهائي غير موجود عند استخدام `--require-tag`.

## طلب المساعدة الصحيح

```text
Notebook:
Cell title:
Full error:
Expected:
Observed:
Runtime: CPU/GPU
One action already tried:
```

لا ترسل screenshot فقط إذا كان الخطأ قابلًا للنسخ. أخفِ البريد، أسماء الملفات الشخصية، tokens، ومسارات Drive الحساسة.

## متى أتوقف؟

توقف واطلب مساعدة إذا:

- ظهرت نافذة صلاحية غير متوقعة.
- طلب الكود password أو token داخل خلية عامة.
- وجدت بيانات شخصية حقيقية.
- تكرر الخطأ بعد runtime جديد والمسار المحدد.
- ستضطر إلى حذف/استبدال ملفات كثيرة ولا تعرف الهدف.
