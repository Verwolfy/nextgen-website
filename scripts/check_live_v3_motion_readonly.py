#!/usr/bin/env python3
"""Lot 90 — anonymous read-only proof of V3 Motion + Industry on the public domain."""
from __future__ import annotations
import hashlib
import html
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.check_live_video_deployment import inspect_url

ROOT=Path(__file__).resolve().parents[1]
ORIGIN="https://nextgen-buildingsolutions.com"
REPORT=ROOT/".ci-artifacts/lot90-live-v3-motion.json"
EXPECTED={
 "fr":("Le terrain inspire.", "Les solutions prennent forme.",
       "Présentation provisoire", "v3-featured-card"),
 "ar":("من الميدان تبدأ الفكرة.", "ومنها تتشكل الحلول.",
       "عرض أولي", "v3-featured-card"),
 "en":("Inspired by the field.", "Shaped into solutions.",
       "Provisional presentation", "v3-featured-card"),
}
MEDIA={
 "video":"videos/nextgen-nexo-geno-welcome.mp4",
 "poster":"videos/nextgen-nexo-geno-poster.webp",
}
QUERY="?v=20261105-v3"


def audit_home(lang:str)->dict:
    url=f"{ORIGIN}/{lang}/?verification=lot90-v3-20261105"
    meta,body=inspect_url(url)
    text=html.unescape(body.decode("utf-8",errors="replace")) if meta["status"]==200 else ""
    markers={word:word in text for word in EXPECTED[lang]}
    media_markers={
      "original_video":f"/{MEDIA['video']}{QUERY}" in text,
      "original_poster":f"/{MEDIA['poster']}{QUERY}" in text,
      "video_player":"data-welcome-card" in text and "data-welcome-video" in text,
    }
    noindex='noindex,nofollow' in text
    good=meta["status"]==200 and not meta.get("oversized") and all(markers.values()) and all(media_markers.values()) and noindex
    return {"lang":lang,"http":meta["status"],"url":url,
            "markers":markers,"media_markers":media_markers,"noindex":noindex,
            "v3_home_confirmed":good}


def audit_media(kind:str)->dict:
    relative=MEDIA[kind]
    url=f"{ORIGIN}/{relative}?verification=lot90-v3-20261105"
    meta,body=inspect_url(url)
    expected=(ROOT/"public"/relative).read_bytes()
    matching=meta["status"]==200 and not meta.get("oversized") and (
        hashlib.sha256(body).digest()==hashlib.sha256(expected).digest()
    )
    return {"kind":kind,"http":meta["status"],"sha256_matches_repository":matching}


def audit_once()->dict:
    pages=[audit_home(lang) for lang in ("fr","ar","en")]
    media=[audit_media(kind) for kind in ("video","poster")] if all(
        p["v3_home_confirmed"] for p in pages) else []
    success=len(media)==2 and all(m["sha256_matches_repository"] for m in media)
    return {"timestamp_utc":datetime.now(timezone.utc).isoformat(),
            "origin":ORIGIN,"pages":pages,"media":media,
            "v3_public_content_verified":success,
            "exact_cloudflare_commit_verified":False,
            "read_only":True,"deployment_performed":False}


def report(result:dict)->None:
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False,indent=2))
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"],"a",encoding="utf-8") as f:
            f.write("\n## Lot 90 — V3 Motion + Industry sur domaine public (lecture seule)\n\n")
            f.write("| Langue | HTTP | Accueil V3 | noindex |\n|---|---|---|---|\n")
            for p in result["pages"]:
                f.write(f"| {p['lang']} | {p['http']} | {p['v3_home_confirmed']} | {p['noindex']} |\n")
            f.write(f"\n**V3 visible avec vidéo originale : {result['v3_public_content_verified']}**. ")
            f.write("Aucune action Cloudflare ; SHA exact du déploiement non démontré.\n")


def main()->int:
    last={}
    for attempt in range(4):
        last=audit_once()
        last["attempt"]=attempt+1
        if last["v3_public_content_verified"]:
            break
        if attempt<3:
            time.sleep(30)
    last["expected_github_main_sha"]=os.environ.get("GITHUB_SHA","unavailable")
    report(last)
    return 0 if last["v3_public_content_verified"] else 1

if __name__=="__main__":
    raise SystemExit(main())
