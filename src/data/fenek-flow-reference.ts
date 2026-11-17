import {buildOtherRecords,type OtherRaw} from './fenek-other-technical-core';
/** FLOW technical references are documentary controls, not measured FENEK properties. */
export const flowDefinitions:OtherRaw[]=[
  {
    "code": "FLOW-AC",
    "group": "flow-admixture",
    "standard": "EN 934-2:2009+A1:2012 — tableau 6",
    "intro": {
      "fr": "Accélérateur de prise pour béton sous contrôle de la compatibilité ciment-température.",
      "ar": "مسرع شك للخرسانة مع فحص توافقه مع الإسمنت والحرارة.",
      "en": "Set accelerator for concrete requiring cement and temperature trial batches."
    },
    "requirements": [
      [
        "Temps de prise",
        "زمن الشك",
        "Setting time",
        "Essai EN 480-2 par rapport au témoin"
      ],
      [
        "Résistance mécanique",
        "المقاومة الميكانيكية",
        "Mechanical strength",
        "Essai à jeune âge EN 12390-3"
      ],
      [
        "Compatibilité avec le ciment",
        "التوافق مع الإسمنت",
        "Cement compatibility",
        "Comparaison par type de ciment"
      ],
      [
        "Teneur en ions chlorure",
        "محتوى أيونات الكلوريد",
        "Chloride ion content",
        "Déclaration EN 934-1"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable technology",
        "Accélération de prise"
      ],
      [
        "Domaine d’usage comparé",
        "مجال استخدام مقارن",
        "Comparable use",
        "Bétonnage rapide"
      ],
      [
        "Paramètre suivi sur des comparables",
        "معيار متابعة في منتجات مقارنة",
        "Comparable test parameter",
        "Temps de début de prise"
      ]
    ]
  },
  {
    "code": "FLOW-AE",
    "group": "flow-admixture",
    "standard": "EN 934-2:2009+A1:2012 — tableau 5",
    "intro": {
      "fr": "Entraîneur de microbulles d’air pour bétons exposés aux cycles de gel et dégel.",
      "ar": "مادة لحبس فقاعات الهواء الدقيقة لتحسين تحمل الخرسانة لدورات التجمد.",
      "en": "Air-entraining admixture for freeze-thaw exposure after controlled mixture design."
    },
    "requirements": [
      [
        "Teneur en air",
        "محتوى الهواء",
        "Air content",
        "≥ 2,5 % vol. vs béton témoin (tableau 5)"
      ],
      [
        "Résistance mécanique",
        "المقاومة الميكانيكية",
        "Mechanical strength",
        "Essai EN 12390-3"
      ],
      [
        "Consistance du béton",
        "قوام الخرسانة",
        "Concrete consistency",
        "Essai EN 12350"
      ],
      [
        "Compatibilité avec le ciment",
        "التوافق مع الإسمنت",
        "Cement compatibility",
        "Mesure d’air après transport"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable technology",
        "Entraînement de microbulles"
      ],
      [
        "Domaine d’usage comparé",
        "مجال استخدام مقارن",
        "Comparable use",
        "Béton exposé au gel"
      ],
      [
        "Paramètre suivi sur des comparables",
        "معيار متابعة في منتجات مقارنة",
        "Comparable test parameter",
        "Teneur en air à la livraison"
      ]
    ]
  },
  {
    "code": "FLOW-CI",
    "group": "flow-admixture",
    "standard": "EN 934-1 / EN 480-14 — inhibition de corrosion à qualifier",
    "intro": {
      "fr": "Inhibiteur de corrosion pour armatures exposées aux chlorures ou à la carbonatation.",
      "ar": "مثبط تآكل حديد التسليح في الخرسانة المعرضة للكلوريدات والكربنة.",
      "en": "Reinforcement corrosion inhibitor for concrete at risk of chlorides and carbonation."
    },
    "requirements": [
      [
        "Effet sur la corrosion des aciers",
        "التأثير على تآكل الحديد",
        "Steel corrosion response",
        "Étude comparative, catégorie non harmonisée"
      ],
      [
        "Teneur en ions chlorure",
        "محتوى أيونات الكلوريد",
        "Chloride ion content",
        "Déclaration de composition"
      ],
      [
        "Résistance mécanique",
        "المقاومة الميكانيكية",
        "Mechanical strength",
        "À comparer au béton témoin"
      ],
      [
        "Compatibilité avec le ciment",
        "التوافق مع الإسمنت",
        "Cement compatibility",
        "Vérification des armatures et ciment"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable technology",
        "Inhibiteur organique liquide"
      ],
      [
        "Domaine d’usage comparé",
        "مجال استخدام مقارن",
        "Comparable use",
        "Béton armé et mortier"
      ],
      [
        "Paramètre suivi sur des comparables",
        "معيار متابعة في منتجات مقارنة",
        "Comparable test parameter",
        "Corrosion accélérée comparative"
      ]
    ]
  },
  {
    "code": "FLOW-CURE",
    "group": "flow-cure",
    "standard": "ASTM C309 (si film de cure) / EN 13670",
    "intro": {
      "fr": "Produit de cure destiné à limiter l’évaporation d’eau dans le béton jeune.",
      "ar": "مادة معالجة تقلل تبخر الماء من الخرسانة الحديثة.",
      "en": "Curing compound to reduce early-age moisture loss from freshly finished concrete."
    },
    "requirements": [
      [
        "Rétention d’eau de cure",
        "حفظ الماء أثناء المعالجة",
        "Curing water retention",
        "Essai de rétention selon produit"
      ],
      [
        "Continuité du film",
        "استمرارية الطبقة",
        "Film continuity",
        "Contrôle visuel après pulvérisation"
      ],
      [
        "Compatibilité des finitions",
        "التوافق مع التشطيبات",
        "Finish compatibility",
        "Essai sur finitions ultérieures"
      ],
      [
        "Formulation et dosage",
        "التركيبة والجرعة",
        "Mix design and dose",
        "Consommation validée par surface"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable technology",
        "Film protecteur de cure"
      ],
      [
        "Domaine d’usage comparé",
        "مجال استخدام مقارن",
        "Comparable use",
        "Béton frais et récemment décoffré"
      ],
      [
        "Paramètre suivi sur des comparables",
        "معيار متابعة في منتجات مقارنة",
        "Comparable test parameter",
        "Pulvérisation de surface"
      ]
    ]
  },
  {
    "code": "FLOW-LAT",
    "group": "flow-latex",
    "standard": "EN 1542 — adjuvant latex d’adhérence à qualifier",
    "intro": {
      "fr": "Dispersion latex pour barbotines d’accrochage et mortiers ciment modifiés.",
      "ar": "مستحلب لاتكس لطبقات الربط ومونة الإسمنت المعدلة.",
      "en": "Latex bonding additive for cement slurries and polymer-modified mortars."
    },
    "requirements": [
      [
        "Adhérence du mortier au support",
        "التصاق المونة بالسطح",
        "Mortar bond to substrate",
        "Essai d’arrachement sur support"
      ],
      [
        "Résistance mécanique",
        "المقاومة الميكانيكية",
        "Mechanical strength",
        "Essai de mortier modifié"
      ],
      [
        "Formulation et dosage",
        "التركيبة والجرعة",
        "Mix design and dose",
        "Rapport eau-latex-ciment à définir"
      ],
      [
        "Compatibilité avec le ciment",
        "التوافق مع الإسمنت",
        "Cement compatibility",
        "Fenêtre d’adhérence à contrôler"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable technology",
        "Dispersion polymère"
      ],
      [
        "Domaine d’usage comparé",
        "مجال استخدام مقارن",
        "Comparable use",
        "Pont d’adhérence cimentaire"
      ],
      [
        "Paramètre suivi sur des comparables",
        "معيار متابعة في منتجات مقارنة",
        "Comparable test parameter",
        "Résistance du mortier"
      ]
    ]
  },
  {
    "code": "FLOW-RT",
    "group": "flow-admixture",
    "standard": "EN 934-2:2009+A1:2012 — tableau 8",
    "intro": {
      "fr": "Retardateur de prise pour faciliter le transport et la mise en place du béton.",
      "ar": "مؤخر شك لتسهيل نقل الخرسانة وصبها.",
      "en": "Set-retarding admixture to extend concrete placing time through qualified trials."
    },
    "requirements": [
      [
        "Temps de prise",
        "زمن الشك",
        "Setting time",
        "Essai EN 480-2 vs témoin"
      ],
      [
        "Résistance mécanique",
        "المقاومة الميكانيكية",
        "Mechanical strength",
        "Contrôle à 28 jours"
      ],
      [
        "Maintien d’ouvrabilité",
        "الحفاظ على التشغيلية",
        "Workability retention",
        "Contrôle pendant transport"
      ],
      [
        "Compatibilité avec le ciment",
        "التوافق مع الإسمنت",
        "Cement compatibility",
        "Essai avec ciment réel"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable technology",
        "Retard de prise"
      ],
      [
        "Domaine d’usage comparé",
        "مجال استخدام مقارن",
        "Comparable use",
        "Bétonnage par temps chaud"
      ],
      [
        "Paramètre suivi sur des comparables",
        "معيار متابعة في منتجات مقارنة",
        "Comparable test parameter",
        "Maintien du temps utile"
      ]
    ]
  },
  {
    "code": "FLOW-SP-HR",
    "group": "flow-admixture",
    "standard": "EN 934-2:2009+A1:2012 — tableaux 3.1/3.2",
    "intro": {
      "fr": "Superplastifiant haut réducteur d’eau pour béton fluide à faible rapport eau/ciment.",
      "ar": "ملدن فائق عالي التخفيض للماء للخرسانة عالية الانسياب.",
      "en": "High-range water-reducing superplasticizer for flowable and low-water concrete."
    },
    "requirements": [
      [
        "Réduction d’eau",
        "تخفيض ماء الخلط",
        "Water reduction",
        "≥ 12 % vs témoin (si classe tableau 3)"
      ],
      [
        "Consistance du béton",
        "قوام الخرسانة",
        "Concrete consistency",
        "EN 12350-2/-5"
      ],
      [
        "Résistance mécanique",
        "المقاومة الميكانيكية",
        "Mechanical strength",
        "EN 12390-3"
      ],
      [
        "Compatibilité avec le ciment",
        "التوافق مع الإسمنت",
        "Cement compatibility",
        "Essais de gâchage"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable technology",
        "Superplastifiant liquide"
      ],
      [
        "Domaine d’usage comparé",
        "مجال استخدام مقارن",
        "Comparable use",
        "Béton pompable à haute performance"
      ],
      [
        "Paramètre suivi sur des comparables",
        "معيار متابعة في منتجات مقارنة",
        "Comparable test parameter",
        "Ouvrabilité et réduction d’eau"
      ]
    ]
  },
  {
    "code": "FLOW-SP-PF",
    "group": "flow-admixture",
    "standard": "EN 934-2:2009+A1:2012 — tableau 3 + essais précoces",
    "intro": {
      "fr": "Superplastifiant de préfabrication pour réduction d’eau et résistances au jeune âge.",
      "ar": "ملدن فائق للخرسانة مسبقة الصنع ورفع المقاومة المبكرة.",
      "en": "Precast-focused superplasticizer requiring early-age strength and water reduction trials."
    },
    "requirements": [
      [
        "Réduction d’eau",
        "تخفيض ماء الخلط",
        "Water reduction",
        "≥ 12 % si classement tableau 3"
      ],
      [
        "Résistance mécanique",
        "المقاومة الميكانيكية",
        "Mechanical strength",
        "Essai au jeune âge de décoffrage"
      ],
      [
        "Consistance du béton",
        "قوام الخرسانة",
        "Concrete consistency",
        "Essai au coulage"
      ],
      [
        "Compatibilité avec le ciment",
        "التوافق مع الإسمنت",
        "Cement compatibility",
        "Température de cure à mesurer"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable technology",
        "Superplastifiant haute efficacité"
      ],
      [
        "Domaine d’usage comparé",
        "مجال استخدام مقارن",
        "Comparable use",
        "Préfabrication et démoulage"
      ],
      [
        "Paramètre suivi sur des comparables",
        "معيار متابعة في منتجات مقارنة",
        "Comparable test parameter",
        "Résistance initiale"
      ]
    ]
  },
  {
    "code": "FLOW-SP-RT",
    "group": "flow-admixture",
    "standard": "EN 934-2:2009+A1:2012 — superplastifiant, maintien à qualifier",
    "intro": {
      "fr": "Superplastifiant de maintien d’ouvrabilité sans présumer un effet retardateur de prise.",
      "ar": "ملدن فائق للحفاظ على التشغيلية دون افتراض أنه مؤخر للشك.",
      "en": "Superplasticizer for workability retention, not automatically a set-retarding admixture."
    },
    "requirements": [
      [
        "Réduction d’eau",
        "تخفيض ماء الخلط",
        "Water reduction",
        "Classe tableau 3 à vérifier"
      ],
      [
        "Maintien d’ouvrabilité",
        "الحفاظ على التشغيلية",
        "Workability retention",
        "Essai EN 12350 dans le temps"
      ],
      [
        "Temps de prise",
        "زمن الشك",
        "Setting time",
        "Vérification distincte vs témoin"
      ],
      [
        "Résistance mécanique",
        "المقاومة الميكانيكية",
        "Mechanical strength",
        "Mesure à l’âge visé"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable technology",
        "Superplastifiant de maintien"
      ],
      [
        "Domaine d’usage comparé",
        "مجال استخدام مقارن",
        "Comparable use",
        "Béton transporté et pompé"
      ],
      [
        "Paramètre suivi sur des comparables",
        "معيار متابعة في منتجات مقارنة",
        "Comparable test parameter",
        "Consistance à délai donné"
      ]
    ]
  },
  {
    "code": "FLOW-VMA",
    "group": "flow-admixture",
    "standard": "EN 934-2:2009+A1:2012 — tableau 13",
    "intro": {
      "fr": "Modificateur de viscosité pour stabilité de bétons autoplaçants.",
      "ar": "معدل لزوجة لتحقيق ثبات الخرسانة ذاتية الدمك.",
      "en": "Viscosity modifying admixture intended for segregation control in self-compacting concrete."
    },
    "requirements": [
      [
        "Résistance à la ségrégation",
        "مقاومة الانفصال الحبيبي",
        "Segregation resistance",
        "EN 12350-11"
      ],
      [
        "Viscosité du mélange",
        "لزوجة الخليط",
        "Mixture viscosity",
        "EN 12350-8/-9"
      ],
      [
        "Résistance mécanique",
        "المقاومة الميكانيكية",
        "Mechanical strength",
        "EN 12390-3"
      ],
      [
        "Teneur en air",
        "محتوى الهواء",
        "Air content",
        "EN 12350-7"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable technology",
        "Modificateur de viscosité"
      ],
      [
        "Domaine d’usage comparé",
        "مجال استخدام مقارن",
        "Comparable use",
        "Béton autoplaçant"
      ],
      [
        "Paramètre suivi sur des comparables",
        "معيار متابعة في منتجات مقارنة",
        "Comparable test parameter",
        "Ségrégation au tamis"
      ]
    ]
  },
  {
    "code": "FLOW-WP",
    "group": "flow-admixture",
    "standard": "EN 934-2:2009+A1:2012 — tableau 9",
    "intro": {
      "fr": "Hydrofuge de masse pour réduire l’absorption capillaire des bétons et mortiers.",
      "ar": "مانع امتصاص ماء للخرسانة والمونة من الداخل.",
      "en": "Integral water-resisting admixture for reducing capillary absorption in cementitious mixes."
    },
    "requirements": [
      [
        "Absorption capillaire",
        "الامتصاص الشعري",
        "Capillary absorption",
        "Essai comparatif tableau 9"
      ],
      [
        "Résistance mécanique",
        "المقاومة الميكانيكية",
        "Mechanical strength",
        "Comparaison témoin"
      ],
      [
        "Consistance du béton",
        "قوام الخرسانة",
        "Concrete consistency",
        "Essai béton frais"
      ],
      [
        "Formulation et dosage",
        "التركيبة والجرعة",
        "Mix design and dose",
        "Dosage selon porosité"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable technology",
        "Adjuvant hydrofuge de masse"
      ],
      [
        "Domaine d’usage comparé",
        "مجال استخدام مقارن",
        "Comparable use",
        "Béton et mortier"
      ],
      [
        "Paramètre suivi sur des comparables",
        "معيار متابعة في منتجات مقارنة",
        "Comparable test parameter",
        "Absorption capillaire"
      ]
    ]
  },
  {
    "code": "FLOW-WR-N",
    "group": "flow-admixture",
    "standard": "EN 934-2:2009+A1:2012 — tableau 2",
    "intro": {
      "fr": "Plastifiant réducteur d’eau classique pour béton à meilleure ouvrabilité.",
      "ar": "ملدن مخفض للماء بدرجة عادية لتحسين تشغيلية الخرسانة.",
      "en": "Conventional water-reducing plasticizer for improved concrete workability."
    },
    "requirements": [
      [
        "Réduction d’eau",
        "تخفيض ماء الخلط",
        "Water reduction",
        "≥ 5 % vs béton témoin (tableau 2)"
      ],
      [
        "Résistance mécanique",
        "المقاومة الميكانيكية",
        "Mechanical strength",
        "EN 12390-3"
      ],
      [
        "Consistance du béton",
        "قوام الخرسانة",
        "Concrete consistency",
        "EN 12350-2/-5"
      ],
      [
        "Teneur en ions chlorure",
        "محتوى أيونات الكلوريد",
        "Chloride ion content",
        "EN 934-1"
      ]
    ],
    "family": [
      [
        "Technologie d’un produit comparable",
        "تقنية منتج مقارن",
        "Comparable technology",
        "Plastifiant réducteur d’eau"
      ],
      [
        "Domaine d’usage comparé",
        "مجال استخدام مقارن",
        "Comparable use",
        "Béton courant"
      ],
      [
        "Paramètre suivi sur des comparables",
        "معيار متابعة في منتجات مقارنة",
        "Comparable test parameter",
        "Gâchées comparatives"
      ]
    ]
  }
];
export const flowRecords=buildOtherRecords(flowDefinitions);
