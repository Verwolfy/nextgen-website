#!/usr/bin/env python3
"""Local Chromium browser acceptance tests. No external deployment or secrets."""
from __future__ import annotations

from functools import partial
import re
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



def check_lot118_global_search(browser, base: str) -> None:
    """Lot 118: accessible instant search, filters, responsive RTL and no private requests."""
    for lang in ("fr", "ar", "en"):
        for width in (320, 390, 1280, 1440):
            page = browser.new_page(viewport={"width": width, "height": 780})
            requests = []
            page.on("request", lambda request: requests.append(request.url))
            try:
                page.goto(f"{base}/{lang}/", wait_until="domcontentloaded")
                trigger = page.locator("[data-search-trigger]")
                panel = page.locator("[data-search-panel]")
                assert trigger.count() == 1 and trigger.is_visible(), (lang, width)
                assert panel.is_hidden() and trigger.get_attribute("aria-expanded") == "false"
                label = trigger.locator(".ng-search-trigger-label")
                assert label.count() == 1 and bool(label.inner_text().strip()), (lang, width)
                if width == 1440:
                    assert label.is_visible(), (lang, "capsule label missing on wide desktop")
                else:
                    assert label.is_hidden(), (lang, "search icon-only on narrow screens")
                if width in (1280, 1440):
                    nav_links = page.locator(".header .nav a")
                    first, last = nav_links.first.bounding_box(), nav_links.last.bounding_box()
                    assert first and last and abs(first["y"] - last["y"]) <= 4, \
                        (lang, "desktop navigation unexpectedly wrapped", first, last)
                assert page.evaluate("document.documentElement.scrollWidth-innerWidth") <= 4, \
                    (lang, width, "search header overflow")
                trigger.click()
                assert panel.is_visible() and trigger.get_attribute("aria-expanded") == "true"
                field = panel.locator("[data-search-input]")
                assert field.evaluate("el => el === document.activeElement"), (lang, width)
                assert page.request.get(base + "/pagefind/pagefind.js").status == 200
                field.fill("C1T")
                panel.locator("[data-search-filter='product']").click()
                result = panel.locator(f"a.ng-search-result[href='/{lang}/catalogue/fenek-bond-c1t/']")
                result.wait_for(state="visible", timeout=20000)
                assert panel.locator("[data-search-filter='product']").get_attribute("aria-pressed") == "true"
                assert panel.locator("[data-search-status]").inner_text().strip(), (lang, width)
                assert all("supabase.co" not in url for url in requests), (lang, requests)
                page.keyboard.press("Escape")
                assert panel.is_hidden() and trigger.get_attribute("aria-expanded") == "false"
                assert trigger.evaluate("el => el === document.activeElement"), (lang, width)
                page.keyboard.press("Control+k")
                assert panel.is_visible() and field.evaluate("el => el === document.activeElement"), (lang, width)
                page.locator("[data-search-close]").click()
                assert panel.is_hidden(), (lang, width)
                if width == 1440:
                    before = trigger.evaluate("el => getComputedStyle(el).color")
                    page.locator("[data-theme-switch]").click()
                    assert page.locator("html").get_attribute("data-theme") == "dark"
                    after = trigger.evaluate("el => getComputedStyle(el).color")
                    assert before != after, (lang, "capsule light/dark styles identical")
                    page.locator("[data-theme-switch]").click()
                    assert page.locator("html").get_attribute("data-theme") == "light"
                if width == 320:
                    page.emulate_media(reduced_motion="reduce")
                    assert trigger.locator("svg").evaluate(
                        "el => getComputedStyle(el).animationName") == "none"
                    assert trigger.evaluate(
                        "el => getComputedStyle(el, '::before').animationName") == "none"
                    assert page.evaluate("document.documentElement.scrollWidth-innerWidth") <= 4
            finally:
                page.close()


def check_header_preferences(browser, base: str) -> None:
    """Lot 60: live navigation, system mode, persistence, and night contrast."""
    for lang in ("fr", "ar", "en"):
        page = browser.new_page(viewport={"width": 390, "height": 844})
        try:
            page.emulate_media(color_scheme="light")
            response = page.goto(f"{base}/{lang}/", wait_until="domcontentloaded")
            assert response is not None and response.status == 200
            # Lot 101: every locale must expose a real icon; avoids Lighthouse favicon.ico 404.
            icon = page.locator('link[rel="icon"][type="image/svg+xml"]')
            assert icon.count() == 1 and icon.get_attribute("href") == "/favicon.svg", lang
            favicon = page.request.get(base + "/favicon.svg")
            assert favicon.status == 200 and b"<svg" in favicon.body(), lang
            switch = page.locator("[data-theme-switch]")
            menu = page.locator("[data-language-picker]")
            assert switch.count() == 1 and menu.count() == 1
            assert switch.get_attribute("role") == "switch"
            assert switch.get_attribute("aria-checked") == "false"
            assert page.locator("html").get_attribute("data-theme") == "light"
            assert menu.locator("summary").is_visible()
            assert menu.locator("summary").inner_text().strip()
            switch.click()
            assert switch.get_attribute("aria-checked") == "true"
            assert page.locator("html").get_attribute("data-theme") == "dark"
            dark_colors = page.evaluate("""() => {
                const css = element => getComputedStyle(document.querySelector(element));
                return {
                  background: css('body').backgroundColor,
                  foreground: css('body').color,
                  card: css('.home-audiences .card').backgroundColor,
                  header: css('.header').backgroundColor
                };
            }""")
            assert dark_colors["background"] == "rgb(8, 23, 38)", dark_colors
            assert dark_colors["card"] != "rgb(255, 255, 255)", dark_colors
            assert dark_colors["foreground"] != dark_colors["background"], dark_colors
            page.reload(wait_until="domcontentloaded")
            assert page.locator("html").get_attribute("data-theme") == "dark"
            assert page.locator("[data-theme-switch]").get_attribute("aria-checked") == "true"
            menu.locator("summary").click()
            assert menu.get_attribute("open") is not None
            assert menu.locator("a").count() == 3
            for target in ("fr", "ar", "en"):
                link = menu.locator(f"a[lang='{target}']")
                assert link.get_attribute("href") == f"/{target}/", (lang, target)
                assert (link.get_attribute("aria-current") == "page") == (target == lang)
            next_lang = "en" if lang != "en" else "fr"
            menu.locator(f"a[lang='{next_lang}']").click()
            page.wait_for_url(f"**/{next_lang}/")
            assert page.locator("html").get_attribute("lang") == next_lang
            assert page.locator("html").get_attribute("data-theme") == "dark"
            menu = page.locator("[data-language-picker]")
            menu.locator("summary").click()
            page.keyboard.press("Escape")
            assert menu.get_attribute("open") is None
            page.locator("[data-theme-switch]").click()
            assert page.locator("html").get_attribute("data-theme") == "light"
            page.evaluate("localStorage.removeItem('nextgen-ui-theme')")
            page.emulate_media(color_scheme="dark")
            page.reload(wait_until="domcontentloaded")
            assert page.locator("html").get_attribute("data-theme") == "dark"
            page.set_viewport_size({"width": 320, "height": 720})
            overflow = page.evaluate("document.documentElement.scrollWidth - innerWidth")
            assert overflow <= 4, (lang, "theme header overflow", overflow)
            page.screenshot(path=str(SHOTS / f"{lang}-night-header-320.png"))
        finally:
            page.close()
    # Native <details> language links remain functional with JS disabled.
    no_js = browser.new_page(java_script_enabled=False, viewport={"width": 320, "height": 720})
    try:
        no_js.goto(base + "/fr/", wait_until="domcontentloaded")
        no_js.locator("[data-language-picker] summary").click()
        no_js.locator("[data-language-picker] a[lang='ar']").click()
        assert no_js.locator("html").get_attribute("lang") == "ar"
    finally:
        no_js.close()



def check_v3_reduced_motion_and_data_saver(browser, base: str) -> None:
    """Lot 109: pause button is for news; film remains independent and data-safe."""
    for lang in ("fr", "ar", "en"):
        page = browser.new_page(viewport={"width": 320, "height": 720})
        try:
            page.emulate_media(reduced_motion="reduce", color_scheme="light")
            response = page.goto(f"{base}/{lang}/", wait_until="domcontentloaded")
            assert response is not None and response.status == 200
            toggle = page.locator("[data-welcome-toggle]")
            player = page.locator("[data-welcome-video]")
            assert toggle.is_hidden(), (lang, "no useless button when news motion is disabled")
            assert player.get_attribute("src") in (None, ""), (lang, "reduced motion eager video")
            assert page.locator('link[rel="preload"][as="image"][fetchpriority="high"]').count() == 1, lang
            assert page.evaluate("document.documentElement.scrollWidth-innerWidth") <= 4, (lang, "320px overflow")
            page.screenshot(path=str(SHOTS / f"{lang}-v3-reduced-motion-320.png"))
        finally:
            page.close()
    page = browser.new_page(viewport={"width": 390, "height": 844})
    try:
        page.add_init_script(
            "Object.defineProperty(navigator,'connection',{configurable:true,"
            "value:{saveData:true}})"
        )
        page.goto(base + "/fr/", wait_until="domcontentloaded")
        toggle = page.locator("[data-welcome-toggle]")
        player = page.locator("[data-welcome-video]")
        toggle.wait_for(state="visible")
        assert toggle.inner_text() == "Ⅱ", "Ticker should move with Data Saver enabled"
        assert player.get_attribute("src") in (None, ""), "Data Saver eagerly fetched MP4"
        toggle.click()
        assert toggle.inner_text() == "▶" and toggle.get_attribute("aria-pressed") == "true"
        assert player.get_attribute("src") in (None, ""), "Ticker button triggered video"
        toggle.click()
        assert toggle.inner_text() == "Ⅱ" and toggle.get_attribute("aria-pressed") == "false"
    finally:
        page.close()


def check_about_video_first(browser, base: str) -> None:
    """Lot 112: title, silent film, description, then industrial steps (FR/AR/EN)."""
    for lang in ("fr", "ar", "en"):
        for size,width,height in (("mobile", 320, 720), ("desktop", 1280, 900)):
            page=browser.new_page(viewport={"width":width,"height":height})
            try:
                page.emulate_media(reduced_motion="reduce")
                response=page.goto(f"{base}/{lang}/a-propos/",wait_until="domcontentloaded")
                assert response is not None and response.status == 200, (lang,size)
                hero=page.locator("main > .about-video-intro:first-child")
                assert hero.count() == 1, (lang,size,"About intro must lead main")
                heading=hero.locator("h1.about-video-title")
                player=hero.locator("[data-about-video]")
                lead=hero.locator(".about-video-lead")
                approach=page.locator("main .industrial-approach")
                assert heading.count()==1 and heading.is_visible(), (lang,size,"missing heading")
                assert player.count()==1 and player.is_visible(), (lang,size,"missing video")
                assert lead.count()==1 and lead.is_visible(), (lang,size,"missing description")
                assert approach.count()==1 and approach.is_visible(), (lang,size,"missing industrial section")
                assert page.locator("[data-about-video]").count()==1, (lang,"duplicate video")
                assert page.locator("main > .page-head").count()==0, (lang,"redundant heading")
                assert page.locator("#about-heading").count()==0, (lang,"obsolete mission")
                assert page.locator(".industrial-step").count()==3, (lang,"3 steps required")
                assert hero.locator(".eyebrow").count()==0, (lang,"no redundant NextGen label")
                assert player.get_attribute("src")=="/videos/nextgen-about-v1.mp4",lang
                assert player.get_attribute("preload")=="none",lang
                assert player.get_attribute("controls") is not None,lang
                title_box=heading.bounding_box()
                video_box=player.bounding_box()
                lead_box=lead.bounding_box()
                approach_box=approach.bounding_box()
                assert title_box and video_box and lead_box and approach_box, (lang,size)
                assert title_box["y"]+title_box["height"] <= video_box["y"]+2, (lang,size,"title must precede video")
                assert video_box["y"]+video_box["height"] <= lead_box["y"]+2, (lang,size,"description must follow video")
                assert lead_box["y"]+lead_box["height"] <= approach_box["y"]+2, (lang,size,"steps must follow description")
                assert video_box["height"]>100 and video_box["width"]>270, (lang,size,video_box)
                # Even native controls cannot permanently enable soundtrack in this interim version.
                page.wait_for_function("""() => {
                  const v=document.querySelector('[data-about-video]');
                  return v && v.muted && v.volume===0;
                }""")
                player.evaluate("el => { el.muted=false; el.volume=1; }")
                page.wait_for_function("""() => {
                  const v=document.querySelector('[data-about-video]');
                  return v && v.muted && v.volume===0;
                }""")
                if size=="mobile":
                    assert title_box["y"]<200, (lang,title_box)
                    assert page.evaluate("document.documentElement.scrollWidth-innerWidth")<=4, (lang,"horizontal overflow")
                    page.screenshot(path=str(SHOTS / f"{lang}-about-title-video-lead-mobile.png"))
            finally:
                page.close()



def check_localized_news_ticker(browser, base: str) -> None:
    """Lot 108: visible nonclickable news; Arabic marquee travels right, FR/EN left."""
    for lang in ("fr", "ar", "en"):
        for motion in ("reduce", "no-preference"):
            page = browser.new_page(viewport={"width": 390, "height": 844})
            try:
                page.emulate_media(reduced_motion=motion)
                response = page.goto(f"{base}/{lang}/", wait_until="domcontentloaded")
                assert response is not None and response.status == 200
                ticker = page.locator("[data-news-ticker]")
                assert ticker.count() == 1, lang
                assert ticker.locator("a").count() == 0, (lang, "news must not be clickable")
                assert page.locator("[data-welcome-toggle]").count() == 1, lang
                result = page.evaluate("""() => {
                  const view = document.querySelector('.welcome-news-viewport').getBoundingClientRect();
                  const track = document.querySelector('.welcome-news-track');
                  const first = track.querySelector('.welcome-news-group:first-child .welcome-news-item:not([hidden])');
                  const visible = [...track.querySelectorAll('.welcome-news-item:not([hidden])')].some(el => {
                    const box=el.getBoundingClientRect();
                    return box.right > view.left && box.left < view.right &&
                           box.bottom > view.top && box.top < view.bottom;
                  });
                  const css=getComputedStyle(track);
                  return { visible, width:view.width, firstWidth:first?.getBoundingClientRect().width ?? 0,
                           direction:css.direction, animation:css.animationDirection,
                           name:css.animationName };
                }""")
                assert result["direction"] == "ltr", (lang, motion, result)
                assert result["visible"] and result["width"] > 0 and result["firstWidth"] > 0, (lang, motion, result)
                if motion == "no-preference":
                    expected = "reverse" if lang == "ar" else "normal"
                    assert result["animation"] == expected, (lang, result)
                    assert result["name"] != "none", (lang, result)
                    # Sample the actual movement direction without waiting for animation frames.
                    direction = page.evaluate("""() => {
                      const track = document.querySelector('.welcome-news-track');
                      const anim = track.getAnimations().find(a => a.effect);
                      if (!anim) return null;
                      anim.pause();
                      anim.currentTime=1000;
                      const a=track.getBoundingClientRect().x;
                      anim.currentTime=3000;
                      const b=track.getBoundingClientRect().x;
                      return b-a;
                    }""")
                    assert direction is not None, (lang, "no motion")
                    assert (direction > 0) == (lang == "ar"), (lang, direction)
                else:
                    assert result["name"] == "none", (lang, result)
            finally:
                page.close()


def check_localized_skip_keyboard(browser, base: str) -> None:
    """Lot 94: keyboard-only skip links work on 320px FR/AR/EN, even without JS."""
    labels = {
        "fr": "Aller au contenu principal",
        "ar": "الانتقال إلى المحتوى الرئيسي",
        "en": "Skip to main content",
    }
    for lang, expected in labels.items():
        page = browser.new_page(viewport={"width": 320, "height": 720},
                                java_script_enabled=False)
        try:
            response = page.goto(f"{base}/{lang}/", wait_until="domcontentloaded")
            assert response is not None and response.status == 200, lang
            assert page.locator("html").get_attribute("dir") == (
                "rtl" if lang == "ar" else "ltr"
            ), lang
            skip = page.locator("a.skip")
            assert skip.count() == 1 and skip.inner_text().strip() == expected, lang
            page.keyboard.press("Tab")
            assert skip.evaluate("el => document.activeElement === el"), (lang, "skip not first")
            assert skip.is_visible(), (lang, "focused skip link not visible")
            page.keyboard.press("Enter")
            assert page.evaluate("window.location.hash") == "#main", lang
            assert page.locator("main#main").count() == 1, lang
            width = page.evaluate("document.documentElement.scrollWidth - innerWidth")
            assert width <= 4, (lang, "skip/RTL mobile overflow", width)
            # The label must be consistent across institutional pages.
            page.goto(f"{base}/{lang}/contact/", wait_until="domcontentloaded")
            assert page.locator("a.skip").inner_text().strip() == expected, lang
        finally:
            page.close()


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
            check_header_preferences(browser, base)
            check_lot118_global_search(browser, base)
            check_v3_reduced_motion_and_data_saver(browser, base)
            check_localized_news_ticker(browser, base)
            check_about_video_first(browser, base)
            check_localized_skip_keyboard(browser, base)
            for lang in ("fr", "ar", "en"):
                for size, width, height in (("desktop", 1280, 900), ("mobile", 390, 844)):
                    page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
                    page.on("pageerror", lambda err: errors.append(str(err)))
                    for section in ("", "contact", "distributeurs", "catalogue", "gammes", "a-propos", "ressources"):
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
                            assert page.locator(".hero-status[role='note']").count() == 0, path
                            welcome = page.locator("[data-welcome-card]")
                            assert welcome.count() == 1, path
                            assert page.locator(".v3-featured-card").count() == 3, path
                            assert page.locator(".v3-hero-signal .v3-signal-item").count() == 3, path
                            if size == "mobile":
                                heading_box = page.locator(".v3-hero-heading").bounding_box()
                                video_box = welcome.bounding_box()
                                summary_box = page.locator(".v3-hero-summary").bounding_box()
                                assert heading_box and video_box and summary_box, path
                                assert heading_box["y"] + heading_box["height"] <= video_box["y"] + 3, path
                                assert video_box["y"] + video_box["height"] <= summary_box["y"] + 3, path
                            video = welcome.locator("[data-welcome-video]")
                            assert video.count() == 1, path
                            expected_video = ("/videos/nextgen-nexo-geno-welcome-v4.mp4?v=20261107-v4"
                                if (ROOT / "public/videos/nextgen-nexo-geno-welcome-v4.mp4").is_file()
                                else "/videos/nextgen-nexo-geno-welcome.mp4?v=20261105-v3")
                            assert video.get_attribute("data-src") == expected_video, path
                            assert page.locator(".v3-hero-eyebrow").count() == 0, path
                            assert page.locator(".hero-status").count() == 0, path
                            assert page.locator(".v3-hero-proof").count() == 0, path
                            assert video.get_attribute("poster") == (
                                "/videos/nextgen-nexo-geno-poster-v4.webp?v=20261107-v4"), path
                            assert video.get_attribute("preload") == "none", path
                            assert video.get_attribute("muted") is not None, path
                            assert video.get_attribute("playsinline") is not None, path
                            assert video.get_attribute("loop") is not None, path
                            assert welcome.locator(".welcome-video-cta").get_attribute("href") == (
                                "/" + lang + "/catalogue/"), path
                            assert page.locator("[data-hero-slider]").count() == 0, path
                            assert page.locator(".hero-mascot-card").count() == 0, path
                            toggle = welcome.locator("[data-welcome-toggle]")
                            toggle.wait_for(state="visible", timeout=5000)
                            assert toggle.inner_text() == "Ⅱ", path
                            assert welcome.locator(".welcome-news-track").evaluate(
                                "el => getComputedStyle(el).animationPlayState") == "running", path
                            video_before = welcome.locator("[data-welcome-video]").evaluate("el => el.paused")
                            toggle.click()
                            assert toggle.inner_text() == "▶", path
                            assert toggle.get_attribute("aria-pressed") == "true", path
                            assert welcome.locator(".welcome-news-track").evaluate(
                                "el => getComputedStyle(el).animationPlayState") == "paused", path
                            assert welcome.locator("[data-welcome-video]").evaluate(
                                "el => el.paused") == video_before, path
                            toggle.click()
                            assert toggle.inner_text() == "Ⅱ", path
                            assert toggle.get_attribute("aria-pressed") == "false", path
                            assert welcome.locator(".welcome-news-track").evaluate(
                                "el => getComputedStyle(el).animationPlayState") == "running", path
                            if size == "desktop":
                                no_js = browser.new_page(java_script_enabled=False)
                                try:
                                    no_js.goto(base + path, wait_until="domcontentloaded")
                                    assert no_js.locator("[data-welcome-video]").count() == 1, path
                                    assert no_js.locator("[data-welcome-video]").get_attribute("poster") == (
                                        "/videos/nextgen-nexo-geno-poster-v4.webp?v=20261107-v4"), path
                                    assert no_js.locator(".welcome-video-cta").is_visible(), path
                                    assert not no_js.locator("[data-welcome-toggle]").is_visible(), path
                                finally:
                                    no_js.close()
                            assert page.locator(".home-approach .editorial-caution").count() == 1, path
                            assert page.locator(".home-approach .chip").count() == 3, path
                            assert page.locator(".home-audiences .card").count() == 2, path
                            paths = page.locator(".home-audiences .card a").evaluate_all(
                                "links => links.map(a => a.getAttribute('href'))")
                            assert paths == ["/"+lang+"/contact/", "/"+lang+"/distributeurs/"], path
                            assert page.locator(".hero .btn-outline").get_attribute("href") == "/"+lang+"/contact/", path
                            assert welcome.evaluate(
                                "e => getComputedStyle(e).borderRadius !== '0px'"
                            ), path
                        if section == "catalogue":
                            assert page.locator(".concept-product-card").count() == 50, path
                            assert page.locator(".concept-product-code").count() == 50, path
                            expected_format = {"fr":"Sac 25 kg","ar":"كيس 25 كغ","en":"25 kg bag"}[lang]
                            assert expected_format in page.locator("#catalogue-bond .concept-formats").first.inner_text(), path
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
                        if section == "a-propos":
                            assert page.locator(".industrial-step").count() == 3, path
                            assert page.locator(".industrial-step img[src^='/images/approche/']").count() == 3, path
                            assert page.locator(".industrial-link").get_attribute("href") == f"/{lang}/contact/", path
                            assert page.locator(".industrial-disclaimer[role='note']").count() == 1, path
                        if section == "ressources":
                            assert page.locator(".resource-card").count() == 2, path
                            assert page.locator(".resource-card-demo").count() == 0, path
                            assert page.locator(".resource-support a[href$='/contact/']").count() == 1, path
                            assert page.locator(".resource-support a").count() == 1, path
                            assert page.locator("a[href*='/maquettes/']").count() == 0, path
                            assert page.locator(".resource-card a[href$='/documentation/']").count() == 1, path
                            assert page.locator(".resource-card a[href*='mailto:']").count() == 0, path
                        if section in ("contact", "distributeurs"):
                            assert page.locator(".contact-direct .contact-channel").count() == 3, path
                            assert page.locator(".contact-channel a[href^='mailto:']").count() == 1, path
                            assert page.locator(".contact-channel a[href^='tel:']").count() == 1, path
                            whatsapp = page.locator(".contact-channel a[href^='https://wa.me/']")
                            assert whatsapp.count() == 1, path
                            assert whatsapp.get_attribute("rel") == "noopener noreferrer", path
                            assert page.locator(".contact-direct .contact-disclosure[role='note']").count() == 1, path
                            assert page.locator(".lead-preview, .lead-panel").count() == 0, path
                            # A global, local-only search field is allowed; no contact/lead input.
                            assert page.locator("form, input:not([data-search-input]), textarea").count() == 0, path
                            assert page.locator("input[data-search-input][type=search]").count() == 1, path
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
                            or (size == "mobile" and section in ("gammes", "a-propos", "ressources", "distributeurs"))
                            or (size == "desktop" and lang == "ar" and section in ("gammes", "a-propos"))):
                            page.screenshot(path=str(SHOTS / (lang + "-" + size + "-" + (section or "home") + ".png")), full_page=True)
                            snapshots += 1
                    # Obsolete routes are no longer part of the static build.
                    assert not (DIST / lang / "emballages").exists(), lang
                    assert not (DIST / "models-demo").exists()
                    assert not (DIST / "images" / "3d-demo").exists()
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
                    # Lot 47: product information organized into accessible native accordions.
                    url = base + "/" + lang + "/documentation/fenek-bond-c1t/"
                    response = page.goto(url, wait_until="domcontentloaded")
                    assert response and response.status == 200, (lang, url)
                    assert page.locator(".fenek-product-intro").count() == 1, lang
                    assert page.locator(".fenek-product-image img").evaluate(
                        "img => img.complete && img.naturalWidth > 0"), lang
                    assert page.locator(".fenek-section-nav a").count() == 4, lang
                    assert page.locator(".fenek-doc-accordion").count() == 8, lang
                    assert page.locator('.fenek-qualification-panel').count() == 2, lang
                    assert page.locator(".fenek-doc-accordion[open]").count() == 3, lang
                    for marker in ("fenek-overview", "fenek-details",
                                   "fenek-application", "fenek-documents"):
                        assert page.locator("#" + marker).count() == 1, (lang, marker)
                    assert page.locator("meta[name='robots']").get_attribute("content") == "noindex,nofollow", lang
                    assert page.locator(".fenek-document-row button[data-print-market-sheet]").count() == 1, lang
                    # Lot 49: browser PDF prints a dedicated branded A4 document.
                    assert page.locator(".fenek-print-document").count() == 1, lang
                    assert page.locator(".fenek-print-logo").get_attribute("src") == "/images/Logo1.jpg", lang
                    assert not page.locator(".fenek-print-document").is_visible(), lang
                    page.emulate_media(media="print")
                    assert page.locator(".fenek-print-document").is_visible(), lang
                    assert not page.locator(".fenek-product-page").is_visible(), lang
                    assert page.locator(".fenek-print-packshot img").evaluate(
                        "img => img.complete && img.naturalWidth > 0"), lang
                    if size == "desktop":
                        pdf_path = SHOTS / ("fenek-bond-c1t-branded-print-" + lang + ".pdf")
                        pdf_bytes = page.pdf(path=str(pdf_path), print_background=True,
                                             prefer_css_page_size=True)
                        assert pdf_bytes.startswith(b"%PDF") and len(pdf_bytes) > 10000, lang
                        # Chromium PDFs keep uncompressed page dictionaries:
                        # prohibit a nearly blank orphan page on the C1T reference.
                        pdf_page_count = len(re.findall(rb"/Type\s*/Page\b", pdf_bytes))
                        assert pdf_page_count == 1, (lang, pdf_page_count)
                    page.emulate_media(media="screen")
                    assert page.locator(".fenek-product-page").is_visible(), lang
                    assert not page.locator(".fenek-print-document").is_visible(), lang
                    assert page.locator("form").count() == 0, lang
                    accordion = page.locator("#fenek-details .fenek-doc-accordion").nth(1)
                    assert accordion.get_attribute("open") is None, lang
                    accordion.locator("summary").click()
                    assert accordion.get_attribute("open") is not None, lang
                    accordion.locator("summary").focus()
                    page.keyboard.press("Enter")
                    assert accordion.get_attribute("open") is None, lang
                    open_states = page.evaluate("""() => {
                        const list = Array.from(document.querySelectorAll('.fenek-doc-accordion'));
                        const before = list.map(d => d.open);
                        window.dispatchEvent(new Event('beforeprint'));
                        const expanded = list.every(d => d.open);
                        window.dispatchEvent(new Event('afterprint'));
                        return {expanded, restored: list.every((d,i) => d.open === before[i])};
                    }""")
                    assert open_states["expanded"] and open_states["restored"], (lang, open_states)
                    assert page.locator(".market-reference,.market-sheet-warning").count() == 0, lang
                    for other_brand in ("Sika", "Mapei", "Fosroc", "Jotun", "Granitex", "Weber"):
                        assert other_brand.lower() not in page.locator("main").inner_text().lower(), (
                            lang, other_brand)
                    overflow = page.evaluate("Math.ceil(document.documentElement.scrollWidth-innerWidth)")
                    assert overflow <= 4, (lang,size,overflow)
                    page.goto(base + "/" + lang + "/documentation/", wait_until="domcontentloaded")
                    assert page.locator(".market-index-card").count() == 50, lang
                    assert page.locator(".market-sheet-warning").count() == 0, lang
                    if size == "desktop":
                        for slug in (
                            "fenek-bond-gp-csii", "fenek-bond-m5", "fenek-bond-m10",
                            "fenek-bond-oc-csiii", "fenek-flow-ci", "fenek-paint-ent-l",
                            "fenek-paint-prim-a", "fenek-paint-prim-fx",
                            "fenek-paint-txt-f", "fenek-proof-ep-sb", "fenek-proof-pu-inj",
                        ):
                            url = base + "/" + lang + "/documentation/" + slug + "/"
                            response = page.goto(url, wait_until="domcontentloaded")
                            assert response and response.status == 200, (lang, url)
                            assert page.locator(".fenek-doc-accordion").count() == 8, (lang, slug)
                            assert page.locator('.fenek-qualification-panel').count() == 2, (lang, slug)
                            assert page.locator(".market-reference").count() == 0, (lang, slug)
                            assert page.locator(".fenek-product-image img").evaluate(
                                "img => img.complete && img.naturalWidth > 0"), (lang,slug)
                    if lang == "ar":
                        assert page.locator("html").get_attribute("dir") == "rtl", lang

                    # Explicitly follow the language navigation to another localized page.
                    page.goto(base + "/" + lang + "/contact/", wait_until="domcontentloaded")
                    assert page.locator(".locale a").count() == 3
                    page.locator("[data-language-picker] summary").click()
                    assert page.locator("[data-language-picker]").get_attribute("open") is not None
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
    print(f"PASS: 42 browser route/viewport checks, 6 language-switch clicks, 9 responsive menus, {snapshots} screenshots")


if __name__ == "__main__":
    check()
