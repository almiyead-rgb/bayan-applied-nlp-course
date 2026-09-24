#!/usr/bin/env python3
"""Portal structure and browser acceptance tests. Does not rerun ML notebooks."""
from __future__ import annotations
import argparse, functools, hashlib, json, os, re, threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from build_learning_portal import ROOT, load_course


def main(render_only: bool = False) -> None:
    checks=[];c=load_course();html=(ROOT/'_site/index.html').read_text()
    soup=BeautifulSoup(html,'html.parser');data=json.loads(soup.find(id='portal-data').string)
    paths={d['path'] for d in data['documents']}
    assert len(paths)==len(data['documents']) and len(paths)>=50
    checks.append('source_documents_and_unique_routes')
    assert len(list((ROOT/'notebooks').glob('*.ipynb')))==9
    assert sum(len(d['notebooks']) for d in c['days'])==8
    checks.append('seven_labs_eight_application_notebooks_plus_doctor')
    for d in data['documents']:
        assert d['sha256']==hashlib.sha256((ROOT/d['path']).read_bytes()).hexdigest()
        content=BeautifulSoup(d['html'],'html.parser')
        assert not content.find('script')
        for a in content.find_all('a',href=True):
            h=a['href'];assert not h.lower().startswith(('javascript:','data:'))
            if h.startswith('#read/'):
                assert unquote(h[6:].split('?')[0]) in paths,h
    checks.extend(['source_hash_integrity','sanitised_reference_HTML','internal_reader_routes'])
    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self,*args): pass
    server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(QuietHandler,directory=ROOT/'_site'))
    threading.Thread(target=server.serve_forever,daemon=True).start()
    errors=[]
    with sync_playwright() as p:
        launch={'headless':True}
        if os.environ.get('BROWSER_EXECUTABLE'): launch['executable_path']=os.environ['BROWSER_EXECUTABLE']
        browser=p.chromium.launch(**launch);page=browser.new_page(viewport={'width':1440,'height':1000})
        page.on('pageerror',lambda e:errors.append(str(e)))
        if render_only: page.set_content(html)
        else: page.goto(f'http://127.0.0.1:{server.server_port}/',wait_until='domcontentloaded')
        def go(route):
            page.evaluate('(h)=>location.hash=h',route);page.wait_for_timeout(80)
        assert page.locator('.day-card').count()==4
        assert not page.evaluate('document.documentElement.scrollWidth>innerWidth')
        checks.extend(['desktop_layout','four_day_navigation'])
        for lang in ['ar','en','both']:
            page.locator(f'.languages [data-language="{lang}"]').click()
            assert page.locator('html').get_attribute('data-language')==lang
        checks.append('three_language_modes')
        go('#home');page.locator('[data-check="gate"]').first.check()
        assert page.locator('[role=progressbar]').get_attribute('aria-valuenow')=='1'
        checks.append('personal_progress_and_next_step')
        if not render_only:
            page.reload();assert page.locator('[role=progressbar]').get_attribute('aria-valuenow')=='1'
            checks.append('local_storage_reload_persistence')
        for d in c['days']:
            go('#day-'+str(d['id']))
            assert page.locator('.topic-card').count()==5
            assert page.locator('.architecture-flow li').count()==4
            assert page.locator('.hour').count()==0
            assert '300 min' not in page.locator('main').inner_text()
            assert page.locator('a[href*="colab.research.google.com"]').count()==len(d['notebooks'])
        checks.append('daily_topic_explanations_architecture_and_colab_links')
        go('#home')
        assert page.locator('.brand-image').evaluate('(e)=>e.complete && e.naturalWidth>0')
        assert page.locator('.architecture-branches').count()==1
        assert page.locator('.new-scores .score').count()==3
        for n in page.locator('.rubric-detail').all(): n.locator('summary').click()
        assert page.locator('.rubric-row').count()==17
        assert '70 / 100' in page.locator('.new-scores').inner_text()
        assert '20 / 100' in page.locator('.new-scores').inner_text()
        assert '10 / 100' in page.locator('.new-scores').inner_text()
        assert page.locator('.one-shot').count()==1
        checks.extend(['embedded_owner_image','home_project_scenario_and_branched_architecture','100_point_rubric_on_home','one_shot_integrity_notice'])
        go('#project')
        assert page.locator('.presentation-flow li').count()==5
        assert page.locator('.markdown pre').count()==1
        assert 'PRESENTATION.md' in page.locator('.markdown pre').inner_text()
        page.locator('#learner-repo').fill('file:///C:/fake/index.html')
        page.locator('#make-links').click();assert page.locator('#learner-links').is_hidden()
        page.locator('#learner-repo').fill(c['repository'])
        page.locator('#make-links').click();assert page.locator('#learner-links').is_hidden()
        page.locator('#learner-repo').fill('https://github.com/learner-one/bayan-nlp-learner-one')
        page.locator('#make-links').click()
        assert page.locator('#learner-links').inner_text().count('https://colab.research.google.com/github/learner-one/')==9
        for n in page.locator('[data-final-check]').all():n.check()
        assert '6 / 6' in page.locator('#review-status').inner_text()
        checks.extend(['individual_presentation_and_file_structure','own_colab_link_generator_validation','self_review_not_grading_or_submission'])
        go('#library');page.locator('#search').fill('الانتباه')
        assert page.locator('#search-results a').count()>0
        page.locator('#search').fill('NER');assert page.locator('#search-results a').count()>0
        page.locator('#search').fill('ZZZZ-not-a-course-term');assert page.locator('#search-results a').count()==0
        checks.extend(['Arabic_English_search','empty_search_state'])
        go('#read/day-01%2FGLOSSARY.md');assert page.locator('.markdown table').count()>0
        assert page.locator('.markdown table').first.evaluate('(e)=>getComputedStyle(e).direction')=='ltr'
        page.locator('.toc-link').first.click();page.wait_for_timeout(80)
        assert '?anchor=' in page.url
        checks.extend(['glossary_reader_and_table_direction','reader_anchor_navigation'])
        for width in [390,768]:
            page.set_viewport_size({'width':width,'height':844})
            for route in ['#home','#day-3','#library','#project','#help','#read/day-01%2FGLOSSARY.md','#read/docs%2Flearner-workflow.md']:
                go(route);assert not page.evaluate('document.documentElement.scrollWidth>innerWidth'),(width,route)
        checks.append('mobile_and_tablet_no_horizontal_overflow')
        go('#unknown');assert page.locator('.empty h1').count()==1
        checks.append('missing_route_recovery')
        go('#help');page.once('dialog',lambda d:d.accept());page.locator('#reset-progress').click()
        go('#home');assert page.locator('[role=progressbar]').get_attribute('aria-valuenow')=='0'
        checks.append('explicit_progress_reset')
        assert not errors,errors;checks.append('no_JavaScript_runtime_errors')
        if not render_only:
            offline=browser.new_page(viewport={'width':1440,'height':1000})
            offline.on('pageerror',lambda e:errors.append(str(e)))
            offline.goto((ROOT/'_site/index.html').as_uri()+'#project',wait_until='domcontentloaded')
            assert offline.locator('.rubric-row').count()==17
            assert offline.locator('.brand-image').evaluate('(e)=>e.complete && e.naturalWidth>0')
            offline.evaluate("location.hash='#day-1'");offline.wait_for_timeout(80)
            assert offline.locator('.topic-card').count()==5
            checks.append('offline_file_URL_project_and_day_navigation')
            assert not errors,errors
            offline.close()
        browser.close()
    server.shutdown()
    result={'result':'PORTAL_ACCEPTANCE_PASS','count':len(checks),'checks':checks,
            'browser_mode':'in_memory_render' if render_only else 'local_HTTP_origin',
            'scope':'Portal only; original ML training notebooks were not rerun.'}
    (ROOT/'_site/acceptance-report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--render-only',action='store_true')
    main(parser.parse_args().render_only)
