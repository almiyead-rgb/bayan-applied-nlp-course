# قبل أن ترسل: افحص ثم ثبّت النسخة | Check before your one final hand-in

**هذه مراجعة ذاتية وليست درجة آلية. يمكن تكرارها قبل الإرسال؛ وبعد الإرسال تُصحح النسخة المستلمة مرة واحدة دون إعادة تسليم.**

**This is self-review, not automatic grading. Repeat before hand-in; the submitted version is assessed once, with no replacement after sending.**

| Check | English | العربية |
|---|---|---|
| T1–T2 | I ran preprocessing/Arabic and attention notebooks and can explain profile, tokenizer, masks and shapes. | شغلت دفاتر المعالجة والعربية والانتباه وأستطيع شرح المعالجة والترميز والأقنعة والأبعاد. |
| T3 | Topic, sentiment, NER and QA work; the split is grouped and no-answer/label-alignment tests are recorded. | تعمل مهام الموضوع والمشاعر والكيانات والأسئلة، مع تقسيم مجموعات وفحوص عدم الإجابة ومحاذاة الوسوم. |
| T4 | Search uses sentence embeddings, FAISS and measured re-ranking, with bilingual examples and Recall/MRR. | يستخدم البحث تضمينات الجمل وFAISS وإعادة ترتيب مقاسة مع أمثلة ثنائية ومقاييس Recall/MRR. |
| T5 | Metrics link to my reports; slices, uncertainty, an error taxonomy and three fixes are documented. | ترتبط المقاييس بتقاريري، مع توثيق الشرائح وعدم اليقين وتصنيف الأخطاء وثلاثة إصلاحات. |
| T6 | I measured my actual PROJECT_ARTIFACT, tested parity/quality and the API; I did not relabel SYSTEMS_SMOKE. | قست PROJECT_ARTIFACT الفعلي وفحصت التكافؤ والجودة والخدمة، ولم أعد تسمية SYSTEMS_SMOKE. |
| T7 | One original-scope extension has an implementation, baseline, measured benefit/cost and evidence link. | لامتداد واحد ضمن النطاق تنفيذ وخط أساس وفائدة وتكلفة مقاسة ورابط دليل. |
| A1–A2 | My own repository is accessible; README has the architecture, own Colab links, results and Academy/trainer attribution. | مستودعي الشخصي متاح، ويتضمن README المعمارية وروابط Colab الشخصية والنتائج ونسب الأكاديمية والمدربة. |
| A3 | All required root files, notebooks, reports and PRESENTATION.md exist; placeholders are replaced with real facts. | جميع ملفات الجذر والدفاتر والتقارير وPRESENTATION.md موجودة، وحقول القالب مستبدلة بمعلومات فعلية. |
| A4–A5 | My contribution and assistance are disclosed, progress is traceable, and the final release/SHA are ready. | مساهمتي والمساعدة معلنتان، والتقدم قابل للتتبع، والإصدار النهائي وSHA جاهزان. |
| P1–P5 | I practised the individual five-part demo and can answer a question or explain a small changed input. | تدربت على العرض الفردي بأقسامه الخمسة وأستطيع الإجابة أو تفسير تغيير صغير في المدخل. |
| Technical checks | Unit tests, the base validator and preflight pass; output markers occur in executed outputs, not source alone. | نجحت اختبارات الوحدات والفاحص الأساسي والفحص المسبق؛ وتظهر علامات النجاح في مخرجات التنفيذ لا في المصدر وحده. |
| Privacy | I inspected notebook outputs, report files and repository history for secrets/personal data; weights and caches stay private. | راجعت مخرجات الدفاتر والتقارير والتاريخ للتأكد من غياب الأسرار والبيانات الشخصية؛ والأوزان والذاكرة المؤقتة خاصة. |
| Fresh reader | A private browser window opens README, notebook links, evidence and the release without extra permissions. | تفتح نافذة خاصة README وروابط الدفاتر والأدلة والإصدار دون طلب صلاحيات إضافية. |
| Freeze | The submitted tag resolves to the exact final commit I declared; I will not move the tag or send replacement files. | يشير الوسم المرسل إلى Commit النهائي الذي أعلنته؛ ولن أنقل الوسم أو أرسل ملفات بديلة. |

<!-- BAYAN_YOUTUBE_START -->
### شاهد الفكرة ثم طبّقها | Video companions

<div class="card youtube-topic youtube-t25"><h3 class="pair"><span class="en" lang="en" dir="ltr">Verify and freeze your submission</span><span class="ar" lang="ar" dir="rtl">تحقق وثبّت نسخة التسليم</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Revisit Colab when needed, then see how a release records a version.</p><p class="ar" lang="ar" dir="rtl">راجع Colab عند الحاجة ثم شاهد كيف يثبت الإصدار نسخة العمل.</p></div><p><strong lang="en" dir="ltr">Getting Started with GitHub Releases</strong><br><span class="micro">Tugdual Grall · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=Gw2vB18X3sQ" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><details><summary>شرح إضافي عند الحاجة · More explanation when needed</summary><p><strong lang="en" dir="ltr">Colab 101: Your Ultimate Beginner’s Guide!</strong><br><span class="micro">Sam Witteveen · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=Ii6gs9zADEA" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p></details><div class="callout warning"><div class="pair"><p class="en" lang="en" dir="ltr">Only release/versioning basics. Maven/Packages/Actions demonstrations are not assignments. Run Bayan’s validators and follow its one-shot policy.</p><p class="ar" lang="ar" dir="rtl">أساسيات الإصدار والنسخ فقط؛ أمثلة Maven وPackages وActions ليست تكليفات. شغّل فواحـص بيان واتبع سياسة التصحيح الواحد.</p></div></div><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">Which commit SHA is graded after your one final submission?</p><p class="ar" lang="ar" dir="rtl">أي بصمة Commit تُصحح بعد إرسالك النهائي الواحد؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<!-- BAYAN_YOUTUBE_END -->

## ماذا لا تثبته الأدوات؟ | What the tools cannot establish

نجاح الفاحص يثبت الفحوص المحددة فقط، ولا يثبت تلقائيًا أصالة العمل أو صحة جميع المقاييس أو أهلية الشهادة. الفحص المحلي لا يرى صلاحيات الروابط العامة. لا يكفي تأشير القائمة أو كتابة `tests_passed: true` دون تنفيذ حقيقي.

The checker only establishes its stated checks. It does not establish authorship, every scientific metric, public-link access or certification. The browser checklist is not sent to the instructor.

[خطوات التشغيل والتصدير](learner-workflow.md) · [سياسة الإرسال](policies/submission.md) · [التقييم](policies/assessment-and-completion.md)
