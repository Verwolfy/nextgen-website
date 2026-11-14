import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {resolve} from 'node:path';
const src = readFileSync(resolve('src/components/FenekApplicationGuide.astro'),'utf8');

test('official product guide never embeds unapproved PROOF draft previews', () => {
  assert.doesNotMatch(src, /FenekAcrRfDraftPreview|FenekProofPartialDraft|previewAcrRf|partialDraftStep/);
});

test('official guides keep exact per-product approved fallback and six-step structure', () => {
  assert.match(src, /reviewedV3GuideFor\(product.code,product.slug\)/);
  assert.match(src, /enhancedArtwork\.find\(item=>item.code===product.code && item.slug===product.slug\)/);
  assert.match(src, /data-application-count=\{steps.length\}/);
  assert.match(src, /data-application-step=\{i\+1\}/);
  assert.match(src, /data-v3-enhanced-hash=\{enhancedV3\?\.sha256\}/);
});

test('current official six-stage artwork remains visible during cleanup', () => {
  assert.match(src, /enhancedV3\?\.sprite \?\? reviewedV3.sprite/);
  assert.match(src, /fenek-v3-upgraded-photo/);
  assert.match(src, /fenek-application-visual-warning/);
});
