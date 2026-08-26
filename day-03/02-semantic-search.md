# 2. البحث الدلالي بتضمينات الجمل
# Semantic Search with Sentence Embeddings

## من التصنيف إلى الاسترجاع

التصنيف يجيب: «إلى أي فئة ينتمي النص؟»  
البحث يجيب: «ما الحالات الأقرب معنى لهذا الاستعلام؟»

في مشروع بيان يصل استعلام جديد، ويسترجع النظام حالات تعليمية سابقة مع حلولها. لا نستخدم task head الخاص بالتصنيف كتضمين جملة؛ نستخدم نموذجًا مدربًا لتمثيل التشابه الدلالي.

## ما هو sentence embedding؟

هو متجه واحد يمثل جملة أو مقطعًا. يضع sentence-transformer النصوص المتقاربة في المعنى بالقرب من بعضها داخل فضاء المتجهات. النموذج الأساسي في الدورة:

`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`

بطاقة النموذج تذكر دعمه لـ50 لغة وترخيص Apache-2.0. اخترناه لمسار عربي/إنجليزي مجاني، لكنه baseline تعليمي وليس ادعاء بأنه الأفضل لكل بيانات سعودية.

## Bi-encoder وCross-encoder

| النوع | كيف يعمل؟ | الميزة | التكلفة |
|---|---|---|---|
| **Bi-encoder** | يرمّز query والوثائق منفصلين | يمكن حساب وثائق corpus مسبقًا | قد يفوّت تفاعلًا دقيقًا |
| **Cross-encoder** | يقرأ query+candidate معًا | ترتيب أدق غالبًا حسب المهمة والنموذج | forward pass لكل زوج |

النمط العملي:

```text
retrieve many cheaply → re-rank a small candidate set carefully
```

Core يبني bi-encoder + FAISS. إعادة الترتيب باستخدام cross-encoder اختيارية؛ لأنها تتطلب checkpoint ثانيًا ووقتًا إضافيًا، ويجب قياس فائدتها وزمنها قبل اعتمادها.

## Cosine وL2 normalisation

نريد مقارنة الاتجاه، لا طول المتجه. مع FAISS نستخدم:

1. L2-normalise جميع corpus embeddings.
2. L2-normalise query embedding.
3. ابنِ `IndexFlatIP`.
4. أعلى inner product يصبح ترتيب cosine similarity.

```python
corpus_embeddings = model.encode(texts, normalize_embeddings=True)
query_embedding = model.encode([query], normalize_embeddings=True)

index = faiss.IndexFlatIP(corpus_embeddings.shape[1])
index.add(corpus_embeddings.astype("float32"))
scores, ids = index.search(query_embedding.astype("float32"), k=3)
```

نسيان التطبيع في جانب واحد يعطي نتائج تبدو معقولة ولا تعني cosine. لذلك يفحص notebook معيار كل متجه قبل الفهرسة.

## لماذا `IndexFlatIP`؟

لدينا 24 حالة تعليمية فقط. البحث exact هنا أبسط وأصدق وأسرع من تعليم ANN مع tuning غير ضروري. FAISS يوفّر IVF وHNSW وPQ لأحجام أكبر، لكن الاختيار يجب أن يبدأ من الحجم والقياس:

| الوضع | البداية المناسبة |
|---|---|
| آلاف أو عشرات آلاف والمتطلبات تسمح | Flat exact |
| ملايين وزمن البحث أصبح مشكلة مقاسة | ANN experiment |
| الذاكرة هي القيد | compression/PQ بعد قياس quality tax |

لا نستخدم HNSW لمجرد أنه متقدم؛ نستخدمه عندما يثبت benchmark أن Flat لم يعد يحقق الميزانية.

## البحث ثنائي اللغة

المشفّر متعدد اللغات يضع ترجمات الجمل في فضاء مشترك، فيصبح من الممكن أن يسترجع سؤال إنجليزي حالة عربية والعكس. لكن «الدعم» في بطاقة النموذج لا يساوي جودة متساوية. نقيس:

- monolingual slice؛
- cross-lingual slice؛
- Arabic vs English queries؛
- Gulf/MSA إن توفرت labels موثوقة.

## Recall@k وMRR@k

نحتاج query set بقرارات relevance معروفة.

### Recall@k

هل ظهرت حالة صحيحة ضمن أول `k`؟

```text
relevant = AR-004
top-3 = [EN-004, AR-004, AR-006]
Recall@3 for this query = 1
```

### MRR@k

يكافئ ظهور أول نتيجة صحيحة مبكرًا:

```text
first relevant at rank 2 → reciprocal rank = 1/2
```

Recall يقول «وجدناها»، وMRR يقول «كم كانت مبكرة؟». لا يعوض أحدهما الآخر.

## No-answer في البحث

لا يجوز عرض نتيجة ضعيفة لكل سؤال. نضبط `min_score` على validation queries التي تحتوي حالات جواب وعدم جواب، ثم نجمده قبل test.

```text
validation → tune threshold
test       → measure once with frozen threshold
```

cosine score ليس نسبة مئوية، و`0.70` لا يعني «70% صحيح». threshold تخص النموذج والبيانات والمعالجة.

## Manifest الفهرس

الفهرس ناتج مشتق، ويجب أن يثبت:

```json
{
  "model_id": "...",
  "embedding_dimension": 384,
  "normalization": "l2",
  "preprocessing_profile": "search@1.0.0/camel",
  "dataset_id": "bayan-day3-synthetic-v1",
  "vector_count": 24
}
```

لا تنسخ `384` يدويًا؛ notebook يأخذ البعد من embeddings الفعلية. إذا تغير النموذج أو profile أو corpus، أعد بناء الفهرس كاملًا.

## أخطاء شائعة

1. استخدام model embedding غير مخصص للتشابه.
2. تطبيع corpus وعدم تطبيع query أو العكس.
3. خلط vectors من إصدارين في فهرس واحد.
4. تقييم ثلاثة استعلامات بالعين دون relevance labels.
5. ضبط threshold على test.
6. تشغيل cross-encoder على corpus كامل بدل مرشحين محدودين.
7. رفع cache أو model weights إلى GitHub.

## التطبيق

نفّذ [Notebook 06 — Semantic Search](../notebooks/06_semantic_search.ipynb)، ثم احفظ manifest وmetrics فقط. الأوزان والكاش تبقى خارج GitHub.

## English recap

Core semantic search uses a multilingual bi-encoder, unit-normalised vectors, and exact FAISS inner-product search. Retrieval claims require a labelled query set, Recall@k, MRR@k, a validation-tuned no-answer threshold, and a manifest pinning the model, preprocessing, corpus, dimension, and vector count.
