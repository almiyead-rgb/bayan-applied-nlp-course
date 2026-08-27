# 4. المختبران وبوابة بيان A  
# Labs and Bayan Gate A

## قبل المختبر

- [ ] `BAYAN_ENV_READY = True`.
- [ ] حفظت نسخة notebook في Drive.
- [ ] مستودعك العام مفتوح.
- [ ] بدأت 🟢 Core.
- [ ] لن تضع أوزان نموذج أو بيانات حساسة في GitHub.

## Lab 1 — Text Processing & Tokenisation

افتح:

[01_text_processing_tokenization.ipynb](../notebooks/01_text_processing_tokenization.ipynb)

### المطلوب

1. افحص Unicode لنص عربي.
2. أنشئ `display_text` و`model_text`.
3. اخفِ email/phone التعليميين.
4. قسّم نسخة النموذج المحمية إلى جمل باستخدام spaCy، واختبر حالة اختصار معروفة.
5. شغّل profile محافظًا.
6. قارن offline WordPiece وmBERT tokenizer إن توفر الاتصال.
7. قس fertility للعربية والإنجليزية.
8. قس truncation rate لطولين.
9. اربط IDs بembedding matrix صغيرة.
10. اكتب قرار tokenizer.

### اختبارات النجاح

```bash
PYTHONPATH=src pytest -q   tests/test_day1_preprocessing.py   tests/test_day1_tokenization.py
```

الهدف `TARGET`: جميع الاختبارات خضراء.

### قرار tokenizer

اكتب في `DECISIONS.md`:

```markdown
## Day 1 — Tokenizer decision

Checkpoint/tokenizer:
Corpus slice:
Arabic fertility [MEASURED]:
English fertility [MEASURED]:
Truncation rate at max_length=... [MEASURED]:
Known limitation:
Decision and reason:
```

## Lab 2 — Attention & Transformers

افتح:

[02_attention_transformers.ipynb](../notebooks/02_attention_transformers.ipynb)

### المطلوب

1. نفذ/شغّل scaled attention.
2. تحقق أن كل صف weights مجموعه 1.
3. طبق keep mask.
4. قارن NumPy وPyTorch SDPA إذا توفر PyTorch.
5. تتبع shapes في multi-head split/combine.
6. مرر tensor عبر EncoderLayer على CPU.
7. نفّذ تدقيق معاملات معماريًا على checkpointين من عائلة BERT، واشرح أثر حجم vocabulary.
8. نفّذ forward pass فعليًا على جملة عربية وأخرى إنجليزية.
9. اعرض رأس attention واحدًا مع أسماء tokens.
10. اشرح attention matrix دون ادعاء سببي.

### اختبار النجاح

```bash
PYTHONPATH=src pytest -q tests/test_day1_attention.py
```

## بوابة بيان A | Gate A

لا تنتقل إلى اليوم الثاني قبل تحققها:

| الدليل | شرط القبول |
|---|---|
| `src/bayan/preprocessing.py` | يستخدم عقد النسختين وprofile معلن |
| preprocessing tests | خضراء |
| attention tests | خضراء |
| notebook 01 | يعمل بالترتيب؛ spaCy وقياسات الترميز ونتائجه موسومة |
| notebook 02 | يعمل بالترتيب؛ تدقيق checkpointين وforward فعلي وخريطة attention ظاهرة |
| `DECISIONS.md#day-1-tokenizer-decision` | يحتوي قياسات وحدًا معروفًا |
| `PROGRESS.md` | Day 1 = complete |
| الخصوصية | لا raw PII ولا secret |
| commit | موجود برسالة واضحة |

### Commit المقترح

`feat: complete day 1 preprocessing tokenization and attention`

## فحص الفهم | Exit ticket

أجب دون تشغيل الكود:

1. لماذا لا يكفي `text.split()` لنموذج BERT؟
2. لماذا يجب أن يأتي tokenizer والنموذج من checkpoint واحد؟
3. اذكر تحويلًا عربيًا قد يزيل معلومة.
4. ماذا تقيس fertility؟ وماذا لا تثبت؟
5. ما الفرق بين token ID وembedding؟
6. ما shape مصفوفة attention لتسلسل طوله (n) في head واحد؟
7. لماذا نقسم scores على (sqrt{d_k})؟
8. لماذا لا نعرض attention weights كتفسير سببي تلقائي؟

## إذا انتهيت مبكرًا

### 🔵 Explore

- قارن profile محافظًا وآخر يزيل التشكيل.
- اكتب جدول الفرق في tokens/fertility.
- لا تعلن فائزًا بلا metric للمهمة.

### 🟣 Distinction

- أضف test للـclitic `وبالخدمة`.
- قارن mask semantics في NumPy وPyTorch.
- نفذ repeated run بثلاث بذور لembedding toy واكتب ما يتغير وما لا.

## نقطة الاستعادة

قبل إغلاق Colab:

1. Save a copy in Drive.
2. احفظ التقرير الصغير.
3. Save a copy in GitHub.
4. افتح الملف من GitHub وتأكد أنه موجود.
5. حدّث `PROGRESS.md`.
6. انسخ رابط commit في ملاحظاتك.
