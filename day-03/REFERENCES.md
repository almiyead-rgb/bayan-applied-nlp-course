# مراجع اليوم الثالث | Day 3 References

**آخر تحقق:** 26 أغسطس 2026.  
الروابط أدناه مصادر أولية أو وثائق رسمية. أرقام نتائج المتدرب لا تؤخذ منها؛ تُقاس داخل Colab وتوسم حسب مصدرها.

## CAMeL Tools والعربية

- [CAMeL Tools 1.6.0 documentation](https://camel-tools.readthedocs.io/en/latest/)
- [CAMeL Tools normalisation API](https://camel-tools.readthedocs.io/en/latest/api/utils/normalize.html)
- [CAMeL Tools dediacritisation API](https://camel-tools.readthedocs.io/en/latest/api/utils/dediac.html)
- [CAMeL Tools dialect identification API](https://camel-tools.readthedocs.io/en/latest/api/dialectid.html)
- [CAMeL Tools package 1.6.0 on PyPI](https://pypi.org/project/camel-tools/1.6.0/)
- [CAMeL Tools paper — ACL Anthology](https://aclanthology.org/2020.lrec-1.868/)
- [CAMeLBERT-Mix official model card](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-mix)
- [CAMeLBERT-DA official model card](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-da)
- [AraBERT v0.2 official model card](https://huggingface.co/aubmindlab/bert-base-arabertv02)

## Sentence embeddings والبحث

- [Sentence Transformers semantic search documentation](https://sbert.net/examples/sentence_transformer/applications/semantic-search/)
- [Sentence Transformers retrieve-and-rerank documentation](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html)
- [Sentence Transformers 6.0.0 on PyPI](https://pypi.org/project/sentence-transformers/6.0.0/)
- [Multilingual MiniLM official model card](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)
- [Multilingual mMARCO cross-encoder model card](https://huggingface.co/cross-encoder/mmarco-mMiniLMv2-L12-H384-v1)
- [Sentence-BERT paper — ACL Anthology](https://aclanthology.org/D19-1410/)
- [Multilingual sentence embeddings paper — ACL Anthology](https://aclanthology.org/2020.emnlp-main.365/)

## FAISS والتقييم

- [FAISS official repository](https://github.com/facebookresearch/faiss)
- [FAISS metric and cosine guidance](https://github.com/facebookresearch/faiss/wiki/MetricType-and-distances)
- [FAISS CPU 1.15.0 on PyPI](https://pypi.org/project/faiss-cpu/1.15.0/)
- [FAISS research paper](https://arxiv.org/abs/1702.08734)
- [scikit-learn F1 score documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)
- [scikit-learn resampling utility](https://scikit-learn.org/stable/modules/generated/sklearn.utils.resample.html)

## حدود الاستخدام

- Model cards تصف التدريب والاستخدام المقصود؛ لا تضمن جودة على بياناتك.
- dialect labels في عينة الدورة مصطنعة/يدوية وليست مخرجات model.
- أي مقارنة جودة أو latency في مشروع المتدرب تحتاج التشغيل والبيئة والبيانات والنسخ.
- راجع الترخيص عند استبدال أي checkpoint أو dataset.
