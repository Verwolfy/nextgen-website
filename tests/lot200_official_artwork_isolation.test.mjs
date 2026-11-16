import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync, existsSync} from 'node:fs';
import {resolve} from 'node:path';
const src=readFileSync(resolve('src/components/FenekApplicationGuide.astro'),'utf8');
const gate=readFileSync(resolve('scripts/verify_fenek_deployment.mjs'),'utf8');

test('only the 50 current per-product guide illustrations are rendered',()=>{
 assert.match(src,/reviewedV3GuideFor\(product.code,product.slug\)/);
 assert.match(src,/enhancedArtwork\.find\(item=>item.code===product.code && item.slug===product.slug\)/);
 assert.match(src,/data-application-count=\{steps.length\}/);
 assert.match(src,/data-application-step=\{i\+1\}/);
 assert.match(src,/data-v3-enhanced-hash=\{enhancedV3.sha256\}/);
 assert.match(src,/fenek-v3-upgraded-photo/);
});
test('draft previews and zoom links cannot return to official guide',()=>{
 assert.doesNotMatch(src,/FenekAcrRfDraftPreview|FenekProofPartialDraft|fullSizeC1T|fullResolution|fenek-v3-detail-link|copy\.zoom/);
 assert.match(gate,/!html\.includes\('data-acrrf-v4-preview'\)/);
 assert.match(gate,/!html\.includes\('data-proof-partial-preview'\)/);
 assert.match(gate,/Retired media or preview still published/);
 assert.match(gate,/verifyMedia\(art\.sprite,art\.sha256/);
 assert.doesNotMatch(gate,/verifyMedia\(candidate\.path|verifyMedia\(acr\.path/);
});
test('all removed premium media and preview pages stay deleted',()=>{
 for(const path of [
 'public/images/illustrations/application-premium',
 'public/images/illustrations/application/v3/fenek-bond-c1t',
 'public/fr/avant-premiere/fenek-proof-acr-rf',
 'public/fr/avant-premiere/lot187-proof',
 'public/fr/avant-premiere/audit-50-illustrations',
 'src/components/FenekProofPartialDraft.astro',
 'src/components/FenekAcrRfDraftPreview.astro',
 ])assert.equal(existsSync(resolve(path)),false,path);
});
