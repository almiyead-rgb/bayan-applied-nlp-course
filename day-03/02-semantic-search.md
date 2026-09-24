# 2. البحث الدلالي بتضمينات الجمل
# Semantic Search with Sentence Embeddings

<!-- BAYAN_YOUTUBE_START -->
### شاهد الفكرة ثم طبّقها | Video companions

<div class="card youtube-topic youtube-t15"><h3 class="pair"><span class="en" lang="en" dir="ltr">Sentence embeddings and cosine</span><span class="ar" lang="ar" dir="rtl">تضمينات الجمل وتشابه جيب التمام</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Represent a sentence, then compare the direction of two vectors.</p><p class="ar" lang="ar" dir="rtl">مثّل الجملة ثم قارن اتجاه متجهين.</p></div><p><strong lang="en" dir="ltr">Sentence Transformers / SBERT</strong><br><span class="micro">James Briggs · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=WS1uVMGhlWQ" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><details><summary>شرح إضافي عند الحاجة · More explanation when needed</summary><p><strong lang="en" dir="ltr">Cosine Similarity, Clearly Explained!</strong><br><span class="micro">StatQuest · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=e9U0QAFbfLI" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p></details><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">Why is a classifier output not automatically a sentence embedding for search?</p><p class="ar" lang="ar" dir="rtl">لماذا لا تُستخدم مخرجات المصنف تلقائيًا كتضمين جملة للبحث؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<div class="card youtube-topic youtube-t16"><h3 class="pair"><span class="en" lang="en" dir="ltr">Semantic search with FAISS</span><span class="ar" lang="ar" dir="rtl">البحث الدلالي باستخدام FAISS</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Follow the query from sentence vector to retrieved candidates.</p><p class="ar" lang="ar" dir="rtl">تتبع الاستعلام من متجه الجملة إلى المرشحين المسترجعين.</p></div><p><strong lang="en" dir="ltr">Introduction to FAISS</strong><br><span class="micro">James Briggs · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=sKyvsdEv6rk" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><div class="callout warning"><div class="pair"><p class="en" lang="en" dir="ltr">Use the course IndexFlatIP setup. Other index types in the video are not additional requirements.</p><p class="ar" lang="ar" dir="rtl">استخدم إعداد IndexFlatIP في الدورة؛ الأنواع الأخرى ليست متطلبات إضافية.</p></div></div><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">Why must query and case vectors follow the same encoding and normalisation contract?</p><p class="ar" lang="ar" dir="rtl">لماذا يجب توحيد عقد ترميز وتطبيع الاستعلامات والحالات؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<div class="card youtube-topic youtube-t17"><h3 class="pair"><span class="en" lang="en" dir="ltr">Retrieve, then re-rank</span><span class="ar" lang="ar" dir="rtl">استرجع ثم أعد الترتيب</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Compare embedding retrieval with a cross-encoder reranking step.</p><p class="ar" lang="ar" dir="rtl">قارن استرجاع التضمينات بمرحلة إعادة الترتيب بالمشفر المشترك.</p></div><p><strong lang="en" dir="ltr">RAG But Better: Rerankers with Cohere AI</strong><br><span class="micro">James Briggs · English audio / الصوت بالإنجليزية</span></p><div class="pair"><p class="en" lang="en" dir="ltr">Suggested segment 01:25–08:20; stop at the end shown.</p><p class="ar" lang="ar" dir="rtl">المقطع المقترح 01:25–08:20؛ توقف عند النهاية المحددة.</p></div><p><a class="button primary" href="https://www.youtube.com/watch?v=Uh9bYiVrW_s&amp;t=85s" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><div class="callout warning"><div class="pair"><p class="en" lang="en" dir="ltr">Watch the explanation only; stop before the paid-service implementation. No Cohere/OpenAI key, Pinecone account or RAG assignment is required.</p><p class="ar" lang="ar" dir="rtl">شاهد المفهوم فقط وتوقف قبل تطبيق الخدمات المدفوعة. لا يلزم مفتاح Cohere أو OpenAI أو حساب Pinecone أو مشروع RAG.</p></div></div><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">Why rerank a shortlist instead of every document?</p><p class="ar" lang="ar" dir="rtl">لماذا نعيد ترتيب قائمة قصيرة بدل جميع المستندات؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<div class="card youtube-topic youtube-t18"><h3 class="pair"><span class="en" lang="en" dir="ltr">Task metrics and retrieval ranking</span><span class="ar" lang="ar" dir="rtl">مقاييس المهام وترتيب البحث</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Separate classification quality from retrieval and ranking quality.</p><p class="ar" lang="ar" dir="rtl">افصل جودة التصنيف عن جودة الاسترجاع والترتيب.</p></div><p><strong lang="en" dir="ltr">Precision, Recall and F1 Score</strong><br><span class="micro">codebasics · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=2osIZ-dSPGE" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><p><strong lang="en" dir="ltr">Evaluation Measures for Search and Recommender Systems</strong><br><span class="micro">James Briggs · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=BD9TkvEsKwM" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><div class="callout warning"><div class="pair"><p class="en" lang="en" dir="ltr">Recall@k and MRR are the focus. Additional ranking metrics shown are enrichment only.</p><p class="ar" lang="ar" dir="rtl">التركيز على Recall@k وMRR؛ المقاييس الإضافية للتوسع فقط.</p></div></div><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">How can Recall@k stay the same while MRR changes?</p><p class="ar" lang="ar" dir="rtl">كيف يبقى Recall@k ثابتًا بينما يتغير MRR؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<!-- BAYAN_YOUTUBE_END -->

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

يبني Core bi-encoder + FAISS، ثم يعيد ترتيب مجموعة صغيرة من المرشحين باستخدام cross-encoder متعدد اللغات. لا يُعتمد الـreranker لمجرد أنه أكثر تعقيدًا: يقيس المختبر `MRR@3` قبل/بعد وزمن المرحلة وحدها، ثم يوثق قرار القبول أو الرفض.

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

نفّذ [Notebook 06 — Semantic Search](../notebooks/06_semantic_search.ipynb)، ثم احفظ manifest وmetrics وقرار re-ranking فقط. الأوزان والكاش تبقى خارج GitHub.

## English recap

Core semantic search uses a multilingual bi-encoder, unit-normalised vectors, and exact FAISS inner-product search. Retrieval claims require a labelled query set, Recall@k, MRR@k, a validation-tuned no-answer threshold, and a manifest pinning the model, preprocessing, corpus, dimension, and vector count.
