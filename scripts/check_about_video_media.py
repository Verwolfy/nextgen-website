#!/usr/bin/env python3
"""Lot 124: verify built FR/AR/EN About video and exact optimized media bytes."""
from __future__ import annotations

import hashlib
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]/"dist"
ASSETS={
    "videos/nextgen-about-v2.mp4":"e322aaf485a24fa3a6c8705077161616f0c129e34da8cd771f5a6f2e0605a17a",
    "videos/nextgen-about-v2-poster.webp":"b5ebd897a82c0e3c8b7d6668fcdd4dc9432911db187ef1d04d543439cf9a5936",
    "videos/nextgen-about-v2.webm":"0c1d040f7984b3877c0c483780e70128cc5ac57eeed5cf8ef06da9378b2a908d",
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
            ("/videos/nextgen-about-v2.webm","video/webm"),
            ("/videos/nextgen-about-v2.mp4","video/mp4")
        ],(lang,p.sources)
        assert data.get("poster")=="/videos/nextgen-about-v2-poster.webp",lang
        assert data.get("data-about-video-version")=="v2",lang
        assert data.get("preload")=="none",lang
        for flag in ("muted","loop","controls","playsinline"):
            assert flag in data,(lang,flag)
        assert data.get("aria-label"),(lang,"missing accessible video label")
    print("PASS: final About v2 video SHA-256, poster and three localized pages")

if __name__=="__main__":
    main()
