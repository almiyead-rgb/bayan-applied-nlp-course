# 3. FastAPI وعقد الخدمة وCanaries
# FastAPI, Service Contracts, and Canaries

## من دالة إلى خدمة

النموذج ينتج logits، لكن المستفيد يحتاج عقدًا ثابتًا:

```json
{
  "request_id": "req-001",
  "language": "ar",
  "prediction": {"label": "positive", "confidence": 0.91},
  "latency_ms": 18.4,
  "model": {
    "id": "bayan-classifier",
    "version": "1.0.0",
    "runtime": "onnxruntime-cpu",
    "preprocessing_version": "ar-en-v1"
  }
}
```

وجود version وruntime في الاستجابة يجعل الخطأ قابلًا للتتبع. لا تُرجع النص الخام أو بيانات حساسة في logs.

## Endpoints الأساسية

| المسار | الوظيفة | نجاح متوقع |
|---|---|---|
| `GET /health` | readiness + model/preprocessing version | 200 بعد نجاح canaries |
| `POST /v1/classify` | تحقق input ثم inference ثم response | 200 لطلب صالح |
| OpenAPI `/docs` | توثيق آلي للتطوير | اختياري داخل runtime |

يجب أن يرفض Pydantic النص الفارغ والطويل جدًا واللغة غير المدعومة قبل وصولها إلى النموذج.

## عقد Request مبسط

```python
from typing import Literal
from pydantic import BaseModel, Field

class ClassifyRequest(BaseModel):
    text: str = Field(min_length=1, max_length=1000)
    language: Literal["ar", "en", "auto"] = "auto"
```

لا تستخدم `str` بلا حدود ثم تتوقع أن tokenizer يحمي الخدمة.

## الاختبار داخل Colab بلا استضافة

```python
from fastapi.testclient import TestClient

with TestClient(app) as client:
    health = client.get("/health")
    arabic = client.post(
        "/v1/classify",
        json={"text": "الخدمة واضحة", "language": "ar"},
    )
    invalid = client.post(
        "/v1/classify",
        json={"text": "", "language": "auto"},
    )

assert health.status_code == 200
assert arabic.status_code == 200
assert invalid.status_code == 422
```

`TestClient` يختبر عقد HTTP داخل العملية نفسها. لا يحتاج رابطًا عامًا أو tunnel أو اشتراكًا. الاستضافة ليست شرطًا لإثبات الهدف.

## ما هي Startup Canary؟

حالة صغيرة معروفة تُشغل عند تجهيز الخدمة لتكشف الانكسار قبل استقبال الطلبات:

- مثال عربي ومثال إنجليزي.
- expected label مثبت من artefact المقبول، لا من الذاكرة.
- confidence ضمن `[0, 1]`.
- response schema كامل.
- model وpreprocessing versions متوافقة.

إذا فشلت canary تبقى readiness غير جاهزة. لا نلتقط الاستثناء ونطبع تحذيرًا ثم نعلن health ناجحًا.

## Train–serve skew

يحدث عندما تختلف معالجة الخدمة عن التدريب، مثل:

- إزالة همزات في الخدمة فقط.
- label map بترتيب مختلف.
- `max_length` أو tokenizer revision مختلف.
- فهرس FAISS مبني بمشفّر قديم.

الحل: وحدة preprocessing واحدة versioned + manifest + golden tests + canaries. نسخ regex من notebook إلى endpoint يخلق مصدرين للحقيقة.

## اختبارات Gate D

- [ ] `/health` يذكر الإصدارات والـruntime.
- [ ] طلب عربي صالح يعيد 200 وschema صحيحًا.
- [ ] طلب إنجليزي صالح يعيد 200.
- [ ] النص الفارغ يعيد 422.
- [ ] اللغة غير المدعومة تعيد 422.
- [ ] النص فوق الحد يعاد رفضه.
- [ ] canaries تمر على artefact المختار.
- [ ] mismatch في preprocessing version يفشل startup.
- [ ] لا raw PII أو secrets في response/logs.

## حدود هذا المختبر

TestClient يثبت صحة العقد الأساسية، لكنه لا يثبت تحمل حمل إنتاجي أو أمن نشر عام. load testing وauthentication وTLS وrate limiting وmonitoring موضوعات نشر لاحقة. لا نعرض خدمة Colab المؤقتة للعامة.

## English recap

FastAPI wraps the chosen artefact in a validated, versioned contract. TestClient proves HTTP behaviour without hosting. Startup canaries and manifest checks fail closed when labels, preprocessing, or artefacts drift; production security and load testing remain outside this classroom smoke test.
