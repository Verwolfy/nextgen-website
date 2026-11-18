import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
const read=path=>readFileSync(path,'utf8');
const catalogue=JSON.parse(read('src/data/catalogue-projets.json'));
const counts={proof:11,flow:12,paint:11};
const all={};
for(const [range,expected] of Object.entries(counts)){
 const text=read('src/data/fenek-'+range+'-reference.ts');
 const start='export const '+range+'Definitions:OtherRaw[]=';
 const first=text.indexOf(start);
 const end=text.indexOf(';\nexport const',first);
 assert.ok(first>0&&end>first,'Missing '+range+' technical definitions');
 all[range]=JSON.parse(text.slice(first+start.length,end));
 assert.equal(all[range].length,expected,range);
}
test('34 PROOF FLOW PAINT records have 102 trilingual sheets with class-specific criteria',()=>{
 assert.equal(catalogue.length,50);
 for(const [range,count] of Object.entries(counts)){
  const products=catalogue.filter(x=>x.gamme===range);
  assert.equal(products.length,count,range);
  for(const record of all[range]){
   const item=products.find(x=>x.code===record.code);
   assert.ok(item,record.code);
   assert.equal(item.certifie,false,record.code);
   assert.equal(item.commercialise,false,record.code);
   assert.equal(record.requirements.length,4,record.code);
   assert.equal(record.family.length,3,record.code);
   for(const lang of ['fr','ar','en']){
    assert.ok(record.intro[lang].length>=30,[record.code,lang]);
    assert.ok(item.contenu[lang].description.length>=140,[record.code,lang]);
    assert.equal(item.contenu[lang].usages.length,3,[record.code,lang]);
    for(const metric of [...record.requirements,...record.family]){
     assert.ok(metric[['fr','ar','en'].indexOf(lang)],[record.code,lang]);
    }
   }
  }
 }
});
test('pilot routes, 150-PDF generator and internal technical sources remain connected',()=>{
 const component=read('src/components/FenekOtherTechnicalPilot.astro');
 const route=read('src/pages/[lang]/documentation/[slug].astro');
 const catRoute=read('src/pages/[lang]/catalogue/[slug].astro');
 const exporter=read('scripts/export_c1t_pdfs.py');
 const csv=read('docs/INTERNE-validation-donnees.csv');
 assert.ok(route.includes('FenekOtherTechnicalPilot'));
 assert.ok(route.includes('otherTechnicalRecords'));
 assert.ok(catRoute.includes('otherTechnicalRecords'));
 for(const marker of ['data-other-technical-pilot','data-other-source-type',
  'fenek-other-technical-print','FenekApplicationGuide lang={lang} product={product} concise',
  'productWhatsappHref','application/ld+json'])
  assert.ok(component.includes(marker),marker);
 assert.doesNotMatch(component,/Mapei|Weber|Sika|Jotun|Caparol|Fosroc|Les seuils de classe et les plages comparatives/);
 for(const range of Object.keys(counts)){
  for(const item of all[range]){
   assert.ok(exporter.includes('fenek-'+item.code.toLowerCase()),item.code);
   const rows=csv.split(/\r?\n/).filter(row=>row.startsWith(item.code+','));
   assert.ok(rows.length>=7,[item.code,rows.length]);
   assert.ok(rows.every(row=>row.includes('à valider par le fabricant/laboratoire')),item.code);
  }
 }
});

test('the same two-page product+guide structure covers all 50 FENEK references',()=>{
 const components=[
   'FenekC1TEPilot','FenekC2FTPilot','FenekC2TEPilot','FenekC2TES1Pilot',
   'FenekCG1Pilot','FenekBondTechnicalPilot','FenekOtherTechnicalPilot'
 ];
 for(const component of components){
   const file=read('src/components/'+component+'.astro');
   assert.match(file,/FenekPrintTechnicalCover/);
   assert.match(file,/FenekPrintApplicationPage/);
   assert.match(file,/(Requirements|requirements)/);
 }
 const guide=read('src/components/FenekPrintApplicationPage.astro');
 const cover=read('src/components/FenekPrintTechnicalCover.astro');
 const qr=read('src/lib/qrcodegen.ts');
 for(const token of ['reviewedV3GuideFor','qrcodegen.QrCode.encodeText','data-fenek-qr-url',
    'data-fenek-guide-sprite','data-fenek-guide-step','background-size:300% 200%',
    'page-break-before:always'])assert.ok(guide.includes(token),token);
 assert.ok(qr.includes('Copyright (c) Project Nayuki. (MIT License)'));
 assert.ok(cover.includes('data-fenek-print-cover'));
 assert.ok(cover.includes('data-fenek-print-criteria'));
 assert.ok(cover.includes('01 / 02'));
 assert.equal((guide.match(/<div class="fenek-print-masthead">/g)||[]).length,1);
 assert.doesNotMatch(guide,/6 ÉTAPES|Parcours de mise en œuvre · Illustrations semi-réalistes validées/);
});
