import type { Lang } from './site';

/** V3 Motion + Industry: editorial presentation only, not a statement of certification or production capacity. */
type HomeV3Copy = {
  eyebrow: string;
  headline: string;
  headlineAccent: string;
  lead: string;
  proof: string;
  featuredTitle: string;
  featuredLead: string;
  featuredLabel: string;
  featuredAction: string;
  featuredDisclaimer: string;
  rangesAction: string;
  stepsLabel: string;
};
export const homeV3Copy: Record<Lang, HomeV3Copy> = {
  fr: {
    eyebrow: 'BTPH · CONCEPTION · SOLUTIONS',
    headline: 'Le terrain inspire.',
    headlineAccent: 'Les solutions prennent forme.',
    lead: 'Découvrez une approche industrielle orientée vers les besoins des chantiers et les gammes FENEK : mortiers, étanchéité, adjuvants et revêtements.',
    proof: 'Des références présentées pour les distributeurs, entreprises et professionnels du BTPH en Algérie.',
    featuredTitle: 'Des références à découvrir',
    featuredLead: 'Une sélection de présentations FENEK. Spécifications et disponibilité à confirmer auprès de notre équipe.',
    featuredLabel: 'Présentation provisoire',
    featuredAction: 'Voir la référence',
    featuredDisclaimer: 'Les images sont des maquettes. Les fiches techniques et les données commerciales définitives ne sont pas validées.',
    rangesAction: 'Explorer le catalogue',
    stepsLabel: 'Notre démarche en trois étapes',
  },
  ar: {
    eyebrow: 'البناء والأشغال العمومية · التطوير · الحلول',
    headline: 'من الميدان تبدأ الفكرة.',
    headlineAccent: 'ومنها تتشكل الحلول.',
    lead: 'اكتشف منهجية صناعية تنطلق من احتياجات المشاريع، مع مجموعات FENEK للملاط والعزل المائي وإضافات الخرسانة والطلاءات.',
    proof: 'مراجع معروضة للموزعين والمؤسسات والمهنيين في قطاع البناء والأشغال العمومية والري في الجزائر.',
    featuredTitle: 'مراجع مقترحة للاطلاع',
    featuredLead: 'مجموعة مختارة من عروض FENEK. يجب تأكيد المواصفات والتوفر مباشرةً مع فريقنا.',
    featuredLabel: 'عرض أولي',
    featuredAction: 'عرض المرجع',
    featuredDisclaimer: 'الصور نماذج توضيحية، والبيانات الفنية والتجارية النهائية لم تُعتمد بعد.',
    rangesAction: 'استعراض الكتالوج',
    stepsLabel: 'منهجيتنا في ثلاث مراحل',
  },
  en: {
    eyebrow: 'CONSTRUCTION · DEVELOPMENT · SOLUTIONS',
    headline: 'Inspired by the field.',
    headlineAccent: 'Shaped into solutions.',
    lead: 'Discover an industry-focused approach grounded in jobsite needs and the FENEK ranges: mortars, waterproofing, admixtures and coatings.',
    proof: 'Catalogue references presented for distributors, contractors and construction professionals in Algeria.',
    featuredTitle: 'Explore selected references',
    featuredLead: 'A selection of FENEK presentations. Confirm technical details and availability with our team.',
    featuredLabel: 'Provisional presentation',
    featuredAction: 'View reference',
    featuredDisclaimer: 'Images are concept mockups. Final technical documents and commercial specifications are not yet validated.',
    rangesAction: 'Browse the catalogue',
    stepsLabel: 'Our three-step approach',
  },
};
