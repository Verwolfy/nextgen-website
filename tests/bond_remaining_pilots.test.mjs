import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync, existsSync} from 'node:fs';
const read = path => readFileSync(path, 'utf8');
const codes = ['CG2WA','CT-C25-F5','GP-CSII','GR-HR','M10','M5','OC-CSIII','R2','R3','R4'];
const data = read('src/data/fenek-bond-remaining-reference.ts');
const match = data.match(/const definitions=([\s\S]*?);\nexport const bondRemainingRecords/);
assert.ok(match, 'Expected structured source definitions');
const defs = JSON.parse(match[1]);
test('all ten remaining BOND references have dedicated FR/AR/EN data and class criteria',()=>{
 assert.equal(defs.length, 10);
 const catalogue = JSON.parse(read('src/data/catalogue-projets.json'));
 const all = catalogue.filter(p=>p.gamme==='bond');
 assert.equal(all.length,16);
 for(const suffix of codes){
  const code='BOND-'+suffix;
  const entry=defs.find(d=>d.code===code);
  const product=catalogue.find(p=>p.code===code);
  assert.ok(entry && product,code);
  assert.equal(product.certifie,false);
  assert.equal(product.commercialise,false);
  assert.ok(entry.requirements.length>=1,code);
  assert.ok(entry.family.length>=3,code);
  assert.ok(entry.requirements.every(m=>m.kind==='norme'),code);
  assert.ok(entry.family.every(m=>m.kind==='famille'),code);
  for(const lang of ['fr','ar','en']){
   assert.ok(product.contenu[lang].description.length>=140,(code,lang));
   assert.equal(product.contenu[lang].usages.length,3,(code,lang));
   assert.ok(entry.copy[lang].lead.length>=30,(code,lang));
   assert.ok(entry.copy[lang].preparation.length>=3,(code,lang));
   assert.ok(entry.copy[lang].conditions.length>=3,(code,lang));
   for(const metric of [...entry.requirements,...entry.family]) assert.ok(metric.label[lang],(code,metric.key,lang));
  }
  const dossier='docs/LOT_BOND_'+suffix.replaceAll('-','_')+'_SOURCES_20261117.md';
  assert.ok(existsSync(dossier),dossier);
 }
 assert.equal(defs.find(d=>d.short==='CG2WA').requirements.length,11);
 assert.equal(defs.find(d=>d.short==='CT-C25-F5').requirements.length,2);
 assert.match(defs.find(d=>d.short==='GR-HR').requirements[0].value,/non classant/);
 assert.match(defs.find(d=>d.short==='R4').standard,/EN 1504-3/);
});
test('shared sheet, language-specific routes and private traceability are connected',()=>{
 const component=read('src/components/FenekBondTechnicalPilot.astro');
 const documentation=read('src/pages/[lang]/documentation/[slug].astro');
 const catalogueRoute=read('src/pages/[lang]/catalogue/[slug].astro');
 const exportScript=read('scripts/export_c1t_pdfs.py');
 const csv=read('docs/INTERNE-validation-donnees.csv');
 assert.match(documentation,/FenekBondTechnicalPilot/);
 for(const pattern of [/data-bond-technical-pilot/,/data-bond-source-type/,/fenek-bond-technical-print/,/FenekApplicationGuide lang=\{lang\} product=\{product\} concise/,/application\/ld\+json/,/productWhatsappHref/])assert.match(component,pattern);
 assert.doesNotMatch(component,/Les seuils de classe et les plages comparatives|présentation provisoire|Mapei|Weber|Bostik|Grupo Puma/);
 for(const suffix of codes){
  const code='BOND-'+suffix;
  const slug='fenek-bond-'+suffix.toLowerCase();
  assert.ok(exportScript.includes(slug),slug);
  assert.ok(catalogueRoute.includes("'"+code+"'"),code);
  const rows=csv.split(/\r?\n/).filter(x=>x.startsWith(code+','));
  assert.ok(rows.length>=4,(code,rows.length));
  assert.ok(rows.every(x=>x.includes('à valider par le fabricant/laboratoire')),code);
  assert.ok(rows.some(x=>x.includes('valeur typique de famille')),code);
 }
});
