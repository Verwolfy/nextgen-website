#!/usr/bin/env python3
"""Fail-closed gate for the 10 FENEK-BOND product-specific concept packshots.

Without uploaded assets this prints an explicit SKIP, with the safe generic
fallback preserved. With ANY uploaded asset, all 20 exact approved WebPs must
remain byte-verified in the build; ten updated user-provided detailed design images\nare now displayed across all three locales.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public/images/illustrations/catalogue-projects"
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
        print("SKIP: 0/20 FENEK-BOND packshots uploaded; generic placeholder images remain in use")
        # An obsolete build directory must never be mistaken for a verified upload.
        assert not list((DIST / "images/illustrations/catalogue-projects").glob("fenek-bond-*.webp")), (
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

    # The 20 original Lot 25 binaries stay byte-for-byte verified on disk and
    # in the build, but the visual design has been superseded by ten images
    # supplied in the Lot 27 gallery. Never silently use a wrong label/code.
    source_gallery = {
        "fenek-bond-c1t":20, "fenek-bond-c1te":21,
        "fenek-bond-c2te":22, "fenek-bond-c2te-s1":23,
        "fenek-bond-c2ft":24, "fenek-bond-cg1":25,
        "fenek-bond-cg2wa":26, "fenek-bond-ct-c25-f5":27,
        "fenek-bond-gr-hr":31, "fenek-bond-gp-csii":32,
    }
    slugs = sorted(mod.approved_assets()[1])
    assert len(slugs) == 10 and set(slugs) == set(source_gallery)
    for slug, number in source_gallery.items():
        asset = DIST / "images" / "illustrations" / "maquettes" / f"maquette-{number:02d}.webp"
        assert asset.is_file() and asset.read_bytes()[:4] == b"RIFF", str(asset)
    for lang in ("fr", "ar", "en"):
        catalogue = DIST / lang / "catalogue/index.html"
        html = catalogue.read_text(encoding="utf-8")
        for slug in slugs:
            design_url = f"/images/illustrations/maquettes/maquette-{source_gallery[slug]:02d}.webp"
            assert design_url in html, f"Updated card not rendered: {lang}, {slug}"
            detail = DIST / lang / "catalogue" / slug / "index.html"
            assert detail.is_file(), f"Missing localized detail: {lang}/{slug}"
            body = detail.read_text(encoding="utf-8")
            assert design_url in body, f"Updated full-size concept missing: {lang}/{slug}"
            assert "concept-detail-note" in body, f"Missing non-contractual notice: {lang}/{slug}"
            assert f"/images/illustrations/catalogue-projects/{slug}.webp" not in body, (
                f"Legacy flat label still displayed: {lang}/{slug}"
            )

    print("PASS: 20/20 archived SHA256-verified WebP assets and 60/60 updated "
          "gallery-image uses (10 cards × 3 + 10 details × 3)")


if __name__ == "__main__":
    check()
