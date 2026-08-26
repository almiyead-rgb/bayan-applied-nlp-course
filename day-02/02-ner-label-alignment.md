# 2. التعرف على الكيانات ومحاذاة BIO
# NER and BIO Label Alignment

## ما هو NER؟

Named Entity Recognition يحدد span في النص ويعطيه نوعًا. مخطط بيان التعليمي:

| النوع | مثال |
|---|---|
| SERVICE | بوابة التصاريح |
| LOCATION | الرياض |
| DATE | 2026-08-20 |
| REF_NUM | BAYAN-204 |
| ORG | وزارة الصحة |

## مخطط BIO

- `B-TYPE`: بداية كيان.
- `I-TYPE`: استمرار الكيان.
- `O`: خارج كيان.

مثال:

| Word | وزارة | الصحة | في | الرياض |
|---|---|---|---|---|
| Tag | B-ORG | I-ORG | O | B-LOCATION |

## فخ Subwords

الـannotation عادة كلمة بكلمة، بينما tokenizer قد يقسم كلمة إلى عدة subwords. نستخدم:

`tokenizer(words, is_split_into_words=True)`

ثم `word_ids()` لربط كل subword بكلمته.

عقد الدورة:

- special token → `-100`
- أول subword للكلمة → label الكلمة
- continuation subword → `-100`

`-100` هو ignore index في loss؛ لا يصوت في التدريب أو التقييم.

```python
from bayan.ner_alignment import align_word_labels

word_ids = [None, 0, 1, 1, 2, None]
word_labels = [0, 3, 0]

print(align_word_labels(word_ids, word_labels))
# [-100, 0, 3, -100, 0, -100]
```

## لماذا لا نكرر label؟

لو كانت كلمة LOCATION انقسمت إلى ثلاثة أجزاء وكررنا `B-LOCATION` ثلاث مرات، نصنع ثلاث بدايات كيانات وهمية. قد تبدو loss طبيعية بينما تنهار حدود الكيانات.

## التقييم الصحيح

Token accuracy قد تخفي خطأ الحدود. نستخدم strict entity-level F1:

- يجب أن يتطابق نوع الكيان وبدايته ونهايته.
- نقص كلمة واحدة من ORG متعددة الكلمات يعد خطأ span.
- نعرض per-type لاحقًا في اليوم الثالث.

```python
from bayan.ner_alignment import entity_f1

truth = [["B-ORG", "I-ORG", "O"]]
guess = [["B-ORG", "O", "O"]]
print(entity_f1(truth, guess))
# strict F1 = 0.0 لأن الحدود مختلفة
```

## العربية واللصائق

قد يظهر الموقع داخل `وبالرياض`. whitespace word لا يعكس دائمًا الوحدة الصرفية. اليوم نثبت محاذاة tokenizer؛ وفي اليوم الثالث نبني profile عربية باستخدام CAMeL Tools، بينما تبقى مقارنة morphological segmentation في Explore، مع قاعدة ثابتة:

> ما يطبق في التدريب يجب أن يطبق نفسه في الاستدلال.

## تحقق يدوي

حاذِم هذا المثال على الورق قبل الكود:

```text
Words:  ["راجعت", "وزارة", "الصحة", "أمس"]
Tags:   ["O", "B-ORG", "I-ORG", "B-DATE"]
```

بعد tokenisation، ضع `-100` عند special tokens وكل continuation.

## أخطاء شائعة

- مقارنة predictions subword مع labels word-level.
- نسيان إزالة `-100` قبل التقرير.
- خلط `label2id` و`id2label`.
- تقييم token accuracy فقط.
- تطبيع train بطريقة وserve بطريقة أخرى.
- تحويل I غير صالح بصمت دون فحص البيانات.

## دليل الاكتمال

- اختبار special tokens أخضر.
- اختبار continuation أخضر.
- اختبار out-of-range يرفض الخطأ.
- entity-level boundary test أخضر.
- training smoke ينتج loss finite.
