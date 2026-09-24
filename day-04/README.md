# اليوم الرابع — قِس، حسّن، اختبر، وسلّم
# Day 4 — Measure, Optimise, Test, and Ship

**إعداد وتقديم | Prepared and delivered by:** ميعاد المري · Meaad Al-Marri  
**المسار:** رحلة تعلم تطبيقية · **البيئة:** Google Colab Free + GitHub

> **السؤال المحوري:** كيف نحوّل نموذجًا يعمل في notebook إلى مسار استدلال مقاس، وخدمة مختبرة، ومشروع يستطيع مراجع جديد إعادة تشغيله؟
>
> **Driving question:** How do we turn a working notebook into measured inference, a tested service, and a reproducible submission?

## قبل البدء | Entry gate

يجب أن تكون [بوابة اليوم الثالث Gate C](../day-03/04-labs-checkpoint.md) مكتملة:

- معالجة العربية والبحث الدلالي يعملان على بيانات بيان الاصطناعية.
- Recall/MRR وtask metrics موثقة بالوسم الصحيح.
- `EVALUATION_REPORT.md` و`MODEL_CARD.md` يحتويان نتائج وحدودًا فعلية.
- error analysis أُجري على validation لا frozen test.
- تقدم الأيام الثلاثة محفوظ في مستودع GitHub العام.

إذا لم تكتمل، استخدم نقطة الاستعادة في Gate C. لا تجعل التكميم يخفي نقصًا في صحة المهمة.

## نواتج اليوم | Outcomes

بنهاية اليوم تستطيع:

1. تعريف latency وp50/p95/p99 وthroughput وRSS observed peak دون خلط بينها.
2. كتابة performance budget **قبل** تجربة البدائل.
3. تنفيذ benchmark منضبط له warm-up و30 تكرارًا على الأقل وبيئة موثقة.
4. تقليل الحشو باستخدام measured length وdynamic padding وbatching مناسب.
5. تصدير نموذج Transformer إلى ONNX والتحقق من numerical/prediction parity.
6. تجربة dynamic INT8 وقياس السرعة والحجم وquality tax بدل افتراض التحسن.
7. بناء عقد FastAPI واختباره داخل Colab عبر `TestClient` وحالات canary.
8. تمييز `SYSTEMS_SMOKE` عن قياس `PROJECT_ARTIFACT` النهائي.
9. اجتياز Gate D ثم فاحص Gate E وإنشاء tag التسليم.
10. عرض مشروع بيان وشرح رقم واحد موثوق وخطأ واحد معروف.

## قاموس اليوم | Day glossary

[افتح قاموس اليوم الرابع](GLOSSARY.md) واتركه في تبويب مستقل. يغطي Benchmark وLatency وThroughput وONNX وINT8 وParity وFastAPI وCanaries وGit والتسليم، مع النطق والتعريف الإنجليزي والشرح العربي ومثال لكل مصطلح. يمكن الرجوع كذلك إلى [قاموس الدورة الكامل](../docs/glossary/README.md).

## رحلة اليوم | Learning journey

| English topic | الموضوع والشرح بالعربية |
|---|---|
| **Benchmark before changing** — Define the workload and performance budget; separate warm-up and record device, repetitions, latency, throughput and observed memory. | **القياس قبل التغيير** — نحدد عبء العمل وميزانية الأداء، ونفصل الإحماء ونسجل الجهاز والتكرارات والزمن ومعدل المعالجة والذاكرة المرصودة. |
| **ONNX and INT8** — Export, check numerical or prediction parity, and measure the quality and speed cost of quantisation. Keep a rollback path. | **ONNX وINT8** — نصدّر النموذج ونفحص التكافؤ العددي أو التنبؤي، ثم نقيس أثر التكميم على الجودة والسرعة مع الاحتفاظ بمسار تراجع. |
| **API contract and canaries** — Connect project components through the documented service interface and test valid Arabic/English input, rejected input and preprocessing consistency. | **عقد الخدمة والاختبارات الحارسة** — نربط المكونات بواجهة الخدمة الموثقة، ونختبر طلبًا عربيًا وإنجليزيًا ومدخلًا مرفوضًا واتساق المعالجة مع النموذج. |
| **Integration and measured extension** — Assemble previous lab outputs, evaluate the actual project artifact and measure one bounded extension against a baseline. | **التكامل والامتداد المقاس** — نجمع مخرجات اللابات السابقة ونقيّم ناتج المشروع الفعلي ونقيس امتدادًا محدودًا واحدًا مقارنة بخط أساس. لا نبدأ مشروعًا جديدًا. |
| **Evidence, presentation and submission** — Trace every number to a report, explain one limitation, practise the individual demo and validate the exact commit you will submit once. | **الأدلة والعرض والتسليم** — نربط كل رقم بتقرير، ونشرح قيدًا معروفًا، ونتدرب على العرض الفردي ونفحص نسخة الـCommit التي سنرسلها مرة واحدة. |

**Architecture:** Actual project artifact → Benchmark → ONNX / INT8 → Parity + quality + API tests → Evidence → release

**المسار المعماري:** ناتج المشروع الفعلي ← قياس ← ONNX / INT8 ← تكافؤ + جودة + اختبارات الخدمة ← أدلة ← إصدار التسليم

**الدليل:** قياس المشروع + خدمة مختبرة + تقارير + فاحص ناجح + submission-v1.0

[المشروع وهيكله](../docs/project-walkthrough.md) · [التشغيل والحفظ خطوة بخطوة](../docs/learner-workflow.md) · [تقييم 100 درجة](../docs/policies/assessment-and-completion.md)

## خط بيان اليوم | Today’s Bayan delivery path

```mermaid
flowchart LR
    A["FP32 project artifact"] --> B["Frozen workload + budget"]
    B --> C["Warm-up + benchmark"]
    C --> D["Length / padding / batching"]
    D --> E["ONNX FP32"]
    E --> F["Dynamic INT8 candidate"]
    F --> G["Parity + quality tax"]
    G --> H{"Budget met?"}
    H -- "yes" --> I["FastAPI contract + canaries"]
    H -- "no" --> J["Keep FP32 / document decision"]
    I --> K["Validator + demo + tag"]
    J --> K
```

## سياقان لا يجوز خلطهما

| السياق | لماذا يوجد؟ | ما الذي يجوز ادعاؤه؟ | هل يكفي للتسليم النهائي؟ |
|---|---|---|---|
| `SYSTEMS_SMOKE` | تعلّم export وORT وAPI بسرعة على checkpoint صغير | أن المسار التقني يعمل وأن الإصدارين متقاربان عدديًا | لا |
| `PROJECT_ARTIFACT` | قياس نموذج بيان الفعلي وبياناته وعقد معالجته | أداء مشروعك ضمن البيئة والعمل والميزانية الموثقة | نعم، مع بقية الأدلة |

دفتر 08 يبدأ بمسار Systems Smoke مقاوم للتأخير، ثم يوضح موضع تبديل المصدر إلى artefact المشروع. فاحص التسليم النهائي يرفض `benchmark_mode: SYSTEMS_SMOKE`.

## سُلّم القرار | Optimisation ladder

غيّر عاملًا واحدًا ثم أعد القياس على workload نفسه:

1. inference mode وإزالة حساب gradients.
2. قياس الطول واختيار `max_length` مدعوم بالبيانات.
3. dynamic padding ثم length bucketing عند batching.
4. ONNX Runtime على الجهاز المستهدف.
5. dynamic INT8 إذا قبلت الجودة والعتاد النتيجة.
6. نموذج أصغر/مقطّر إذا بقيت الميزانية غير محققة.
7. عتاد أو استضافة مختلفة فقط بعد توثيق ما سبق.

لا يوجد ضمان أن ONNX أو INT8 أسرع على كل جهاز أو batch. النتيجة المقاسة هي التي تحكم.

## مسارات المستوى | Learning lanes

- 🟢 **Core:** Systems Smoke + benchmark صحيح + ONNX + INT8 candidate + TestClient + validator pre-tag.
- 🔵 **Explore:** bucketed batching أو مقارنة batch sizes أو Optimum ONNX مع workload نفسه.
- 🟣 **Distinction:** benchmark متزامن مضبوط، أو مقارنة نموذج distilled، أو drift/startup canary إضافي.

لا تعوّض إضافة متقدمة غياب benchmark المشروع أو التقارير أو tag.

## الموارد والتكلفة | Cost

المسار الإلزامي مجاني ولا يحتاج API key أو استضافة عامة:

- Google Colab Free؛ CPU يكفي لمسار Core، وGPU غير مضمون ولا يشترط.
- PyTorch وTransformers وONNX وONNX Runtime مفتوحة المصدر.
- FastAPI وHTTPX2/TestClient مفتوحة المصدر.
- GitHub Public للتاريخ والتسليم.

الاستضافة الدائمة وColab المدفوع وmanaged endpoints خيارات تشغيلية لاحقة، وليست جزءًا من الاجتياز.

## مخرج بيان في نهاية اليوم

عند Gate E يملك كل متدرب:

- benchmark قبل/بعد ببيئة وworkload ثابتين.
- p50/p95/p99 وthroughput وRSS observed peak وحجم artefact.
- parity check وquality tax وقرار نشر/تراجع معلل.
- خدمة FastAPI مختبرة بطلب عربي وإنجليزي وطلب مرفوض.
- canaries تمنع model/preprocessing skew.
- `BENCHMARKS.md` و`DECISIONS.md` و`PROGRESS.md` مكتملة.
- `PROJECT_SUMMARY.json` و`SUBMISSION.yml` صالحان.
- امتداد مشروع واحد مقاس ومربوط بدليل داخل `PROJECT_SUMMARY.json`.
- فاحص محلي ناجح، مستودع عام، وعلامة `submission-v1.0`.
- عرض موجز يربط كل claim بدليل.

## English recap

Day 4 turns Bayan into a measured, testable delivery artefact. Learners freeze a workload and budget, benchmark with warm-up and tail percentiles, test length/padding/batching, export to ONNX, evaluate a dynamic INT8 candidate, quantify quality tax, test a FastAPI contract with canaries, and validate the final public repository. A systems smoke proves mechanics; only a project-artifact benchmark supports the final submission.
