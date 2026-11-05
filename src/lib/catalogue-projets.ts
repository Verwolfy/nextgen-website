import raw from '../data/catalogue-projets.json';
import type { Lang, Range } from '../data/site';
import { existsSync } from 'node:fs';
import { resolve } from 'node:path';

// Editorial concepts explicitly accepted by the user for a draft catalogue.
// These NEVER pass the certified-product synchronization gate.
export type CatalogueProject = {
  code: string; slug: string; nom: string; gamme: Range; ordre: number;
  contenu: Record<Lang,{accroche:string;description:string;usages:string[]}>;
  mode_fr_preparatoire: string;
  conditionnements: {format:string;poids_net:number|null;unite:string}[];
  statut:'presentation_provisoire'; certifie:false; commercialise:false;
};
const projects=raw as CatalogueProject[];
const slugPattern=/^[a-z0-9]+(?:-[a-z0-9]+)*$/;
if(projects.length!==50 || new Set(projects.map(p=>p.slug)).size!==50) throw Error('Catalogue projet incomplet ou doublons');
for(const p of projects){
 if(!slugPattern.test(p.slug)||!['bond','proof','flow','paint'].includes(p.gamme)||p.statut!=='presentation_provisoire'||p.certifie!==false||p.commercialise!==false)
   throw Error('Produit projet non conforme: '+p.code);
 if(!p.nom||!p.mode_fr_preparatoire||!Array.isArray(p.conditionnements)||p.conditionnements.some(c=>typeof c.format!=='string'))
   throw Error('Source produit incomplète: '+p.code);
 for(const lang of ['fr','ar','en'] as const){
   const t=p.contenu[lang];
   if(!t||!t.description||!t.accroche||!Array.isArray(t.usages)) throw Error('Traduction projet incomplète: '+p.code);
   if([t.description,t.accroche,...t.usages].some(s=>s.includes('<')||s.includes('>'))) throw Error('Texte HTML interdit');
 }
}
export const catalogueProjects = projects;
export const projectsByRange=(range:Range)=>catalogueProjects.filter(p=>p.gamme===range);
/** Exact product codes visually read from the uploaded 46-image concept gallery.
 * This links editorial mockups, not technical/certified/contractual imagery.
 * Eleven FENEK-PAINT references have no individual image in this archive.
 */
export const reviewedGalleryForReference:Readonly<Record<string,number>> = {
  // Lot 29: studio bag renders replacing ten flat-label concept shots.
  'fenek-bond-c1t':20, 'fenek-bond-c1te':21,
  'fenek-bond-c2te':22, 'fenek-bond-c2te-s1':23,
  'fenek-bond-c2ft':24, 'fenek-bond-cg1':25,
  'fenek-bond-cg2wa':26, 'fenek-bond-ct-c25-f5':27,
  'fenek-bond-gr-hr':31, 'fenek-bond-gp-csii':32,
  'fenek-bond-m10':35, 'fenek-bond-m5':34, 'fenek-bond-oc-csiii':33,
  'fenek-bond-r2':28, 'fenek-bond-r3':29, 'fenek-bond-r4':30,
  'fenek-proof-acr-rf':39, 'fenek-proof-cm-o1p':36, 'fenek-proof-cm-o2p':37,
  'fenek-proof-ep-anc':44, 'fenek-proof-ep-inj':43, 'fenek-proof-ep-prim':40,
  'fenek-proof-ep-sb':42, 'fenek-proof-ep-sr':41, 'fenek-proof-pu-1k':38,
  'fenek-proof-pu-inj':45, 'fenek-proof-pu-seal':4
};
const reviewedGalleryImage=(product:CatalogueProject):string|null=>{
  const number=reviewedGalleryForReference[product.slug];
  if(number===undefined) return null;
  const relative='images/maquettes/maquette-'+String(number).padStart(2,'0')+'.webp';
  if(!existsSync(resolve(process.cwd(),'public',relative))) {
    throw Error('Maquette de conception absente: '+product.code+' -> '+relative);
  }
  return '/'+relative;
};

export const conceptImage:Record<Range,string>={
  // Neutral branding only: never substitute a packaging concept for another SKU.
  bond:'/images/Logo1.jpg',
  proof:'/images/Logo1.jpg',
  flow:'/images/Logo1.jpg',
  paint:'' // no fallback: missing individual PAINT artwork fails the build
};


/**
 * A product-specific mockup is used only if the exact reviewed WebP exists
 * in the repository at build time. Never show broken src URLs and never infer
 * a certified pack or an approved net-volume label from an AI picture.
 * No dynamic client JS, network request or external image host is involved.
 */
export const conceptPackshot=(product:CatalogueProject,variant:'card'|'full'='card'):string=>{
 // Exact code-specific photorealistic editorial PAINT assets from the
 // user's 11-reference concept board. Fail closed if one binary is missing:
 // never silently show the generic 15 L collage or a different product code.
 if(product.gamme==='paint'){
   const relative='images/catalogue-projects/'+product.slug+'.webp';
   if(!existsSync(resolve(process.cwd(),'public',relative)))
      throw Error('FENEK-PAINT concept asset missing: '+product.code+' -> '+relative);
   return '/'+relative;
 }
 // Prefer the code-specific realistic studio render already in the concept
 // gallery for BOND. Preserve the original reviewed WebP files as archival
 // sources, but do not keep showing the older flat-label composition.
 if(product.gamme==='bond'){
   const updatedConcept=reviewedGalleryImage(product);
   if(updatedConcept) return updatedConcept;
 }
 const flow = product.gamme==='flow' && product.conditionnements.some(c=>c.format==='Bidon 20 L');
 const bond = product.gamme==='bond' && product.conditionnements.some(c=>c.format==='Sac 25 kg');
 if(flow || bond){
   const name=product.slug+(variant==='card'?'-card':'')+'.webp';
   const relative='images/catalogue-projects/'+name;
   const absolute=resolve(process.cwd(),'public',relative);
   const alternate=resolve(process.cwd(),'public','images/catalogue-projects/',
      product.slug+(variant==='card'?'': '-card')+'.webp');
   // Never show an incomplete binary upload (only card or only full).
   if(existsSync(absolute)&&existsSync(alternate)) return '/'+relative;
 }
 // Reuse exact label-matched design concepts from Lot 27 before generic art.
 return reviewedGalleryImage(product)??conceptImage[product.gamme];
};
export const hasProductPackshot=(product:CatalogueProject):boolean=>
 conceptPackshot(product,'full')!==conceptImage[product.gamme];


/**
 * Editorial contact prompt for resin kits with unknown composition and capacity.
 * Do not infer a pack volume, mass or a technical formulation.
 * The original French wording follows the user's packaging instruction.
 */
export const packagingLabelFor = (format:string, lang:Lang):string => {
  if(format==="Kit : seau 5 kg + seau 5 kg") return {
    fr:"Kit : seau 5 kg + seau 5 kg",
    en:"Kit: two 5 kg buckets (10 kg total)",
    ar:"طقم: دلوان، كل واحد 5 كغ (10 كغ إجمالاً)",
  }[lang];
  if(format==="Kit : seau 10 kg + seau 3 kg") return {
    fr:"Kit : seau 10 kg + seau 3 kg",
    en:"Kit: 10 kg bucket + 3 kg bucket",
    ar:"طقم: دلو 10 كغ + دلو 3 كغ",
  }[lang];
  if(format==="Kit : seau A 10 kg + seau B 3 kg") return {
    fr:"Kit : seau A 10 kg + seau B 3 kg",
    en:"Kit: 10 kg bucket A + 3 kg bucket B",
    ar:"طقم: دلو أ 10 كغ + دلو ب 3 كغ",
  }[lang];
  if(format==="Double cartouche 300 + 300 mL (600 mL au total)") return {
    fr:"Double cartouche 300 + 300 mL (600 mL au total)",
    en:"Dual cartridge 300 + 300 mL (600 mL total)",
    ar:"خرطوشة مزدوجة 300 + 300 مل (600 مل إجمالاً)",
  }[lang];
  if(format==="Double cartouche bicomposant 600 mL (A : résine + B : durcisseur)") return {
    fr:"Double cartouche bicomposant 600 mL (A : résine + B : durcisseur)",
    en:"600 mL dual-component cartridge (A: resin + B: hardener)",
    ar:"خرطوشة مزدوجة المكونات 600 مل (أ: راتنج + ب: مصلّب)",
  }[lang];
  if(format==="Kit : sac 30 kg + bidon 10 kg") return {
    fr:"Kit : sac 30 kg + bidon 10 kg",
    en:"Kit: 30 kg bag + 10 kg canister",
    ar:"طقم: كيس 30 كغ + عبوة 10 كغ",
  }[lang];
  if(format==="Cartouche 300 mL") return {
    fr:"Cartouche 300 mL",
    en:"300 mL cartridge",
    ar:"خرطوشة 300 مل",
  }[lang];
  if(format!=="Kit résine - Contacter nous pour plus d'informations") return format;
  return {
    fr:"Kit résine - Contacter nous pour plus d'informations",
    en:"Resin kit — Contact us for more information",
    ar:"طقم راتنج — تواصل معنا لمزيد من المعلومات",
  }[lang];
};
