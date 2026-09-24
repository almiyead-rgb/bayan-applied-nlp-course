# ابدأ مشروع بيان | Start your Bayan repository

حزمة البداية التعليمية لبرنامج SDA-AIE-211 بإعداد ميعاد المري. التقييم 70 تقنية + 20 إدارية + 10 عرض = 100. التصحيح مرة واحدة بعد الإرسال؛ صحح وافحص قبل التسليم.

Use this scaffold for your own work. Save and run your own nine notebooks, upload actual outputs and code, complete the required reports and PRESENTATION.md, then validate your final release. No edited replacement is accepted after hand-in.

1. فك ZIP وارفع محتوياته مع المجلدات إلى مستودعك الشخصي العام على main؛ لا ترفع ZIP فقط.
2. استبدل حقول القالب في ملفات الجذر بمعلوماتك الفعلية، لا بمخرجات منسوخة.
3. احفظ نسخك في Drive وشغّل الخلايا بالترتيب، ثم احفظ notebooks/00–08 في GitHub بأسمائها المطلوبة.
4. احفظ التقارير وتعديلات src/bayan منفصلة؛ حفظ الدفتر لا يحفظ جميع ملفات runtime.
5. شغّل: PYTHONPATH=src python -m pytest -q tests
6. شغّل: python scripts/validate_submission.py .
7. شغّل: python scripts/preflight_submission.py . --report reports/preflight.json
8. افحص الروابط والخصوصية والعرض، ثم أنشئ submission-v1.0 وأعد الفحص مع --require-tag.

تظهر حزمة البداية فشلًا متوقعًا قبل ملء حقول الطالب. لا تغيّر الفاحص لكي يمر. أنشطة PA تدريبية دون درجة مستقلة؛ كود PA-1 معطوب عمدًا ولا يدخل pytest العام.

Full step-by-step learner guide / الدليل الكامل:
https://github.com/almiyead-rgb/bayan-applied-nlp-course/blob/main/docs/learner-workflow.md

Rubric / التقييم:
https://github.com/almiyead-rgb/bayan-applied-nlp-course/blob/main/docs/policies/assessment-and-completion.md

Do not upload model weights, secrets or real personal data. / لا تنشر الأوزان أو الأسرار أو البيانات الشخصية الحقيقية.
