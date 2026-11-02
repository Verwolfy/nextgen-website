#!/usr/bin/env python3
"""Local Chromium browser acceptance tests. No external deployment or secrets."""
from __future__ import annotations

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote
from threading import Thread

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
SHOTS = ROOT / ".ci-artifacts" / "screenshots"


class SilentHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        return


def check() -> None:
    assert (DIST / "fr" / "index.html").is_file(), "Site not built"
    SHOTS.mkdir(parents=True, exist_ok=True)
    srv = ThreadingHTTPServer(
        ("127.0.0.1", 0),
        partial(SilentHandler, directory=str(DIST)),
    )
    thread = Thread(target=srv.serve_forever, daemon=True)
    thread.start()
    base = "http://127.0.0.1:" + str(srv.server_address[1])
    errors = []
    snapshots = 0
    flow_images_present = bool(list((ROOT / "public/images/catalogue-projects").glob("fenek-flow-*.webp")))
    bond_images_present = bool(list((ROOT / "public/images/catalogue-projects").glob("fenek-bond-*.webp")))
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
            for lang in ("fr", "ar", "en"):
                for size, width, height in (("desktop", 1280, 900), ("mobile", 390, 844)):
                    page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
                    page.on("pageerror", lambda err: errors.append(str(err)))
                    for section in ("", "contact", "distributeurs", "catalogue", "emballages", "maquettes", "gammes", "a-propos", "ressources"):
                        path = "/" + lang + "/" + (section + "/" if section else "")
                        response = page.goto(base + path, wait_until="domcontentloaded", timeout=20000)
                        assert response is not None and response.status == 200, path
                        assert page.locator("html").get_attribute("lang") == lang, path
                        assert page.locator("html").get_attribute("dir") == ("rtl" if lang == "ar" else "ltr"), path
                        assert page.locator("h1").count() == 1, path
                        assert page.locator("main").count() == 1, path
                        assert page.locator("form").count() == 0, path
                        if section == "":
                            if lang == "ar":
                                assert "فئات FENEK" in page.locator(".section .eyebrow").all_inner_texts(), path
                            assert page.locator(".hero-status[role='note']").count() == 1, path
                            assert page.locator(".hero-mascot-card img").count() == 1, path
                            assert page.locator(".home-approach .editorial-caution").count() == 1, path
                            assert page.locator(".home-approach .chip").count() == 3, path
                            assert page.locator(".home-audiences .card").count() == 2, path
                            paths = page.locator(".home-audiences .card a").evaluate_all(
                                "links => links.map(a => a.getAttribute('href'))")
                            assert paths == ["/"+lang+"/contact/", "/"+lang+"/distributeurs/"], path
                            assert page.locator(".hero .btn-outline").get_attribute("href") == "/"+lang+"/contact/", path
                            assert page.locator(".hero-mascot-card").evaluate(
                                "e => getComputedStyle(e).borderRadius !== '0px'"
                            ), path
                        if section == "catalogue":
                            assert page.locator(".concept-product-card").count() == 50, path
                            assert page.locator(".concept-range-section").count() == 4, path
                            assert page.locator(".concept-product-status").count() == 50, path
                            assert page.locator(".catalogue-projects .editorial-caution").count() == 1, path
                            if lang == "ar":
                                assert "كتالوج" in page.locator("h1").inner_text(), path
                        if section == "catalogue":
                            # Lot 31: 27 BOND/PROOF gallery photo renders plus
                            # 11 individual code-matched PAINT WebPs from source board.
                            gallery_cards = page.locator(".concept-product-card img[src*='/images/maquettes/']")
                            assert gallery_cards.count() == 27, f"{lang}, {size}: incorrect gallery mapping"
                            paint_imgs = page.locator("#catalogue-paint .concept-product-card img[src*='/images/catalogue-projects/fenek-paint-']")
                            assert paint_imgs.count() == 11, f"{lang}, {size}: missing PAINT product images"
                            srcs = paint_imgs.evaluate_all("els => els.map(e => e.getAttribute('src'))")
                            required = {f"/images/catalogue-projects/fenek-paint-{slug}.webp"
                                        for slug in ("ent-l","fac-el","fac-m","fac-sx","int-m","int-s",
                                                     "int-wa","prim-a","prim-fx","sol-a","txt-f")}
                            assert set(srcs) == required, f"{lang}: wrong PAINT source-to-product mapping"
                            assert page.locator("#catalogue-paint .paint-concept-art").count()==0, (
                                f"{lang}, {size}: obsolete schematic vector images still visible"
                            )
                            if size == "mobile":
                                for k in (0, 5, 16, 26):
                                    im = gallery_cards.nth(k)
                                    im.scroll_into_view_if_needed()
                                    assert im.evaluate("""async im => {
                                        try { await im.decode(); } catch (_) { return false; }
                                        return im.complete && im.naturalWidth > 0 &&
                                          getComputedStyle(im).objectFit === 'contain';
                                    }"""), f"{lang}: gallery image {k} missing"
                                for k in range(paint_imgs.count()):
                                    pic = paint_imgs.nth(k)
                                    pic.scroll_into_view_if_needed()
                                    assert pic.evaluate("""async im => {
                                        try { await im.decode(); } catch (_) { return false; }
                                        return im.complete && im.naturalWidth === 800 &&
                                          im.naturalHeight === 800 &&
                                          getComputedStyle(im).objectFit === 'contain';
                                    }"""), f"{lang}, {size}: paint render {k} missing or deformed"
                                page.evaluate("window.scrollTo(0,0)")
                        if section == "catalogue" and flow_images_present:
                            packshots = page.locator(".concept-product-card .concept-product-image img[src*='/images/catalogue-projects/fenek-flow-']")
                            assert packshots.count() == 12, f"{lang}, {size}: missing FLOW card imagery"
                            if size == "mobile":
                                for k in range(packshots.count()):
                                    packshots.nth(k).scroll_into_view_if_needed()
                                    assert packshots.nth(k).evaluate("""async im => {
                                        try { await im.decode(); } catch (_) { return false; }
                                        return im.complete && im.naturalWidth === 560 &&
                                            im.naturalHeight === 560 && getComputedStyle(im).objectFit === 'contain';
                                    }"""), (
                                        f"{lang}: distorted, missing or broken FLOW card {k}"
                                    )
                            page.evaluate("window.scrollTo(0,0)")
                        if section == "catalogue" and bond_images_present:
                            # Lot 29: exact labels on the newly supplied studio mockups,
                            # rather than the first-generation flat-label WebP cards.
                            bags=page.locator("#catalogue-bond .concept-product-card img[src*='/images/maquettes/']")
                            assert bags.count()==16, f"{lang}, {size}: incomplete updated BOND cards"
                            assert page.locator(".concept-product-card img[src*='/images/catalogue-projects/fenek-bond-']").count()==0, (
                                f"{lang}, {size}: old BOND label design is still displayed"
                            )
                            if size=="mobile":
                                for k in range(bags.count()):
                                    bags.nth(k).scroll_into_view_if_needed()
                                    assert bags.nth(k).evaluate("""async im => {
                                        try { await im.decode(); } catch (_) { return false; }
                                        return im.complete && im.naturalWidth === 880 &&
                                            im.naturalHeight === 880 && getComputedStyle(im).objectFit === 'contain';
                                    }"""), f"{lang}: broken or stretched updated BOND card {k}"
                                page.evaluate("window.scrollTo(0,0)")
                        if section == "gammes":
                            assert page.locator(".range-overview-card").count() == 4, path
                            assert page.locator(".range-overview-card h3 bdi[dir='ltr']").count() == 4, path
                            if lang == "ar":
                                assert "الفئات التقنية" in page.locator("h1").inner_text(), path
                                assert "الملاط" in page.locator(".range-overview").inner_text(), path
                            assert page.locator(".editorial-caution").count() >= 1, path
                        if section == "emballages":
                            if lang == "ar":
                                assert "تصاميم أولية" in page.locator(".page-head .eyebrow").inner_text(), path
                            assert page.locator("model-viewer").count() == 5, path
                            assert page.locator(".showcase-card a[href^='/"+lang+"/emballages/']").count() == 5, path
                            posters = page.locator("button[slot='poster'] img")
                            assert posters.count() == 5, path
                            # Native img tag inside the local poster slot must render BEFORE the 3D GLB is loaded.
                            for i in range(posters.count()):
                                posters.nth(i).scroll_into_view_if_needed()
                                assert posters.nth(i).evaluate("im => im.complete && im.naturalWidth > 0"), path
                            assert page.locator("model-viewer[reveal='interaction']").count() == 5, path
                            assert page.locator("button[slot='poster']").count() == 5, path
                            page.evaluate("window.scrollTo(0,0)")
                        if section == "a-propos":
                            assert page.locator(".about-step").count() == 3, path
                            assert page.locator(".editorial-caution").count() >= 1, path
                        if section == "maquettes":
                            assert page.locator(".visual-concept-card").count() == 46, path
                            images = page.locator(".visual-concept-card img")
                            assert images.count() == 46, path
                            assert page.locator(".notice[role='note']").count() == 1, path
                            for idx in (0, 20, 45):
                                images.nth(idx).scroll_into_view_if_needed()
                                assert images.nth(idx).evaluate("im => im.complete && im.naturalWidth > 0"), path
                            page.evaluate("window.scrollTo(0,0)")
                        if section == "ressources":
                            assert page.locator(".resource-card").count() == 3, path
                            assert page.locator(".resource-card-demo a[href$='/emballages/']").count() == 1, path
                            assert page.locator(".resource-visuals-link a[href$='/maquettes/']").count() == 1, path
                            assert page.locator(".resource-card:not(.resource-card-demo) a").count() == 0, path
                        if section in ("contact", "distributeurs"):
                            assert page.locator(".contact-direct .contact-channel").count() == 3, path
                            assert page.locator(".contact-channel a[href^='mailto:']").count() == 1, path
                            assert page.locator(".contact-channel a[href^='tel:']").count() == 1, path
                            whatsapp = page.locator(".contact-channel a[href^='https://wa.me/']")
                            assert whatsapp.count() == 1, path
                            assert whatsapp.get_attribute("rel") == "noopener noreferrer", path
                            assert page.locator(".contact-direct .contact-disclosure[role='note']").count() == 1, path
                            assert page.locator(".lead-preview, .lead-panel").count() == 0, path
                            assert page.locator("form, input, textarea").count() == 0, path
                            if section == "distributeurs":
                                assert page.locator("a[href='#contact-direct']").count() == 1, path
                        # Overflows on phone screens make navigation unusable.
                        diff = page.evaluate("Math.ceil(document.documentElement.scrollWidth - window.innerWidth)")
                        if diff > 4:
                            overflowing = page.evaluate("""Array.from(document.querySelectorAll('*'))
                                .filter(e => e.getBoundingClientRect().right > innerWidth + 3)
                                .slice(0,8)
                                .map(e => ({tag:e.tagName, cls:String(e.className).slice(0,50), width:Math.round(e.getBoundingClientRect().width)}))""")
                            raise AssertionError(f"Horizontal overflow: {path} {width}px: {diff}px; elements={overflowing}")
                        if (section in ("", "contact")
                            or (size == "mobile" and section in ("gammes", "a-propos", "ressources", "distributeurs", "emballages"))
                            or (size == "desktop" and lang == "ar" and section in ("gammes", "a-propos", "emballages"))):
                            page.screenshot(path=str(SHOTS / (lang + "-" + size + "-" + (section or "home") + ".png")), full_page=True)
                            snapshots += 1
                    # Real local 3D GLB can be opened directly from the homepage.
                    model_route = "/"+lang+"/emballages/sac-25kg/"
                    result = page.goto(base+model_route, wait_until="domcontentloaded", timeout=20000)
                    assert result is not None and result.status == 200, model_route
                    assert page.locator("model-viewer").count() == 1, model_route
                    assert page.locator("model-viewer").get_attribute("src") == "/models-demo/sac-25kg.glb", model_route
                    assert page.locator("model-viewer").get_attribute("reveal") == "interaction", model_route
                    assert page.locator("button[slot='poster'] img").count() == 1, model_route
                    assert page.locator("a[download='sac-25kg.glb']").count() == 1, model_route
                    assert page.locator("form").count() == 0, model_route
                    assert page.locator("meta[name='robots']").get_attribute("content") == "noindex,nofollow", model_route
                    assert page.evaluate("Math.ceil(document.documentElement.scrollWidth - window.innerWidth)") <= 4, model_route
                    # Smoke-check four individual conceptual products, not certified SKUs.
                    for slug in ("fenek-bond-c1t", "fenek-proof-cm-o1p",
                                 "fenek-flow-wr-n", "fenek-paint-int-m"):
                        concept_path = "/"+lang+"/catalogue/"+slug+"/"
                        response = page.goto(base+concept_path, wait_until="domcontentloaded", timeout=20000)
                        assert response is not None and response.status==200, concept_path
                        assert page.locator("h1").count()==1, concept_path
                        assert page.locator(".concept-detail-status").count()==1, concept_path
                        assert page.locator(".concept-steps li").count()==0, concept_path
                        assert page.locator(".concept-source-method").count()==0, concept_path
                        assert page.locator(".concept-detail-note").count()>=1, concept_path
                        email_action = page.locator(".concept-detail-aside a[href^='mailto:']")
                        assert email_action.count() == 1, concept_path
                        email_target = unquote(email_action.get_attribute("href"))
                        assert email_target.startswith("mailto:contact@nextgen-buildingsolutions.com?subject="), concept_path
                        assert page.locator("h1 bdi").inner_text() in email_target, concept_path
                        assert "[valeur à confirmer]" not in page.content(), concept_path
                        assert page.locator("form").count()==0, concept_path
                        detail_overflow=page.evaluate("Math.ceil(document.documentElement.scrollWidth-innerWidth)")
                        assert detail_overflow<=4, f"Concept details overflow: {concept_path}, {width}px, {detail_overflow}px"
                        if slug=="fenek-paint-int-m":
                            full = page.locator(".concept-detail-aside img")
                            assert full.count()==1 and full.get_attribute("src")=="/images/catalogue-projects/fenek-paint-int-m.webp", concept_path
                            full.scroll_into_view_if_needed()
                            assert full.evaluate("""async im => {
                                try { await im.decode(); } catch (_) { return false; }
                                return im.complete && im.naturalWidth === 800 &&
                                    im.naturalHeight === 800 && getComputedStyle(im).objectFit === 'contain';
                            }"""), f"{lang}, {size}: INT-M studio image missing or distorted"
                        if slug=="fenek-bond-c1t" and bond_images_present:
                            full=page.locator(".concept-detail-image img")
                            full.scroll_into_view_if_needed()
                            assert full.evaluate("""async im => {
                                try { await im.decode(); } catch (_) { return false; }
                                return im.complete && im.naturalWidth === 880 &&
                                    im.naturalHeight === 880 &&
                                    im.getAttribute('src') === '/images/maquettes/maquette-20.webp' &&
                                    getComputedStyle(im).objectFit === 'contain';
                            }"""), f"{lang}, {size}: detailed BOND C1T bag missing or distorted"
                            page.screenshot(path=str(SHOTS/(lang+"-"+size+"-fenek-bond-c1t.png")),full_page=True)
                            snapshots+=1
                        if slug=="fenek-flow-wr-n" and flow_images_present:
                            full = page.locator(".concept-detail-image img")
                            full.scroll_into_view_if_needed()
                            assert full.evaluate("""async im => {
                                try { await im.decode(); } catch (_) { return false; }
                                return im.complete && im.naturalWidth === 1120 &&
                                    im.naturalHeight === 1120 && getComputedStyle(im).objectFit === 'contain';
                            }"""), (
                                f"{lang}, {size}: WR-N packshot missing or compressed"
                            )
                            page.screenshot(path=str(SHOTS/(lang+"-"+size+"-fenek-flow-wr-n.png")),full_page=True)
                            snapshots+=1
                        if slug=="fenek-bond-c1t":
                            page.screenshot(path=str(SHOTS/(lang+"-"+size+"-catalogue-concept.png")),full_page=True)
                            snapshots+=1
                    # Lot 38: filters run locally; no network request, cookie or form.
                    page.goto(base + "/" + lang + "/catalogue/", wait_until="domcontentloaded")
                    controls = page.locator("[data-catalogue-controls]")
                    assert controls.is_visible(), lang
                    visible_cards = page.locator(".concept-product-card:visible")
                    assert visible_cards.count() == 50, lang
                    search = page.locator("#catalogue-query")
                    search.fill("fenek-flow-wr-n")
                    assert visible_cards.count() == 1, lang
                    assert "WR-N" in visible_cards.first.inner_text(), lang
                    search.fill("no-such-product-reference-xyz")
                    assert visible_cards.count() == 0, lang
                    assert page.locator("[data-catalogue-empty]").is_visible(), lang
                    page.locator("[data-catalogue-reset]").click()
                    assert visible_cards.count() == 50, lang
                    selector = page.locator("#catalogue-range")
                    selector.select_option("paint")
                    assert visible_cards.count() == 11, lang
                    assert page.locator(".concept-range-section:visible").count() == 1, lang
                    page.locator("[data-catalogue-nav='bond']").click()
                    assert visible_cards.count() == 16, lang
                    assert selector.input_value() == "bond", lang
                    page.locator("[data-catalogue-reset]").click()
                    assert visible_cards.count() == 50, lang
                    assert page.locator("form").count() == 0, lang
                    # Lot 39: match any public description, usage, or range keyword.
                    # 'mortier' must include BOND; FLOW may also match legitimately.
                    for term, target_range in (
                        ("mortier", "bond"),
                        ("colle carrelage", "bond"),
                        ("étanchéité", "proof"),
                        ("etancheite", "proof"),
                        ("waterproofing", "proof"),
                        ("الملاط", "bond"),
                    ):
                        search.fill(term)
                        assert page.locator("#catalogue-"+target_range+
                                            " .concept-product-card:visible").count() > 0, (
                            lang, size, term, target_range)
                    search.fill("fenek bond c1t")
                    assert visible_cards.count() >= 1, (lang, size)
                    search.fill("absent-keyword-zzzz")
                    assert visible_cards.count() == 0, lang
                    page.locator("[data-catalogue-reset]").click()
                    assert visible_cards.count() == 50, lang
                    # Explicitly follow the language navigation to another localized page.
                    page.goto(base + "/" + lang + "/contact/", wait_until="domcontentloaded")
                    assert page.locator(".locale a").count() == 3
                    page.locator(".locale a[href='/en/contact/']").click()
                    assert page.url.endswith("/en/contact/")
                    # Native responsive navigation: desktop stays visible, mobile is keyboard operable.
                    page.goto(base + "/" + lang + "/", wait_until="domcontentloaded")
                    assert page.locator(".nav a").count() == 6
                    if size == "mobile":
                        assert not page.locator(".nav").is_visible(), lang
                        toggle = page.locator(".mobile-trigger")
                        assert toggle.is_visible(), lang
                        assert page.locator(".mobile-links a").count() == 6
                        assert not page.locator(".mobile-links").is_visible()
                        if lang == "ar":
                            assert "القائمة" in toggle.inner_text()
                        toggle.focus()
                        page.keyboard.press("Enter")
                        assert page.locator(".mobile-links").is_visible()
                        page.locator(".mobile-links a[href='/" + lang + "/ressources/']").focus()
                        page.keyboard.press("Enter")
                        # Key presses do not imply navigation has completed: wait explicitly.
                        page.wait_for_url("**/" + lang + "/ressources/", timeout=10000)
                        assert page.url.endswith("/" + lang + "/ressources/"), lang
                    else:
                        assert page.locator(".nav").is_visible(), lang
                        assert not page.locator(".mobile-trigger").is_visible(), lang
                    page.close()
                # Also exercise the 320px viewport where the menu label is visually shortened.
                tiny = browser.new_page(viewport={"width": 320, "height": 700})
                tiny.goto(base + "/" + lang + "/", wait_until="domcontentloaded")
                assert tiny.locator(".mobile-trigger").is_visible()
                tiny.locator(".mobile-trigger").click()
                assert tiny.locator(".mobile-links a").count() == 6
                assert tiny.locator(".mobile-links").is_visible()
                tiny_width = tiny.evaluate("Math.ceil(document.documentElement.scrollWidth - innerWidth)")
                assert tiny_width <= 4, f"320px navigation overflow ({lang}): {tiny_width}"
                tiny.screenshot(path=str(SHOTS / (lang + "-mobile-320-home.png")), full_page=True)
                snapshots += 1
                tiny.goto(base + "/" + lang + "/contact/", wait_until="domcontentloaded")
                assert tiny.locator(".contact-channel").count() == 3
                assert tiny.locator(".lead-preview, .lead-panel").count() == 0
                tiny_contact_width = tiny.evaluate("Math.ceil(document.documentElement.scrollWidth - innerWidth)")
                assert tiny_contact_width <= 4, f"320px contact overflow ({lang}): {tiny_contact_width}"
                tiny.screenshot(path=str(SHOTS / (lang + "-mobile-320-contact.png")), full_page=True)
                snapshots += 1
                tiny.close()
            browser.close()
    finally:
        srv.shutdown()
        srv.server_close()
    assert not errors, "Unexpected browser JavaScript errors: " + str(errors[:5])
    print(f"PASS: 54 browser route/viewport checks, 6 language-switch clicks, 9 responsive menus, {snapshots} screenshots")


if __name__ == "__main__":
    check()
