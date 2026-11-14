import test from 'node:test';
import assert from 'node:assert/strict';
import { inspectGallery, inspectGuide, inspectWebP, validateSource, verifyLiveRelease } from '../scripts/audit_fenek_live_release.mjs';

const sha = 'a'.repeat(40);
const digest = 'b'.repeat(64);
const art = { code: 'BOND-GR-HR', slug: 'fenek-bond-gr-hr', sha256: digest,
  sprite: '/images/application-upgraded/fenek-bond-gr-hr-steps.webp' };
const positions = ['0% 0%','50% 0%','100% 0%','0% 100%','50% 100%','100% 100%'];
const card = row => '<details data-product-code="' + row.code + '" data-sha256="' + row.sha256 +
  '" style="--media:url(' + row.sprite + ')"><ol class="steps">' +
  positions.map(pos=>'<li class="step"><div class="crop" style="--pos:' + pos + '"></div></li>').join('') + '</ol></details>';
const gallery = card(art);
const page = '<section data-reference="' + art.code + '" data-application-count="6" data-v3-enhanced-sprite="' +
  art.sprite + '" data-v3-enhanced-hash="' + art.sha256 + '">' + Array.from({length:6},(_,i)=>'<li data-application-step="' + (i+1) + '"><div data-v3-step="' + (i+1) + '"></div></li>').join('') + '</section>';
function fakeFetch(commit = sha) {
  const resources = new Map([
    ['/deployment.json', JSON.stringify({application:'nextgen-website',branch:'main',commit})],
    ['/fr/avant-premiere/audit-50-illustrations/', gallery]
  ]);
  return async url => ({ok:resources.has(url.pathname),status:resources.has(url.pathname)?200:404,
    text:async()=>resources.get(url.pathname)});
}
test('gallery validates exact media identity and six official panels', () => {
  assert.deepEqual(inspectGallery(gallery,[art]), {products:1,officialScenes:6});
  assert.throws(()=>inspectGallery(card({...art,sha256:'0'.repeat(64)}),[art]),/SHA identity mismatch/);
  assert.throws(()=>inspectGallery(gallery.replace('<div class="crop" style="--pos:0% 0%"></div>',''),[art]),/image crops/);
});
test('page validates step order and correct sprite', () => {
  assert.doesNotThrow(()=>inspectGuide(page,art.code,art.sprite,art.sha256));
  assert.throws(()=>inspectGuide(page.replace('step="4"','step="9"'),art.code,art.sprite,art.sha256),/step numbering/);
});
test('invalid WebP fails closed', () => {
  assert.throws(()=>inspectWebP(Buffer.from('invalid'),digest,art.code),/invalid WebP/);
});
test('deployment drift blocks gallery verification', async () => {
  await assert.rejects(verifyLiveRelease({origin:'https://nextgen-buildingsolutions.com/',expectedCommit:sha,catalog:[art],expectedProducts:1,
    artwork:[art],fetcher:fakeFetch('c'.repeat(40))}),/DEPLOYMENT DRIFT/);
});
test('quick mode passes with matching marker and gallery', async () => {
  const report=await verifyLiveRelease({origin:'https://nextgen-buildingsolutions.com/',expectedCommit:sha,
    catalog:[art],expectedProducts:1,artwork:[art],fetcher:fakeFetch()});
  assert.equal(report.status,'PASS');
  assert.equal(report.gallery.officialScenes,6);
  assert.equal(report.pagesChecked,0);
});
test('missing gallery returns HTTP failure', async () => {
  const fetcher=async url=>({ok:url.pathname==='/deployment.json',status:404,
    text:async()=>JSON.stringify({application:'nextgen-website',branch:'main',commit:sha})});
  await assert.rejects(verifyLiveRelease({origin:'https://nextgen-buildingsolutions.com/',
    expectedCommit:sha,catalog:[art],expectedProducts:1,artwork:[art],fetcher}),/HTTP 404/);
});
test('non-HTTPS origins are rejected', async () => {
  await assert.rejects(verifyLiveRelease({origin:'http://example.org/',expectedCommit:sha,
    catalog:[art],expectedProducts:1,artwork:[art],fetcher:fakeFetch()}),/HTTPS/);
});

test('gallery rejects artwork that is only linked but not displayed', () => {
  const fraud = gallery.replace('style="--media:url(' + art.sprite + ')', 'style="--media:none') +
    '<a href="' + art.sprite + '">media</a>';
  assert.throws(() => inspectGallery(fraud,[art]), /artwork not rendered/);
});
test('guide rejects incorrect artwork SHA', () => {
  assert.throws(() => inspectGuide(page,art.code,art.sprite,'0'.repeat(64)), /wrong artwork SHA/);
});
test('guide rejects missing rendered image despite six text steps', () => {
  const missing = page.replace('<div data-v3-step="3"></div>', '');
  assert.throws(() => inspectGuide(missing,art.code,art.sprite,art.sha256), /missing rendered six scenes/);
});

test('source manifest refuses missing references even in quick mode', async () => {
  await assert.rejects(verifyLiveRelease({origin:'https://nextgen-buildingsolutions.com/',expectedCommit:sha,
    catalog:[],artwork:[],fetcher:fakeFetch()}),/expected exactly 50/);
});
test('source manifest rejects duplicate and altered artwork identities', () => {
  assert.throws(()=>validateSource([art,art],[art,art],2),/duplicate catalog/);
  assert.throws(()=>validateSource([art],[{...art,sha256:'not-a-hash'}],1),/artwork\/slug\/hash mismatch/);
});
test('gallery rejects a missing crop even if six captions survive', () => {
  const missing = gallery.replace('<div class="crop" style="--pos:0% 0%"></div>', '');
  assert.throws(()=>inspectGallery(missing,[art]),/image crops/);
});
test('gallery rejects out of order crop placement', () => {
  const bad = gallery.replace('style="--pos:50% 0%"','style="--pos:0% 0%"');
  assert.throws(()=>inspectGallery(bad,[art]),/image crops/);
});
