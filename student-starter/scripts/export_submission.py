#!/usr/bin/env python3
"""Export allowlisted learner files. Does not capture an open Colab tab or upload files."""
from __future__ import annotations
import argparse, hashlib, json, zipfile
from pathlib import Path
from preflight_submission import review
ROOT_FILES={'README.md','STUDENT_PROFILE.md','PROGRESS.md','DECISIONS.md','BENCHMARKS.md','EVALUATION_REPORT.md','MODEL_CARD.md','DATA_CARD.md','PRESENTATION.md','PROJECT_SUMMARY.json','SUBMISSION.yml','.gitignore'}
DIRS={'notebooks','src','tests','reports','sample_outputs','scripts','data','presentation'}
SUFFIXES={'.md','.py','.ipynb','.json','.jsonl','.yml','.yaml','.csv','.txt','.png','.jpg','.jpeg','.pdf','.pptx'}
SKIP={'.git','__pycache__','.pytest_cache','.ipynb_checkpoints','artifacts','checkpoints','cache','secrets','credentials'}
def export(root: Path, output: Path):
    root=root.resolve();output=output.resolve()
    if output.is_relative_to(root): raise ValueError('Place the ZIP outside the project directory')
    result=review(root)
    if result['status']!='PASS': raise ValueError('Preflight failed. Fix before export: '+'; '.join(result['errors'][:6]))
    paths=[]
    for p in root.rglob('*'):
        if p.is_symlink(): raise ValueError('Symlinks are not permitted in a submission export')
        if not p.is_file():continue
        rel=p.relative_to(root)
        if set(rel.parts)&SKIP:continue
        if p.stat().st_size>10*1024*1024:raise ValueError('Course file limit exceeded: '+str(rel))
        if len(rel.parts)==1:
            allowed=rel.name in ROOT_FILES or (rel.name.startswith('requirements') and p.suffix=='.txt')
        else:allowed=rel.parts[0] in DIRS and p.suffix.lower() in SUFFIXES
        if allowed: paths.append(p)
    output.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(paths):z.write(p,p.relative_to(root).as_posix())
    print('BAYAN_EXPORT_CREATED',str(output))
    print('FILES',len(paths),'SHA256',hashlib.sha256(output.read_bytes()).hexdigest())
    print('Review every output for private data before uploading. This tool does not establish privacy or grade.')
    return paths
if __name__=='__main__':
    a=argparse.ArgumentParser(description=__doc__);a.add_argument('project');a.add_argument('--output',required=True)
    v=a.parse_args()
    try:export(Path(v.project),Path(v.output))
    except (OSError,ValueError) as e:a.exit(1,str(e)+'\n')
