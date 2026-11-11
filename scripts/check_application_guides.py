#!/usr/bin/env python3
"""Fail-closed integrity and correspondence audit for all 50 × 3 V3 FENEK guides."""
from __future__ import annotations
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/"dist"
CATALOGUE=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf8"))
MANUALS=json.loads((ROOT/"src/data/fenek-v3-manuals.json").read_text(encoding="utf8"))
TILE={"BOND-C1T","BOND-C1TE","BOND-C2FT","BOND-C2TE","BOND-C2TE-S1"}
LEGACY={
    "BOND-C1T":"9ba666ddca06c036e4f84c19416b03ea5f75e51d2ea55129d3527d58a4e166e3",
    "BOND-C1TE":"0d4ea8e4b5fc7ec44e3b772f470aeffa81cc50009b2f724d0420c89fd8cd58ce",
}

class Parser(HTMLParser):
    def __init__(self):
        super().__init__();self.guides=[];self.steps=[];self.v3=[];self.fullres=[]
    def handle_starttag(self,tag,pairs):
        d=dict(pairs)
        if 'data-application-visual' in d:self.guides.append(d)
        if 'data-application-step' in d:self.steps.append(d['data-application-step'])
        if 'data-v3-step' in d:self.v3.append((d['data-v3-step'],d.get('aria-label',''),d.get('role','')))
        if tag=='a' and 'fenek-v3-detail-link' in (d.get('class','')).split():self.fullres.append(d.get('href'))

def main():
    if len(CATALOGUE)!=50 or len(MANUALS)!=50:
        raise AssertionError('Expected 50 exact catalogue/manual entries')
    by_code={m['code']:m for m in MANUALS}
    if len(by_code)!=50 or set(by_code)!={p['code'] for p in CATALOGUE}:
        raise AssertionError('V3 catalogue identity mismatch')
    original=DIST/'images/application/tile-application-6.webp'
    assert original.exists(), 'Missing legacy drawing - preserve old pages and tests'
    assert hashlib.sha256(original.read_bytes()).hexdigest()=="55197582655ba03f9de8d933047236e63efbd5df27a1acde136c5fc342059b1c"
    count=0
    for product in CATALOGUE:
        code,slug=product['code'],product['slug']
        manual=by_code[code]
        assert manual['slug']==slug and manual['status']=='BROUILLON',(code,'source mismatch')
        assert not product['certifie'] and not product['commercialise'],code
        assert len(manual['steps'])==6 and [x['image'] for x in manual['steps']]==list(range(1,7)),code
        sprite=f'/images/application-v3/{slug}-steps.webp'
        assert manual['sprite']==sprite,(code,'wrong sprite path')
        actual_sha=LEGACY.get(code,manual['sha256'])
        asset=DIST/sprite.lstrip('/')
        assert asset.is_file(),(code,'asset missing',sprite)
        raw=asset.read_bytes()
        assert raw[:4]==b'RIFF' and raw[8:12]==b'WEBP',(code,'invalid WebP')
        assert hashlib.sha256(raw).hexdigest()==actual_sha,(code,'unexpected image hash')
        for lang in ('fr','ar','en'):
            html_path=DIST/lang/'documentation'/slug/'index.html'
            assert html_path.is_file(),html_path
            html=html_path.read_text(encoding='utf8')
            parser=Parser();parser.feed(html)
            assert len(parser.guides)==1,(lang,code,'guide count')
            guide=parser.guides[0]
            assert guide.get('data-reference')==code,(lang,code,'reference')
            assert guide.get('data-application-count')=='6',(lang,code,'six steps')
            assert guide.get('data-v3-reviewed')=='BROUILLON',(lang,code,'approval status')
            assert guide.get('data-v3-sprite')==sprite,(lang,code,'wrong asset source')
            assert guide.get('data-v3-hash')==actual_sha,(lang,code,'wrong media SHA')
            assert parser.steps==[str(i) for i in range(1,7)],(lang,code,'step order')
            assert [s[0] for s in parser.v3]==[str(i) for i in range(1,7)],(lang,code,'V3 step order')
            for i,(_,aria,role) in enumerate(parser.v3):
                title=manual['steps'][i]['title'][lang]
                if code in LEGACY:
                    # C1T/C1TE use their already reviewed editorial titles.
                    assert role=='img' and aria,(lang,code,i,'missing access label')
                else:
                    assert role=='img' and title in aria,(lang,code,i,'wrong title for image')
            assert sprite in html,(lang,code,'sprite not shown')
            if code=='BOND-C1T':
                assert len(parser.fullres)==6,(lang,code,'C1T full-resolution links')
            else:
                assert not parser.fullres,(lang,code,'unreviewed full-size links')
            count+=1
    assert count==150,count
    print('PASS: 150 V3 guides, 50 exact references, 300 images/steps, FR/AR/EN and SHA-256 integrity')

if __name__=='__main__': main()