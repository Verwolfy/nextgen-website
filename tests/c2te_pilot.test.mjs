import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';

const read=path=>readFileSync(path,'utf8');
test('C2TE source-backed page remains unique, localized and without obsolete disclaimers',()=>{
 const route=read('src/pages/[lang]/documentation/[slug].astro');
 const component=read('src/components/FenekC2TEPilot.astro');
 const data=read('src/data/fenek-c2te-reference.ts');
 const catalogue=JSON.parse(read('src/data/catalogue-projets.json'));
 const item=catalogue.find(x=>x.code==='BOND-C2TE');
 assert.equal(item.slug,'fenek-bond-c2te');
 assert.equal(item.gamme,'bond');
 assert.equal(item.certifie,false);
 assert.equal(item.commercialise,false);
 assert.match(route,/product.code==='BOND-C2TE'/);
 assert.match(route,/FenekC2TEPilot/);
 assert.match(component,/product.code!=='BOND-C2TE'/);
 assert.match(component,/data-c2te-pilot/);
 assert.match(component,/FenekApplicationGuide lang=\{lang\} product=\{product\} concise/);
 assert.match(component,/data-c2te-source-type/);
 assert.match(component,/fenek-c2te-print/);
 assert.match(component,/hasPublishedPdf/);
 assert.match(component,/application\/ld\+json/);
 assert.match(component,/productWhatsappHref/);
 assert.doesNotMatch(component,/t[.]important|figuresNote|BROUILLON|présentation provisoire/i);
 assert.doesNotMatch(component,/Sika|Mapei|Weber/i);
 assert.doesNotMatch(data,/important:|figuresNote:|Les seuils de classe et les plages comparatives/);
 assert.match(data,/value:'≥ 1,0 N\/mm²'/);
 assert.match(data,/value:'≥ 0,5 N\/mm² \\(30 min\\)'/);
 assert.match(data,/value:'≤ 0,5 mm'/);
 assert.match(data,/c2teCopy:Record<Lang,Copy>/);
 const normative=(data.match(/kind:'norme'/g)||[]).length;
 const family=(data.match(/kind:'famille'/g)||[]).length;
 assert.equal(normative,7);
 assert.equal(family,6);
 for(const lang of ['fr','ar','en']){
   assert.ok(item.contenu[lang].description.length>130);
   assert.equal(item.contenu[lang].usages.length,3);
 }
});

test('C2TE internal source log names three independent competitors and normative class',()=>{
 const csv=read('docs/INTERNE-validation-donnees.csv');
 const rows=csv.trim().split(/\r?\n/).filter(line=>line.startsWith('BOND-C2TE,'));
 assert.ok(rows.length>=45,`Expected extensive C2TE provenance, got ${rows.length}`);
 for(const brand of [
   'Mapei — Adesilex P9 (SG)',
   'Sika — SikaCeram-205 NG Grey (NG)',
   'Weber / Saint-Gobain — weberset easy flex 218 (MY)'
 ])assert.ok(csv.includes(brand),brand);
 assert.match(csv,/BOND-C2TE,Adhérence après temps ouvert prolongé E/);
 assert.match(csv,/à valider par le fabricant\/laboratoire/);
 assert.ok(!read('src/components/FenekC2TEPilot.astro').includes('https://cdnmedia.mapei.com'));
});
