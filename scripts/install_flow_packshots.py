#!/usr/bin/env python3
"""Install reviewed FENEK-FLOW concept WebPs from a local ZIP, never from an unknown URL.

Usage:
    python scripts/install_flow_packshots.py /path/to/NextGen_FENEK_FLOW_12_packshots_lot21.zip

The ZIP is the private review artifact created from 12 distinct AI mockups.
This script never changes product approval flags or external services.
"""
import hashlib
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "public" / "images" / "catalogue-projects"
EXPECTED = {
    "fenek-flow-ac", "fenek-flow-ae", "fenek-flow-ci", "fenek-flow-cure",
    "fenek-flow-lat", "fenek-flow-rt", "fenek-flow-sp-hr",
    "fenek-flow-sp-pf", "fenek-flow-sp-rt", "fenek-flow-vma",
    "fenek-flow-wp", "fenek-flow-wr-n"
}

def check_package(archive: zipfile.ZipFile) -> dict[str, bytes]:
    manifest = json.loads(archive.read("catalogue-packshots-manifest.json"))
    assert manifest["category"] == "flow"
    items = manifest["assets"]
    assert len(items) == 12
    assert {item["slug"] for item in items} == EXPECTED
    all_bytes = {}
    for item in items:
        for name_key, hash_key in (("full", "full_sha256"), ("card", "card_sha256")):
            raw_path = item[name_key]
            expected_path = "public/images/catalogue-projects/" + item["slug"] + (
                "-card.webp" if name_key == "card" else ".webp"
            )
            assert raw_path == expected_path, raw_path
            raw = archive.read(raw_path)
            assert raw.startswith(b"RIFF") and raw[8:12] == b"WEBP", raw_path
            assert hashlib.sha256(raw).hexdigest() == item[hash_key], raw_path
            assert 20_000 < len(raw) < 600_000, raw_path
            all_bytes[expected_path] = raw
    assert len(all_bytes) == 24
    return all_bytes

def main(archive_path: Path) -> None:
    with zipfile.ZipFile(archive_path) as z:
        payload = check_package(z)
    # All validation occurs before copying a single image.
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    for relative, data in payload.items():
        dest = ROOT / relative
        dest.write_bytes(data)
    assert len(list(ASSET_DIR.glob("fenek-flow-*.webp"))) >= 24
    print("PASS: 12/12 FENEK-FLOW concepts installed (24 WebPs), no distortion.")
    print("NEXT: commit assets in the private repo, then run Astro/Chromium CI.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/install_flow_packshots.py <reviewed-ZIP>")
    main(Path(sys.argv[1]))
