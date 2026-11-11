#!/usr/bin/env python3
"""Read-only production check: 50 V3 illustration refs × FR/AR/EN, exact served SHA."""
from __future__ import annotations
import argparse
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

from check_live_production import LANGS, fetch, validate_html

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / 'src' / 'data' / 'catalogue-projets.json'
MANUALS = ROOT / 'src' / 'data' / 'fenek-v3-manuals.json'
SPRITE_SHA256 = '55197582655ba03f9de8d933047236e63efbd5df27a1acde136c5fc342059b1c'
C1T_V3_SHA256 = '9ba666ddca06c036e4f84c19416b03ea5f75e51d2ea55129d3527d58a4e166e3'
C1TE_V3_SHA256 = '0d4ea8e4b5fc7ec44e3b772f470aeffa81cc50009b2f724d0420c89fd8cd58ce'
LEGACY = {'BOND-C1T': C1T_V3_SHA256, 'BOND-C1TE': C1TE_V3_SHA256}
TILE_ADHESIVES = frozenset({'BOND-C1T','BOND-C1TE','BOND-C2FT','BOND-C2TE','BOND-C2TE-S1'})


class ApplicationGuideMarkup(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.guides: list[dict[str,str|None]]=[]
        self.steps: list[str]=[]
        self.v3: list[str]=[]
        self.drawing_count=0
        self.pictogram_count=0
        self.notes=0
    def handle_starttag(self, tag: str, pairs: list[tuple[str,str|None]]) -> None:
        attrs=dict(pairs)
        if tag=='section' and 'data-application-visual' in attrs:
            self.guides.append(attrs)
        if tag=='li' and 'data-application-step' in attrs:
            self.steps.append(attrs.get('data-application-step') or '')
        if tag=='div':
            classes=(attrs.get('class') or '').split()
            if 'fenek-application-visual-photo' in classes:
                self.drawing_count+=1
                if attrs.get('role')!='img' or not attrs.get('aria-label'):
                    raise AssertionError('Illustration has no meaningful alt label')
            if 'fenek-application-visual-icon' in classes:
                self.pictogram_count+=1
            if 'fenek-application-visual-attention' in classes:
                self.notes+=1
            if 'data-v3-step' in attrs:
                self.v3.append(attrs['data-v3-step'] or '')


def validate_guide(raw: bytes, lang: str, product: dict) -> None:
    """Validate 6 illustrated stages on every product. Detailed SHA checks in verify_all_guides."""
    validate_html(raw, lang, kind='sheet')
    guide=ApplicationGuideMarkup()
    guide.feed(raw.decode('utf-8'))
    code=product['code']
    if len(guide.guides)!=1: raise AssertionError((lang,code,'missing or duplicate guide'))
    attrs=guide.guides[0]
    if attrs.get('data-reference')!=code: raise AssertionError((lang,code,'wrong reference'))
    if attrs.get('data-application-count')!='6': raise AssertionError((lang,code,'six stages required'))
    if guide.steps!=[str(i) for i in range(1,7)]: raise AssertionError((lang,code,'step order'))
    if guide.drawing_count!=6 or guide.pictogram_count!=0:
        raise AssertionError((lang,code,'six own drawings required; generic pictograms forbidden'))
    if guide.notes!=1: raise AssertionError((lang,code,'missing reference-specific note'))
    if b'SUPABASE_SERVICE_ROLE_KEY' in raw:
        raise AssertionError((lang,code,'private credentials exposed'))


def verify_all_guides(origin: str, timeout: float, workers: int=6) -> int:
    """Only run after the exact deployed Git SHA has been verified by the release gate."""
    catalog=json.loads(CATALOGUE.read_text(encoding='utf-8'))
    manuals=json.loads(MANUALS.read_text(encoding='utf-8'))
    if len(catalog)!=50 or len(manuals)!=50 or len({p['code'] for p in catalog})!=50:
        raise AssertionError('Source catalogue must contain 50 distinct references')
    if len({p['slug'] for p in catalog})!=50 or {p['gamme'] for p in catalog}!={'bond','flow','proof','paint'}:
        raise AssertionError('Invalid source catalogue')
    index={m['code']:m for m in manuals}
    if len(index)!=50 or set(index)!={p['code'] for p in catalog}:
        raise AssertionError('Manual reference map mismatch')
    legacy=fetch(origin,'/images/application/tile-application-6.webp',timeout)
    if hashlib.sha256(legacy).hexdigest()!=SPRITE_SHA256:
        raise AssertionError('Original customer illustration modified')
    print('PASS original V2 fallback integrity',flush=True)

    # Check each actual, public image independently, not merely the source manifest.
    def test_asset(p:dict)->str:
        code=p['code'];manual=index[code];slug=p['slug']
        if manual['slug']!=slug or manual['status']!='BROUILLON':
            raise AssertionError((code,'slug/status mismatch'))
        path=f'/images/application-v3/{slug}-steps.webp'
        if manual['sprite']!=path: raise AssertionError((code,'asset path mismatch'))
        raw=fetch(origin,path,timeout)
        expected=LEGACY.get(code,manual['sha256'])
        if raw[:4]!=b'RIFF' or raw[8:12]!=b'WEBP' or hashlib.sha256(raw).hexdigest()!=expected:
            raise AssertionError((code,'published image SHA incorrect',path))
        return code
    with ThreadPoolExecutor(max_workers=workers) as pool:
        results=list(pool.map(test_asset,catalog))
    if len(results)!=50: raise AssertionError('Some V3 media could not be verified')
    print('PASS 50 served V3 reference-specific media SHA-256',flush=True)

    tasks=[(lang,p,f"/{lang}/documentation/{p['slug']}/") for lang in LANGS for p in catalog]
    def test_page(task):
        lang,p,path=task
        try:
            raw=fetch(origin,path,timeout)
            validate_guide(raw,lang,p)
            doc=ApplicationGuideMarkup();doc.feed(raw.decode('utf-8'))
            code=p['code'];manual=index[code]
            expected_sprite=f'/images/application-v3/{p["slug"]}-steps.webp'
            expected_hash=LEGACY.get(code,manual['sha256'])
            if doc.v3!=[str(i) for i in range(1,7)]:
                raise AssertionError('Incorrect V3 stage numbering')
            attrs=doc.guides[0]
            if attrs.get('data-v3-reviewed')!='BROUILLON':
                raise AssertionError('Provisional V3 status missing')
            if attrs.get('data-v3-sprite')!=expected_sprite or attrs.get('data-v3-hash')!=expected_hash:
                raise AssertionError('Product linked to wrong illustration')
            if expected_sprite.encode('utf-8') not in raw:
                raise AssertionError('Source art not actually displayed')
        except Exception as exc:
            raise AssertionError(f'{lang}/{p["code"]} ({path}): {exc}') from exc
        return path
    checked=0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures={pool.submit(test_page,t):t for t in tasks}
        for future in as_completed(futures):
            future.result();checked+=1
    if checked!=150: raise AssertionError(f'Only {checked}/150 application pages were checked')
    print('PASS Cloudflare: 150 FR/AR/EN V3 pages, 50 art SHAs, noindex, stage order and identity',flush=True)
    return checked


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--origin',default='https://nextgen-buildingsolutions.com')
    parser.add_argument('--timeout',type=float,default=15)
    parser.add_argument('--workers',type=int,default=6)
    args=parser.parse_args()
    parsed=urlsplit(args.origin)
    if parsed.scheme!='https' or not parsed.netloc or parsed.path.rstrip('/') or parsed.query:
        raise AssertionError('A clean HTTPS site origin is required')
    if not (1<=args.workers<=8 and 1<=args.timeout<=30):
        raise AssertionError('Unsafe monitor concurrency or timeout')
    verify_all_guides(args.origin.rstrip('/'),args.timeout,args.workers)

if __name__=='__main__':main()