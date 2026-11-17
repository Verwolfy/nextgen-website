import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
const read=p=>readFileSync(p,'utf8');

test('C2TE-S1 has dedicated FR AR EN product sheet, S1 classification and no removed note',()=>{
 const route=read('src/pages/[lang]/documentation/[slug].astro');
 const component=read('src/components/FenekC2TES1Pilot.astro');
 const data=read('src/data/fenek-c2tes1-reference.ts');
 const cat=JSON.parse(read('src/data/catalogue-projets.json'));
 const item=cat.find(x=>x.code==='BOND-C2TE-S1');
 assert.ok(item);
 assert.equal(item.certifie,false);
 assert.equal(item.commercialise,false);
 assert.match(route,/FenekC2TES1Pilot/);
 assert.match(route,/product.code==='BOND-C2TE-S1'/);
 assert.match(component,/product.code!=='BOND-C2TE-S1'/);
 for(const re of [/data-c2tes1-pilot/,/fenek-c2tes1-print/,/FenekApplicationGuide lang=\{lang\} product=\{product\} concise/,/data-c2tes1-source-type/,/productWhatsappHref/,/application\/ld\+json/]) assert.match(component,re);
 assert.doesNotMatch(component,/Sika|Mapei|Weber|BROUILLON|présentation provisoire|t[.]important/);
 assert.doesNotMatch(data,/important:|figuresNote:|Les seuils de classe et les plages comparatives/);
 assert.equal((data.match(/kind:'norme'/g)||[]).length,8);
 assert.equal((data.match(/kind:'famille'/g)||[]).length,6);
 assert.match(data,/key:'s1-deformabilite'/);
 assert.ok(data.includes("value:'≥ 2,5 mm ; < 5 mm'"));
 assert.ok(data.includes("value:'≥ 0,5 N/mm² (30 min)'"));
 for(const lang of ['fr','ar','en']){
   assert.ok(item.contenu[lang].description.length>125);
   assert.equal(item.contenu[lang].usages.length,3);
 }
});

test('C2TE-S1 traceability registry names three distinct manufacturers',()=>{
 const csv=read('docs/INTERNE-validation-donnees.csv');
 const rows=csv.trim().split(/\r?\n/).filter(x=>x.startsWith('BOND-C2TE-S1,'));
 assert.ok(rows.length>=35,rows.length);
 for(const maker of ['Sika - SikaCeram-288 MY','Mapei - Keraflex Maxi S1 Zero','Weber - weberset SPF'])
   assert.ok(csv.includes(maker),maker);
 assert.match(csv,/exigence normative EN 12004-1:2017 S1/);
 assert.match(csv,/à valider par le fabricant\/laboratoire/);
});
