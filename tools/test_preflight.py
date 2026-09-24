"""Regression tests for v2.1 submission guidance helpers; no ML training."""
import json, runpy, subprocess, sys, zipfile
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'scripts')]
from preflight_submission import review, MARKERS
from export_submission import export
build_base=runpy.run_path(str(ROOT/'tests/test_day4_submission.py'))['build_valid_project']

def fixture(root):
    build_base(root)
    for name,marker in MARKERS.items():
        nb={'cells':[{'cell_type':'code','execution_count':1,'metadata':{},'source':['print("example")'],
                     'outputs':[{'output_type':'stream','name':'stdout','text':[marker]}]}],
            'nbformat':4,'nbformat_minor':5,'metadata':{}}
        (root/'notebooks'/name).write_text(json.dumps(nb))
    readme='SDA-AIE-211 SDAIA Academy https://github.com/SDAIAAcademy #SDAIAAcademy Meaad Al-Marri\n## My contribution\nImplemented a measured extension.\n## AI assistance\nNone.\n'
    for name in MARKERS:readme+=f'https://colab.research.google.com/github/student-one/bayan-nlp-student-one/blob/main/notebooks/{name}\n'
    (root/'README.md').write_text(readme);(root/'PRESENTATION.md').write_text('Problem, architecture, AR/EN demo, quality and performance, limitation and decision.\n')

@pytest.mark.parametrize('case',['valid','source_only','error_output','unexecuted','missing_credit','missing_presentation','template_presentation','wrong_own_link','unsafe_extension','bad_json'])
def test_preflight_cases(tmp_path,case):
    fixture(tmp_path);p=tmp_path/'notebooks/01_text_processing_tokenization.ipynb';nb=json.loads(p.read_text())
    if case=='source_only':nb['cells'][0]['source']=[MARKERS[p.name]];nb['cells'][0]['outputs']=[];p.write_text(json.dumps(nb))
    elif case=='error_output':nb['cells'][0]['outputs'].append({'output_type':'error','ename':'RuntimeError','evalue':'failed','traceback':[]});p.write_text(json.dumps(nb))
    elif case=='unexecuted':nb['cells'][0]['execution_count']=None;p.write_text(json.dumps(nb))
    elif case=='missing_credit':(tmp_path/'README.md').write_text('No credits')
    elif case=='missing_presentation':(tmp_path/'PRESENTATION.md').unlink()
    elif case=='template_presentation':(tmp_path/'PRESENTATION.md').write_text('FILL_ME')
    elif case=='wrong_own_link':p2=tmp_path/'README.md';p2.write_text(p2.read_text().replace('github/student-one/','github/another/'))
    elif case=='unsafe_extension':p2=tmp_path/'PROJECT_SUMMARY.json';x=json.loads(p2.read_text());x['extension']['evidence']='../outside.md';p2.write_text(json.dumps(x))
    elif case=='bad_json':p.write_text('{malformed')
    r=review(tmp_path)
    assert (r['status']=='PASS')==(case=='valid'),r
    assert any('not a grade' in x for x in r['warnings'])

def test_tag_is_exact_and_dirty_code_fails(tmp_path):
    fixture(tmp_path)
    def git(*args):return subprocess.run(['git','-C',str(tmp_path),*args],check=True,capture_output=True,text=True)
    git('init');git('config','user.name','Test');git('config','user.email','test@example.invalid');git('add','.');git('commit','-m','ready');git('tag','submission-v1.0')
    assert review(tmp_path,True)['status']=='PASS'
    (tmp_path/'BENCHMARKS.md').write_text('Changed after freeze')
    assert review(tmp_path,True)['status']=='FAIL'
    git('add','.');git('commit','-m','later version')
    assert any('tag does not point' in x for x in review(tmp_path,True)['errors'])

def test_export_allowlist_and_no_working_tree_mutation(tmp_path):
    root=tmp_path/'project';root.mkdir();fixture(root)
    (root/'unknown.txt').write_text('not allowed')
    before={p.relative_to(root):p.read_bytes() for p in root.rglob('*') if p.is_file()}
    archive=tmp_path/'export.zip';export(root,archive)
    with zipfile.ZipFile(archive) as z:
        assert 'unknown.txt' not in z.namelist();assert 'PRESENTATION.md' in z.namelist()
        assert not any(n.startswith('/') or '..' in Path(n).parts for n in z.namelist())
    assert before=={p.relative_to(root):p.read_bytes() for p in root.rglob('*') if p.is_file()}
    with pytest.raises(ValueError):export(root,root/'bad.zip')

def test_secret_artifact_blocks_export(tmp_path):
    root=tmp_path/'project';root.mkdir();fixture(root);(root/'.env').write_text('KEY=hidden')
    with pytest.raises(ValueError):export(root,tmp_path/'export.zip')
