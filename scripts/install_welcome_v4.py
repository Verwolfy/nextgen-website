#!/usr/bin/env python3
"""Install user-approved optimized NextGen welcome media from verified ASCII staging.

The GitHub connector transports only UTF-8 text. Staged base64 fragments are
decoded and SHA256-validated on GitHub Actions before the binary is committed.
"""
from __future__ import annotations
import argparse
import base64
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGE = ROOT / ".media-staging" / "lot116"
DEST = ROOT / "public" / "videos"
EXPECTED = (
    ("nextgen-nexo-geno-welcome-v4.mp4",
     ("welcome-v4.part01.b64", "welcome-v4.part02.b64",
      "welcome-v4.part03.b64", "welcome-v4.part04.b64"),
     712241, "e7ac28368254aff457c57067c79adf2973584becbfc9e2375180e20301494a13"),
    ("nextgen-nexo-geno-poster-v4.webp", ("poster-v4.b64",),
     26946, "7a4ba9144d9bde9844fb779b24eab728e408e11682c6ad5095be45756f3fd90b"),
)


def decoded_assets() -> dict[str, bytes]:
    assets = {}
    for name, parts, expected_size, expected_sha in EXPECTED:
        joined = "".join((STAGE / part).read_text(encoding="ascii").strip() for part in parts)
        data = base64.b64decode(joined, validate=True)
        observed = hashlib.sha256(data).hexdigest()
        if len(data) != expected_size or observed != expected_sha:
            raise ValueError(f"{name}: staging checksum/size mismatch: bytes={len(data)} sha256={observed}")
        assets[name] = data
    return assets


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Validate only; never write assets")
    args = parser.parse_args()
    assets = decoded_assets()
    if not args.check:
        DEST.mkdir(parents=True, exist_ok=True)
        for name, data in assets.items():
            path = DEST / name
            if path.exists() and path.read_bytes() != data:
                raise ValueError(f"{name}: refusing to overwrite a different existing asset")
            path.write_bytes(data)
    for name, data in assets.items():
        print(f"{'VALID' if args.check else 'WRITTEN'}: {name} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
