#!/usr/bin/env python3
"""Fail-closed checks of the generated, non-public NextGen static site.

No HTTP requests, no secrets, no access to Supabase, no publishing.
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / "dist"
LANGS = ("fr", "ar", "en")
SECTIONS = ("gammes", "catalogue", "distributeurs", "ressources",
            "a-propos", "contact", "mentions-legales", "confidentialite")
RANGES = ("bond", "proof", "flow", "paint")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


class Tags(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.html = []
        self.links = []
        self.media = []
        self.forms = 0
        self.lead_depth = 0
        self.lead_controls = []
        self.lang_switches = []
        self._locale_depth = 0
        self.main_seen = False
        self.has_heading = False
        self.noindex = False
        self.viewport = False

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if tag == "html":
            self.html.append(attrs)
        if tag == "main" and attrs.get("id") == "main":
            self.main_seen = True
        if tag == "h1":
            self.has_heading = True
        if tag == "meta" and attrs.get("name") == "robots":
            self.noindex = "noindex" in (attrs.get("content") or "").lower()
        if tag == "meta" and attrs.get("name") == "viewport":
            self.viewport = True
        if tag == "form":
            self.forms += 1
        if tag in {"a", "link"} and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag in {"img", "model-viewer"} and attrs.get("src"):
            self.media.append(attrs["src"])
        if tag == "div" and "locale" in (attrs.get("class") or "").split():
            self._locale_depth = 1
        elif self._locale_depth and tag not in VOID:
            self._locale_depth += 1
        if self._locale_depth and tag == "a":
            self.lang_switches.append(attrs.get("href"))
        if tag == "section" and "lead-panel" in (attrs.get("class") or "").split():
            self.lead_depth = 1
        elif self.lead_depth and tag not in VOID:
            self.lead_depth += 1
        if self.lead_depth and tag in {"input", "textarea", "button"}:
            self.lead_controls.append((tag, "disabled" in attrs))

    def handle_startendtag(self, tag, pairs):
        self.handle_starttag(tag, pairs)

    def handle_endtag(self, tag):
        if self.lead_depth and tag not in VOID:
            self.lead_depth -= 1
        if self._locale_depth and tag not in VOID:
            self._locale_depth -= 1


def local_path(raw: str) -> Path | None:
    parts = urlsplit(raw)
    if parts.scheme or parts.netloc or raw.startswith("//"):
        return None
    path = unquote(parts.path)
    if not path.startswith("/"):
        return None
    segments = path.split("/")
    if any(seg in ("..", ".") for seg in segments):
        raise AssertionError("Unsafe relative link: " + raw)
    target = ROOT.joinpath(*[part for part in segments if part])
    if path.endswith("/") or not target.suffix:
        target /= "index.html"
    if not target.resolve().is_relative_to(ROOT.resolve()):
        raise AssertionError("Path outside static build")
    return target


def check_page(filename: Path, lang: str) -> int:
    html = filename.read_text(encoding="utf-8")
    tags = Tags()
    tags.feed(html)
    assert len(tags.html) == 1, str(filename)
    assert tags.html[0].get("lang") == lang, str(filename)
    assert tags.html[0].get("dir") == ("rtl" if lang == "ar" else "ltr"), str(filename)
    assert tags.main_seen and tags.has_heading and tags.noindex and tags.viewport, str(filename)
    assert tags.forms == 0, "Unexpected active data collection: " + str(filename)
    assert len(tags.lang_switches) == 3, "Language navigation missing: " + str(filename)
    assert all("price=" not in link.lower() for link in tags.links), str(filename)
    for url in (*tags.links, *tags.media):
        target = local_path(url)
        if target is not None:
            assert target.is_file(), "Broken static link: " + str(filename) + " -> " + url
    return len(tags.links)


def main() -> None:
    assert ROOT.is_dir(), "Run npm run build first"
    checked = 0
    refs = 0
    for lang in LANGS:
        for suffix in ("", *SECTIONS, "emballages", "maquettes", *(("gammes/" + r) for r in RANGES)):
            fn = ROOT / lang / suffix / "index.html"
            assert fn.is_file(), "Missing translated route: " + str(fn)
            refs += check_page(fn, lang)
            checked += 1
        for part in ("contact", "distributeurs"):
            fn = ROOT / lang / part / "index.html"
            parsed = Tags()
            parsed.feed(fn.read_text(encoding="utf-8"))
            # Visitors see functioning direct contact channels, never a
            # disabled form preview that suggests the site is unfinished.
            html = fn.read_text(encoding="utf-8")
            assert 'class="contact-direct"' in html and html.count('class="contact-channel"') == 3, fn
            assert "lead-preview" not in html and "lead-panel" not in html, fn
            assert not parsed.lead_controls, "Unexpected lead input: " + str(fn)
        # Lot 27: all unique images are linked from the localized, non-indexed gallery.
        gallery = (ROOT / lang / "maquettes" / "index.html").read_text(encoding="utf-8")
        assert "non contractuelles" in gallery.lower() or "NON VALIDÉES" in gallery or "غير معتمدة" in gallery or "UNAPPROVED" in gallery, lang
        for i in range(1, 47):
            asset = f"/images/maquettes/maquette-{i:02d}.webp"
            assert asset in gallery, "Missing image in "+lang+": "+asset
            image = ROOT / asset.lstrip("/")
            assert image.is_file() and image.read_bytes()[:4] == b"RIFF", str(image)
        catalog = (ROOT / lang / "catalogue" / "index.html").read_text(encoding="utf-8")
        # Lots 28–29: all 27 BOND/PROOF references must show
        # their actual label-matched, reviewed gallery image in all 3 locales.
        reviewed_visuals = {
            # Lot 29: render the detailed BOND images from the real gallery.
            "fenek-bond-c1t":20,"fenek-bond-c1te":21,
            "fenek-bond-c2te":22,"fenek-bond-c2te-s1":23,
            "fenek-bond-c2ft":24,"fenek-bond-cg1":25,
            "fenek-bond-cg2wa":26,"fenek-bond-ct-c25-f5":27,
            "fenek-bond-gr-hr":31,"fenek-bond-gp-csii":32,
            "fenek-bond-m10":35, "fenek-bond-m5":34,
            "fenek-bond-oc-csiii":33, "fenek-bond-r2":28,
            "fenek-bond-r3":29, "fenek-bond-r4":30,
            "fenek-proof-acr-rf":39, "fenek-proof-cm-o1p":36,
            "fenek-proof-cm-o2p":37, "fenek-proof-ep-anc":44,
            "fenek-proof-ep-inj":43, "fenek-proof-ep-prim":40,
            "fenek-proof-ep-sb":42, "fenek-proof-ep-sr":41,
            "fenek-proof-pu-1k":38, "fenek-proof-pu-inj":45,
            "fenek-proof-pu-seal":4,
        }
        for slug, number in reviewed_visuals.items():
            asset = f"/images/maquettes/maquette-{number:02d}.webp"
            assert asset in catalog, f"Missing reference visual in {lang}: {slug}"
            detail = ROOT / lang / "catalogue" / slug / "index.html"
            assert detail.is_file() and asset in detail.read_text(encoding="utf-8"), (
                f"Wrong detail image: {lang}/{slug}"
            )
        # Lot 33: no unpublished field directions or numeric placeholders may
        # leak into the 150 public catalogue detail pages, even in a closed
        # disclosure widget. Their source remains private to the repository.
        import json
        source = json.loads((ROOT.parent / "src" / "data" /
                             "catalogue-projets.json").read_text(encoding="utf-8"))
        assert len(source) == 50
        for entry in source:
            path = ROOT / lang / "catalogue" / entry["slug"] / "index.html"
            markup = path.read_text(encoding="utf-8")
            for forbidden in ("[valeur à confirmer]", "Mode d’emploi source",
                              "Original French instructions (draft)",
                              "نص طريقة الاستعمال الأصلي بالفرنسية",
                              "concept-source-method", "concept-steps"):
                assert forbidden not in markup, (
                    f"Draft technical procedure leaked to {lang}/{entry['slug']}: {forbidden}"
                )
            for stale in ("Contenu révisable. Les données du laboratoire",
                          "This content can be revised as laboratory",
                          "يمكن تحديث هذا المحتوى لاحقًا"):
                assert stale not in markup, f"Old revision copy still public: {lang}/{entry['slug']}"
            assert "concept-detail-note" in markup, f"Missing documentation notice {lang}/{entry['slug']}"
        # Lot 31: eleven photo-realistic renderings cut from the user-selected
        # concept board, associated strictly with their true FENEK-PAINT code.
        # No flat vector pail and no shared 15 L image may appear.
        paint_slugs = ("ent-l", "fac-el", "fac-m", "fac-sx",
                       "int-m", "int-s", "int-wa",
                       "prim-a", "prim-fx", "sol-a", "txt-f")
        assert len(paint_slugs) == 11
        assert catalog.count("/images/catalogue-projects/fenek-paint-") == 11, lang
        assert 'class="paint-concept-art"' not in catalog, lang
        assert '/images/maquettes/maquette-19.webp' not in catalog, lang
        for item in paint_slugs:
            slug = "fenek-paint-" + item
            asset = f"/images/catalogue-projects/{slug}.webp"
            built_asset = ROOT / asset.lstrip("/")
            assert built_asset.is_file() and built_asset.read_bytes()[8:12] == b"WEBP", slug
            assert asset in catalog, f"Wrong card image in {lang}/{slug}"
            detail = (ROOT / lang / "catalogue" / slug / "index.html").read_text(encoding="utf-8")
            assert asset in detail, f"Wrong full-size PAINT concept: {lang}/{slug}"
            assert 'class="paint-concept-art"' not in detail and '/images/maquettes/maquette-19.webp' not in detail, slug
            assert "concept-detail-note" in detail, slug
        assert "PF-001" not in catalog and "PF-006" not in catalog
        assert not (ROOT / lang / "produits").is_dir(), "No real product was approved"
        assert "SIMULATION" in (ROOT / "fr" / "emballages" / "index.html").read_text(encoding="utf-8")
        # Lot 26: every local 3D asset must have a dedicated, fully linked,
        # non-indexed route in each language, with the real GLB and WebP poster.
        gallery_html = (ROOT / lang / "emballages" / "index.html").read_text(encoding="utf-8")
        for model in ("sac-25kg", "seau-20kg", "bidon-20l", "fut-200l", "ibc-1000l"):
            model_page = ROOT / lang / "emballages" / model / "index.html"
            assert model_page.is_file(), "Missing 3D inspection route: " + str(model_page)
            refs += check_page(model_page, lang)
            checked += 1
            content = model_page.read_text(encoding="utf-8")
            assert f"/models-demo/{model}.glb" in content, str(model_page)
            assert f"/images/3d-demo/{model}-30.webp" in content, str(model_page)
            assert "<model-viewer" in content and "download=" in content, str(model_page)
            assert f"/{lang}/emballages/{model}/" in gallery_html, model

    for item in ("sac-25kg", "seau-20kg", "bidon-20l", "fut-200l", "ibc-1000l"):
        assert (ROOT / "models-demo" / (item + ".glb")).stat().st_size > 0
        assert (ROOT / "images" / "3d-demo" / (item + "-30.webp")).stat().st_size > 0
    assert (ROOT / "data" / "products.json").read_text(encoding="utf-8").strip() == "[]"
    print(f"PASS: {checked} localized routes checked, {refs} links validated, zero active forms, zero fake products")


if __name__ == "__main__":
    main()
