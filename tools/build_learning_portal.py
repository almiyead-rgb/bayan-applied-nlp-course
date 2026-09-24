#!/usr/bin/env python3
"""Build an offline-capable, source-backed Bayan learner portal; never mutate lessons."""
from __future__ import annotations
import argparse, hashlib, json, posixpath, re
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
import bleach
from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
SOURCE_GLOBS = ('README.md', 'START_HERE.md', 'COURSE_GUIDE.md',
                'day-0[1-4]/**/*.md', 'docs/**/*.md', 'assessments/**/*.md', 'data/DATA_CARD.md')
EXCLUDED = {'private', 'solutions', 'answer_keys', 'instructor', 'trainer', 'archives'}
TAGS = {'p','a','strong','em','s','del','blockquote','ul','ol','li','hr','br','h1','h2','h3','h4','h5','h6',
        'table','thead','tbody','tfoot','tr','th','td','pre','code','div','span','details','summary','img','sup','sub','kbd'}
ATTR = {'*':['lang','dir','class','id','title'], 'a':['href'], 'img':['src','alt','width','height'],
        'td':['colspan','rowspan','align'],'th':['colspan','rowspan','align'],'ol':['start'],'details':['open']}

def source_paths() -> list[Path]:
    found = {p for pattern in SOURCE_GLOBS for p in ROOT.glob(pattern) if p.is_file()}
    return sorted(p for p in found if not (set(p.relative_to(ROOT).parts) & EXCLUDED))

def load_course() -> dict:
    c = json.loads((ROOT/'portal/course.json').read_text(encoding='utf-8'))
    assert c['instruction_minutes'] == 300 and c['lab_minutes'] == 60
    assert len(c['days']) == 4 and sum(c['assessment_weights']) == 100
    assert [d['id'] for d in c['days']] == [1,2,3,4]
    assert set(o for d in c['days'] for o in d['outcomes']) == {f'LO{i}' for i in range(1,7)}
    for d in c['days']:
        assert len(d['hours']) == 5 and sum(x[0] for x in d['lab_plan']) == 60
        for f in d['lessons'] + d['datasets'] + [d['gate']] + ['notebooks/'+n for n in d['notebooks']]:
            if not (ROOT/f).is_file(): raise FileNotFoundError(f'Missing course source: {f}')
    return c

def route(path: str, anchor: str = '') -> str:
    return '#read/' + quote(path, safe='') + ('?anchor='+quote(anchor,safe='') if anchor else '')

def slug(text: str) -> str:
    return re.sub(r'[^\w\-\s]', '', text.lower(), flags=re.UNICODE).strip().replace(' ', '-')

def convert(path: Path, known: set[str], c: dict) -> dict:
    rel = path.relative_to(ROOT).as_posix()
    raw = path.read_text(encoding='utf-8')
    rendered = MarkdownIt('commonmark', {'html':True}).enable(['table','strikethrough']).render(raw)
    html = bleach.clean(rendered, tags=TAGS, attributes=ATTR, protocols={'http','https','mailto'}, strip=True)
    soup = BeautifulSoup(html, 'html.parser')
    headings, used = [], {}
    for h in soup.find_all(re.compile('^h[1-6]$')):
        text = h.get_text(' ',strip=True); base=slug(text) or 'section'
        suffix = used.get(base,0); used[base]=suffix+1
        h['id'] = base + (f'-{suffix}' if suffix else '')
        if h.name in {'h2','h3'}: headings.append({'id':h['id'],'text':text,'level':int(h.name[1])})
    for a in soup.find_all('a',href=True):
        href = a['href']; parts=urlsplit(href)
        if parts.scheme or parts.netloc:
            if parts.scheme not in {'http','https','mailto'}: del a['href']; continue
            if parts.scheme in {'http','https'}: a['target']='_blank'; a['rel']='noopener noreferrer'
            continue
        if not parts.path:
            a['href']=route(rel,unquote(parts.fragment)); continue
        target=posixpath.normpath(posixpath.join(posixpath.dirname(rel),unquote(parts.path)))
        if target.startswith('../') or target.startswith('/'):
            a['href']=c['repository']; continue
        if target in known:
            a['href']=route(target,unquote(parts.fragment))
        else:
            a['href']=c['repository']+'/blob/main/'+quote(target,safe='/')+('#'+quote(unquote(parts.fragment),safe='') if parts.fragment else '')
            a['target']='_blank'; a['rel']='noopener noreferrer'
    for img in soup.find_all('img',src=True):
        src=img['src']; parts=urlsplit(src)
        if not parts.scheme and not parts.netloc:
            target=posixpath.normpath(posixpath.join(posixpath.dirname(rel),unquote(parts.path)))
            img['src']=c['repository'].replace('https://github.com/','https://raw.githubusercontent.com/')+'/main/'+quote(target,safe='/')
        img['loading']='lazy'
    for cell in soup.find_all(['td','th']):
        if not cell.has_attr('dir'): cell['dir']='auto'
    for table in soup.find_all('table'):
        wrap=soup.new_tag('div',attrs={'class':'table-wrap'});table.wrap(wrap)
    for code in soup.select('code.language-mermaid'):
        tip=soup.new_tag('p',attrs={'class':'diagram-note'})
        link=soup.new_tag('a',href=c['repository']+'/blob/main/'+quote(rel,safe='/'),target='_blank',rel='noopener noreferrer')
        link.string='View the rendered diagram on GitHub · شاهد المخطط المرئي في GitHub'
        tip.append(link);code.parent.insert_before(tip)
    first=soup.find('h1')
    return {'path':rel, 'title':first.get_text(' ',strip=True) if first else path.stem,
            'html':str(soup), 'headings':headings, 'search':soup.get_text(' ',strip=True),
            'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}

def build(out: Path) -> dict:
    c=load_course();paths=source_paths();known={p.relative_to(ROOT).as_posix() for p in paths}
    docs=[convert(p,known,c) for p in paths]
    data=json.dumps({'course':c,'documents':docs},ensure_ascii=False,separators=(',',':')).replace('<','\\u003c').replace('\u2028','\\u2028').replace('\u2029','\\u2029')
    template=(ROOT/'portal/template.html').read_text(encoding='utf-8')
    replacements={'/*PORTAL_CSS*/':(ROOT/'portal/styles.css').read_text(), '/*PORTAL_DATA*/':data,
                  '/*PORTAL_JS*/':(ROOT/'portal/app.js').read_text()}
    for marker,text in replacements.items():
        if template.count(marker)!=1: raise ValueError(f'Template marker: {marker}')
        template=template.replace(marker,text)
    out.mkdir(parents=True,exist_ok=True)
    (out/'index.html').write_text(template,encoding='utf-8');(out/'.nojekyll').touch()
    manifest={'course':c['id'],'version':c['version'],'baseline':c['baseline'],
              'learning_minutes':4*(c['instruction_minutes']+c['lab_minutes']),
              'source_count':len(docs),'sources':{d['path']:d['sha256'] for d in docs},
              'notebooks':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'notebooks').glob('*.ipynb'))}}
    (out/'source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'result':'PORTAL_BUILD_PASS','documents':len(docs),'notebooks':len(manifest['notebooks']),'output':str(out)},ensure_ascii=False))
    return manifest

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--out',type=Path,default=ROOT/'_site')
    build(parser.parse_args().out)
