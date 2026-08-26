# مصفوفة الأهداف والأدلة | Outcomes-to-Evidence Map

هذه المصفوفة تمنع وجود شرح بلا تطبيق أو تطبيق بلا تقييم. كل هدف رسمي مرتبط بدرس، مختبر، مخرج في مشروع **بيان**، ودليل داخل مستودع المتدرب.

| # | الهدف | اليوم/الوحدة | التطبيق الإلزامي | مخرج بيان | دليل الاجتياز |
|---:|---|---|---|---|---|
| 1 | معالجة النصوص والترميز، ومنها العربية | يوم 1: M1؛ [يوم 3: M4](../day-03/01-arabic-nlp-camel-tools.md) | Unicode، regex، masking، tokenizer fertility، normalisation profiles | `src/bayan/preprocessing.py` + `arabic_profiles.py` | اختبارات ذهبية + قرار tokenizer/profile |
| 2 | شرح الانتباه والمحولات | يوم 1: M2 | حساب attention صغير وتتبع shapes وencoder block | notebook يشرح forward pass | assert مكافأة + تفسير مصفوفة الانتباه |
| 3 | Fine-tuning للتصنيف وNER وQA | [يوم 2: M3](../day-02/README.md) | baseline ثم نموذج BERT-family؛ label alignment؛ null answer | `03_text_classification.ipynb` + `04_ner_and_qa.ipynb` | metrics موسومة + zero leakage + اختبارات alignment/no-answer |
| 4 | البحث الدلالي بالتضمينات | [يوم 3: M5](../day-03/02-semantic-search.md) | bi-encoder، cosine، FAISS، retrieve ثم re-rank اختياري | bilingual case search | Recall@k وMRR + اختبار cross-lingual |
| 5 | التقييم وتحليل الأخطاء | [يوم 3: M6](../day-03/03-evaluation-error-analysis.md) | task metrics، slices، CIs، behavioural tests، taxonomy | `EVALUATION_REPORT.md` وmodel cards | نتائج قابلة لإعادة الإنتاج + 3 إصلاحات مرتبة |
| 6 | تحسين الاستدلال والذاكرة | [يوم 4: M7](../day-04/README.md) | batching/length، ONNX، INT8 حيث يدعم، benchmark منضبط | optimized serving path | latency/memory/quality tax قبل وبعد |
| 7 | مشروع عربي/إنجليزي مكتمل | [الأيام 1–4](../day-04/04-capstone-assembly-demo.md) | تجميع المكونات، API، README، demo | مستودع Bayan عام | [validator + rubric + tag](../day-04/05-lab-gates-submission.md) `submission-v1.0` |

## التدرّج حسب المستوى | Level differentiation

| المسار | ما ينجزه | معيار النجاح |
|---|---|---|
| 🟢 أساسي | خلايا TODO المحددة، البيانات المصغرة، نموذج صغير، تقارير القالب | جميع الأدلة الإلزامية تعمل وتُشرح |
| 🔵 استكشاف | مقارنة نموذجين/مخططين، slice إضافي، re-ranking أو tuning | قرار تقني مدعوم بقياس |
| 🟣 تميّز | Arabizi، drift، ANN scale، أو cross-encoder مضبوط | إضافة مستقلة لا تكسر المسار الأساسي |

## تغطية القياس | Assessment coverage

| مكوّن التقييم | LO1 | LO2 | LO3 | LO4 | LO5 | LO6 | LO7 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| المختبرات 35% | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| العملي 15% | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |
| الاختبار 10% | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| المشروع 40% | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |

> لا يُعد الهدف مغطى لمجرد ذكره في الشرائح؛ يجب أن ينتج عنه **سلوك قابل للملاحظة ودليل قابل للفحص**.  
> An outcome is not covered merely because it appears on a slide; it needs observable performance and inspectable evidence.
