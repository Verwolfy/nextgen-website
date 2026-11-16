#!/usr/bin/env python3
"""Lot 80: verify manufacturing approach on the public domain, read-only.

No Cloudflare credentials, no deployment, no authentication or redirected GET.
A matching section and SVG hashes prove served content, not a deployed Git SHA.
"""
from __future__ import annotations
import hashlib
import html
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
import sys
if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.check_live_video_deployment import inspect_url

ROOT=Path(__file__).resolve().parents[1]
ORIGIN="https://nextgen-buildingsolutions.com"
PAGES={
    "fr":("Notre démarche industrielle", "Concevoir pour le terrain",
          "Produire avec méthode", "Distribuer et accompagner"),
    "ar":("منهجيتنا الصناعية", "تصميم حلول للميدان",
          "تصنيع بمنهجية واضحة", "التوزيع والمرافقة"),
    "en":("Our manufacturing approach", "Design for the jobsite",
          "Manufacture with purpose", "Distribute and support"),
}
ASSETS=("01-concevoir.svg", "02-produire.svg", "03-distribuer.svg")
REPORT=ROOT/".ci-artifacts/lot80-public-demarche.json"


def audit_page(lang:str)->dict:
    url=f"{ORIGIN}/{lang}/a-propos/?verification=lot80-20261105"
    meta,body=inspect_url(url)
    text=html.unescape(body.decode("utf-8", errors="replace")) if meta["status"]==200 else ""
    markers={s:s in text for s in PAGES[lang]}
    picture_paths={f"/images/illustrations/approche/{s}":f"/images/illustrations/approche/{s}" in text for s in ASSETS}
    noindex="noindex,nofollow" in text
    return {"lang":lang, "url":url, "http":meta["status"],
            "result":"new_content_visible" if meta["status"]==200
                      and not meta.get("oversized") and all(markers.values())
                      and all(picture_paths.values()) and noindex
                      else "content_not_confirmed",
            "markers":markers, "images_referenced":picture_paths, "noindex":noindex}


def audit_asset(asset:str)->dict:
    url=f"{ORIGIN}/images/illustrations/approche/{asset}?verification=lot80-20261105"
    meta,body=inspect_url(url)
    expected=(ROOT/"public/images/illustrations/approche"/asset).read_bytes()
    match=meta["status"]==200 and not meta.get("oversized") and hashlib.sha256(body).digest()==hashlib.sha256(expected).digest()
    return {"asset":asset,"http":meta["status"],"sha256_matches_source":match}


def audit_once()->dict:
    pages=[audit_page(lang) for lang in ("fr","ar","en")]
    # Query binary assets only once all three pages identify the new content.
    assets=[audit_asset(s) for s in ASSETS] if all(
        p["result"]=="new_content_visible" for p in pages) else []
    return {"checked_utc":datetime.now(timezone.utc).isoformat(),
            "origin":ORIGIN,
            "pages":pages, "assets":assets,
            "new_industrial_section_verified":len(assets)==len(ASSETS)
              and all(a["sha256_matches_source"] for a in assets),
            "release_commit_exactly_verified":False,
            "read_only":True,"deployment_performed":False}


def write_report(result:dict)->None:
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False,indent=2))
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"],"a",encoding="utf-8") as stream:
            stream.write("\n## Lot 80 — Domaine public NextGen (lecture seule)\n\n")
            stream.write("| Langue | HTTP | Nouvelle démarche | noindex |\n|---|---|---|---|\n")
            for p in result["pages"]:
                stream.write(f"| {p['lang']} | {p['http']} | {p['result']} | {p['noindex']} |\n")
            stream.write("\nIllustrations vérifiées : "+str(len(result["assets"]))+"/3\n\n")
            stream.write("**Nouvelle section présente : "+str(result["new_industrial_section_verified"])+"**. "
                         "Ce diagnostic n'effectue aucun déploiement et ne prouve pas le SHA Cloudflare.\n")


def main()->int:
    # The Cloudflare Git integration may still be building after a main push.
    # Retry only anonymous reads, with a bounded 90-second diagnostic window.
    last={}
    for attempt in range(4):
        last=audit_once()
        last["attempt"]=attempt+1
        if last["new_industrial_section_verified"]:
            break
        if attempt<3:
            time.sleep(30)
    last["expected_github_main_sha"]=os.environ.get("GITHUB_SHA","unavailable")
    write_report(last)
    return 0 if last["new_industrial_section_verified"] else 1


if __name__=="__main__":
    raise SystemExit(main())
