import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';

const read=p=>readFileSync(p,'utf8');
test('C2FT owns a distinct professional FR/AR/EN page without the removed footer note',()=>{
  const route=read('src/pages/[lang]/documentation/[slug].astro');
  const sheet=read('src/components/FenekC2FTPilot.astro');
  const content=read('src/data/fenek-c2ft-reference.ts');
  const catalogue=JSON.parse(read('src/data/catalogue-projets.json'));
  assert.match(route,/product.code==='BOND-C2FT'/);
  assert.match(route,/FenekC2FTPilot/);
  assert.match(sheet,/product.code!=='BOND-C2FT'/);
  assert.match(sheet,/data-c2ft-pilot/);
  assert.match(sheet,/FenekApplicationGuide lang=\{lang\} product=\{product\} concise/);
  assert.match(sheet,/data-c2ft-source-type/);
  assert.match(sheet,/fenek-c2ft-print/);
  assert.match(sheet,/productWhatsappHref/);
  assert.match(sheet,/hasPublishedPdf/);
  assert.match(sheet,/application\/ld\+json/);
  assert.doesNotMatch(sheet,/t[.]important|figuresNote|BROUILLON|présentation provisoire/i);
  assert.doesNotMatch(sheet,/Sika|Mapei|Weber/i);
  const prod=catalogue.find(x=>x.code==='BOND-C2FT');
  assert.equal(prod.slug,'fenek-bond-c2ft');
  assert.equal(prod.certifie,false);
  assert.equal(prod.commercialise,false);
  for(const lang of ['fr','ar','en']){
    assert.ok(prod.contenu[lang].usages.length===3);
    assert.ok(prod.contenu[lang].description.length>110);
  }
  assert.match(content,/value:'≥ 1,0 N\/mm²'/);
  assert.match(content,/value:'≥ 0,5 N\/mm² \(≤ 6 h\)'/);
  assert.match(content,/value:'≤ 0,5 mm'/);
  assert.match(content,/c2ftCopy:Record<Lang,Copy>/);
  for(const key of ['c2-initial','f-precoce','f-ouvert','t-glissement','consommation-par-mm','eau']){
    assert.ok(content.includes(key),key);
  }
  assert.doesNotMatch(content,/important:|figuresNote:|Les seuils de classe et les plages comparatives/);
});

test('C2FT internal research traces 3 independent manufacturers and all class limits',()=>{
 const csv=read('docs/INTERNE-validation-donnees.csv');
 const rows=csv.trim().split(/\r?\n/).filter(x=>x.startsWith('BOND-C2FT,'));
 assert.ok(rows.length>=35,`Only ${rows.length} C2FT sources`);
 for(const brand of ['Mapei – Keraquick C2FT S1','Weber – weberset rapid plus','Sika – SikaCeram Flexible Rapid Set WHITE'])
   assert.ok(csv.includes(brand),brand);
 assert.match(csv,/exigence normative EN 12004-1:2017 C2/);
 assert.match(csv,/exigence normative EN 12004-1:2017 F/);
 assert.match(csv,/à valider par le fabricant\/laboratoire/);
 assert.doesNotMatch(read('src/components/FenekC2FTPilot.astro'),/cdnmedia[.]mapei[.]com|gbr[.]sika[.]com|uk[.]weber/);
});
