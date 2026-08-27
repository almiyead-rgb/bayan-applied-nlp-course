# اليوم الأول — من النص إلى Tensor  
# Day 1 — From Text to Tensor

**إعداد وتقديم | Prepared and delivered by:** ميعاد المري · Meaad Al-Marri  
**الوقت | Time:** 08:30–13:30 · **المسار الأساسي:** CPU · **المشروع:** بوابة بيان A

## سؤال اليوم | Driving question

> كيف تتحول جملة مثل «الخدمة ممتازة» إلى مصفوفات يستطيع Transformer معالجتها، وما الذي قد يفسد في الطريق؟

اليوم لا نحفظ أسماء مكتبات فقط؛ سنبني المسار كاملًا ونفحص كل انتقال:

```mermaid
flowchart LR
    A["نص خام"] --> B["نسخة عرض + حماية"]
    B --> C["تطبيع معلن"]
    C --> D["Tokens + IDs"]
    D --> E["Embeddings"]
    E --> F["Attention"]
    F --> G["Encoder output"]
```

**English:** We follow a bilingual sentence from raw text to protected model text, tokens, IDs, embeddings, self-attention, and an encoder representation.

## بنهاية اليوم ستتمكن من

1. فحص Unicode دون إفساد العربية.
2. فصل نسخة العرض عن نسخة النموذج.
3. تطبيق masking وnormalisation وتقسيم الجمل بـspaCy بقرارات صريحة.
4. تفسير token وsubword وspecial token.
5. قياس token fertility وخطر truncation.
6. شرح الفرق بين token ID وembedding.
7. حساب scaled dot-product attention وفحص shapes.
8. رسم Transformer encoder block وشرح دور كل جزء.
9. تسليم بوابة بيان A باختبارات خضراء وقرار tokenizer.

## الجدول | Schedule

| الوقت | الموضوع | ما ستنتجه |
|---|---|---|
| 08:30–09:20 | انطلاقة البرنامج: لماذا أُعيد بناء NLP؟ + مشروع بيان + [خط النص](01-text-preprocessing.md) | خريطة المشروع + مخاطر corpus أولية |
| 09:20–09:30 | استراحة | — |
| 09:30–10:20 | [المعالجة والترميز والتضمينات](01-text-preprocessing.md) + [تفاصيل tokenisation](02-tokenization-embeddings.md) | عقد نسختين + fertility + token IDs |
| 10:20–10:30 | استراحة | — |
| 10:30–11:20 | Lab 1: [Notebook 01](../notebooks/01_text_processing_tokenization.ipynb) | pipeline ثنائي اللغة + golden tests + قرار tokenizer |
| 11:20–11:30 | استراحة | — |
| 11:30–12:20 | [Attention وTransformers](03-attention-transformers.md) | attention matrix + encoder map |
| 12:20–12:40 | استراحة طويلة/صلاة | احفظ نقطة استعادة |
| 12:40–13:30 | Lab 2: [Notebook 02](../notebooks/02_attention_transformers.ipynb) + [Gate A](04-labs-checkpoint.md) | parameter audit + forward/heatmap + commit |

## دفاتر اليوم | Notebooks

| الدفتر | الغرض | التكلفة |
|---|---|---|
| [01 — Text Processing & Tokenisation](../notebooks/01_text_processing_tokenization.ipynb) | Unicode، masking، profiles، spaCy، WordPiece، fertility، embeddings | مجاني، CPU |
| [02 — Attention & Transformers](../notebooks/02_attention_transformers.ipynb) | Q/K/V، scaling، masks، multi-head، تدقيق معاملات وforward فعلي | مجاني، CPU |

## مستويات اليوم

### 🟢 Core — للجميع

- تشغيل الدفترين بالترتيب.
- نجاح اختبارات preprocessing وattention.
- مقارنة العربية والإنجليزية في fertility.
- كتابة قرار tokenizer من 4 أسطر.
- commit بوابة اليوم.

### 🔵 Explore

- قارن profile عربيين وسجّل ما تغير في token count.
- قس truncation rate عند طولين.
- غيّر keep mask وفسّر النتيجة.

### 🟣 Distinction

- أضف slice للهجة أو Arabizi دون تغيير النص الأصلي.
- قارن tokenizer إضافيًا موثقًا مع المعيار نفسه.
- تحقق عدديًا من PyTorch SDPA على أكثر من seed.

## قواعد اليوم

- لا تنظف النص قبل أن تحفظ نسخة عرض آمنة.
- لا تستخدم normalization لأن شكل النص “أجمل”.
- لا تفصل tokenizer عن checkpoint الذي ينتمي إليه.
- لا تعامل token ID كأنه معنى؛ المعنى المتعلم في embedding/model.
- لا تعرض attention heatmap كبرهان سببي على تفسير القرار.
- لا تنتقل إلى Explore قبل نجاح Core.

## نقطة البداية

1. شغّل [Runtime Doctor](../notebooks/00_runtime_doctor.ipynb).
2. افتح الدفتر 01 واحفظ نسخة في Drive.
3. أبقِ هذه الصفحة في تبويب منفصل للعودة إلى التعريفات.
4. عند ظهور خطأ استخدم [دليل الأعطال](../docs/setup/troubleshooting.md).

## قاموس اليوم

[Unicode](../docs/glossary/README.md#قاموس-معالجة-اللغات-الطبيعية--nlp-glossary) · Token · Subword · Vocabulary · Fertility · Embedding · Attention · Query · Key · Value · Encoder · Checkpoint

## مراجع اليوم

جميع الادعاءات التقنية مرتبطة بمصادرها الأولية في [REFERENCES.md](REFERENCES.md).
