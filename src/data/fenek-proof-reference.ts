import {buildOtherRecords,type OtherRaw} from './fenek-other-technical-core';
/** PROOF documentary criteria are NOT measured FENEK performances. See docs/LOT_PROOF_SOURCES_20261117.md. */
export const proofDefinitions:OtherRaw[]=[
  {
    "code": "PROOF-ACR-RF",
    "group": "proof-membrane",
    "standard": "EAD 030350-00-0402 (système toiture liquide, si ETA)",
    "intro": {
      "fr": "Membrane d’étanchéité acrylique en phase aqueuse pour toitures et terrasses accessibles à l’entretien.",
      "ar": "غشاء عزل أكريليكي مائي للأسطح مع تفاصيل الوصلات ومناطق الصيانة.",
      "en": "Water-based acrylic roof waterproofing membrane for roof surfaces and properly detailed junctions."
    },
    "requirements": [
      [
        "Destination du kit et support",
        "مجال استعمال النظام والسطح",
        "System intended use and substrate",
        "ETA ou justification de système à définir"
      ],
      [
        "Étanchéité du système",
        "عزل النظام للماء",
        "Water-tightness of the assembly",
        "À vérifier après traitement des points singuliers"
      ],
      [
        "Résistance au vieillissement et aux UV",
        "مقاومة التقادم والأشعة",
        "UV and ageing resistance",
        "Méthode EAD selon système"
      ],
      [
        "Épaisseur sèche minimale",
        "الحد الأدنى للسماكة الجافة",
        "Minimum dry film thickness",
        "Déclaration fabricant à établir"
      ]
    ],
    "family": [
      [
        "Liant de membrane comparable",
        "رابط غشاء مقارن",
        "Comparable membrane binder",
        "Dispersion acrylique"
      ],
      [
        "Mode de pose comparable",
        "طريقة وضع مادة مقارنة",
        "Comparable application method",
        "Application à froid"
      ],
      [
        "Accessoires documentés de toiture",
        "ملحقات عزل السطح الموثقة",
        "Documented roof accessories",
        "Renforts et relevés du système"
      ]
    ]
  },
  {
    "code": "PROOF-CM-O1P",
    "group": "proof-cement",
    "standard": "EN 14891:2017 — CM O1P (désignation à qualifier)",
    "intro": {
      "fr": "Mortier cimentaire d’étanchéité sous carrelage désigné CM O1P, avec pontage à basse température et exposition à l’eau chlorée à qualifier.",
      "ar": "مونة عزل إسمنتية تحت البلاط برمز CM O1P تتطلب إثبات جسر الشقوق في البرد ومقاومة الماء المعالج بالكلور.",
      "en": "Cementitious under-tile waterproofing designated CM O1P, requiring low-temperature crack-bridging and chlorinated-water qualification."
    },
    "requirements": [
      [
        "Adhérence en traction du système CM",
        "قوة التصاق نظام CM",
        "CM system tensile adhesion",
        "≥ 0,5 N/mm² (seuil normatif)"
      ],
      [
        "Pontage des fissures additionnel O1",
        "جسر التشققات الإضافي O1",
        "Additional O1 crack bridging",
        "Essai à −5 °C"
      ],
      [
        "Résistance à l’eau chlorée (P)",
        "مقاومة الماء المكلور P",
        "Chlorinated-water resistance (P)",
        "Essai de classe P selon EN 14891"
      ],
      [
        "Imperméabilité sous pression d’eau",
        "النفاذية تحت ضغط الماء",
        "Water impermeability under pressure",
        "Essai du système EN 14891"
      ]
    ],
    "family": [
      [
        "Procédé cimentaire comparé",
        "نظام عزل إسمنتي مقارن",
        "Comparable cementitious method",
        "Enduit ciment modifié polymère"
      ],
      [
        "Constitution du produit comparable",
        "تركيب منتج إسمنتي مقارن",
        "Comparable product composition",
        "Ciment + dispersion polymère"
      ],
      [
        "Renfort des raccords",
        "تقوية الزوايا والفواصل",
        "Junction reinforcement",
        "Bande d’étanchéité compatible"
      ]
    ]
  },
  {
    "code": "PROOF-CM-O2P",
    "group": "proof-cement",
    "standard": "EN 14891:2017 — CM O2P (désignation à qualifier)",
    "intro": {
      "fr": "Système d’étanchéité cimentaire souple bicomposant sous carrelage, avec classement très basse température O2 et résistance P à documenter.",
      "ar": "نظام عزل إسمنتي مرن بمكونين تحت البلاط مع اختبار التشققات O2 في البرودة الشديدة والماء المكلور P.",
      "en": "Two-component flexible cementitious under-tile membrane requiring O2 very-low-temperature and P chlorinated-water qualification."
    },
    "requirements": [
      [
        "Adhérence en traction du système CM",
        "قوة الالتصاق لنظام CM",
        "CM system tensile adhesion",
        "≥ 0,5 N/mm² (seuil normatif)"
      ],
      [
        "Pontage des fissures additionnel O2",
        "جسر التشققات الإضافي O2",
        "Additional O2 crack bridging",
        "Essai à −20 °C"
      ],
      [
        "Contact avec eau chlorée (P)",
        "ملامسة الماء المكلور P",
        "Chlorinated-water exposure (P)",
        "Essai P selon EN 14891"
      ],
      [
        "Compatibilité du kit bicomposant",
        "توافق مكونات الطقم",
        "Two-component kit compatibility",
        "Sac 20 kg + bidon 10 kg (catalogue FENEK)"
      ]
    ],
    "family": [
      [
        "Système cimentaire comparé",
        "نظام إسمنتي مقارن",
        "Comparable cementitious system",
        "Deux composants"
      ],
      [
        "Destination d’étanchéité comparable",
        "استخدام عزل مقارن",
        "Comparable waterproofing use",
        "Balcons, sanitaires et carrelage"
      ],
      [
        "Application de membrane comparée",
        "تطبيق غشاء مقارن",
        "Comparable membrane application",
        "Brosse, taloche ou rouleau selon produit"
      ]
    ]
  },
  {
    "code": "PROOF-EP-ANC",
    "group": "proof-anchor",
    "standard": "EAD 330499-01-0601 / ETA de scellement selon usage",
    "intro": {
      "fr": "Résine de scellement chimique à base époxy pour tiges d’ancrage, sous dimensionnement et évaluation technique du système.",
      "ar": "راتنج إيبوكسي للتثبيت الكيميائي للقضبان مع تصميم هندسي وتقييم فني للنظام.",
      "en": "Epoxy chemical anchoring resin for threaded rods and dowels, subject to system ETA and engineered anchorage design."
    },
    "requirements": [
      [
        "Agrément du système d’ancrage",
        "تقييم نظام التثبيت",
        "Anchoring system approval",
        "ETA valide requise pour l’usage revendiqué"
      ],
      [
        "Béton fissuré ou non fissuré",
        "الخرسانة المتشققة وغير المتشققة",
        "Cracked/uncracked concrete",
        "Domaine couvert par l’ETA"
      ],
      [
        "Résistance et distances aux rives",
        "مقاومة التثبيت والمسافات",
        "Capacity and edge distances",
        "Dimensionnement selon ETA/EN 1992-4"
      ],
      [
        "Durée de polymérisation avant charge",
        "زمن المعالجة قبل التحميل",
        "Cure before loading",
        "Valeur spécifique à déclarer"
      ]
    ],
    "family": [
      [
        "Chimie d’un ancrage comparable",
        "كيمياء مرساة مقارنة",
        "Comparable anchor chemistry",
        "Résine époxy à deux composants"
      ],
      [
        "Support de scellement comparé",
        "سطح تثبيت مقارن",
        "Comparable anchoring substrate",
        "Béton fissuré et non fissuré selon ETA"
      ],
      [
        "Rapport de mélange comparable",
        "نسبة خلط مرجع مقارن",
        "Comparable mixing ratio",
        "1:1 pour une référence époxy"
      ]
    ]
  },
  {
    "code": "PROOF-EP-INJ",
    "group": "proof-injection",
    "standard": "EN 1504-5:2013 — injection béton F/D/S selon emploi",
    "intro": {
      "fr": "Résine d’injection époxydique destinée au remplissage de fissures stables du béton, avec objectif de transfert de forces à établir.",
      "ar": "راتنج إيبوكسي لحقن الشقوق الخرسانية الثابتة مع تحديد هدف نقل القوى قبل التنفيذ.",
      "en": "Epoxy injection resin for stable concrete cracking, with load-transfer injection purpose to be established by diagnosis."
    },
    "requirements": [
      [
        "Catégorie d’injection EN 1504-5",
        "فئة الحقن وفق EN 1504-5",
        "EN 1504-5 injection category",
        "F, D ou S à caractériser selon formulation"
      ],
      [
        "Injectabilité et ouverture de fissure",
        "قابلية الحقن وعرض الشق",
        "Injectability and crack width",
        "Essai de classe à documenter"
      ],
      [
        "Viscosité et vie en pot",
        "اللزوجة ومدة التشغيل",
        "Viscosity and pot life",
        "Valeurs mesurées à déclarer"
      ],
      [
        "Adhérence et résistance après cure",
        "الالتصاق والمقاومة بعد المعالجة",
        "Bond and cured strength",
        "Essais adaptés à la catégorie"
      ]
    ],
    "family": [
      [
        "Chimie d’injection comparable",
        "نوع راتنج حقن مقارن",
        "Comparable injection chemistry",
        "Époxy bi-composant"
      ],
      [
        "Caractéristique rhéologique comparable",
        "خاصية انسياب مقارنة",
        "Comparable flow behavior",
        "Faible viscosité"
      ],
      [
        "Domaine d’injection comparable",
        "استخدام حقن مقارن",
        "Comparable injection purpose",
        "Fissures et vides de béton"
      ]
    ]
  },
  {
    "code": "PROOF-EP-PRIM",
    "group": "proof-epoxy",
    "standard": "EN 1504-2 (si système de protection du béton) — essai d’adhérence",
    "intro": {
      "fr": "Primaire époxy bicomposant pour préparation des supports minéraux avant les couches de finition compatibles.",
      "ar": "برايمر إيبوكسي بمكونين لتحضير الأسطح المعدنية قبل طبقات التشطيب المتوافقة.",
      "en": "Two-component epoxy primer to prepare sound mineral substrates for compatible resin floor or protection systems."
    },
    "requirements": [
      [
        "Adhérence au support préparé",
        "الالتصاق بالسطح المحضر",
        "Bond to prepared substrate",
        "À qualifier par essai d’arrachement"
      ],
      [
        "Humidité admissible du béton",
        "الرطوبة المقبولة للخرسانة",
        "Permissible concrete moisture",
        "Selon système et FDS/FT"
      ],
      [
        "Compatibilité avec le revêtement final",
        "التوافق مع الطلاء النهائي",
        "Topcoat system compatibility",
        "À documenter par système complet"
      ],
      [
        "Temps utile de travail",
        "مدة التشغيل",
        "Pot life",
        "À mesurer selon température"
      ]
    ],
    "family": [
      [
        "Chimie d’un primaire comparable",
        "كيمياء برايمر مقارن",
        "Comparable primer chemistry",
        "Époxy deux composants"
      ],
      [
        "Usage de primaire comparable",
        "استخدام برايمر مقارن",
        "Comparable primer use",
        "Promoteur d’adhérence"
      ],
      [
        "Support comparable",
        "السطح المقارن",
        "Comparable substrate",
        "Béton et chape ciment"
      ]
    ]
  },
  {
    "code": "PROOF-EP-SB",
    "group": "proof-epoxy",
    "standard": "EN 1504-4:2004 — collage structurel selon emploi",
    "intro": {
      "fr": "Adhésif structural époxy pour reprise de collage sur béton, dont le caractère structurel doit être démontré pour l’emploi ciblé.",
      "ar": "لاصق إيبوكسي إنشائي لأعمال ربط الخرسانة مع التحقق من الأداء بحسب الاستخدام المحدد.",
      "en": "Structural epoxy adhesive for concrete bonding applications, with suitability and load transfer to be demonstrated for the use."
    },
    "requirements": [
      [
        "Domaine du collage structurel",
        "مجال الربط الإنشائي",
        "Structural bonding field",
        "EN 1504-4 selon système qualifié"
      ],
      [
        "Résistance à l’adhérence",
        "مقاومة الالتصاق",
        "Adhesive bond performance",
        "Essais selon support et conception"
      ],
      [
        "Temps ouvert et prise",
        "زمن التطبيق والتصلب",
        "Working and curing times",
        "Valeurs selon température"
      ],
      [
        "Comportement sous charge",
        "السلوك تحت الحمل",
        "Behavior under load",
        "Validation par essais du système"
      ]
    ],
    "family": [
      [
        "Type de colle structurelle comparable",
        "نوع لاصق إنشائي مقارن",
        "Comparable structural adhesive type",
        "Époxy bi-composant"
      ],
      [
        "Support de collage comparable",
        "سطح ربط مقارن",
        "Comparable bond substrate",
        "Béton et éléments métalliques compatibles"
      ],
      [
        "Format d’application comparable",
        "طريقة التطبيق في مرجع مقارن",
        "Comparable installation",
        "Colle thixotrope"
      ]
    ]
  },
  {
    "code": "PROOF-EP-SR",
    "group": "proof-epoxy",
    "standard": "EN 1504-2 (revêtement béton) / EN 13813 (si classification chape)",
    "intro": {
      "fr": "Système de sol époxy autolissant à deux composants pour supports béton préparés et résistances d’usage à qualifier.",
      "ar": "نظام أرضيات إيبوكسي ذاتي التسوية بمكونين فوق الخرسانة المحضرة مع اختبار مقاومة الاستخدام.",
      "en": "Two-component self-smoothing epoxy flooring system for prepared concrete with service performance to be qualified."
    },
    "requirements": [
      [
        "Épaisseur sèche du système",
        "السماكة الجافة للنظام",
        "System dry film thickness",
        "À définir selon trafic"
      ],
      [
        "Adhérence et cohésion du support",
        "الالتصاق وتماسك السطح",
        "Bond and substrate cohesion",
        "Essai de traction adapté"
      ],
      [
        "Résistance à l’usure et chimique",
        "مقاومة التآكل والمواد الكيميائية",
        "Wear and chemical resistance",
        "Essais selon sollicitations réelles"
      ],
      [
        "Classe de glissance",
        "فئة مقاومة الانزلاق",
        "Slip-resistance class",
        "À spécifier selon destination"
      ]
    ],
    "family": [
      [
        "Procédé comparable",
        "طريقة نظام مقارن",
        "Comparable system process",
        "Époxy bi-composant"
      ],
      [
        "Type de finition comparable",
        "نوع تشطيب مقارن",
        "Comparable finish type",
        "Autolissant et multicouche"
      ],
      [
        "Épaisseur d’un système comparable",
        "سماكة نظام أرضية مقارن",
        "Comparable system thickness",
        "2 à 4 mm pour une référence"
      ]
    ]
  },
  {
    "code": "PROOF-PU-1K",
    "group": "proof-membrane",
    "standard": "EAD 030350-00-0402 — membrane liquide de toiture en kit",
    "intro": {
      "fr": "Membrane de toiture polyuréthane monocomposante pour étanchéité liquide, avec primaire, renforts et cure définis par le système.",
      "ar": "غشاء عزل أسطح من البولي يوريثان بمكون واحد مع أساس وتقويات ومعالجة وفق النظام.",
      "en": "Single-component polyurethane liquid roof membrane, with primer, reinforcement and curing defined by the complete system."
    },
    "requirements": [
      [
        "Type de système liquide",
        "نوع نظام العزل السائل",
        "Liquid waterproofing system type",
        "PU 1K à qualifier"
      ],
      [
        "Vie utile et charges de service",
        "العمر الافتراضي وأحمال الاستخدام",
        "Service life and loads",
        "Classe de kit selon ETA"
      ],
      [
        "Pontage et tenue climatique",
        "جسر الشقوق ومقاومة المناخ",
        "Crack bridging and weathering",
        "Évaluation EAD selon usage"
      ],
      [
        "Épaisseur et consommation du kit",
        "سماكة النظام واستهلاكه",
        "Kit thickness and coverage",
        "Déclaration selon procédé complet"
      ]
    ],
    "family": [
      [
        "Chimie de membrane comparable",
        "نوع غشاء مقارن",
        "Comparable membrane chemistry",
        "Polyuréthane mono-composant"
      ],
      [
        "Procédé toiture comparable",
        "نظام سطح مقارن",
        "Comparable roof process",
        "Pose à froid et sans joints"
      ],
      [
        "Renfort de membrane comparable",
        "تقوية غشاء مقارنة",
        "Comparable reinforcement",
        "Voile de renforcement selon kit"
      ]
    ]
  },
  {
    "code": "PROOF-PU-INJ",
    "group": "proof-injection",
    "standard": "EN 1504-5:2013 — injection flexible/gonflante selon classement",
    "intro": {
      "fr": "Résine d’injection polyuréthane pour obturation de venues d’eau dans le béton, dont la réactivité à l’eau et la classification sont à qualifier.",
      "ar": "راتنج بولي يوريثان لحقن تسربات الماء في الخرسانة مع التحقق من التفاعل بالماء وفئة الحقن.",
      "en": "Polyurethane injection resin to address water ingress in concrete, subject to classification and water-reactivity assessment."
    },
    "requirements": [
      [
        "Catégorie d’injection visée",
        "فئة الحقن المستهدفة",
        "Target injection category",
        "D ou S selon formulation et usage"
      ],
      [
        "Réactivité à l’eau et expansion",
        "التفاعل مع الماء والتمدد",
        "Water reaction and expansion",
        "Essais de procédé à définir"
      ],
      [
        "Pression d’injection et injectabilité",
        "ضغط الحقن وقابليته",
        "Injection pressure and injectability",
        "Selon ouverture de fissure"
      ],
      [
        "Étanchéité après injection",
        "العزل بعد الحقن",
        "Water-tightness after injection",
        "Contrôle sur ouvrage"
      ]
    ],
    "family": [
      [
        "Chimie comparable",
        "كيمياء راتنج مقارن",
        "Comparable resin chemistry",
        "Polyuréthane réactif"
      ],
      [
        "Procédé d’injection comparable",
        "طريقة حقن مقارنة",
        "Comparable injection procedure",
        "Injection par packers"
      ],
      [
        "Réaction d’obturation comparable",
        "آلية إيقاف التسرب في مرجع مقارن",
        "Comparable water-stop response",
        "Formation de mousse selon résine"
      ]
    ]
  },
  {
    "code": "PROOF-PU-SEAL",
    "group": "proof-sealant",
    "standard": "EN 15651-1 / EN 15651-4:2012 selon destination du joint",
    "intro": {
      "fr": "Mastic d’étanchéité polyuréthane pour joints de mouvement, avec largeur et capacité de déplacement à dimensionner.",
      "ar": "مادة سد فواصل من البولي يوريثان للفواصل المتحركة مع تحديد العرض والقدرة على الحركة.",
      "en": "Polyurethane joint sealant for movement joints with width, depth and movement accommodation established by design."
    },
    "requirements": [
      [
        "Destination du mastic",
        "مجال استعمال المعجون",
        "Sealant intended use",
        "F façade / PW sol selon EN 15651"
      ],
      [
        "Capacité de mouvement",
        "سعة الحركة",
        "Movement capability",
        "Classe à déclarer par essais"
      ],
      [
        "Adhérence aux lèvres",
        "الالتصاق بجوانب الفاصل",
        "Adhesion to joint flanks",
        "Essai selon matériau"
      ],
      [
        "Compatibilité fond de joint",
        "توافق حشوة خلفية",
        "Backing rod compatibility",
        "Conception de joint à valider"
      ]
    ],
    "family": [
      [
        "Chimie de mastic comparable",
        "كيمياء مادة سد مقارنة",
        "Comparable sealant chemistry",
        "Polyuréthane mono-composant"
      ],
      [
        "Catégorie de joint comparable",
        "نوع فاصل مقارن",
        "Comparable joint application",
        "Joints de sol et génie civil"
      ],
      [
        "Norme d’un mastic comparable",
        "معيار مادة مقارنة",
        "Comparable sealant standard",
        "EN 15651-4 (référence distincte)"
      ]
    ]
  }
];
export const proofRecords=buildOtherRecords(proofDefinitions);
