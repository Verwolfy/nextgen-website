import type { Lang } from './site';

/** Lot 106: manually verified, dated editorial facts. No live feed or external calls. */
export type TickerCategory = 'btph' | 'economy' | 'innovation';
type RecordEntry = {
  id: string;
  category: TickerCategory;
  published: string;
  expires: string;
  source: string;
  sourceUrl: string; // Provenance only; NEVER emitted as a clickable site link.
  text: Record<Lang, string>;
};
const entries: RecordEntry[] = [
  {
    id:'roads-95',category:'btph',published:'2026-10-31',expires:'2026-11-21',source:'APS',
    sourceUrl:'https://www.aps.dz/fr/algerie/developpement/mvwf185y-lancement-et-mise-en-service-de-95-projets-de-developpement-du-reseau-routier-a-travers-24-wilayas',
    text:{fr:'95 projets routiers annoncés dans 24 wilayas',ar:'الإعلان عن 95 مشروعًا للطرق عبر 24 ولاية',en:'95 road projects announced across 24 provinces'},
  },
  {
    id:'roads-853',category:'btph',published:'2026-10-31',expires:'2026-11-21',source:'APS',
    sourceUrl:'https://www.aps.dz/fr/algerie/developpement/mvwf185y-lancement-et-mise-en-service-de-95-projets-de-developpement-du-reseau-routier-a-travers-24-wilayas',
    text:{fr:'853,5 km concernés par le programme routier annoncé',ar:'853.5 كلم ضمن برنامج الطرق المعلن عنه',en:'853.5 km covered by the announced road programme'},
  },
  {
    id:'housing-starts',category:'btph',published:'2026-10-22',expires:'2026-11-13',source:'APS',
    sourceUrl:'https://www.aps.dz/fr/economie/habitat-et-infrastructure/mvju9svb-plus-de-896-milliards-de-da-de-credits-de-paiement-proposes-au-secteur-de-l-habitat',
    text:{fr:'253 326 logements mis en chantier à fin septembre 2026',ar:'انطلاق أشغال 253326 سكنًا حتى نهاية سبتمبر 2026',en:'253,326 homes started by end-September 2026'},
  },
  {
    id:'housing-distribution',category:'btph',published:'2026-10-31',expires:'2026-11-21',source:'APS',
    sourceUrl:'https://www.aps.dz/fr/economie/habitat-et-infrastructure/mvw8zwu1-distribution-de-133-780-logements-a-travers-le-pays-a-partir-de-dimanche',
    text:{fr:'133 780 logements et aides : distribution annoncée',ar:'الإعلان عن توزيع 133780 سكنًا وإعانة',en:'133,780 homes and housing grants announced for distribution'},
  },
  {
    id:'setif-water',category:'btph',published:'2026-11-03',expires:'2026-11-24',source:'APS',
    sourceUrl:'https://www.aps.dz/fr/algerie/developpement/mw0tqlwj-bouzegza-donne-le-coup-d-envoi-du-projet-d-aep-d-el-eulma-et-de-15-autres-communes',
    text:{fr:'Sétif : lancement du projet d’eau potable pour El Eulma et 15 communes',ar:'سطيف: انطلاق مشروع المياه الصالحة للشرب للعلمـة و15 بلدية',en:'Sétif: drinking-water project launched for El Eulma and 15 municipalities'},
  },
  {
    id:'eur-dzd',category:'economy',published:'2026-11-05',expires:'2026-11-12',source:'Banque d’Algérie',
    sourceUrl:'https://www.bank-of-algeria.dz/',
    text:{fr:'EUR/DZD : 152,76 DA, vente officielle du 05/11',ar:'يورو/دينار: 152.76 دج سعر البيع الرسمي 05/11',en:'EUR/DZD: 152.76 DZD official selling rate, 05 Nov'},
  },
  {
    id:'usd-dzd',category:'economy',published:'2026-11-05',expires:'2026-11-12',source:'Banque d’Algérie',
    sourceUrl:'https://www.bank-of-algeria.dz/',
    text:{fr:'USD/DZD : 135,94 DA, vente officielle du 05/11',ar:'دولار/دينار: 135.94 دج سعر البيع الرسمي 05/11',en:'USD/DZD: 135.94 DZD official selling rate, 05 Nov'},
  },
  {
    id:'cement-energy',category:'innovation',published:'2026-04-20',expires:'2026-11-20',source:'APS',
    sourceUrl:'https://www.aps.dz/fr/algerie/developpement/mo7ar2xh-lancement-d-un-projet-de-valorisation-energetique-des-dechets',
    text:{fr:'Cimenterie de Chlef : projet de valorisation énergétique des déchets',ar:'مصنع الإسمنت بالشلف: مشروع لاسترجاع الطاقة من النفايات',en:'Chlef cement plant: waste-to-energy recovery project'},
  },
];
const categories: Record<Lang,Record<TickerCategory,string>> = {
  fr:{btph:'BTPH',economy:'Économie',innovation:'Innovation'},
  ar:{btph:'البناء',economy:'الاقتصاد',innovation:'ابتكار'},
  en:{btph:'Construction',economy:'Economy',innovation:'Innovation'},
};
const labels:Record<Lang,{label:string;fallback:string}>={
  fr:{label:'Fil BTPH et économie — informations datées',fallback:'Informations en cours d’actualisation'},
  ar:{label:'شريط أخبار البناء والاقتصاد — معلومات مؤرخة',fallback:'يجري تحديث المعلومات'},
  en:{label:'Construction and economy — dated updates',fallback:'Information being updated'},
};
export const tickerRecords=entries; // Trusted editorial register, not sent as client JS.
export const tickerContent=Object.fromEntries((['fr','ar','en'] as const).map(lang=>[
  lang,{...labels[lang],items:entries.map(item=>({
    id:item.id,category:categories[lang][item.category],
    text:item.text[lang],source:item.source,date:item.published,expires:item.expires,
  }))},
])) as Record<Lang,{label:string;fallback:string;items:{id:string;category:string;text:string;source:string;date:string;expires:string}[]}>;
