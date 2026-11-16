#!/usr/bin/env python3
"""Install 10 verified FENEK-BOND concept packshots from the conversation ZIP.

Usage:
    python scripts/install_bond_packshots.py /path/to/NextGen_FENEK_BOND_10_packshots_lot25.zip
    python scripts/install_bond_packshots.py --verify

Non-contractual product visuals only. No product approval or deployment.
The trust anchor is scripts/bond-packshots-approved.json committed in GitHub.
"""
import hashlib
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "public" / "images" / "illustrations" / "catalogue-projects"
APPROVED = ROOT / "scripts" / "bond-packshots-approved.json"


def approved_assets() -> tuple[dict, dict]:
    manifest = json.loads(APPROVED.read_text(encoding="utf-8"))
    assert manifest["category"] == "bond"
    assert manifest["status"] == "preview_non_contractual"
    assets = manifest["assets"]
    assert len(assets) == 10
    indexed = {p["slug"]: p for p in assets}
    assert len(indexed) == 10
    assert all(p["slug"].startswith("fenek-bond-") for p in assets)
    assert len({p["full_sha256"] for p in assets}) == 10
    assert len({p["card_sha256"] for p in assets}) == 10
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
            files["public/images/illustrations/catalogue-projects/" + name] = (
                asset[key], tuple(approved["size"][kind])
            )
    assert len(files) == 20
    return files


def verify_asset(path: str, data: bytes, digest: str, dimensions: tuple[int, int]) -> None:
    assert 20_000 < len(data) < 600_000, path
    assert hashlib.sha256(data).hexdigest() == digest, path
    assert webp_dimensions(data) == dimensions, path


def check_package(archive: zipfile.ZipFile) -> dict[str, bytes]:
    inner = json.loads(archive.read("bond-packshots-manifest.json"))
    assert inner["category"] == "bond" and len(inner["assets"]) == 10
    expected = expected_files()
    package_paths = set()
    for asset in inner["assets"]:
        for variant, sha_key in (("full", "full_sha256"), ("card", "card_sha256")):
            name = asset[variant]
            expected_path = "public/images/illustrations/catalogue-projects/" + asset["slug"] + (
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
    print("PASS: 10/10 product-specific concepts, 20/20 images match approved SHA256 and dimensions.")


def main(archive_path: Path) -> None:
    with zipfile.ZipFile(archive_path) as archive:
        payload = check_package(archive)
    # All ZIP validation happens before writing any file.
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    for relative, data in payload.items():
        (ROOT / relative).write_bytes(data)
    verify_installed()
    print("NEXT: commit public/images/illustrations/catalogue-projects/*.webp on a PR and run CI.")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--verify":
        verify_installed()
    elif len(sys.argv) == 2:
        main(Path(sys.argv[1]))
    else:
        raise SystemExit("Usage: install_bond_packshots.py <ZIP> | --verify")
