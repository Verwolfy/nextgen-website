import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
const read=p=>readFileSync(p,'utf8');

test('CG1 has dedicated trilingual grout sheet and the correct normative family',()=>{
 const route=read('src/pages/[lang]/documentation/[slug].astro');
 const catalogueRoute=read('src/pages/[lang]/catalogue/[slug].astro');
 const component=read('src/components/FenekCG1Pilot.astro');
 const data=read('src/data/fenek-cg1-reference.ts');
 const items=JSON.parse(read('src/data/catalogue-projets.json'));
 const item=items.find(x=>x.code==='BOND-CG1');
 assert.ok(item);assert.equal(item.certifie,false);assert.equal(item.commercialise,false);
 assert.match(route,/FenekCG1Pilot/);assert.match(route,/isCG1Pilot=product.code==='BOND-CG1'/);
 assert.match(catalogueRoute,/'BOND-CG1'/);
 for(const pattern of [/product.code!=='BOND-CG1'/,/data-cg1-pilot/,/fenek-cg1-print/,/data-cg1-source-type/,/FenekApplicationGuide lang=\{lang\} product=\{product\} concise/,/application\/ld\+json/,/EN 13888-1:2022/])assert.match(component,pattern);
 assert.doesNotMatch(component,/EN 12004|C2TE-S1|Weber|Bostik|Mapei|Sika|Les seuils de classe et les plages comparatives/);
 assert.equal((data.match(/kind:'norme'/g)||[]).length,8);
 assert.equal((data.match(/kind:'famille'/g)||[]).length,6);
 for(const lang of ['fr','ar','en']){assert.ok(item.contenu[lang].description.length>125);assert.equal(item.contenu[lang].usages.length,3);}
 assert.match(data,/EN 13888-1:2022/);
 assert.doesNotMatch(data,/important:|Les seuils de classe et les plages comparatives/);
});
test('CG1 registry distinguishes the norm from four source manufacturers',()=>{
 const rows=read('docs/INTERNE-validation-donnees.csv').split(/\r?\n/).filter(x=>x.startsWith('BOND-CG1,'));
 assert.ok(rows.length>=22,rows.length);
 for(const maker of ['Sika - SikaCeram-500 TG','BAL - BAL Grout','Weber - weberjoint wall','Bostik - CeraBest Fuga 105'])assert.ok(rows.some(x=>x.includes(maker)),maker);
 assert.equal(rows.filter(x=>x.includes('exigence normative EN 13888-1:2022 CG1')).length,8);
});
