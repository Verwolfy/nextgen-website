import type {Lang} from './site';
import type {ReferenceMetric} from './fenek-c1t-reference';
import {c2tes1Copy} from './fenek-c2tes1-reference';

// Documentary class criteria and third-party benchmarks are not FENEK laboratory results.
export type BondRemainingRecord={
 code:string;short:string;group:string;standard:string;
 requirements:ReferenceMetric[];family:ReferenceMetric[];
 copy:Record<Lang,typeof c2tes1Copy.fr>;
};
const definitions=[
  {
    "code": "BOND-CG2WA",
    "short": "CG2WA",
    "group": "grout",
    "standard": "EN 13888-1:2022",
    "requirements": [
      {
        "key": "abrasion-base",
        "kind": "norme",
        "label": {
          "fr": "Abrasion de base CG1",
          "ar": "البري الأساسي CG1",
          "en": "Base CG1 abrasion"
        },
        "value": "≤ 2 000 mm³"
      },
      {
        "key": "flex-sec",
        "kind": "norme",
        "label": {
          "fr": "Flexion à sec",
          "ar": "الانحناء الجاف",
          "en": "Dry flexural strength"
        },
        "value": "≥ 2,5 N/mm²"
      },
      {
        "key": "flex-gel",
        "kind": "norme",
        "label": {
          "fr": "Flexion gel/dégel",
          "ar": "الانحناء بعد التجمد",
          "en": "Freeze-thaw flexural strength"
        },
        "value": "≥ 2,5 N/mm²"
      },
      {
        "key": "comp-sec",
        "kind": "norme",
        "label": {
          "fr": "Compression à sec",
          "ar": "الضغط الجاف",
          "en": "Dry compression"
        },
        "value": "≥ 15 N/mm²"
      },
      {
        "key": "comp-gel",
        "kind": "norme",
        "label": {
          "fr": "Compression gel/dégel",
          "ar": "الضغط بعد التجمد",
          "en": "Freeze-thaw compression"
        },
        "value": "≥ 15 N/mm²"
      },
      {
        "key": "shrink",
        "kind": "norme",
        "label": {
          "fr": "Retrait",
          "ar": "الانكماش",
          "en": "Shrinkage"
        },
        "value": "≤ 3 mm/m"
      },
      {
        "key": "water30-base",
        "kind": "norme",
        "label": {
          "fr": "Absorption 30 min de base",
          "ar": "امتصاص 30 دقيقة الأساسي",
          "en": "Basic 30 min absorption"
        },
        "value": "≤ 5 g"
      },
      {
        "key": "water240-base",
        "kind": "norme",
        "label": {
          "fr": "Absorption 240 min de base",
          "ar": "امتصاص 240 دقيقة الأساسي",
          "en": "Basic 240 min absorption"
        },
        "value": "≤ 10 g"
      },
      {
        "key": "abrasion-a",
        "kind": "norme",
        "label": {
          "fr": "Abrasion améliorée A",
          "ar": "تحسين البري A",
          "en": "Additional abrasion A"
        },
        "value": "≤ 1 000 mm³"
      },
      {
        "key": "water30-w",
        "kind": "norme",
        "label": {
          "fr": "Absorption réduite 30 min W",
          "ar": "تقليل امتصاص 30 دقيقة W",
          "en": "Reduced 30 min absorption W"
        },
        "value": "≤ 2 g"
      },
      {
        "key": "water240-w",
        "kind": "norme",
        "label": {
          "fr": "Absorption réduite 240 min W",
          "ar": "تقليل امتصاص 240 دقيقة W",
          "en": "Reduced 240 min absorption W"
        },
        "value": "≤ 5 g"
      }
    ],
    "family": [
      {
        "key": "sika",
        "kind": "famille",
        "label": {
          "fr": "Largeur de joints Sika CG2WA",
          "ar": "عرض فواصل سيكا",
          "en": "Sika CG2WA joint width"
        },
        "value": "1–8 mm"
      },
      {
        "key": "mapei",
        "kind": "famille",
        "label": {
          "fr": "Dosage d’un comparable Mapei CG2FWA",
          "ar": "ماء خلط مابي CG2FWA",
          "en": "Mapei CG2FWA mixing ratio"
        },
        "value": "21–23 % eau"
      },
      {
        "key": "weber",
        "kind": "famille",
        "label": {
          "fr": "Largeur d’un comparable Weber CG2WA",
          "ar": "عرض فواصل ويبر",
          "en": "Weber CG2WA joint width"
        },
        "value": "1–20 mm"
      }
    ],
    "copy": {
      "fr": {
        "pageTitle": "FENEK-BOND CG2WA | Joint cimentaire amélioré à abrasion renforcée et absorption réduite",
        "metaDescription": "Joint cimentaire amélioré à abrasion renforcée et absorption réduite. Référence de la gamme BOND. EN 13888-1:2022",
        "sheetTitle": "Fiche produit — FENEK-BOND CG2WA",
        "lead": "Joint cimentaire amélioré à abrasion renforcée et absorption réduite. Référence de la gamme BOND.",
        "techTitle": "Critères de classe et contrôles — EN 13888-1:2022",
        "familyTitle": "Repères comparatifs de formulations tierces",
        "usesTitle": "Applications selon système",
        "substratesTitle": "Préparation et supports",
        "consumptionTitle": "Paramètres comparatifs documentés",
        "comparisonTitle": "Produits liés dans la gamme",
        "comparisonNote": "Les classes ne sont pas interchangeables : choisir le système selon les contraintes du chantier.",
        "benefits": [
          "Joint cimentaire amélioré à abrasion renforcée et absorption réduite",
          "Abrasion de base CG1: ≤ 2 000 mm³",
          "Le procédé et les paramètres de gâchage dépendent de la fiche de formulation."
        ],
        "uses": [
          "Joint cimentaire amélioré à abrasion renforcée et absorption réduite",
          "Garnir les joints après durcissement de la colle; retirer les excès et poussières.",
          "Respecter la largeur autorisée et laisser libres les joints de mouvement."
        ],
        "substrates": [
          "Garnir les joints après durcissement de la colle; retirer les excès et poussières.",
          "Respecter la largeur autorisée et laisser libres les joints de mouvement.",
          "Vérifier la compatibilité du support avec le dossier technique."
        ],
        "preparation": [
          "Garnir les joints après durcissement de la colle; retirer les excès et poussières.",
          "Respecter la largeur autorisée et laisser libres les joints de mouvement.",
          "Gâcher selon la fiche du produit livré, appliquer à la taloche caoutchouc et nettoyer sans délaver."
        ],
        "conditions": [
          "Gâcher selon la fiche du produit livré, appliquer à la taloche caoutchouc et nettoyer sans délaver.",
          "Respecter les délais de travail, la météo et la cure spécifiés par le fabricant.",
          "Contrôler la qualité du résultat avant remise en service."
        ],
        "safety": [
          "Porter gants, lunettes et protection respiratoire adaptée à la poussière de ciment.",
          "Prévenir les projections alcalines et garantir l’accès sécurisé au chantier.",
          "Ne pas rejeter mortier, laitance ni eaux de lavage dans les évacuations."
        ]
      },
      "ar": {
        "pageTitle": "FENEK-BOND CG2WA | مونة فواصل إسمنتية محسنة قليلة الامتصاص ومقاومة للبري",
        "metaDescription": "مونة فواصل إسمنتية محسنة قليلة الامتصاص ومقاومة للبري. مرجع من مجموعة BOND. EN 13888-1:2022",
        "sheetTitle": "بطاقة المنتج — FENEK-BOND CG2WA",
        "lead": "مونة فواصل إسمنتية محسنة قليلة الامتصاص ومقاومة للبري. مرجع من مجموعة BOND.",
        "techTitle": "متطلبات الفئة والفحوص — EN 13888-1:2022",
        "familyTitle": "مؤشرات مقارنة من منتجات أخرى",
        "usesTitle": "الاستخدامات بحسب النظام",
        "substratesTitle": "السطح والتحضير",
        "consumptionTitle": "بيانات مقارنة موثقة",
        "comparisonTitle": "منتجات مرتبطة في المجموعة",
        "comparisonNote": "لا يمكن استبدال فئة بأخرى دون فحص ظروف المشروع.",
        "benefits": [
          "مونة فواصل إسمنتية محسنة قليلة الامتصاص ومقاومة للبري",
          "البري الأساسي CG1: ≤ 2 000 mm³",
          "تعتمد طريقة الاستخدام ونسبة الماء على النشرة الفنية للتركيبة."
        ],
        "uses": [
          "مونة فواصل إسمنتية محسنة قليلة الامتصاص ومقاومة للبري",
          "املأ الفواصل بعد تصلب اللاصق ونظف الغبار والبقايا.",
          "احترم العرض المسموح واترك فواصل الحركة مفتوحة."
        ],
        "substrates": [
          "املأ الفواصل بعد تصلب اللاصق ونظف الغبار والبقايا.",
          "احترم العرض المسموح واترك فواصل الحركة مفتوحة.",
          "تحقق من توافق السطح مع الملف الفني."
        ],
        "preparation": [
          "املأ الفواصل بعد تصلب اللاصق ونظف الغبار والبقايا.",
          "احترم العرض المسموح واترك فواصل الحركة مفتوحة.",
          "اخلط وفق نشرة المنتج المورّد وطبّق بالمالج المطاطي ونظف دون ماء زائد."
        ],
        "conditions": [
          "اخلط وفق نشرة المنتج المورّد وطبّق بالمالج المطاطي ونظف دون ماء زائد.",
          "اتبع زمن العمل والطقس والمعالجة المحددة من المصنع.",
          "افحص الجودة قبل إعادة الاستخدام."
        ],
        "safety": [
          "استعمل القفازات والنظارات ووسيلة حماية من غبار الإسمنت.",
          "تجنب رشاشات المونة القلوية وأمّن الوصول إلى منطقة العمل.",
          "لا تصرف المونة أو مياه الغسل إلى المجاري."
        ]
      },
      "en": {
        "pageTitle": "FENEK-BOND CG2WA | Improved low-absorption, high-abrasion cementitious grout",
        "metaDescription": "Improved low-absorption, high-abrasion cementitious grout. Part of the BOND range. EN 13888-1:2022",
        "sheetTitle": "Product sheet — FENEK-BOND CG2WA",
        "lead": "Improved low-absorption, high-abrasion cementitious grout. Part of the BOND range.",
        "techTitle": "Class criteria and checks — EN 13888-1:2022",
        "familyTitle": "Comparable third-party product benchmarks",
        "usesTitle": "Potential use by system",
        "substratesTitle": "Substrates and preparation",
        "consumptionTitle": "Documented comparative parameters",
        "comparisonTitle": "Related range references",
        "comparisonNote": "Classes are not interchangeable; select the system to project conditions.",
        "benefits": [
          "Improved low-absorption, high-abrasion cementitious grout",
          "Base CG1 abrasion: ≤ 2 000 mm³",
          "Working method and mixing ratio depend on the actual formulation sheet."
        ],
        "uses": [
          "Improved low-absorption, high-abrasion cementitious grout",
          "Wait for tile adhesive to cure and clean all joints.",
          "Check permissible joint width and preserve movement joints."
        ],
        "substrates": [
          "Wait for tile adhesive to cure and clean all joints.",
          "Check permissible joint width and preserve movement joints.",
          "Check substrate compatibility with technical documentation."
        ],
        "preparation": [
          "Wait for tile adhesive to cure and clean all joints.",
          "Check permissible joint width and preserve movement joints.",
          "Mix as specified for the supplied grout, pack with rubber float and clean without washout."
        ],
        "conditions": [
          "Mix as specified for the supplied grout, pack with rubber float and clean without washout.",
          "Observe the actual working time, weather restrictions and curing schedule.",
          "Verify the installation before returning to service."
        ],
        "safety": [
          "Wear gloves, eye protection and suitable respiratory dust protection.",
          "Prevent alkaline splashes and maintain safe site access.",
          "Keep mortar, slurry and wash water out of drains."
        ]
      }
    }
  },
  {
    "code": "BOND-CT-C25-F5",
    "short": "CT-C25-F5",
    "group": "screed",
    "standard": "EN 13813:2002",
    "requirements": [
      {
        "key": "c",
        "kind": "norme",
        "label": {
          "fr": "Résistance en compression C25",
          "ar": "مقاومة الضغط C25",
          "en": "Compressive strength C25"
        },
        "value": "≥ 25 N/mm²"
      },
      {
        "key": "f",
        "kind": "norme",
        "label": {
          "fr": "Résistance en flexion F5",
          "ar": "مقاومة الانحناء F5",
          "en": "Flexural strength F5"
        },
        "value": "≥ 5 N/mm²"
      }
    ],
    "family": [
      {
        "key": "sika",
        "kind": "famille",
        "label": {
          "fr": "Classe d’un ragréage Sika",
          "ar": "فئة منتج تسوية سيكا",
          "en": "Sika leveller grade"
        },
        "value": "CT-C25-F5"
      },
      {
        "key": "mapei",
        "kind": "famille",
        "label": {
          "fr": "Eau d’un ragréage Mapei",
          "ar": "نسبة الماء لمنتج مابي",
          "en": "Mapei leveller mixing water"
        },
        "value": "17–19 %"
      },
      {
        "key": "ardex",
        "kind": "famille",
        "label": {
          "fr": "Ragréages ARDEX",
          "ar": "منتجات التسوية من أردكس",
          "en": "ARDEX levellers"
        },
        "value": "Épaisseur selon produit"
      }
    ],
    "copy": {
      "fr": {
        "pageTitle": "FENEK-BOND CT-C25-F5 | Ragréage de sol cimentaire autolissant CT-C25-F5",
        "metaDescription": "Ragréage de sol cimentaire autolissant CT-C25-F5. Référence de la gamme BOND. EN 13813:2002",
        "sheetTitle": "Fiche produit — FENEK-BOND CT-C25-F5",
        "lead": "Ragréage de sol cimentaire autolissant CT-C25-F5. Référence de la gamme BOND.",
        "techTitle": "Critères de classe et contrôles — EN 13813:2002",
        "familyTitle": "Repères comparatifs de formulations tierces",
        "usesTitle": "Applications selon système",
        "substratesTitle": "Préparation et supports",
        "consumptionTitle": "Paramètres comparatifs documentés",
        "comparisonTitle": "Produits liés dans la gamme",
        "comparisonNote": "Les classes ne sont pas interchangeables : choisir le système selon les contraintes du chantier.",
        "benefits": [
          "Ragréage de sol cimentaire autolissant CT-C25-F5",
          "Résistance en compression C25: ≥ 25 N/mm²",
          "Le procédé et les paramètres de gâchage dépendent de la fiche de formulation."
        ],
        "uses": [
          "Ragréage de sol cimentaire autolissant CT-C25-F5",
          "Vérifier planéité, humidité et cohésion de la chape; préparer le primaire.",
          "Respecter les joints et traiter les fissures avant application."
        ],
        "substrates": [
          "Vérifier planéité, humidité et cohésion de la chape; préparer le primaire.",
          "Respecter les joints et traiter les fissures avant application.",
          "Vérifier la compatibilité du support avec le dossier technique."
        ],
        "preparation": [
          "Vérifier planéité, humidité et cohésion de la chape; préparer le primaire.",
          "Respecter les joints et traiter les fissures avant application.",
          "Verser sans interruption et laisser sécher selon la documentation du produit livré."
        ],
        "conditions": [
          "Verser sans interruption et laisser sécher selon la documentation du produit livré.",
          "Respecter les délais de travail, la météo et la cure spécifiés par le fabricant.",
          "Contrôler la qualité du résultat avant remise en service."
        ],
        "safety": [
          "Porter gants, lunettes et protection respiratoire adaptée à la poussière de ciment.",
          "Prévenir les projections alcalines et garantir l’accès sécurisé au chantier.",
          "Ne pas rejeter mortier, laitance ni eaux de lavage dans les évacuations."
        ]
      },
      "ar": {
        "pageTitle": "FENEK-BOND CT-C25-F5 | مونة إسمنتية ذاتية التسوية للأرضيات CT-C25-F5",
        "metaDescription": "مونة إسمنتية ذاتية التسوية للأرضيات CT-C25-F5. مرجع من مجموعة BOND. EN 13813:2002",
        "sheetTitle": "بطاقة المنتج — FENEK-BOND CT-C25-F5",
        "lead": "مونة إسمنتية ذاتية التسوية للأرضيات CT-C25-F5. مرجع من مجموعة BOND.",
        "techTitle": "متطلبات الفئة والفحوص — EN 13813:2002",
        "familyTitle": "مؤشرات مقارنة من منتجات أخرى",
        "usesTitle": "الاستخدامات بحسب النظام",
        "substratesTitle": "السطح والتحضير",
        "consumptionTitle": "بيانات مقارنة موثقة",
        "comparisonTitle": "منتجات مرتبطة في المجموعة",
        "comparisonNote": "لا يمكن استبدال فئة بأخرى دون فحص ظروف المشروع.",
        "benefits": [
          "مونة إسمنتية ذاتية التسوية للأرضيات CT-C25-F5",
          "مقاومة الضغط C25: ≥ 25 N/mm²",
          "تعتمد طريقة الاستخدام ونسبة الماء على النشرة الفنية للتركيبة."
        ],
        "uses": [
          "مونة إسمنتية ذاتية التسوية للأرضيات CT-C25-F5",
          "افحص استواء ورطوبة وتماسك الأرضية وجهز البرايمر.",
          "احفظ الفواصل وعالج الشقوق قبل الصب."
        ],
        "substrates": [
          "افحص استواء ورطوبة وتماسك الأرضية وجهز البرايمر.",
          "احفظ الفواصل وعالج الشقوق قبل الصب.",
          "تحقق من توافق السطح مع الملف الفني."
        ],
        "preparation": [
          "افحص استواء ورطوبة وتماسك الأرضية وجهز البرايمر.",
          "احفظ الفواصل وعالج الشقوق قبل الصب.",
          "صب باستمرار واترك السطح حتى الجفاف وفق نشرة المنتج المورّد."
        ],
        "conditions": [
          "صب باستمرار واترك السطح حتى الجفاف وفق نشرة المنتج المورّد.",
          "اتبع زمن العمل والطقس والمعالجة المحددة من المصنع.",
          "افحص الجودة قبل إعادة الاستخدام."
        ],
        "safety": [
          "استعمل القفازات والنظارات ووسيلة حماية من غبار الإسمنت.",
          "تجنب رشاشات المونة القلوية وأمّن الوصول إلى منطقة العمل.",
          "لا تصرف المونة أو مياه الغسل إلى المجاري."
        ]
      },
      "en": {
        "pageTitle": "FENEK-BOND CT-C25-F5 | CT-C25-F5 cementitious self-levelling floor compound",
        "metaDescription": "CT-C25-F5 cementitious self-levelling floor compound. Part of the BOND range. EN 13813:2002",
        "sheetTitle": "Product sheet — FENEK-BOND CT-C25-F5",
        "lead": "CT-C25-F5 cementitious self-levelling floor compound. Part of the BOND range.",
        "techTitle": "Class criteria and checks — EN 13813:2002",
        "familyTitle": "Comparable third-party product benchmarks",
        "usesTitle": "Potential use by system",
        "substratesTitle": "Substrates and preparation",
        "consumptionTitle": "Documented comparative parameters",
        "comparisonTitle": "Related range references",
        "comparisonNote": "Classes are not interchangeable; select the system to project conditions.",
        "benefits": [
          "CT-C25-F5 cementitious self-levelling floor compound",
          "Compressive strength C25: ≥ 25 N/mm²",
          "Working method and mixing ratio depend on the actual formulation sheet."
        ],
        "uses": [
          "CT-C25-F5 cementitious self-levelling floor compound",
          "Check screed flatness, moisture and soundness; use specified primer.",
          "Respect movement joints and treat cracks before pouring."
        ],
        "substrates": [
          "Check screed flatness, moisture and soundness; use specified primer.",
          "Respect movement joints and treat cracks before pouring.",
          "Check substrate compatibility with technical documentation."
        ],
        "preparation": [
          "Check screed flatness, moisture and soundness; use specified primer.",
          "Respect movement joints and treat cracks before pouring.",
          "Pour continuously and cure according to the supplied product sheet."
        ],
        "conditions": [
          "Pour continuously and cure according to the supplied product sheet.",
          "Observe the actual working time, weather restrictions and curing schedule.",
          "Verify the installation before returning to service."
        ],
        "safety": [
          "Wear gloves, eye protection and suitable respiratory dust protection.",
          "Prevent alkaline splashes and maintain safe site access.",
          "Keep mortar, slurry and wash water out of drains."
        ]
      }
    }
  },
  {
    "code": "BOND-GP-CSII",
    "short": "GP-CSII",
    "group": "render",
    "standard": "EN 998-1:2016",
    "requirements": [
      {
        "key": "csii",
        "kind": "norme",
        "label": {
          "fr": "Compression CSII à 28 jours",
          "ar": "ضغط CSII بعد 28 يوماً",
          "en": "28-day CSII compressive strength"
        },
        "value": "1,5–5,0 N/mm²"
      }
    ],
    "family": [
      {
        "key": "mapei",
        "kind": "famille",
        "label": {
          "fr": "Consommation Planitop 510",
          "ar": "استهلاك Planitop 510",
          "en": "Planitop 510 coverage"
        },
        "value": "≈ 1,3 kg/m²/mm"
      },
      {
        "key": "caparol",
        "kind": "famille",
        "label": {
          "fr": "Classification Caparol",
          "ar": "فئة كابارول",
          "en": "Caparol grade"
        },
        "value": "GP CS II"
      },
      {
        "key": "keim",
        "kind": "famille",
        "label": {
          "fr": "Classification KEIM",
          "ar": "فئة كايم",
          "en": "KEIM grade"
        },
        "value": "GP CS II"
      }
    ],
    "copy": {
      "fr": {
        "pageTitle": "FENEK-BOND GP-CSII | Enduit ciment d’usage courant de classe GP-CSII",
        "metaDescription": "Enduit ciment d’usage courant de classe GP-CSII. Référence de la gamme BOND. EN 998-1:2016",
        "sheetTitle": "Fiche produit — FENEK-BOND GP-CSII",
        "lead": "Enduit ciment d’usage courant de classe GP-CSII. Référence de la gamme BOND.",
        "techTitle": "Critères de classe et contrôles — EN 998-1:2016",
        "familyTitle": "Repères comparatifs de formulations tierces",
        "usesTitle": "Applications selon système",
        "substratesTitle": "Préparation et supports",
        "consumptionTitle": "Paramètres comparatifs documentés",
        "comparisonTitle": "Produits liés dans la gamme",
        "comparisonNote": "Les classes ne sont pas interchangeables : choisir le système selon les contraintes du chantier.",
        "benefits": [
          "Enduit ciment d’usage courant de classe GP-CSII",
          "Compression CSII à 28 jours: 1,5–5,0 N/mm²",
          "Le procédé et les paramètres de gâchage dépendent de la fiche de formulation."
        ],
        "uses": [
          "Enduit ciment d’usage courant de classe GP-CSII",
          "Contrôler résistance, propreté et absorption du support mural.",
          "Traiter les angles, interfaces et joints avant enduisage."
        ],
        "substrates": [
          "Contrôler résistance, propreté et absorption du support mural.",
          "Traiter les angles, interfaces et joints avant enduisage.",
          "Vérifier la compatibilité du support avec le dossier technique."
        ],
        "preparation": [
          "Contrôler résistance, propreté et absorption du support mural.",
          "Traiter les angles, interfaces et joints avant enduisage.",
          "Respecter l’eau, l’épaisseur de couche, la finition et la cure indiquées pour la formulation."
        ],
        "conditions": [
          "Respecter l’eau, l’épaisseur de couche, la finition et la cure indiquées pour la formulation.",
          "Respecter les délais de travail, la météo et la cure spécifiés par le fabricant.",
          "Contrôler la qualité du résultat avant remise en service."
        ],
        "safety": [
          "Porter gants, lunettes et protection respiratoire adaptée à la poussière de ciment.",
          "Prévenir les projections alcalines et garantir l’accès sécurisé au chantier.",
          "Ne pas rejeter mortier, laitance ni eaux de lavage dans les évacuations."
        ]
      },
      "ar": {
        "pageTitle": "FENEK-BOND GP-CSII | لياسة إسمنتية عامة من فئة GP-CSII",
        "metaDescription": "لياسة إسمنتية عامة من فئة GP-CSII. مرجع من مجموعة BOND. EN 998-1:2016",
        "sheetTitle": "بطاقة المنتج — FENEK-BOND GP-CSII",
        "lead": "لياسة إسمنتية عامة من فئة GP-CSII. مرجع من مجموعة BOND.",
        "techTitle": "متطلبات الفئة والفحوص — EN 998-1:2016",
        "familyTitle": "مؤشرات مقارنة من منتجات أخرى",
        "usesTitle": "الاستخدامات بحسب النظام",
        "substratesTitle": "السطح والتحضير",
        "consumptionTitle": "بيانات مقارنة موثقة",
        "comparisonTitle": "منتجات مرتبطة في المجموعة",
        "comparisonNote": "لا يمكن استبدال فئة بأخرى دون فحص ظروف المشروع.",
        "benefits": [
          "لياسة إسمنتية عامة من فئة GP-CSII",
          "ضغط CSII بعد 28 يوماً: 1,5–5,0 N/mm²",
          "تعتمد طريقة الاستخدام ونسبة الماء على النشرة الفنية للتركيبة."
        ],
        "uses": [
          "لياسة إسمنتية عامة من فئة GP-CSII",
          "افحص صلابة ونظافة وامتصاص الحائط.",
          "عالج الزوايا والفواصل والانتقالات قبل اللياسة."
        ],
        "substrates": [
          "افحص صلابة ونظافة وامتصاص الحائط.",
          "عالج الزوايا والفواصل والانتقالات قبل اللياسة.",
          "تحقق من توافق السطح مع الملف الفني."
        ],
        "preparation": [
          "افحص صلابة ونظافة وامتصاص الحائط.",
          "عالج الزوايا والفواصل والانتقالات قبل اللياسة.",
          "احترم الماء وسماكة الطبقة والتشطيب والمعالجة بحسب النشرة."
        ],
        "conditions": [
          "احترم الماء وسماكة الطبقة والتشطيب والمعالجة بحسب النشرة.",
          "اتبع زمن العمل والطقس والمعالجة المحددة من المصنع.",
          "افحص الجودة قبل إعادة الاستخدام."
        ],
        "safety": [
          "استعمل القفازات والنظارات ووسيلة حماية من غبار الإسمنت.",
          "تجنب رشاشات المونة القلوية وأمّن الوصول إلى منطقة العمل.",
          "لا تصرف المونة أو مياه الغسل إلى المجاري."
        ]
      },
      "en": {
        "pageTitle": "FENEK-BOND GP-CSII | GP-CSII general-purpose cement render",
        "metaDescription": "GP-CSII general-purpose cement render. Part of the BOND range. EN 998-1:2016",
        "sheetTitle": "Product sheet — FENEK-BOND GP-CSII",
        "lead": "GP-CSII general-purpose cement render. Part of the BOND range.",
        "techTitle": "Class criteria and checks — EN 998-1:2016",
        "familyTitle": "Comparable third-party product benchmarks",
        "usesTitle": "Potential use by system",
        "substratesTitle": "Substrates and preparation",
        "consumptionTitle": "Documented comparative parameters",
        "comparisonTitle": "Related range references",
        "comparisonNote": "Classes are not interchangeable; select the system to project conditions.",
        "benefits": [
          "GP-CSII general-purpose cement render",
          "28-day CSII compressive strength: 1,5–5,0 N/mm²",
          "Working method and mixing ratio depend on the actual formulation sheet."
        ],
        "uses": [
          "GP-CSII general-purpose cement render",
          "Check wall strength, cleanliness and suction.",
          "Treat corners, transitions and joints before rendering."
        ],
        "substrates": [
          "Check wall strength, cleanliness and suction.",
          "Treat corners, transitions and joints before rendering.",
          "Check substrate compatibility with technical documentation."
        ],
        "preparation": [
          "Check wall strength, cleanliness and suction.",
          "Treat corners, transitions and joints before rendering.",
          "Follow the actual water ratio, layer thickness, finish timing and curing requirements."
        ],
        "conditions": [
          "Follow the actual water ratio, layer thickness, finish timing and curing requirements.",
          "Observe the actual working time, weather restrictions and curing schedule.",
          "Verify the installation before returning to service."
        ],
        "safety": [
          "Wear gloves, eye protection and suitable respiratory dust protection.",
          "Prevent alkaline splashes and maintain safe site access.",
          "Keep mortar, slurry and wash water out of drains."
        ]
      }
    }
  },
  {
    "code": "BOND-GR-HR",
    "short": "GR-HR",
    "group": "bedding",
    "standard": "Essais de calage selon usage (EN 1504-6 si ancrage)",
    "requirements": [
      {
        "key": "grade",
        "kind": "norme",
        "label": {
          "fr": "Désignation GR-HR",
          "ar": "الرمز GR-HR",
          "en": "GR-HR designation"
        },
        "value": "Code catalogue non classant"
      },
      {
        "key": "flow",
        "kind": "norme",
        "label": {
          "fr": "Fluidité et stabilité",
          "ar": "السيولة والثبات",
          "en": "Flow and stability"
        },
        "value": "À qualifier sur formulation"
      },
      {
        "key": "strength",
        "kind": "norme",
        "label": {
          "fr": "Compression et transfert des charges",
          "ar": "مقاومة الضغط ونقل الأحمال",
          "en": "Strength and load transfer"
        },
        "value": "Selon dimensionnement"
      }
    ],
    "family": [
      {
        "key": "sika",
        "kind": "famille",
        "label": {
          "fr": "Eau du SikaGrout-212 ZA",
          "ar": "ماء SikaGrout-212 ZA",
          "en": "SikaGrout-212 ZA water"
        },
        "value": "4,0 L / 25 kg"
      },
      {
        "key": "mapei",
        "kind": "famille",
        "label": {
          "fr": "Consommation Mapefill GP ME",
          "ar": "استهلاك Mapefill GP ME",
          "en": "Mapefill GP ME coverage"
        },
        "value": "≈ 1,90 kg/m²/mm"
      },
      {
        "key": "weber",
        "kind": "famille",
        "label": {
          "fr": "Gamme des calages Weber",
          "ar": "مجموعة الحشو من ويبر",
          "en": "Weber precision grouts"
        },
        "value": "Consistance selon système"
      }
    ],
    "copy": {
      "fr": {
        "pageTitle": "FENEK-BOND GR-HR | Mortier de calage et de scellement, résistance à qualifier",
        "metaDescription": "Mortier de calage et de scellement, résistance à qualifier. Référence de la gamme BOND. Essais de calage selon usage (EN 1504-6 si ancrage)",
        "sheetTitle": "Fiche produit — FENEK-BOND GR-HR",
        "lead": "Mortier de calage et de scellement, résistance à qualifier. Référence de la gamme BOND.",
        "techTitle": "Critères de classe et contrôles — Essais de calage selon usage (EN 1504-6 si ancrage)",
        "familyTitle": "Repères comparatifs de formulations tierces",
        "usesTitle": "Applications selon système",
        "substratesTitle": "Préparation et supports",
        "consumptionTitle": "Paramètres comparatifs documentés",
        "comparisonTitle": "Produits liés dans la gamme",
        "comparisonNote": "Les classes ne sont pas interchangeables : choisir le système selon les contraintes du chantier.",
        "benefits": [
          "Mortier de calage et de scellement, résistance à qualifier",
          "Désignation GR-HR: Code catalogue non classant",
          "Le procédé et les paramètres de gâchage dépendent de la fiche de formulation."
        ],
        "uses": [
          "Mortier de calage et de scellement, résistance à qualifier",
          "Contrôler béton, platines, réservations et coffrage étanche.",
          "Faire valider charges, niveaux, épaisseurs et ancrages par l’ingénieur."
        ],
        "substrates": [
          "Contrôler béton, platines, réservations et coffrage étanche.",
          "Faire valider charges, niveaux, épaisseurs et ancrages par l’ingénieur.",
          "Vérifier la compatibilité du support avec le dossier technique."
        ],
        "preparation": [
          "Contrôler béton, platines, réservations et coffrage étanche.",
          "Faire valider charges, niveaux, épaisseurs et ancrages par l’ingénieur.",
          "Couler en continu selon la fluidité qualifiée, puis protéger de la dessiccation."
        ],
        "conditions": [
          "Couler en continu selon la fluidité qualifiée, puis protéger de la dessiccation.",
          "Respecter les délais de travail, la météo et la cure spécifiés par le fabricant.",
          "Contrôler la qualité du résultat avant remise en service."
        ],
        "safety": [
          "Porter gants, lunettes et protection respiratoire adaptée à la poussière de ciment.",
          "Prévenir les projections alcalines et garantir l’accès sécurisé au chantier.",
          "Ne pas rejeter mortier, laitance ni eaux de lavage dans les évacuations."
        ]
      },
      "ar": {
        "pageTitle": "FENEK-BOND GR-HR | مونة حشو وتثبيت للصفائح والمعدات مع مقاومة مطلوب التحقق منها",
        "metaDescription": "مونة حشو وتثبيت للصفائح والمعدات مع مقاومة مطلوب التحقق منها. مرجع من مجموعة BOND. Essais de calage selon usage (EN 1504-6 si ancrage)",
        "sheetTitle": "بطاقة المنتج — FENEK-BOND GR-HR",
        "lead": "مونة حشو وتثبيت للصفائح والمعدات مع مقاومة مطلوب التحقق منها. مرجع من مجموعة BOND.",
        "techTitle": "متطلبات الفئة والفحوص — Essais de calage selon usage (EN 1504-6 si ancrage)",
        "familyTitle": "مؤشرات مقارنة من منتجات أخرى",
        "usesTitle": "الاستخدامات بحسب النظام",
        "substratesTitle": "السطح والتحضير",
        "consumptionTitle": "بيانات مقارنة موثقة",
        "comparisonTitle": "منتجات مرتبطة في المجموعة",
        "comparisonNote": "لا يمكن استبدال فئة بأخرى دون فحص ظروف المشروع.",
        "benefits": [
          "مونة حشو وتثبيت للصفائح والمعدات مع مقاومة مطلوب التحقق منها",
          "الرمز GR-HR: Code catalogue non classant",
          "تعتمد طريقة الاستخدام ونسبة الماء على النشرة الفنية للتركيبة."
        ],
        "uses": [
          "مونة حشو وتثبيت للصفائح والمعدات مع مقاومة مطلوب التحقق منها",
          "افحص الخرسانة والصفائح والتجاويف والقوالب المحكمة.",
          "اعتمد الأحمال والمناسيب والسماكات والمراسي هندسياً."
        ],
        "substrates": [
          "افحص الخرسانة والصفائح والتجاويف والقوالب المحكمة.",
          "اعتمد الأحمال والمناسيب والسماكات والمراسي هندسياً.",
          "تحقق من توافق السطح مع الملف الفني."
        ],
        "preparation": [
          "افحص الخرسانة والصفائح والتجاويف والقوالب المحكمة.",
          "اعتمد الأحمال والمناسيب والسماكات والمراسي هندسياً.",
          "اصب باستمرار وفق السيولة المعتمدة واحم المونة من الجفاف."
        ],
        "conditions": [
          "اصب باستمرار وفق السيولة المعتمدة واحم المونة من الجفاف.",
          "اتبع زمن العمل والطقس والمعالجة المحددة من المصنع.",
          "افحص الجودة قبل إعادة الاستخدام."
        ],
        "safety": [
          "استعمل القفازات والنظارات ووسيلة حماية من غبار الإسمنت.",
          "تجنب رشاشات المونة القلوية وأمّن الوصول إلى منطقة العمل.",
          "لا تصرف المونة أو مياه الغسل إلى المجاري."
        ]
      },
      "en": {
        "pageTitle": "FENEK-BOND GR-HR | Precision bedding and grouting mortar requiring strength qualification",
        "metaDescription": "Precision bedding and grouting mortar requiring strength qualification. Part of the BOND range. Essais de calage selon usage (EN 1504-6 si ancrage)",
        "sheetTitle": "Product sheet — FENEK-BOND GR-HR",
        "lead": "Precision bedding and grouting mortar requiring strength qualification. Part of the BOND range.",
        "techTitle": "Class criteria and checks — Essais de calage selon usage (EN 1504-6 si ancrage)",
        "familyTitle": "Comparable third-party product benchmarks",
        "usesTitle": "Potential use by system",
        "substratesTitle": "Substrates and preparation",
        "consumptionTitle": "Documented comparative parameters",
        "comparisonTitle": "Related range references",
        "comparisonNote": "Classes are not interchangeable; select the system to project conditions.",
        "benefits": [
          "Precision bedding and grouting mortar requiring strength qualification",
          "GR-HR designation: Code catalogue non classant",
          "Working method and mixing ratio depend on the actual formulation sheet."
        ],
        "uses": [
          "Precision bedding and grouting mortar requiring strength qualification",
          "Inspect concrete, plates, voids and watertight formwork.",
          "Have loads, levels, grout depths and anchors engineered."
        ],
        "substrates": [
          "Inspect concrete, plates, voids and watertight formwork.",
          "Have loads, levels, grout depths and anchors engineered.",
          "Check substrate compatibility with technical documentation."
        ],
        "preparation": [
          "Inspect concrete, plates, voids and watertight formwork.",
          "Have loads, levels, grout depths and anchors engineered.",
          "Place continuously to approved flow consistency and protect against drying."
        ],
        "conditions": [
          "Place continuously to approved flow consistency and protect against drying.",
          "Observe the actual working time, weather restrictions and curing schedule.",
          "Verify the installation before returning to service."
        ],
        "safety": [
          "Wear gloves, eye protection and suitable respiratory dust protection.",
          "Prevent alkaline splashes and maintain safe site access.",
          "Keep mortar, slurry and wash water out of drains."
        ]
      }
    }
  },
  {
    "code": "BOND-M10",
    "short": "M10",
    "group": "masonry",
    "standard": "EN 998-2:2016",
    "requirements": [
      {
        "key": "compression",
        "kind": "norme",
        "label": {
          "fr": "Résistance en compression M10",
          "ar": "مقاومة الضغط M10",
          "en": "M10 compressive strength"
        },
        "value": "≥ 10 N/mm²"
      }
    ],
    "family": [
      {
        "key": "weber",
        "kind": "famille",
        "label": {
          "fr": "Classe du mortier Weber",
          "ar": "فئة مونة ويبر",
          "en": "Weber mortar class"
        },
        "value": "M10"
      },
      {
        "key": "lafac",
        "kind": "famille",
        "label": {
          "fr": "Classe du mortier Lafac",
          "ar": "فئة مونة لافاك",
          "en": "Lafac mortar class"
        },
        "value": "M10"
      },
      {
        "key": "suco",
        "kind": "famille",
        "label": {
          "fr": "Classe du mortier SUCO",
          "ar": "فئة مونة سوكو",
          "en": "SUCO mortar class"
        },
        "value": "M10"
      }
    ],
    "copy": {
      "fr": {
        "pageTitle": "FENEK-BOND M10 | Mortier de montage de maçonnerie de classe M10",
        "metaDescription": "Mortier de montage de maçonnerie de classe M10. Référence de la gamme BOND. EN 998-2:2016",
        "sheetTitle": "Fiche produit — FENEK-BOND M10",
        "lead": "Mortier de montage de maçonnerie de classe M10. Référence de la gamme BOND.",
        "techTitle": "Critères de classe et contrôles — EN 998-2:2016",
        "familyTitle": "Repères comparatifs de formulations tierces",
        "usesTitle": "Applications selon système",
        "substratesTitle": "Préparation et supports",
        "consumptionTitle": "Paramètres comparatifs documentés",
        "comparisonTitle": "Produits liés dans la gamme",
        "comparisonNote": "Les classes ne sont pas interchangeables : choisir le système selon les contraintes du chantier.",
        "benefits": [
          "Mortier de montage de maçonnerie de classe M10",
          "Résistance en compression M10: ≥ 10 N/mm²",
          "Le procédé et les paramètres de gâchage dépendent de la fiche de formulation."
        ],
        "uses": [
          "Mortier de montage de maçonnerie de classe M10",
          "Vérifier résistance et absorption des briques et blocs.",
          "Tracer les niveaux et préparer des lits d’assise propres."
        ],
        "substrates": [
          "Vérifier résistance et absorption des briques et blocs.",
          "Tracer les niveaux et préparer des lits d’assise propres.",
          "Vérifier la compatibilité du support avec le dossier technique."
        ],
        "preparation": [
          "Vérifier résistance et absorption des briques et blocs.",
          "Tracer les niveaux et préparer des lits d’assise propres.",
          "Gâcher selon la fiche, monter les rangs à joints réguliers et protéger la maçonnerie fraîche."
        ],
        "conditions": [
          "Gâcher selon la fiche, monter les rangs à joints réguliers et protéger la maçonnerie fraîche.",
          "Respecter les délais de travail, la météo et la cure spécifiés par le fabricant.",
          "Contrôler la qualité du résultat avant remise en service."
        ],
        "safety": [
          "Porter gants, lunettes et protection respiratoire adaptée à la poussière de ciment.",
          "Prévenir les projections alcalines et garantir l’accès sécurisé au chantier.",
          "Ne pas rejeter mortier, laitance ni eaux de lavage dans les évacuations."
        ]
      },
      "ar": {
        "pageTitle": "FENEK-BOND M10 | مونة بناء من فئة M10",
        "metaDescription": "مونة بناء من فئة M10. مرجع من مجموعة BOND. EN 998-2:2016",
        "sheetTitle": "بطاقة المنتج — FENEK-BOND M10",
        "lead": "مونة بناء من فئة M10. مرجع من مجموعة BOND.",
        "techTitle": "متطلبات الفئة والفحوص — EN 998-2:2016",
        "familyTitle": "مؤشرات مقارنة من منتجات أخرى",
        "usesTitle": "الاستخدامات بحسب النظام",
        "substratesTitle": "السطح والتحضير",
        "consumptionTitle": "بيانات مقارنة موثقة",
        "comparisonTitle": "منتجات مرتبطة في المجموعة",
        "comparisonNote": "لا يمكن استبدال فئة بأخرى دون فحص ظروف المشروع.",
        "benefits": [
          "مونة بناء من فئة M10",
          "مقاومة الضغط M10: ≥ 10 N/mm²",
          "تعتمد طريقة الاستخدام ونسبة الماء على النشرة الفنية للتركيبة."
        ],
        "uses": [
          "مونة بناء من فئة M10",
          "افحص مقاومة وامتصاص الطوب والبلوك.",
          "حدد المناسيب وجهز مداميك نظيفة."
        ],
        "substrates": [
          "افحص مقاومة وامتصاص الطوب والبلوك.",
          "حدد المناسيب وجهز مداميك نظيفة.",
          "تحقق من توافق السطح مع الملف الفني."
        ],
        "preparation": [
          "افحص مقاومة وامتصاص الطوب والبلوك.",
          "حدد المناسيب وجهز مداميك نظيفة.",
          "اخلط حسب النشرة وابنِ بفواصل منتظمة واحم الجدران الحديثة."
        ],
        "conditions": [
          "اخلط حسب النشرة وابنِ بفواصل منتظمة واحم الجدران الحديثة.",
          "اتبع زمن العمل والطقس والمعالجة المحددة من المصنع.",
          "افحص الجودة قبل إعادة الاستخدام."
        ],
        "safety": [
          "استعمل القفازات والنظارات ووسيلة حماية من غبار الإسمنت.",
          "تجنب رشاشات المونة القلوية وأمّن الوصول إلى منطقة العمل.",
          "لا تصرف المونة أو مياه الغسل إلى المجاري."
        ]
      },
      "en": {
        "pageTitle": "FENEK-BOND M10 | M10-class masonry mortar",
        "metaDescription": "M10-class masonry mortar. Part of the BOND range. EN 998-2:2016",
        "sheetTitle": "Product sheet — FENEK-BOND M10",
        "lead": "M10-class masonry mortar. Part of the BOND range.",
        "techTitle": "Class criteria and checks — EN 998-2:2016",
        "familyTitle": "Comparable third-party product benchmarks",
        "usesTitle": "Potential use by system",
        "substratesTitle": "Substrates and preparation",
        "consumptionTitle": "Documented comparative parameters",
        "comparisonTitle": "Related range references",
        "comparisonNote": "Classes are not interchangeable; select the system to project conditions.",
        "benefits": [
          "M10-class masonry mortar",
          "M10 compressive strength: ≥ 10 N/mm²",
          "Working method and mixing ratio depend on the actual formulation sheet."
        ],
        "uses": [
          "M10-class masonry mortar",
          "Check block or brick strength and suction.",
          "Set levels and prepare clean bearing beds."
        ],
        "substrates": [
          "Check block or brick strength and suction.",
          "Set levels and prepare clean bearing beds.",
          "Check substrate compatibility with technical documentation."
        ],
        "preparation": [
          "Check block or brick strength and suction.",
          "Set levels and prepare clean bearing beds.",
          "Mix to the actual sheet, build consistent joints and protect new masonry."
        ],
        "conditions": [
          "Mix to the actual sheet, build consistent joints and protect new masonry.",
          "Observe the actual working time, weather restrictions and curing schedule.",
          "Verify the installation before returning to service."
        ],
        "safety": [
          "Wear gloves, eye protection and suitable respiratory dust protection.",
          "Prevent alkaline splashes and maintain safe site access.",
          "Keep mortar, slurry and wash water out of drains."
        ]
      }
    }
  },
  {
    "code": "BOND-M5",
    "short": "M5",
    "group": "masonry",
    "standard": "EN 998-2:2016",
    "requirements": [
      {
        "key": "compression",
        "kind": "norme",
        "label": {
          "fr": "Résistance en compression M5",
          "ar": "مقاومة الضغط M5",
          "en": "M5 compressive strength"
        },
        "value": "≥ 5 N/mm²"
      }
    ],
    "family": [
      {
        "key": "baumit",
        "kind": "famille",
        "label": {
          "fr": "Joint d’assise cité par Baumit",
          "ar": "سماكة فاصل بوميت",
          "en": "Baumit bed joint"
        },
        "value": "10–12 mm"
      },
      {
        "key": "weber",
        "kind": "famille",
        "label": {
          "fr": "Classe du mortier Weber",
          "ar": "فئة مونة ويبر",
          "en": "Weber mortar class"
        },
        "value": "M5"
      },
      {
        "key": "lafac",
        "kind": "famille",
        "label": {
          "fr": "Classe du mortier Lafac",
          "ar": "فئة مونة لافاك",
          "en": "Lafac mortar class"
        },
        "value": "M5"
      }
    ],
    "copy": {
      "fr": {
        "pageTitle": "FENEK-BOND M5 | Mortier de montage courant de classe M5",
        "metaDescription": "Mortier de montage courant de classe M5. Référence de la gamme BOND. EN 998-2:2016",
        "sheetTitle": "Fiche produit — FENEK-BOND M5",
        "lead": "Mortier de montage courant de classe M5. Référence de la gamme BOND.",
        "techTitle": "Critères de classe et contrôles — EN 998-2:2016",
        "familyTitle": "Repères comparatifs de formulations tierces",
        "usesTitle": "Applications selon système",
        "substratesTitle": "Préparation et supports",
        "consumptionTitle": "Paramètres comparatifs documentés",
        "comparisonTitle": "Produits liés dans la gamme",
        "comparisonNote": "Les classes ne sont pas interchangeables : choisir le système selon les contraintes du chantier.",
        "benefits": [
          "Mortier de montage courant de classe M5",
          "Résistance en compression M5: ≥ 5 N/mm²",
          "Le procédé et les paramètres de gâchage dépendent de la fiche de formulation."
        ],
        "uses": [
          "Mortier de montage courant de classe M5",
          "Vérifier résistance et absorption des briques et blocs.",
          "Tracer les niveaux et préparer des lits d’assise propres."
        ],
        "substrates": [
          "Vérifier résistance et absorption des briques et blocs.",
          "Tracer les niveaux et préparer des lits d’assise propres.",
          "Vérifier la compatibilité du support avec le dossier technique."
        ],
        "preparation": [
          "Vérifier résistance et absorption des briques et blocs.",
          "Tracer les niveaux et préparer des lits d’assise propres.",
          "Gâcher selon la fiche, monter les rangs à joints réguliers et protéger la maçonnerie fraîche."
        ],
        "conditions": [
          "Gâcher selon la fiche, monter les rangs à joints réguliers et protéger la maçonnerie fraîche.",
          "Respecter les délais de travail, la météo et la cure spécifiés par le fabricant.",
          "Contrôler la qualité du résultat avant remise en service."
        ],
        "safety": [
          "Porter gants, lunettes et protection respiratoire adaptée à la poussière de ciment.",
          "Prévenir les projections alcalines et garantir l’accès sécurisé au chantier.",
          "Ne pas rejeter mortier, laitance ni eaux de lavage dans les évacuations."
        ]
      },
      "ar": {
        "pageTitle": "FENEK-BOND M5 | مونة بناء عادية من فئة M5",
        "metaDescription": "مونة بناء عادية من فئة M5. مرجع من مجموعة BOND. EN 998-2:2016",
        "sheetTitle": "بطاقة المنتج — FENEK-BOND M5",
        "lead": "مونة بناء عادية من فئة M5. مرجع من مجموعة BOND.",
        "techTitle": "متطلبات الفئة والفحوص — EN 998-2:2016",
        "familyTitle": "مؤشرات مقارنة من منتجات أخرى",
        "usesTitle": "الاستخدامات بحسب النظام",
        "substratesTitle": "السطح والتحضير",
        "consumptionTitle": "بيانات مقارنة موثقة",
        "comparisonTitle": "منتجات مرتبطة في المجموعة",
        "comparisonNote": "لا يمكن استبدال فئة بأخرى دون فحص ظروف المشروع.",
        "benefits": [
          "مونة بناء عادية من فئة M5",
          "مقاومة الضغط M5: ≥ 5 N/mm²",
          "تعتمد طريقة الاستخدام ونسبة الماء على النشرة الفنية للتركيبة."
        ],
        "uses": [
          "مونة بناء عادية من فئة M5",
          "افحص مقاومة وامتصاص الطوب والبلوك.",
          "حدد المناسيب وجهز مداميك نظيفة."
        ],
        "substrates": [
          "افحص مقاومة وامتصاص الطوب والبلوك.",
          "حدد المناسيب وجهز مداميك نظيفة.",
          "تحقق من توافق السطح مع الملف الفني."
        ],
        "preparation": [
          "افحص مقاومة وامتصاص الطوب والبلوك.",
          "حدد المناسيب وجهز مداميك نظيفة.",
          "اخلط حسب النشرة وابنِ بفواصل منتظمة واحم الجدران الحديثة."
        ],
        "conditions": [
          "اخلط حسب النشرة وابنِ بفواصل منتظمة واحم الجدران الحديثة.",
          "اتبع زمن العمل والطقس والمعالجة المحددة من المصنع.",
          "افحص الجودة قبل إعادة الاستخدام."
        ],
        "safety": [
          "استعمل القفازات والنظارات ووسيلة حماية من غبار الإسمنت.",
          "تجنب رشاشات المونة القلوية وأمّن الوصول إلى منطقة العمل.",
          "لا تصرف المونة أو مياه الغسل إلى المجاري."
        ]
      },
      "en": {
        "pageTitle": "FENEK-BOND M5 | M5-class general masonry mortar",
        "metaDescription": "M5-class general masonry mortar. Part of the BOND range. EN 998-2:2016",
        "sheetTitle": "Product sheet — FENEK-BOND M5",
        "lead": "M5-class general masonry mortar. Part of the BOND range.",
        "techTitle": "Class criteria and checks — EN 998-2:2016",
        "familyTitle": "Comparable third-party product benchmarks",
        "usesTitle": "Potential use by system",
        "substratesTitle": "Substrates and preparation",
        "consumptionTitle": "Documented comparative parameters",
        "comparisonTitle": "Related range references",
        "comparisonNote": "Classes are not interchangeable; select the system to project conditions.",
        "benefits": [
          "M5-class general masonry mortar",
          "M5 compressive strength: ≥ 5 N/mm²",
          "Working method and mixing ratio depend on the actual formulation sheet."
        ],
        "uses": [
          "M5-class general masonry mortar",
          "Check block or brick strength and suction.",
          "Set levels and prepare clean bearing beds."
        ],
        "substrates": [
          "Check block or brick strength and suction.",
          "Set levels and prepare clean bearing beds.",
          "Check substrate compatibility with technical documentation."
        ],
        "preparation": [
          "Check block or brick strength and suction.",
          "Set levels and prepare clean bearing beds.",
          "Mix to the actual sheet, build consistent joints and protect new masonry."
        ],
        "conditions": [
          "Mix to the actual sheet, build consistent joints and protect new masonry.",
          "Observe the actual working time, weather restrictions and curing schedule.",
          "Verify the installation before returning to service."
        ],
        "safety": [
          "Wear gloves, eye protection and suitable respiratory dust protection.",
          "Prevent alkaline splashes and maintain safe site access.",
          "Keep mortar, slurry and wash water out of drains."
        ]
      }
    }
  },
  {
    "code": "BOND-OC-CSIII",
    "short": "OC-CSIII",
    "group": "render",
    "standard": "EN 998-1:2016",
    "requirements": [
      {
        "key": "csiii",
        "kind": "norme",
        "label": {
          "fr": "Compression CSIII à 28 jours",
          "ar": "ضغط CSIII بعد 28 يوماً",
          "en": "28-day CSIII compressive strength"
        },
        "value": "3,5–7,5 N/mm²"
      }
    ],
    "family": [
      {
        "key": "ec",
        "kind": "famille",
        "label": {
          "fr": "Consommation Morcemdur EC (10 mm)",
          "ar": "استهلاك Morcemdur EC عند 10 مم",
          "en": "Morcemdur EC coverage at 10 mm"
        },
        "value": "≈ 18 kg/m²"
      },
      {
        "key": "ft",
        "kind": "famille",
        "label": {
          "fr": "Consommation Morcemdur FT",
          "ar": "استهلاك Morcemdur FT",
          "en": "Morcemdur FT coverage"
        },
        "value": "≈ 1,6 kg/m²/mm"
      },
      {
        "key": "piedra",
        "kind": "famille",
        "label": {
          "fr": "Classe Morcemdur Piedra",
          "ar": "فئة Morcemdur Piedra",
          "en": "Morcemdur Piedra class"
        },
        "value": "OC CSIII W2"
      }
    ],
    "copy": {
      "fr": {
        "pageTitle": "FENEK-BOND OC-CSIII | Enduit monocouche de façade OC-CSIII",
        "metaDescription": "Enduit monocouche de façade OC-CSIII. Référence de la gamme BOND. EN 998-1:2016",
        "sheetTitle": "Fiche produit — FENEK-BOND OC-CSIII",
        "lead": "Enduit monocouche de façade OC-CSIII. Référence de la gamme BOND.",
        "techTitle": "Critères de classe et contrôles — EN 998-1:2016",
        "familyTitle": "Repères comparatifs de formulations tierces",
        "usesTitle": "Applications selon système",
        "substratesTitle": "Préparation et supports",
        "consumptionTitle": "Paramètres comparatifs documentés",
        "comparisonTitle": "Produits liés dans la gamme",
        "comparisonNote": "Les classes ne sont pas interchangeables : choisir le système selon les contraintes du chantier.",
        "benefits": [
          "Enduit monocouche de façade OC-CSIII",
          "Compression CSIII à 28 jours: 3,5–7,5 N/mm²",
          "Le procédé et les paramètres de gâchage dépendent de la fiche de formulation."
        ],
        "uses": [
          "Enduit monocouche de façade OC-CSIII",
          "Contrôler résistance, propreté et absorption du support mural.",
          "Traiter les angles, interfaces et joints avant enduisage."
        ],
        "substrates": [
          "Contrôler résistance, propreté et absorption du support mural.",
          "Traiter les angles, interfaces et joints avant enduisage.",
          "Vérifier la compatibilité du support avec le dossier technique."
        ],
        "preparation": [
          "Contrôler résistance, propreté et absorption du support mural.",
          "Traiter les angles, interfaces et joints avant enduisage.",
          "Respecter l’eau, l’épaisseur de couche, la finition et la cure indiquées pour la formulation."
        ],
        "conditions": [
          "Respecter l’eau, l’épaisseur de couche, la finition et la cure indiquées pour la formulation.",
          "Respecter les délais de travail, la météo et la cure spécifiés par le fabricant.",
          "Contrôler la qualité du résultat avant remise en service."
        ],
        "safety": [
          "Porter gants, lunettes et protection respiratoire adaptée à la poussière de ciment.",
          "Prévenir les projections alcalines et garantir l’accès sécurisé au chantier.",
          "Ne pas rejeter mortier, laitance ni eaux de lavage dans les évacuations."
        ]
      },
      "ar": {
        "pageTitle": "FENEK-BOND OC-CSIII | لياسة واجهات بطبقة واحدة OC-CSIII",
        "metaDescription": "لياسة واجهات بطبقة واحدة OC-CSIII. مرجع من مجموعة BOND. EN 998-1:2016",
        "sheetTitle": "بطاقة المنتج — FENEK-BOND OC-CSIII",
        "lead": "لياسة واجهات بطبقة واحدة OC-CSIII. مرجع من مجموعة BOND.",
        "techTitle": "متطلبات الفئة والفحوص — EN 998-1:2016",
        "familyTitle": "مؤشرات مقارنة من منتجات أخرى",
        "usesTitle": "الاستخدامات بحسب النظام",
        "substratesTitle": "السطح والتحضير",
        "consumptionTitle": "بيانات مقارنة موثقة",
        "comparisonTitle": "منتجات مرتبطة في المجموعة",
        "comparisonNote": "لا يمكن استبدال فئة بأخرى دون فحص ظروف المشروع.",
        "benefits": [
          "لياسة واجهات بطبقة واحدة OC-CSIII",
          "ضغط CSIII بعد 28 يوماً: 3,5–7,5 N/mm²",
          "تعتمد طريقة الاستخدام ونسبة الماء على النشرة الفنية للتركيبة."
        ],
        "uses": [
          "لياسة واجهات بطبقة واحدة OC-CSIII",
          "افحص صلابة ونظافة وامتصاص الحائط.",
          "عالج الزوايا والفواصل والانتقالات قبل اللياسة."
        ],
        "substrates": [
          "افحص صلابة ونظافة وامتصاص الحائط.",
          "عالج الزوايا والفواصل والانتقالات قبل اللياسة.",
          "تحقق من توافق السطح مع الملف الفني."
        ],
        "preparation": [
          "افحص صلابة ونظافة وامتصاص الحائط.",
          "عالج الزوايا والفواصل والانتقالات قبل اللياسة.",
          "احترم الماء وسماكة الطبقة والتشطيب والمعالجة بحسب النشرة."
        ],
        "conditions": [
          "احترم الماء وسماكة الطبقة والتشطيب والمعالجة بحسب النشرة.",
          "اتبع زمن العمل والطقس والمعالجة المحددة من المصنع.",
          "افحص الجودة قبل إعادة الاستخدام."
        ],
        "safety": [
          "استعمل القفازات والنظارات ووسيلة حماية من غبار الإسمنت.",
          "تجنب رشاشات المونة القلوية وأمّن الوصول إلى منطقة العمل.",
          "لا تصرف المونة أو مياه الغسل إلى المجاري."
        ]
      },
      "en": {
        "pageTitle": "FENEK-BOND OC-CSIII | OC-CSIII one-coat exterior render",
        "metaDescription": "OC-CSIII one-coat exterior render. Part of the BOND range. EN 998-1:2016",
        "sheetTitle": "Product sheet — FENEK-BOND OC-CSIII",
        "lead": "OC-CSIII one-coat exterior render. Part of the BOND range.",
        "techTitle": "Class criteria and checks — EN 998-1:2016",
        "familyTitle": "Comparable third-party product benchmarks",
        "usesTitle": "Potential use by system",
        "substratesTitle": "Substrates and preparation",
        "consumptionTitle": "Documented comparative parameters",
        "comparisonTitle": "Related range references",
        "comparisonNote": "Classes are not interchangeable; select the system to project conditions.",
        "benefits": [
          "OC-CSIII one-coat exterior render",
          "28-day CSIII compressive strength: 3,5–7,5 N/mm²",
          "Working method and mixing ratio depend on the actual formulation sheet."
        ],
        "uses": [
          "OC-CSIII one-coat exterior render",
          "Check wall strength, cleanliness and suction.",
          "Treat corners, transitions and joints before rendering."
        ],
        "substrates": [
          "Check wall strength, cleanliness and suction.",
          "Treat corners, transitions and joints before rendering.",
          "Check substrate compatibility with technical documentation."
        ],
        "preparation": [
          "Check wall strength, cleanliness and suction.",
          "Treat corners, transitions and joints before rendering.",
          "Follow the actual water ratio, layer thickness, finish timing and curing requirements."
        ],
        "conditions": [
          "Follow the actual water ratio, layer thickness, finish timing and curing requirements.",
          "Observe the actual working time, weather restrictions and curing schedule.",
          "Verify the installation before returning to service."
        ],
        "safety": [
          "Wear gloves, eye protection and suitable respiratory dust protection.",
          "Prevent alkaline splashes and maintain safe site access.",
          "Keep mortar, slurry and wash water out of drains."
        ]
      }
    }
  },
  {
    "code": "BOND-R2",
    "short": "R2",
    "group": "repair",
    "standard": "EN 1504-3:2005",
    "requirements": [
      {
        "key": "compressive",
        "kind": "norme",
        "label": {
          "fr": "Résistance en compression R2",
          "ar": "مقاومة الضغط R2",
          "en": "R2 compressive strength"
        },
        "value": "≥ 15 MPa"
      },
      {
        "key": "bond",
        "kind": "norme",
        "label": {
          "fr": "Adhérence R2",
          "ar": "قوة الالتصاق R2",
          "en": "R2 bond strength"
        },
        "value": "≥ 0,8 MPa"
      },
      {
        "key": "chlorides",
        "kind": "norme",
        "label": {
          "fr": "Ions chlorure",
          "ar": "أيونات الكلوريد",
          "en": "Chloride ions"
        },
        "value": "≤ 0,05 %"
      }
    ],
    "family": [
      {
        "key": "sika",
        "kind": "famille",
        "label": {
          "fr": "Référence Sika",
          "ar": "مرجع سيكا",
          "en": "Sika comparable"
        },
        "value": "MonoTop-2020 R2"
      },
      {
        "key": "mapei",
        "kind": "famille",
        "label": {
          "fr": "Référence Mapei",
          "ar": "مرجع مابي",
          "en": "Mapei comparable"
        },
        "value": "Planitop Rasa & Ripara R2"
      },
      {
        "key": "emaco",
        "kind": "famille",
        "label": {
          "fr": "Référence SikaEmaco",
          "ar": "مرجع سيكا إيماكو",
          "en": "SikaEmaco comparable"
        },
        "value": "N 5200 R2"
      }
    ],
    "copy": {
      "fr": {
        "pageTitle": "FENEK-BOND R2 | Mortier de réparation non structurelle R2",
        "metaDescription": "Mortier de réparation non structurelle R2. Référence de la gamme BOND. EN 1504-3:2005",
        "sheetTitle": "Fiche produit — FENEK-BOND R2",
        "lead": "Mortier de réparation non structurelle R2. Référence de la gamme BOND.",
        "techTitle": "Critères de classe et contrôles — EN 1504-3:2005",
        "familyTitle": "Repères comparatifs de formulations tierces",
        "usesTitle": "Applications selon système",
        "substratesTitle": "Préparation et supports",
        "consumptionTitle": "Paramètres comparatifs documentés",
        "comparisonTitle": "Produits liés dans la gamme",
        "comparisonNote": "Les classes ne sont pas interchangeables : choisir le système selon les contraintes du chantier.",
        "benefits": [
          "Mortier de réparation non structurelle R2",
          "Résistance en compression R2: ≥ 15 MPa",
          "Le procédé et les paramètres de gâchage dépendent de la fiche de formulation."
        ],
        "uses": [
          "Mortier de réparation non structurelle R2",
          "Diagnostiquer les désordres et purger le béton non adhérent.",
          "Préparer les armatures, la rugosité et l’humidité selon le système de réparation."
        ],
        "substrates": [
          "Diagnostiquer les désordres et purger le béton non adhérent.",
          "Préparer les armatures, la rugosité et l’humidité selon le système de réparation.",
          "Vérifier la compatibilité du support avec le dossier technique."
        ],
        "preparation": [
          "Diagnostiquer les désordres et purger le béton non adhérent.",
          "Préparer les armatures, la rugosité et l’humidité selon le système de réparation.",
          "Appliquer dans l’épaisseur admise, compacter et assurer la cure avant remise en service."
        ],
        "conditions": [
          "Appliquer dans l’épaisseur admise, compacter et assurer la cure avant remise en service.",
          "Respecter les délais de travail, la météo et la cure spécifiés par le fabricant.",
          "Contrôler la qualité du résultat avant remise en service."
        ],
        "safety": [
          "Porter gants, lunettes et protection respiratoire adaptée à la poussière de ciment.",
          "Prévenir les projections alcalines et garantir l’accès sécurisé au chantier.",
          "Ne pas rejeter mortier, laitance ni eaux de lavage dans les évacuations."
        ]
      },
      "ar": {
        "pageTitle": "FENEK-BOND R2 | مونة إصلاح خرسانة غير إنشائي R2",
        "metaDescription": "مونة إصلاح خرسانة غير إنشائي R2. مرجع من مجموعة BOND. EN 1504-3:2005",
        "sheetTitle": "بطاقة المنتج — FENEK-BOND R2",
        "lead": "مونة إصلاح خرسانة غير إنشائي R2. مرجع من مجموعة BOND.",
        "techTitle": "متطلبات الفئة والفحوص — EN 1504-3:2005",
        "familyTitle": "مؤشرات مقارنة من منتجات أخرى",
        "usesTitle": "الاستخدامات بحسب النظام",
        "substratesTitle": "السطح والتحضير",
        "consumptionTitle": "بيانات مقارنة موثقة",
        "comparisonTitle": "منتجات مرتبطة في المجموعة",
        "comparisonNote": "لا يمكن استبدال فئة بأخرى دون فحص ظروف المشروع.",
        "benefits": [
          "مونة إصلاح خرسانة غير إنشائي R2",
          "مقاومة الضغط R2: ≥ 15 MPa",
          "تعتمد طريقة الاستخدام ونسبة الماء على النشرة الفنية للتركيبة."
        ],
        "uses": [
          "مونة إصلاح خرسانة غير إنشائي R2",
          "شخّص التلف وأزل الخرسانة الضعيفة.",
          "جهز حديد التسليح وخشونة ورطوبة السطح حسب نظام الإصلاح."
        ],
        "substrates": [
          "شخّص التلف وأزل الخرسانة الضعيفة.",
          "جهز حديد التسليح وخشونة ورطوبة السطح حسب نظام الإصلاح.",
          "تحقق من توافق السطح مع الملف الفني."
        ],
        "preparation": [
          "شخّص التلف وأزل الخرسانة الضعيفة.",
          "جهز حديد التسليح وخشونة ورطوبة السطح حسب نظام الإصلاح.",
          "طبق بسماكة معتمدة وادمك وعالج المونة قبل إعادة الخدمة."
        ],
        "conditions": [
          "طبق بسماكة معتمدة وادمك وعالج المونة قبل إعادة الخدمة.",
          "اتبع زمن العمل والطقس والمعالجة المحددة من المصنع.",
          "افحص الجودة قبل إعادة الاستخدام."
        ],
        "safety": [
          "استعمل القفازات والنظارات ووسيلة حماية من غبار الإسمنت.",
          "تجنب رشاشات المونة القلوية وأمّن الوصول إلى منطقة العمل.",
          "لا تصرف المونة أو مياه الغسل إلى المجاري."
        ]
      },
      "en": {
        "pageTitle": "FENEK-BOND R2 | R2 non-structural concrete repair mortar",
        "metaDescription": "R2 non-structural concrete repair mortar. Part of the BOND range. EN 1504-3:2005",
        "sheetTitle": "Product sheet — FENEK-BOND R2",
        "lead": "R2 non-structural concrete repair mortar. Part of the BOND range.",
        "techTitle": "Class criteria and checks — EN 1504-3:2005",
        "familyTitle": "Comparable third-party product benchmarks",
        "usesTitle": "Potential use by system",
        "substratesTitle": "Substrates and preparation",
        "consumptionTitle": "Documented comparative parameters",
        "comparisonTitle": "Related range references",
        "comparisonNote": "Classes are not interchangeable; select the system to project conditions.",
        "benefits": [
          "R2 non-structural concrete repair mortar",
          "R2 compressive strength: ≥ 15 MPa",
          "Working method and mixing ratio depend on the actual formulation sheet."
        ],
        "uses": [
          "R2 non-structural concrete repair mortar",
          "Diagnose defects and remove unsound concrete.",
          "Prepare reinforcement, texture and moisture per the repair system."
        ],
        "substrates": [
          "Diagnose defects and remove unsound concrete.",
          "Prepare reinforcement, texture and moisture per the repair system.",
          "Check substrate compatibility with technical documentation."
        ],
        "preparation": [
          "Diagnose defects and remove unsound concrete.",
          "Prepare reinforcement, texture and moisture per the repair system.",
          "Apply within permitted thickness, compact and cure before returning to service."
        ],
        "conditions": [
          "Apply within permitted thickness, compact and cure before returning to service.",
          "Observe the actual working time, weather restrictions and curing schedule.",
          "Verify the installation before returning to service."
        ],
        "safety": [
          "Wear gloves, eye protection and suitable respiratory dust protection.",
          "Prevent alkaline splashes and maintain safe site access.",
          "Keep mortar, slurry and wash water out of drains."
        ]
      }
    }
  },
  {
    "code": "BOND-R3",
    "short": "R3",
    "group": "repair",
    "standard": "EN 1504-3:2005",
    "requirements": [
      {
        "key": "compressive",
        "kind": "norme",
        "label": {
          "fr": "Résistance en compression R3",
          "ar": "مقاومة الضغط R3",
          "en": "R3 compressive strength"
        },
        "value": "≥ 25 MPa"
      },
      {
        "key": "bond",
        "kind": "norme",
        "label": {
          "fr": "Adhérence R3",
          "ar": "قوة الالتصاق R3",
          "en": "R3 bond strength"
        },
        "value": "≥ 1,5 MPa"
      },
      {
        "key": "modulus",
        "kind": "norme",
        "label": {
          "fr": "Module élastique R3",
          "ar": "معامل المرونة R3",
          "en": "R3 elastic modulus"
        },
        "value": "≥ 15 GPa"
      },
      {
        "key": "chlorides",
        "kind": "norme",
        "label": {
          "fr": "Ions chlorure",
          "ar": "أيونات الكلوريد",
          "en": "Chloride ions"
        },
        "value": "≤ 0,05 %"
      }
    ],
    "family": [
      {
        "key": "sika",
        "kind": "famille",
        "label": {
          "fr": "Référence Sika",
          "ar": "مرجع سيكا",
          "en": "Sika comparable"
        },
        "value": "MonoTop-615 R3"
      },
      {
        "key": "mapei",
        "kind": "famille",
        "label": {
          "fr": "Référence Mapei",
          "ar": "مرجع مابي",
          "en": "Mapei comparable"
        },
        "value": "Mapegrout T40 R3"
      },
      {
        "key": "puma",
        "kind": "famille",
        "label": {
          "fr": "Épaisseur Morcemrest C5 R3",
          "ar": "سماكة Morcemrest C5 R3",
          "en": "Morcemrest C5 R3 layer"
        },
        "value": "2–5 mm"
      }
    ],
    "copy": {
      "fr": {
        "pageTitle": "FENEK-BOND R3 | Mortier de réparation structurelle R3",
        "metaDescription": "Mortier de réparation structurelle R3. Référence de la gamme BOND. EN 1504-3:2005",
        "sheetTitle": "Fiche produit — FENEK-BOND R3",
        "lead": "Mortier de réparation structurelle R3. Référence de la gamme BOND.",
        "techTitle": "Critères de classe et contrôles — EN 1504-3:2005",
        "familyTitle": "Repères comparatifs de formulations tierces",
        "usesTitle": "Applications selon système",
        "substratesTitle": "Préparation et supports",
        "consumptionTitle": "Paramètres comparatifs documentés",
        "comparisonTitle": "Produits liés dans la gamme",
        "comparisonNote": "Les classes ne sont pas interchangeables : choisir le système selon les contraintes du chantier.",
        "benefits": [
          "Mortier de réparation structurelle R3",
          "Résistance en compression R3: ≥ 25 MPa",
          "Le procédé et les paramètres de gâchage dépendent de la fiche de formulation."
        ],
        "uses": [
          "Mortier de réparation structurelle R3",
          "Diagnostiquer les désordres et purger le béton non adhérent.",
          "Préparer les armatures, la rugosité et l’humidité selon le système de réparation."
        ],
        "substrates": [
          "Diagnostiquer les désordres et purger le béton non adhérent.",
          "Préparer les armatures, la rugosité et l’humidité selon le système de réparation.",
          "Vérifier la compatibilité du support avec le dossier technique."
        ],
        "preparation": [
          "Diagnostiquer les désordres et purger le béton non adhérent.",
          "Préparer les armatures, la rugosité et l’humidité selon le système de réparation.",
          "Appliquer dans l’épaisseur admise, compacter et assurer la cure avant remise en service."
        ],
        "conditions": [
          "Appliquer dans l’épaisseur admise, compacter et assurer la cure avant remise en service.",
          "Respecter les délais de travail, la météo et la cure spécifiés par le fabricant.",
          "Contrôler la qualité du résultat avant remise en service."
        ],
        "safety": [
          "Porter gants, lunettes et protection respiratoire adaptée à la poussière de ciment.",
          "Prévenir les projections alcalines et garantir l’accès sécurisé au chantier.",
          "Ne pas rejeter mortier, laitance ni eaux de lavage dans les évacuations."
        ]
      },
      "ar": {
        "pageTitle": "FENEK-BOND R3 | مونة إصلاح خرسانة إنشائي R3",
        "metaDescription": "مونة إصلاح خرسانة إنشائي R3. مرجع من مجموعة BOND. EN 1504-3:2005",
        "sheetTitle": "بطاقة المنتج — FENEK-BOND R3",
        "lead": "مونة إصلاح خرسانة إنشائي R3. مرجع من مجموعة BOND.",
        "techTitle": "متطلبات الفئة والفحوص — EN 1504-3:2005",
        "familyTitle": "مؤشرات مقارنة من منتجات أخرى",
        "usesTitle": "الاستخدامات بحسب النظام",
        "substratesTitle": "السطح والتحضير",
        "consumptionTitle": "بيانات مقارنة موثقة",
        "comparisonTitle": "منتجات مرتبطة في المجموعة",
        "comparisonNote": "لا يمكن استبدال فئة بأخرى دون فحص ظروف المشروع.",
        "benefits": [
          "مونة إصلاح خرسانة إنشائي R3",
          "مقاومة الضغط R3: ≥ 25 MPa",
          "تعتمد طريقة الاستخدام ونسبة الماء على النشرة الفنية للتركيبة."
        ],
        "uses": [
          "مونة إصلاح خرسانة إنشائي R3",
          "شخّص التلف وأزل الخرسانة الضعيفة.",
          "جهز حديد التسليح وخشونة ورطوبة السطح حسب نظام الإصلاح."
        ],
        "substrates": [
          "شخّص التلف وأزل الخرسانة الضعيفة.",
          "جهز حديد التسليح وخشونة ورطوبة السطح حسب نظام الإصلاح.",
          "تحقق من توافق السطح مع الملف الفني."
        ],
        "preparation": [
          "شخّص التلف وأزل الخرسانة الضعيفة.",
          "جهز حديد التسليح وخشونة ورطوبة السطح حسب نظام الإصلاح.",
          "طبق بسماكة معتمدة وادمك وعالج المونة قبل إعادة الخدمة."
        ],
        "conditions": [
          "طبق بسماكة معتمدة وادمك وعالج المونة قبل إعادة الخدمة.",
          "اتبع زمن العمل والطقس والمعالجة المحددة من المصنع.",
          "افحص الجودة قبل إعادة الاستخدام."
        ],
        "safety": [
          "استعمل القفازات والنظارات ووسيلة حماية من غبار الإسمنت.",
          "تجنب رشاشات المونة القلوية وأمّن الوصول إلى منطقة العمل.",
          "لا تصرف المونة أو مياه الغسل إلى المجاري."
        ]
      },
      "en": {
        "pageTitle": "FENEK-BOND R3 | R3 structural concrete repair mortar",
        "metaDescription": "R3 structural concrete repair mortar. Part of the BOND range. EN 1504-3:2005",
        "sheetTitle": "Product sheet — FENEK-BOND R3",
        "lead": "R3 structural concrete repair mortar. Part of the BOND range.",
        "techTitle": "Class criteria and checks — EN 1504-3:2005",
        "familyTitle": "Comparable third-party product benchmarks",
        "usesTitle": "Potential use by system",
        "substratesTitle": "Substrates and preparation",
        "consumptionTitle": "Documented comparative parameters",
        "comparisonTitle": "Related range references",
        "comparisonNote": "Classes are not interchangeable; select the system to project conditions.",
        "benefits": [
          "R3 structural concrete repair mortar",
          "R3 compressive strength: ≥ 25 MPa",
          "Working method and mixing ratio depend on the actual formulation sheet."
        ],
        "uses": [
          "R3 structural concrete repair mortar",
          "Diagnose defects and remove unsound concrete.",
          "Prepare reinforcement, texture and moisture per the repair system."
        ],
        "substrates": [
          "Diagnose defects and remove unsound concrete.",
          "Prepare reinforcement, texture and moisture per the repair system.",
          "Check substrate compatibility with technical documentation."
        ],
        "preparation": [
          "Diagnose defects and remove unsound concrete.",
          "Prepare reinforcement, texture and moisture per the repair system.",
          "Apply within permitted thickness, compact and cure before returning to service."
        ],
        "conditions": [
          "Apply within permitted thickness, compact and cure before returning to service.",
          "Observe the actual working time, weather restrictions and curing schedule.",
          "Verify the installation before returning to service."
        ],
        "safety": [
          "Wear gloves, eye protection and suitable respiratory dust protection.",
          "Prevent alkaline splashes and maintain safe site access.",
          "Keep mortar, slurry and wash water out of drains."
        ]
      }
    }
  },
  {
    "code": "BOND-R4",
    "short": "R4",
    "group": "repair",
    "standard": "EN 1504-3:2005",
    "requirements": [
      {
        "key": "compressive",
        "kind": "norme",
        "label": {
          "fr": "Résistance en compression R4",
          "ar": "مقاومة الضغط R4",
          "en": "R4 compressive strength"
        },
        "value": "≥ 45 MPa"
      },
      {
        "key": "bond",
        "kind": "norme",
        "label": {
          "fr": "Adhérence R4",
          "ar": "قوة الالتصاق R4",
          "en": "R4 bond strength"
        },
        "value": "≥ 2,0 MPa"
      },
      {
        "key": "modulus",
        "kind": "norme",
        "label": {
          "fr": "Module élastique R4",
          "ar": "معامل المرونة R4",
          "en": "R4 elastic modulus"
        },
        "value": "≥ 20 GPa"
      },
      {
        "key": "chlorides",
        "kind": "norme",
        "label": {
          "fr": "Ions chlorure",
          "ar": "أيونات الكلوريد",
          "en": "Chloride ions"
        },
        "value": "≤ 0,05 %"
      }
    ],
    "family": [
      {
        "key": "sika",
        "kind": "famille",
        "label": {
          "fr": "Référence Sika fibrée",
          "ar": "مرجع سيكا الليفي",
          "en": "Sika reinforced comparable"
        },
        "value": "MonoTop-412 N R4"
      },
      {
        "key": "mapei",
        "kind": "famille",
        "label": {
          "fr": "Référence Mapei fibrée",
          "ar": "مرجع مابي الليفي",
          "en": "Mapei reinforced comparable"
        },
        "value": "Mapegrout T60 R4"
      },
      {
        "key": "puma",
        "kind": "famille",
        "label": {
          "fr": "Conditionnement Morcemrest Repair",
          "ar": "عبوة Morcemrest Repair",
          "en": "Morcemrest Repair pack"
        },
        "value": "25 kg"
      },
      {
        "key": "weber",
        "kind": "famille",
        "label": {
          "fr": "Référence Weber",
          "ar": "مرجع ويبر",
          "en": "Weber comparable"
        },
        "value": "webercem R4 duo"
      }
    ],
    "copy": {
      "fr": {
        "pageTitle": "FENEK-BOND R4 | Mortier de réparation structurelle fibré thixotrope R4",
        "metaDescription": "Mortier de réparation structurelle fibré thixotrope R4. Référence de la gamme BOND. EN 1504-3:2005",
        "sheetTitle": "Fiche produit — FENEK-BOND R4",
        "lead": "Mortier de réparation structurelle fibré thixotrope R4. Référence de la gamme BOND.",
        "techTitle": "Critères de classe et contrôles — EN 1504-3:2005",
        "familyTitle": "Repères comparatifs de formulations tierces",
        "usesTitle": "Applications selon système",
        "substratesTitle": "Préparation et supports",
        "consumptionTitle": "Paramètres comparatifs documentés",
        "comparisonTitle": "Produits liés dans la gamme",
        "comparisonNote": "Les classes ne sont pas interchangeables : choisir le système selon les contraintes du chantier.",
        "benefits": [
          "Mortier de réparation structurelle fibré thixotrope R4",
          "Résistance en compression R4: ≥ 45 MPa",
          "Le procédé et les paramètres de gâchage dépendent de la fiche de formulation."
        ],
        "uses": [
          "Mortier de réparation structurelle fibré thixotrope R4",
          "Diagnostiquer les désordres et purger le béton non adhérent.",
          "Préparer les armatures, la rugosité et l’humidité selon le système de réparation."
        ],
        "substrates": [
          "Diagnostiquer les désordres et purger le béton non adhérent.",
          "Préparer les armatures, la rugosité et l’humidité selon le système de réparation.",
          "Vérifier la compatibilité du support avec le dossier technique."
        ],
        "preparation": [
          "Diagnostiquer les désordres et purger le béton non adhérent.",
          "Préparer les armatures, la rugosité et l’humidité selon le système de réparation.",
          "Appliquer dans l’épaisseur admise, compacter et assurer la cure avant remise en service."
        ],
        "conditions": [
          "Appliquer dans l’épaisseur admise, compacter et assurer la cure avant remise en service.",
          "Respecter les délais de travail, la météo et la cure spécifiés par le fabricant.",
          "Contrôler la qualité du résultat avant remise en service."
        ],
        "safety": [
          "Porter gants, lunettes et protection respiratoire adaptée à la poussière de ciment.",
          "Prévenir les projections alcalines et garantir l’accès sécurisé au chantier.",
          "Ne pas rejeter mortier, laitance ni eaux de lavage dans les évacuations."
        ]
      },
      "ar": {
        "pageTitle": "FENEK-BOND R4 | مونة إصلاح خرسانة إنشائي ليفية ثيكسوتروبية R4",
        "metaDescription": "مونة إصلاح خرسانة إنشائي ليفية ثيكسوتروبية R4. مرجع من مجموعة BOND. EN 1504-3:2005",
        "sheetTitle": "بطاقة المنتج — FENEK-BOND R4",
        "lead": "مونة إصلاح خرسانة إنشائي ليفية ثيكسوتروبية R4. مرجع من مجموعة BOND.",
        "techTitle": "متطلبات الفئة والفحوص — EN 1504-3:2005",
        "familyTitle": "مؤشرات مقارنة من منتجات أخرى",
        "usesTitle": "الاستخدامات بحسب النظام",
        "substratesTitle": "السطح والتحضير",
        "consumptionTitle": "بيانات مقارنة موثقة",
        "comparisonTitle": "منتجات مرتبطة في المجموعة",
        "comparisonNote": "لا يمكن استبدال فئة بأخرى دون فحص ظروف المشروع.",
        "benefits": [
          "مونة إصلاح خرسانة إنشائي ليفية ثيكسوتروبية R4",
          "مقاومة الضغط R4: ≥ 45 MPa",
          "تعتمد طريقة الاستخدام ونسبة الماء على النشرة الفنية للتركيبة."
        ],
        "uses": [
          "مونة إصلاح خرسانة إنشائي ليفية ثيكسوتروبية R4",
          "شخّص التلف وأزل الخرسانة الضعيفة.",
          "جهز حديد التسليح وخشونة ورطوبة السطح حسب نظام الإصلاح."
        ],
        "substrates": [
          "شخّص التلف وأزل الخرسانة الضعيفة.",
          "جهز حديد التسليح وخشونة ورطوبة السطح حسب نظام الإصلاح.",
          "تحقق من توافق السطح مع الملف الفني."
        ],
        "preparation": [
          "شخّص التلف وأزل الخرسانة الضعيفة.",
          "جهز حديد التسليح وخشونة ورطوبة السطح حسب نظام الإصلاح.",
          "طبق بسماكة معتمدة وادمك وعالج المونة قبل إعادة الخدمة."
        ],
        "conditions": [
          "طبق بسماكة معتمدة وادمك وعالج المونة قبل إعادة الخدمة.",
          "اتبع زمن العمل والطقس والمعالجة المحددة من المصنع.",
          "افحص الجودة قبل إعادة الاستخدام."
        ],
        "safety": [
          "استعمل القفازات والنظارات ووسيلة حماية من غبار الإسمنت.",
          "تجنب رشاشات المونة القلوية وأمّن الوصول إلى منطقة العمل.",
          "لا تصرف المونة أو مياه الغسل إلى المجاري."
        ]
      },
      "en": {
        "pageTitle": "FENEK-BOND R4 | R4 fibre-reinforced thixotropic structural repair mortar",
        "metaDescription": "R4 fibre-reinforced thixotropic structural repair mortar. Part of the BOND range. EN 1504-3:2005",
        "sheetTitle": "Product sheet — FENEK-BOND R4",
        "lead": "R4 fibre-reinforced thixotropic structural repair mortar. Part of the BOND range.",
        "techTitle": "Class criteria and checks — EN 1504-3:2005",
        "familyTitle": "Comparable third-party product benchmarks",
        "usesTitle": "Potential use by system",
        "substratesTitle": "Substrates and preparation",
        "consumptionTitle": "Documented comparative parameters",
        "comparisonTitle": "Related range references",
        "comparisonNote": "Classes are not interchangeable; select the system to project conditions.",
        "benefits": [
          "R4 fibre-reinforced thixotropic structural repair mortar",
          "R4 compressive strength: ≥ 45 MPa",
          "Working method and mixing ratio depend on the actual formulation sheet."
        ],
        "uses": [
          "R4 fibre-reinforced thixotropic structural repair mortar",
          "Diagnose defects and remove unsound concrete.",
          "Prepare reinforcement, texture and moisture per the repair system."
        ],
        "substrates": [
          "Diagnose defects and remove unsound concrete.",
          "Prepare reinforcement, texture and moisture per the repair system.",
          "Check substrate compatibility with technical documentation."
        ],
        "preparation": [
          "Diagnose defects and remove unsound concrete.",
          "Prepare reinforcement, texture and moisture per the repair system.",
          "Apply within permitted thickness, compact and cure before returning to service."
        ],
        "conditions": [
          "Apply within permitted thickness, compact and cure before returning to service.",
          "Observe the actual working time, weather restrictions and curing schedule.",
          "Verify the installation before returning to service."
        ],
        "safety": [
          "Wear gloves, eye protection and suitable respiratory dust protection.",
          "Prevent alkaline splashes and maintain safe site access.",
          "Keep mortar, slurry and wash water out of drains."
        ]
      }
    }
  }
];
export const bondRemainingRecords:Record<string,BondRemainingRecord>=Object.fromEntries(
 definitions.map(row=>[row.code,{...row,
  requirements:row.requirements as ReferenceMetric[],
  family:row.family as ReferenceMetric[],
  copy:{
    fr:{...c2tes1Copy.fr,...row.copy.fr},
    ar:{...c2tes1Copy.ar,...row.copy.ar},
    en:{...c2tes1Copy.en,...row.copy.en}
  } as Record<Lang,typeof c2tes1Copy.fr>
 }])
);
export const bondRemainingCodes=Object.keys(bondRemainingRecords);
