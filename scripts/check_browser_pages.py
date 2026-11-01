#!/usr/bin/env python3
"""Local Chromium browser acceptance tests. No external deployment or secrets."""
from __future__ import annotations

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
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
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
            for lang in ("fr", "ar", "en"):
                for size, width, height in (("desktop", 1280, 900), ("mobile", 390, 844)):
                    page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
                    page.on("pageerror", lambda err: errors.append(str(err)))
                    for section in ("", "contact", "distributeurs", "catalogue", "emballages"):
                        path = "/" + lang + "/" + (section + "/" if section else "")
                        response = page.goto(base + path, wait_until="domcontentloaded", timeout=20000)
                        assert response is not None and response.status == 200, path
                        assert page.locator("html").get_attribute("lang") == lang, path
                        assert page.locator("html").get_attribute("dir") == ("rtl" if lang == "ar" else "ltr"), path
                        assert page.locator("h1").count() == 1, path
                        assert page.locator("main").count() == 1, path
                        assert page.locator("form").count() == 0, path
                        if section in ("contact", "distributeurs"):
                            all_controls = page.locator(".lead-panel input, .lead-panel textarea, .lead-panel button")
                            count = all_controls.count()
                            assert count > 5, path
                            assert all(all_controls.nth(i).is_disabled() for i in range(count)), path
                        # Overflows on phone screens make navigation unusable.
                        diff = page.evaluate("Math.ceil(document.documentElement.scrollWidth - window.innerWidth)")
                        if diff > 4:
                            overflowing = page.evaluate("""Array.from(document.querySelectorAll('*'))
                                .filter(e => e.getBoundingClientRect().right > innerWidth + 3)
                                .slice(0,8)
                                .map(e => ({tag:e.tagName, cls:String(e.className).slice(0,50), width:Math.round(e.getBoundingClientRect().width)}))""")
                            raise AssertionError(f"Horizontal overflow: {path} {width}px: {diff}px; elements={overflowing}")
                        if section in ("", "contact"):
                            page.screenshot(path=str(SHOTS / (lang + "-" + size + "-" + (section or "home") + ".png")), full_page=True)
                            snapshots += 1
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
                tiny.close()
            browser.close()
    finally:
        srv.shutdown()
        srv.server_close()
    assert not errors, "Unexpected browser JavaScript errors: " + str(errors[:5])
    print(f"PASS: 30 browser route/viewport checks, 6 language-switch clicks, 9 responsive menus, {snapshots} screenshots")


if __name__ == "__main__":
    check()
