#!/usr/bin/env python3
"""Fail-closed post-build checks for the public-only NextGen Pagefind index."""
from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
LANGS = ("fr", "ar", "en")
CATEGORIES = ("product", "application", "sheet", "page")


class SearchMarkup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.html_lang = None
        self.body_count = 0
        self.kinds = []
        self.triggers = []
        self.panels = []
        self.inputs = []
        self.forms = 0

    def handle_starttag(self, tag, pairs):
        a = dict(pairs)
        if tag == "html":
            self.html_lang = a.get("lang")
        if tag == "main" and "data-pagefind-body" in a:
            self.body_count += 1
            self.kinds.append(a.get("data-pagefind-filter"))
        if tag == "button" and "data-search-trigger" in a:
            self.triggers.append(a)
        if tag == "div" and "data-search-panel" in a:
            self.panels.append(a)
        if tag == "input" and "data-search-input" in a:
            self.inputs.append(a)
        if tag == "form":
            self.forms += 1


def inspect(path: Path, lang: str, expected: str):
    assert path.is_file(), f"Missing localized page: {path}"
    content = path.read_text(encoding="utf-8")
    parsed = SearchMarkup()
    parsed.feed(content)
    assert parsed.html_lang == lang, path
    assert parsed.body_count == 1, f"Missing index scope: {path}"
    assert parsed.kinds == [f"kind:{expected}"], (path, parsed.kinds)
    assert len(parsed.triggers) == len(parsed.panels) == len(parsed.inputs) == 1, path
    assert parsed.triggers[0].get("aria-expanded") == "false", path
    assert parsed.panels[0].get("hidden") is not None or "hidden" in parsed.panels[0], path
    assert parsed.forms == 0, f"Search may not activate any lead form: {path}"
    assert "service_role" not in content and "SUPABASE_SERVICE_ROLE" not in content, path


def main():
    bundle = DIST / "pagefind"
    entry = bundle / "pagefind-entry.json"
    assert (bundle / "pagefind.js").is_file(), "Pagefind JS missing after npm run build"
    assert entry.is_file(), "Pagefind entry metadata missing after npm run build"
    record = json.loads(entry.read_text(encoding="utf-8"))
    languages = record.get("languages")
    assert isinstance(languages, (dict, list)), record
    indexed = set(languages if isinstance(languages, dict) else languages)
    assert set(LANGS).issubset(indexed), f"Incomplete Pagefind locales: {indexed}"
    assert all(any(bundle.glob(f"pagefind.{lang}_*.pf_meta")) for lang in LANGS), \
        "A localized Pagefind metadata bundle is missing"

    for lang in LANGS:
        inspect(DIST / lang / "index.html", lang, "page")
        inspect(DIST / lang / "catalogue" / "fenek-bond-c1t" / "index.html", lang, "product")
        inspect(DIST / lang / "documentation" / "fenek-bond-c1t" / "index.html", lang, "sheet")
        inspect(DIST / lang / "gammes" / "bond" / "index.html", lang, "application")
    print("PASS: Pagefind bundle + FR/AR/EN index + 4 filter kinds + privacy gates")


if __name__ == "__main__":
    main()
