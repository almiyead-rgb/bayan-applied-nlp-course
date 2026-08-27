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
}
COPY_DIRECTORIES = ("notebooks", "src", "tests", "data", "assessments")
COPY_FILES = (
    "requirements-day1.txt",
    "requirements-day2.txt",
    "requirements-day3.txt",
    "requirements-day4.txt",
)

GETTING_STARTED = """# ابدأ مشروع بيان | Start your Bayan repository

هذه الحزمة هي نقطة بدء المتدرب الرسمية لبرنامج `SDA-AIE-211`.

1. فك الضغط وارفع **محتويات** المجلد إلى مستودع GitHub عام باسم `bayan-nlp-YOUR-GITHUB-USERNAME`.
2. استبدل كل `FILL_ME` و`TODO` و`YOUR_USERNAME` في ملفات الجذر.
3. افتح الدفاتر بالترتيب `00` إلى `08`. تحتوي النسخ على نتائج مرجعية محفوظة؛ نفّذ خلاياك واحفظ نتائجك أنت قبل التسليم.
4. شغّل `PYTHONPATH=src python -m pytest -q`.
5. شغّل `PYTHONPATH=src python scripts/validate_submission.py .` قبل إنشاء الوسم النهائي.

ملاحظة: `assessments/pa-01/starter_buggy.py` معطوب **عن قصد**؛ أمر PA‑1 يبدأ بثلاث حالات FAIL ثم يصل إلى PASS بعد إصلاحك. لا يدخل هذا السيناريو في أمر pytest العام.

المصدر العام الكامل والتعليمات المحدثة:
https://github.com/almiyead-rgb/bayan-applied-nlp-course

لا ترفع أوزان النماذج أو مفاتيح API أو بيانات أشخاص. استخدم بيانات الدورة الاصطناعية فقط.
"""

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
    shutil.copy2(ROOT / "scripts" / "validate_submission.py", scripts_directory)
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
