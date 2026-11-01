import type { Lang, Range } from './site';

// Editorial taxonomy, NOT approved products, performance claims or laboratory results.
type RangeTopics = Record<Range, readonly [string, string, string]>;
type EditorialCopy = {
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
    rangesLead: 'تعرّف إلى مجموعات FENEK الأربع. تعرض الأقسام مجالات عامة قيد التحضير، وليست منتجات معتمدة للبيع.',
    topicsHeading: 'المجالات المعروضة',
    rangeDisclaimer: 'عرض توضيحي لمجموعة قيد التطوير: لم تتم الموافقة على أي مرجع منتج أو أداء تقني للنشر.',
    rangeBack: 'جميع المجموعات',
    rangeGallery: 'استعراض نماذج العبوات',
    rangeContact: 'الاتصال بنكست جن',
    rangeTopics: {
      bond: ['الملاط', 'المواد اللاصقة والحشو', 'الإصلاح'],
      proof: ['العزل', 'الحماية', 'الراتنجات'],
      flow: ['الخرسانة', 'الملاط', 'الإضافات'],
      paint: ['الدهانات', 'الطلاءات', 'التشطيبات'],
    },
    aboutHeading: 'منهجية عمل قيد الإعداد',
    aboutLead: 'يجري إعداد عرض NextGen. تصف الخطوات التالية منهجية مقترحة، وليست شهادة اعتماد أو خدمات معتمدة ومتاحة حالياً.',
    aboutSteps: ['فهم الاحتياجات', 'مراجعة مراجع المنتجات', 'توثيق المعلومات قبل نشرها'],
    aboutDetails: [
      'تحديد أصناف احتياجات الموزعين وشركات البناء والمشاريع.',
      'فحص البيانات التقنية مع المختصين قبل تقديم أي ادعاء تجاري.',
      'التحقق من الوثائق والموافقات اللازمة قبل نشر أي بطاقة منتج.',
    ],
    aboutNotice: 'لا يُعلن عن توفر المنتجات أو اعتماد نتائج المختبر أو الخدمات.',
    resourceHeading: 'الوثائق والموارد',
    resourceLead: 'يمكن الاطلاع على النماذج التوضيحية للعبوات. أما الوثائق التقنية ووثائق السلامة فتبقى قيد المراجعة والاعتماد.',
    resourceTechTitle: 'النشرات التقنية',
    resourceTechInfo: 'لن تُنشر قبل اعتماد الخصائص والقياسات ومجالات الاستعمال.',
    resourceSafetyTitle: 'نشرات بيانات السلامة',
    resourceSafetyInfo: 'لن تُنشر قبل استكمال المراجعة التنظيمية والوثائقية.',
    resource3dTitle: 'تصاميم ثلاثية الأبعاد للعبوات',
    resource3dInfo: 'خمسة نماذج توضيحية غير تعاقدية لأشكال عبوات مقترحة.',
    resourcePending: 'بانتظار الاعتماد',
    resourceDemo: 'محاكاة',
    resourceExplore: 'فتح معرض النماذج ثلاثية الأبعاد',
  },
  en: {
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
