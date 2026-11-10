#!/usr/bin/env python3
"""Lot 124: verify built FR/AR/EN About video and exact optimized media bytes."""
from __future__ import annotations

import hashlib
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]/"dist"
ASSETS={
    "videos/nextgen-about-v4.mp4":"46ab654f906dbe4e679c5b96fbed7b79b5cce143e288117a923470a9d7443e71",
    "videos/nextgen-about-v4-poster.webp":"071ecc7f73af7c9b5fec5c5f55b28ac755739c78cc8edc4c7b376c85107373e5",
    "videos/nextgen-about-v4.webm":"33b312897fd3443c6424c8ea4dd4a69db4d608f7b3c59b1aa6d8e19e8054d327",
}
class AboutVideoParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.players=[]
        self.sources=[]
        self.in_video=False
    def handle_starttag(self,tag,pairs):
        attr=dict(pairs)
        if tag=="video" and "data-about-video" in attr:
            self.players.append(attr)
            self.in_video=True
        if tag=="source" and self.in_video:
            self.sources.append(attr)
    def handle_endtag(self,tag):
        if tag=="video":
            self.in_video=False

def main():
    for asset,digest in ASSETS.items():
        path=ROOT/asset
        assert path.is_file(),f"Missing optimized About media {asset}"
        assert hashlib.sha256(path.read_bytes()).hexdigest()==digest,asset
    for lang in ("fr","ar","en"):
        path=ROOT/lang/"a-propos"/"index.html"
        assert path.is_file(),path
        p=AboutVideoParser();p.feed(path.read_text(encoding="utf-8"))
        assert len(p.players)==1,(lang,"video count")
        data=p.players[0]
        assert [(x.get("src"),x.get("type")) for x in p.sources]==[
            ("/videos/nextgen-about-v4.webm","video/webm"),
            ("/videos/nextgen-about-v4.mp4","video/mp4")
        ],(lang,p.sources)
        assert data.get("poster")=="/videos/nextgen-about-v4-poster.webp",lang
        assert data.get("data-about-video-version")=="v4",lang
        assert data.get("preload")=="none",lang
        for flag in ("muted","loop","controls","playsinline"):
            assert flag in data,(lang,flag)
        assert data.get("aria-label"),(lang,"missing accessible video label")
    print("PASS: final About v4 video SHA-256, poster and three localized pages")

if __name__=="__main__":
    main()
