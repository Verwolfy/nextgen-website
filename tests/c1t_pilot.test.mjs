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
  assert.match(pilot,/hasPublishedPdf/);
  assert.match(pilot,/download/);
  assert.match(pilot,/c1tFamilyReferences\.filter/);
  assert.match(pilot,/fenek-application/);
  assert.doesNotMatch(pilot,/t[.]important|fenek-document-footer c1t-legal/);
  assert.doesNotMatch(read('src/data/fenek-c1t-reference.ts'),/important:'/);
  assert.doesNotMatch(pilot,/Sika|Mapei|Bostik|BROUILLON|présentation provisoire/);
});
test('pilot requirements and family benchmarks remain distinct',()=>{
  const src=read('src/data/fenek-c1t-reference.ts');
  assert.match(src,/kind:'norme'/);
  assert.match(src,/kind:'famille'/);
  assert.match(src,/≥ 0,5 N\/mm²/);
  assert.match(src,/≤ 0,5 mm/);
  assert.match(src,/c1tContent: Record<Lang/);
  assert.match(src,/temps-ouvert-comparatif/);
  assert.match(src,/ajustabilite-comparative/);
  assert.match(src,/consommation-simple/);
  assert.match(src,/consommation-double/);
  assert.match(src,/downloadLabel/);
  assert.match(src,/fr:/);
  assert.match(src,/ar:/);
  assert.match(src,/en:/);
});
test('internal source registry is never placed under public',()=>{
  const csv=read('docs/INTERNE-validation-donnees.csv');
  assert.match(csv,/source_url/);
  assert.match(csv,/à valider par le fabricant\/laboratoire/);
  for(const manufacturer of ['Sika','Mapei','Bostik','Weber'])assert.ok(csv.includes(manufacturer));
  assert.ok(csv.trimEnd().split('\n').length>=31);
  assert.match(csv,/saint-gobain-africa\.com/);
});

test('reviewed C1T A4 V3 keeps original assets and a nonredundant print layout',()=>{
  const pilot=read('src/components/FenekC1TPilot.astro');
  const print=pilot.slice(pilot.indexOf('<section class="fenek-print-document fenek-c1t-print"'),pilot.indexOf('<style>'));
  const required=[
    'data-c1t-one-page','src="/images/Logo1.jpg"','src={image}',
    'data-print-hero','data-print-description','data-print-overview',
    'data-print-designation','data-print-standards','data-print-method',
    'data-print-safety','data-print-contact',
    'c1tRequirements.map','p.designation.map'
  ];
  for(const item of required)assert.ok(print.includes(item),item);
  const markers=['data-print-hero','data-print-description','data-print-overview','data-print-designation','data-print-standards','data-print-method','data-print-safety','data-print-contact'];
  const positions=markers.map(m=>print.indexOf(m));
  assert.ok(positions.every((p,i)=>p>=0&&(i===0||p>positions[i-1])),positions.join(','));
  assert.ok(pilot.includes("conceptPackshot(product,'full')"));
  assert.doesNotMatch(print,/c1tFamilyReferences|data-print-benchmarks|5–6,5 L|3–5 kg\/m²/);
  assert.equal((print.match(/<section class="fenek-print-card/g)||[]).length,7);
  assert.equal((print.match(/data-print-standards/g)||[]).length,1);
  assert.ok(pilot.includes('grid-template-columns:repeat(3,minmax(0,1fr))'));
});
