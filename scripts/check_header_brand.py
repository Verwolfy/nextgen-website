#!/usr/bin/env python3
"""Check generated NextGen brand video, poster, and FR/AR/EN headers."""
from __future__ import annotations

import hashlib
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]/"dist"
MP4="videos/nextgen-header-logo-v1.mp4"
WEBM="videos/nextgen-header-logo-v1.webm"
POSTER="images/nextgen-header-logo-poster-v1.webp"
EXPECTED={
    MP4:"ae3ec46c8123065c3178f0543de93ba8d1d8a8a646dff0a22c8bd4f1e277f116",
    WEBM:"08162155ad64397604bbcd81befafec000b39f6c190999542a2788dd41bfb94d",
    POSTER:"a35f94aefd101087cc9a1609935790d1b64b79c938d782cb363ebe783753a60a",
}


class Brand(HTMLParser):
    def __init__(self):
        super().__init__()
        self.brands=[]
        self.images=[]
        self.videos=[]
        self.sources=[]
        self.search=0
    def handle_starttag(self,tag,pairs):
        a=dict(pairs)
        if tag=="a" and "data-header-brand" in a:self.brands.append(a)
        if tag=="img" and "ng-brand-poster" in (a.get("class") or ""):self.images.append(a)
        if tag=="video" and "data-header-brand-video" in a:self.videos.append(a)
        if tag=="source" and "data-src" in a:self.sources.append(a)
        if tag=="button" and "data-search-trigger" in a:self.search+=1


def main():
    for path,sha in EXPECTED.items():
        target=ROOT/path
        assert target.is_file(),f"Missing encoded logo asset: {path}"
        assert hashlib.sha256(target.read_bytes()).hexdigest()==sha,f"Incorrect logo bytes: {path}"
    for lang in ("fr","ar","en"):
        for suffix in ("","documentation/fenek-bond-c1t"):
            path=ROOT/lang/suffix/"index.html"
            assert path.is_file(),str(path)
            p=Brand()
            p.feed(path.read_text(encoding="utf8"))
            assert len(p.brands)==len(p.images)==len(p.videos)==1, (lang,suffix)
            assert len(p.sources)==2, (lang,suffix,"two interoperable codecs")
            assert p.brands[0].get("href")==f"/{lang}/", (lang,suffix,"logo link")
            assert p.brands[0].get("aria-label"), (lang,suffix,"accessible name")
            assert p.images[0].get("src")=="/"+POSTER, (lang,suffix,"poster")
            assert p.sources[0].get("data-src")=="/"+WEBM, (lang,suffix,"WebM source")
            assert p.sources[1].get("data-src")=="/"+MP4, (lang,suffix,"MP4 fallback")
            assert all("src" not in source for source in p.sources), (lang,suffix,"eager media download")
            v=p.videos[0]
            assert "muted" in v and "loop" in v and "playsinline" in v, (lang,suffix,"playback")
            assert v.get("preload")=="none", (lang,suffix,"preload")
            assert p.search==1, (lang,suffix,"search intact")
    print("PASS: optimized header video/poster + accessible FR/AR/EN links and lazy loop")


if __name__=="__main__":
    main()
