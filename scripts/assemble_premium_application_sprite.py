#!/usr/bin/env python3
"""Pack six reviewed trade-scene images into a numbered, review-only FENEK WebP sprite.

Usage:
  python scripts/assemble_premium_application_sprite.py \
    --code PROOF-PU-1K --slug fenek-proof-pu-1k \
    --scene scene1.png --scene scene2.png --scene scene3.png \
    --scene scene4.png --scene scene5.png --scene scene6.png \
    --output /tmp/fenek-proof-pu-1k-steps-v4.webp

Requires Pillow locally. Does not modify website metadata or approve publication.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--code", required=True)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--scene", action="append", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    if len(args.scene) != 6:
        ap.error("Six distinct source images are mandatory, in application step order")
    if len({p.resolve() for p in args.scene}) != 6:
        ap.error("The same source image must not be reused for separate steps")
    if not re.fullmatch(r"[A-Z]+-[A-Z0-9-]+", args.code):
        ap.error("Invalid product code")
    if not re.fullmatch(r"fenek-[a-z0-9-]+", args.slug):
        ap.error("Invalid slug")
    expected_name = f"{args.slug}-steps-v4.webp"
    if args.output.name != expected_name:
        ap.error(f"The output file must be named {expected_name}")

    try:
        from PIL import Image, ImageDraw, ImageFont, ImageOps
    except ImportError as exc:
        raise SystemExit("Pillow is required for local sprite assembly (python -m pip install Pillow)") from exc

    tile_w, tile_h = 540, 360
    sheet = Image.new("RGB", (1620, 720), "white")
    checks = []
    for idx, source in enumerate(args.scene):
        with Image.open(source) as original:
            im = ImageOps.exif_transpose(original).convert("RGB")
            if im.width < tile_w or im.height < tile_h:
                raise ValueError(f"Step {idx+1}: low-resolution source {im.size}; 540x360 minimum")
            # Crop to the intended 3:2 aspect ratio, without stretching.
            cropped = ImageOps.fit(im, (tile_w, tile_h), method=Image.Resampling.LANCZOS,
                                   centering=(0.5, 0.5))
            x, y = (idx % 3) * tile_w, (idx // 3) * tile_h
            sheet.paste(cropped, (x, y))
            checks.append({
                "step": idx + 1,
                "source": source.name,
                "input_dimensions": list(im.size),
                "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            })

    draw = ImageDraw.Draw(sheet)
    # Each panel is cropped to a consistent grid. Solid opaque borders prevent
    # seams; numbers are rendered here, never guessed by image generation.
    for i in range(6):
        x, y = (i % 3) * tile_w, (i // 3) * tile_h
        draw.rounded_rectangle((x + 4, y + 4, x + tile_w - 5, y + tile_h - 5),
                               radius=15, outline="#12295C", width=3)
        cx, cy, rad = x + 47, y + 44, 28
        draw.ellipse((cx-rad-4, cy-rad-4, cx+rad+4, cy+rad+4),
                     fill="#FFFFFF")
        draw.ellipse((cx-rad, cy-rad, cx+rad, cy+rad),
                     fill="#0A843F", outline="#065D31", width=2)
        try:
            font = ImageFont.truetype("DejaVuSans-Bold.ttf", 34)
        except OSError:
            font = ImageFont.load_default()
        text = str(i + 1)
        box = draw.textbbox((0, 0), text, font=font)
        draw.text((cx-(box[2]-box[0])/2, cy-(box[3]-box[1])/2-box[1]),
                  text, font=font, fill="#FFFFFF")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(args.output, "WEBP", quality=92, method=6)
    raw = args.output.read_bytes()
    manifest = {
        "code": args.code,
        "slug": args.slug,
        "status": "BROUILLON_A_REVOIR",
        "visualQualityApproved": False,
        "technicalApproved": False,
        "sourceType": "six-original-editorial-semi-realistic-scenes",
        "width": 1620,
        "height": 720,
        "panels": [3, 2],
        "output": args.output.name,
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "scenes": checks,
        "required_qa": [
            "Read each approved technical and safety sheet",
            "Verify correct gestures, materials, PPE and surroundings",
            "No generated official logos, certifications or technical quantities",
            "Inspect crop at mobile 360px and desktop",
            "Confirm FR/AR/EN captions are served by website HTML",
            "Preserve source WebP fallback and wait for CI + visual approval",
        ],
    }
    manifest_file = args.output.with_suffix(".manifest.json")
    manifest_file.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8")
    print(f"REVIEW ONLY: {args.output} SHA256={manifest['sha256']} bytes={len(raw)}")
    print(f"QA manifest: {manifest_file}")


if __name__ == "__main__":
    main()
