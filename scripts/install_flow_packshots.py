#!/usr/bin/env python3
"""Install 12 verified FENEK-FLOW concept packshots from the conversation ZIP.

Usage:
    python scripts/install_flow_packshots.py /path/to/NextGen_FENEK_FLOW_12_packshots_lot21.zip
    python scripts/install_flow_packshots.py --verify

Non-contractual product visuals only. No product approval or deployment.
The trust anchor is scripts/flow-packshots-approved.json committed in GitHub.
"""
import hashlib
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "public" / "images" / "illustrations" / "produits"
APPROVED = ROOT / "scripts" / "flow-packshots-approved.json"


def approved_assets() -> tuple[dict, dict]:
    manifest = json.loads(APPROVED.read_text(encoding="utf-8"))
    assert manifest["category"] == "flow"
    assert manifest["status"] == "reviewed_visual_concept_only"
    assets = manifest["assets"]
    assert len(assets) == 12
    indexed = {p["slug"]: p for p in assets}
    assert len(indexed) == 12
    assert all(p["slug"].startswith("fenek-flow-") for p in assets)
    assert len({p["full_sha256"] for p in assets}) == 12
    assert len({p["card_sha256"] for p in assets}) == 12
    return manifest, indexed


def webp_dimensions(data: bytes) -> tuple[int, int]:
    # This controlled batch uses standard WebP lossy VP8, no animation.
    assert len(data) >= 30 and data[:4] == b"RIFF" and data[8:12] == b"WEBP"
    assert int.from_bytes(data[4:8], "little") + 8 == len(data)
    assert data[12:16] == b"VP8 " and data[23:26] == b"\x9d\x01\x2a"
    width = int.from_bytes(data[26:28], "little") & 0x3FFF
    height = int.from_bytes(data[28:30], "little") & 0x3FFF
    assert width > 0 and height > 0
    return (width, height)


def expected_files() -> dict[str, tuple[str, tuple[int, int]]]:
    approved, items = approved_assets()
    files = {}
    for slug, asset in items.items():
        for kind, key in (("full", "full_sha256"), ("card", "card_sha256")):
            name = slug + ("-card.webp" if kind == "card" else ".webp")
            files["public/images/illustrations/produits/" + name] = (
                asset[key], tuple(approved["dimensions"][kind])
            )
    assert len(files) == 24
    return files


def verify_asset(path: str, data: bytes, digest: str, dimensions: tuple[int, int]) -> None:
    assert 20_000 < len(data) < 600_000, path
    assert hashlib.sha256(data).hexdigest() == digest, path
    assert webp_dimensions(data) == dimensions, path


def check_package(archive: zipfile.ZipFile) -> dict[str, bytes]:
    inner = json.loads(archive.read("catalogue-packshots-manifest.json"))
    assert inner["category"] == "flow" and len(inner["assets"]) == 12
    expected = expected_files()
    package_paths = set()
    for asset in inner["assets"]:
        for variant, sha_key in (("full", "full_sha256"), ("card", "card_sha256")):
            name = asset[variant]
            expected_path = "public/images/illustrations/produits/" + asset["slug"] + (
                "-card.webp" if variant == "card" else ".webp"
            )
            assert name == expected_path, name
            assert name in expected and asset[sha_key] == expected[name][0], name
            package_paths.add(name)
    assert package_paths == set(expected)
    output = {}
    for path, (digest, dimensions) in expected.items():
        raw = archive.read(path)
        verify_asset(path, raw, digest, dimensions)
        output[path] = raw
    return output


def verify_installed() -> None:
    expected = expected_files()
    for relative, (digest, dims) in expected.items():
        path = ROOT / relative
        assert path.is_file(), f"Missing WebP: {relative}"
        verify_asset(relative, path.read_bytes(), digest, dims)
    print("PASS: 12/12 product-specific concepts, 24/24 images match approved SHA256 and dimensions.")


def main(archive_path: Path) -> None:
    with zipfile.ZipFile(archive_path) as archive:
        payload = check_package(archive)
    # All ZIP validation happens before writing any file.
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    for relative, data in payload.items():
        (ROOT / relative).write_bytes(data)
    verify_installed()
    print("NEXT: commit public/images/illustrations/produits/*.webp on a PR and run CI.")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--verify":
        verify_installed()
    elif len(sys.argv) == 2:
        main(Path(sys.argv[1]))
    else:
        raise SystemExit("Usage: install_flow_packshots.py <ZIP> | --verify")
