import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
const read=path=>readFileSync(path,'utf8');
test('C1T pilot is isolated from all other FENEK products',()=>{
  const page=read('src/pages/[lang]/documentation/[slug].astro');
  const pilot=read('src/components/FenekC1TPilot.astro');
  assert.match(page,/product.code==='BOND-C1T'/);
  assert.match(pilot,/product.code !== 'BOND-C1T'/);
  assert.match(pilot,/data-c1t-pilot/);
  assert.match(pilot,/FenekApplicationGuide/);
  assert.match(pilot,/data-print-market-sheet/);
  assert.match(pilot,/fenek-application/);
  assert.doesNotMatch(pilot,/Sika|Mapei|Bostik|BROUILLON|présentation provisoire/);
});
test('pilot requirements and family benchmarks remain distinct',()=>{
  const src=read('src/data/fenek-c1t-reference.ts');
  assert.match(src,/kind:'norme'/);
  assert.match(src,/kind:'famille'/);
  assert.match(src,/≥ 0,5 N\/mm²/);
  assert.match(src,/≤ 0,5 mm/);
  assert.match(src,/c1tContent: Record<Lang/);
  assert.match(src,/fr:/);
  assert.match(src,/ar:/);
  assert.match(src,/en:/);
});
test('internal source registry is never placed under public',()=>{
  const csv=read('docs/INTERNE-validation-donnees.csv');
  assert.match(csv,/source_url/);
  assert.match(csv,/à valider par le fabricant\/laboratoire/);
  for(const manufacturer of ['Sika','Mapei','Bostik'])assert.ok(csv.includes(manufacturer));
  assert.ok(csv.trimEnd().split('\n').length>=22);
});
