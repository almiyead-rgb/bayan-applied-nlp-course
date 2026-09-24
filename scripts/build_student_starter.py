#!/usr/bin/env python3
"""Build the browser-downloadable Bayan student starter deterministically."""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import shutil
import zipfile


ROOT = Path(__file__).resolve().parents[1]
STARTER = ROOT / "student-starter"
DOWNLOADS = ROOT / "downloads"
ARCHIVE = DOWNLOADS / "bayan-student-starter.zip"

TEMPLATE_MAP = {
    "PROJECT_README_TEMPLATE.md": "README.md",
    "STUDENT_PROFILE_TEMPLATE.md": "STUDENT_PROFILE.md",
    "PROGRESS_TEMPLATE.md": "PROGRESS.md",
    "DECISIONS_TEMPLATE.md": "DECISIONS.md",
    "BENCHMARKS_TEMPLATE.md": "BENCHMARKS.md",
    "EVALUATION_REPORT_TEMPLATE.md": "EVALUATION_REPORT.md",
    "MODEL_CARD_TEMPLATE.md": "MODEL_CARD.md",
    "DATA_CARD_TEMPLATE.md": "DATA_CARD.md",
    "PROJECT_SUMMARY.template.json": "PROJECT_SUMMARY.json",
    "SUBMISSION.template.yml": "SUBMISSION.yml",
    "DEMO_SCRIPT_TEMPLATE.md": "PRESENTATION.md",
}
COPY_DIRECTORIES = ("notebooks", "src", "tests", "data", "assessments")
COPY_FILES = (
    "requirements-day1.txt",
    "requirements-day2.txt",
    "requirements-day3.txt",
    "requirements-day4.txt",
)

GETTING_STARTED = '# ابدأ مشروع بيان | Start your Bayan repository\n\nحزمة البداية التعليمية لبرنامج SDA-AIE-211 بإعداد ميعاد المري. التقييم 70 تقنية + 20 إدارية + 10 عرض = 100. التصحيح مرة واحدة بعد الإرسال؛ صحح وافحص قبل التسليم.\n\nUse this scaffold for your own work. Save and run your own nine notebooks, upload actual outputs and code, complete the required reports and PRESENTATION.md, then validate your final release. No edited replacement is accepted after hand-in.\n\n1. فك ZIP وارفع محتوياته مع المجلدات إلى مستودعك الشخصي العام على main؛ لا ترفع ZIP فقط.\n2. استبدل حقول القالب في ملفات الجذر بمعلوماتك الفعلية، لا بمخرجات منسوخة.\n3. احفظ نسخك في Drive وشغّل الخلايا بالترتيب، ثم احفظ notebooks/00–08 في GitHub بأسمائها المطلوبة.\n4. احفظ التقارير وتعديلات src/bayan منفصلة؛ حفظ الدفتر لا يحفظ جميع ملفات runtime.\n5. شغّل: PYTHONPATH=src python -m pytest -q tests\n6. شغّل: python scripts/validate_submission.py .\n7. شغّل: python scripts/preflight_submission.py . --report reports/preflight.json\n8. افحص الروابط والخصوصية والعرض، ثم أنشئ submission-v1.0 وأعد الفحص مع --require-tag.\n\nتظهر حزمة البداية فشلًا متوقعًا قبل ملء حقول الطالب. لا تغيّر الفاحص لكي يمر. أنشطة PA تدريبية دون درجة مستقلة؛ كود PA-1 معطوب عمدًا ولا يدخل pytest العام.\n\nFull step-by-step learner guide / الدليل الكامل:\nhttps://github.com/almiyead-rgb/bayan-applied-nlp-course/blob/main/docs/learner-workflow.md\n\nRubric / التقييم:\nhttps://github.com/almiyead-rgb/bayan-applied-nlp-course/blob/main/docs/policies/assessment-and-completion.md\n\nDo not upload model weights, secrets or real personal data. / لا تنشر الأوزان أو الأسرار أو البيانات الشخصية الحقيقية.\n'

GITIGNORE = """# Model and runtime artefacts
*.bin
*.ckpt
*.onnx
*.pt
*.pth
*.safetensors
__pycache__/
.pytest_cache/
.ipynb_checkpoints/
cache/
artifacts/

# Secrets and local environments
.env
.venv/
venv/
credentials.json
service-account.json

# OS/editor files
.DS_Store
Thumbs.db
"""

REPORTS_README = """# Reports

ضع هنا تقارير JSON/CSV/Markdown الصغيرة الناتجة من القياس. لا ترفع أوزان النماذج أو بيانات غير عامة.
"""

SAMPLES_README = """# Sample outputs

ضع هنا عينات مخرجات آمنة بالعربية والإنجليزية لا تحتوي بيانات شخصية أو أسرارًا.
"""


def copy_tree(source: Path, destination: Path) -> None:
    shutil.copytree(
        source,
        destination,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".ipynb_checkpoints"),
    )


def main() -> None:
    if STARTER.exists():
        shutil.rmtree(STARTER)
    STARTER.mkdir(parents=True)

    for source_name, destination_name in TEMPLATE_MAP.items():
        shutil.copy2(ROOT / "templates" / source_name, STARTER / destination_name)
    for directory in COPY_DIRECTORIES:
        copy_tree(ROOT / directory, STARTER / directory)
    for filename in COPY_FILES:
        shutil.copy2(ROOT / filename, STARTER / filename)

    scripts_directory = STARTER / "scripts"
    scripts_directory.mkdir()
    for name in ("validate_submission.py", "preflight_submission.py", "export_submission.py"):
        shutil.copy2(ROOT / "scripts" / name, scripts_directory)
    (STARTER / "reports").mkdir()
    (STARTER / "reports" / "README.md").write_text(REPORTS_README, encoding="utf-8")
    (STARTER / "sample_outputs").mkdir()
    (STARTER / "sample_outputs" / "README.md").write_text(SAMPLES_README, encoding="utf-8")
    (STARTER / "GETTING_STARTED.md").write_text(GETTING_STARTED, encoding="utf-8")
    (STARTER / ".gitignore").write_text(GITIGNORE, encoding="utf-8")

    DOWNLOADS.mkdir(exist_ok=True)
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(STARTER.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(STARTER).as_posix()
            info = zipfile.ZipInfo(relative, date_time=(2026, 8, 27, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    digest = sha256(ARCHIVE.read_bytes()).hexdigest()
    (DOWNLOADS / "SHA256SUMS.txt").write_text(
        f"{digest}  {ARCHIVE.name}\n", encoding="utf-8"
    )
    print(f"Built {ARCHIVE.relative_to(ROOT)} ({ARCHIVE.stat().st_size} bytes)")
    print(f"SHA256 {digest}")


if __name__ == "__main__":
    main()
