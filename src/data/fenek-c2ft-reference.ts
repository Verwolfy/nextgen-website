import type {Lang} from './site';
import type {ReferenceMetric} from './fenek-c1t-reference';

/** EN 12004-1 class C2FT requirements and third-party benchmarks.
 * Classification thresholds are not asserted to be verified FENEK results.
 * Source details are recorded privately to the site in docs/INTERNE-validation-donnees.csv.
 */
export const c2ftRequirements:ReferenceMetric[]=[
 {key:'c2-initial',kind:'norme',label:{fr:'Adhérence initiale en traction (C2)',ar:'قوة الالتصاق الأولية بالشد (C2)',en:'Initial tensile adhesion (C2)'},value:'≥ 1,0 N/mm²'},
 {key:'c2-eau',kind:'norme',label:{fr:'Adhérence après immersion dans l’eau',ar:'الالتصاق بعد الغمر في الماء',en:'Adhesion after water immersion'},value:'≥ 1,0 N/mm²'},
 {key:'c2-chaleur',kind:'norme',label:{fr:'Adhérence après vieillissement thermique',ar:'الالتصاق بعد التعتيق الحراري',en:'Adhesion after heat ageing'},value:'≥ 1,0 N/mm²'},
 {key:'c2-gel',kind:'norme',label:{fr:'Adhérence après cycles gel/dégel',ar:'الالتصاق بعد دورات التجمد والذوبان',en:'Adhesion after freeze-thaw cycles'},value:'≥ 1,0 N/mm²'},
 {key:'f-precoce',kind:'norme',label:{fr:'Adhérence précoce en traction (F)',ar:'الالتصاق المبكر بالشد (F)',en:'Early tensile adhesion (F)'},value:'≥ 0,5 N/mm² à 6 h au plus'},
 {key:'f-ouvert',kind:'norme',label:{fr:'Adhérence au temps ouvert pour prise rapide',ar:'الالتصاق بعد الزمن المفتوح للفئة سريعة التصلب',en:'Open-time adhesion for fast-setting class'},value:'≥ 0,5 N/mm² après 10 min'},
 {key:'t-glissement',kind:'norme',label:{fr:'Glissement vertical réduit (T)',ar:'انزلاق رأسي منخفض (T)',en:'Reduced vertical slip (T)'},value:'≤ 0,5 mm'},
];

export const c2ftFamilyReferences:ReferenceMetric[]=[
 {key:'consommation-par-mm',kind:'famille',label:{fr:'Consommation de référence par mm de lit',ar:'استهلاك مرجعي لكل ملم من طبقة اللاصق',en:'Reference coverage per mm of bed'},value:'≈ 1,5 kg/m²/mm'},
 {key:'eau',kind:'famille',label:{fr:'Eau des équivalents, ramenée à un sac de 25 kg',ar:'ماء الخلط في المنتجات المماثلة محسوباً لكل 25 كغ',en:'Comparable mixing water normalized to a 25 kg bag'},value:'≈ 4,75–6,25 L / 25 kg'},
 {key:'duree-vie',kind:'famille',label:{fr:'Durée pratique d’utilisation de produits comparables',ar:'مدة استعمال الخليط في منتجات مماثلة',en:'Pot life in comparable technical sheets'},value:'≈ 30 min'},
 {key:'temps-ouvert',kind:'famille',label:{fr:'Temps ouvert déclaré selon formulation',ar:'الزمن المفتوح المعلن بحسب التركيبة',en:'Declared open time across comparable products'},value:'≈ 10–30 min'},
 {key:'jointoiement',kind:'famille',label:{fr:'Jointoiement annoncé après pose sur produits comparables',ar:'موعد تعبئة الفواصل لدى منتجات مماثلة',en:'Grouting times declared for comparable products'},value:'≈ 2–3 h'},
 {key:'ajustement',kind:'famille',label:{fr:'Délai d’ajustement sur références comparables',ar:'مدة تعديل موضع البلاط في منتجات مماثلة',en:'Adjustment time in comparable technical sheets'},value:'≈ 10 min'},
];

type Copy={
 pageTitle:string;metaDescription:string;sheetTitle:string;lead:string;nav:string[];
 uses:string[];benefits:string[];substrates:string[];
 usesTitle:string;substratesTitle:string;identityTitle:string;
 designationLabel:string;referenceLabel:string;rangeLabel:string;formatLabel:string;classLabel:string;
 techTitle:string;familyTitle:string;fieldTitle:string;metricTitle:string;
 applicationTitle:string;prepTitle:string;preparation:string[];conditionsTitle:string;conditions:string[];
 consumptionTitle:string;stepsTitle:string;safetyTitle:string;safety:string[];
 documentsTitle:string;downloadLabel:string;printLabel:string;requestLabel:string;quoteLabel:string;whatsappLabel:string;
 relatedTitle:string;comparisonTitle:string;comparisonNote:string;linkLabel:string;
};
export const c2ftCopy:Record<Lang,Copy>={
 fr:{
  pageTitle:'FENEK-BOND C2FT | Colle carrelage améliorée à prise rapide',
  metaDescription:'FENEK-BOND C2FT : repères EN 12004-1 pour mortier-colle amélioré, rapide et à glissement réduit. Supports, application, critères techniques, documentation et devis.',
  sheetTitle:'Fiche produit — FENEK-BOND C2FT',
  lead:'Mortier-colle cimentaire à désignation C2FT pour travaux de carrelage nécessitant une classe d’adhérence améliorée, une prise rapide et un glissement vertical réduit.',
  nav:['Aperçu','Détails produits','Application','Documents'],
  uses:['Pose de carreaux céramiques et grès cérame sur murs et sols, selon compatibilité du système.','Travaux où un enchaînement rapide des opérations peut être recherché.','Pose sur supports cimentaires préparés, en intérieur et en extérieur selon la fiche applicable.'],
  benefits:['C2 : classe d’adhérence améliorée, seuils à 1,0 N/mm².','F : critère de résistance précoce à 6 heures au plus.','T : contrôle du glissement vertical en laboratoire.'],
  substrates:['Béton suffisamment durci et chapes à base de ciment, stables et propres.','Enduits ciment cohésifs, sans poussière, laitance ni parties friables.','Supports déformables, anciens carrelages et zones humides : choix du système à confirmer séparément.'],
  usesTitle:'Applications usuelles de la famille',substratesTitle:'Supports à examiner',identityTitle:'Identification produit',
  designationLabel:'Désignation',referenceLabel:'Code catalogue',rangeLabel:'Gamme',formatLabel:'Format de présentation',classLabel:'Classe dans la désignation',
  techTitle:'Exigences normatives de la classe C2FT',familyTitle:'Repères quantitatifs de produits comparables',
  fieldTitle:'Propriété',metricTitle:'Seuil / donnée comparative',
  applicationTitle:'Application',prepTitle:'Préparation du support',
  preparation:['Vérifier stabilité, planéité, cohésion, propreté et humidité du fond.','Éliminer huiles, poussières, laitance et résidus qui nuisent à l’adhérence.','Employer une spatule crantée adaptée et contrôler le transfert par soulèvement ponctuel du carreau.'],
  conditionsTitle:'Conditions de chantier',conditions:['Préparer de petites gâchées lorsque l’adhésif est à prise rapide.','Ne jamais prolonger artificiellement la durée d’utilisation par ajout d’eau.','Vérifier la formation éventuelle d’une peau avant de poser ; éviter gel, vent fort et surfaces surchauffées.'],
  consumptionTitle:'Repères de consommation et de gâchage de la famille',stepsTitle:'Six étapes illustrées',safetyTitle:'Environnement et sécurité',
  safety:['Porter gants, lunettes et protection respiratoire adaptée lors de la manipulation de la poudre.','Éviter les projections et inhalations de poussières ; se laver les mains après usage.','Conserver au sec et éviter tout rejet de mortier dans les eaux usées.'],
  documentsTitle:'Documents et demande de devis',downloadLabel:'Télécharger la fiche produit PDF',printLabel:'Imprimer / enregistrer en PDF',
  requestLabel:'Demander la fiche technique et la FDS',quoteLabel:'Obtenir un devis',whatsappLabel:'Échanger sur WhatsApp',
  relatedTitle:'Références voisines',comparisonTitle:'Comparer les classes de colles BOND',
  comparisonNote:'C1TE, C2FT et C2TE désignent trois combinaisons de propriétés de classement distinctes.',linkLabel:'Voir la fiche'
 },
 ar:{
  pageTitle:'FENEK-BOND C2FT | لاصق بلاط إسمنتي محسن وسريع التصلب',
  metaDescription:'FENEK-BOND C2FT: معلومات EN 12004-1 للفئة المحسنة وسريعة التصلب والمنخفضة الانزلاق، وتحضير الأسطح والتطبيق وطلب الوثائق.',
  sheetTitle:'بطاقة المنتج — FENEK-BOND C2FT',
  lead:'ملاط لاصق إسمنتي يحمل الرمز C2FT، مخصص لفئة التصاق محسنة مع خاصية التصلب السريع وانخفاض الانزلاق الرأسي عند اختبار التصنيف.',
  nav:['نظرة عامة','تفاصيل المنتج','التطبيق','الوثائق'],
  uses:['تركيب بلاط السيراميك والخزف على الجدران والأرضيات بحسب ملاءمة النظام.','أعمال البلاط التي تتطلب تنظيماً سريعاً للمراحل التالية.','التركيب على الأسطح الإسمنتية المهيأة داخل المباني وخارجها وفق النشرة الفنية ذات الصلة.'],
  benefits:['C2: فئة التصاق محسن مع حدود لا تقل عن 1.0 نيوتن/مم².','F: معيار التصاق مبكر خلال ست ساعات كحد أقصى.','T: الحد من الانزلاق الرأسي وفق اختبار التصنيف.'],
  substrates:['خرسانة ناضجة وطبقات تسوية إسمنتية نظيفة وثابتة.','محارة إسمنتية متماسكة خالية من الأتربة والطبقات الضعيفة.','الأسطح القابلة للتشوه والبلاط القديم والمناطق الرطبة تتطلب اختياراً مستقلاً لنظام التركيب.'],
  usesTitle:'استخدامات الفئة المعتادة',substratesTitle:'فحص الأسطح',identityTitle:'بيانات المنتج',
  designationLabel:'التسمية',referenceLabel:'رمز الكتالوج',rangeLabel:'المجموعة',formatLabel:'العبوة المذكورة',classLabel:'الفئة في التسمية',
  techTitle:'المتطلبات المعيارية للفئة C2FT',familyTitle:'مؤشرات رقمية من منتجات مماثلة',
  fieldTitle:'الخاصية',metricTitle:'الحد أو القيمة المقارنة',
  applicationTitle:'التطبيق',prepTitle:'تحضير السطح',
  preparation:['فحص الثبات والاستواء والتماسك والنظافة والرطوبة.','إزالة الزيوت والأتربة والطبقات الإسمنتية الضعيفة وبقايا المواد غير المتماسكة.','اختيار المالج المسنن المناسب وفحص انتقال اللاصق إلى ظهر البلاطة.'],
  conditionsTitle:'ظروف الورشة',conditions:['تحضير دفعات خلط صغيرة عند استخدام لاصق سريع التصلب.','عدم محاولة تمديد مدة استخدام الخليط بإضافة الماء مجدداً.','التحقق من عدم تشكل قشرة على اللاصق قبل وضع البلاط وتجنب الصقيع والرياح والسطوح الساخنة.'],
  consumptionTitle:'مؤشرات استهلاك وماء خلط منتجات مماثلة',stepsTitle:'ست مراحل تطبيق مصورة',safetyTitle:'البيئة والسلامة',
  safety:['استخدام القفازات والنظارات ووسيلة مناسبة للحماية من غبار المسحوق.','تجنب استنشاق الغبار ووصول الخليط إلى العينين وغسل اليدين بعد الاستخدام.','حفظ الأكياس في مكان جاف ومنع تصريف الملاط في شبكة الصرف.'],
  documentsTitle:'الوثائق وطلب الأسعار',downloadLabel:'تنزيل بطاقة المنتج PDF',printLabel:'طباعة البطاقة أو حفظها PDF',
  requestLabel:'طلب النشرة الفنية وصحيفة بيانات السلامة',quoteLabel:'طلب عرض سعر',whatsappLabel:'التواصل عبر واتساب',
  relatedTitle:'منتجات مرتبطة',comparisonTitle:'مقارنة فئات لواصق BOND',
  comparisonNote:'ترمز C1TE وC2FT وC2TE إلى مجموعات مختلفة من خصائص التصنيف.',linkLabel:'عرض البطاقة'
 },
 en:{
  pageTitle:'FENEK-BOND C2FT | Improved fast-setting tile adhesive',
  metaDescription:'FENEK-BOND C2FT: EN 12004-1 improved fast-setting reduced-slip tile adhesive class, substrates, installation steps, independent benchmarks and document requests.',
  sheetTitle:'Product sheet — FENEK-BOND C2FT',
  lead:'Cementitious tile adhesive designated C2FT, combining an improved adhesion class with fast-setting and reduced vertical slip classification.',
  nav:['Overview','Product details','Application','Documents'],
  uses:['Fixing ceramic and porcelain tiles to walls and floors where the system is suitable.','Tiling operations for which rapid sequencing of subsequent work is sought.','Installation over prepared cementitious backgrounds, indoors or outdoors subject to the applicable product sheet.'],
  benefits:['C2: improved adhesion class with 1.0 N/mm² tensile thresholds.','F: early adhesion requirement within six hours.','T: reduced vertical slip in classification testing.'],
  substrates:['Sound, cured concrete and stable cement screeds.','Clean cohesive cement renders free from dust and laitance.','Deformable bases, existing tiling and wet areas require separate system selection.'],
  usesTitle:'Common uses in the class',substratesTitle:'Substrates to assess',identityTitle:'Product identification',
  designationLabel:'Designation',referenceLabel:'Catalogue code',rangeLabel:'Range',formatLabel:'Catalogue packaging',classLabel:'Class shown in designation',
  techTitle:'EN 12004-1 C2FT class requirements',familyTitle:'Quantitative figures from comparable products',
  fieldTitle:'Property',metricTitle:'Threshold / comparison',
  applicationTitle:'Application',prepTitle:'Substrate preparation',
  preparation:['Check soundness, flatness, cleanliness and moisture of the background.','Remove oil, dust, laitance and any loose materials.','Use an appropriate notched trowel and lift a sample tile to check adhesive transfer.'],
  conditionsTitle:'Working conditions',conditions:['Prepare smaller batches for fast-setting adhesives.','Never extend the usable life of a stiffening mix by adding water.','Check for surface skinning before laying; avoid frost, strong wind and overheated substrates.'],
  consumptionTitle:'Family consumption and mixing-water benchmarks',stepsTitle:'Six illustrated installation stages',safetyTitle:'Environment and safety',
  safety:['Wear gloves, safety glasses and appropriate dust protection while handling dry powder.','Avoid dust inhalation and eye splashes; wash hands after handling.','Store bags dry and avoid discharging mortar into drains.'],
  documentsTitle:'Documents and quotations',downloadLabel:'Download product sheet PDF',printLabel:'Print / save as PDF',
  requestLabel:'Request technical and safety data sheets',quoteLabel:'Request quotation',whatsappLabel:'Contact by WhatsApp',
  relatedTitle:'Related references',comparisonTitle:'Compare BOND adhesive classes',
  comparisonNote:'C1TE, C2FT and C2TE combine different classification properties.',linkLabel:'View sheet'
 }
};
