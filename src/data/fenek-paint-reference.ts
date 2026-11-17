import {buildOtherRecords,type OtherRaw} from './fenek-other-technical-core';
/** PAINT reference test methods and third-party data are not certified FENEK results. */
export const paintDefinitions:OtherRaw[]=[
  {
    "code": "PAINT-ENT-L",
    "group": "paint-paste",
    "standard": "EN 16566:2014",
    "intro": {
      "fr": "Enduit en pâte pour lisser les supports intérieurs avant peinture.",
      "ar": "معجون جاهز لتسوية الجدران الداخلية قبل الدهان.",
      "en": "Ready-mixed filler for smoothing interior walls before painting."
    },
    "requirements": [
      [
        "Adhérence au support",
        "الالتصاق بالسطح",
        "Bond to substrate",
        "Essai sur support"
      ],
      [
        "État du support",
        "حالة السطح",
        "Substrate condition",
        "Planéité et défauts à vérifier"
      ],
      [
        "Séchage et recouvrement",
        "الجفاف وإعادة الطلاء",
        "Drying and recoating",
        "Séchage selon épaisseur"
      ],
      [
        "Compatibilité des finitions",
        "توافق الطلاءات",
        "Topcoat compatibility",
        "Essai avec primaire"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable product technology",
        "Enduit organique en pâte"
      ],
      [
        "Usage d’un produit comparable",
        "استخدام منتج مقارن",
        "Comparable product application",
        "Lissage avant peinture"
      ],
      [
        "Classe ou propriété tierce documentée",
        "فئة أو خاصية موثقة لدى منتج آخر",
        "Documented third-party class or property",
        "État du support à contrôler"
      ]
    ]
  },
  {
    "code": "PAINT-FAC-EL",
    "group": "paint-exterior",
    "standard": "EN 1062-1 / EN 1062-7",
    "intro": {
      "fr": "Peinture élastomère de façade pour microfissures stabilisées, avec pontage à qualifier.",
      "ar": "دهان واجهات مرن للشقوق الشعرية الثابتة مع اختبار جسر التشققات.",
      "en": "Elastomeric facade paint for stable hairline cracks, subject to crack-bridging qualification."
    },
    "requirements": [
      [
        "Pontage des fissures A",
        "جسر التشققات A",
        "Crack bridging A",
        "Classe A à établir"
      ],
      [
        "Perméabilité eau liquide W",
        "نفاذية الماء W",
        "Liquid-water permeability W",
        "Classe W à déclarer"
      ],
      [
        "Perméabilité vapeur V",
        "نفاذية بخار الماء V",
        "Water vapour permeability V",
        "Classe V à déclarer"
      ],
      [
        "Vieillissement UV et climatique",
        "مقاومة الأشعة والمناخ",
        "UV and weathering",
        "Essai d’exposition"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable product technology",
        "Peinture élastomère"
      ],
      [
        "Usage d’un produit comparable",
        "استخدام منتج مقارن",
        "Comparable product application",
        "Fissures capillaires stables"
      ],
      [
        "Classe ou propriété tierce documentée",
        "فئة أو خاصية موثقة لدى منتج آخر",
        "Documented third-party class or property",
        "Essai de pontage"
      ]
    ]
  },
  {
    "code": "PAINT-FAC-M",
    "group": "paint-exterior",
    "standard": "EN 1062-1",
    "intro": {
      "fr": "Peinture acrylique mate pour protection décorative des façades préparées.",
      "ar": "دهان أكريليكي مطفي لحماية الواجهات المحضرة وتزيينها.",
      "en": "Matt acrylic paint for the decorative protection of prepared façades."
    },
    "requirements": [
      [
        "Classe de brillance",
        "فئة اللمعان",
        "Gloss class",
        "Classe G à mesurer"
      ],
      [
        "Perméabilité eau liquide W",
        "نفاذية الماء W",
        "Liquid-water permeability W",
        "Classe W à établir"
      ],
      [
        "Perméabilité vapeur V",
        "نفاذية بخار الماء V",
        "Water vapour permeability V",
        "Classe V à établir"
      ],
      [
        "Vieillissement UV et climatique",
        "مقاومة الأشعة والمناخ",
        "UV and weathering",
        "Tenue UV à tester"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable product technology",
        "Acrylique en phase aqueuse"
      ],
      [
        "Usage d’un produit comparable",
        "استخدام منتج مقارن",
        "Comparable product application",
        "Façade minérale"
      ],
      [
        "Classe ou propriété tierce documentée",
        "فئة أو خاصية موثقة لدى منتج آخر",
        "Documented third-party class or property",
        "Finition mate"
      ]
    ]
  },
  {
    "code": "PAINT-FAC-SX",
    "group": "paint-exterior",
    "standard": "EN 1062-1",
    "intro": {
      "fr": "Peinture de façade siloxane conçue pour une faible absorption d’eau et un bon transfert de vapeur.",
      "ar": "دهان واجهات سيلوكساني منخفض امتصاص ماء المطر ونفاذ لبخار الماء بعد اختبار.",
      "en": "Siloxane facade coating for reduced rainwater absorption and vapour diffusion after testing."
    },
    "requirements": [
      [
        "Perméabilité vapeur V",
        "نفاذية بخار الماء V",
        "Water vapour permeability V",
        "Classe V à mesurer"
      ],
      [
        "Perméabilité eau liquide W",
        "نفاذية الماء W",
        "Liquid-water permeability W",
        "Classe W à mesurer"
      ],
      [
        "Adhérence au support",
        "الالتصاق بالسطح",
        "Bond to substrate",
        "Essai sur enduit"
      ],
      [
        "Vieillissement UV et climatique",
        "مقاومة الأشعة والمناخ",
        "UV and weathering",
        "Résistance aux UV"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable product technology",
        "Résine silicone"
      ],
      [
        "Usage d’un produit comparable",
        "استخدام منتج مقارن",
        "Comparable product application",
        "Façade respirante"
      ],
      [
        "Classe ou propriété tierce documentée",
        "فئة أو خاصية موثقة لدى منتج آخر",
        "Documented third-party class or property",
        "V1 et W3 sur un produit comparable"
      ]
    ]
  },
  {
    "code": "PAINT-INT-M",
    "group": "paint-interior",
    "standard": "EN 13300",
    "intro": {
      "fr": "Peinture acrylique mate pour murs et plafonds intérieurs propres et préparés.",
      "ar": "دهان أكريليكي مطفي للجدران والأسقف الداخلية المحضرة.",
      "en": "Matt acrylic paint for clean, prepared interior walls and ceilings."
    },
    "requirements": [
      [
        "Classe de brillance",
        "فئة اللمعان",
        "Gloss class",
        "Classe mat à mesurer"
      ],
      [
        "Résistance à l’abrasion humide",
        "مقاومة الفرك الرطب",
        "Wet scrub resistance",
        "Classe 1 à 5 à définir"
      ],
      [
        "Pouvoir couvrant",
        "قدرة التغطية",
        "Hiding power",
        "Pouvoir couvrant à tester"
      ],
      [
        "Séchage et recouvrement",
        "الجفاف وإعادة الطلاء",
        "Drying and recoating",
        "Temps de recouvrement"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable product technology",
        "Finition intérieure mate"
      ],
      [
        "Usage d’un produit comparable",
        "استخدام منتج مقارن",
        "Comparable product application",
        "Murs et plafonds"
      ],
      [
        "Classe ou propriété tierce documentée",
        "فئة أو خاصية موثقة لدى منتج آخر",
        "Documented third-party class or property",
        "Classe de frottement chez comparables"
      ]
    ]
  },
  {
    "code": "PAINT-INT-S",
    "group": "paint-interior",
    "standard": "EN 13300",
    "intro": {
      "fr": "Peinture acrylique satinée pour murs intérieurs à entretien régulier.",
      "ar": "دهان أكريليكي ساتان للجدران الداخلية التي تحتاج تنظيفاً دورياً.",
      "en": "Satin acrylic coating for interior walls requiring regular maintenance."
    },
    "requirements": [
      [
        "Classe de brillance",
        "فئة اللمعان",
        "Gloss class",
        "Classe satin à établir"
      ],
      [
        "Résistance à l’abrasion humide",
        "مقاومة الفرك الرطب",
        "Wet scrub resistance",
        "Essai EN ISO 11998"
      ],
      [
        "Pouvoir couvrant",
        "قدرة التغطية",
        "Hiding power",
        "Essai de contraste"
      ],
      [
        "Séchage et recouvrement",
        "الجفاف وإعادة الطلاء",
        "Drying and recoating",
        "Séchage selon température"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable product technology",
        "Finition satinée"
      ],
      [
        "Usage d’un produit comparable",
        "استخدام منتج مقارن",
        "Comparable product application",
        "Murs intérieurs entretenus"
      ],
      [
        "Classe ou propriété tierce documentée",
        "فئة أو خاصية موثقة لدى منتج آخر",
        "Documented third-party class or property",
        "Frottement humide classifié chez tiers"
      ]
    ]
  },
  {
    "code": "PAINT-INT-WA",
    "group": "paint-interior",
    "standard": "EN 13300 / EN ISO 11998",
    "intro": {
      "fr": "Peinture lessivable haute résistance dont la classe d’abrasion humide reste à vérifier.",
      "ar": "دهان قابل للغسل عالي التحمل يتطلب إثبات مقاومة الفرك الرطب.",
      "en": "High-durability washable paint requiring actual wet scrub classification."
    },
    "requirements": [
      [
        "Résistance à l’abrasion humide",
        "مقاومة الفرك الرطب",
        "Wet scrub resistance",
        "Classe FENEK par essai EN ISO 11998"
      ],
      [
        "Classe de brillance",
        "فئة اللمعان",
        "Gloss class",
        "Classe de brillance"
      ],
      [
        "Pouvoir couvrant",
        "قدرة التغطية",
        "Hiding power",
        "Pouvoir couvrant"
      ],
      [
        "Séchage et recouvrement",
        "الجفاف وإعادة الطلاء",
        "Drying and recoating",
        "Aptitude au nettoyage après cure"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable product technology",
        "Peinture intérieure lessivable"
      ],
      [
        "Usage d’un produit comparable",
        "استخدام منتج مقارن",
        "Comparable product application",
        "Murs à entretien fréquent"
      ],
      [
        "Classe ou propriété tierce documentée",
        "فئة أو خاصية موثقة لدى منتج آخر",
        "Documented third-party class or property",
        "Classe 1 déclarée chez un comparable, pas FENEK"
      ]
    ]
  },
  {
    "code": "PAINT-PRIM-A",
    "group": "paint-primer",
    "standard": "EN ISO 4624",
    "intro": {
      "fr": "Primaire acrylique d’accrochage pour améliorer l’adhésion de la finition.",
      "ar": "أساس أكريليكي لتعزيز التصاق طلاء التشطيب.",
      "en": "Acrylic adhesion primer for improving the bonding of a compatible finish."
    },
    "requirements": [
      [
        "Adhérence au support",
        "الالتصاق بالسطح",
        "Bond to substrate",
        "Essai EN ISO 4624"
      ],
      [
        "Compatibilité des finitions",
        "توافق الطلاءات",
        "Topcoat compatibility",
        "Compatibilité primaire/finition"
      ],
      [
        "Pénétration et fixation",
        "اختراق وتثبيت السطح",
        "Penetration and consolidation",
        "Imprégnation à vérifier"
      ],
      [
        "Séchage et recouvrement",
        "الجفاف وإعادة الطلاء",
        "Drying and recoating",
        "Séchage à déclarer"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable product technology",
        "Primaire d’accrochage"
      ],
      [
        "Usage d’un produit comparable",
        "استخدام منتج مقارن",
        "Comparable product application",
        "Sous-couche avant peinture"
      ],
      [
        "Classe ou propriété tierce documentée",
        "فئة أو خاصية موثقة لدى منتج آخر",
        "Documented third-party class or property",
        "Contrôle d’adhérence"
      ]
    ]
  },
  {
    "code": "PAINT-PRIM-FX",
    "group": "paint-primer",
    "standard": "EN ISO 4624",
    "intro": {
      "fr": "Fixateur de fond pour supports minéraux légèrement pulvérulents et absorbants.",
      "ar": "مثبت للأسطح المعدنية الماصة والضعيفة نسبياً قبل الطلاء.",
      "en": "Penetrating fixative for mildly friable, absorbent mineral substrates before painting."
    },
    "requirements": [
      [
        "Pénétration et fixation",
        "اختراق وتثبيت السطح",
        "Penetration and consolidation",
        "Pénétration à mesurer"
      ],
      [
        "Adhérence au support",
        "الالتصاق بالسطح",
        "Bond to substrate",
        "Cohésion à vérifier"
      ],
      [
        "Compatibilité des finitions",
        "توافق الطلاءات",
        "Topcoat compatibility",
        "Système de finition adapté"
      ],
      [
        "Séchage et recouvrement",
        "الجفاف وإعادة الطلاء",
        "Drying and recoating",
        "Temps de séchage"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable product technology",
        "Fixateur pénétrant"
      ],
      [
        "Usage d’un produit comparable",
        "استخدام منتج مقارن",
        "Comparable product application",
        "Enduit absorbant"
      ],
      [
        "Classe ou propriété tierce documentée",
        "فئة أو خاصية موثقة لدى منتج آخر",
        "Documented third-party class or property",
        "Consolidation des fonds"
      ]
    ]
  },
  {
    "code": "PAINT-SOL-A",
    "group": "paint-floor",
    "standard": "EN 1504-2 si protection béton / ISO 2812-3",
    "intro": {
      "fr": "Peinture de sol pour locaux à trafic léger, dont l’usure et l’adhérence doivent être testées.",
      "ar": "دهان أرضيات للاستعمال الخفيف مع اختبار مقاومة التآكل والالتصاق.",
      "en": "Floor paint for light-use premises, requiring verified wear and bond performance."
    },
    "requirements": [
      [
        "Résistance à l’usure",
        "مقاومة التآكل",
        "Wear resistance",
        "Essai selon usage"
      ],
      [
        "Adhérence au support",
        "الالتصاق بالسطح",
        "Bond to substrate",
        "Adhérence au béton"
      ],
      [
        "Résistance chimique",
        "المقاومة الكيميائية",
        "Chemical resistance",
        "Résistance à l’eau"
      ],
      [
        "Résistance à la glissance",
        "مقاومة الانزلاق",
        "Slip resistance",
        "Essai glissance"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable product technology",
        "Peinture de sol en phase aqueuse"
      ],
      [
        "Usage d’un produit comparable",
        "استخدام منتج مقارن",
        "Comparable product application",
        "Locaux et passages légers"
      ],
      [
        "Classe ou propriété tierce documentée",
        "فئة أو خاصية موثقة لدى منتج آخر",
        "Documented third-party class or property",
        "Tenue mécanique selon produit"
      ]
    ]
  },
  {
    "code": "PAINT-TXT-F",
    "group": "paint-exterior",
    "standard": "EN 1062-1 (si revêtement de façade)",
    "intro": {
      "fr": "Revêtement décoratif texturé fin pour support minéral cohésif et correctement préparé.",
      "ar": "طلاء زخرفي ناعم الملمس على سطح معدني محضر ومتماسك.",
      "en": "Fine textured decorative coating for sound, properly prepared mineral backgrounds."
    },
    "requirements": [
      [
        "Épaisseur du film E",
        "سماكة طبقة الطلاء E",
        "Dry film thickness E",
        "Épaisseur E à déclarer"
      ],
      [
        "Vieillissement UV et climatique",
        "مقاومة الأشعة والمناخ",
        "UV and weathering",
        "Usage extérieur/intérieur à préciser"
      ],
      [
        "Adhérence au support",
        "الالتصاق بالسطح",
        "Bond to substrate",
        "Essai sur support"
      ],
      [
        "Perméabilité eau liquide W",
        "نفاذية الماء W",
        "Liquid-water permeability W",
        "Classe W si façade"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable product technology",
        "Peinture texturée acrylique"
      ],
      [
        "Usage d’un produit comparable",
        "استخدام منتج مقارن",
        "Comparable product application",
        "Décoration à relief fin"
      ],
      [
        "Classe ou propriété tierce documentée",
        "فئة أو خاصية موثقة لدى منتج آخر",
        "Documented third-party class or property",
        "Grain de finition"
      ]
    ]
  }
];
export const paintRecords=buildOtherRecords(paintDefinitions);
