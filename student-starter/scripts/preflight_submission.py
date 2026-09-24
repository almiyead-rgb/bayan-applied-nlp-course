#!/usr/bin/env python3
"""Evidence preflight; not an automatic grade, model rerun or plagiarism verdict."""
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from bayan.submission import validate_project, REQUIRED_NOTEBOOKS, REQUIRED_MARKERS

MARKERS = dict(REQUIRED_MARKERS, **{'00_runtime_doctor.ipynb': 'BAYAN_ENV_READY = True'})
PLACEHOLDER = re.compile(r'\b(?:FILL_ME|YOUR_USERNAME|TODO|TBD|REPLACE_ME)\b', re.I)

def text(value):
    return ''.join(value) if isinstance(value, list) else str(value or '')

def review(root: Path, require_tag: bool = False) -> dict:
    root = root.resolve(); errors = []; warnings = []; checks = []
    try:
        base = validate_project(root, require_git_tag=require_tag)
        errors.extend(base.errors); warnings.extend(base.warnings); checks.extend(base.checks)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        errors.append(f'Base validation could not complete: {type(exc).__name__}: {exc}')
    hashes = {}; executed = 0
    for name in REQUIRED_NOTEBOOKS:
        path = root / 'notebooks' / name
        if not path.is_file(): continue
        try:
            raw = path.read_bytes(); hashes[name] = hashlib.sha256(raw).hexdigest()
            nb = json.loads(raw); code = [c for c in nb.get('cells', []) if c.get('cell_type') == 'code' and text(c.get('source')).strip()]
            if not code: errors.append(f'{name}: no code cells'); continue
            captured = []
            for i, cell in enumerate(code, 1):
                count = cell.get('execution_count')
                if not isinstance(count, int) or isinstance(count, bool) or count < 1:
                    errors.append(f'{name}: code cell {i} has no saved execution count')
                else: executed += 1
                for out in cell.get('outputs', []):
                    if out.get('output_type') == 'error': errors.append(f'{name}: saved error in code cell {i}')
                    captured.append(text(out.get('text')))
                    captured.append(text(out.get('data', {}).get('text/plain')))
            if MARKERS[name] not in '\n'.join(captured):
                errors.append(f'{name}: expected marker is absent from executed outputs (source text alone is insufficient)')
        except (OSError, ValueError, TypeError, AttributeError) as exc:
            errors.append(f'{name}: malformed notebook: {exc}')
    checks.append('Checked notebook code cells, saved output markers and errors; did not execute ML')
    readme_path = root / 'README.md'; readme = readme_path.read_text(encoding='utf-8') if readme_path.is_file() else ''
    for token in ['SDA-AIE-211','SDAIA Academy','https://github.com/SDAIAAcademy','#SDAIAAcademy','Meaad Al-Marri']:
        if token not in readme: errors.append(f'README: missing attribution {token}')
    for en, ar in [('My contribution','مساهمتي'),('AI assistance','الاستعانة بالأدوات')]:
        if en.lower() not in readme.lower() and ar not in readme: errors.append(f'README: missing {en} section')
    try:
        summary = json.loads((root / 'PROJECT_SUMMARY.json').read_text())
        repo = str(summary.get('repository_url','')).rstrip('/')
        if repo == 'https://github.com/almiyead-rgb/bayan-applied-nlp-course': errors.append('Use your own repository, not the instructor repository')
        parts = urlsplit(repo).path.strip('/').split('/')
        if len(parts) != 2: raise ValueError('repository_url must identify owner/repository')
        if str(summary.get('student_github','')).casefold() != parts[0].casefold(): errors.append('student_github must match the repository owner')
        for name in REQUIRED_NOTEBOOKS:
            expected = f'https://colab.research.google.com/github/{parts[0]}/{parts[1]}/blob/main/notebooks/{name}'
            if expected not in readme: errors.append(f'README: missing own Colab link for {name}')
        evidence = str(summary.get('extension',{}).get('evidence','')).split('#',1)[0]
        ep = (root / unquote(evidence)).resolve()
        if not evidence or not ep.is_relative_to(root) or not ep.is_file(): errors.append('Measured-extension evidence must resolve to a file inside the repository')
    except (OSError, ValueError, AttributeError) as exc:
        errors.append(f'Cannot verify project identity/evidence: {exc}')
    presentation = root / 'PRESENTATION.md'
    if not presentation.is_file() or not presentation.read_text().strip(): errors.append('PRESENTATION.md is required')
    elif PLACEHOLDER.search(presentation.read_text()): errors.append('PRESENTATION.md still contains placeholders')
    # Broken relative README evidence links are a mechanical check, not content validation.
    for href in re.findall(r'\]\(([^)]+)\)', readme):
        u=urlsplit(href)
        if not u.path or u.scheme or u.netloc: continue
        dest=(root / unquote(u.path)).resolve()
        if not dest.is_relative_to(root) or not dest.exists(): errors.append(f'README: missing/unsafe relative link {href}')
    sha = None
    try:
        sha=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True,stderr=subprocess.DEVNULL,timeout=10).strip()
        if require_tag:
            tag_sha=subprocess.check_output(['git','-C',str(root),'rev-parse','submission-v1.0^{commit}'],text=True,stderr=subprocess.DEVNULL,timeout=10).strip()
            if sha != tag_sha: errors.append('Final tag does not point to the reviewed HEAD')
            changed=subprocess.check_output(['git','-C',str(root),'diff','--name-only','HEAD','--','.',':!reports/preflight.json',':!reports/submission_validation.json'],text=True,timeout=10).strip()
            if changed: errors.append('Tracked files differ from the reviewed commit: '+changed.replace('\n',', '))
    except (OSError, subprocess.SubprocessError):
        if require_tag: errors.append('Cannot verify final Git commit/tag')
        else: warnings.append('No Git metadata; final commit/tag must be checked after upload')
    warnings.extend(['Authorship, scientific accuracy, privacy inside arbitrary text and public access require human review.',
                     'PASS is not a grade, an automatic plagiarism verdict or certification.'])
    return {'status':'FAIL' if errors else 'PASS','policy':'BAYAN-100-v2.1','reviewed_commit':sha,
            'executed_code_cells':executed,'notebook_sha256':hashes,'checks':checks,'errors':errors,'warnings':warnings}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('project',nargs='?',default='.')
    parser.add_argument('--require-tag',action='store_true');parser.add_argument('--report')
    args=parser.parse_args();result=review(Path(args.project),args.require_tag)
    print('BAYAN_PREFLIGHT='+result['status'])
    for error in result['errors']: print('[ERROR]',error)
    for warning in result['warnings']: print('[WARN]',warning)
    if args.report:
        out=Path(args.report);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    return 0 if result['status']=='PASS' else 1
if __name__=='__main__': raise SystemExit(main())
