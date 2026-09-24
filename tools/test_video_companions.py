#!/usr/bin/env python3
"""Test topic placement, direct links and existing reader navigation, not playback."""
from __future__ import annotations
import argparse, functools, json, os, threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, quote, urlsplit
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from build_video_companions import ROOT, GROUPS

def main(render_only=False):
    catalog=json.loads((ROOT/'portal/videos.json').read_text())
    html=(ROOT/'_site/index.html').read_text()
    soup=BeautifulSoup(html,'html.parser')
    data=json.loads(soup.select_one('#portal-data').string)
    docs={d['path']:BeautifulSoup(d['html'],'html.parser') for d in data['documents']}
    checks=[]
    def check(ok,label):
        assert ok,label
        checks.append(label)
    check(len(catalog['topics'])==26 and len(catalog['videos'])==34,'26_topics_34_unique_videos')
    guides=[g[3] for g in GROUPS]+['docs/youtube-videos.md']
    check(all(p in docs for p in guides),'seven_searchable_video_guides')
    library=docs['docs/youtube-videos.md']
    check(len(library.select('.youtube-topic'))==26,'one_library_card_per_topic')
    links=library.select('a[href^="https://www.youtube.com/watch?"]')
    ids={parse_qs(urlsplit(a['href']).query)['v'][0] for a in links}
    check(ids==set(catalog['videos']),'every_selected_video_has_direct_watch_link')
    check(all(a.get('target')=='_blank' and set(a.get('rel',[]))>={'noopener','noreferrer'} for a in links),'safe_new_tab_youtube_links')
    for t in catalog['topics']:
        for path in t['lessons']:
            if path=='docs/learner-workflow.md':continue
            for c in t['clips']:
                check(bool(docs[path].select(f'a[href*="v={c["video"]}"]')),f'{t["id"]}_placed_in_{path}_{c["video"]}')
    for stage,_,_,path in GROUPS:
        check(len(docs[path].select('.youtube-topic'))==sum(t['stage']==stage for t in catalog['topics']),f'{stage}_stage_grouping')
    for n in range(1,5):
        route='#read/'+quote(f'day-0{n}/VIDEOS.md',safe='')
        check(bool(docs[f'day-0{n}/README.md'].find('a',href=route)),f'day_{n}_guide_video_entry')
    check(soup.select_one('[data-youtube-nav]') is not None and soup.select_one('#youtube-companions') is not None,'global_navigation_and_stage_entry_strip')
    check('youtube.com/embed' not in html and 'youtu.be/embed' not in html,'no_external_video_player_loaded')
    check(data['course']['assessment_weights']==[70,20,10],'grading_unchanged')
    for t in catalog['topics']:
        for c in t['clips']:
            if 'start' in c:check(bool(library.select(f'a[href*="v={c["video"]}"][href*="t={c["start"]}s"]')),f'{t["id"]}_segment_start_preserved')
    class Quiet(SimpleHTTPRequestHandler):
        def log_message(self,*args):pass
    server=None
    if not render_only:
        server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=ROOT/'_site'))
        threading.Thread(target=server.serve_forever,daemon=True).start()
    errors=[]
    with sync_playwright() as p:
        launch={'headless':True}
        if os.getenv('BROWSER_EXECUTABLE'):launch['executable_path']=os.environ['BROWSER_EXECUTABLE']
        browser=p.chromium.launch(**launch);page=browser.new_page(viewport={'width':1440,'height':1000})
        page.on('pageerror',lambda e:errors.append(str(e)))
        if render_only:page.set_content(html)
        else:page.goto(f'http://127.0.0.1:{server.server_port}/',wait_until='domcontentloaded')
        def go(path):
            page.evaluate('(p)=>{location.hash="#read/"+encodeURIComponent(p);render();}',path)
            page.wait_for_timeout(100)
        page.locator('[data-youtube-nav]').click();page.wait_for_timeout(150)
        check(page.locator('.markdown .youtube-topic').count()==26,'video_navigation_opens_library')
        for _,_,_,path in GROUPS:
            go(path)
            check(page.locator('.markdown a[href^="https://www.youtube.com/watch?"]').count()>0,'reader_buttons_'+path)
        for lang in ['ar','en','both']:
            page.locator(f'.languages [data-language="{lang}"]').click()
            check(page.locator('html').get_attribute('data-language')==lang,'language_mode_'+lang)
        go('day-01/VIDEOS.md')
        page.context.route('https://www.youtube.com/**',lambda r:r.fulfill(status=200,content_type='text/html',body='<p>YouTube navigation test</p>'))
        link=page.locator('.markdown a[href*="v=eMlx5fFNoYc"]')
        check(link.get_attribute('href')=='https://www.youtube.com/watch?v=eMlx5fFNoYc','attention_button_exact_destination')
        if not render_only:
            with page.expect_popup() as popup:link.click()
            tab=popup.value;tab.wait_for_load_state('domcontentloaded')
            check('youtube.com/watch?v=eMlx5fFNoYc' in tab.url,'one_click_correct_video_new_tab_not_playback')
            tab.close()
        for width in [390,768,1440]:
            page.set_viewport_size({'width':width,'height':1000})
            for path in ['docs/youtube-videos.md','day-01/VIDEOS.md','docs/learner-workflow.md','day-03/02-semantic-search.md']:
                go(path)
                check(not page.evaluate('document.documentElement.scrollWidth>innerWidth'),f'no_horizontal_overflow_{width}_{path}')
        go('day-01/03-attention-transformers.md')
        check(page.locator('.markdown a[href*="v=eMlx5fFNoYc"]').count()==1,'attention_link_in_correct_scientific_lesson')
        page.screenshot(path=str(ROOT/'_site/videos-context-desktop.png'),full_page=False)
        go('docs/youtube-videos.md');page.screenshot(path=str(ROOT/'_site/videos-library-desktop.png'),full_page=False)
        page.set_viewport_size({'width':390,'height':844});page.screenshot(path=str(ROOT/'_site/videos-library-mobile.png'),full_page=False)
        check(not errors,'no_javascript_runtime_errors')
        browser.close()
    if server:server.shutdown()
    result={'result':'VIDEO_COMPANIONS_PASS','checks':checks,'count':len(checks),'topics':26,'unique_videos':34,'browser_mode':'in_memory_preview' if render_only else 'local_HTTP_origin','scope':'Portal links, content placement and navigation; no full YouTube playback or ML rerun.'}
    (ROOT/'_site/video-acceptance.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'}))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--render-only',action='store_true')
    main(parser.parse_args().render_only)
