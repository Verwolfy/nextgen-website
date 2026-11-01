#!/usr/bin/env python3
"""Cloudflare Pages release candidate checks. Offline. Never publishes or reads secrets."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/"dist"
ROUTES={"version":1,"include":["/api/lead"],"exclude":[]}


def check_release(root:Path=ROOT)->dict:
    dist=root/"dist"
    assert dist.is_dir(), "Run npm run build before release checks"
    node=(root/".node-version").read_text(encoding="utf-8").strip()
    assert node=="22.23.4", "Cloudflare Node version changed; update release checks and CI deliberately"
    source=json.loads((root/"public/_routes.json").read_text(encoding="utf-8"))
    built=json.loads((dist/"_routes.json").read_text(encoding="utf-8"))
    assert source==ROUTES and built==ROUTES, "Cloudflare Function routing must be /api/lead only"
    assert (root/"functions/api/lead.js").is_file(), "Cloudflare Pages Function missing"
    for lang in ("fr","ar","en"):
        assert (dist/lang/"index.html").is_file(), "Localized build missing: "+lang
    assert json.loads((dist/"data/products.json").read_text(encoding="utf-8"))==[], (
        "No unapproved products may be published"
    )
    assert "Disallow: /" in (dist/"robots.txt").read_text(encoding="utf-8")
    headers=(dist/"_headers").read_text(encoding="utf-8")
    assert "X-Robots-Tag: noindex, nofollow, noarchive" in headers
    from html.parser import HTMLParser
    class FormParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.form_count=0
        def handle_starttag(self,tag,attrs):
            if tag=="form": self.form_count+=1
    checked=0
    for html in dist.rglob("*.html"):
        parser=FormParser()
        parser.feed(html.read_text(encoding="utf-8"))
        assert parser.form_count==0, "Active HTML form generated: "+str(html)
        checked+=1
    assert checked>=42, "Not enough verified localized HTML pages"
    api=(root/"functions/api/lead.js").read_text(encoding="utf-8")
    assert "env?.NEXTGEN_LEADS_ENABLED !== 'true'" in api, "API fail-closed guard missing"
    return {"ready_for_pages_build":True,"deploy_performed":False,
            "catalogue_public":False,"forms_active":False,
            "static_pages_checked":checked,"functions_routes":["/api/lead"]}


def main()->None:
    print(json.dumps(check_release(),ensure_ascii=False,sort_keys=True))

if __name__=="__main__":
    main()
