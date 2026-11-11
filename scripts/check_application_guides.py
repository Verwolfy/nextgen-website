#!/usr/bin/env python3
"""Lot 128 — fail-closed 50-product, 150-page V3 application-guide audit."""
from __future__ import annotations
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/"dist"
CATALOGUE=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf8"))
ARCHIVED=json.loads((ROOT/"src/data/fenek-v3-verified-45.json").read_text(encoding="utf8"))
ORIGINAL_SPRITE_SHA="55197582655ba03f9de8d933047236e63efbd5df27a1acde136c5fc342059b1c"
V3={
 "BOND-C1T":("fenek-bond-c1t","9ba666ddca06c036e4f84c19416b03ea5f75e51d2ea55129d3527d58a4e166e3"),
 "BOND-C1TE":("fenek-bond-c1te","0d4ea8e4b5fc7ec44e3b772f470aeffa81cc50009b2f724d0420c89fd8cd58ce"),
 "BOND-C2FT":("fenek-bond-c2ft","506e65960964c110475562979fe315e4b5b883b2008e2c2b037405a163dd3e27"),
 "BOND-C2TE":("fenek-bond-c2te","6c69deff4f07f9f9f2f212bc2358ce52d441aad6bf34e601e70142c8ce6a3711"),
 "BOND-C2TE-S1":("fenek-bond-c2te-s1","21143de69601caf85196a931b30396c1332da1a8cc9e0ef3b0e1670d5d8d7499")
}
for item in ARCHIVED:
    if item["code"] in V3:raise AssertionError("Duplicate V3 product "+item["code"])
    V3[item["code"]]=(item["slug"],item["sha256"])
assert len(V3)==50 and len(ARCHIVED)==45
assert {p["code"] for p in CATALOGUE}==set(V3)

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.guides=[]
        self.steps=[]
        self.v3_steps=[]
        self.notes=0
    def handle_starttag(self,tag,pairs):
        d=dict(pairs)
        if "data-application-visual" in d:self.guides.append(d)
        if "data-application-step" in d:self.steps.append(d["data-application-step"])
        if "data-v3-step" in d:self.v3_steps.append(d["data-v3-step"])
        if "fenek-application-visual-attention" in (d.get("class") or "").split():self.notes+=1

def main():
    sprite=DIST/"images/application/tile-application-6.webp"
    assert sprite.is_file(),"Missing historical illustration archive"
    assert hashlib.sha256(sprite.read_bytes()).hexdigest()==ORIGINAL_SPRITE_SHA
    for code,(slug,sha) in V3.items():
        path=DIST/"images/application-v3"/(slug+"-steps.webp")
        assert path.is_file(),(code,"missing V3 artwork")
        data=path.read_bytes()
        assert data[:4]==b"RIFF" and data[8:12]==b"WEBP",(code,"invalid WebP")
        assert hashlib.sha256(data).hexdigest()==sha,(code,"wrong V3 illustration")
    n=0
    for product in CATALOGUE:
        code,slug=product["code"],product["slug"]
        assert slug==V3[code][0],(code,"source/reference mismatch")
        for lang in ("fr","ar","en"):
            path=DIST/lang/"documentation"/slug/"index.html"
            assert path.is_file(),path
            html=path.read_text(encoding="utf8")
            parser=Parser()
            parser.feed(html)
            assert len(parser.guides)==1,(lang,code,"guide count")
            assert parser.guides[0].get("data-reference")==code,(lang,code,"wrong reference")
            assert parser.guides[0].get("data-v3-reviewed")=="BROUILLON",(lang,code,"approval status")
            assert parser.guides[0].get("data-application-count")=="6",(lang,code,"six-stage count")
            assert parser.steps==[str(i) for i in range(1,7)],(lang,code,"numbered stages")
            assert parser.v3_steps==[str(i) for i in range(1,7)],(lang,code,"V3 illustrated stages")
            assert parser.notes==1,(lang,code,"reference-specific qualification note")
            expected=slug+"-steps.webp"
            assert expected in html,(lang,code,"V3 sprite absent")
            assert html.count(expected)>=6,(lang,code,"missing individual visual panels")
            assert "SUPABASE_SERVICE_ROLE_KEY" not in html,(lang,code,"private credentials")
            n+=1
    assert n==150,n
    print("PASS: 50 independently matched V3 sprites and 150 six-step FR/AR/EN draft pages")

if __name__=="__main__":
    main()
