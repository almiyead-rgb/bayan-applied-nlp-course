# 1. معالجة العربية باستخدام CAMeL Tools
# Arabic NLP with CAMeL Tools

## الفكرة الأولى: العربية ليست «نصًا يحتاج تنظيفًا أكثر»

العربية تضع قرارات هندسية مختلفة أمام pipeline:

- **الصرف | Morphology:** الجذر والنمط واللواحق تنتج أشكالًا كثيرة من المعنى نفسه.
- **اللواصق | Clitics:** في `وبالرياض` تلتصق الواو والباء و`الـ` بالاسم.
- **التشكيل | Diacritics:** قد يوجد أو يغيب، وقد يغير المعنى.
- **التنوع الإملائي | Orthographic variation:** مثل `أ/إ/آ/ا` و`ى/ي`.
- **السجل واللهجة | Register and dialect:** MSA في النص الرسمي، ولهجات في المحادثة، وقد يجتمعان.
- **Arabizi:** عربية بحروف لاتينية وأرقام، مثل `ma wasalni code 3al jawal`.

لا يعني ذلك تطبيق أكبر عدد من التحويلات. المعالجة الجيدة هي **أقل تحويل موثق تحتاجه المهمة والنموذج**.

## قاعدة النسختين | Two-copy contract

لا نعدل النص الذي سيُعرض للمستخدم أو تستخدم إزاحاته في QA. ننشئ نسختين:

| النسخة | وظيفتها | ما يجوز عليها؟ |
|---|---|---|
| `display_text` | العرض والتدقيق والإزاحات | تبقى كما كتبها المستخدم، مع حماية التخزين حسب السياسة |
| `model_text` | النموذج والفهرس | PII masking ثم profile موثق ومتكرر |

مثال:

```text
display_text: "إِدَارَةُ الهُدَى"
model_text:   "ادارة الهدي"
```

التغيير في `model_text` مقصود للبحث التعليمي. لا يعاد عرضه على أنه كتابة المستخدم.

## ما الذي يقدمه CAMeL Tools؟

في Core نستخدم utilities لا تحتاج تنزيل حزم بيانات لغوية كبيرة:

```python
from camel_tools.utils.dediac import dediac_ar
from camel_tools.utils.normalize import (
    normalize_alef_ar,
    normalize_alef_maksura_ar,
    normalize_unicode,
)
```

وظائف CAMeL Tools الرسمية تفصل Unicode normalisation، إزالة التشكيل، وتوحيد أشكال الألف والياء المقصورة. نستخدمها لأنها معرفة ومختبرة وواضحة السلوك، لا لأن كل وظيفة يجب تشغيلها دائمًا.

## Profiles اليوم الثالث

| Profile | التحويلات | الاستخدام التعليمي |
|---|---|---|
| `conservative` | NFC + إزالة التطويل + PII masking + whitespace | نموذج أو مهمة تحتاج حفظ أكبر قدر من الرسم |
| `search` | السابق + إزالة التشكيل + توحيد الألف + `ى→ي` | نسخة الفهرسة والاستعلام في مختبر البحث |

لا يطبع `search` التاء المربوطة إلى هاء. هذا تحويل إضافي قد يدمج فروقًا، ولا نطبقه بلا دليل من المهمة أو بطاقة checkpoint.

### لماذا profile باسم ونسخة؟

لأن الخطأ الأخطر ليس اختيار تحويل غير مثالي؛ بل اختلافه بين المراحل:

```text
index build: search@1.0.0/camel
query time:  conservative@1.0.0/camel   ← preprocessing skew
```

يجب أن يحمل manifest اسم profile والنسخة والbackend، وأن ترفض الخدمة تحميل فهرس لا يطابق إعدادها.

## التطبيع ليس تحسينًا مضمونًا

| قرار | قد يفيد | قد يضر |
|---|---|---|
| إزالة التشكيل | توحيد النص الشائع غير المشكول | مهمة تعتمد على التشكيل |
| توحيد الألف | search/dedup في بيانات متغيرة | استعادة الشكل الأصلي إن فقدت raw copy |
| `ى→ي` | تقليل التباين | نموذج تدرب على وصفة مختلفة |
| فصل اللواصق | إظهار حدود NER | mismatch إذا لم يستخدم في train وserve معًا |
| transliteration لـArabizi | توسيع التغطية | أخطاء تحويل تحتاج تقييمًا مستقلًا |

## اللهجة: قِسها ولا تفترضها

ملف اليوم الثالث يحتوي عمود `variant` معرفًا يدويًا لأغراض الدورة: `Gulf` و`MSA` و`Arabizi`. هذا العمود **ليس** تنبؤًا من CAMeL Tools. نستخدمه لبناء slices ومعرفة ما إذا كان المتوسط العام يخفي ضعفًا.

يوفر CAMeL Tools dialect identifier مدربًا مسبقًا ويمكنه إرجاع label على مستوى المدينة أو الدولة أو المنطقة. لكنه يحتاج حزمة بيانات إضافية، والوثائق الرسمية تنبه إلى أن مكون dialect ID غير متاح على Windows. لذلك هو Explore، وليس شرط Core أو الاجتياز.

## اختيار checkpoint عربي

الاسم المشهور لا يكفي. املأ بطاقة القرار التالية:

| سؤال | دليل مطلوب |
|---|---|
| ما نسبة MSA واللهجة وEnglish وArabizi؟ | corpus audit |
| ما المهمة؟ | classification/NER/QA/embeddings |
| ما وصفة preprocessing؟ | model card |
| هل tokenizer مناسب للنص؟ | fertility + truncation |
| هل الأداء متوازن؟ | per-variant slices |
| ما التكلفة؟ | parameters + latency + memory |
| ما الترخيص؟ | model card/license file |

CAMeLBERT يقدم checkpoints منفصلة لـMSA واللهجات والعربية الكلاسيكية والمزيج. AraBERT يملك إصدارات تختلف في pre-segmentation. هذه الفروق هي سبب قراءة بطاقة النموذج بدل نسخ اسم checkpoint فقط.

## أخطاء شائعة

1. تغيير `display_text` ثم فقدان offsets الأصلية.
2. تطبيق profile واحدة على كل checkpoints بلا قراءة model card.
3. استخدام segmentation أثناء التدريب ونسيانها في الخدمة.
4. وصف Arabizi heuristic بأنه dialect classifier.
5. تقييم نموذج عربي على MSA فقط مع أن الاستخدام الفعلي لهجي.
6. تنزيل كل CAMeL data أثناء الحصة رغم أن Core يحتاج utilities فقط.

## تحقق سريع

أجب قبل فتح notebook:

1. لماذا نحفظ raw/display copy؟
2. ما الفرق بين profile مرتبطة بالمهمة و«تنظيف عام»؟
3. هل `ى→ي` حقيقة لغوية أم قرار نمذجة؟
4. لماذا لا يكفي aggregate metric عند وجود Gulf وMSA؟
5. ماذا يجب أن يحدث للفهرس إذا تغير profile؟

## التطبيق

نفّذ [Notebook 05 — Arabic NLP](../notebooks/05_arabic_nlp.ipynb). المطلوب ليس حفظ أسماء الدوال؛ المطلوب إثبات عقد ثابت بين corpus وmodel وindex وquery.

## English recap

Arabic processing is an explicit model contract, not generic cleaning. Preserve an authoritative display copy, create a protected model copy, pin a named profile and backend, audit traffic variants, and evaluate the slices you actually serve. CAMeL Tools utilities are Core; large data-backed components remain optional.
