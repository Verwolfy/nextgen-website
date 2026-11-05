#!/usr/bin/env python3
"""Lot 100 — audit compiled multilingual catalogue search attributes, read-only.

Full cross-language terms are preserved, but exact duplicate whitespace tokens
must not be repeated in every card's HTML attribute. No user data or network.
"""
from __future__ import annotations

import gzip
import json
import os
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / ".ci-artifacts" / "lot100-catalogue-index.json"

class CatalogueParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.indexes: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        attrs_dict = dict(attrs)
        if "data-catalogue-search" in attrs_dict:
            self.indexes.append(attrs_dict["data-catalogue-search"] or "")


def report_catalogue(root: Path = ROOT) -> dict:
    data = {"checked_utc": datetime.now(timezone.utc).isoformat(),
            "scope": "Local built HTML attributes, not network bytes or real-user metrics",
            "pages": {}}
    for lang in ("fr", "ar", "en"):
        page = root / "dist" / lang / "catalogue" / "index.html"
        raw = page.read_bytes()
        parser = CatalogueParser()
        parser.feed(raw.decode("utf-8"))
        indexes = parser.indexes
        counts = [len(x.split()) for x in indexes]
        repeated = [len(words) - len(set(words)) for x in indexes if (words := x.split())]
        data["pages"][lang] = {
            "cards": len(indexes),
            "html_source_bytes": len(raw),
            "html_gzip_estimate_bytes": len(gzip.compress(raw, compresslevel=9)),
            "search_index_characters": sum(len(x) for x in indexes),
            "search_index_utf8_bytes": sum(len(x.encode("utf-8")) for x in indexes),
            "total_word_occurrences": sum(counts),
            "repeated_words": sum(repeated),
            "unique_index_count": len(set(indexes)),
        }
    data["safe"] = all(p["cards"] == 50 and p["repeated_words"] == 0 and
                        p["unique_index_count"] == 50 for p in data["pages"].values())
    return data


def main() -> int:
    result = report_catalogue()
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as out:
            out.write("\n## Lot 100 — Index de recherche catalogue FR/AR/EN\n\n")
            out.write("| Langue | Références | Index (octets) | HTML gzip estimé | Doublons |\n")
            out.write("|---|---:|---:|---:|---:|\n")
            for lang, page in result["pages"].items():
                out.write(f"| {lang} | {page['cards']} | {page['search_index_utf8_bytes']} | {page['html_gzip_estimate_bytes']} | {page['repeated_words']} |\n")
            out.write("\nTaille du HTML compilé, pas un temps LCP réel.\n")
    return 0 if result["safe"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
