import type { Lang } from './site';
/** Public editorial labels. Technical application instructions are intentionally
 * excluded until a product-specific, reviewed datasheet exists. */
export const catalogueCopy:Record<Lang,{
 title:string;lead:string;intro:string;count:string;view:string;concept:string;
 format:string;unknownFormat:string;application:string;back:string;quote:string;
 rangeNav:string;category:string;contactNote:string;
}>={
 fr:{
  title:'Catalogue FENEK · 50 références',
  lead:'Explorez les quatre gammes FENEK et leurs familles d’applications.',
  intro:'Découvrez les références par gamme, leur présentation et les conditionnements répertoriés.',
  count:'références',view:'Voir la fiche',concept:'Catalogue FENEK',
  format:'Conditionnements',unknownFormat:'Nous consulter',application:'Présentation',
  back:'Retour au catalogue',quote:'Nous contacter',rangeNav:'Explorer par gamme',
  category:'Domaine',contactNote:'Pour les informations techniques et les modalités de fourniture, contactez NextGen.',
 },
 ar:{
  title:'كتالوج FENEK · 50 مرجعًا',
  lead:'تعرّف على مجموعات FENEK الأربع ومجالاتها.',
  intro:'استكشف المراجع حسب المجموعة مع وصف موجز وتفاصيل العبوات المدرجة.',
  count:'مرجعًا',view:'عرض المنتج',concept:'كتالوج FENEK',
  format:'العبوات',unknownFormat:'يرجى التواصل معنا',application:'التعريف بالمنتج',
  back:'العودة إلى الكتالوج',quote:'تواصل معنا',rangeNav:'تصفّح حسب المجموعة',
  category:'المجال',contactNote:'للاستفسار عن المعلومات الفنية وشروط التوريد، تواصل مع NextGen.',
 },
 en:{
  title:'FENEK catalogue · 50 references',
  lead:'Explore the four FENEK ranges and their areas of application.',
  intro:'Browse product references by range, with descriptions and listed packaging options.',
  count:'references',view:'View details',concept:'FENEK catalogue',
  format:'Packaging options',unknownFormat:'Contact us',application:'Overview',
  back:'Back to catalogue',quote:'Contact us',rangeNav:'Browse by range',
  category:'Category',contactNote:'Contact NextGen for technical information and supply enquiries.',
 },
};
