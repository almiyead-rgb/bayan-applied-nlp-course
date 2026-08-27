# الأدوات المجانية والخيارات | Free Tools and Options

## القرار الأساسي

كل ما يلزم للاجتياز متاح بلا اشتراك مدفوع. إذا ظهر خيار مدفوع في الشرح فهو للمقارنة المهنية فقط، وليس خطوة مطلوبة.

| الحاجة | الأداة الأساسية المجانية | لماذا؟ | خيار مدفوع/بديل | هل يلزم؟ |
|---|---|---|---|---|
| تشغيل Python | Google Colab Free | لا تثبيت محلي، مناسب للصف | Colab paid / cloud VM | لا |
| حفظ notebooks/checkpoints | Google Drive المجاني | متكامل مع Colab | تخزين سحابي إضافي | لا |
| التسليم والتاريخ | GitHub Public | commits وREADME وtag | GitHub paid/private | لا؛ العام إلزامي |
| نماذج ومكتبات | Hugging Face open-source stack | Transformers/Datasets/Evaluate | Inference APIs | لا |
| معالجة العربية | CAMeL Tools | أدوات عربية مفتوحة | خدمات تجارية | لا |
| ML كلاسيكي | scikit-learn | baselines وmetrics | منصات AutoML | لا |
| NER metrics | seqeval | entity-level evaluation | منصة تقييم | لا |
| البحث الدلالي | sentence-transformers + FAISS CPU | embeddings وفهرسة محلية | vector database managed | لا |
| التحسين | ONNX Runtime/Optimum | export وCPU inference | خدمة optimisation | لا |
| API | FastAPI + TestClient | اختبار داخل Colab | hosting دائم | لا |
| الاختبارات | pytest | مجاني وقابل للأتمتة | منصات QA | لا |
| الرسوم | pandas + matplotlib/seaborn | تقارير قابلة للتكرار | BI مدفوع | لا |

## Colab Free مقابل الخيارات المدفوعة

| السؤال | المجاني | المدفوع |
|---|---|---|
| هل يكفي للمسار الأساسي؟ | نعم، مع reduced path | نعم |
| هل GPU مضمون؟ | لا | ليس ضمانًا مطلقًا؛ يعتمد على الخطة والتوفر |
| هل الجلسة دائمة؟ | لا | لا تعاملها كتخزين دائم |
| هل يمنح compute أكثر؟ | محدود وديناميكي | قد يمنح compute units/خيارات أكثر |
| هل يؤثر على الدرجة؟ | لا | لا |

المصدر: [Google Colab FAQ](https://research.google.com/colaboratory/faq.html).

## لماذا لا نستخدم API مدفوعة؟

لأن أهداف البرنامج هي فهم وبناء وتقييم خط NLP قابل لإعادة الإنتاج. API الخارجية قد تخفي tokenizer/model/version وتضيف تكلفة ومفتاحًا سريًا، بينما يستطيع المسار المحلي المفتوح إثبات المهارة المطلوبة.

## ما الذي يمكن تثبيته لاحقًا محليًا؟

للمتدرب المختص فقط، بعد نجاح Colab:

- Python virtual environment.
- VS Code.
- Git CLI.
- Docker.
- local ONNX service.

هذه خيارات تطوير مهنية وليست متطلبات صفية، ولن تعتمد تعليمات Core عليها.

## قاعدة اختيار أداة

اسأل أربعة أسئلة:

1. هل تحقق هدفًا رسميًا؟
2. هل تعمل مجانًا على Colab/CPU؟
3. هل يمكن قياس مخرجها؟
4. هل نستطيع إعادة إنتاج النتيجة دون secret أو حساب إضافي؟

إذا كانت الإجابة “لا” على أحدها، فالأداة ليست جزءًا إلزاميًا.

## إصدارات اليوم الثالث | Day 3 versions

يستخدم المختبر ملف [`requirements-day3.txt`](../../requirements-day3.txt) المثبت والمراجع في 27 أغسطس 2026. المسار الإلزامي لا يحتاج token أو API أو قاعدة متجهات خارجية. model weights تُنزّل إلى runtime المؤقت ولا تُرفع إلى GitHub.

- CAMeL Tools utilities فقط في Core؛ حزم بيانات dialect الكبيرة Explore.
- Sentence Transformer متعدد اللغات + FAISS CPU في Core.
- Cross-encoder متعدد اللغات على top candidates جزء Core مقاس؛ أما استبداله/ضبطه وقاعدة vector database مُدارة فخيارات لاحقة لا تعوض الأدلة الإلزامية.

## إصدارات اليوم الرابع | Day 4 versions

يستخدم [مختبر اليوم الرابع](../../notebooks/08_optimization_serving.ipynb) ملف [`requirements-day4.txt`](../../requirements-day4.txt)، المراجع في 27 أغسطس 2026:

- ONNX وONNX Runtime CPU للتصدير والاستدلال والتكميم المحلي.
- FastAPI وHTTPX2/TestClient لاختبار HTTP داخل Colab بلا استضافة.
- psutil لقياس RSS observed peak بوصفه قياسًا تقريبيًا.
- Transformers مع checkpoint صغير في `SYSTEMS_SMOKE`، ثم artefact المشروع في Gate D.

`optimum-onnx` خيار Explore رسمي، لكنه ليس مطلوبًا للمسار الأساسي. لا تحتاج managed endpoint أو tunnel أو قاعدة بيانات مدفوعة، ولا تمنح الاستضافة العامة نقاطًا إضافية. راجع [مراجع اليوم الرابع](../../day-04/REFERENCES.md).
