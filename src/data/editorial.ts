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
  aboutLead: string;
  aboutSteps: readonly [string, string, string];
  aboutDetails: readonly [string, string, string];
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
    aboutHeading: 'Notre démarche',
    aboutLead: 'Découvrez notre approche des besoins de construction et de la documentation technique.',
    aboutSteps: ['Écouter les besoins', 'Qualifier les références', 'Documenter avant publication'],
    aboutDetails: [
      'Identifier les catégories de besoins des distributeurs, entreprises et chantiers.',
      'Examiner les données techniques avec les équipes compétentes avant toute affirmation commerciale.',
      'Vérifier les documents et autorisations nécessaires avant de publier une fiche.',
    ],
    aboutNotice: 'Contactez notre équipe pour les informations techniques et commerciales.',
    resourceHeading: 'Ressources et documents',
    resourceLead: 'Pour toute demande de fiche technique ou de données de sécurité, contactez notre équipe.',
    resourceTechTitle: 'Fiches techniques',
    resourceTechInfo: 'Renseignements et documents techniques disponibles auprès de notre équipe.',
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
    aboutHeading: 'منهجية عملنا',
    aboutLead: 'تعرّف على منهجيتنا في فهم احتياجات قطاع البناء وتوثيق المعلومات الفنية.',
    aboutSteps: ['فهم احتياجات المشاريع', 'مراجعة بيانات المنتجات', 'توثيق المعلومات قبل النشر'],
    aboutDetails: [
      'دراسة احتياجات الموزعين وشركات المقاولات والمشاريع الإنشائية.',
      'مراجعة البيانات الفنية مع المختصين قبل اعتماد أي وصف تجاري.',
      'التحقق من المستندات والموافقات المطلوبة قبل نشر بطاقات المنتجات.',
    ],
    aboutNotice: 'للحصول على المعلومات الفنية والتجارية، تواصل مع فريقنا.',
    resourceHeading: 'الموارد والوثائق الفنية',
    resourceLead: 'للاستفسار عن النشرات الفنية وبيانات السلامة، تواصل مع فريقنا.',
    resourceTechTitle: 'النشرات الفنية للمنتجات',
    resourceTechInfo: 'الوثائق الفنية والمعلومات متاحة عبر فريقنا.',
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
    aboutHeading: 'Our approach',
    aboutLead: 'Learn how NextGen approaches building needs and technical documentation.',
    aboutSteps: ['Understand requirements', 'Review product references', 'Document before publishing'],
    aboutDetails: [
      'Identify the broad needs of distributors, contractors and construction projects.',
      'Have qualified teams review technical inputs before making commercial claims.',
      'Check documentation and required approvals before publishing a product page.',
    ],
    aboutNotice: 'Contact our team for technical and commercial information.',
    resourceHeading: 'Resources and documents',
    resourceLead: 'Contact our team for technical documentation and safety data sheet enquiries.',
    resourceTechTitle: 'Technical datasheets',
    resourceTechInfo: 'Contact our team for technical documentation and details.',
    resourceSafetyTitle: 'Safety data sheets',
    resourceSafetyInfo: 'For safety documentation, please contact our team.',
    resourcePending: 'Contact us',
  },
};
