#!/usr/bin/env python3
"""Read-only, anonymous check of the currently hosted NextGen welcome V4.

No authentication, secret, publish, DNS mutation or Cloudflare API is used.
HTTP redirects are deliberately NOT followed: they may be Access login pages.
This is diagnostic evidence, not authorization to publish.
"""
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener

ORIGINS = (
    "https://nextgen-buildingsolutions.com",
    "https://www.nextgen-buildingsolutions.com",
    # Historical Pages host reported by the project, not independently verified.
    "https://nextgen-website-8te.pages.dev",
)
VIDEO = "/videos/nextgen-nexo-geno-welcome-v4.mp4?v=20261107-v4"
POSTER = "/videos/nextgen-nexo-geno-poster-v4.webp?v=20261107-v4"
MARKER = "nextgen-nexo-geno-welcome-v4.mp4?v=20261107-v4"
EXPECTED_VIDEO_SHA256 = "e7ac28368254aff457c57067c79adf2973584becbfc9e2375180e20301494a13"
EXPECTED_POSTER_SHA256 = "7a4ba9144d9bde9844fb779b24eab728e408e11682c6ad5095be45756f3fd90b"
MAX_BYTES = 800_000


class StopRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


def inspect_url(url: str) -> tuple[dict, bytes]:
    """Use a bounded GET and report status; never follow login redirects."""
    req = Request(
        url,
        headers={"User-Agent": "NextGen-release-readonly-audit/1.0", "Accept": "*/*"},
        method="GET",
    )
    opener = build_opener(StopRedirect())
    try:
        with opener.open(req, timeout=9) as response:
            body = response.read(MAX_BYTES + 1)
            return {
                "status": response.status,
                "oversized": len(body) > MAX_BYTES,
                "bytes_read": min(len(body), MAX_BYTES),
                "type": (response.headers.get("Content-Type") or "").split(";")[0],
            }, body[:MAX_BYTES]
    except HTTPError as exc:
        # A 30x may be a legitimate www redirect or Cloudflare Access.
        return {
            "status": exc.code,
            "redirect_host": urlparse(exc.headers.get("Location", "")).hostname,
        }, b""
    except (URLError, TimeoutError, OSError) as exc:
        return {"status": "network_error", "error_type": type(exc).__name__}, b""


def classify(home: dict, video: dict | None, poster: dict | None) -> str:
    status = home["status"]
    if status in (401, 403):
        return "access_protected_or_blocked"
    if status in (301, 302, 303, 307, 308):
        return "redirect_not_followed"
    if status == "network_error":
        return "unreachable_from_runner"
    if status != 200:
        return "unverified_http_status"
    if not home.get("v4_marker"):
        return "v4_not_visible_on_home"
    if not video or not poster:
        return "assets_not_checked"
    if video.get("sha256_match") and poster.get("sha256_match"):
        return "v4_verified_anonymously_accessible"
    return "html_updated_but_assets_not_v4"


def audit_origin(origin: str) -> dict:
    home, html = inspect_url(origin + "/fr/")
    if home["status"] == 200:
        home["v4_marker"] = MARKER.encode("ascii") in html
    video = poster = None
    if home["status"] == 200 and home.get("v4_marker"):
        video, v_body = inspect_url(origin + VIDEO)
        video["sha256_match"] = (
            video["status"] == 200 and not video.get("oversized")
            and hashlib.sha256(v_body).hexdigest() == EXPECTED_VIDEO_SHA256
        )
        poster, p_body = inspect_url(origin + POSTER)
        poster["sha256_match"] = (
            poster["status"] == 200 and not poster.get("oversized")
            and hashlib.sha256(p_body).hexdigest() == EXPECTED_POSTER_SHA256
        )
    return {
        "origin": origin,
        "home": home,
        "video": video,
        "poster": poster,
        "result": classify(home, video, poster),
    }


def main() -> None:
    report = {
        "checked_utc": datetime.now(timezone.utc).isoformat(),
        "expected_main_commit": os.environ.get("GITHUB_SHA", "unavailable"),
        "read_only": True,
        "performed_deployment": False,
        "checks": [audit_origin(origin) for origin in ORIGINS],
    }
    out = Path(".ci-artifacts/lot62-live-check.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        lines = [
            "## NextGen — diagnostic HTTP V4 (lecture seule)",
            "",
            "**Aucun déploiement, aucune connexion Cloudflare, aucune modification DNS.**",
            "",
            "| Origine | HTTP page FR | V3 | Résultat |",
            "|---|---|---|---|",
        ]
        for check in report["checks"]:
            lines.append(
                f"| {check['origin']} | {check['home']['status']} | "
                f"{'oui' if check['home'].get('v4_marker') else 'non vérifié'} | {check['result']} |"
            )
        lines += [
            "",
            "Un HTTP 200 anonyme signifie que la page est accessible publiquement, même avec noindex.",
            "Une redirection vers Cloudflare Access ne prouve pas le contenu de la version déployée.",
            "Si aucun résultat n'est `v4_verified_anonymously_accessible`, la mise en ligne V4 demeure non confirmée.",
            "",
        ]
        with open(summary, "a", encoding="utf-8") as stream:
            stream.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
