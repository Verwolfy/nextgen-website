#!/usr/bin/env python3
"""Lot 98-99 — summarize Lighthouse lab diagnostics (never real-user CWV).

Reads local JSON reports only. Scores are informational; no arbitrary thresholds.
Includes source audit links via artifacts and does not upload to external services.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

REPORT_DIR = Path(".ci-artifacts/lighthouse")
SUMMARY = REPORT_DIR / "summary.json"

def summarize(paths: list[Path]) -> dict:
    runs = []
    for path in paths:
        j = json.loads(path.read_text(encoding="utf-8"))
        if j.get("runtimeError"):
            raise ValueError(f"Lighthouse runtime error in {path.name}: {j['runtimeError']}")
        categories = j.get("categories") or {}
        audits = j.get("audits") or {}
        entry = {
            "scenario": path.stem.replace("lighthouse-", ""),
            "url_path": (j.get("finalDisplayedUrl") or j.get("finalUrl") or "").split("127.0.0.1")[-1],
            "lighthouse_version": j.get("lighthouseVersion"),
            "scores_0_to_100": {
                key: round(100 * categories[key]["score"])
                if categories.get(key) and categories[key].get("score") is not None else None
                for key in ("performance", "accessibility", "best-practices")
            },
            "lab_metrics": {
                label: audits.get(name, {}).get("numericValue")
                for label, name in (
                    ("lcp_ms", "largest-contentful-paint"),
                    ("tbt_ms", "total-blocking-time"),
                    ("cls", "cumulative-layout-shift"),
                    ("fcp_ms", "first-contentful-paint"),
                    ("speed_index_ms", "speed-index"),
                )
            },
            "accessibility_issues": [
                {"id": key, "title": item.get("title"), "score": item.get("score"),
                 "affected": [
                     {"selector": (node.get("node") or {}).get("selector"),
                      "snippet": ((node.get("node") or {}).get("snippet") or "")[:180],
                      "label": ((node.get("node") or {}).get("nodeLabel") or "")[:120]}
                     for node in (item.get("details") or {}).get("items", [])[:12]
                     if node.get("node")
                 ]}
                for key, item in audits.items()
                if item.get("scoreDisplayMode") == "binary"
                and item.get("score") == 0
                and key in (categories.get("accessibility", {}).get("auditRefs") and
                           {x["id"] for x in categories["accessibility"]["auditRefs"]} or set())
            ][:25],
        }
        runs.append(entry)
    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Lighthouse synthetic localhost audit; not real-user INP/LCP/CLS",
        "score_threshold_gate": False,
        "remote_url_audited": False,
        "scenarios": runs,
    }

def main() -> int:
    paths = sorted(REPORT_DIR.glob("lighthouse-*.json"))
    if len(paths) != 4:
        raise RuntimeError(f"Expected four Lighthouse reports, found {len(paths)}")
    result = summarize(paths)
    SUMMARY.write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as out:
            out.write("\n## Lots 98–99 — Lighthouse sur build local (indicateur)\n\n")
            out.write("| Page | Performance | Accessibilité | Bonnes pratiques | LCP labo (ms) | CLS labo |\n")
            out.write("|---|---:|---:|---:|---:|---:|\n")
            for r in result["scenarios"]:
                scores = r["scores_0_to_100"]
                values = r["lab_metrics"]
                out.write(
                    f"| {r['scenario']} | {scores['performance']} | {scores['accessibility']} | "
                    f"{scores['best-practices']} | {values['lcp_ms']} | {values['cls']} |\n")
            out.write("\n**Scores de laboratoire local, pas des Core Web Vitals terrain.** "
                      "Les scores n'empêchent pas la fusion ; les erreurs d'exécution, oui.\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
