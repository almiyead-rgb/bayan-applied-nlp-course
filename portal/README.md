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

## Preservation | الحفاظ على المحتوى

The update preserves lesson bodies, the nine notebooks, datasets, executable NLP source, technical tests, starter ZIP and assessment thresholds. Delivery-only documentation now uses 300 explanation minutes and 60 dedicated lab minutes per day. Assessment windows and breaks are explicitly outside the 24 net learning hours. See the [delivery plan](../docs/04-delivery-plan.md).

يحافظ التحديث على الدروس والدفاتر التسعة والبيانات والكود العلمي والاختبارات التقنية وحزمة البداية وحدود التقييم. يستخدم تنظيم التنفيذ 300 دقيقة شرح و60 دقيقة لاب يوميًا، وتُعلن نوافذ التقييم والاستراحات خارج 24 ساعة تعلم صافية. راجع [خطة التنفيذ](../docs/04-delivery-plan.md).

Portal acceptance tests do not rerun ML training. A hosted-Colab clean-account rehearsal and lab duration measurement remain operational checks before teaching. No new accreditation or production-readiness claim is made.

لا تعيد اختبارات الواجهة تدريب النماذج. تبقى تجربة Colab المستضافة بحساب نظيف وقياس مدة اللاب فحصين تشغيليين قبل التدريس. لا يدّعي التحديث اعتمادًا جديدًا أو جاهزية إنتاجية.
