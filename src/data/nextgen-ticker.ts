import type { Lang } from './site';

/** Curated, dated links. No live claims, unverified exchange values, or client API calls. */
type TickerItem = { category: string; text: string; source: string; date: string; url: string };
type TickerCopy = { label: string; items: TickerItem[] };
const roads = 'https://www.aps.dz/fr/algerie/developpement/mvwf185y-lancement-et-mise-en-service-de-95-projets-de-developpement-du-reseau-routier-a-travers-24-wilayas';
const maintenance = 'https://www.aps.dz/fr/economie/habitat-et-infrastructure/mvnxgk43-djellaoui-preside-une-reunion-de-coordination-sur-l-entretien-des-routes';
const fx = 'https://www.bank-of-algeria.dz/';
export const tickerContent: Record<Lang, TickerCopy> = {
  fr: {
    label: 'Fil d’informations BTPH et économie, sources datées',
    items: [
      { category: 'BTPH', text: 'Réseau routier : 95 projets annoncés dans 24 wilayas', source: 'APS', date: '31/10/2026', url: roads },
      { category: 'Économie', text: 'Cours officiels EUR/DZD et USD/DZD : consulter la Banque d’Algérie', source: 'Banque d’Algérie', date: 'Source officielle', url: fx },
      { category: 'BTPH', text: 'Programme d’entretien des routes et autoroutes', source: 'APS', date: '25/10/2026', url: maintenance },
    ],
  },
  ar: {
    label: 'شريط أخبار البناء والأشغال العمومية والاقتصاد مع مصادر مؤرخة',
    items: [
      { category: 'البناء', text: 'الإعلان عن 95 مشروعًا للطرق عبر 24 ولاية', source: 'وأج', date: '31/10/2026', url: roads },
      { category: 'الاقتصاد', text: 'أسعار الصرف الرسمية لليورو والدولار: بنك الجزائر', source: 'بنك الجزائر', date: 'المصدر الرسمي', url: fx },
      { category: 'البناء', text: 'برنامج صيانة الطرق والطرق السريعة', source: 'وأج', date: '25/10/2026', url: maintenance },
    ],
  },
  en: {
    label: 'Construction and economy news ticker with dated sources',
    items: [
      { category: 'Construction', text: '95 road projects announced across 24 provinces', source: 'APS', date: '31 Oct 2026', url: roads },
      { category: 'Economy', text: 'Official EUR/DZD and USD/DZD rates: consult the Bank of Algeria', source: 'Bank of Algeria', date: 'Official source', url: fx },
      { category: 'Construction', text: 'Road and motorway maintenance programme', source: 'APS', date: '25 Oct 2026', url: maintenance },
    ],
  },
};
