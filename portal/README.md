# Bayan learner portal | بوابة بيان

The website is an additional navigation and explanation layer over the existing course, not a replacement curriculum. English is on the left and Arabic on the right in paired summaries. Original reference pages retain their original language and full source text.

الموقع طبقة إضافية للتنقل والشرح فوق محتوى الدورة الحالي، وليس منهجًا بديلًا. تعرض الملخصات الإنجليزية يسارًا والعربية يمينًا، وتحتفظ الصفحات المرجعية بالنص الكامل وبلغته الأصلية.

## Build and test | البناء والفحص

```bash
python -m pip install -r portal/requirements.txt
python tools/build_learning_portal.py
node --check portal/app.js
python -m playwright install chromium
python tools/test_learning_portal.py
```

Open `_site/index.html` in a browser. The compiled page contains its styles, scripts and all learner reference pages. External notebooks, downloads and primary sources still require internet access. Personal progress is local to the browser, is not a grade, and is not sent to the instructor.

افتح `_site/index.html` في المتصفح. تتضمن الصفحة المجمعة التنسيق والبرمجة والصفحات المرجعية. يحتاج فتح دفاتر Colab والتنزيلات والمصادر الخارجية إلى الإنترنت. التقدم شخصي ومحلي، وليس درجة ولا يُرسل إلى المدربة.

## Publishing | النشر

The **Bayan learning portal** workflow builds and tests the site and publishes a downloadable artifact. GitHub Pages deployment runs only when the repository's Pages source is configured to **GitHub Actions**. If Pages is not configured, an owner must select **Settings → Pages → Source → GitHub Actions**, then run the workflow. The workflow summary reports the actual deployment state; a successful build alone does not mean the website is live.

تبني آلية **Bayan learning portal** الموقع وتفحصه وتنتج نسخة قابلة للتنزيل. يجري النشر عندما يكون مصدر Pages مضبوطًا على **GitHub Actions**. عند عدم التفعيل، يختار مالك المستودع **Settings → Pages → Source → GitHub Actions** ثم يشغّل الآلية. يعرض ملخص التنفيذ الحالة الفعلية؛ نجاح البناء وحده لا يعني أن الموقع منشور.

## Preservation and scope | الحفظ والنطاق

Scientific notebooks, datasets, shared NLP implementation and existing scientific unit tests are preserved. The instructor-directed v2.1 update changes the assessment and learner guidance: 70 technical +20 administrative +10 presentation =100; one final assessment; narrative day journeys without detailed times. Student templates, validation helpers and the starter ZIP are regenerated consistently.

تبقى الدفاتر العلمية والبيانات والتنفيذ العلمي واختباراته محفوظة. يحدّث الإصدار 2.1 التقييم والإرشادات بتوجيه المدربة: 70 تقنية و20 إدارية و10 عرض =100؛ وتصحيح واحد؛ ورحلة أيام دون تقسيم زمني مفصل. تعاد توليد القوالب والفواحـص الإضافية وحزمة البداية بصورة متسقة.

Portal/preflight tests do not rerun model training or establish authorship. No new accreditation claim is made.
