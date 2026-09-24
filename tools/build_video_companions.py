#!/usr/bin/env python3
"""Generate declarative Markdown/HTML YouTube companions; no new frontend JavaScript.

Run --sources before the existing course builder, then --navigation afterward.
Every generated block is bounded and reproducible from portal/videos.json.
"""
from __future__ import annotations
import argparse, hashlib, html, json, re
from pathlib import Path
from urllib.parse import quote
ROOT=Path(__file__).resolve().parents[1]
START='<!-- BAYAN_YOUTUBE_START -->'
END='<!-- BAYAN_YOUTUBE_END -->'
GROUPS=[('start','Before you begin','قبل البدء','docs/youtube-start.md'),
('day-1','Day 1 · Text and attention','اليوم الأول · النص والانتباه','day-01/VIDEOS.md'),
('day-2','Day 2 · Models and tasks','اليوم الثاني · النماذج والمهام','day-02/VIDEOS.md'),
('day-3','Day 3 · Arabic and search','اليوم الثالث · العربية والبحث','day-03/VIDEOS.md'),
('day-4','Day 4 · Optimise and serve','اليوم الرابع · التحسين والخدمة','day-04/VIDEOS.md'),
('project','Project, submission and presentation','المشروع والتسليم والعرض','docs/youtube-project.md')]

def pair(values,tag='p'):
    return f'<div class="pair"><{tag} class="en" lang="en" dir="ltr">{html.escape(values[0])}</{tag}><{tag} class="ar" lang="ar" dir="rtl">{html.escape(values[1])}</{tag}></div>'

def watch(clip,catalog):
    v=catalog['videos'][clip['video']]
    url='https://www.youtube.com/watch?v='+clip['video']
    if clip.get('start'): url+='&t='+str(clip['start'])+'s'
    out=f'<p><strong lang="en" dir="ltr">{html.escape(v["title"])}</strong><br><span class="micro">{html.escape(v["channel"])} · English audio / الصوت بالإنجليزية</span></p>'
    if 'start' in clip:
        stamp=lambda n:f'{n//60:02}:{n%60:02}'
        out+=pair([f'Suggested segment {stamp(clip["start"])}–{stamp(clip["end"])}; stop at the end shown.',f'المقطع المقترح {stamp(clip["start"])}–{stamp(clip["end"])}؛ توقف عند النهاية المحددة.'])
    out+=f'<p><a class="button primary" href="{html.escape(url,quote=True)}" target="_blank" rel="noopener noreferrer">▶ Watch on YouTube · شاهد على YouTube ↗</a></p>'
    return out

def card(t,catalog,full=True):
    out='<div class="card youtube-topic youtube-'+t['id']+'">'+'<h3 class="pair"><span class="en" lang="en" dir="ltr">'+html.escape(t['title'][0])+'</span><span class="ar" lang="ar" dir="rtl">'+html.escape(t['title'][1])+'</span></h3>'+pair(t['purpose'])
    out+=''.join(watch(c,catalog) for c in t['clips'] if c.get('role')!='support')
    extra=[c for c in t['clips'] if c.get('role')=='support']
    if extra: out+='<details><summary>شرح إضافي عند الحاجة · More explanation when needed</summary>'+''.join(watch(c,catalog) for c in extra)+'</details>'
    if t.get('boundary'):out+='<div class="callout warning">'+pair(t['boundary'])+'</div>'
    out+='<details><summary>بعد المشاهدة: اربط الفكرة ببيان · Connect it to Bayan</summary>'+pair(t['question'])+pair(['Self-check, not a graded task.','سؤال للفهم الذاتي، وليس تكليفًا بدرجة.'])+'</details>'
    if full: out+='<p><a class="button" href="'+html.escape('https://github.com/almiyead-rgb/bayan-applied-nlp-course/blob/main/'+t['lessons'][0],quote=True)+'">Course lesson · درس الدورة</a></p>'
    return out+'</div>\n\n'

GUIDANCE=['Choose your current topic, open its YouTube button, then return to your own lab. Watching does not award points or count as lab completion. Use the course code and data, not older video installation commands.',
'اختر موضوعك الحالي واضغط زر YouTube، ثم عد إلى لابك الشخصي. المشاهدة لا تمنح درجات ولا تعني إنجاز اللاب. استخدم كود وبيانات الدورة لا أوامر تثبيت قديمة من الفيديو.']
FOOT=['All playback links open individual YouTube videos in a new tab. There is no embedded player or viewing tracker. Segment links start at the suggested time but do not stop automatically. Shared videos need not be watched twice. Availability and captions may change; use the course lesson if a video cannot open.',
'تفتح أزرار المشاهدة فيديوهات YouTube محددة في تبويب جديد. لا يوجد مشغل مضمّن أو تتبع مشاهدة. يبدأ رابط المقطع من الزمن المقترح ولا يتوقف تلقائيًا. لا يلزم تكرار المقاطع المشتركة. قد تتغير الإتاحة والترجمة؛ ارجع إلى درس الدورة إذا تعذر فتح مقطع.']

def bounded_insert(path,block,anchor=None):
    raw=path.read_text(encoding='utf-8')
    wrapped=START+'\n'+block+END
    if START in raw:
        assert raw.count(START)==1 and raw.count(END)==1
        raw=re.sub(re.escape(START)+r'.*?'+re.escape(END),lambda _:wrapped,raw,flags=re.S)
    else:
        if anchor:
            match=re.search(r'^## '+re.escape(anchor)+r'[^\n]*\n',raw,re.M)
            if not match:raise ValueError(f'Missing heading in {path}: {anchor}')
            position=match.end()
        else:
            position=raw.find('\n## ')
            if position<0:position=len(raw)
        raw=raw[:position]+'\n'+wrapped+'\n'+raw[position:]
    path.write_text(raw,encoding='utf-8')

def sources():
    catalog=json.loads((ROOT/'portal/videos.json').read_text(encoding='utf-8'))
    assert len(catalog['topics'])==26 and len(catalog['videos'])==34
    topics={t['id']:t for t in catalog['topics']}
    for t in topics.values():
        assert all((ROOT/p).is_file() for p in t['lessons'])
        for c in t['clips']:assert c['video'] in catalog['videos'] and re.fullmatch(r'[\w-]{11}',c['video'])
    generated=[]
    root='# مكتبة الفيديوهات | Video library\n\n'+pair(['26 topics · 34 selected videos · Prepared by Meaad Al-Marri','26 موضوعًا · 34 فيديو مختارًا · إعداد ميعاد المري'])+'\n\n'+pair(GUIDANCE)+'\n\n'
    root+='## اختر مرحلتك | Choose your stage\n\n'
    for stage,en,ar,path in GROUPS:
        rel='../'+path if path.startswith('day-') else path.removeprefix('docs/')
        root+=f'- [{ar} · {en}]({rel})\n'
    for stage,en,ar,path in GROUPS:
        selected=[t for t in catalog['topics'] if t['stage']==stage]
        section=f'## {ar} | {en}\n\n'+''.join(card(t,catalog) for t in selected)
        root+='\n'+section
        text=f'# {ar} | {en}\n\n'+pair(GUIDANCE)+'\n'+''.join(card(t,catalog) for t in selected)+pair(FOOT)+'\n'
        (ROOT/path).write_text(text,encoding='utf-8');generated.append(path)
    root+='\n## استخدام المقاطع | Using the videos\n\n'+pair(FOOT)+'\n'
    (ROOT/'docs/youtube-videos.md').write_text(root,encoding='utf-8');generated.append('docs/youtube-videos.md')
    mappings={}
    for t in catalog['topics']:
        for p in t['lessons']:
            if p!='docs/learner-workflow.md':mappings.setdefault(p,[]).append(t)
    for path,selected in mappings.items():
        block='### شاهد الفكرة ثم طبّقها | Video companions\n\n'+''.join(card(t,catalog,False) for t in selected)
        bounded_insert(ROOT/path,block);generated.append(path)
    wf=ROOT/'docs/learner-workflow.md';raw=wf.read_text(encoding='utf-8')
    for number,tid in [(2,'t02'),(3,'t01'),(4,'t03'),(8,'t25')]:
        pattern=re.compile(r'(^## '+str(number)+r'\. [^\n]*\n)',re.M)
        begin=f'<!-- BAYAN_YOUTUBE_STEP_{number} -->';end=f'<!-- /BAYAN_YOUTUBE_STEP_{number} -->'
        block=begin+'\n'+card(topics[tid],catalog,False)+end
        if begin in raw:
            raw,count=re.subn(re.escape(begin)+r'.*?'+re.escape(end),lambda _:block,raw,count=1,flags=re.S)
        else:
            raw,count=pattern.subn(lambda m:m.group(1)+'\n'+block+'\n',raw,count=1)
        assert count==1,(number,tid)
    wf.write_text(raw,encoding='utf-8');generated.append('docs/learner-workflow.md')
    for n in range(1,5):
        path=f'day-0{n}/README.md'
        bounded_insert(ROOT/path,f'## فيديوهات هذا اليوم | Videos for this day\n\n[▶ افتح فيديوهات اليوم {n} حسب الموضوع · Open Day {n} video companions](VIDEOS.md)\n\nتوجد أزرار المشاهدة كذلك داخل الدروس التفصيلية في موضع الموضوع. · Direct video buttons also appear in the related detailed lessons.\n')
        generated.append(path)
    for path,rel in [('README.md','docs/youtube-videos.md'),('START_HERE.md','docs/youtube-start.md')]:
        bounded_insert(ROOT/path,f'## تعلم بالمشاهدة | Learn with video\n\n[▶ افتح فيديوهات YouTube المرتبة حسب الرحلة · Open the topic-matched YouTube videos]({rel})\n')
        generated.append(path)
    report={'result':'VIDEO_COMPANION_SOURCES_PASS','topics':26,'unique_videos':34,'paths':sorted(set(generated)),
            'frontend_javascript_added':False,'catalog_sha256':hashlib.sha256((ROOT/'portal/videos.json').read_bytes()).hexdigest()}
    (ROOT/'portal/video-source-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'result':report['result'],'paths':len(report['paths'])}))

def navigation(site):
    raw=site.read_text(encoding='utf-8')
    link='<a href="#read/docs%2Fyoutube-videos.md" data-youtube-nav>Videos · الفيديوهات</a>'
    if 'data-youtube-nav' not in raw:
        assert '</nav>' in raw
        raw=raw.replace('</nav>',link+'</nav>',1)
    if 'id="youtube-companions"' not in raw:
        buttons=''.join('<a class="button" href="#read/'+quote(path,safe='')+'">'+html.escape(ar)+'</a>' for _,_,ar,path in GROUPS)
        bar='<section class="wrap" id="youtube-companions" aria-label="YouTube companions"><details><summary>▶ فيديوهات تعليمية بحسب موضوعك · Topic-matched YouTube videos</summary><p><a class="button primary" href="#read/docs%2Fyoutube-videos.md">مكتبة الفيديوهات · Video library</a></p><div class="actions">'+buttons+'</div><p class="micro">روابط مباشرة؛ المشاهدة للمساعدة وليست متطلب تقييم إضافيًا. · Direct links; viewing is support, not an extra assessment.</p></details></section>'
        m=re.search(r'<main\b',raw);assert m
        raw=raw[:m.start()]+bar+raw[m.start():]
    if 'id="youtube-companion-style"' not in raw:
        css='<style id="youtube-companion-style">#youtube-companions{padding-top:12px;padding-bottom:12px}#youtube-companions>details{border:1px solid #cee2e8;border-radius:12px;background:white;padding:12px 18px}#youtube-companions summary{cursor:pointer;font-weight:600;color:#075865}.youtube-topic{margin:18px 0;padding:24px}.youtube-topic h3{font-size:19px}.youtube-topic summary{cursor:pointer;padding:12px;color:#075865;background:#f1f8f9;border-radius:8px;margin:12px 0}.youtube-topic .button.primary{background:#075865;color:white;text-decoration:none;line-height:1.7;white-space:normal;text-align:center}.youtube-topic .callout{font-size:14px;padding:16px}.youtube-topic .pair{gap:24px}.youtube-topic p{margin-top:8px;margin-bottom:16px}@media(max-width:760px){.youtube-topic{padding:16px}.youtube-topic h3{font-size:17px}.youtube-topic .pair{gap:12px}.youtube-topic .button{display:flex;max-width:100%}}</style>'
        raw=raw.replace('</head>',css+'</head>',1)
    site.write_text(raw,encoding='utf-8')
    print('VIDEO_STATIC_NAVIGATION_PASS')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sources',action='store_true')
    parser.add_argument('--navigation',type=Path)
    args=parser.parse_args()
    if args.sources:sources()
    if args.navigation:navigation(args.navigation)
