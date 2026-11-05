#!/usr/bin/env python3
"""Lots 95-97: synthetic LOCAL Chromium baseline, not real-user Core Web Vitals.

Reads only locally built Astro dist pages; no external network or deployment.
LCP/CLS samples are unthrottled CI diagnostics, never a performance claim.
"""
from __future__ import annotations

import gzip
import json
import os
from datetime import datetime, timezone
from functools import partial
from http.server import ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.parse import urlparse
import sys

ROOT = Path(__file__).resolve().parents[1]
if __package__ in (None, ''):
    sys.path.insert(0, str(ROOT))

from playwright.sync_api import sync_playwright
from scripts.check_browser_pages import SilentHandler
DIST = ROOT / "dist"
REPORT = ROOT / ".ci-artifacts" / "lot95-97-browser-metrics.json"

SCENARIOS = (
    ("fr-home-mobile", "/fr/", 390, 844),
    ("ar-home-mobile", "/ar/", 390, 844),
    ("en-home-mobile", "/en/", 390, 844),
    ("fr-home-320", "/fr/", 320, 720),
    ("fr-home-desktop", "/fr/", 1280, 900),
    ("fr-catalogue-mobile", "/fr/catalogue/", 390, 844),
    ("fr-ep-anc-desktop", "/fr/catalogue/fenek-proof-ep-anc/", 1280, 900),
    ("ar-contact-mobile", "/ar/contact/", 390, 844),
)

INIT_SCRIPT = r"""
window.__v3Metrics = { lcp_ms: null, cls: 0, lcp_tag: null };
try {
  new PerformanceObserver(list => {
    for (const entry of list.getEntries()) {
      window.__v3Metrics.lcp_ms = Math.round(entry.startTime);
      window.__v3Metrics.lcp_tag = entry.element?.tagName || null;
    }
  }).observe({type: 'largest-contentful-paint', buffered: true});
} catch {}
try {
  new PerformanceObserver(list => {
    for (const entry of list.getEntries()) {
      if (!entry.hadRecentInput) window.__v3Metrics.cls += entry.value || 0;
    }
  }).observe({type: 'layout-shift', buffered: true});
} catch {}
"""

READ_SCRIPT = r"""() => {
 const nav = performance.getEntriesByType('navigation')[0];
 const resources = performance.getEntriesByType('resource');
 const videoRequests = resources.filter(x => x.name.includes('nextgen-nexo-geno-welcome.mp4'));
 return {
   lcp_ms: window.__v3Metrics?.lcp_ms ?? null,
   lcp_element: window.__v3Metrics?.lcp_tag ?? null,
   cls_observed: Number((window.__v3Metrics?.cls ?? 0).toFixed(5)),
   navigation_response_start_ms: nav ? Math.round(nav.responseStart) : null,
   dom_content_loaded_ms: nav ? Math.round(nav.domContentLoadedEventEnd) : null,
   load_event_ms: nav ? Math.round(nav.loadEventEnd) : null,
   local_resource_count: resources.length,
   video_request_count: videoRequests.length,
   images_in_dom: document.images.length,
   lazy_images_in_dom: document.querySelectorAll('img[loading="lazy"]').length,
   rtl: document.documentElement.dir === 'rtl',
   overflow_px: Math.max(0, Math.ceil(document.documentElement.scrollWidth - innerWidth))
 };
}"""

def local_browser_report() -> dict:
    if not (DIST / "fr/index.html").is_file():
        raise FileNotFoundError("Astro dist/ missing; run npm run build first")
    server = ThreadingHTTPServer(
        ("127.0.0.1", 0), partial(SilentHandler, directory=str(DIST)))
    Thread(target=server.serve_forever, daemon=True).start()
    origin = "http://127.0.0.1:" + str(server.server_address[1])
    results = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True,
                         args=["--no-sandbox","--disable-dev-shm-usage"])
            try:
                for label, route, width, height in SCENARIOS:
                    page = browser.new_page(
                        viewport={"width":width,"height":height},
                        device_scale_factor=1,
                        reduced_motion="reduce",
                    )
                    try:
                        # Only local files are allowed during the benchmark.
                        page.route("**/*", lambda req: (
                            req.continue_() if urlparse(req.request.url).netloc ==
                               urlparse(origin).netloc else req.abort()))
                        page.add_init_script(script=INIT_SCRIPT)
                        response = page.goto(origin+route, wait_until="load", timeout=20000)
                        page.wait_for_timeout(600)
                        vals = page.evaluate(READ_SCRIPT)
                        results.append({
                            "scenario":label,"route":route,"viewport_px":width,
                            "status":response.status if response else None,
                            **vals,
                        })
                    finally:
                        page.close()
            finally:
                browser.close()
    finally:
        server.shutdown()
        server.server_close()
    css_files=list((DIST/"_astro").glob("*.css"))
    return {
      "timestamp_utc":datetime.now(timezone.utc).isoformat(),
      "scope":"Synthetic local Chromium, unthrottled, reduced-motion; NOT field LCP/CLS/INP or Lighthouse",
      "motion_mode":"prefers-reduced-motion: reduce",
      "external_network_used":False,
      "is_deployment":False,
      "css_compiled_file_count":len(css_files),
      "css_compiled_bytes":sum(p.stat().st_size for p in css_files),
      "css_compiled_gzip_estimate_bytes":sum(
         len(gzip.compress(p.read_bytes(),compresslevel=9)) for p in css_files),
      "scenarios":results,
    }

def main() -> int:
    result=local_browser_report()
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False,indent=2))
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"],"a",encoding="utf-8") as out:
            out.write("\n## Lots 95–97 — Baseline navigateur local V3 (indicatif)\n\n")
            out.write("| Scénario | LCP synth. (ms) | CLS observé | Débordement (px) | Vidéo demandée |\n")
            out.write("|---|---:|---:|---:|---:|\n")
            for x in result["scenarios"]:
                out.write(f"| {x['scenario']} | {x['lcp_ms']} | {x['cls_observed']} | {x['overflow_px']} | {x['video_request_count']} |\n")
            out.write("\n**Ces mesures locales ne sont pas des métriques terrain ni un score Lighthouse.**\n")
    # Only structural regressions block the CI; no fabricated CWV performance SLA.
    return 0 if all(x["status"]==200 and x["overflow_px"]<=4
                    and x["video_request_count"]==0
                    for x in result["scenarios"]) else 1

if __name__=="__main__":
    raise SystemExit(main())
