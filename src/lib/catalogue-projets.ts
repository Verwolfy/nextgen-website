import raw from '../data/catalogue-projets.json';
import type { Lang, Range } from '../data/site';

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
export const conceptImage:Record<Range,string>={
  bond:'/images/3d-demo/sac-25kg-30.webp',
  proof:'/images/3d-demo/seau-20kg-30.webp',
  flow:'/images/3d-demo/bidon-20l-30.webp',
  paint:'/images/3d-demo/seau-20kg-30.webp'
};
