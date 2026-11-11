import type { Lang } from './site';

/**
 * Lot 127 — V3 product-by-product image QA, source: NEXTGEN_modes_emploi_V3.zip.
 * BROUILLON: trade illustrations only; never a certified FENEK TDS/SDS.
 * Only specifically reviewed references may use these images on the website.
 */
type Localized = Record<Lang,string>;
type ReviewStep = { title:Localized; description:Localized; image:number; icon:string };
export type ReviewedV3Guide = {
  code:string;
  slug:string;
  sprite:string;
  sha256:string;
  steps:ReviewStep[];
  status:'BROUILLON';
};
const l=(fr:string,ar:string,en:string):Localized=>({fr,ar,en});

const c1t:ReviewedV3Guide={
  code:'BOND-C1T',
  slug:'fenek-bond-c1t',
  sprite:'/images/application-v3/fenek-bond-c1t-steps.webp',
  sha256:'9ba666ddca06c036e4f84c19416b03ea5f75e51d2ea55129d3527d58a4e166e3',
  status:'BROUILLON',
  steps:[
    {image:1,icon:'brush',
      title:l('Nettoyer et vérifier le support','نظّف السطح وتأكد من سلامته واستوائه','Clean and inspect substrate'),
      description:l('Vérifier la cohésion et la planéité ; éliminer poussière et résidus.','فحص تماسك السطح واستوائه وإزالة الأتربة والبقايا.','Check soundness and flatness; remove dust and residues.')},
    {image:2,icon:'shield',
      title:l('Porter gants, lunettes et masque','ارتدِ القفازات والنظارات والكمامة','Wear gloves, goggles and dust mask'),
      description:l('Utiliser les EPI adaptés au produit et à sa FDS avant toute manipulation.','استعمال وسائل الوقاية المناسبة طبقًا لنشرة السلامة قبل الاستخدام.','Use suitable PPE in accordance with the approved safety sheet.')},
    {image:3,icon:'water',
      title:l('Ajouter l’eau selon la fiche technique','أضف الماء حسب النشرة الفنية','Measure water as specified'),
      description:l('Le dosage eau/poudre et la masse de référence restent à confirmer par la FT FENEK approuvée.','تحديد كمية الماء وكتلة المسحوق من النشرة الفنية المعتمدة فقط.','Use only water and powder quantities from an approved FENEK sheet.')},
    {image:4,icon:'clock',
      title:l('Laisser reposer puis remalaxer','اترك الخليط يرتاح ثم أعد الخلط','Rest and remix as specified'),
      description:l('Respecter un repos puis un nouveau malaxage uniquement si la procédure validée le prévoit.','اتباع مدة الاستراحة وإعادة الخلط إذا نصت النشرة المعتمدة على ذلك.','Allow a rest and remix only when required by the approved product method.')},
    {image:5,icon:'trowel',
      title:l('Étaler avec une spatule crantée','وزّع اللاصق بمالج مسنن','Spread with a notched trowel'),
      description:l('Adapter le peigne au carrelage et vérifier le transfert de colle.','اختيار المشط المناسب للبلاط والتحقق من تغطية اللاصق.','Choose the appropriate notch and verify adhesive transfer.')},
    {image:6,icon:'tile',
      title:l('Poser et presser les carreaux','ضع البلاط واضغطه جيدًا','Set and press tiles'),
      description:l('Respecter le temps ouvert confirmé par la FT ; contrôler planéité et couverture.','الالتزام بزمن الفتح المعتمد والتحقق من الاستواء والتغطية.','Observe validated open time and check flatness and tile-back coverage.')},
  ]
};

const c1te:ReviewedV3Guide={
  code:'BOND-C1TE',
  slug:'fenek-bond-c1te',
  sprite:'/images/application-v3/fenek-bond-c1te-steps.webp',
  sha256:'0d4ea8e4b5fc7ec44e3b772f470aeffa81cc50009b2f724d0420c89fd8cd58ce',
  status:'BROUILLON',
  steps:[
    {image:1,icon:'brush',
      title:l('Nettoyer et vérifier le support','نظّف السطح وتحقق من ثباته','Clean and inspect substrate'),
      description:l('Contrôler adhérence, propreté et planéité avant encollage.','التحقق من نظافة السطح وثباته واستوائه قبل الفرد.','Check that the substrate is sound, clean and flat.')},
    {image:2,icon:'shield',
      title:l('Porter gants, lunettes et masque','ارتدِ القفازات والنظارات والكمامة','Wear gloves, goggles and dust mask'),
      description:l('Utiliser les EPI adaptés selon la FDS approuvée lors de la manipulation et du gâchage.','استخدم وسائل الوقاية المطلوبة في نشرة السلامة أثناء الخلط.','Wear PPE specified by the approved safety sheet during handling and mixing.')},
    {image:3,icon:'water',
      title:l('Ajouter l’eau selon la fiche technique','أضف الماء حسب النشرة الفنية','Measure water as specified'),
      description:l('Ne pas deviner le dosage : respecter les quantités de la FT FENEK validée.','لا تخمّن الجرعة؛ اتبع كميات الماء في النشرة الفنية المعتمدة.','Follow the approved FENEK water ratio; never estimate quantities.')},
    {image:4,icon:'clock',
      title:l('Laisser reposer puis remalaxer','اترك الخليط يرتاح ثم أعد الخلط','Rest and remix if required'),
      description:l('Suivre le temps de repos et le remalaxage seulement si la procédure approuvée les prescrit.','اتبع الاستراحة وإعادة الخلط فقط إذا نصت النشرة المعتمدة.','Observe resting and remixing only if required by the approved procedure.')},
    {image:5,icon:'trowel',
      title:l('Étaler avec une spatule crantée','وزّع اللاصق بمالج مسنن','Spread with a notched trowel'),
      description:l('Choisir le peigne selon le format du carreau et vérifier le transfert.','اختر المشط بحسب حجم البلاط وتحقق من تغطية اللاصق.','Choose the correct notch for the tile and verify adhesive transfer.')},
    {image:6,icon:'tile',
      title:l('Poser avant la fin du temps ouvert','اضغط البلاط قبل انتهاء الزمن المفتوح','Set tiles within the open time'),
      description:l('Respecter le temps ouvert réellement validé pour C1TE ; presser et contrôler la couverture.','التزم بزمن الفتح المعتمد لهذا المرجع واضغط البلاط وتحقق من التغطية.','Set and press within the approved C1TE open time; inspect tile-back coverage.')},
  ]
};

const reviewed:Readonly<Record<string,ReviewedV3Guide>>=Object.freeze({'BOND-C1T':c1t,'BOND-C1TE':c1te});
export function reviewedV3GuideFor(code:string,slug:string):ReviewedV3Guide|null{
  const guide=reviewed[code];
  if(!guide)return null;
  if(guide.slug!==slug || guide.code!==code)
    throw Error('V3 illustration/product mismatch: '+code+'/'+slug);
  if(guide.steps.length!==6 || guide.steps.some((s,i)=>s.image!==i+1))
    throw Error('Invalid V3 step sequence for '+code);
  return guide;
}
