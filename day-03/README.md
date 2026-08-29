# اليوم الثالث — العربية، البحث، والحقيقة
# Day 3 — Arabic, Search, and Truth

**إعداد وتقديم | Prepared and delivered by:** ميعاد المري · Meaad Al-Marri  
**الوقت:** 08:30–13:30 · **البيئة:** Google Colab Free + GitHub

> **السؤال المحوري:** كيف نبني بحثًا دلاليًا عربيًا/إنجليزيًا، ثم نثبت بصدق أين ينجح وأين يضعف؟
>
> **Driving question:** How do we build bilingual semantic search and produce evidence that shows both strengths and weaknesses?

## قبل البدء | Entry gate

يجب أن تكون [بوابة اليوم الثاني Gate B](../day-02/05-labs-checkpoint.md) مكتملة:

- معالجة النص موثقة ولا تحتوي بيانات حقيقية.
- تقسيم البيانات بلا تداخل `group_id`.
- مسارات classification وNER وQA تعمل.
- نتائج العينة موسومة `MEASURED_SMOKE`.
- التقدم محفوظ في مستودع GitHub العام للمتدرب.

إذا لم تكتمل، استخدم نقطة الاستعادة في Gate B ولا تبدأ تنزيل نموذج بحث جديد قبل حفظ اليوم الثاني.

## نواتج اليوم | Outcomes

بنهاية اليوم تستطيع:

1. تفسير أثر الصرف واللواصق والتنوع الإملائي واللهجات وArabizi على NLP العربية.
2. إنشاء نسخة عرض محفوظة ونسخة نموذج مطبّعة باستخدام CAMeL Tools وعقد واضح.
3. تنفيذ مقارنة ضبط دقيق مصغرة بين نموذج متعدد اللغات و`CAMeLBERT-DA` على شريحة خليجية مجمدة.
4. تمييز sentence embedding عن token embedding وعن مخرجات مصنف اليوم الثاني.
5. بناء فهرس `FAISS IndexFlatIP` بعد L2 normalisation على جانبي البحث.
6. تنفيذ بحث دلالي ثنائي اللغة بمشفّر جمل متعدد اللغات ثم إعادة ترتيب المرشحين بـcross-encoder.
7. قياس `Recall@k` و`MRR@k` وفرق الجودة/الزمن وضبط no-answer threshold على validation فقط.
8. إنشاء sliced evaluation مع bootstrap confidence intervals.
9. تحويل الأخطاء إلى taxonomy وإصلاحات مرتبة وتقرير مشروع.
10. إكمال Gate C وربط الأدلة في GitHub.

## قاموس اليوم | Day glossary

[افتح قاموس اليوم الثالث](GLOSSARY.md) واتركه في تبويب مستقل. يغطي صرف العربية واللهجات وArabizi وCAMeL Tools وSentence Embeddings وFAISS وRecall/MRR والتقييم بالشرائح وتحليل الأخطاء، مع النطق والتعريف الإنجليزي والشرح العربي ومثال لكل مصطلح. يمكن الرجوع كذلك إلى [قاموس الدورة الكامل](../docs/glossary/README.md).

## جدول اليوم | Schedule

| الوقت | الجلسة | الناتج المرئي |
|---|---|---|
| 08:30–09:20 | Lab 4: [العربية وCAMeL Tools](01-arabic-nlp-camel-tools.md) + [Notebook 05](../notebooks/05_arabic_nlp.ipynb) | profile + golden tests + مقارنة نموذجين |
| 09:20–09:30 | استراحة | حفظ أول نقطة تقدم |
| 09:30–10:20 | [البحث الدلالي](02-semantic-search.md) | bi-encoder/CE + embedding → FAISS → ranking |
| 10:20–10:30 | استراحة | إبقاء runtime مفتوحًا |
| 10:30–11:20 | Lab 5: [Notebook 06](../notebooks/06_semantic_search.ipynb) | bilingual retrieval + reranking + Recall/MRR |
| 11:20–11:30 | استراحة | حفظ manifest وmetrics |
| 11:30–12:20 | [التقييم وتحليل الأخطاء](03-evaluation-error-analysis.md) | metrics + slices + CI + taxonomy |
| 12:20–12:40 | استراحة طويلة/صلاة | حفظ Drive وتحرير الذاكرة إن لزم |
| 12:40–13:20 | Lab 6: [Notebook 07](../notebooks/07_evaluation_error_analysis.ipynb) | sliced report + behavioural tests + fixes |
| 13:20–13:30 | [Gate C](04-labs-checkpoint.md) | تقارير + commits + exit ticket |

**نافذة PA‑1:** يستغرق [التقييم العملي الأول](../assessments/pa-01/README.md) 30 دقيقة. يعلن المنظم إن كان في ذيل اليوم الثالث أو في نافذة self-paced مراقبة؛ لا يُقتطع من Core بصمت.

إجمالي التعلم 250 دقيقة والاستراحات 50 دقيقة. إذا تأخر تنزيل النموذج، يستمر الصف في Notebook 07 لأنه لا يحتاج checkpoint جديدًا.

## خط بيان اليوم | Today’s Bayan pipeline

```mermaid
flowchart LR
    A["Raw AR/EN text"] --> B["Display copy"]
    A --> C["Protected model copy"]
    C --> D["Sentence encoder"]
    D --> E["L2-normalised vectors"]
    E --> F["FAISS IndexFlatIP"]
    F --> G["Ranked cases"]
    G --> H["Recall/MRR + slices + CI"]
    H --> I["Error taxonomy + decisions"]
```

## كيف ننفذ المقارنة العربية دون تضليل؟

يعيد مختبر 05 ضبط الطبقة الأخيرة ورأس المهمة في نموذج اليوم الثاني متعدد اللغات و`CAMeLBERT-DA`، ويختار epoch من validation ثم يفتح شريحة Gulf المجمدة مرة واحدة. التنفيذ حقيقي، لكن البيانات الاصطناعية صغيرة جدًا؛ لذلك تسمى النتيجة `MEASURED_SMOKE` وتثبت سلامة المنهج فقط، لا تفوقًا عامًا أو إنتاجيًا. إذا تعذر التنزيل أثناء الحصة، تُقرأ النتيجة المحفوظة أولًا ثم يُعاد التشغيل بعد استقرار الشبكة، ولا يُستبدل النموذج بتنبؤات مصطنعة.

## مسارات المستوى | Learning lanes

- 🟢 **Core:** CAMeL Tools + مقارنة عربية مصغرة + multilingual sentence encoder + exact FAISS + cross-encoder على top candidates + metrics + slices. إلزامي، ومختبر مسبقًا على CPU.
- 🔵 **Explore:** تشغيل dialect identifier بعد تنزيل بياناته، أو توسيع مقارنة النماذج والبذور.
- 🟣 **Distinction:** مقارنة Flat مع HNSW، أو Arabizi lane، أو paired bootstrap لمقارنة إصدارين فعليين.

## الموارد والتكلفة | Cost

المسار الإلزامي مجاني ولا يحتاج API key:

- Google Colab Free؛ لا يشترط GPU.
- CAMeL Tools مفتوحة المصدر بترخيص MIT.
- Sentence Transformers والنموذج المختار بترخيص Apache-2.0.
- FAISS CPU مفتوح المصدر.
- GitHub Public للتسليم.

`Colab Pro` وخدمات الاستضافة أو قواعد المتجهات المدفوعة خيارات تشغيلية فقط؛ لا تمنح نقاطًا ولا يحتاجها المشروع.

## قاعدة الصدق العلمي | Evidence rule

بيانات اليوم الثالث اصطناعية وصغيرة. لذلك:

- نتائج البحث والتقييم تسمى `MEASURED_SMOKE`.
- بيانات التنبؤات الجاهزة تسمى `COURSE_FIXTURE`، وليست ناتج نموذج خفي.
- لا توجد قيمة نجاح ثابتة منسوخة في المشروع.
- كل threshold يضبط على validation، ثم يثبت قبل test.
- كل slice صغيرة تظهر بعلامة `SMALL_SLICE` بدل إخفائها.
- CI تعكس عدم اليقين في العينة، ولا تجعل العينة الصغيرة إنتاجية.

## مخرج بيان في نهاية اليوم

عند Gate C يملك كل متدرب:

- profile عربي versioned وموثق ومقارنة fine-tuning مصغرة موسومة بحدودها.
- فهرس بحث بمظهر manifest قابل للمراجعة.
- نتائج bilingual وcross-lingual موثقة.
- Recall@k وMRR@k وفرق re-ranking في الجودة والزمن وقرار no-answer.
- sliced report مع CIs وتحذيرات العينات الصغيرة.
- error taxonomy وثلاثة إصلاحات مرتبة.
- `EVALUATION_REPORT.md` وقرار بحث مضاف إلى `DECISIONS.md`.
- ثلاثة commits عامة تربط Labs 4–6.

## English recap

Day 3 turns Bayan into an evidence-backed bilingual retrieval system. The required path preserves raw text, applies a pinned Arabic profile to a protected model copy, embeds cases with a multilingual Sentence Transformer, indexes unit vectors with FAISS, measures Recall@k and MRR, re-ranks a small candidate set with a multilingual cross-encoder, and reports uncertainty and sliced failures. Cross-encoder tuning, ANN scaling, and full dialect identification remain extensions after Core.
