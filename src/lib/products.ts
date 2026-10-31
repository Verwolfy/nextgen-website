import raw from '../../public/data/products.json';
import type { Lang, Range } from '../data/site';
export type Product = {slug:string;nom:string;gamme:Range;contenu:Record<Lang,{accroche:string;description:string;usages:string[]}>; conditionnements:{format:string;poids_net:number|null;unite:string}[];ordre:number;image?:string|null;modele_3d?:string|null;fiche_technique?:string|null;fds?:string|null};
// The secure Python sync is the sole publisher; no browser database requests.
// Keep build fail-closed if the JSON has an unexpected shape.
if (!Array.isArray(raw)) throw new Error('Catalogue public non conforme : tableau attendu');
export const products:Product[] = raw.map((r:unknown)=>{
 if (!r || typeof r!=='object') throw new Error('Produit invalide');
 const p=r as Record<string,unknown>;
 if (typeof p.slug !== 'string' || !/^[a-z0-9]+(-[a-z0-9]+)*$/.test(p.slug) || !['bond','proof','flow','paint'].includes(String(p.gamme))) throw new Error('Produit non validé');
 if (typeof p.nom !== 'string' || typeof p.contenu !== 'object' || !p.contenu || !Array.isArray(p.conditionnements)) throw new Error('Contenu manquant');
 for(const lang of ['fr','ar','en']){const d=(p.contenu as Record<string,unknown>)[lang] as Record<string,unknown>; if(!d || typeof d.description!=='string' || typeof d.accroche!=='string' || !Array.isArray(d.usages)) throw new Error('Traductions produit incomplètes');}
 return p as Product;
});
