#!/usr/bin/env python3
"""Lot 120: public, read-only NextGen search journey against deployed Cloudflare.

Requires Playwright Python and Chromium, installed only in GitHub Actions.
No Supabase client, Cloudflare token, real form submissions, or persistence.
"""
from __future__ import annotations

import argparse
from urllib.parse import urlsplit
from playwright.sync_api import sync_playwright

LANGS = ("fr", "ar", "en")
EXPECTED_LABELS = {"fr": "Rechercher", "ar": "بحث", "en": "Search"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--origin", default="https://nextgen-buildingsolutions.com")
    args = ap.parse_args()
    base = args.origin.rstrip("/")
    parsed = urlsplit(base)
    assert parsed.scheme == "https" and parsed.netloc and not parsed.path, "Invalid HTTPS origin"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        try:
            for lang in LANGS:
                for width in (390, 1440):
                    page = browser.new_page(
                        viewport={"width": width, "height": 850},
                        reduced_motion="reduce",
                    )
                    requests = []
                    page.on("request", lambda req: requests.append(req.url))
                    try:
                        response = page.goto(
                            f"{base}/{lang}/", wait_until="domcontentloaded", timeout=30000
                        )
                        assert response is not None and response.status == 200, (lang, width)
                        assert page.locator("html").get_attribute("lang") == lang
                        trigger = page.locator("[data-search-trigger]")
                        panel = page.locator("[data-search-panel]")
                        label = trigger.locator(".ng-search-trigger-label")
                        assert trigger.is_visible() and panel.is_hidden(), (lang, width)
                        assert EXPECTED_LABELS[lang] == label.inner_text().strip(), (lang, width)
                        assert label.is_visible() == (width == 1440), (lang, width)
                        assert page.evaluate("document.documentElement.scrollWidth-innerWidth") <= 4, (lang, width)
                        trigger.click()
                        assert panel.is_visible() and trigger.get_attribute("aria-expanded") == "true"
                        field = panel.locator("[data-search-input]")
                        assert field.evaluate("el => el === document.activeElement")
                        field.fill("C1T")
                        panel.locator("[data-search-filter='product']").click()
                        result = panel.locator(
                            f"a.ng-search-result[href='/{lang}/catalogue/fenek-bond-c1t/']"
                        )
                        result.wait_for(state="visible", timeout=30000)
                        assert result.inner_text().strip(), (lang, width)
                        assert any("/pagefind/" in url for url in requests), (lang, "Pagefind not loaded")
                        assert not any("supabase.co" in url for url in requests), (lang, "unexpected DB request")
                        page.keyboard.press("Escape")
                        assert panel.is_hidden() and trigger.get_attribute("aria-expanded") == "false"
                        if width == 1440:
                            positions = [x.bounding_box() for x in page.locator(".header .nav a").all()]
                            assert positions and all(x for x in positions)
                            assert max(x["y"] for x in positions) - min(x["y"] for x in positions) <= 4, \
                                (lang, "desktop menu wrapped")
                        print(f"PASS live Chromium: {lang} {width}px, search C1T / Pagefind / keyboard")
                    finally:
                        page.close()
        finally:
            browser.close()


if __name__ == "__main__":
    main()
