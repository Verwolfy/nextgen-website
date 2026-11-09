#!/usr/bin/env python3
"""Audit generated HTML for all 150 localized FENEK application walkthroughs."""
from __future__ import annotations
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/"dist"
CATALOGUE=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf8"))
TILE={"BOND-C1T","BOND-C1TE","BOND-C2FT","BOND-C2TE","BOND-C2TE-S1"}
SHA="55197582655ba03f9de8d933047236e63efbd5df27a1acde136c5fc342059b1c"

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.guides=[]
        self.steps=[]
    def handle_starttag(self,tag,pairs):
        d=dict(pairs)
        if "data-application-visual" in d:self.guides.append(d)
        if "data-application-step" in d:self.steps.append(d["data-application-step"])

def main():
    sprite=DIST/"images/application/tile-application-6.webp"
    assert sprite.is_file(),"Missing user illustrations in static output"
    assert hashlib.sha256(sprite.read_bytes()).hexdigest()==SHA,"Unexpected user sprite image"
    n=0
    for product in CATALOGUE:
        exp=6 if product["code"] in TILE else 4
        for lang in ("fr","ar","en"):
            path=DIST/lang/"documentation"/product["slug"]/"index.html"
            assert path.is_file(),path
            parser=Parser()
            parser.feed(path.read_text(encoding="utf8"))
            assert len(parser.guides)==1,(lang,product["code"],"guide count")
            assert parser.guides[0].get("data-reference")==product["code"],(lang,product["code"],"reference mismatch")
            assert int(parser.guides[0].get("data-application-count","-1"))==exp,(lang,product["code"],"step count")
            assert parser.steps==[str(i) for i in range(1,exp+1)],(lang,product["code"],parser.steps)
            n+=1
    assert n==150,n
    print("PASS: 150 localized illustrated FENEK walkthroughs and genuine user sprite SHA256")

if __name__=="__main__":
    main()
