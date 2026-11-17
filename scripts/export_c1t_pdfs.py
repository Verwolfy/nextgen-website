#!/usr/bin/env python3
"""Export four BOND pilots as trilingual presentation sheets from the exact built Astro pages.

This produces product INFORMATION sheets, not laboratory-approved TDS or SDS.
Usage:
    npm run build
    python -m pip install -r requirements-supports.txt
    python scripts/export_c1t_pdfs.py
    npm run build  # includes generated PDFs from public/ in dist/
"""
from __future__ import annotations

import argparse
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://nextgen-buildingsolutions.com"
LANGUAGES = ("fr", "ar", "en")
PILOT_SLUGS = ("fenek-bond-c1t", "fenek-bond-c1te", "fenek-bond-c2ft", "fenek-bond-c2te", "fenek-bond-c2te-s1")


def local_fetcher(dist: Path):
    """Serve ONLY Astro build assets locally, never access the network."""
    from weasyprint import default_url_fetcher

    def fetch(url: str, **kwargs):
        parts = urlsplit(url)
        if parts.scheme == "data":
            return default_url_fetcher(url, **kwargs)
        if parts.scheme == "file":
            resource = Path(unquote(parts.path)).resolve()
        elif parts.scheme == "https" and parts.netloc == "nextgen-buildingsolutions.com":
            resource = (dist / unquote(parts.path).lstrip("/")).resolve()
        else:
            raise ValueError("External resource forbidden during PDF generation: " + url)
        if not resource.is_relative_to(dist) or not resource.is_file():
            raise ValueError("Missing or unsafe built asset: " + parts.path)
        return default_url_fetcher(resource.as_uri(), **kwargs)

    return fetch


def export_pdfs(dist: Path, output: Path) -> list[Path]:
    dist = dist.resolve()
    output = output.resolve()
    if not dist.is_dir():
        raise RuntimeError("Missing dist/: run npm run build first")
    try:
        from weasyprint import HTML
    except ImportError as exc:
        raise RuntimeError("Install requirements-supports.txt before exporting PDFs") from exc
    output.mkdir(parents=True, exist_ok=True)
    generated: list[Path] = []
    for slug in PILOT_SLUGS:
        suffix = slug.rsplit("-", 1)[-1]
        for lang in LANGUAGES:
            file = dist / lang / "documentation" / slug / "index.html"
            if not file.is_file():
                raise RuntimeError(f"Missing built pilot sheet: {file}")
            markup = file.read_text(encoding="utf-8")
            if f'data-{suffix}-pilot' not in markup or f'fenek-{suffix}-print' not in markup:
                raise RuntimeError(f"Expected {suffix.upper()} presentation structure missing: {lang}")
            target = output / f"{slug}-{lang}.pdf"
            HTML(string=markup, base_url=ORIGIN + "/", url_fetcher=local_fetcher(dist)).write_pdf(target)
            if not target.read_bytes().startswith(b"%PDF-"):
                raise RuntimeError(f"Invalid generated PDF: {target}")
            generated.append(target)
    return generated


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, default=ROOT / "dist")
    parser.add_argument("--output", type=Path, default=ROOT / "public/docs/fiches")
    args = parser.parse_args()
    for path in export_pdfs(args.dist, args.output):
        print(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path)


if __name__ == "__main__":
    main()
