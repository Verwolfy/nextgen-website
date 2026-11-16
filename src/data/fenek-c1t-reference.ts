import type { Lang } from './site';

/**
 * Publicly displayable CLASS requirements and FAMILY comparison benchmarks.
 * No figure in this file is a measured or certified FENEK performance.
 * Source-by-source provenance lives in docs/INTERNE-validation-donnees.csv.
 */
export type ReferenceMetric = {
  key: string;
  kind: 'norme' | 'famille';
  label: Record<Lang, string>;
  value: string;
};

export const c1tRequirements: ReferenceMetric[] = [
  {key:'adhesion-initiale',kind:'norme',label:{fr:'Adhérence initiale en traction',ar:'قوة الالتصاق الأولية بالشد',en:'Initial tensile adhesion'},value:'≥ 0,5 N/mm²'},
  {key:'adhesion-eau',kind:'norme',label:{fr:'Adhérence après immersion dans l’eau',ar:'الالتصاق بعد الغمر في الماء',en:'Tensile adhesion after water immersion'},value:'≥ 0,5 N/mm²'},
  {key:'adhesion-chaleur',kind:'norme',label:{fr:'Adhérence après vieillissement thermique',ar:'الالتصاق بعد التعتيق الحراري',en:'Tensile adhesion after heat ageing'},value:'≥ 0,5 N/mm²'},
  {key:'adhesion-gel',kind:'norme',label:{fr:'Adhérence après cycles gel/dégel',ar:'الالتصاق بعد دورات التجمد والذوبان',en:'Tensile adhesion after freeze-thaw cycles'},value:'≥ 0,5 N/mm²'},
  {key:'glissement',kind:'norme',label:{fr:'Glissement vertical (T)',ar:'الانزلاق الرأسي (T)',en:'Vertical slip (T)'},value:'≤ 0,5 mm'},
  {key:'temps-ouvert-essai',kind:'norme',label:{fr:'Essai de temps ouvert normal',ar:'اختبار الزمن المفتوح القياسي',en:'Normal open-time test'},value:'≥ 0,5 N/mm² après 20 min'},
];

export const c1tFamilyReferences: ReferenceMetric[] = [
  {key:'consommation-simple',kind:'famille',label:{fr:'Consommation de référence : simple encollage',ar:'استهلاك مرجعي: اللصق على السطح فقط',en:'Reference coverage: single-sided bedding'},value:'3–5 kg/m²'},
  {key:'consommation-double',kind:'famille',label:{fr:'Consommation de référence : double encollage',ar:'استهلاك مرجعي: اللصق المزدوج',en:'Reference coverage: back-buttering and substrate'},value:'5–8 kg/m²'},
  {key:'eau',kind:'famille',label:{fr:'Eau observée sur produits comparables (sac de 25 kg)',ar:'الماء في منتجات مقارنة (كيس 25 كغ)',en:'Water used by comparable products (25 kg bag)'},value:'5–6,5 L / 25 kg'},
  {key:'temperature',kind:'famille',label:{fr:'Température de chantier couramment recommandée',ar:'درجة حرارة التطبيق الشائعة لدى منتجات مماثلة',en:'Common recommended application temperature'},value:'+5 à +30 °C'},
  {key:'temps-ouvert-comparatif',kind:'famille',label:{fr:'Temps ouvert observé sur les produits comparables',ar:'الزمن المفتوح في المنتجات المقارنة',en:'Open time observed on comparable products'},value:'≈ 20 min'},
  {key:'ajustabilite-comparative',kind:'famille',label:{fr:'Délai d’ajustement observé (variable selon la formulation)',ar:'مدة تعديل موضع البلاط في المنتجات المقارنة',en:'Observed adjustment time (formulation-dependent)'},value:'≈ 20–45 min'},
];

export const c1tContent: Record<Lang, {
  pageTitle:string; metaDescription:string; sheetTitle:string; lead:string; nav:string[];
  uses:string[]; benefits:string[]; substrates:string[]; introTitle:string; techTitle:string; familyTitle:string; figuresNote:string;
  identityTitle:string; codeLabel:string; rangeLabel:string; designationLabel:string; packLabel:string; classLabel:string;
  applicationTitle:string; preparationTitle:string; preparation:string[]; conditionsTitle:string; conditions:string[];
  stepsTitle:string; consumptionTitle:string; safetyTitle:string; safety:string[];
  documentsTitle:string; exportLabel:string; downloadLabel:string; documentAction:string; quoteAction:string; whatsappAction:string; sourceNote:string;
  comparisonTitle:string; comparisonHeadings:string[]; comparisonNote:string; relatedTitle:string; important:string;
}> = {
  fr:{
    pageTitle:'FENEK-BOND C1T | Mortier-colle carrelage C1T',
    metaDescription:'FENEK-BOND C1T : mortier-colle cimentaire pour carrelage. Usages de la famille C1T, critères EN 12004-1, conseils de pose et demande de documentation.',
    sheetTitle:'Fiche produit – FENEK-BOND C1T',
    lead:'Mortier-colle cimentaire de désignation C1T. Repères techniques pour la pose courante de carrelage sur supports minéraux préparés.',
    nav:['Aperçu','Détails produits','Application','Documents'],
    uses:['Pose courante de carrelage et faïence sur murs et sols intérieurs, selon compatibilité du support.','Carreaux céramiques absorbants sur supports minéraux traditionnels.','Travaux neufs sur béton, chapes et enduits à base de ciment suffisamment secs et stables.'],
    benefits:['C : mortier-colle à base de ciment.','1 : niveau normal d’adhérence défini par la norme.','T : glissement vertical réduit dans l’essai normalisé.'],
    substrates:['Béton durci et propre.','Chape et enduit à base de ciment cohésifs.','Tout autre support : vérifier la compatibilité et le primaire adapté.'],
    introTitle:'Utilisations et supports de la famille C1T',techTitle:'Critères normatifs de la classe C1T',familyTitle:'Valeurs de référence de la famille',
    figuresNote:'Les critères normatifs sont des seuils de classification, pas des résultats d’essais FENEK. Les plages de famille proviennent de produits comparables ; elles ne constituent pas une prescription de gâchage ou d’emploi pour FENEK.',
    identityTitle:'Identification',codeLabel:'Code catalogue',rangeLabel:'Gamme',designationLabel:'Désignation',packLabel:'Présentation catalogue',classLabel:'Classe mentionnée dans la désignation',
    applicationTitle:'Application',preparationTitle:'Préparation du support',
    preparation:['Éliminer poussières, huiles, laitance et parties non adhérentes.','Vérifier cohésion, planéité et humidité du support avant pose.','Choisir une spatule crantée adaptée au carreau ; contrôler le transfert de colle.'],
    conditionsTitle:'Conditions d’intervention',
    conditions:['Préparer une quantité adaptée à la surface qui pourra être carrelée avant formation d’une peau.','Éviter les supports surchauffés, le gel, les courants d’air forts et le séchage accéléré.','Utiliser le dosage et les délais de la fiche technique FENEK applicable au lot réellement fourni.'],
    stepsTitle:'Parcours illustré en six étapes',consumptionTitle:'Consommation et eau de gâchage : références de marché',safetyTitle:'Environnement et sécurité',
    safety:['Porter des gants, des lunettes adaptées et une protection respiratoire contre les poussières lors du mélange.','Limiter l’émission de poussière ; se laver les mains après manipulation et éviter le contact avec les yeux.','Conserver les sacs au sec et éliminer les résidus selon les règles locales ; ne pas déverser de mortier dans les réseaux d’eau.'],
    documentsTitle:'Documents et contact',exportLabel:'Imprimer / enregistrer cette fiche en PDF',downloadLabel:'Télécharger la fiche produit (PDF)',documentAction:'Demander la fiche technique et la FDS',quoteAction:'Obtenir un devis',whatsappAction:'Poser une question via WhatsApp',
    sourceNote:'Fiche de présentation informative. La FT et la FDS propres à la formulation FENEK sont communiquées par l’équipe technique lorsqu’elles sont disponibles.',
    comparisonTitle:'Repères de la gamme BOND',comparisonHeadings:['Référence','Classe indiquée','Élément distinctif de la désignation'],comparisonNote:'Comparaison de désignations, sans comparaison de performances mesurées FENEK.',
    relatedTitle:'Produits complémentaires et références voisines',
    important:'Informations importantes : les valeurs présentées sont des exigences de classe ou des ordres de grandeur issus de produits comparables. Elles ne constituent pas les performances mesurées de FENEK-BOND C1T. La tenue de l’ouvrage dépend du support et des conditions de chantier ; consulter la FT applicable avant emploi.'
  },
  ar:{
    pageTitle:'FENEK-BOND C1T | ملاط لاصق للبلاط من فئة C1T',
    metaDescription:'FENEK-BOND C1T: ملاط لاصق إسمنتي للبلاط، مع شرح فئة C1T ومتطلبات EN 12004-1 وإرشادات تحضير السطح وطلب المستندات الفنية.',
    sheetTitle:'بطاقة المنتج – FENEK-BOND C1T',
    lead:'ملاط لاصق إسمنتي يحمل الرمز C1T في تسميته. معلومات مرجعية عن تركيب البلاط على الأسطح الإسمنتية المهيأة.',
    nav:['نظرة عامة','تفاصيل المنتج','التطبيق','الوثائق'],
    uses:['تركيب البلاط والسيراميك على الجدران والأرضيات الداخلية وفق ملاءمة السطح.','تركيب البلاط الخزفي الممتص للماء على الأسطح الإسمنتية التقليدية.','أعمال البناء الجديدة على الخرسانة والمونة الإسمنتية المتماسكة والجافة بالقدر الملائم.'],
    benefits:['C: لاصق يعتمد على الإسمنت.','1: مستوى الالتصاق العادي كما تحدده المواصفة.','T: انخفاض الانزلاق الرأسي وفق الاختبار المعياري.'],
    substrates:['خرسانة متصلبة ونظيفة.','طبقات تسوية ومحارة إسمنتية متماسكة.','للأسطح الأخرى، تُراجع الملاءمة ونوع البرايمر المطلوب.'],
    introTitle:'استخدامات فئة C1T والأسطح المناسبة',techTitle:'المتطلبات المعيارية لفئة C1T',familyTitle:'قيم مرجعية لفئة المنتج',
    figuresNote:'المتطلبات المعيارية حدود تصنيف وليست نتائج اختبارات لمنتج FENEK. أما مجالات القيم فهي مستخلصة من منتجات مقارنة ولا تُعد تعليمات لخلط منتج FENEK أو تطبيقه.',
    identityTitle:'بيانات التعريف',codeLabel:'رمز الكتالوج',rangeLabel:'المجموعة',designationLabel:'التسمية',packLabel:'العبوة في الكتالوج',classLabel:'الفئة الواردة في التسمية',
    applicationTitle:'التطبيق',preparationTitle:'تحضير السطح',
    preparation:['إزالة الغبار والزيوت والطبقات الضعيفة وبقايا المواد التي تمنع الالتصاق.','فحص تماسك السطح واستوائه ورطوبته قبل التركيب.','اختيار مالج مسنن يلائم أبعاد البلاط، والتحقق من توزيع اللاصق خلفه.'],
    conditionsTitle:'ظروف التنفيذ',conditions:['تحضير كمية تلائم المساحة التي يمكن تبليطها قبل تشكّل قشرة على اللاصق.','تجنب الأسطح شديدة السخونة والصقيع والتيارات الهوائية القوية والجفاف السريع.','اعتماد نسبة الخلط ومدد العمل الواردة في النشرة الفنية الخاصة بتشغيلة FENEK المستخدمة.'],
    stepsTitle:'ست مراحل تطبيق مصورة',consumptionTitle:'الاستهلاك وماء الخلط: مؤشرات من منتجات مماثلة',safetyTitle:'البيئة والسلامة',
    safety:['ارتداء قفازات ونظارات واقية ووسيلة مناسبة للوقاية من غبار المساحيق أثناء الخلط.','تقليل انتشار الغبار وغسل اليدين بعد العمل وتجنب ملامسة العينين.','حفظ الأكياس في مكان جاف والتخلص من المخلفات وفق القواعد المحلية، وعدم سكب الملاط في شبكات الصرف.'],
    documentsTitle:'الوثائق والتواصل',exportLabel:'طباعة هذه البطاقة أو حفظها بصيغة PDF',downloadLabel:'تنزيل بطاقة المنتج (PDF)',documentAction:'طلب النشرة الفنية وصحيفة بيانات السلامة',quoteAction:'طلب عرض سعر',whatsappAction:'استفسار عبر واتساب',
    sourceNote:'بطاقة تعريفية. يقدم الفريق الفني النشرة الفنية وصحيفة بيانات السلامة الخاصة بتركيبة FENEK عند توفرهما.',
    comparisonTitle:'مقارنة تسميات مجموعة BOND',comparisonHeadings:['المرجع','الفئة في التسمية','الخاصية التي يبينها الرمز'],comparisonNote:'هذه مقارنة بين رموز التصنيف وليست مقارنة لنتائج أداء منتجات FENEK.',
    relatedTitle:'مراجع قريبة ومنتجات مكملة',
    important:'معلومات مهمة: الأرقام المعروضة هي حدود معيارية للفئة أو قيم تقريبية لمنتجات مماثلة، وليست نتائج اختبارات مقاسة لمنتج FENEK-BOND C1T. يتأثر أداء التنفيذ بحالة السطح وظروف الورشة؛ يجب الرجوع إلى النشرة الفنية الخاصة بالمنتج قبل الاستخدام.'
  },
  en:{
    pageTitle:'FENEK-BOND C1T | C1T Cementitious Tile Adhesive',
    metaDescription:'FENEK-BOND C1T cementitious tile adhesive: C1T family applications, EN 12004-1 class requirements, installation guidance and technical document requests.',
    sheetTitle:'Product information – FENEK-BOND C1T',
    lead:'Cementitious tile adhesive designated C1T. Practical family-level guidance for conventional tiling on properly prepared mineral substrates.',
    nav:['Overview','Product details','Application','Documents'],
    uses:['Conventional fixing of ceramic wall and floor tiles indoors where substrate compatibility is established.','Absorbent ceramic tiles on traditional cement-based backgrounds.','New work on sufficiently cured and stable concrete, cement screeds and renders.'],
    benefits:['C: cement-based adhesive.','1: normal tensile adhesion class defined by the standard.','T: reduced vertical slip in the standardized test.'],
    substrates:['Clean, sufficiently cured concrete.','Sound cement screeds and renders.','Other backgrounds require a substrate-specific compatibility and primer assessment.'],
    introTitle:'Typical C1T applications and substrates',techTitle:'C1T class requirements',familyTitle:'Family reference values',
    figuresNote:'Normative limits are classification thresholds, not FENEK test results. Family ranges are derived from comparable products and are not FENEK mixing or installation instructions.',
    identityTitle:'Product identification',codeLabel:'Catalogue code',rangeLabel:'Range',designationLabel:'Designation',packLabel:'Catalogue presentation',classLabel:'Class shown in designation',
    applicationTitle:'Application',preparationTitle:'Substrate preparation',
    preparation:['Remove dust, oil, laitance and all loose or poorly bonded layers.','Check substrate soundness, flatness and moisture before laying.','Select a notched trowel for the tile format and check adhesive transfer.'],
    conditionsTitle:'Working conditions',
    conditions:['Mix only the quantity that can be installed before the adhesive skins over.','Avoid overheated backgrounds, freezing conditions, strong draughts and accelerated drying.','Follow the mixing ratio and working times in the FENEK technical sheet for the actual supplied batch.'],
    stepsTitle:'Six illustrated application stages',consumptionTitle:'Consumption and mixing water: market references',safetyTitle:'Environment and safety',
    safety:['Use gloves, protective eyewear and suitable dust respiratory protection when handling dry powder.','Minimize dust generation, wash hands after use and avoid eye contact.','Keep bags dry and dispose of residues according to local rules; do not discharge mortar to drains.'],
    documentsTitle:'Documents and contacts',exportLabel:'Print / save this sheet as PDF',downloadLabel:'Download product sheet (PDF)',documentAction:'Request the technical and safety data sheets',quoteAction:'Request a quote',whatsappAction:'Ask via WhatsApp',
    sourceNote:'Informative product sheet. Product-specific FENEK technical and safety data sheets can be requested from the technical team when available.',
    comparisonTitle:'BOND range designation comparison',comparisonHeadings:['Reference','Class in name','Meaning of code'],comparisonNote:'Designation comparison only; no comparison of measured FENEK performance.',
    relatedTitle:'Related references and complementary products',
    important:'Important information: figures are class requirements or indicative values from comparable products, not measured FENEK-BOND C1T performance. Final results depend on the substrate and site conditions; consult the applicable FENEK technical data sheet before use.'
  }
};

export const c1tComparativeCodes: Record<'BOND-C1T'|'BOND-C1TE'|'BOND-C2TE', Record<Lang,string>> = {
  'BOND-C1T':{fr:'C1 : adhérence normale ; T : glissement réduit',ar:'C1: التصاق عادي؛ T: انزلاق رأسي منخفض',en:'C1: normal adhesion; T: reduced slip'},
  'BOND-C1TE':{fr:'E : essai de temps ouvert prolongé',ar:'E: زمن مفتوح ممتد في الاختبار',en:'E: extended open-time test'},
  'BOND-C2TE':{fr:'C2 : seuils d’adhérence renforcés ; E et T',ar:'C2: حدود التصاق أعلى؛ E وT',en:'C2: higher adhesion thresholds; E and T'}
};
