# تجميع بيان وعرضه | Assemble and present Bayan

<!-- BAYAN_YOUTUBE_START -->
### شاهد الفكرة ثم طبّقها | Video companions

<div class="card youtube-topic youtube-t24"><h3 class="pair"><span class="en" lang="en" dir="ltr">Connect the NLP pipeline</span><span class="ar" lang="ar" dir="rtl">ربط مسار معالجة اللغة</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Follow preprocessing, model inference and postprocessing; then connect Bayan’s branches.</p><p class="ar" lang="ar" dir="rtl">تتبع المعالجة والاستدلال وتجهيز المخرج ثم اربط فروع بيان.</p></div><p><strong lang="en" dir="ltr">What Happens Inside the Pipeline Function?</strong><br><span class="micro">Hugging Face · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=1pedAIvTWXk" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><div class="callout warning"><div class="pair"><p class="en" lang="en" dir="ltr">One pipeline building block, not the full Bayan architecture. Use the project diagram for the parallel task and search branches.</p><p class="ar" lang="ar" dir="rtl">لبنة واحدة لا معمارية بيان الكاملة. استخدم مخطط المشروع لفروع المهام والبحث.</p></div></div><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">Which components are prepared offline and which run for each request?</p><p class="ar" lang="ar" dir="rtl">أي المكونات تُجهز مسبقًا وأيها يعمل لكل طلب؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<!-- BAYAN_YOUTUBE_END -->

## اربط ما بنيته | Connect your existing work

اربط المعالجة بنماذج الموضوع والمشاعر والكيانات والأسئلة وبالبحث الدلالي. تحقق من الإصدارات والوسوم واتساق المعالجة، ثم افحص الخدمة وسجل القياس الفعلي. لا تبدأ مشروعًا ثانيًا ولا تنسخ SYSTEMS_SMOKE بوصفه قياس المشروع.

Connect preprocessing, topic/sentiment, NER/QA and semantic search. Check versioning and preprocessing consistency, test the service and record actual project measurements. Do not start another project or relabel a systems smoke as final evidence.

## راجع بمساعدة زميل دون نقل ملكية العمل | Peer review without copying

يتتبع الزميل رقمًا إلى تقريره، ويفحص رابط تشغيل وقيدًا معروفًا؛ ويكتب ملاحظة لصاحب المشروع. لا يغير ملفات زميله ولا يعيد استخدام أدلته باسمه. تنجز المراجعة والإصلاح **قبل** الإرسال النهائي.

Ask a peer to trace one metric, open one notebook and read a limitation. Feedback belongs to the project owner; copied work is not individual evidence. Review and repairs happen **before** final hand-in.

## الأدلة | Evidence

| Claim | Evidence |
|---|---|
| Problem, architecture and own links | README.md |
| Data and model boundaries | DATA_CARD.md + MODEL_CARD.md |
| Task/search quality and errors | EVALUATION_REPORT.md + reports/ |
| Speed, memory and quality trade-off | BENCHMARKS.md |
| Decisions and measured extension | DECISIONS.md + PROJECT_SUMMARY.json |
| Demonstration and personal understanding | PRESENTATION.md + individual questions |
| Final version | submission-v1.0 + recorded commit SHA |

## العرض والتسليم | Presentation and submission

العرض **فردي**، حتى خمس شرائح، وخمس دقائق يتبعها دقيقتان للتحقق. نقاطه العشر ضمن التقييم 100. لا تدريب طويل أثناء العرض؛ افتح الأمثلة والتقارير مسبقًا. عند العطل أعلن استخدام نتائج محفوظة من نسختك نفسها.

The presentation is individual: up to five slides, five minutes plus two minutes of verification. Its ten points are included in 100. Prepare examples and evidence beforehand; label any saved fallback honestly.

[السيناريو والمعمارية](../docs/project-walkthrough.md) · [متطلبات العرض ونقاطه](../docs/presentation-guide.md) · [قائمة الفحص النهائي](../docs/pre-submission-checklist.md) · [سياسة التصحيح مرة واحدة](../docs/policies/submission.md)
