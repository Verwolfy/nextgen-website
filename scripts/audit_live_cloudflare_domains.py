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

if __name__ == "__main__":
    main()
