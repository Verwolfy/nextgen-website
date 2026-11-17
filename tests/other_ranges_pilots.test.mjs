import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
const read=p=>readFileSync(p,'utf8');
const source=JSON.parse(read('src/data/catalogue-projets.json'));
const groups={proof:11,flow:12,paint:11};
const data={};
for(const [range,count] of Object.entries(groups)){
 const txt=read('src/data/fenek-'+range+'-reference.ts');
 const pattern=new RegExp('export const '+range+'Definitions:OtherRaw\\[\\]=([\\s\\S]*?);\\nexport const');
 const m=txt.match(pattern);
 assert.ok(m,range+' definitions missing');
 const definitions=JSON.parse(m[1]);assert.equal(definitions.length,count,range);
 data[range]=definitions;
}
test('all 34 PROOF FLOW PAINT records are localized and not certified',()=>{
 assert.equal(source.length,50);
 for(const [range,count] of Object.entries(groups)){
  const products=source.filter(x=>x.gamme===range);
  assert.equal(products.length,count);
  const defs=data[range];
  for(const d of defs){
   const product=products.find(x=>x.code===d.code);
   assert.ok(product,d.code);
   assert.equal(product.certifie,false,d.code);
   assert.equal(product.commercialise,false,d.code);
   assert.equal(d.requirements.length,4,d.code);
   assert.equal(d.family.length,3,d.code);
   for(const lang of ['fr','ar','en']){
    assert.ok(d.intro[lang].length>=45,(d.code,lang));
    assert.ok(product.contenu[lang].description.length>=140,(d.code,lang));
    assert.equal(product.contenu[lang].usages.length,3,(d.code,lang));
    for(const metric of [...d.requirements,...d.family])assert.ok(metric[['fr','ar','en'].indexOf(lang)],d.code);
   }
  }
 }
});
test('public route and print component exclusively use product-qualified information',()=>{
 const comp=read('src/components/FenekOtherTechnicalPilot.astro');
 const route=read('src/pages/[lang]/documentation/[slug].astro');
 const catalogue=read('src/pages/[lang]/catalogue/[slug].astro');
 const exporter=read('scripts/export_c1t_pdfs.py');
 const csv=read('docs/INTERNE-validation-donnees.csv');
 assert.match(route,/FenekOtherTechnicalPilot/);
 assert.match(route,/otherTechnicalRecords/);
 assert.match(catalogue,/otherTechnicalRecords/);
 for(const pattern of [/data-other-technical-pilot/,/data-other-source-type/,/fenek-other-technical-print/,/FenekApplicationGuide lang=\\{lang\\} product=\\{product\\} concise/,/productWhatsappHref/,/application\\/ld\\+json/])assert.match(comp,pattern);
 assert.doesNotMatch(comp,/Mapei|Weber|Sika|Jotun|Caparol|Fosroc|Les seuils de classe et les plages comparatives/);
 for(const range of Object.keys(groups)){
  for(const def of data[range]){
   const slug='fenek-'+def.code.toLowerCase();
   assert.ok(exporter.includes(slug),slug);
   const rows=csv.split(/\\r?\\n/).filter(x=>x.startsWith(def.code+','));
   assert.ok(rows.length>=7,(def.code,rows.length));
   assert.ok(rows.every(x=>x.includes('à valider par le fabricant/laboratoire')),def.code);
  }
 }
});
