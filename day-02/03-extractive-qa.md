# 3. الإجابة الاستخراجية عن الأسئلة
# Extractive Question Answering

## ما الفرق؟

- **Extractive QA:** تختار answer span موجودًا داخل context.
- **Abstractive QA:** تولد نصًا جديدًا.

اليوم نستخدم Extractive QA، لذلك يجب أن تكون الإجابة جزءًا حرفيًا من الوثيقة، أو تكون النتيجة «لا توجد إجابة».

```text
Question + Context
→ encoder
→ start logits + end logits
→ valid span or no-answer
```

## تجهيز البيانات

كل مثال يحتوي:

- `question`
- `context`
- `answer_text`
- `answer_start`
- أو `answer_text=null` للحالة غير القابلة للإجابة.

Fast tokenizer يعيد `offset_mapping` لربط tokens بمواضع الأحرف في context. نستخدم `sequence_ids()` لتمييز السؤال عن السياق.

## السياقات الطويلة

إذا تجاوز السياق حد النموذج:

1. نستخدم `truncation="only_second"`.
2. نقسمه إلى windows.
3. نضيف stride حتى لا تضيع إجابة على الحافة.
4. نجمع المرشحين من كل windows.

قص أول 384 token فقط قد يحذف الإجابة؛ لا يسمى ذلك خطأ النموذج قبل فحص التغطية.

## اختيار Span صالح

لا نأخذ argmax للبداية والنهاية بصورة مستقلة. المرشح يجب أن يحقق:

- start ≤ end
- الطول ≤ `max_answer_length`
- offsets تنتمي إلى context
- score = start logit + end logit

ثم نقارن أفضل span مع null score.

```python
from bayan.qa_postprocess import best_span

result = best_span(
    start_logits,
    end_logits,
    offsets,
    context,
    null_threshold=0.0,
)
print(result)
```

## لماذا No-answer إلزامية؟

إذا لم نقارن مع null score، سيستخرج النظام شيئًا حتى عندما لا تحتوي الوثيقة جوابًا. هذه ليست «إجابة ضعيفة» فقط؛ تصميم المسار يجبر النموذج على الادعاء.

في عينة اليوم:

```text
Context: تعمل العيادة من الأحد إلى الخميس.
Question: ما رقم هاتف العيادة؟
Expected: answer=None
```

## التطبيع وOffsets

إذا حسبت offsets على `model_text` ثم قصصت `display_text` المختلف، قد تعرض أحرفًا خاطئة. احتفظ بعلاقة واضحة بين النسختين أو نفذ extraction على النص الذي ستعرض منه النتيجة.

## المقاييس

- Exact Match: هل النص مطابق للإجابة المرجعية؟
- Token F1: مقدار تداخل tokens.
- Null accuracy: هل رفض الأسئلة غير القابلة للإجابة؟
- Coverage: هل windowing احتوى answer span أصلًا؟

في يوم التقييم سنفصل المقاييس حسب العربية والإنجليزية وطول السياق.

## أخطاء شائعة

- end قبل start.
- span طويل بلا حد.
- offsets من السؤال بدل context.
- تجاهل no-answer.
- tuning للـthreshold على test.
- ادعاء جودة من 10 أمثلة Smoke.

## دليل الاكتمال

- QA preprocessing ينتج start/end positions صحيحة.
- optimizer step واحدة على الأقل تنجح.
- اختبار span الصالح أخضر.
- اختبار no-answer أخضر.
- العينة موصوفة بأنها `MEASURED_SMOKE`.
