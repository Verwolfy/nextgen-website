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
/**
 * One product-only image directory for BOND, PROOF, FLOW and PAINT.
 * All 50 product references have their own editable-label illustration.
 * FLOW uses a smaller -card thumbnail, with both variants required.
 * The corrected 20 kg CM-O2P packaging retains an explicit versioned name.
 * These are unapproved editorial visuals, never certified packaging.
 */
const productImageName=(product:CatalogueProject,variant:'card'|'full'):string=>{
 const slug=product.code==='PROOF-CM-O2P'
   ? 'fenek-proof-cm-o2p-sac-20kg-v2' : product.slug;
 return slug+(product.gamme==='flow' && variant==='card'?'-card':'')+'.webp';
};

export const conceptPackshot=(product:CatalogueProject,variant:'card'|'full'='card'):string=>{
 const base='images/illustrations/produits/';
 const file=productImageName(product,variant);
 const relative=base+file;
 if(!existsSync(resolve(process.cwd(),'public',relative)))
   throw Error('FENEK product illustration missing: '+product.code+' -> '+relative);
 // Do not publish FLOW if either the full-size or catalogue thumbnail is absent.
 if(product.gamme==='flow' &&
   (!existsSync(resolve(process.cwd(),'public',base+productImageName(product,'card'))) ||
    !existsSync(resolve(process.cwd(),'public',base+productImageName(product,'full')))))
   throw Error('FENEK-FLOW card/full pair incomplete: '+product.code);
 return '/'+relative;
};

export const hasProductPackshot=(product:CatalogueProject):boolean=>{
 conceptPackshot(product,'full');
 return true;
};


/**
 * Editorial contact prompt for resin kits with unknown composition and capacity.
 * Do not infer a pack volume, mass or a technical formulation.
 * The original French wording follows the user's packaging instruction.
 */
export const packagingLabelFor = (format:string, lang:Lang):string => {
  if(format==="Sac 25 kg") return {
    fr:"Sac 25 kg",
    en:"25 kg bag",
    ar:"كيس 25 كغ",
  }[lang];
  if(format==="Bidon 5 L") return {
    fr:"Bidon 5 L",
    en:"5 L canister",
    ar:"عبوة 5 لترات",
  }[lang];
  if(format==="Bidon 20 L") return {
    fr:"Bidon 20 L",
    en:"20 L canister",
    ar:"عبوة 20 لترًا",
  }[lang];
  if(format==="Fût 200 L") return {
    fr:"Fût 200 L",
    en:"200 L drum",
    ar:"برميل 200 لتر",
  }[lang];
  if(format==="IBC 1000 L") return {
    fr:"IBC 1000 L",
    en:"1,000 L IBC",
    ar:"حاوية IBC سعة 1000 لتر",
  }[lang];
  if(format==="Seau 5 kg") return {
    fr:"Seau 5 kg",
    en:"5 kg bucket",
    ar:"دلو 5 كغ",
  }[lang];
  if(format==="Seau 10 kg") return {
    fr:"Seau 10 kg",
    en:"10 kg bucket",
    ar:"دلو 10 كغ",
  }[lang];
  if(format==="Seau 20 kg") return {
    fr:"Seau 20 kg",
    en:"20 kg bucket",
    ar:"دلو 20 كغ",
  }[lang];
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
  if(format==="Kit : sac 20 kg + bidon 10 kg") return {
    fr:"Kit : sac 20 kg + bidon 10 kg (30 kg au total)",
    en:"Kit: 20 kg bag + 10 kg canister (30 kg total)",
    ar:"طقم: كيس 20 كغ + عبوة 10 كغ (30 كغ إجمالاً)",
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
