#!/usr/bin/env python3
"""Migrate all 50 FENEK illustration kits to public/images/fenek-products/.

Usage (on an authenticated, clean checkout of main):
  python3 scripts/migrate_fenek_illustrations.py /path/to/50-products.zip --purge

Requires Pillow: python3 -m pip install Pillow.
This utility edits the local checkout only; review, build, commit and push separately.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile
from io import BytesIO
from pathlib import Path
from PIL import Image

LEGACY = [
    'public/images/application-upgraded',
    'public/images/application-v3',
    'public/images/application/v3',
    'public/images/application-premium',
]
EXPECTED = [f'{i:02}.webp' for i in range(1, 7)] + [
    'planche-complete.webp', 'instructions.json'
]

def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def write_file(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_bytes() != data:
        path.write_bytes(data)

def git(root: Path, *args: str) -> str:
    return subprocess.check_output(
        ['git', '-C', str(root), *args], text=True
    ).strip()

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--purge', action='store_true', help='Delete legacy folders only if unreferenced by site sources')
    args = parser.parse_args()
    root = args.repo.resolve()
    archive = args.archive.resolve()

    if not (root/'.git').is_dir() or not (root/'src/components/FenekApplicationGuide.astro').exists():
        sys.exit('Invalid nextgen-website checkout')
    if git(root, 'branch', '--show-current') != 'main':
        sys.exit('Only the main branch may be migrated')
    if git(root, 'status', '--porcelain'):
        sys.exit('Working tree must be clean')
    if not archive.is_file():
        sys.exit(f'Missing archive: {archive}')

    mapping = {}
    destination = root/'public/images/fenek-products'
    with zipfile.ZipFile(archive) as z:
        if z.testzip():
            sys.exit('The source ZIP failed its integrity check')
        names = set(z.namelist())
        products = sorted({p.split('/')[0] for p in names if '/' in p})
        if len(products) != 50 or len(names) != 400:
            sys.exit(f'Expected 50 product folders and 400 files, got {len(products)} folders and {len(names)} files')

        for product in products:
            missing = {f'{product}/{f}' for f in EXPECTED} - names
            if missing:
                sys.exit(f'Missing files for {product}: {sorted(missing)}')
            instructions = json.loads(z.read(product+'/instructions.json'))
            if (instructions.get('language_order') or instructions.get('languages') or instructions.get('langue_ordre')) != ['ar', 'en', 'fr']:
                sys.exit(f'Missing AR/EN/FR language order: {product}')
            slug = instructions.get('slug') or product.lower().replace('_', '-')
            code = instructions.get('product_code') or product.replace('FENEK-', '')
            if slug in mapping:
                sys.exit(f'Duplicate slug: {slug}')
            target = destination/slug
            pictures = []
            for filename in EXPECTED:
                payload = z.read(f'{product}/{filename}')
                if filename.endswith('.webp'):
                    with Image.open(BytesIO(payload)) as im:
                        im.verify()
                    if filename != 'planche-complete.webp':
                        with Image.open(BytesIO(payload)) as im:
                            frame = im.convert('RGB')
                        if frame.size != (720, 480):
                            if frame.width*2 != frame.height*3:
                                sys.exit(f'Invalid image aspect ratio: {product}/{filename}')
                            frame = frame.resize((720, 480), Image.Resampling.LANCZOS)
                        pictures.append(frame)
                write_file(target/filename, payload)

            sprite = Image.new('RGB', (2160, 960), 'white')
            for idx, frame in enumerate(pictures):
                sprite.paste(frame, ((idx % 3)*720, (idx//3)*480))
            stream = BytesIO()
            sprite.save(stream, format='WEBP', quality=92, method=6)
            sprite_data = stream.getvalue()
            write_file(target/'sprite.webp', sprite_data)
            mapping[slug] = {
                'code': code,
                'sprite': f'/images/fenek-products/{slug}/sprite.webp',
                'folder': f'/images/fenek-products/{slug}',
                'sha256': sha256(sprite_data),
            }

    sources = [
        root/'src/data/fenek-enhanced-artwork.json',
        root/'src/data/fenek-v3-manuals.json',
        root/'src/data/fenek-v3-reviewed.ts',
    ]
    for path in sources:
        if not path.is_file():
            sys.exit(f'Missing Astro source: {path}')
        text = path.read_text(encoding='utf-8')
        for slug, info in mapping.items():
            text = text.replace(
                f'/images/application-upgraded/{slug}-steps.webp',
                info['sprite'])
            text = text.replace(
                f'/images/application-v3/{slug}-steps.webp',
                info['sprite'])
            text = re.sub(
                r'/images/application/v3/' + re.escape(slug) + r'/0([1-6])_[^\x27\x22\s,]+\.png',
                lambda m: info['folder']+'/0'+m.group(1)+'.webp', text)

        if path.suffix == '.json':
            data = json.loads(text)
            for entry in data:
                slug = entry.get('slug')
                if slug in mapping:
                    entry['sprite'] = mapping[slug]['sprite']
                    if 'sha256' in entry:
                        entry['sha256'] = mapping[slug]['sha256']
                    if 'artworkDimensions' in entry:
                        entry['artworkDimensions'] = [720, 480]
            text = json.dumps(data, ensure_ascii=False, indent=2)+'\n'
        else:
            for slug, info in mapping.items():
                pos = text.find(f"slug:'{slug}'")
                if pos < 0:
                    continue
                fragment = text[pos:pos+320]
                fragment = re.sub(
                    r"sha256:'[a-f0-9]{64}'",
                    f"sha256:'{info['sha256']}'",
                    fragment, count=1)
                text = text[:pos] + fragment + text[pos+320:]
        path.write_text(text, encoding='utf-8')

    legacy_references = {}
    for directory in LEGACY:
        url_prefix = '/' + directory.removeprefix('public/') + '/'
        refs = []
        for path in (root/'src').rglob('*'):
            if path.suffix not in ('.ts','.tsx','.astro','.js','.json','.css'):
                continue
            if url_prefix in path.read_text(encoding='utf-8'):
                refs.append(str(path.relative_to(root)))
        legacy_references[directory] = refs
        if args.purge and not refs:
            shutil.rmtree(root/directory, ignore_errors=True)

    report = {
        'products': len(mapping),
        'original_files': len(mapping)*8,
        'output_assets': len(mapping)*9,
        'destination': str(destination.relative_to(root)),
        'legacy_references': legacy_references,
        'deleted_only_unreferenced': bool(args.purge),
    }
    (root/'NEXTGEN_ILLUSTRATIONS_MIGRATION.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print('MIGRATION PREPARED: run npm ci && npm run build, review diff, then git add/commit/push.')

if __name__ == '__main__':
    main()
