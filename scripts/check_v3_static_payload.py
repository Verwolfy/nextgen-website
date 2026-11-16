#!/usr/bin/env python3
"""Lot 93 — report static payload budgets; not a Lighthouse or field CWV measurement.

Only local build artifacts and images are read. No network, no deployment and no
unapproved technical content. Retains the previous Nexo/Geno size ceilings.
"""
from __future__ import annotations
import gzip
import json
import os
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/".ci-artifacts/lot93-v3-static-payload.json"
VIDEO=ROOT/"public/videos/nextgen-nexo-geno-welcome.mp4"
POSTER=ROOT/"public/videos/nextgen-nexo-geno-poster.webp"
V3=ROOT/"src/styles/v3.css"

LIMITS={"video_bytes":250*1024, "poster_bytes":30*1024, "v3_css_source_bytes":24*1024}

def static_report(root:Path=ROOT)->dict:
    video=root/"public/videos/nextgen-nexo-geno-welcome.mp4"
    poster=root/"public/videos/nextgen-nexo-geno-poster.webp"
    css=root/"src/styles/v3.css"
    media={"video_bytes":video.stat().st_size,
           "poster_bytes":poster.stat().st_size,
           "v3_css_source_bytes":css.stat().st_size}
    image_dir=root/"public/images/illustrations/produits"
    images=list(image_dir.glob("*.webp"))
    result={
      "checked_utc":datetime.now(timezone.utc).isoformat(),
      "source_media":media,
      "source_limits":LIMITS,
      "source_limits_pass":all(media[key]<=size for key,size in LIMITS.items()),
      "packshot_webp_files":len(images),
      "packshot_webp_total_bytes":sum(p.stat().st_size for p in images),
      "packshot_largest":[{"path":str(p.relative_to(root)),"bytes":p.stat().st_size}
                           for p in sorted(images,key=lambda p:p.stat().st_size,reverse=True)[:5]],
      "metric_scope":"Static file weights only; not Lighthouse, LCP, INP or CLS",
    }
    dist=root/"dist"
    if dist.exists():
        def page(lang:str)->dict:
            file=dist/lang/"index.html"
            content=file.read_bytes()
            return {"bytes":len(content),"gzip_bytes":len(gzip.compress(content,compresslevel=9))}
        css_files=list((dist/"_astro").glob("*.css"))
        result["built_homepages"]={lang:page(lang) for lang in ("fr","ar","en")}
        result["built_css_files"]=len(css_files)
        result["built_css_total_bytes"]=sum(p.stat().st_size for p in css_files)
        result["built_css_total_gzip_bytes"]=sum(
           len(gzip.compress(p.read_bytes(),compresslevel=9)) for p in css_files)
    return result

def main()->int:
    result=static_report()
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False,indent=2))
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"],"a",encoding="utf-8") as out:
            out.write("\n## Lot 93 — Budgets statiques V3 (pas un Lighthouse)\n\n")
            for key,size in result["source_media"].items():
                out.write(f"- {key}: {size} / {LIMITS[key]} octets\n")
            out.write(f"- Budgets source respectés : **{result['source_limits_pass']}**\n")
            if "built_css_total_gzip_bytes" in result:
                out.write(f"- CSS Astro gzip cumulé : **{result['built_css_total_gzip_bytes']} octets**\n")
            out.write("- Les métriques LCP/INP/CLS nécessitent des mesures navigateur dédiées.\n")
    return 0 if result["source_limits_pass"] else 1

if __name__=="__main__":
    raise SystemExit(main())
