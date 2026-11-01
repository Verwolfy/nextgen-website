#!/usr/bin/env python3
"""CI gate: no website deployment action without a separate approved process.

Scans GitHub Actions YAML only; does not pretend to prove external settings.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / '.github' / 'workflows'
FORBIDDEN = (
    r'\bwrangler\s+(?:pages\s+)?deploy\b',
    r'\bwrangler\s+pages\s+deploy\b',
    r'cloudflare/pages-action@',
    r'cloudflare/wrangler-action@',
    r'\bCLOUDFLARE_API_TOKEN\b',
    r'\bCF_API_TOKEN\b',
    r'\bpages\.deployments\.create\b',
)


def unsafe_workflows(path: Path) -> list[tuple[str, str]]:
    findings = []
    for file in sorted([*path.glob('*.yml'), *path.glob('*.yaml')]):
        content = file.read_text(encoding='utf-8')
        # Comments do not authorize a deployment, but lines with commands do.
        active = '\n'.join(line for line in content.splitlines()
                           if not line.lstrip().startswith('#'))
        for expression in FORBIDDEN:
            if re.search(expression, active, flags=re.IGNORECASE):
                findings.append((file.name, expression))
    return findings


def main() -> int:
    if not WORKFLOWS.is_dir():
        print('BLOCK: GitHub workflows folder missing')
        return 1
    bad = unsafe_workflows(WORKFLOWS)
    if bad:
        for name, pattern in bad:
            print(f'BLOCK: unapproved publication in {name}, rule {pattern}')
        return 1
    print('PASS: no Cloudflare deployment commands or provider tokens in GitHub workflows')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
