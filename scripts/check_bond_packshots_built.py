#!/usr/bin/env python3
"""Fail-closed gate for the 10 FENEK-BOND product-specific concept packshots.

Without uploaded assets this prints an explicit SKIP, with the safe generic
fallback preserved. With ANY uploaded asset, all 20 exact approved WebPs must
be present and built into all 3 localized catalogue pages and 36 detail pages.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public/images/catalogue-projects"
DIST = ROOT / "dist"
INSTALLER = ROOT / "scripts/install_bond_packshots.py"


def load_installer():
    spec = importlib.util.spec_from_file_location("bond_packshots_installer", INSTALLER)
    assert spec and spec.loader, "Missing packshot installer"
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def check() -> None:
    mod = load_installer()
    expected = mod.expected_files()
    assert len(expected) == 20

    actual = {str(path.relative_to(ROOT)) for path in PUBLIC.glob("fenek-bond-*.webp")} if PUBLIC.exists() else set()
    if not actual:
        print("SKIP: 0/20 FENEK-BOND packshots uploaded; generic 3D placeholders remain in use")
        # An obsolete build directory must never be mistaken for a verified upload.
        assert not list((DIST / "images/catalogue-projects").glob("fenek-bond-*.webp")), (
            "Stale packshots in dist despite no source assets"
        )
        return

    assert actual == set(expected), (
        "Incomplete or unexpected packshots: "
        f"missing={sorted(set(expected) - actual)} unexpected={sorted(actual - set(expected))}"
    )
    mod.verify_installed()  # SHA256, VP8 dimensions and source size
    assert DIST.is_dir(), "Run npm run build before checking assets"
    for relative, (digest, dims) in expected.items():
        generated = DIST / Path(relative).relative_to("public")
        assert generated.is_file(), "WebP not copied by Astro build: " + relative
        mod.verify_asset(relative, generated.read_bytes(), digest, dims)

    slugs = sorted(mod.approved_assets()[1])
    assert len(slugs) == 10
    for lang in ("fr", "ar", "en"):
        catalogue = DIST / lang / "catalogue/index.html"
        html = catalogue.read_text(encoding="utf-8")
        for slug in slugs:
            card_url = f"/images/catalogue-projects/{slug}-card.webp"
            assert card_url in html, f"Card not rendered: {lang}, {slug}"
            detail = DIST / lang / "catalogue" / slug / "index.html"
            assert detail.is_file(), f"Missing localized detail: {lang}/{slug}"
            body = detail.read_text(encoding="utf-8")
            full_url = f"/images/catalogue-projects/{slug}.webp"
            assert full_url in body, f"Specific packshot not rendered: {lang}/{slug}"
            assert "concept-detail-note" in body, f"Missing non-contractual notice: {lang}/{slug}"

    print("PASS: 20/20 verified images and 60/60 localized uses (10 cards × 3 + 10 details × 3)")


if __name__ == "__main__":
    check()
