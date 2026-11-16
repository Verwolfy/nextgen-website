#!/usr/bin/env node
/** Read-only release audit. Does not mutate Cloudflare, GitHub, or site content. */
import { readFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const LANGS = ['fr', 'en', 'ar'];
const SHA = /^[0-9a-f]{40}$/i;
const sha256 = bytes => createHash('sha256').update(bytes).digest('hex');

export function validateSource(catalog, artwork, expectedProducts = 50) {
  if (!Number.isInteger(expectedProducts) || expectedProducts < 1 ||
      !Array.isArray(catalog) || !Array.isArray(artwork) ||
      catalog.length !== expectedProducts || artwork.length !== expectedProducts)
    throw Error('source: expected exactly ' + expectedProducts + ' catalog and artwork records');
  const codes = new Map();
  const slugs = new Set();
  for (const item of catalog) {
    if (!item || !/^[A-Z0-9-]+$/.test(item.code ?? '') ||
        !/^[a-z0-9-]+$/.test(item.slug ?? '') || codes.has(item.code) || slugs.has(item.slug))
      throw Error('source: invalid or duplicate catalog identity');
    codes.set(item.code, item.slug);
    slugs.add(item.slug);
  }
  const seen = new Set();
  for (const item of artwork) {
    if (!item || seen.has(item.code) || codes.get(item.code) !== item.slug ||
        !/^[0-9a-f]{64}$/i.test(item.sha256 ?? '') ||
        item.sprite !== '/images/illustrations/application-upgraded/' + item.slug + '-steps.webp')
      throw Error('source: artwork/slug/hash mismatch ' + (item?.code ?? 'missing'));
    seen.add(item.code);
  }
  return true;
}

export function inspectGallery(html, artwork) {
  const entries = [...html.matchAll(/<details\b[^>]*\bdata-product-code="([^"]+)"[^>]*>[\s\S]*?<\/details>/g)];
  if (entries.length !== artwork.length) throw Error('gallery: expected ' + artwork.length + ' products, got ' + entries.length);
  const found = new Set();
  for (const match of entries) {
    const code = match[1], block = match[0];
    if (found.has(code)) throw Error('gallery: duplicate product ' + code);
    found.add(code);
    const item = artwork.find(a => a.code === code);
    if (!item) throw Error('gallery: unexpected product ' + code);
    if (!block.includes('data-sha256="' + item.sha256 + '"')) throw Error('gallery: SHA identity mismatch ' + code);
    const backgrounds = ["--media:url('" + item.sprite + "')", '--media:url(' + item.sprite + ')', '--media:url("' + item.sprite + '")'];
    if (!backgrounds.some(value => block.includes(value))) throw Error('gallery: artwork not rendered ' + code);
    const grid = block.match(/<ol class="steps">([\s\S]*?)<\/ol>/);
    const positions = ['0% 0%','50% 0%','100% 0%','0% 100%','50% 100%','100% 100%'];
    const tiles = grid ? [...grid[1].matchAll(/<li class="step">([\s\S]*?)<\/li>/g)] : [];
    if (tiles.length !== 6 || tiles.some((tile, i) =>
        !tile[1].includes('class="crop"') || !tile[1].includes('style="--pos:' + positions[i] + '"')))
      throw Error('gallery: missing or displaced six image crops ' + code);
  }
  for (const item of artwork) if (!found.has(item.code)) throw Error('gallery: absent ' + item.code);
  return { products: found.size, officialScenes: found.size * 6 };
}

export function inspectGuide(html, code, sprite, digest) {
  if (!html.includes('data-reference="' + code + '"')) throw Error('page: wrong reference ' + code);
  if (!html.includes('data-application-count="6"')) throw Error('page: wrong scene count ' + code);
  if (!html.includes('data-v3-enhanced-sprite="' + sprite + '"')) throw Error('page: wrong artwork mapping ' + code);
  if (!html.includes('data-v3-enhanced-hash="' + digest + '"')) throw Error('page: wrong artwork SHA ' + code);
  const rendered = [...html.matchAll(/data-v3-step="([0-9]+)"/g)].map(m => Number(m[1]));
  if (JSON.stringify(rendered) !== '[1,2,3,4,5,6]') throw Error('page: missing rendered six scenes ' + code);
  const steps = [...html.matchAll(/data-application-step="([0-9]+)"/g)].map(m => Number(m[1]));
  if (JSON.stringify(steps) !== '[1,2,3,4,5,6]') throw Error('page: wrong step numbering ' + code);
}

export function inspectWebP(bytes, digest, code) {
  const data = Buffer.from(bytes);
  if (data.length < 30 || data.toString('ascii', 0, 4) !== 'RIFF' ||
      data.toString('ascii', 8, 12) !== 'WEBP') throw Error('media: invalid WebP ' + code);
  if (sha256(data) !== digest) throw Error('media: SHA mismatch ' + code);
}

async function concurrencyMap(items, parallel, fn) {
  let cursor = 0;
  const worker = async () => {
    while (cursor < items.length) {
      const i = cursor++;
      await fn(items[i]);
    }
  };
  await Promise.all(Array.from({ length: Math.min(parallel, items.length) }, worker));
}

export async function verifyLiveRelease({ origin, expectedCommit, catalog, artwork, fetcher = fetch, full = false, expectedProducts = 50 }) {
  validateSource(catalog, artwork, expectedProducts);
  if (!SHA.test(expectedCommit)) throw Error('Expected a complete 40-character Git commit');
  const base = new URL(origin);
  if (base.protocol !== 'https:' || base.username || base.password || base.search ||
      base.hash || base.pathname !== '/') throw Error('Origin must be a bare HTTPS site origin');
  const get = async (path, binary = false) => {
    const url = new URL(path, base);
    if (url.origin !== base.origin) throw Error('Cross-origin URL forbidden');
    const res = await fetcher(url, { signal: AbortSignal.timeout(12000), redirect: 'error' });
    if (!res.ok) throw Error(path + ': HTTP ' + res.status);
    return binary ? Buffer.from(await res.arrayBuffer()) : await res.text();
  };
  const marker = JSON.parse(await get('/deployment.json'));
  if (marker.application !== 'nextgen-website' || marker.branch !== 'main' ||
      marker.commit !== expectedCommit.toLowerCase())
    throw Error('DEPLOYMENT DRIFT: expected ' + expectedCommit.toLowerCase() +
      ', public ' + (marker.commit ?? 'missing'));
  const html = await get('/fr/avant-premiere/audit-50-illustrations/');
  const gallery = inspectGallery(html, artwork);
  const report = { commit: marker.commit, gallery, pagesChecked: 0, mediaChecked: 0, status: 'PASS' };
  if (!full) return report;
  const artworkByCode = new Map(artwork.map(a => [a.code, a]));
  if (catalog.length !== 50 || artwork.length !== 50 || artworkByCode.size !== 50)
    throw Error('Expected exactly 50 source catalog/artwork entries');
  await concurrencyMap(artwork, 6, async row => {
    const bytes = await get(row.sprite, true);
    inspectWebP(bytes, row.sha256, row.code);
    report.mediaChecked++;
  });
  const jobs = catalog.flatMap(row => LANGS.map(lang => ({ row, lang })));
  await concurrencyMap(jobs, 6, async ({ row, lang }) => {
    const art = artworkByCode.get(row.code);
    if (!art || art.slug !== row.slug) throw Error('source mapping: ' + row.code);
    const page = await get('/' + lang + '/documentation/' + row.slug + '/');
    inspectGuide(page, row.code, art.sprite, art.sha256);
    report.pagesChecked++;
  });
  return report;
}

function runCli() {
  const args = process.argv.slice(2);
  const value = flag => {
    const index = args.indexOf(flag);
    if (index < 0 || !args[index + 1]) throw Error('Missing ' + flag);
    return args[index + 1];
  };
  const expectedCommit = value('--expected-commit');
  const origin = args.includes('--origin') ? value('--origin') : 'https://nextgen-buildingsolutions.com/';
  const catalog = JSON.parse(readFileSync(resolve(root, 'src/data/catalogue-projets.json'), 'utf8'));
  const artwork = JSON.parse(readFileSync(resolve(root, 'src/data/fenek-enhanced-artwork.json'), 'utf8'));
  return verifyLiveRelease({ origin, expectedCommit, catalog, artwork, full: args.includes('--full') });
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  runCli().then(report => console.log(JSON.stringify(report, null, 2)))
    .catch(err => { console.error('FAIL:', err.message); process.exitCode = 1; });
}
