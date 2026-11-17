import type {Lang} from './site';
import type {ReferenceMetric} from './fenek-c1t-reference';

/**
 * EN 12004-1 class thresholds and independent C1TE-family comparisons.
 * NOT tested or certified FENEK performance; references and individual
 * manufacturer measurements: docs/INTERNE-validation-donnees.csv.
 */
export const c1teRequirements:ReferenceMetric[]=[
  {key:'adhesion-initiale',kind:'norme',label:{fr:'Adhérence initiale en traction',ar:'قوة الالتصاق الأولية بالشد',en:'Initial tensile adhesion'},value:'≥ 0,5 N/mm²'},
  {key:'adhesion-eau',kind:'norme',label:{fr:'Adhérence après immersion dans l’eau',ar:'الالتصاق بعد الغمر في الماء',en:'Tensile adhesion after water immersion'},value:'≥ 0,5 N/mm²'},
  {key:'adhesion-chaleur',kind:'norme',label:{fr:'Adhérence après vieillissement thermique',ar:'الالتصاق بعد التعتيق الحراري',en:'Tensile adhesion after heat ageing'},value:'≥ 0,5 N/mm²'},
  {key:'adhesion-gel',kind:'norme',label:{fr:'Adhérence après cycles gel/dégel',ar:'الالتصاق بعد دورات التجمد والذوبان',en:'Tensile adhesion after freeze-thaw cycles'},value:'≥ 0,5 N/mm²'},
  {key:'glissement',kind:'norme',label:{fr:'Glissement vertical (T)',ar:'الانزلاق الرأسي (T)',en:'Vertical slip (T)'},value:'≤ 0,5 mm'},
  {key:'temps-ouvert-normal',kind:'norme',label:{fr:'Adhérence après temps ouvert normal',ar:'الالتصاق بعد الزمن المفتوح العادي',en:'Adhesion after normal open-time test'},value:'≥ 0,5 N/mm² après 20 min'},
  {key:'temps-ouvert-e',kind:'norme',label:{fr:'Adhérence après temps ouvert prolongé (E)',ar:'الالتصاق بعد الزمن المفتوح الممتد (E)',en:'Adhesion after extended open-time test (E)'},value:'≥ 0,5 N/mm² après 30 min'},
];

export const c1teFamilyReferences:ReferenceMetric[]=[
  {key:'consommation-simple',kind:'famille',label:{fr:'Consommation comparative : lit simple selon peigne',ar:'استهلاك مقارن: طبقة لصق واحدة بحسب المشط',en:'Comparable consumption: single bedding, by notch'},value:'≈ 3–5,5 kg/m²'},
  {key:'consommation-double',kind:'famille',label:{fr:'Consommation comparative : avec double encollage',ar:'استهلاك مقارن: مع دهن ظهر البلاط',en:'Comparable consumption: with back-buttering'},value:'≈ 4–7,2 kg/m²'},
  {key:'eau',kind:'famille',label:{fr:'Eau de gâchage des équivalents (ramenée à 25 kg)',ar:'ماء الخلط في المنتجات المماثلة (مكافئ 25 كغ)',en:'Comparable mixing water (normalized to 25 kg)'},value:'5–7,5 L / 25 kg'},
  {key:'ajustabilite',kind:'famille',label:{fr:'Délai d’ajustement observé sur deux équivalents',ar:'مدة تعديل موضع البلاط في منتجين مماثلين',en:'Observed adjustment time for two comparables'},value:'≈ 10–25 min'},
  {key:'temps-ouvert-comparatif',kind:'famille',label:{fr:'Temps ouvert annoncé sur des produits C1TE comparables',ar:'الزمن المفتوح المعلن لمنتجات C1TE المماثلة',en:'Declared open time for comparable C1TE adhesives'},value:'≈ 30 min ou plus'},
];

type Copy={
  pageTitle:string;metaDescription:string;sheetTitle:string;lead:string;nav:string[];
  uses:string[];benefits:string[];substrates:string[];
  usesTitle:string;substratesTitle:string;identityTitle:string;
  designationLabel:string;referenceLabel:string;rangeLabel:string;formatLabel:string;classLabel:string;
  techTitle:string;familyTitle:string;fieldTitle:string;metricTitle:string;figuresNote:string;
  applicationTitle:string;prepTitle:string;preparation:string[];conditionsTitle:string;conditions:string[];
  consumptionTitle:string;stepsTitle:string;safetyTitle:string;safety:string[];
  documentsTitle:string;downloadLabel:string;printLabel:string;requestLabel:string;quoteLabel:string;whatsappLabel:string;
  relatedTitle:string;comparisonTitle:string;comparisonNote:string;linkLabel:string;important:string;
};
export const c1teCopy:Record<Lang,Copy>={
  fr:{
    pageTitle:'FENEK-BOND C1TE | Colle carrelage cimentaire C1TE',
    metaDescription:'FENEK-BOND C1TE : repères EN 12004-1 pour colle cimentaire à glissement réduit et temps ouvert prolongé. Supports, application, consommations de famille et documentation.',
    sheetTitle:'Fiche produit — FENEK-BOND C1TE',
    lead:'Mortier-colle cimentaire de désignation C1TE pour la pose de carreaux sur supports minéraux préparés. Le code T désigne un glissement réduit et E un essai de temps ouvert prolongé.',
    nav:['Aperçu','Détails produits','Application','Documents'],
    uses:['Collage courant des carreaux céramiques sur murs et sols intérieurs.','Pose de faïence et de carreaux céramiques sur béton, chapes et enduits ciment cohésifs.','Sélection des supports, formats et conditions de pose en fonction de la fiche technique du produit fourni.'],
    benefits:['C1 : seuils d’adhérence normale de la norme EN 12004-1.','T : résistance au glissement vertical selon l’essai de classement.','E : maintien de l’adhérence dans l’essai de temps ouvert à 30 minutes.'],
    substrates:['Béton suffisamment durci, propre et stable.','Chapes et enduits à base de ciment avec cohésion et planéité vérifiées.','Supports sensibles à l’humidité, anciens revêtements et grands formats : système de collage à spécifier séparément.'],
    usesTitle:'Domaines d’utilisation de la famille',substratesTitle:'Supports courants',identityTitle:'Identification',
    designationLabel:'Désignation',referenceLabel:'Code catalogue',rangeLabel:'Gamme',formatLabel:'Présentation catalogue',classLabel:'Classe figurant dans la désignation',
    techTitle:'Exigences normatives de la classe C1TE',familyTitle:'Références chiffrées issues de produits comparables',fieldTitle:'Propriété',metricTitle:'Seuil ou valeur',
    figuresNote:'Les seuils normatifs décrivent la classe et non des mesures FENEK. Les chiffres de la famille comparent d’autres formulations : ils ne définissent pas le dosage, le temps de pose ou le rendement de FENEK-BOND C1TE.',
    applicationTitle:'Application',prepTitle:'Préparation du support',
    preparation:['Contrôler la stabilité, la propreté, la planéité et l’humidité du support.','Enlever poussières, huiles, laitance et toutes les zones non adhérentes.','Adapter le peigne au carreau ; vérifier le transfert de colle par soulèvement ponctuel.'],
    conditionsTitle:'Conditions de pose',conditions:['Éviter pluie, gel, supports surchauffés, courants d’air et séchage trop rapide.','N’étaler que la quantité d’adhésif pouvant être recouverte avant l’apparition d’une peau.','Le temps ouvert prolongé est une classification de laboratoire ; respecter les durées confirmées dans la FT du produit utilisé.'],
    consumptionTitle:'Consommation et eau de gâchage — comparaison de famille',stepsTitle:'Six étapes illustrées',safetyTitle:'Environnement et sécurité',
    safety:['Porter des gants, des lunettes adaptées et une protection respiratoire contre les poussières lors de la manipulation du mortier sec.','Limiter les poussières de mélange, éviter les projections dans les yeux et se laver les mains après usage.','Conserver les sacs à l’abri de l’humidité et éliminer les déchets selon la réglementation locale, sans rejeter de mortier dans les canalisations.'],
    documentsTitle:'Documents et demande de devis',downloadLabel:'Télécharger la fiche produit (PDF)',printLabel:'Imprimer / enregistrer en PDF',requestLabel:'Demander la fiche technique et la FDS',quoteLabel:'Obtenir un devis',whatsappLabel:'Contacter via WhatsApp',
    relatedTitle:'Produits associés',comparisonTitle:'Comparer les désignations de la gamme BOND',comparisonNote:'Comparaison de classes figurant dans les noms, et non de performances FENEK attestées.',linkLabel:'Voir la fiche',
    important:'Informations importantes : les valeurs sont des exigences de classement ou des références de famille, non des résultats mesurés pour FENEK-BOND C1TE. Les performances finales dépendent du support et des conditions de chantier. Consulter la fiche technique applicable avant emploi.'
  },
  ar:{
    pageTitle:'FENEK-BOND C1TE | لاصق بلاط إسمنتي بفئة C1TE',
    metaDescription:'بطاقة FENEK-BOND C1TE: متطلبات EN 12004-1 لفئة C1TE، إرشادات تجهيز السطح والتركيب، وقيم مقارنة للاستهلاك وطلب النشرة الفنية.',
    sheetTitle:'بطاقة المنتج — FENEK-BOND C1TE',
    lead:'ملاط لاصق إسمنتي يحمل الرمز C1TE في تسميته، للاسترشاد به في تركيب البلاط على الأسطح المعدنية المهيأة. يشير T إلى انخفاض الانزلاق وE إلى اختبار زمن مفتوح ممتد.',
    nav:['نظرة عامة','تفاصيل المنتج','التطبيق','الوثائق'],
    uses:['تركيب بلاط السيراميك على الجدران والأرضيات الداخلية.','تركيب القيشاني والبلاط الخزفي على الخرسانة وطبقات التسوية والمحارة الإسمنتية المتماسكة.','اختيار نوع السطح ومقاس البلاط وظروف التركيب وفق النشرة الفنية الخاصة بالمنتج المورّد.'],
    benefits:['C1: حدود الالتصاق العادي وفق المواصفة EN 12004-1.','T: الحد من الانزلاق الرأسي في اختبار التصنيف.','E: الحفاظ على قوة الالتصاق في اختبار الزمن المفتوح بعد 30 دقيقة.'],
    substrates:['خرسانة ناضجة ونظيفة وثابتة.','طبقات تسوية ومحارة إسمنتية بعد فحص تماسكها واستوائها.','الأسطح الحساسة للرطوبة والكسوات القديمة والمقاسات الكبيرة تحتاج إلى تحديد نظام لصق مناسب بصورة مستقلة.'],
    usesTitle:'مجالات الاستخدام المعتادة للفئة',substratesTitle:'الأسطح الشائعة',identityTitle:'بيانات المنتج',
    designationLabel:'التسمية',referenceLabel:'رمز الكتالوج',rangeLabel:'المجموعة',formatLabel:'العبوة في الكتالوج',classLabel:'الفئة المذكورة في التسمية',
    techTitle:'المتطلبات المعيارية لفئة C1TE',familyTitle:'قيم مرجعية مستخلصة من منتجات مماثلة',fieldTitle:'الخاصية',metricTitle:'الحد أو القيمة',
    figuresNote:'هذه حدود تصنيف معيارية وليست نتائج اختبارات لمنتج FENEK. أما قيم الفئة فهي مقارنة بين تركيبات أخرى ولا تحدد ماء الخلط أو مدة العمل أو استهلاك FENEK-BOND C1TE.',
    applicationTitle:'التطبيق',prepTitle:'تحضير السطح',
    preparation:['فحص ثبات السطح ونظافته واستوائه ونسبة رطوبته.','إزالة الغبار والزيوت وطبقة الإسمنت الضعيفة والمواد غير المتماسكة.','اختيار المالج المسنن حسب مقاس البلاط وفحص تغطية ظهر البلاطة برفع عينة أثناء التركيب.'],
    conditionsTitle:'شروط التركيب',conditions:['تجنب المطر والصقيع والأسطح شديدة السخونة والتيارات الهوائية والجفاف السريع.','فرد كمية من اللاصق يمكن تغطيتها بالبلاط قبل تشكّل قشرة على السطح.','الزمن المفتوح الممتد خاصية تصنيف مختبرية؛ تُتبع المدد الواردة في النشرة الفنية للمنتج المستعمل.'],
    consumptionTitle:'الاستهلاك وماء الخلط — قيم مقارنة للفئة',stepsTitle:'ست مراحل تطبيق مصورة',safetyTitle:'البيئة والسلامة',
    safety:['ارتداء قفازات ونظارات واقية ووسيلة مناسبة للوقاية من غبار المسحوق أثناء التعامل مع الملاط الجاف.','الحد من الغبار أثناء الخلط وتجنب وصوله إلى العينين وغسل اليدين بعد الانتهاء.','حفظ الأكياس بعيدًا عن الرطوبة والتخلص من المخلفات وفق الأنظمة المحلية دون صب الملاط في شبكة الصرف.'],
    documentsTitle:'الوثائق وطلب عرض السعر',downloadLabel:'تنزيل بطاقة المنتج (PDF)',printLabel:'طباعة البطاقة أو حفظها PDF',requestLabel:'طلب النشرة الفنية وصحيفة بيانات السلامة',quoteLabel:'طلب عرض سعر',whatsappLabel:'التواصل عبر واتساب',
    relatedTitle:'منتجات مرتبطة',comparisonTitle:'مقارنة رموز مجموعة BOND',comparisonNote:'هذه مقارنة لرموز الفئات المذكورة في الأسماء وليست مقارنة لأداء منتجات FENEK المقاس.',linkLabel:'عرض البطاقة',
    important:'معلومات مهمة: القيم المعروضة حدود تصنيف أو مؤشرات لفئة المنتج وليست نتائج قياس خاصة بـ FENEK-BOND C1TE. تعتمد النتيجة النهائية على حالة السطح وظروف الورشة. يجب الرجوع إلى النشرة الفنية الخاصة بالمنتج قبل الاستخدام.'
  },
  en:{
    pageTitle:'FENEK-BOND C1TE | C1TE Cementitious Tile Adhesive',
    metaDescription:'FENEK-BOND C1TE: EN 12004-1 C1TE classification criteria, substrate preparation, tile fixing guidance, comparable-family consumption and technical document requests.',
    sheetTitle:'Product sheet — FENEK-BOND C1TE',
    lead:'Cementitious tile adhesive designated C1TE for fixing tiles to prepared mineral substrates. T indicates reduced slip; E identifies an extended open-time classification test.',
    nav:['Overview','Product details','Application','Documents'],
    uses:['Conventional fixing of ceramic wall and floor tiles indoors.','Wall and floor tiling on sound concrete, cement screeds and cement renders.','Select tile formats, compatible substrates and working conditions according to the supplied product technical sheet.'],
    benefits:['C1: normal adhesion class thresholds in EN 12004-1.','T: reduced vertical slip under the classification test.','E: adhesion retained in the extended open-time test at 30 minutes.'],
    substrates:['Clean, stable, properly cured concrete.','Sound cementitious screeds and renders with checked flatness.','Moisture-sensitive substrates, existing finishes and large-format tiles require separate system assessment.'],
    usesTitle:'Typical applications within the class',substratesTitle:'Common substrates',identityTitle:'Product identification',
    designationLabel:'Designation',referenceLabel:'Catalogue code',rangeLabel:'Range',formatLabel:'Catalogue presentation',classLabel:'Class appearing in the name',
    techTitle:'EN 12004-1 C1TE classification requirements',familyTitle:'Numerical benchmarks from comparable products',fieldTitle:'Property',metricTitle:'Threshold or figure',
    figuresNote:'Normative limits are class criteria, not FENEK test results. Family figures compare other formulations and do not prescribe water dosage, working time or coverage for FENEK-BOND C1TE.',
    applicationTitle:'Application',prepTitle:'Substrate preparation',
    preparation:['Check substrate stability, cleanliness, flatness and moisture.','Remove dust, oil, laitance and any poorly bonded material.','Select an appropriate notched trowel and lift a sample tile to verify adhesive transfer.'],
    conditionsTitle:'Laying conditions',conditions:['Avoid rain, frost, overheated backgrounds, draughts and rapid drying.','Spread only the area that can be tiled before a surface skin forms.','Extended open time is a laboratory classification: follow the working times stated in the actual FENEK technical sheet.'],
    consumptionTitle:'Coverage and mixing water — family comparisons',stepsTitle:'Six illustrated installation stages',safetyTitle:'Environment and safety',
    safety:['Wear gloves, suitable eye protection and respiratory protection against dust when handling the dry mortar.','Reduce mixing dust, prevent eye contact and wash hands after handling.','Keep bags dry and dispose of residues in accordance with local requirements; never discharge mortar into drains.'],
    documentsTitle:'Documents and quotations',downloadLabel:'Download product sheet (PDF)',printLabel:'Print / save as PDF',requestLabel:'Request technical and safety data sheets',quoteLabel:'Request a quote',whatsappLabel:'Contact via WhatsApp',
    relatedTitle:'Related products',comparisonTitle:'BOND range designation comparison',comparisonNote:'Comparison of classes stated in product names, not verified FENEK performance.',linkLabel:'View sheet',
    important:'Important information: figures are classification requirements or family benchmarks, not measured FENEK-BOND C1TE values. Final performance depends on substrates and site conditions. Consult the applicable technical data sheet before use.'
  }
};
