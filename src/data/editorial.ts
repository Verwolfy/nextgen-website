import type { Lang, Range } from './site';

// Editorial taxonomy, NOT approved products, performance claims or laboratory results.
type RangeTopics = Record<Range, readonly [string, string, string]>;
type EditorialCopy = {
  marketTag: string;
  homeStatus: string;
  homeContact: string;
  homeApproachTag: string;
  mascotAlt: string;
  rangesLead: string;
  topicsHeading: string;
  rangeDisclaimer: string;
  rangeBack: string;
  rangeCatalogue: string;
  rangeContact: string;
  rangeTopics: RangeTopics;
  aboutHeading: string;
  aboutKicker: string;
  aboutLead: string;
  aboutSteps: readonly [string, string, string];
  aboutDetails: readonly [string, string, string];
  aboutHighlights: readonly [readonly string[], readonly string[], readonly string[]];
  aboutCta: string;
  aboutNotice: string;
  resourceHeading: string;
  resourceLead: string;
  resourceTechTitle: string;
  resourceTechInfo: string;
  resourceSafetyTitle: string;
  resourceSafetyInfo: string;
  resourcePending: string;
};
export const editorialCopy: Record<Lang, EditorialCopy> = {
  fr: {
    marketTag: 'NextGen Building Solutions · Algérie',
    homeStatus: 'Découvrez les familles FENEK.',
    homeContact: 'Nous contacter',
    homeApproachTag: 'Notre démarche',
    mascotAlt: 'Nexo, mascotte NextGen',
    rangesLead: 'Parcourez les quatre familles FENEK et leurs domaines d’application.',
    topicsHeading: 'Domaines présentés',
    rangeDisclaimer: 'Pour les spécifications techniques et la disponibilité, contactez NextGen.',
    rangeBack: 'Toutes les gammes',
    rangeCatalogue: 'Explorer les références',
    rangeContact: 'Contacter NextGen',
    rangeTopics: {
      bond: ['Mortiers', 'Colles et joints', 'Réparation'],
      proof: ['Étanchéité', 'Protection', 'Résines'],
      flow: ['Béton', 'Mortier', 'Adjuvants'],
      paint: ['Peintures', 'Revêtements', 'Finitions'],
    },
    aboutHeading: 'Notre démarche industrielle',
    aboutKicker: 'Solutions BTPH · Vision industrielle',
    aboutLead: 'De la conception des produits à leur fabrication, jusqu’aux professionnels du BTPH : une démarche guidée par les besoins du terrain.',
    aboutSteps: ['Concevoir pour le terrain', 'Produire avec méthode', 'Distribuer et accompagner'],
    aboutDetails: [
      'Comprendre les contraintes des ouvrages et traduire les besoins des professionnels en solutions de mortiers, résines, adjuvants et revêtements.',
      'Structurer la fabrication, les matières premières et le conditionnement, avec des contrôles à définir et valider pour chaque référence.',
      'Préparer la mise à disposition des produits et accompagner les distributeurs et applicateurs avec une documentation vérifiée avant diffusion.',
    ],
    aboutHighlights: [
      ['Besoins des chantiers', 'Développement produit', 'Solutions adaptées'],
      ['Fabrication', 'Conditionnement', 'Contrôle qualité', 'Traçabilité'],
      ['Réseau professionnel', 'Assistance technique', 'Retour terrain'],
    ],
    aboutCta: 'Des solutions pensées pour être produites et utiles sur les chantiers.',
    aboutNotice: 'Les caractéristiques, contrôles et documents propres à chaque produit restent soumis aux validations requises.',
    resourceHeading: 'Ressources et documents',
    resourceLead: 'Retrouvez les fiches produits FENEK et les informations utiles à vos projets.',
    resourceTechTitle: 'Fiches produits FENEK',
    resourceTechInfo: 'Descriptifs, domaines d’application et présentations de nos 50 références.',
    resourceSafetyTitle: 'Fiches de données de sécurité',
    resourceSafetyInfo: 'Pour toute question relative aux fiches de sécurité, contactez notre équipe.',
    resourcePending: 'Nous contacter',
  },
  ar: {
    marketTag: 'NextGen Building Solutions · الجزائر',
    homeStatus: 'تعرّف على مجموعات FENEK.',
    homeContact: 'تواصل معنا',
    homeApproachTag: 'منهجية العمل',
    mascotAlt: 'نيكسو، شخصية نكست جن التوضيحية',
    rangesLead: 'تعرّف على مجموعات FENEK الأربع ومجالات استخدامها.',
    topicsHeading: 'مجالات الاستخدام',
    rangeDisclaimer: 'للحصول على التفاصيل الفنية والتوفر، تواصل مع فريق NextGen.',
    rangeBack: 'العودة إلى الفئات',
    rangeCatalogue: 'استعراض المراجع',
    rangeContact: 'تواصل مع نكست جن',
    rangeTopics: {
      bond: ['الملاط', 'لواصق البلاط وملء الفواصل', 'مواد الإصلاح'],
      proof: ['العزل المائي', 'الحماية السطحية', 'الراتنجات'],
      flow: ['الخرسانة', 'الملاط', 'الإضافات'],
      paint: ['الدهانات', 'الطلاءات', 'التشطيبات'],
    },
    aboutHeading: 'منهجيتنا الصناعية',
    aboutKicker: 'حلول البناء · رؤية صناعية',
    aboutLead: 'من تطوير المنتجات إلى تصنيعها ثم وصولها إلى مهنيّي البناء والأشغال العمومية والري: منهجية تنطلق من احتياجات الميدان.',
    aboutSteps: ['تصميم حلول للميدان', 'تصنيع بمنهجية واضحة', 'التوزيع والمرافقة'],
    aboutDetails: [
      'فهم متطلبات شركات المقاولات والمشاريع وتحويل احتياجات المهنيين إلى حلول في الملاط والراتنجات والإضافات والطلاءات.',
      'تنظيم التصنيع والمواد الأولية والتعبئة ومراجعة بيانات المنتجات، مع تحديد اختبارات المراقبة واعتمادها لكل منتج على حدة.',
      'التحضير لتوفير المنتجات ودعم الموزعين والمطبقين بوثائق فنية تُراجع قبل نشرها.',
    ],
    aboutHighlights: [
      ['احتياجات المشاريع', 'تطوير المنتجات', 'حلول ملائمة'],
      ['التصنيع', 'التعبئة', 'مراقبة الجودة', 'التتبع'],
      ['شبكة المهنيين', 'الدعم التقني', 'ملاحظات الميدان'],
    ],
    aboutCta: 'حلول مصممة للتصنيع وخدمة مشاريع البناء.',
    aboutNotice: 'تظل خصائص كل منتج واختباراته ووثائقه خاضعة للمراجعة والموافقات اللازمة.',
    resourceHeading: 'الموارد والوثائق الفنية',
    resourceLead: 'تصفح بطاقات منتجات FENEK والمعلومات المفيدة لمشاريعك.',
    resourceTechTitle: 'بطاقات منتجات FENEK',
    resourceTechInfo: 'الأوصاف ومجالات الاستخدام وأشكال التعبئة المقترحة لمراجعنا الخمسين.',
    resourceSafetyTitle: 'نشرات بيانات السلامة',
    resourceSafetyInfo: 'للاستفسار عن نشرات السلامة، تواصل مع فريقنا.',
    resourcePending: 'تواصل معنا',
  },
  en: {
    marketTag: 'NextGen Building Solutions · Algeria',
    homeStatus: 'Discover the FENEK ranges.',
    homeContact: 'Contact us',
    homeApproachTag: 'Our approach',
    mascotAlt: 'Nexo, NextGen mascot',
    rangesLead: 'Explore the four FENEK families and their application areas.',
    topicsHeading: 'Areas covered',
    rangeDisclaimer: 'Contact NextGen for technical specifications and availability.',
    rangeBack: 'All product ranges',
    rangeCatalogue: 'Browse references',
    rangeContact: 'Contact NextGen',
    rangeTopics: {
      bond: ['Mortars', 'Adhesives and grouts', 'Repair'],
      proof: ['Waterproofing', 'Protection', 'Resins'],
      flow: ['Concrete', 'Mortar', 'Admixtures'],
      paint: ['Paints', 'Coatings', 'Finishes'],
    },
    aboutHeading: 'Our manufacturing approach',
    aboutKicker: 'Construction solutions · Industrial vision',
    aboutLead: 'From product development to manufacturing and on to construction professionals: an approach shaped by real site needs.',
    aboutSteps: ['Design for the jobsite', 'Manufacture with purpose', 'Distribute and support'],
    aboutDetails: [
      'Understand project constraints and turn professional needs into solutions across mortars, resins, admixtures and coatings.',
      'Structure manufacturing, raw material selection and packaging, with checks defined and validated for each product reference.',
      'Plan product availability and support distributors and applicators with documentation reviewed before release.',
    ],
    aboutHighlights: [
      ['Site requirements', 'Product development', 'Fit-for-purpose solutions'],
      ['Manufacturing', 'Packaging', 'Quality checks', 'Traceability'],
      ['Professional network', 'Technical support', 'Field feedback'],
    ],
    aboutCta: 'Building solutions designed for production and practical use.',
    aboutNotice: 'Product-specific characteristics, checks and documents remain subject to the required approvals.',
    resourceHeading: 'Resources and documents',
    resourceLead: 'Explore FENEK product sheets and useful information for your projects.',
    resourceTechTitle: 'FENEK product sheets',
    resourceTechInfo: 'Descriptions, application areas and catalogue presentations for all 50 references.',
    resourceSafetyTitle: 'Safety data sheets',
    resourceSafetyInfo: 'For safety documentation, please contact our team.',
    resourcePending: 'Contact us',
  },
};
