# مراجع اليوم الرابع | Day 4 References

**آخر تحقق | Last verified:** 26 August 2026

المصادر هنا رسمية/أولية. لا تُستخدم الأرقام المنشورة كبديل للقياس على Colab الخاص بالمتدرب.

## القياس والمدخلات

- [PyTorch `inference_mode`](https://docs.pytorch.org/docs/stable/generated/torch.autograd.grad_mode.inference_mode.html) — إيقاف overhead المرتبط بـautograd أثناء الاستدلال؛ لا يغني عن `model.eval()`.
- [Transformers: Padding and truncation](https://huggingface.co/docs/transformers/en/pad_truncation) — `padding`, `truncation`, و`max_length`.
- [Python `time.perf_counter_ns`](https://docs.python.org/3/library/time.html#time.perf_counter_ns) — ساعة عالية الدقة لقياس مدد قصيرة.
- [psutil process memory](https://psutil.readthedocs.io/en/latest/#psutil.Process.memory_info) — RSS للعملية؛ قياس تقريبي يجب وصف حدوده.

## ONNX وONNX Runtime

- [ONNX overview](https://onnx.ai/onnx/intro/) — صيغة graph المفتوحة ومبادئها.
- [PyTorch ONNX exporter](https://docs.pytorch.org/docs/stable/onnx.html) — التصدير من PyTorch.
- [ONNX model checker](https://onnx.ai/onnx/api/checker.html) — التحقق البنيوي من model graph.
- [ONNX Runtime Python quickstart](https://onnxruntime.ai/docs/get-started/with-python.html) — إنشاء جلسة inference.
- [ONNX Runtime quantisation](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html) — dynamic/static quantisation واختيار الطريقة؛ توصي الصفحة عمومًا بـdynamic quantisation للمحولات مع ضرورة القياس.
- [Hugging Face Optimum ONNX](https://huggingface.co/docs/optimum-onnx/index) — مسار اختياري رسمي للتصدير والتحسين.
- [Optimum ONNX quantisation guide](https://huggingface.co/docs/optimum-onnx/onnxruntime/usage_guides/quantization) — API الحزمة المنفصلة الحالية.

## FastAPI والاختبار

- [FastAPI request body](https://fastapi.tiangolo.com/tutorial/body/) — نماذج Pydantic والتحقق.
- [FastAPI testing with TestClient](https://fastapi.tiangolo.com/tutorial/testing/) — نمط اختبار HTTP المباشر.
- [Starlette TestClient](https://www.starlette.io/testclient/) — المرجع الحالي لاستخدام TestClient المبني على HTTPX2.
- [FastAPI lifespan testing](https://fastapi.tiangolo.com/advanced/testing-events/) — تشغيل startup/shutdown عند الاختبار.
- [Pydantic fields](https://docs.pydantic.dev/latest/concepts/fields/) — قيود الحقول والعقود.

## GitHub release

- [About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [Managing releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)

## إصدارات Core المثبتة

ملف [`requirements-day4.txt`](../requirements-day4.txt) هو عقد المختبر المراجع في التاريخ أعلاه:

- Transformers 5.15.1 وTokenizers 0.22.2.
- ONNX 1.22.0.
- ONNX Runtime 1.29.0 (CPU).
- FastAPI 0.141.1 وHTTPX2 2.12.0.
- psutil 7.2.2.

تستخدم بيئة Colab المرجعية NumPy وPyTorch المثبتين مسبقًا. لا تثبت `onnxruntime` و`onnxruntime-gpu` معًا في Core. حزمة `optimum-onnx` 0.1.0 خيار Explore منفصل وليست لازمة لدفتر 08.

## Checkpoint مسار Systems Smoke

- [`prajjwal1/bert-tiny` model card](https://huggingface.co/prajjwal1/bert-tiny) — BERT صغير (L=2, H=128)، English-only، MIT. يستخدم فقط لفحص البنية التقنية بسرعة، ولا يمثل جودة بيان العربية/الإنجليزية.

المشروع النهائي يعيد القياس على artefact المتدرب متعدد اللغات. لا تنسب إلى checkpoint الصغير قدرة عربية أو جودة مهمة لم تُقَس.
