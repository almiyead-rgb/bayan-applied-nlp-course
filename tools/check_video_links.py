#!/usr/bin/env python3
"""Record live YouTube oEmbed metadata; this does not verify full playback."""
from __future__ import annotations
import argparse, concurrent.futures, datetime, json, time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError
ROOT=Path(__file__).resolve().parents[1]

def inspect(item):
    video_id,video=item
    url='https://www.youtube.com/watch?v='+video_id
    endpoint='https://www.youtube.com/oembed?'+urlencode({'url':url,'format':'json'})
    result={'video_id':video_id,'url':url,'expected_title':video['title'],'reference':video['source']}
    for attempt in range(2):
        try:
            request=Request(endpoint,headers={'User-Agent':'Bayan-course-link-check/1.0','Accept':'application/json'})
            with urlopen(request,timeout=12) as response: metadata=json.load(response)
            if metadata.get('provider_name')!='YouTube' or not metadata.get('title'): raise ValueError('Unexpected metadata response')
            return {**result,'status':'METADATA_RESOLVED','title':metadata['title'],'author':metadata.get('author_name'),'playback_verified':False}
        except HTTPError as error:
            result.update(status='REVIEW_REQUIRED' if error.code in (400,401,404) else 'NETWORK_UNCONFIRMED',http_status=error.code)
        except Exception as error:
            result.update(status='NETWORK_UNCONFIRMED',error=type(error).__name__)
        if attempt==0: time.sleep(1)
    return {**result,'playback_verified':False}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=ROOT/'_site/video-link-check.json')
    args=parser.parse_args()
    catalog=json.loads((ROOT/'portal/videos.json').read_text(encoding='utf-8'))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: videos=list(pool.map(inspect,catalog['videos'].items()))
    counts={state:sum(v['status']==state for v in videos) for state in ('METADATA_RESOLVED','NETWORK_UNCONFIRMED','REVIEW_REQUIRED')}
    report={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'total':len(videos),'counts':counts,'videos':videos,'scope':'YouTube metadata only; no full video playback or regional availability guarantee.'}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'total':len(videos),'counts':counts,'report':str(args.out)}))
    if counts['REVIEW_REQUIRED']:
        print('Review these IDs:',[v['video_id'] for v in videos if v['status']=='REVIEW_REQUIRED'])
        raise SystemExit(1)
