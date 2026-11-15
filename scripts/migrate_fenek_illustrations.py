#!/usr/bin/env python3
"""Replace 50 official FENEK WebP sprites IN PLACE on main.

No new branches, no public/images/fenek-products directory, no old-folder purge.
The official files remain public/images/application-upgraded/<slug>-steps.webp.
Only graphical assets and their SHA-256 in fenek-enhanced-artwork.json change.
FR/EN/AR text and BROUILLON/FT-FDS validation restrictions stay unchanged.

Usage from a clean main checkout (Pillow installed):
  python3 scripts/migrate_fenek_illustrations.py /path/to/NEXTGEN_TEMP_50_PRODUCTS_FOR_GITHUB_MIGRATION.zip --dry-run
  python3 scripts/migrate_fenek_illustrations.py /path/to/NEXTGEN_TEMP_50_PRODUCTS_FOR_GITHUB_MIGRATION.zip
  npm ci --no-audit --no-fund && npm run build
  git add public/images/application-upgraded src/data/fenek-enhanced-artwork.json
  git commit -m "assets: replace 50 FENEK sprites in place"
  git push origin main
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

REFERENCE_SCAN_TREES = ('src', 'tests', 'scripts', '.github', 'public')
REFERENCE_SCAN_SUFFIXES = {'.astro', '.ts', '.tsx', '.js', '.mjs', '.css', '.json', '.html', '.py', '.yml', '.yaml', '.sh', '.md', '.txt'}

def find_legacy_references(root: Path, directory: str) -> list[str]:
    """Fail closed: an old image URL may be used outside src (e.g. public HTML previews)."""
    url_prefix = '/' + directory.removeprefix('public/') + '/'
    refs: set[str] = set()
    for tree in REFERENCE_SCAN_TREES:
        base = root / tree
        if not base.is_dir():
            continue
        for path in base.rglob('*'):
            if not path.is_file() or path.suffix.lower() not in REFERENCE_SCAN_SUFFIXES:
                continue
            try:
                source = path.read_text(encoding='utf-8')
            except (UnicodeDecodeError, OSError):
                # An unreadable reference file cannot justify deleting assets.
                refs.add(str(path.relative_to(root)) + ' (unreadable)')
                continue
            if url_prefix in source:
                refs.add(str(path.relative_to(root)))
    return sorted(refs)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--dry-run', action='store_true', help='Check and render without writing files')
    args = parser.parse_args()
    root, archive = args.repo.resolve(), args.archive.resolve()
    dest = root/'public/images/application-upgraded'
    manifest_path = root/'src/data/fenek-enhanced-artwork.json'
    if not (root/'.git').is_dir() or not dest.is_dir() or not manifest_path.is_file():
        sys.exit('Invalid nextgen-website checkout')
    if git(root, 'branch', '--show-current') != 'main':
        sys.exit('Only main may be migrated')
    if git(root, 'status', '--porcelain'):
        sys.exit('Working tree must be clean before migration')
    if not archive.is_file():
        sys.exit(f'Missing source ZIP: {archive}')
    raw = archive.read_bytes()
    if sha256(raw) != '40f32540218d95f6d987edf93ad210a9382fbed373cdcc926da5ed044988f719':
        sys.exit('Source ZIP SHA-256 mismatch; exact user-supplied archive required')
    rows = json.loads(manifest_path.read_text(encoding='utf-8'))
    if len(rows) != 50 or len({r['code'] for r in rows}) != 50:
        sys.exit('Expected 50 unique official codes')
    by_code = {r['code']:r for r in rows}
    expected = set(EXPECTED)
    output, original = {}, {}
    from PIL import Image
    with zipfile.ZipFile(BytesIO(raw)) as z:
        names = z.namelist()
        if len(names) != 400 or len(set(names)) != 400 or z.testzip():
            sys.exit('Archive must contain exactly 400 unique valid entries')
        folders = {}
        for name in names:
            parts = name.split('/')
            if len(parts) != 2 or not all(parts) or any(p in ('.','..') for p in parts):
                sys.exit('Unexpected source ZIP path: '+name)
            folders.setdefault(parts[0],set()).add(parts[1])
        if len(folders) != 50:
            sys.exit('Expected exactly 50 product folders')
        for folder, files in folders.items():
            if files != expected:
                sys.exit('Incomplete image kit: '+folder)
            code = folder.removeprefix('FENEK-')
            if folder != 'FENEK-'+code or code not in by_code:
                sys.exit('Unknown product: '+folder)
            entry = by_code[code]
            slug = entry['slug']
            instructions = json.loads(z.read(folder+'/instructions.json'))
            if instructions.get('product_code',code)!=code or instructions.get('code',folder)!=folder:
                sys.exit('Product code mismatch: '+folder)
            if instructions.get('slug',slug)!=slug:
                sys.exit('Slug mismatch: '+folder)
            langs = instructions.get('language_order') or instructions.get('langue_ordre') or instructions.get('languages')
            if langs != ['ar','en','fr']:
                sys.exit('AR/EN/FR order mismatch: '+folder)
            steps = instructions.get('instructions') or instructions.get('steps')
            if not isinstance(steps,list) or len(steps)!=6:
                sys.exit('Expected six steps: '+folder)
            for i,step in enumerate(steps,1):
                if step.get('number',step.get('step',step.get('numero',i)))!=i or step.get('image',f'{i:02}.webp')!=f'{i:02}.webp':
                    sys.exit('Step order mismatch: '+folder)
            with Image.open(BytesIO(z.read(folder+'/planche-complete.webp'))) as board:
                board.verify()
            sheet = Image.new('RGB',(1620,720),'white')
            for i in range(6):
                payload = z.read(f'{folder}/{i+1:02}.webp')
                with Image.open(BytesIO(payload)) as image:
                    image.verify()
                with Image.open(BytesIO(payload)) as image:
                    if image.width*2 != image.height*3:
                        sys.exit('Invalid source aspect ratio: '+folder+f' step {i+1}')
                    frame = image.convert('RGB').resize((540,360),Image.Resampling.LANCZOS)
                sheet.paste(frame,((i%3)*540,(i//3)*360))
            data = None
            for quality in (82,78,74,70,66):
                stream = BytesIO()
                sheet.save(stream,format='WEBP',quality=quality,method=3)
                if len(stream.getvalue()) < 250000:
                    data = stream.getvalue()
                    break
            if data is None:
                sys.exit('WebP exceeds the 250-KB CI budget: '+folder)
            link = f'/images/application-upgraded/{slug}-steps.webp'
            path = root/'public'/link.lstrip('/')
            if entry['sprite'] != link or entry.get('layout') != '3x2' or entry.get('artworkDimensions') != [540,360]:
                sys.exit('Current official manifest mismatch: '+folder)
            if not path.is_file():
                sys.exit('Existing official image missing (no new files allowed): '+str(path))
            old = path.read_bytes()
            if sha256(old) != entry['sha256']:
                sys.exit('Original asset checksum mismatch: '+folder)
            output[path] = data
            original[path] = old
            entry['sha256'] = sha256(data)
            if code == 'BOND-R4':
                entry.pop('sharedArtworkFrom',None) # R4 now has its own source image.
        if set(folders) != {'FENEK-'+code for code in by_code}:
            sys.exit('Archive / official 50 products differ')
    replacement = (json.dumps(rows,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
    print(json.dumps({'branch':'main','existing_directory':'public/images/application-upgraded',
                      'images':len(output),'changed':sum(output[p]!=original[p] for p in output),
                      'new_directories':0,'new_image_paths':0,'dry_run':args.dry_run},ensure_ascii=False))
    if args.dry_run:
        return
    original_manifest = manifest_path.read_bytes()
    written = []
    try:
        for path,data in output.items():
            tmp = path.with_name(path.name+'.nextgen-temp')
            tmp.write_bytes(data)
            tmp.replace(path)
            written.append(path)
        tmp = manifest_path.with_name(manifest_path.name+'.nextgen-temp')
        tmp.write_bytes(replacement)
        tmp.replace(manifest_path)
    except Exception:
        for path in written:
            path.write_bytes(original[path])
        manifest_path.write_bytes(original_manifest)
        raise
    print('IN-PLACE SUCCESS: 50 sprites overwritten in working tree; run CI, then push main.')

if __name__ == '__main__':
    main()
