#!/usr/bin/env bash
# One-shot import of the reviewed FENEK-FLOW ZIP from an authenticated GitHub Codespace.
# Does NOT publish Cloudflare, change ERP, or mark technical certifications as approved.
set -euo pipefail

if [[ $# -ne 1 || ! -f "$1" ]]; then
  echo "Usage: bash scripts/create_flow_packshots_pr.sh /tmp/NextGen_FENEK_FLOW_12_packshots_lot21.zip" >&2
  exit 2
fi
zip_path="$(realpath "$1")"
cd "$(dirname "$0")/.."
git rev-parse --is-inside-work-tree >/dev/null
if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "Abort: commit or stash unrelated tracked changes before importing." >&2
  exit 1
fi
command -v gh >/dev/null || { echo "Install gh CLI or use the GitHub PR URL after pushing." >&2; exit 1; }

branch="assets/flow-12-packshots-$(date -u +%Y%m%d%H%M%S)"
git switch main
git pull --ff-only origin main
git switch -c "$branch"
python scripts/install_flow_packshots.py "$zip_path"
python scripts/install_flow_packshots.py --verify
python -m unittest discover -s tests -v
npm ci --no-audit --no-fund
npm run build
python scripts/check_flow_packshots_built.py
python scripts/check_built_pages.py

git add -- public/images/catalogue-projects/fenek-flow-*.webp
count="$(git diff --cached --name-only | grep -c '^public/images/catalogue-projects/fenek-flow-.*\.webp$' || true)"
if [[ "$count" -ne 24 ]]; then
  echo "Abort: expected 24 new/changed FENEK-FLOW images, got $count" >&2
  exit 1
fi
git commit -m "assets(site): 12 packshots FENEK-FLOW verified and non-contractual"
git push -u origin "$branch"
gh pr create --base main --head "$branch" \
  --title "Assets — 12 FENEK-FLOW packshots reviewed (24 WebPs)" \
  --body "Imports the 12 reviewed FENEK-FLOW concept packshots with card/full sizes. Exact SHA256 and image sizes verified against the approved manifesto, all 72 FR/AR/EN usages checked in the local Astro build. Every image remains a NON-CONTRACTUAL CONCEPT; no product approvals, Cloudflare, DNS or ERP modifications. Merge only after 2 green GitHub CI checks and visual screenshots review."
echo "PR created. Do not deploy Cloudflare until Access/security and commercial approvals are checked."
