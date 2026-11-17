import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';

const read=path=>readFileSync(path,'utf8');
test('C1TE has its own FR/AR/EN product sheet, no template dilution',()=>{
  const route=read('src/pages/[lang]/documentation/[slug].astro');
  const component=read('src/components/FenekC1TEPilot.astro');
  const c1te=read('src/data/fenek-c1te-reference.ts');
  assert.match(route,/product.code==='BOND-C1TE'/);
  assert.match(route,/FenekC1TEPilot/);
  assert.match(component,/product.code!=='BOND-C1TE'/);
  assert.match(component,/data-c1te-pilot/);
  assert.match(component,/FenekApplicationGuide lang=\{lang\} product=\{product\} concise/);
  assert.match(component,/data-c1te-source-type/);
  assert.match(component,/data-print-market-sheet/);
  assert.match(component,/hasPublishedPdf/);
  assert.match(component,/fenek-c1te-print/);
  assert.match(component,/application\/ld\+json/);
  assert.match(component,/productWhatsappHref/);
  assert.match(component,/c1teFamilyReferences\.filter/);
  assert.match(component,/data-reference/);
  assert.doesNotMatch(component,/t\\.important|fenek-document-footer c1te-reference-note/);
  assert.doesNotMatch(c1te,/important:'/);
  assert.doesNotMatch(component,/Sika|Mapei|Weber|Bostik|BROUILLON|présentation provisoire/i);
  for(const language of ['fr:','ar:','en:']) assert.ok(c1te.includes(language),language);
  for(const key of ['consommation-simple','consommation-double','eau','temps-ouvert-e']){
    assert.ok(c1te.includes(key),key);
  }
  assert.match(c1te,/≥ 0,5 N\/mm² après 30 min/);
  assert.match(c1te,/≤ 0,5 mm/);
  assert.doesNotMatch(c1te,/certifi[ée] FENEK|FENEK compliant with EN/i);
});

test('C1TE internal CSV documents independent comparable brands and classifications',()=>{
 const csv=read('docs/INTERNE-validation-donnees.csv');
 const rows=csv.trim().split(/\r?\n/).filter(x=>x.startsWith('BOND-C1TE,'));
 assert.ok(rows.length>=30,`Expected C1TE traceability, got ${rows.length}`);
 for(const source of ['Sika - SikaCeram-125 Easy Fix IN','Mapei - Tixobond White','Weber - weberset 303']){
   assert.ok(csv.includes(source),source);
 }
 assert.match(csv,/exigence normative EN 12004-1:2017 E/);
 assert.match(csv,/à valider par le fabricant\/laboratoire/);
 assert.ok(!read('src/components/FenekC1TEPilot.astro').includes('https://ind.sika.com'));
});
