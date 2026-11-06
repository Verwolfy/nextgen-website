#!/usr/bin/env python3
"""Lot 103: anonymous read-only verification of favicon and key V3 public routes.

No DNS, Access, deployment or authentication changes. Confirms content, not SHA.
"""
from __future__ import annotations
import hashlib
import html
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.check_live_video_deployment import inspect_url

ROOT=Path(__file__).resolve().parents[1]
ORIGIN="https://nextgen-buildingsolutions.com"
REPORT=ROOT/".ci-artifacts/lot103-live-fullsite-readonly.json"
ROUTES={
    "catalogue":("data-catalogue-search=",50),
    "a-propos":('class="industrial-step"',3),
    "contact":('class="contact-channel"',3),
}
FAVICON="/favicon.svg"
FAVICON_LINK='<link rel="icon" type="image/svg+xml" href="/favicon.svg"'

def inspect_page(lang:str,section:str,marker:str,expected_count:int)->dict:
    url=f"{ORIGIN}/{lang}/{section}/?verification=lot103-20261106"
    meta,body=inspect_url(url)
    content=html.unescape(body.decode("utf-8",errors="replace")) if meta["status"]==200 else ""
    count=content.count(marker)
    favicon=FAVICON_LINK in content
    noindex='noindex,nofollow' in content
    no_form="<form" not in content
    good=(meta["status"]==200 and not meta.get("oversized") and
          count==expected_count and favicon and noindex and no_form)
    return {"lang":lang,"section":section,"url":url,
            "http":meta["status"],"matching_elements":count,"expected":expected_count,
            "favicon_declared":favicon,"noindex":noindex,"no_form":no_form,
            "visible_and_consistent":good}

def check_once()->dict:
    icon_meta,icon_data=inspect_url(ORIGIN+FAVICON+"?verification=lot103-20261106")
    expected=(ROOT/"public"/"favicon.svg").read_bytes()
    icon_match=(icon_meta["status"]==200 and not icon_meta.get("oversized") and
                hashlib.sha256(icon_data).digest()==hashlib.sha256(expected).digest())
    pages=[inspect_page(lang,route,marker,count)
           for lang in ("fr","ar","en")
           for route,(marker,count) in ROUTES.items()]
    ok=icon_match and all(p["visible_and_consistent"] for p in pages)
    return {
        "checked_utc":datetime.now(timezone.utc).isoformat(),
        "origin":ORIGIN,"favicon_http":icon_meta["status"],
        "favicon_matches_source_sha256":icon_match,
        "pages":pages,"public_routes_verified":ok,
        "exact_cloudflare_commit_verified":False,
        "read_only":True,"deployment_performed":False,
    }

def main()->int:
    latest={}
    for attempt in range(3):
        latest=check_once()
        latest["attempt"]=attempt+1
        if latest["public_routes_verified"]:
            break
        if attempt<2:
            time.sleep(15)
    latest["expected_main_sha"]=os.environ.get("GITHUB_SHA","unavailable")
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text(json.dumps(latest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(latest,indent=2,ensure_ascii=False))
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"],"a",encoding="utf-8") as out:
            out.write("\n## Lot 103 — contrôle public en lecture seule\n\n")
            out.write("| Langue | Page | HTTP | Éléments | Conforme |\n|---|---|---:|---:|---|\n")
            for p in latest["pages"]:
                out.write(f"| {p['lang']} | {p['section']} | {p['http']} | {p['matching_elements']} | {p['visible_and_consistent']} |\n")
            out.write(f"\nFavicon SHA-256 correct : {latest['favicon_matches_source_sha256']}. "
                      "Aucun déploiement ni preuve du SHA Cloudflare.\n")
    return 0 if latest["public_routes_verified"] else 1

if __name__=="__main__":
    raise SystemExit(main())
