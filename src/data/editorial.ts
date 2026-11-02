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
  rangeGallery: string;
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
  resource3dTitle: string;
  resource3dInfo: string;
  resourcePending: string;
  resourceDemo: string;
  resourceExplore: string;
};
export const editorialCopy: Record<Lang, EditorialCopy> = {
  fr: {
    marketTag: 'NextGen Building Solutions · Algeria / Algérie',
    homeStatus: 'Site en préparation : aucun produit réel approuvé pour publication.',
    homeContact: 'Nous contacter',
    homeApproachTag: 'Démarche en préparation',
    mascotAlt: 'Nexo, mascotte NextGen',
    rangesLead: 'Parcourez les quatre familles FENEK. Les rubriques ci-dessous présentent des domaines de travail, pas des références commercialisées.',
    topicsHeading: 'Domaines présentés',
    rangeDisclaimer: 'Présentation indicative de la gamme en préparation : aucun SKU ni performance produit n’est validé pour publication.',
    rangeBack: 'Toutes les gammes',
    rangeGallery: 'Voir les maquettes d’emballages',
    rangeContact: 'Contacter NextGen',
    rangeTopics: {
      bond: ['Mortiers', 'Colles et joints', 'Réparation'],
      proof: ['Étanchéité', 'Protection', 'Résines'],
      flow: ['Béton', 'Mortier', 'Adjuvants'],
      paint: ['Peintures', 'Revêtements', 'Finitions'],
    },
    aboutHeading: 'Notre démarche en préparation',
    aboutLead: 'L’offre NextGen est en structuration. Les étapes ci-dessous décrivent une méthode de travail envisagée, et non une certification ou un service déjà homologué.',
    aboutSteps: ['Écouter les besoins', 'Qualifier les références', 'Documenter avant publication'],
    aboutDetails: [
      'Identifier les catégories de besoins des distributeurs, entreprises et chantiers.',
      'Examiner les données techniques avec les équipes compétentes avant toute affirmation commerciale.',
      'Vérifier les documents et autorisations nécessaires avant de publier une fiche.',
    ],
    aboutNotice: 'Les produits, validations de laboratoire et prestations ne sont pas annoncés comme disponibles ou certifiés.',
    resourceHeading: 'Ressources et documents',
    resourceLead: 'Accédez aux maquettes illustratives déjà visibles. Les documents techniques et de sécurité restent réservés à un circuit de validation.',
    resourceTechTitle: 'Fiches techniques',
    resourceTechInfo: 'Publication suspendue à la validation des caractéristiques, mesures et usages.',
    resourceSafetyTitle: 'Fiches de données de sécurité',
    resourceSafetyInfo: 'Documents non diffusés tant que la revue réglementaire et documentaire n’est pas achevée.',
    resource3dTitle: 'Concepts d’emballages 3D',
    resource3dInfo: 'Cinq maquettes non contractuelles, accessibles pour visualiser des formats indicatifs.',
    resourcePending: 'En attente de validation',
    resourceDemo: 'Simulation',
    resourceExplore: 'Ouvrir la galerie 3D',
  },
  ar: {
    marketTag: 'NextGen Building Solutions · الجزائر',
    homeStatus: 'الموقع قيد الإعداد. لم تُعتمد بعد أي منتجات للنشر أو البيع.',
    homeContact: 'تواصل معنا',
    homeApproachTag: 'منهجية قيد الإعداد',
    mascotAlt: 'نيكسو، شخصية نكست جن التوضيحية',
    rangesLead: 'استكشف مجموعات FENEK الأربع المقترحة ومجالاتها العامة. لا تمثل هذه التصنيفات منتجات معتمدة أو معروضة للبيع.',
    topicsHeading: 'مجالات الاستخدام',
    rangeDisclaimer: 'هذه معلومات تعريفية أولية؛ لم تُعتمد بعد أي مراجع منتجات أو بيانات أداء للنشر.',
    rangeBack: 'العودة إلى الفئات',
    rangeGallery: 'مشاهدة نماذج العبوات',
    rangeContact: 'تواصل مع نكست جن',
    rangeTopics: {
      bond: ['الملاط', 'لواصق البلاط وملء الفواصل', 'مواد الإصلاح'],
      proof: ['العزل المائي', 'الحماية السطحية', 'الراتنجات'],
      flow: ['الخرسانة', 'الملاط', 'الإضافات'],
      paint: ['الدهانات', 'الطلاءات', 'التشطيبات'],
    },
    aboutHeading: 'كيف نُعدّ فئات المنتجات',
    aboutLead: 'نعرض هنا خطوات العمل المقترحة. ولا تعني هذه المراحل توفر خدمات معتمدة أو حصول أي منتج على شهادة مطابقة.',
    aboutSteps: ['فهم احتياجات المشاريع', 'مراجعة بيانات المنتجات', 'توثيق المعلومات قبل النشر'],
    aboutDetails: [
      'دراسة احتياجات الموزعين وشركات المقاولات والمشاريع الإنشائية.',
      'مراجعة البيانات الفنية مع المختصين قبل اعتماد أي وصف تجاري.',
      'التحقق من المستندات والموافقات المطلوبة قبل نشر بطاقات المنتجات.',
    ],
    aboutNotice: 'لا يُعلن عن توفر المنتجات أو الخدمات، ولا عن اعتماد نتائج الاختبارات المخبرية.',
    resourceHeading: 'الموارد والوثائق الفنية',
    resourceLead: 'يمكن معاينة تصاميم العبوات التوضيحية، أما البيانات الفنية ونشرات السلامة فلا تزال قيد المراجعة والاعتماد.',
    resourceTechTitle: 'النشرات الفنية للمنتجات',
    resourceTechInfo: 'لن تُنشر البيانات قبل التحقق من الخصائص الفنية ونتائج القياس ومجالات الاستخدام.',
    resourceSafetyTitle: 'نشرات بيانات السلامة',
    resourceSafetyInfo: 'لن تُنشر قبل استكمال المراجعة الفنية والتنظيمية اللازمة.',
    resource3dTitle: 'نماذج العبوات ثلاثية الأبعاد',
    resource3dInfo: 'خمسة تصاميم توضيحية غير معتمدة تُظهر أشكالًا مقترحة للعبوات.',
    resourcePending: 'قيد المراجعة',
    resourceDemo: 'تصميم توضيحي',
    resourceExplore: 'استعرض نماذج العبوات ثلاثية الأبعاد',
  },
  en: {
    marketTag: 'NextGen Building Solutions · Algeria',
    homeStatus: 'Website in preparation: no verified product is approved for publication.',
    homeContact: 'Contact us',
    homeApproachTag: 'Approach in development',
    mascotAlt: 'Nexo, NextGen mascot',
    rangesLead: 'Explore the four FENEK families. These are editorial categories, not approved commercial products.',
    topicsHeading: 'Areas covered',
    rangeDisclaimer: 'Illustrative range in development: no product SKU or performance claim has been cleared for publication.',
    rangeBack: 'All product ranges',
    rangeGallery: 'See packaging concepts',
    rangeContact: 'Contact NextGen',
    rangeTopics: {
      bond: ['Mortars', 'Adhesives and grouts', 'Repair'],
      proof: ['Waterproofing', 'Protection', 'Resins'],
      flow: ['Concrete', 'Mortar', 'Admixtures'],
      paint: ['Paints', 'Coatings', 'Finishes'],
    },
    aboutHeading: 'Our proposed approach',
    aboutLead: 'NextGen’s offer is being developed. The following is an intended workflow, not a certification or a claim that services are already validated.',
    aboutSteps: ['Understand requirements', 'Review product references', 'Document before publishing'],
    aboutDetails: [
      'Identify the broad needs of distributors, contractors and construction projects.',
      'Have qualified teams review technical inputs before making commercial claims.',
      'Check documentation and required approvals before publishing a product page.',
    ],
    aboutNotice: 'Products, laboratory validations and services are not represented as available or certified.',
    resourceHeading: 'Resources and documents',
    resourceLead: 'Explore the illustrative designs that are already available. Technical and safety documents remain subject to review.',
    resourceTechTitle: 'Technical datasheets',
    resourceTechInfo: 'Publication is pending the review of characteristics, measurements and intended uses.',
    resourceSafetyTitle: 'Safety data sheets',
    resourceSafetyInfo: 'Documents are withheld pending regulatory and documentary review.',
    resource3dTitle: '3D packaging concepts',
    resource3dInfo: 'Five non-contractual models illustrating possible packaging formats.',
    resourcePending: 'Awaiting approval',
    resourceDemo: 'Simulation',
    resourceExplore: 'Open the 3D gallery',
  },
};
