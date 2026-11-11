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
V3_C1T_SHA="9ba666ddca06c036e4f84c19416b03ea5f75e51d2ea55129d3527d58a4e166e3"
V3_C1TE_SHA="0d4ea8e4b5fc7ec44e3b772f470aeffa81cc50009b2f724d0420c89fd8cd58ce"

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.guides=[]
        self.steps=[]
        self.v3_steps=[]
    def handle_starttag(self,tag,pairs):
        d=dict(pairs)
        if "data-application-visual" in d:self.guides.append(d)
        if "data-application-step" in d:self.steps.append(d["data-application-step"])
        if "data-v3-step" in d:self.v3_steps.append(d["data-v3-step"])

def main():
    sprite=DIST/"images/application/tile-application-6.webp"
    assert sprite.is_file(),"Missing user illustrations in static output"
    assert hashlib.sha256(sprite.read_bytes()).hexdigest()==SHA,"Unexpected user sprite image"
    new_sprite=DIST/"images/application-v3/fenek-bond-c1t-steps.webp"
    assert new_sprite.is_file(),"Missing the reviewed BOND-C1T V3 artwork"
    raw=new_sprite.read_bytes()
    assert raw[:4]==b"RIFF" and raw[8:12]==b"WEBP","Invalid C1T V3 WebP"
    assert hashlib.sha256(raw).hexdigest()==V3_C1T_SHA,"Changed C1T V3 asset"
    c1te_sprite=DIST/"images/application-v3/fenek-bond-c1te-steps.webp"
    assert c1te_sprite.is_file(),"Missing reviewed BOND-C1TE V3 artwork"
    assert hashlib.sha256(c1te_sprite.read_bytes()).hexdigest()==V3_C1TE_SHA,"Changed C1TE artwork"
    verified_c1t={
        "01_support.png":"833a54cc1ac69570a446cc411423e22c5789a2efa597a4eef7ca701ad37fc74c",
        "02_epi.png":"c767d4dc7bc6381c8bbfd8e1f31e48549b594d939a787d5806ba091cbd4c7602",
        "03_gachage.png":"ecbb94776fa0c8491764dc13e11e0bb7fad2c7ddfbdaaafdbcc4b9be5102844d",
        "04_repos.png":"5492a8016643a71794641c60b6ed030f733bef87ff9583cc8a1db10c4fc8377f",
        "05_encollage.png":"75542d1f85bb51938463046d9d9a727c76fd1cadc9fcade06cadb90497ce9381",
        "06_pose.png":"cb4decfb17ae12da149f6efc3d7d44bd625ea4a7c58893a4dd74ffb6fb05ac0d",
    }
    for name,digest in verified_c1t.items():
        asset=DIST/"images/application/v3/fenek-bond-c1t"/name
        assert asset.is_file(),("Missing V3 original PNG",name)
        assert hashlib.sha256(asset.read_bytes()).hexdigest()==digest,("Changed V3 original PNG",name)
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
            if product["code"] in {"BOND-C1T","BOND-C1TE"}:
                assert parser.guides[0].get("data-v3-reviewed")=="BROUILLON",(lang,"V3 status")
                assert parser.v3_steps==[str(i) for i in range(1,7)],(lang,"V3 step number mismatch")
                expected_image="fenek-bond-c1te-steps.webp" if product["code"]=="BOND-C1TE" else "fenek-bond-c1t-steps.webp"
                html=path.read_text(encoding="utf-8")
                assert expected_image in html,(lang,"V3 sprite missing")
                other_image="fenek-bond-c1t-steps.webp" if product["code"]=="BOND-C1TE" else "fenek-bond-c1te-steps.webp"
                assert other_image not in html,(lang,"cross-reference sprite leak")
                actual=path.read_text(encoding="utf-8")
                for name in verified_c1t:
                    assert name in actual,(lang,"Full-size V3 reference missing",name,actual.count('class="fenek-v3-detail-link"'))
                assert actual.count('class="fenek-v3-detail-link"')==6,(lang,"Full-size link count")
            else:
                assert not parser.v3_steps,(lang,product["code"],"unreviewed product received V3 image")

            n+=1
    assert n==150,n
    print("PASS: 150 localized FENEK guides, 2 independently reviewed tile V3 guides across FR/AR/EN, both sprite SHAs")

if __name__=="__main__":
    main()
