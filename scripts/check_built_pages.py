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
        if tag == "img" and attrs.get("src"):
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
        for suffix in ("", *SECTIONS, *(("gammes/" + r) for r in RANGES)):
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
        # Gallery pages are retired; keep their WebP files as catalogue/hero assets.
        # Source-labelled documentation: every reference is viewable in three languages.
        info_index = ROOT / lang / "documentation" / "index.html"
        assert info_index.is_file(), str(info_index)
        refs += check_page(info_index, lang)
        checked += 1
        assert not (ROOT / lang / "maquettes").exists(), lang
        for i in range(1, 47):
            image = ROOT / "images" / "maquettes" / f"maquette-{i:02d}.webp"
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
            # Lot 125: CM-O2P retains archived image 37 but publicly displays
            # the corrected bag label "SAC 20 KG" (canister unchanged at 10 KG).
            asset = ("/images/maquettes/maquette-37-sac-20kg.svg"
                     if slug == "fenek-proof-cm-o2p"
                     else f"/images/maquettes/maquette-{number:02d}.webp")
            assert asset in catalog, f"Missing reference visual in {lang}: {slug}"
            detail = ROOT / lang / "catalogue" / slug / "index.html"
            assert detail.is_file() and asset in detail.read_text(encoding="utf-8"), (
                f"Wrong detail image: {lang}/{slug}"
            )
        corrected_asset = ROOT / "images/maquettes/maquette-37-sac-20kg.svg"
        assert corrected_asset.is_file(), "Missing corrected CM-O2P 20 kg mockup"
        corrected_markup = corrected_asset.read_text(encoding="utf-8")
        assert "SAC 20 KG</text>" in corrected_markup
        assert "image/webp;base64," in corrected_markup
        assert "bidon composant B 10 kg" in corrected_markup
        assert not any(
            "Kit : sac 30 kg + bidon 10 kg" in
            (ROOT / lang / "catalogue" / "fenek-proof-cm-o2p" / "index.html").read_text(encoding="utf-8")
            for lang in LANGS
        ), "Old wrong bag quantity still in catalog"
        # Lot 33: no unpublished field directions or numeric placeholders may
        # leak into the 150 public catalogue detail pages, even in a closed
        # disclosure widget. Their source remains private to the repository.
        import json
        source = json.loads((ROOT.parent / "src" / "data" /
                             "catalogue-projets.json").read_text(encoding="utf-8"))
        assert len(source) == 50
        for entry in source:
            info = ROOT / lang / "documentation" / entry["slug"] / "index.html"
            assert info.is_file(), f"Missing information page: {info}"
            markup = info.read_text(encoding="utf-8")
            assert 'class="fenek-product-intro"' in markup, info
            assert markup.count('class="fenek-doc-accordion"') == 8, info
            assert markup.count('<summary>') == 8, info
            assert markup.count('class="fenek-accordion-indicator"') == 8, info
            # The expanded application walkthrough makes four default-open sections.
            assert markup.count('class="fenek-doc-accordion" open') == 4, info
            for anchor in ('fenek-overview', 'fenek-details',
                           'fenek-application', 'fenek-documents'):
                assert f'id="{anchor}"' in markup, (info, anchor)
                assert f'href="#{anchor}"' in markup, (info, anchor)
            assert 'data-print-market-sheet' in markup, info
            assert entry["nom"] in markup, info
            assert "noindex,nofollow" in markup, info
            for forbidden in (
                "market-sheet-warning", "market-reference-list", "source officielle",
                "produits tiers cités", "Sika", "Mapei", "Fosroc", "Jotun",
                "Granitex", "Weber", "certified FENEK",
                "FENEK certifié", "validated NextGen SDS",
                "[valeur à confirmer]", "mode_fr_preparatoire",
            ):
                assert forbidden.lower() not in markup.lower(), (info, forbidden)
            refs += check_page(info, lang)
            checked += 1
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
        # Retired visualization routes and packaged models must not enter dist.
        assert not (ROOT / lang / "emballages").exists(), lang
    assert not (ROOT / "models-demo").exists()
    assert not (ROOT / "images" / "3d-demo").exists()
    # No third-party brand or legacy market comparison may appear in public HTML.
    external_names = ("sikaceram", "sikadur", "sikaflex", "sika",
                      "mapei", "fosroc", "jotun", "granitex",
                      "saint-gobain weber", "weberpral")
    for html_path in ROOT.rglob("*.html"):
        content = html_path.read_text(encoding="utf-8").lower()
        for name in external_names:
            assert name not in content, f"External manufacturer in public site: {html_path}: {name}"
    assert (ROOT / "data" / "products.json").read_text(encoding="utf-8").strip() == "[]"
    print(f"PASS: {checked} localized routes checked, {refs} links validated, zero active forms, zero fake products")


if __name__ == "__main__":
    main()
    # The same CI entrypoint now checks the generated trilingual Pagefind bundle.
    from check_search_index import main as check_search_index
    check_search_index()
    # Lot 121: all 50 provisional product guides in three locales.
    from check_application_guides import main as check_application_guides
    check_application_guides()
    # Lot 123: animated logo preserves the public pages and all three locales.
    from check_header_brand import main as check_header_brand
    check_header_brand()
    # Lot 124: new 10-second About video and poster, all locales.
    from check_about_video_media import main as check_about_video_media
    check_about_video_media()
