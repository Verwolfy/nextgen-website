#!/usr/bin/env python3
"""Fail-closed checks of the generated, non-public NextGen static site.

No HTTP requests, no secrets, no access to Supabase, no publishing.
"""
from __future__ import annotations

import json
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


def assert_product_whatsapp(markup: str, lang: str, code: str) -> None:
    tags = Tags()
    tags.feed(markup)
    opening = {"fr": "Bonjour,", "ar": "مرحبًا،", "en": "Hello,"}[lang]
    assert any(
        link.startswith("https://wa.me/") and "?text=" in link
        and f"({code})" in unquote(link) and opening in unquote(link)
        for link in tags.links
    ), f"Missing contextual WhatsApp link: {lang}/{code}"


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
        # The obsolete homepage gallery is retired; only product-linked WebPs remain.
        # Source-labelled documentation: every reference is viewable in three languages.
        info_index = ROOT / lang / "documentation" / "index.html"
        assert info_index.is_file(), str(info_index)
        refs += check_page(info_index, lang)
        checked += 1
        assert not (ROOT / lang / "maquettes").exists(), lang
        catalog = (ROOT / lang / "catalogue" / "index.html").read_text(encoding="utf-8")
        products = json.loads((ROOT.parent/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        assert len(products)==50 and len({p["slug"] for p in products})==50
        asset_dir=ROOT/"images/illustrations/produits"
        assert len(list(asset_dir.glob("*.webp")))==62, "One complete product directory expected"
        for p in products:
            slug=p["slug"];code=p["code"]
            name="fenek-proof-cm-o2p-sac-20kg-v2" if code=="PROOF-CM-O2P" else slug
            card=name+("-card" if p["gamme"]=="flow" else "")+".webp"
            full=name+".webp"
            for filename in {card,full}:
                image=asset_dir/filename
                assert image.is_file(),("Missing product image",code,filename)
                raw=image.read_bytes()
                assert raw[:4]==b"RIFF" and raw[8:12]==b"WEBP",(code,filename)
            card_url="/images/illustrations/produits/"+card
            full_url="/images/illustrations/produits/"+full
            assert card_url in catalog,(lang,code,"Missing catalogue card")
            for scope in ("catalogue","documentation"):
                detail=ROOT/lang/scope/slug/"index.html"
                assert detail.is_file() and full_url in detail.read_text(encoding="utf-8"),(lang,scope,code)
        from hashlib import sha256
        corrected=(asset_dir/"fenek-proof-cm-o2p-sac-20kg-v2.webp").read_bytes()
        assert sha256(corrected).hexdigest()=="552f3f850fca117410d0268265f5f7db8c4506dcbc93620ba07529657ea291b7", "Incorrect CM-O2P correction"
        assert not any(
            "Kit : sac 30 kg + bidon 10 kg" in
            (ROOT / lang / "catalogue" / "fenek-proof-cm-o2p" / "index.html").read_text(encoding="utf-8")
            for lang in LANGS
        ), "Old wrong bag quantity still in catalogue"
        # Lot 33: no unpublished field directions or numeric placeholders may
        # leak into the 150 public catalogue detail pages, even in a closed
        # disclosure widget. Their source remains private to the repository.
        source = json.loads((ROOT.parent / "src" / "data" /
                             "catalogue-projets.json").read_text(encoding="utf-8"))
        assert len(source) == 50
        for entry in source:
            info = ROOT / lang / "documentation" / entry["slug"] / "index.html"
            assert info.is_file(), f"Missing information page: {info}"
            markup = info.read_text(encoding="utf-8")
            assert 'class="fenek-product-intro"' in markup, info
            assert_product_whatsapp(markup, lang, entry["code"])
            # New print specification: exactly one localized cover + one
            # six-scene application page. C1T has its previously approved layout.
            expected_qr=f"https://nextgen-buildingsolutions.com/{lang}/documentation/{entry['slug']}/"
            if entry["code"] == "BOND-C1T":
                assert markup.count('data-c1t-application-page') == 1, info
                assert f'data-c1t-qr-href="{expected_qr}"' in markup, info
                assert markup.count('data-c1t-guide-step=') == 6, info
            else:
                assert markup.count('data-fenek-print-cover') == 1, info
                assert markup.count('data-fenek-print-application') == 1, info
                assert f'data-fenek-qr-url="{expected_qr}"' in markup, info
                assert markup.count('data-fenek-guide-step=') == 6, info
                assert markup.count('data-fenek-guide-sprite=') == 1, info
                assert 'class="fpg-qr"' in markup, info
            if entry["code"] == "BOND-C1T":
                # The first product pilot replaces generic accordions with sourced C1T tables.
                assert "data-c1t-pilot" in markup, info
                assert markup.count('data-c1t-source-type="norme"') == 6, info
                assert markup.count('data-c1t-source-type="famille"') == 6, info
                assert "fenek-c1t-print" in markup, info
                assert ("data-print-market-sheet" in markup or f'/docs/fiches/fenek-bond-c1t-{lang}.pdf' in markup), info
                assert "présentation provisoire" not in markup.lower(), info
                assert "Sika" not in markup and "Mapei" not in markup and "Bostik" not in markup, info
            elif entry["code"] == "BOND-C1TE":
                assert "data-c1te-pilot" in markup, info
                assert markup.count('data-c1te-source-type="norme"') == 7, info
                assert markup.count('data-c1te-source-type="famille"') == 5, info
                assert "fenek-c1te-print" in markup, info
                assert ("data-print-market-sheet" in markup or f'/docs/fiches/fenek-bond-c1te-{lang}.pdf' in markup), info
                assert "présentation provisoire" not in markup.lower(), info
                assert all(brand not in markup for brand in ("Sika","Mapei","Bostik","Weber")), info
            elif entry["code"] == "BOND-C2FT":
                assert "data-c2ft-pilot" in markup, info
                assert markup.count('data-c2ft-source-type="norme"') == 7, info
                assert markup.count('data-c2ft-source-type="famille"') == 6, info
                assert "fenek-c2ft-print" in markup, info
                assert ("data-print-market-sheet" in markup or f'/docs/fiches/fenek-bond-c2ft-{lang}.pdf' in markup), info
                assert "présentation provisoire" not in markup.lower(), info
                assert "Les seuils de classe et les plages comparatives" not in markup, info
                assert all(brand not in markup for brand in ("Sika","Mapei","Bostik","Weber")), info
            elif entry["code"] in ("BOND-CG2WA", "BOND-CT-C25-F5", "BOND-GP-CSII", "BOND-GR-HR", "BOND-M10", "BOND-M5", "BOND-OC-CSIII", "BOND-R2", "BOND-R3", "BOND-R4"):
                assert "data-bond-technical-pilot" in markup, info
                assert markup.count('data-bond-source-type="norme"') >= 1, info
                assert markup.count('data-bond-source-type="famille"') >= 3, info
                assert "fenek-bond-technical-print" in markup, info
                assert ("data-print-market-sheet" in markup or f'/docs/fiches/{entry["slug"]}-{lang}.pdf' in markup), info
                assert "présentation provisoire" not in markup.lower(), info
                assert "Les seuils de classe et les plages comparatives" not in markup, info
            elif entry["gamme"] in ("proof", "flow", "paint"):
                assert "data-other-technical-pilot" in markup, info
                assert markup.count('data-other-source-type="referentiel"') >= 4, info
                assert markup.count('data-other-source-type="famille"') >= 3, info
                assert "fenek-other-technical-print" in markup, info
                assert ("data-print-market-sheet" in markup or f'/docs/fiches/{entry["slug"]}-{lang}.pdf' in markup), info
                assert "présentation provisoire" not in markup.lower(), info
                assert "Les seuils de classe et les plages comparatives" not in markup, info
            elif entry["code"] == "BOND-CG1":
                assert "data-cg1-pilot" in markup, info
                assert markup.count('data-cg1-source-type="norme"') == 8, info
                assert markup.count('data-cg1-source-type="famille"') == 6, info
                assert "fenek-cg1-print" in markup, info
                assert ("data-print-market-sheet" in markup or f'/docs/fiches/fenek-bond-cg1-{lang}.pdf' in markup), info
                assert "présentation provisoire" not in markup.lower(), info
                assert "Les seuils de classe et les plages comparatives" not in markup, info
            elif entry["code"] == "BOND-C2TE-S1":
                assert "data-c2tes1-pilot" in markup, info
                assert markup.count('data-c2tes1-source-type="norme"') == 8, info
                assert markup.count('data-c2tes1-source-type="famille"') == 6, info
                assert "fenek-c2tes1-print" in markup, info
                assert ("data-print-market-sheet" in markup or f'/docs/fiches/fenek-bond-c2te-s1-{lang}.pdf' in markup), info
                assert "présentation provisoire" not in markup.lower(), info
                assert "Les seuils de classe et les plages comparatives" not in markup, info
            elif entry["code"] == "BOND-C2TE":
                assert "data-c2te-pilot" in markup, info
                assert markup.count('data-c2te-source-type="norme"') == 7, info
                assert markup.count('data-c2te-source-type="famille"') == 6, info
                assert "fenek-c2te-print" in markup, info
                assert ("data-print-market-sheet" in markup or f'/docs/fiches/fenek-bond-c2te-{lang}.pdf' in markup), info
                assert "présentation provisoire" not in markup.lower(), info
                assert "Les seuils de classe et les plages comparatives" not in markup, info
                assert all(brand not in markup for brand in ("Sika", "Mapei", "Bostik", "Weber")), info
            else:
                assert markup.count('class="fenek-doc-accordion"') == 8, info
                assert markup.count('<summary>') == 8, info
                assert markup.count('class="fenek-accordion-indicator"') == 8, info
                assert markup.count('class="fenek-doc-accordion" open') == 4, info
            for anchor in ('fenek-overview', 'fenek-details',
                           'fenek-application', 'fenek-documents'):
                assert f'id="{anchor}"' in markup, (info, anchor)
                assert f'href="#{anchor}"' in markup, (info, anchor)
            if entry["gamme"] == "bond" and entry["code"] not in ("BOND-C1T", "BOND-C1TE", "BOND-C2FT", "BOND-C2TE", "BOND-C2TE-S1", "BOND-CG1", "BOND-CG2WA", "BOND-CT-C25-F5", "BOND-GP-CSII", "BOND-GR-HR", "BOND-M10", "BOND-M5", "BOND-OC-CSIII", "BOND-R2", "BOND-R3", "BOND-R4"):
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
            if entry["gamme"] == "bond" and entry["code"] not in ("BOND-C1T", "BOND-C1TE", "BOND-C2FT", "BOND-C2TE", "BOND-C2TE-S1", "BOND-CG1", "BOND-CG2WA", "BOND-CT-C25-F5", "BOND-GP-CSII", "BOND-GR-HR", "BOND-M10", "BOND-M5", "BOND-OC-CSIII", "BOND-R2", "BOND-R3", "BOND-R4"):
                assert "concept-detail-note" in markup, f"Missing documentation notice {lang}/{entry['slug']}"
            assert_product_whatsapp(markup, lang, entry["code"])
        # Lot 31: eleven photo-realistic renderings cut from the user-selected
        # concept board, associated strictly with their true FENEK-PAINT code.
        # No flat vector pail and no shared 15 L image may appear.
        paint_slugs = ("ent-l", "fac-el", "fac-m", "fac-sx",
                       "int-m", "int-s", "int-wa",
                       "prim-a", "prim-fx", "sol-a", "txt-f")
        assert len(paint_slugs) == 11
        assert catalog.count("/images/illustrations/produits/fenek-paint-") == 11, lang
        assert 'class="paint-concept-art"' not in catalog, lang
        assert '/images/illustrations/produits/maquette-19.webp' not in catalog, lang
        for item in paint_slugs:
            slug = "fenek-paint-" + item
            asset = f"/images/illustrations/produits/{slug}.webp"
            built_asset = ROOT / asset.lstrip("/")
            assert built_asset.is_file() and built_asset.read_bytes()[8:12] == b"WEBP", slug
            assert asset in catalog, f"Wrong card image in {lang}/{slug}"
            detail = (ROOT / lang / "catalogue" / slug / "index.html").read_text(encoding="utf-8")
            assert asset in detail, f"Wrong full-size PAINT concept: {lang}/{slug}"
            assert 'class="paint-concept-art"' not in detail and '/images/illustrations/produits/maquette-19.webp' not in detail, slug
            assert "concept-detail-note" not in detail, f"Legacy conceptual disclaimer on approved editorial template: {slug}"
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
