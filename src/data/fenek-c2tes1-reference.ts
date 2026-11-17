import type {Lang} from './site';
import type {ReferenceMetric} from './fenek-c1t-reference';

/** Classification EN 12004-1:2017 and independently sourced product-family
 * comparisons. Never treat a competitor formulation as an approved FENEK TDS.
 * Sources: docs/INTERNE-validation-donnees.csv (internal to site).
 */
export const c2tes1Requirements:ReferenceMetric[]=[
 {key:'c2-initial',kind:'norme',label:{fr:'Adhérence initiale en traction (C2)',ar:'قوة الالتصاق الأولية بالشد (C2)',en:'Initial tensile adhesion (C2)'},value:'≥ 1,0 N/mm²'},
 {key:'c2-eau',kind:'norme',label:{fr:'Adhérence après immersion dans l’eau',ar:'الالتصاق بعد الغمر في الماء',en:'Adhesion after water immersion'},value:'≥ 1,0 N/mm²'},
 {key:'c2-chaleur',kind:'norme',label:{fr:'Adhérence après vieillissement thermique',ar:'الالتصاق بعد التعتيق الحراري',en:'Adhesion after heat ageing'},value:'≥ 1,0 N/mm²'},
 {key:'c2-gel',kind:'norme',label:{fr:'Adhérence après cycles gel/dégel',ar:'الالتصاق بعد دورات التجمد والذوبان',en:'Adhesion after freeze-thaw cycles'},value:'≥ 1,0 N/mm²'},
 {key:'t-glissement',kind:'norme',label:{fr:'Glissement vertical réduit (T)',ar:'انزلاق رأسي منخفض (T)',en:'Reduced vertical slip (T)'},value:'≤ 0,5 mm'},
 {key:'temps-ouvert-normal',kind:'norme',label:{fr:'Adhérence après temps ouvert normal',ar:'الالتصاق بعد زمن الفتح العادي',en:'Normal open-time adhesion'},value:'≥ 0,5 N/mm² (20 min)'},
 {key:'e-temps-ouvert',kind:'norme',label:{fr:'Adhérence après temps ouvert prolongé (E)',ar:'الالتصاق بعد زمن الفتح الممتد (E)',en:'Extended open-time adhesion (E)'},value:'≥ 0,5 N/mm² (30 min)'},,
 {key:'s1-deformabilite',kind:'norme',label:{fr:'Déformabilité transversale (S1)',ar:'قابلية التشوه العرضي (S1)',en:'Transverse deformation (S1)'},value:'≥ 2,5 mm ; < 5 mm'},
];

export const c2tes1FamilyReferences:ReferenceMetric[]=[
 {key:'eau',kind:'famille',label:{fr:'Eau de gâchage, produits C2TE S1 comparables',ar:'ماء خلط منتجات مماثلة من فئة C2TE S1',en:'Mixing water of C2TE S1 comparables'},value:'≈ 5,75–7,75 L / 25 kg'},
 {key:'temps-ouvert',kind:'famille',label:{fr:'Temps ouvert annoncé sur équivalent de même classe',ar:'الزمن المفتوح المعلن لمنتج مماثل',en:'Declared open time of comparable adhesive'},value:'≈ 30 min'},
 {key:'vie-en-pot',kind:'famille',label:{fr:'Durée pratique du mortier chez un fabricant comparable',ar:'مدة استعمال الخليط في منتج مماثل',en:'Pot life declared for comparable formulation'},value:'> 8 h (23 °C)'},
 {key:'consommation-peigne',kind:'famille',label:{fr:'Consommation déclarée selon dents et support',ar:'الاستهلاك المعلن حسب المشط والسطح',en:'Declared coverage according to trowel and substrate'},value:'≈ 2,25–5 kg/m²'},
 {key:'deformabilite',kind:'famille',label:{fr:'Plage de classement de déformation S1',ar:'مجال تصنيف التشوه S1',en:'S1 class transverse-deformation interval'},value:'≥ 2,5 mm ; < 5 mm'},
 {key:'jointoiement',kind:'famille',label:{fr:'Jointoiement des carreaux muraux, équivalent',ar:'تعبئة فواصل البلاط الجداري في منتج مماثل',en:'Wall grouting time on comparable product'},value:'≈ 4–8 h'},
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
export const c2tes1Copy:Record<Lang,Copy>={
 fr:{
  pageTitle:'FENEK-BOND C2TE-S1 | Mortier-colle déformable à temps ouvert prolongé',
  metaDescription:'FENEK-BOND C2TE-S1 : mortier-colle à adhérence améliorée, glissement réduit, temps ouvert prolongé et déformabilité S1. Exigences EN 12004-1, supports, guide d’application et documentation.',
  sheetTitle:'Fiche produit — FENEK-BOND C2TE-S1',
  lead:'Mortier-colle cimentaire de désignation C2TE-S1 associant classe d’adhérence améliorée, glissement réduit, temps ouvert prolongé et déformabilité S1 pour la pose de carrelage.',
  nav:['Aperçu','Détails produits','Application','Documents'],
  uses:['Pose de carrelage céramique et grès cérame sur murs et sols, selon système retenu.','Pose dans des systèmes exigeant une colle déformable S1, après vérification du support et du carrelage.','Usage intérieur ou extérieur et dans les zones humides sous réserve d’une spécification compatible.'],
  benefits:['C2 : exigences d’adhérence améliorée de 1,0 N/mm².','T : glissement réduit dans l’essai normalisé.','E : temps ouvert prolongé ; S1 : déformation transversale entre 2,5 et 5 mm.'],
  substrates:['Béton durci, stable, propre, avec planéité contrôlée.','Chapes et enduits ciment cohésifs, préparés et convenablement secs.','Supports présentant des mouvements : prévoir joints de fractionnement et une étude du système, même en présence de la classe S1.'],
  usesTitle:'Domaines d’emploi possibles selon système',substratesTitle:'Supports à préparer',identityTitle:'Identification',
  designationLabel:'Désignation',referenceLabel:'Code catalogue',rangeLabel:'Gamme',formatLabel:'Conditionnement catalogue',classLabel:'Classe dans la désignation',
  techTitle:'Critères normatifs EN 12004-1 — C2TE-S1',familyTitle:'Repères chiffrés issus d’équivalents de la famille',
  fieldTitle:'Caractéristique',metricTitle:'Seuil / ordre de grandeur',
  applicationTitle:'Application',prepTitle:'Préparer le support',
  preparation:['Vérifier cohésion, propreté, planéité et humidité avant encollage.','Éliminer poussière, graisse, huile, peinture non adhérente et laitance.','Adapter la denture au carrelage et contrôler le transfert de colle en soulevant une pièce.'],
  conditionsTitle:'Précautions de pose',conditions:['Réduire la surface encollée si le vent, le soleil ou un support absorbant accélère la formation d’une peau.','Pour une pose nécessitant un contact renforcé, contrôler la couverture au dos des carreaux et envisager le double encollage selon le système.','Respecter les délais de travail et de jointoiement indiqués dans la fiche technique du produit réellement utilisé.'],
  consumptionTitle:'Consommation et eau de gâchage comparatives',stepsTitle:'Six étapes d’application illustrées',safetyTitle:'Sécurité et environnement',
  safety:['Prévoir gants, protection oculaire et protection respiratoire adaptée aux poussières lors de la manipulation des poudres.','Travailler dans un espace ventilé et éviter le contact du mélange avec les yeux et la peau.','Conserver les sacs au sec et ne pas rejeter les résidus de mortier dans les canalisations.'],
  documentsTitle:'Documentation et devis',downloadLabel:'Télécharger la fiche informative PDF',printLabel:'Imprimer / enregistrer en PDF',
  requestLabel:'Demander la fiche technique et la FDS',quoteLabel:'Demander un devis',whatsappLabel:'Contacter par WhatsApp',
  relatedTitle:'Produits associés',comparisonTitle:'Repères de classement dans la gamme BOND',
  comparisonNote:'C2FT, C2TE et C2TE-S1-S1 combinent des caractéristiques normatives distinctes.',linkLabel:'Consulter la fiche'
 },
 ar:{
  pageTitle:'FENEK-BOND C2TE-S1 | لاصق بلاط محسن بزمن مفتوح ممتد',
  metaDescription:'FENEK-BOND C2TE-S1: فئة لاصق إسمنتي محسن منخفض الانزلاق بزمن مفتوح ممتد، متطلبات EN 12004-1 وتحضير السطح ومراحل التطبيق والوثائق.',
  sheetTitle:'بطاقة المنتج — FENEK-BOND C2TE-S1',
  lead:'ملاط لاصق إسمنتي يحمل الرمز C2TE-S1 ويجمع بين الالتصاق المحسن والانزلاق المنخفض والزمن المفتوح الممتد وقابلية التشوه العرضي من الفئة S1.',
  nav:['نظرة عامة','تفاصيل المنتج','التطبيق','الوثائق'],
  uses:['تركيب البلاط الخزفي والسيراميك على الجدران والأرضيات بحسب النظام المعتمد.','أعمال التبليط التي تتطلب مادة لاصقة قابلة للتشوه من الفئة S1 بعد دراسة النظام.','استخدام داخلي أو خارجي وفي الأماكن الرطبة بعد تحديد نظام متوافق.'],
  benefits:['C2: متطلبات التصاق محسّن بحدود 1.0 نيوتن/مم².','T: انخفاض الانزلاق وفق اختبار معياري.','E: زمن مفتوح ممتد في الاختبار؛ S1: تشوه عرضي بين 2.5 و5 مم.'],
  substrates:['خرسانة ناضجة وثابتة ونظيفة بعد التحقق من استوائها.','طبقات تسوية ومحارة إسمنتية متماسكة ومحضّرة وجافة بالشكل المناسب.','البلاط القديم والأسطح القابلة للتشوه والبيئات شديدة الرطوبة تحتاج إلى تقييم خاص.'],
  usesTitle:'مجالات استخدام محتملة بحسب النظام',substratesTitle:'تحضير الأسطح',identityTitle:'بيانات المنتج',
  designationLabel:'التسمية',referenceLabel:'رمز الكتالوج',rangeLabel:'المجموعة',formatLabel:'العبوة في الكتالوج',classLabel:'الفئة المذكورة في التسمية',
  techTitle:'متطلبات EN 12004-1 للفئة C2TE-S1',familyTitle:'قيم مقارنة من منتجات الفئة',
  fieldTitle:'الخاصية',metricTitle:'الحد أو القيمة المرجعية',
  applicationTitle:'التطبيق',prepTitle:'تجهيز السطح',
  preparation:['فحص التماسك والنظافة والاستواء والرطوبة قبل توزيع اللاصق.','إزالة الأتربة والدهون والزيوت والطلاء غير المتماسك والطبقة الإسمنتية الضعيفة.','اختيار المالج المسنن حسب نوع البلاط وفحص انتقال اللاصق إلى خلف البلاطة.'],
  conditionsTitle:'احتياطات أثناء التركيب',conditions:['تقليل المساحة المدهونة إذا أدّت الشمس أو الرياح أو امتصاص السطح إلى تشكل قشرة على اللاصق.','فحص تغطية ظهر البلاط واختيار دهن إضافي للجهة الخلفية عند الحاجة حسب النظام.','اتباع مدة العمل وموعد ملء الفواصل المحددين في النشرة الفنية للمنتج المستخدم.'],
  consumptionTitle:'مؤشرات مقارنة للاستهلاك وماء الخلط',stepsTitle:'ست مراحل تطبيق مصورة',safetyTitle:'السلامة والبيئة',
  safety:['ارتداء القفازات وواقي العينين ووسيلة مناسبة للحماية من غبار المسحوق عند التعامل مع المادة الجافة.','العمل في مكان جيد التهوية وتجنب ملامسة الخليط للعينين والجلد.','حفظ الأكياس بعيداً عن الرطوبة وعدم تصريف بقايا الملاط في شبكة المياه المستعملة.'],
  documentsTitle:'الوثائق وطلب الأسعار',downloadLabel:'تنزيل بطاقة المنتج PDF',printLabel:'طباعة البطاقة أو حفظها PDF',
  requestLabel:'طلب النشرة الفنية وصحيفة بيانات السلامة',quoteLabel:'طلب عرض سعر',whatsappLabel:'التواصل عبر واتساب',
  relatedTitle:'منتجات مرتبطة',comparisonTitle:'مقارنة رموز فئات لواصق BOND',
  comparisonNote:'تمثل C2FT وC2TE وC2TE-S1-S1 مجموعات مختلفة من خصائص التصنيف.',linkLabel:'عرض البطاقة'
 },
 en:{
  pageTitle:'FENEK-BOND C2TE-S1 | Improved tile adhesive with extended open time',
  metaDescription:'FENEK-BOND C2TE-S1: improved cementitious adhesive class with reduced slip and extended open time. EN 12004-1 criteria, substrate preparation, application and documents.',
  sheetTitle:'Product sheet — FENEK-BOND C2TE-S1',
  lead:'Cementitious tile adhesive designated C2TE-S1, combining improved adhesion class, reduced vertical slip and extended open-time classification for ceramic tiling.',
  nav:['Overview','Product details','Application','Documents'],
  uses:['Ceramic and porcelain tiling on walls and floors subject to compatible installation design.','Jobs requiring an appropriate positioning window for the tile format selected.','Indoor and outdoor or wet-area use only where the specified system is suitable.'],
  benefits:['C2: improved adhesion class thresholds of 1.0 N/mm².','T: reduced slip under standard test conditions.','E: extended open-time classification test at 30 minutes.'],
  substrates:['Clean, stable, properly cured concrete with checked flatness.','Sound prepared cement screeds and renders with appropriate moisture levels.','Existing tiles, deformable bases and high-moisture areas call for separate system assessment.'],
  usesTitle:'Potential applications by system',substratesTitle:'Substrates to prepare',identityTitle:'Product identification',
  designationLabel:'Designation',referenceLabel:'Catalogue code',rangeLabel:'Range',formatLabel:'Catalogue packaging',classLabel:'Class appearing in designation',
  techTitle:'EN 12004-1 C2TE-S1 classification criteria',familyTitle:'Numerical benchmarks from comparable adhesives',
  fieldTitle:'Property',metricTitle:'Threshold / indicative value',
  applicationTitle:'Application',prepTitle:'Substrate preparation',
  preparation:['Check soundness, cleanliness, flatness and moisture prior to fixing.','Remove dust, grease, oil, loose paint and any weak laitance.','Match the trowel notch to the tiles and lift a sample tile to verify adhesive transfer.'],
  conditionsTitle:'Installation precautions',conditions:['Reduce the area spread when sun, wind or absorbent surfaces accelerate skin formation.','Check adhesive transfer to the tile back and consider back-buttering where required by the installation system.','Use the actual product technical sheet for working time and grouting wait periods.'],
  consumptionTitle:'Comparable coverage and mixing-water values',stepsTitle:'Six illustrated application stages',safetyTitle:'Environment and safety',
  safety:['Wear gloves, eye protection and suitable respiratory dust protection when handling dry powder.','Work with ventilation and avoid mixture contact with eyes or skin.','Store bags dry and keep mortar waste out of drains.'],
  documentsTitle:'Documents and quotations',downloadLabel:'Download informative product PDF',printLabel:'Print / save as PDF',
  requestLabel:'Request technical and safety data sheets',quoteLabel:'Request quotation',whatsappLabel:'Contact via WhatsApp',
  relatedTitle:'Related products',comparisonTitle:'BOND adhesive class comparison',
  comparisonNote:'C2FT, C2TE-S1 and C2TE-S1-S1 have different combinations of classification properties.',linkLabel:'View sheet'
 }
};
