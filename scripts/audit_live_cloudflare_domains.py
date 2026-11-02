#!/usr/bin/env python3
"""Read-only diagnostic of NextGen's already-public Cloudflare Pages hosts.

No credentials, no writes, no production changes. Intended for GitHub Actions,
whose public-network access can differ from the assistant's sandbox.
"""
from __future__ import annotations
import hashlib
import re
import socket
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit

HOSTS = {
    "apex": "https://nextgen-buildingsolutions.com",
    "www": "https://www.nextgen-buildingsolutions.com",
    "pages-main": "https://nextgen-website-8te.pages.dev",
    "pages-pr27-old": "https://b2addc89.nextgen-website-8te.pages.dev",
}
PATHS = ("/fr/catalogue/", "/")
HEADERS_TO_CHECK = ("server", "cf-cache-status", "age", "cache-control",
                    "etag", "location", "cf-ray", "content-type")
MARKERS = {
    "new-c1t-gallery-render": "/images/maquettes/maquette-20.webp",
    "old-c1t-flat-label": "/images/catalogue-projects/fenek-bond-c1t-card.webp",
    "new-bond-c1te": "/images/maquettes/maquette-21.webp",
    "new-bond-gr-hr": "/images/maquettes/maquette-31.webp",
    # Lot 31: all eleven individual PAINT packshots must be linked from the
    # public catalogue. The entire proof is read-only and cannot publish data.
    "paint-ent-l": "/images/catalogue-projects/fenek-paint-ent-l.webp",
    "paint-fac-el": "/images/catalogue-projects/fenek-paint-fac-el.webp",
    "paint-fac-m": "/images/catalogue-projects/fenek-paint-fac-m.webp",
    "paint-fac-sx": "/images/catalogue-projects/fenek-paint-fac-sx.webp",
    "paint-int-m": "/images/catalogue-projects/fenek-paint-int-m.webp",
    "paint-int-s": "/images/catalogue-projects/fenek-paint-int-s.webp",
    "paint-int-wa": "/images/catalogue-projects/fenek-paint-int-wa.webp",
    "paint-prim-a": "/images/catalogue-projects/fenek-paint-prim-a.webp",
    "paint-prim-fx": "/images/catalogue-projects/fenek-paint-prim-fx.webp",
    "paint-sol-a": "/images/catalogue-projects/fenek-paint-sol-a.webp",
    "paint-txt-f": "/images/catalogue-projects/fenek-paint-txt-f.webp",
}

def one(name: str, base: str, path: str, fresh: bool = False) -> None:
    url = base + path
    if fresh:
        url += "?nextgen_diag=" + str(int(time.time() * 1000))
    request = Request(url, headers={
        "User-Agent": "NextGen-public-site-diagnostics/1.0",
        "Accept": "text/html",
        "Cache-Control": "no-cache" if fresh else "max-age=0",
    })
    try:
        with urlopen(request, timeout=12) as response:
            data = response.read(2_000_000)
            text = data.decode("utf-8", errors="replace")
            headers = {h: response.headers.get(h, "-") for h in HEADERS_TO_CHECK}
            marks = {key: needle in text for key, needle in MARKERS.items()}
            html_title = re.search(r"<title>([^<]{0,180})</title>", text, re.I)
            print({
                "site": name, "path": path, "fresh": fresh,
                "http": response.status, "final_url": response.geturl(),
                "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()[:20],
                "markers": marks if path.startswith("/fr/catalogue") else {},
                "title": html_title.group(1) if html_title else None,
                "headers": headers,
            }, flush=True)
    except HTTPError as ex:
        print({"site": name, "path": path, "fresh": fresh,
               "http": ex.code, "error": str(ex)[:120]}, flush=True)
    except (URLError, OSError, TimeoutError) as ex:
        print({"site": name, "path": path, "fresh": fresh,
               "error": repr(ex)[:220]}, flush=True)

def verify_live_paint_packshots() -> None:
    """Confirm all eleven uploaded WebPs are directly accessible in production."""
    codes = ("ent-l", "fac-el", "fac-m", "fac-sx", "int-m", "int-s",
             "int-wa", "prim-a", "prim-fx", "sol-a", "txt-f")
    ok = 0
    for code in codes:
        url = HOSTS["apex"] + "/images/catalogue-projects/fenek-paint-" + code + ".webp"
        with urlopen(Request(url, headers={"User-Agent": "NextGen-public-assets-check/1.0"}), timeout=12) as resp:
            data = resp.read(250_000)
            valid = (resp.status == 200 and data[:4] == b"RIFF" and
                     data[8:12] == b"WEBP" and len(data) > 20_000)
            print({"paint_asset": code, "http": resp.status, "webp_valid": valid,
                   "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}, flush=True)
            assert valid, "Missing or invalid public PAINT file: " + code
            ok += 1
    assert ok == 11
    print({"paint_public_assets": "11/11 accessible and valid"}, flush=True)

def audit_trilingual_catalogue_copy() -> None:
    """Read-only smoke check of the latest public catalogue descriptions."""
    checks={
      "fr": ("Gamme : Mortiers, colles et réparation.", "Concept de produit (non validé) :"),
      "en": ("Range: Mortars, adhesives and repair.", "Unvalidated product concept:"),
      "ar": ("الفئة: الملاط والمواد اللاصقة والإصلاح.", "تصور منتج غير معتمد:"),
    }
    for lang,(new,old) in checks.items():
        url=HOSTS["apex"]+"/"+lang+"/catalogue/fenek-bond-c1t/"
        req=Request(url,headers={"Cache-Control":"no-cache","User-Agent":"NextGen-editorial-public-audit/1.0"})
        with urlopen(req,timeout=12) as resp:
            html=resp.read(100_000).decode("utf-8",errors="replace")
            ok=resp.status==200 and new in html and old not in html
            print({"lang":lang,"code":"BOND-C1T","http":resp.status,
                   "new_description_visible":new in html,"legacy_description_absent":old not in html,
                   "valid":ok},flush=True)
            assert ok, "Public product text not yet updated: "+lang
    # Lot 33: the 150 generated catalogue pages retain private source
    # instructions only in the Git repository. Inspect examples on public
    # Cloudflare in every language, with cache-bypass on a GET.
    codes=("fenek-bond-c1t","fenek-proof-cm-o1p",
           "fenek-flow-wr-n","fenek-paint-int-m")
    for lang in checks:
        for code in codes:
            url=HOSTS["apex"]+"/"+lang+"/catalogue/"+code+"/?audit_lot33=1"
            req=Request(url,headers={"Cache-Control":"no-cache",
                "User-Agent":"NextGen-procedure-safety-check/1.0"})
            with urlopen(req,timeout=12) as resp:
                html=resp.read(150_000).decode("utf-8",errors="replace")
                forbidden=("[valeur à confirmer]","concept-source-method",
                           "Mode d’emploi source (brouillon français)",
                           "Original French instructions (draft)",
                           "نص طريقة الاستعمال الأصلي بالفرنسية",
                           "Contenu révisable. Les données du laboratoire",
                           "This content can be revised as laboratory",
                           "يمكن تحديث هذا المحتوى لاحقًا")
                absent=all(x not in html for x in forbidden)
                has_notice="concept-detail-note" in html
                ok=resp.status==200 and absent and has_notice
                print({"lang":lang,"product":code,"status":resp.status,
                       "draft_content_absent":absent,"documentation_notice":has_notice,
                       "valid":ok},flush=True)
                assert ok, "Public draft procedure still available: "+lang+"/"+code
    print({"lot33_public_samples":"12/12 pages checked"},flush=True)

def audit_contact_page_publication() -> None:
    """Verify 6 real public contact/distributor pages have no inactive demos."""
    checked=0
    for lang in ("fr","en","ar"):
        for section in ("contact","distributeurs"):
            url=HOSTS["apex"]+"/"+lang+"/"+section+"/?audit_lot35=1"
            req=Request(url,headers={"Cache-Control":"no-cache",
                "User-Agent":"NextGen-public-contact-audit/1.0"})
            with urlopen(req,timeout=12) as response:
                html=response.read(200_000).decode("utf-8",errors="replace")
                # Cloudflare may email-obfuscate mailto: into its own
                # /cdn-cgi/l/email-protection link in the served HTML.
                email_ok=("mailto:" in html or "/cdn-cgi/l/email-protection" in html)
                tel_ok="tel:" in html
                whatsapp_ok="https://wa.me/" in html
                demo_absent="lead-preview" not in html and "lead-panel" not in html
                ok=response.status==200 and demo_absent and email_ok and tel_ok and whatsapp_ok
                print({"section":section,"lang":lang,"http":response.status,
                       "email_link_or_cf_obfuscation":email_ok,
                       "phone_link":tel_ok,"whatsapp_link":whatsapp_ok,
                       "demo_forms_absent":demo_absent, "valid":ok,
                       "html_size":len(html)},flush=True)
                assert ok, "Live contact page still contains demo or missing channel: "+lang+"/"+section
                checked+=1
    assert checked==6
    print({"lot35_live_contact":"6/6 pages verified"},flush=True)

def main() -> None:
    for name, base in HOSTS.items():
        host = urlsplit(base).hostname
        try:
            ips = sorted({info[4][0] for info in socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)})
            print({"host": host, "dns_addresses": ips[:8]}, flush=True)
        except OSError as ex:
            print({"host": host, "dns_error": repr(ex)}, flush=True)
        for path in PATHS:
            one(name, base, path)
        one(name, base, "/fr/catalogue/", fresh=True)
    verify_live_paint_packshots()
    audit_trilingual_catalogue_copy()
    audit_contact_page_publication()

if __name__ == "__main__":
    main()
