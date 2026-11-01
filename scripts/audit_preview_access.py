#!/usr/bin/env python3
"""Anonymous, read-only Cloudflare Pages Access probe. No credentials or body logs.

NEVER authorizes release: a login challenge only demonstrates one tested route.
Offline unless explicitly invoked with --execute and exact approved URLs.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener


@dataclass(frozen=True)
class Result:
    category: str
    host: str
    status: str
    code: int | None = None


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


def valid_url(url: str, expected_project: str, category: str) -> str:
    parts = urlsplit(url)
    host = parts.hostname or ''
    if (parts.scheme != 'https' or parts.username or parts.password or parts.port
            or parts.path not in ('', '/') or parts.query or parts.fragment):
        raise ValueError('Only bare HTTPS origins can be checked')
    if not expected_project or not all(c.isascii() and (c.isalnum() or c == '-') for c in expected_project):
        raise ValueError('Invalid project name')
    root = expected_project + '.pages.dev'
    if category == 'primary' and host != root:
        raise ValueError('Primary must be the exact Pages domain')
    if category == 'preview':
        # Do not confuse the primary deployment with a protected preview.
        if host == root or not host.endswith('.' + root) or len(host[:-len('.' + root)]) < 1:
            raise ValueError('Preview must be a distinct Pages alias')
    if category == 'custom' and (host == root or host.endswith('.pages.dev') or not host or '.' not in host):
        raise ValueError('Custom domain must be a different fully qualified hostname')
    if category not in {'primary', 'preview', 'custom'}:
        raise ValueError('Unknown category')
    return host


def challenge_location(location: str | None, current_host: str) -> bool:
    if not location:
        return False
    parts = urlsplit(location)
    host = (parts.hostname or '').lower()
    if parts.scheme not in {'', 'https'} or parts.username or parts.password:
        return False
    if host and host.endswith('.cloudflareaccess.com') and host != 'cloudflareaccess.com':
        return True
    if (not host or host == current_host) and parts.path.startswith('/cdn-cgi/access/'):
        return True
    return False


def classify(code: int, location: str | None, current_host: str) -> str:
    if code in (301, 302, 303, 307, 308) and challenge_location(location, current_host):
        return 'ACCESS_CHALLENGE_OBSERVED'
    if code == 200:
        return 'EXPOSED_ANONYMOUSLY'
    return 'INCONCLUSIVE_NOT_PROOF_OF_ACCESS'


def probe(category: str, url: str, expected_project: str, opener=None) -> Result:
    host = valid_url(url, expected_project, category)
    opener = opener or build_opener(NoRedirect())
    request = Request(urlunsplit(('https', host, '/', '', '')),
                      headers={'User-Agent': 'NextGen-Access-ReadOnly-Audit/1.0'},
                      method='GET')
    try:
        with opener.open(request, timeout=12) as response:
            code = response.status
            location = response.headers.get('Location')
    except HTTPError as exc:
        code = exc.code
        location = exc.headers.get('Location')
    except (URLError, OSError, TimeoutError):
        return Result(category, host, 'NETWORK_INCONCLUSIVE')
    return Result(category, host, classify(code, location, host), code)


def main() -> int:
    parser = argparse.ArgumentParser(description='Anonymous Pages Access probe, NO RELEASE AUTHORIZATION')
    parser.add_argument('--project', required=True, help='Exact existing Cloudflare Pages project name')
    parser.add_argument('--primary', required=True, help='Existing https://project.pages.dev origin')
    parser.add_argument('--preview', action='append', required=True, help='Existing branch or hash preview origin')
    parser.add_argument('--custom', action='append', default=[], help='Any already-associated custom domain')
    parser.add_argument('--execute', action='store_true', help='Opt in to network reads against exact URLs')
    args = parser.parse_args()
    targets = [('primary', args.primary), *[('preview', x) for x in args.preview],
               *[('custom', x) for x in args.custom]]
    try:
        validated = [(category, url, valid_url(url, args.project, category))
                     for category, url in targets]
    except ValueError as exc:
        print('INVALID_INPUT:', str(exc))
        return 2
    if not args.execute:
        print(f'NO_NETWORK: {len(validated)} hostnames validated; GO NOT AUTHORIZED')
        return 0
    results = [probe(category, url, args.project) for category, url, _ in validated]
    for item in results:
        print(f'{item.category}: {item.host} : {item.status}' +
              (f' (HTTP {item.code})' if item.code is not None else ''))
    print('REQUIRES_OWNER_PROOF: Access policy, allowlist and authenticated QA still pending')
    return 0 if all(r.status == 'ACCESS_CHALLENGE_OBSERVED' for r in results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
