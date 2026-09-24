# من أول خلية إلى تسليمك | From your first cell to your submission

## 1. افهم الأداتين | Understand the two workspaces

| Term | English | العربية |
|---|---|---|
| Colab notebook | An `.ipynb` document with explanation cells, Python cells and saved outputs. | ملف `.ipynb` يجمع خلايا الشرح والكود والمخرجات المحفوظة. |
| Runtime | A temporary machine that runs the code. Saving the notebook does not save every runtime file or model weight. | جهاز مؤقت يشغل الكود. حفظ الدفتر لا يحفظ تلقائيًا جميع ملفات الجلسة أو أوزان النموذج. |
| GitHub repository | The folder-like home for code, documents, evidence and version history. It does not execute your notebook merely because you uploaded it. | مستودع للكود والوثائق والأدلة وتاريخ النسخ. رفع الدفتر إليه لا يشغله تلقائيًا. |
| README.md | The front page explaining the project and how to reproduce it. | الصفحة التعريفية التي تشرح المشروع وكيف يعاد تشغيله. |
| Commit | A recorded change with an identifier. | تغيير محفوظ له معرّف يمكن الرجوع إليه. |
| Tag / Release | A tag points to a Git version; a release presents it with a title and notes. | يشير الوسم إلى نسخة في Git، ويعرض الإصدار هذه النسخة مع عنوان وملاحظات. |

[مرجع Colab الرسمي](https://research.google.com/colaboratory/faq.html) · [README في GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

## 2. أنشئ مستودعك الشخصي | Create your own repository

<!-- BAYAN_YOUTUBE_STEP_2 -->
<div class="card youtube-topic youtube-t02"><h3 class="pair"><span class="en" lang="en" dir="ltr">Your repository and README</span><span class="ar" lang="ar" dir="rtl">مستودعك وملف README</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Create your own repository and recognise the role of README and gitignore.</p><p class="ar" lang="ar" dir="rtl">أنشئ مستودعك وافهم دور README وملف gitignore.</p></div><p><strong lang="en" dir="ltr">GitHub for Beginners #1: Create Your First Repository</strong><br><span class="micro">Ben Day · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=5A9oLJRLVl4" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">Where will your own notebook, code and evidence be stored?</p><p class="ar" lang="ar" dir="rtl">أين ستحفظ دفترك وكودك وأدلتك الشخصية؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<!-- /BAYAN_YOUTUBE_STEP_2 -->

| Step | English | العربية |
|---|---|---|
| 1 | Sign in to your own GitHub account, open **New repository** and select your account as owner. | ادخل حسابك في GitHub وافتح **New repository** واختر حسابك مالكًا. |
| 2 | Name it `bayan-nlp-YOUR_USERNAME`, replacing the example with your GitHub username. Add a short description. | سمّه `bayan-nlp-YOUR_USERNAME` مع استبدال الجزء الأخير باسم مستخدمك، وأضف وصفًا مختصرًا. |
| 3 | Choose **Public**, enable **Add README** and select **Create repository**. Do not enter private personal information in public fields. | اختر **Public** وفعّل **Add README** ثم **Create repository**. لا تدخل بيانات شخصية خاصة في الحقول العامة. |
| 4 | Download the [student starter](../downloads/bayan-student-starter.zip), extract it, then use **Add file → Upload files** to upload its **contents**, keeping folders. Do not upload only the ZIP or the course website. | نزّل [حزمة البداية](../downloads/bayan-student-starter.zip) وفكها ثم استخدم **Add file → Upload files** وارفع **المحتويات** مع المجلدات. لا ترفع ZIP فقط أو موقع الدورة بدل المشروع. |
| 5 | Confirm `README.md`, `src/bayan`, `notebooks`, `tests`, `reports` and `scripts` are at the expected level, not inside an extra wrapper directory. Include the supplied `.gitignore`. | تحقق من أن الملفات والمجلدات في المستوى الصحيح وليست داخل مجلد تغليف إضافي، وأن `.gitignore` المرفق موجود. |
| 6 | Save with a clear **Commit changes** message. Select `main` consistently in links and submission metadata. | احفظ عبر **Commit changes** برسالة واضحة، واستخدم `main` باستمرار في الروابط وبيانات التسليم. |

[إنشاء المستودع — GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) · [رفع الملفات — GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)

## 3. افتح نسختك في Colab وشغّلها | Open and run your Colab copy

<!-- BAYAN_YOUTUBE_STEP_3 -->
<div class="card youtube-topic youtube-t01"><h3 class="pair"><span class="en" lang="en" dir="ltr">Colab essentials</span><span class="ar" lang="ar" dir="rtl">أساسيات Colab</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">See cells, runtime and outputs before your first lab.</p><p class="ar" lang="ar" dir="rtl">شاهد الخلايا وبيئة التشغيل والمخرجات قبل أول لاب.</p></div><p><strong lang="en" dir="ltr">Get started with Google Colaboratory</strong><br><span class="micro">TensorFlow · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=inN8seMm7UI" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">What is saved in a notebook, and what lives only in the runtime?</p><p class="ar" lang="ar" dir="rtl">ما الذي يُحفظ في الدفتر، وما الذي يوجد في الجلسة المؤقتة فقط؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<!-- /BAYAN_YOUTUBE_STEP_3 -->

| Step | English | العربية |
|---|---|---|
| 1 | Open the assigned notebook. Choose **File → Save a copy in Drive** before editing; verify it is your saved copy. Keep the required notebook filename for GitHub. | افتح الدفتر المطلوب ثم **File → Save a copy in Drive** قبل التعديل؛ تحقق أنها نسختك المحفوظة. حافظ على اسم الدفتر المطلوب عند حفظه في GitHub. |
| 2 | Read the first markdown cells and prerequisites. Run **00 Runtime Doctor** first; follow the documented CPU path when no GPU is available. | اقرأ خلايا الشرح الأولى والمتطلبات. شغّل **00 Runtime Doctor** أولًا واتبع مسار CPU الموثق عند عدم توفر GPU. |
| 3 | A **Text/Markdown cell** explains; a **Code cell** runs with ▶ or **Shift+Enter**. Its output appears beneath it. | خلية **Text/Markdown** للشرح؛ وخلية **Code** للتنفيذ بزر ▶ أو **Shift+Enter**. يظهر الناتج أسفلها. |
| 4 | Run cells top to bottom: setup → imports → data → processing/model → evaluation → save/checkpoint. Do not skip a failed cell. | نفّذ من الأعلى للأسفل: الإعداد ثم الاستيراد فالبيانات فالمعالجة والنموذج فالتقييم فالحفظ والفحص. لا تتجاوز خلية فاشلة. |
| 5 | Complete your required work, add your own explained decisions and inspect your actual outputs. A provided reference output is not your run. | أكمل عملك المطلوب وأضف قراراتك المفسّرة وافحص نتائجك الفعلية. النتيجة المرجعية المرفقة ليست تشغيلك. |
| 6 | Before final evidence, save private model artifacts and reports, then restart the session and use **Runtime → Run all**. Menu wording can vary slightly. | قبل الدليل النهائي احفظ الأوزان الخاصة والتقارير، ثم أعد تشغيل الجلسة واختر **Runtime → Run all**. قد تختلف صياغة القوائم قليلًا. |
| 7 | Review every error, output and end-of-notebook marker. Keep required outputs in the saved notebook; do not enable the setting that omits outputs on save. | راجع كل خطأ ومخرج وعلامة نهاية الدفتر. أبقِ المخرجات المطلوبة في الدفتر المحفوظ؛ لا تفعّل حذف المخرجات عند الحفظ. |

توضح [وثائق Colab](https://research.google.com/colaboratory/faq.html) أن ملفات الجهاز المؤقت لا تُشارك تلقائيًا مع الدفتر، وأن موارد المجاني متغيرة. احتفظ بالتقارير والأوزان الخاصة اللازمة قبل إنهاء الجلسة. لترحيل نموذج اليوم الثاني إلى اليوم الرابع اتبع [دليل حفظ النموذج](setup/colab.md)، ولا ترفع وزنه علنًا.

The notebook and runtime files are different things. Preserve your reports and private project model before ending the runtime. Follow the [model handoff guide](setup/colab.md) for Day 2 → Day 4.

## 4. احفظ دفاترك والكود والمخرجات | Save notebooks, code and outputs

<!-- BAYAN_YOUTUBE_STEP_4 -->
<div class="card youtube-topic youtube-t03"><h3 class="pair"><span class="en" lang="en" dir="ltr">Save your own Colab work</span><span class="ar" lang="ar" dir="rtl">حفظ عملك الشخصي في Colab</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Use this walkthrough when making and saving your own copy.</p><p class="ar" lang="ar" dir="rtl">استعن بالشرح عند إنشاء نسختك الشخصية وحفظها.</p></div><p><strong lang="en" dir="ltr">Colab 101: Your Ultimate Beginner’s Guide!</strong><br><span class="micro">Sam Witteveen · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=Ii6gs9zADEA" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><div class="callout warning"><div class="pair"><p class="en" lang="en" dir="ltr">Colab orientation, not the complete Bayan export procedure. Follow the linked learner guide for separate code and report files.</p><p class="ar" lang="ar" dir="rtl">مدخل لاستخدام Colab، وليس شرحًا كاملًا لتصدير بيان. اتبع دليل المتدرب لحفظ ملفات الكود والتقارير المنفصلة.</p></div></div><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">Does saving the notebook upload all generated reports to GitHub?</p><p class="ar" lang="ar" dir="rtl">هل حفظ الدفتر يرفع تلقائيًا جميع التقارير إلى GitHub؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<!-- /BAYAN_YOUTUBE_STEP_4 -->

| Step | English | العربية |
|---|---|---|
| 1 | After your run, choose **File → Save a copy in GitHub**, authorize only the official dialog, choose your own repository and `main`. | بعد تشغيلك اختر **File → Save a copy in GitHub**، وامنح الصلاحية من النافذة الرسمية فقط، ثم اختر مستودعك و`main`. |
| 2 | Set the exact path, for example `notebooks/03_text_classification.ipynb`, write a meaningful commit message, then verify the saved outputs on GitHub. | حدد المسار بدقة مثل `notebooks/03_text_classification.ipynb`، واكتب رسالة Commit مفهومة، ثم تحقق من المخرجات المحفوظة في GitHub. |
| 3 | If direct saving fails, use **File → Download → Download .ipynb**, then upload it to the same `notebooks/` path in your repository. | إذا تعذر الحفظ المباشر، استخدم **File → Download → Download .ipynb** ثم ارفعه إلى مساره نفسه داخل `notebooks/` في مستودعك. |
| 4 | An optional `.py` export is not a substitute: it does not preserve the notebook's outputs and markdown structure. | تصدير `.py` اختياري وليس بديلًا؛ فهو لا يحفظ مخرجات الدفتر وهيكل خلايا الشرح. |
| 5 | Save actual `src/bayan` changes and small generated report/sample files separately. Notebook saving does **not** automatically upload these runtime files. | احفظ تعديلات `src/bayan` وملفات التقارير والعينات الصغيرة بصورة منفصلة؛ حفظ الدفتر لا يرفع ملفات الجلسة هذه تلقائيًا. |
| 6 | Review exported files, then upload them with folders intact. Keep weights, secrets and caches outside the public repository. | راجع الملفات المصدّرة ثم ارفعها مع المحافظة على المجلدات. اترك الأوزان والأسرار وملفات cache خارج المستودع العام. |

[تكامل Colab وGitHub — دفتر Google الرسمي](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)

## 5. جهّز README ووسم الأكاديمية | README and Academy attribution

افتح `README.md` واضغط رمز القلم، ثم عدّل **قالب الطالب** بمعلومات مشروعك الفعلية. استبدل حقول القالب في الملفات المطلوبة؛ لا تغيّر الكلمات التقنية داخل كود المكتبات لمجرد أنها تشبه حقلًا فارغًا.

Edit the student README with the pencil icon. Replace template fields with real project facts, not fabricated metrics. The required sections are the problem, scope, architecture, own Colab links, results and evidence, reproduction, known limits, personal contribution, assistance disclosure and acknowledgements.

ضع كتلة النسب التالية كما هي، ثم أضف مساهمتك بصورة منفصلة. لا تعني هذه الكتلة أن المشروع معتمد أو مملوك للأكاديمية:

```markdown
## Training context | السياق التدريبي
This educational project was developed during Applied Natural Language Processing
with Transformers (SDA-AIE-211) in the SDAIA Academy training context.
أُنجز هذا المشروع التعليمي ضمن دورة معالجة اللغات الطبيعية باستخدام المحولات
(SDA-AIE-211) في السياق التدريبي لأكاديمية سدايا.

Academy | الأكاديمية: [SDAIA Academy](https://github.com/SDAIAAcademy)
Trainer | المدربة: Meaad Al-Marri — ميعاد المري
Course source | مصدر الدورة: https://github.com/almiyead-rgb/bayan-applied-nlp-course
#SDAIAAcademy

## My contribution | مساهمتي
Describe your own change, file, decision and measured evidence.
اشرح تغييرك الشخصي ومسار الملف والقرار والدليل المقاس.

## AI assistance | الاستعانة بالأدوات
State the tool, assistance and how you verified it—or honestly state none.
اذكر الأداة ونوع المساعدة وكيف راجعتها، أو اذكر بصدق أنك لم تستخدمها.
```

**الفرق بين الوسوم:** `#SDAIAAcademy` عبارة نسب في النص، ورابط الأكاديمية رابط إلى حسابها، أما `submission-v1.0` فهو **Git tag لنسخة المشروع**. هذه ليست الأشياء نفسها. إضافة نجمة أو متابعة حساب ليست شرطًا للدرجة.

**Different markers:** `#SDAIAAcademy` is a text attribution hashtag; the Academy URL is an organisation link; `submission-v1.0` is a Git version tag. Stars/follows are not grading requirements. The public [SDAIA Academy account](https://github.com/SDAIAAcademy) is linked for attribution, not an endorsement of a particular student submission.

## 6. افحص نسخة GitHub في Colab | Validate the uploaded repository

افتح **دفتر Colab جديدًا للفحص** وشغّل الخلية التالية. أدخل رابط مستودعك، لا رابط المدربة. تُنشئ الخلية نسخة جديدة للفحص ولا تدفع أي تعديل إلى GitHub. هذه فحوص هيكل وأدلة واختبارات وحدات؛ **لا تعيد تدريب النماذج ولا تتحقق من صحة كل رقم علمي**.

Open a separate Colab notebook and run the cell below. Supply your repository URL. It clones a fresh copy for review without writing to GitHub. These structural, saved-evidence and unit tests do not retrain models or establish every scientific claim.

```python
from pathlib import Path
import os, re, subprocess, sys, tempfile

repo_url = input("Your GitHub repository URL / رابط مستودعك: ").strip().rstrip("/")
if not re.fullmatch(r"https://github\.com/[A-Za-z0-9_-]+/[A-Za-z0-9_.-]+", repo_url):
    raise ValueError("Enter the repository URL, not a file/Colab/local path.")
if repo_url == "https://github.com/almiyead-rgb/bayan-applied-nlp-course":
    raise ValueError("Use your own learner repository, not the course repository.")
PROJECT = Path(tempfile.mkdtemp(prefix="learner-review-")) / "project"
subprocess.run(["git", "clone", "--branch", "main", repo_url, str(PROJECT)], check=True)
subprocess.run([sys.executable, "-m", "pip", "install", "numpy", "pytest"], check=True)
env = dict(os.environ, PYTHONPATH=str(PROJECT / "src"))
subprocess.run([sys.executable, "-m", "pytest", "-q", "tests"], cwd=PROJECT, env=env, check=True)
subprocess.run([sys.executable, "scripts/validate_submission.py", ".",
                "--json-report", "reports/submission_validation.json"],
               cwd=PROJECT, env=env, check=True)
subprocess.run([sys.executable, "scripts/preflight_submission.py", ".",
                "--report", "reports/preflight.json"], cwd=PROJECT, env=env, check=True)
print("PRE_SUBMISSION_CHECKS_PASSED — inspect reports and rubric before hand-in.")
```

إذا ظهرت `FAIL` فاقرأ **أول ERROR**، أصلح ملفك الأصلي، واحفظه في GitHub، ثم أعد خلية الفحص قبل التسليم. لا تغيّر الفاحص أو تكتب PASS يدويًا. مجرد فتح صفحة GitHub لا يعيد الحساب.

On failure, fix the original file, save it to GitHub and repeat the clean review **before hand-in**. Do not weaken tests or fabricate PASS outputs.

### حفظ تقارير الفحص | Save the validation reports

في دفتر الفحص نفسه، نزّل التقريرين ثم ارفعهما إلى `reports/` في مستودعك **قبل** إنشاء الوسم النهائي:

```python
from google.colab import files
files.download(str(PROJECT / "reports/submission_validation.json"))
files.download(str(PROJECT / "reports/preflight.json"))
```

التقرير يسجل نسخة المصدر التي فُحصت. بعد رفع التقارير لا تغير الكود أو الأدلة العلمية؛ ثم أنشئ الإصدار وأعد فحص الوسم. رفع التقرير بحد ذاته يصنع Commit جديدًا، ولذلك لا تنسخ SHA أقدم بوصفه نسخة التسليم.

The report records the reviewed source revision. Uploading a report creates another commit; use the actual final commit for hand-in, not a stale SHA. Recheck the tag after publishing.

## 7. صدّر مجلد المشروع بأمان عند الحاجة | Export the project folder when needed

احفظ أولًا الدفاتر في GitHub أو ضع نسخ `.ipynb` المنزلة داخل مجلد المشروع الذي ستصدره. مساعد التصدير **لا يقرأ تلقائيًا الدفتر المفتوح في المتصفح ولا يجمع ملفات Drive كلها**. يختار ملفات المشروع المسموحة فقط ويوقف التصدير عند فشل الفحص؛ ومع ذلك يجب مراجعة الملفات يدويًا قبل نشرها.

First save or place the actual `.ipynb` files inside the project you will export. The helper does not capture the browser notebook or scan your entire Drive. It exports allowlisted project files after preflight; manual privacy review remains required.

```python
# PROJECT must point to the project containing your latest notebooks/code/reports.
from pathlib import Path
from google.colab import files
import subprocess, sys
out = Path("/content/learner-submission.zip")
subprocess.run([sys.executable, str(PROJECT / "scripts/export_submission.py"),
                str(PROJECT), "--output", str(out)], check=True)
files.download(str(out))
```

استخدم نسخة `PROJECT` أعلاه فقط عندما تكون **أحدث نسخة رفعتها بالفعل**. إذا كان عملك أحدث في مجلد آخر فحدد ذلك المجلد بدلًا منها. فك ZIP وارفع محتوياته، لا ZIP وحده. تحقق من أن `README.md` ظاهر في جذر المستودع.

## 8. بوابة الإرسال النهائي | Final hand-in gate

<!-- BAYAN_YOUTUBE_STEP_8 -->
<div class="card youtube-topic youtube-t25"><h3 class="pair"><span class="en" lang="en" dir="ltr">Verify and freeze your submission</span><span class="ar" lang="ar" dir="rtl">تحقق وثبّت نسخة التسليم</span></h3><div class="pair"><p class="en" lang="en" dir="ltr">Revisit Colab when needed, then see how a release records a version.</p><p class="ar" lang="ar" dir="rtl">راجع Colab عند الحاجة ثم شاهد كيف يثبت الإصدار نسخة العمل.</p></div><p><strong lang="en" dir="ltr">Getting Started with GitHub Releases</strong><br><span class="micro">Tugdual Grall · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=Gw2vB18X3sQ" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p><details><summary>شرح إضافي عند الحاجة · More explanation when needed</summary><p><strong lang="en" dir="ltr">Colab 101: Your Ultimate Beginner’s Guide!</strong><br><span class="micro">Sam Witteveen · English audio / الصوت بالإنجليزية</span></p><p><a class="button primary" href="https://www.youtube.com/watch?v=Ii6gs9zADEA" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p></details><div class="callout warning"><div class="pair"><p class="en" lang="en" dir="ltr">Only release/versioning basics. Maven/Packages/Actions demonstrations are not assignments. Run Bayan’s validators and follow its one-shot policy.</p><p class="ar" lang="ar" dir="rtl">أساسيات الإصدار والنسخ فقط؛ أمثلة Maven وPackages وActions ليست تكليفات. شغّل فواحـص بيان واتبع سياسة التصحيح الواحد.</p></div></div><details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary><div class="pair"><p class="en" lang="en" dir="ltr">Which commit SHA is graded after your one final submission?</p><p class="ar" lang="ar" dir="rtl">أي بصمة Commit تُصحح بعد إرسالك النهائي الواحد؟</p></div><div class="pair"><p class="en" lang="en" dir="ltr">Self-check, not a graded task.</p><p class="ar" lang="ar" dir="rtl">سؤال للفهم الذاتي، وليس تكليفًا بدرجة.</p></div></details></div>

<!-- /BAYAN_YOUTUBE_STEP_8 -->

راجع [قائمة ما قبل التسليم](pre-submission-checklist.md) و[سلم 100 درجة](policies/assessment-and-completion.md) و[العرض](presentation-guide.md). أنشئ `submission-v1.0` وأرسل رابط المستودع ورابط الإصدار وSHA النهائي بالطريقة الخاصة التي تحددها المدربة. **التصحيح مرة واحدة؛ لا تقبل نسخة معدلة بعد الإرسال.**


### إنشاء الإصدار ثم نسخ SHA النهائي في Colab | Release and final SHA in Colab

| Step | English | العربية |
|---|---|---|
| 1 | Finish every fix, upload the validation reports, then open your repository's **Releases → Draft a new release**. | أكمل الإصلاحات وارفع تقارير الفحص، ثم افتح **Releases → Draft a new release** في مستودعك. |
| 2 | Select **Choose a tag**, enter `submission-v1.0`, choose **Create new tag** and set the target to `main`. | اختر **Choose a tag** واكتب `submission-v1.0` ثم **Create new tag**، واجعل الهدف `main`. |
| 3 | Use the title **Bayan NLP Final Submission**, add a brief description and publish. Copy the release URL; this alone does not send it to the instructor. | اكتب عنوان **Bayan NLP Final Submission** ووصفًا مختصرًا وانشر. انسخ رابط الإصدار؛ نشره لا يرسله إلى المدربة تلقائيًا. |
| 4 | In the separate validation notebook, run the Python cell below after the earlier validation cell. It reads a fresh clone, checks the tag and prints the exact SHA to submit. | في دفتر الفحص المنفصل شغّل خلية Python التالية بعد خلية الفحص السابقة. تقرأ نسخة جديدة وتفحص الوسم وتطبع SHA المطلوب إرساله. |

```python
# Continue in the validation notebook from step 6; repo_url is your own URL.
FINAL = Path(tempfile.mkdtemp(prefix="learner-final-")) / "project"
subprocess.run(["git", "clone", "--branch", "main", repo_url, str(FINAL)], check=True)
final_env = dict(os.environ, PYTHONPATH=str(FINAL / "src"))
subprocess.run([sys.executable, "scripts/preflight_submission.py", ".", "--require-tag"],
               cwd=FINAL, env=final_env, check=True)
sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=FINAL, text=True).strip()
print("FINAL_COMMIT_SHA:", sha)
print("Commit URL:", repo_url + "/commit/" + sha)
print("Release URL:", repo_url + "/releases/tag/submission-v1.0")
print("Review the rubric and send these links yourself through the announced hand-in channel.")
```

لا تعدّل الكود أو تنقل الوسم بعد الإرسال النهائي. هذه الخلية لا ترسل المشروع ولا تمنح درجة ولا تقفل GitHub؛ دورها التحقق من نسخة التسليم وبيان بصمتها.

Do not change the submitted code or move the tag after hand-in. This cell does not submit, grade or lock GitHub; it identifies and checks your final revision.

[إدارة الإصدارات — GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
