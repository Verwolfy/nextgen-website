#!/usr/bin/env python3
"""Lot 120: read-only Cloudflare Pages production release and content smoke test.

Checks exact Git commit via the build-time public /deployment.json marker, then
public localized pages, signature capsule, Pagefind index, and privacy guards.
No Cloudflare token, Supabase access, POST request, or state-changing action.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

LANGS = ("fr", "ar", "en")
LABELS = {"fr": "Rechercher", "ar": "بحث", "en": "Search"}
EXPECTED_DIR = {"fr": "ltr", "ar": "rtl", "en": "ltr"}
CATEGORY_ROUTES = {
    "product": "catalogue/fenek-bond-c1t/",
    "sheet": "documentation/fenek-bond-c1t/",
    "application": "gammes/bond/",
}
MAX_BYTES = 4 * 1024 * 1024
BRAND_MEDIA = {
    "/videos/nextgen-header-logo-v1.mp4":
        "ae3ec46c8123065c3178f0543de93ba8d1d8a8a646dff0a22c8bd4f1e277f116",
    "/videos/nextgen-header-logo-v1.webm":
        "08162155ad64397604bbcd81befafec000b39f6c190999542a2788dd41bfb94d",
    "/images/nextgen-header-logo-poster-v1.webp":
        "a35f94aefd101087cc9a1609935790d1b64b79c938d782cb363ebe783753a60a",
}

# Lot 124 — final About video: exact public binary assets, never interim media.
ABOUT_MEDIA = {
    "/videos/nextgen-about-v2.mp4":
        "e322aaf485a24fa3a6c8705077161616f0c129e34da8cd771f5a6f2e0605a17a",
    "/videos/nextgen-about-v2.webm":
        "0c1d040f7984b3877c0c483780e70128cc5ac57eeed5cf8ef06da9378b2a908d",
    "/videos/nextgen-about-v2-poster.webp":
        "b5ebd897a82c0e3c8b7d6668fcdd4dc9432911db187ef1d04d543439cf9a5936",
}


def fetch(origin: str, path: str, timeout: float) -> bytes:
    """HTTP GET only: predictable public origin and bounded body."""
    assert origin.startswith("https://") and path.startswith("/")
    request = Request(
        origin.rstrip("/") + path,
        headers={
            "User-Agent": "NextGen-LiveSmoke/1.0 (+GitHub-Actions)",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
        },
        method="GET",
    )
    with urlopen(request, timeout=timeout) as response:
        if response.status != 200:
            raise AssertionError(f"{path}: unexpected HTTP {response.status}")
        final = urlsplit(response.geturl())
        if final.scheme != "https" or final.netloc != urlsplit(origin).netloc:
            raise AssertionError(f"{path}: unexpected redirect to {final.netloc}")
        result = response.read(MAX_BYTES + 1)
        if len(result) > MAX_BYTES:
            raise AssertionError(f"{path}: body larger than {MAX_BYTES} bytes")
        return result


def validate_marker(raw: bytes, expected_sha: str) -> str:
    """Do not accept an outdated Cloudflare deployment as a successful release."""
    data = json.loads(raw.decode("utf-8"))
    if not isinstance(data, dict) or data.get("application") != "nextgen-website":
        raise AssertionError("Missing NextGen deployment identity")
    commit = data.get("commit", "")
    if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise AssertionError("Missing /deployment.json commit SHA")
    if data.get("branch") != "main":
        raise AssertionError("Production marker must belong to main")
    if commit != expected_sha.lower():
        raise AssertionError(f"Cloudflare serves {commit[:10]}, waiting for {expected_sha[:10]}")
    return commit


class PageMarkup(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.lang = ""
        self.direction = ""
        self.main_kind = []
        self.triggers = []
        self.panels = []
        self.inputs = []
        self.labels = []
        self._in_label = False
        self.form_count = 0
        self.robots = ""

    def handle_starttag(self, tag, pairs) -> None:
        attrs = dict(pairs)
        if tag == "html":
            self.lang, self.direction = attrs.get("lang", ""), attrs.get("dir", "")
        if tag == "main" and "data-pagefind-body" in attrs:
            self.main_kind.append(attrs.get("data-pagefind-filter"))
        if tag == "button" and "data-search-trigger" in attrs:
            self.triggers.append(attrs)
        if tag == "div" and "data-search-panel" in attrs:
            self.panels.append(attrs)
        if tag == "input" and "data-search-input" in attrs:
            self.inputs.append(attrs)
        if tag == "span" and "ng-search-trigger-label" in (attrs.get("class") or "").split():
            self._in_label = True
        if tag == "meta" and attrs.get("name") == "robots":
            self.robots = attrs.get("content", "")
        if tag == "form":
            self.form_count += 1

    def handle_endtag(self, tag) -> None:
        if tag == "span" and self._in_label:
            self._in_label = False

    def handle_data(self, data: str) -> None:
        if self._in_label:
            self.labels.append(data.strip())


def validate_html(raw: bytes, lang: str, kind: str = "page") -> None:
    text = raw.decode("utf-8")
    html = PageMarkup()
    html.feed(text)
    assert html.lang == lang and html.direction == EXPECTED_DIR[lang], (lang, "language/RTL")
    assert html.main_kind == [f"kind:{kind}"], (lang, kind, html.main_kind)
    assert len(html.triggers) == len(html.panels) == len(html.inputs) == 1, (lang, "search UI")
    assert html.triggers[0].get("aria-expanded") == "false", (lang, "expanded default")
    assert "hidden" in html.panels[0], (lang, "hidden initial panel")
    assert html.inputs[0].get("type") == "search", (lang, "search input")
    assert LABELS[lang] in html.labels, (lang, "localized capsule", html.labels)
    assert "ng-search-signal" in text, (lang, "signature signal")
    assert html.robots.startswith("noindex"), (lang, "SEO guard")
    assert html.form_count == 0, (lang, "no lead collection")
    assert "SUPABASE_SERVICE_ROLE_KEY" not in text, (lang, "no secret exposure")


def verify_content(origin: str, timeout: float) -> None:
    """Verify publicly accessible content, never private Supabase source."""
    for lang in LANGS:
        homepage = fetch(origin, f"/{lang}/", timeout)
        validate_html(homepage, lang)
        text = homepage.decode("utf-8")
        for asset in BRAND_MEDIA:
            if asset not in text:
                raise AssertionError(f"/{lang}/: missing animated logo asset {asset}")
        if "data-header-brand" not in text or "data-header-brand-video" not in text:
            raise AssertionError(f"/{lang}/: missing accessible animated header logo")
        print(f"PASS /{lang}/ : local search, animated brand, Pagefind scope, noindex")
        for kind, suffix in CATEGORY_ROUTES.items():
            validate_html(fetch(origin, f"/{lang}/{suffix}", timeout), lang, kind)
        print(f"PASS /{lang}/ : product, application and sheet routes")

    # About video is the newest user-supplied 10s presentation.
    for lang in LANGS:
        html = fetch(origin, f"/{lang}/a-propos/", timeout)
        validate_html(html, lang)
        page = html.decode("utf-8")
        for asset in ABOUT_MEDIA:
            if asset not in page:
                raise AssertionError(f"/{lang}/a-propos/: missing final About media {asset}")
        if 'data-about-video-version="v2"' not in page:
            raise AssertionError(f"/{lang}/a-propos/: interim About video still in use")
    print("PASS About video v2 in FR/AR/EN, safe initial noindex")

    for asset, digest in ABOUT_MEDIA.items():
        public_bytes = fetch(origin, asset, timeout)
        if hashlib.sha256(public_bytes).hexdigest() != digest:
            raise AssertionError(f"Live optimized final About media altered: {asset}")
    print("PASS final About MP4 and poster WebP (exact SHA256)", flush=True)

    js = fetch(origin, "/pagefind/pagefind.js", timeout)
    assert len(js) > 100 and b"<html" not in js[:300].lower(), "Missing Pagefind runtime"
    entry = json.loads(fetch(origin, "/pagefind/pagefind-entry.json", timeout))
    languages = entry.get("languages")
    assert isinstance(languages, (dict, list)), "Missing Pagefind language manifest"
    assert set(LANGS).issubset(set(languages)), "Incomplete FR/AR/EN Pagefind index"
    print("PASS Pagefind runtime and FR/AR/EN index")

    for asset, digest in BRAND_MEDIA.items():
        public_bytes = fetch(origin, asset, timeout)
        if hashlib.sha256(public_bytes).hexdigest() != digest:
            raise AssertionError(f"Live NextGen animated-logo asset altered: {asset}")
    print("PASS optimized MP4/WebM/WebP assets (exact SHA256)", flush=True)

    products = json.loads(fetch(origin, "/data/products.json", timeout))
    assert products == [], "Unpublished product data unexpectedly accessible"
    robots = fetch(origin, "/robots.txt", timeout).decode("utf-8")
    assert "Disallow: /" in robots, "robots.txt publication guard changed"
    print("PASS privacy guards (no products, noindex)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--origin", default="https://nextgen-buildingsolutions.com")
    parser.add_argument("--expected-sha", required=True)
    parser.add_argument("--attempts", type=int, default=24)
    parser.add_argument("--interval", type=float, default=20)
    parser.add_argument("--timeout", type=float, default=15)
    args = parser.parse_args()
    assert re.fullmatch(r"[0-9a-f]{40}", args.expected_sha.lower()), "Invalid expected SHA"
    assert args.attempts >= 1 and 0 <= args.interval <= 60 and 0 < args.timeout <= 30
    parsed = urlsplit(args.origin)
    assert parsed.scheme == "https" and parsed.netloc and not parsed.path.rstrip("/"), "HTTPS origin required"
    origin = args.origin.rstrip("/")

    for attempt in range(1, args.attempts + 1):
        try:
            current = validate_marker(
                fetch(origin, "/deployment.json", args.timeout),
                args.expected_sha.lower(),
            )
            print(f"PASS Cloudflare deployment: {current} ({attempt}/{args.attempts})")
            break
        except (AssertionError, HTTPError, URLError, ValueError, TimeoutError, OSError) as exc:
            print(f"Cloudflare not ready ({attempt}/{args.attempts}): {exc}", flush=True)
            if attempt == args.attempts:
                raise AssertionError("Latest main commit not yet live on Cloudflare") from exc
            time.sleep(args.interval)

    verify_content(origin, args.timeout)
    print("PASS LIVE NextGen production checks; no Cloudflare or database mutations")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, ValueError, HTTPError, URLError, TimeoutError, OSError) as exc:
        print(f"FAIL NextGen production smoke: {exc}", file=sys.stderr)
        sys.exit(1)
