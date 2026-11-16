import type { Lang } from './site';
import manualEntries from './fenek-v3-manuals.json';

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
  fullResolution?:ReadonlyArray<string>;
  steps:ReviewStep[];
  status:'BROUILLON';
};
const l=(fr:string,ar:string,en:string):Localized=>({fr,ar,en});

const c1t:ReviewedV3Guide={
  code:'BOND-C1T',
  slug:'fenek-bond-c1t',
  sprite:'/images/illustrations/application-upgraded/fenek-bond-c1t-steps.webp',
  sha256:'d3d6c1d5ef31bca31108d9ddafa82e5bb1ffd0b16350345caee13c19b1fe0213',
  status:'BROUILLON',
  fullResolution:[
    '/images/illustrations/application/v3/fenek-bond-c1t/01_support.png',
    '/images/illustrations/application/v3/fenek-bond-c1t/02_epi.png',
    '/images/illustrations/application/v3/fenek-bond-c1t/03_gachage.png',
    '/images/illustrations/application/v3/fenek-bond-c1t/04_repos.png',
    '/images/illustrations/application/v3/fenek-bond-c1t/05_encollage.png',
    '/images/illustrations/application/v3/fenek-bond-c1t/06_pose.png',
  ],
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
  sprite:'/images/illustrations/application-upgraded/fenek-bond-c1te-steps.webp',
  sha256:'363e65cdf9d601a65037deca58b8e51667cbb5fdbd75fc1111ef7e142a7e521b',
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

/**
 * C2FT / C1TE: six SOURCE illustrations have strictly identical RGB pixels
 * in rows [0..1589] of every 2048×2048 PNG; only the embedded AR/FR captions
 * (from row 1590) differ. Proof: SHA-256 of concatenated six RGB crops:
 * 6ea7fb90b80a57a5b0f293ba95e79afea2063765d5e2601563ca974758c0d321.
 * Reuse the already reviewed 6-panel bitmap ONLY with embedded captions cropped;
 * titles below come from C2FT's own legends.csv. Replace by its own full-res
 * assets when the binary upload is available. Never infer C2FT working times.
 */
const reviewed:Readonly<Record<string,ReviewedV3Guide>>=Object.freeze((()=>{
  const all:Record<string,ReviewedV3Guide>={'BOND-C1T':c1t,'BOND-C1TE':c1te};
  const seen=new Set<string>();
  for(const entry of manualEntries){
    if(seen.has(entry.code) || !/^[A-Z][A-Z0-9-]+$/.test(entry.code) || !/^fenek-[a-z0-9-]+$/.test(entry.slug))
      throw Error('Invalid or duplicate V3 reference '+entry.code+'/'+entry.slug);
    seen.add(entry.code);
    if(entry.status!=='BROUILLON' || entry.steps.length!==6 || entry.steps.some((step,i)=>step.image!==i+1))
      throw Error('Incorrect V3 source sequence '+entry.code);
    // Preserve the original approved-for-editorial-display C1T and C1TE assets.
    if(entry.code==='BOND-C1T' || entry.code==='BOND-C1TE') continue;
    all[entry.code]={
      code:entry.code,slug:entry.slug,sprite:entry.sprite,sha256:entry.sha256,
      status:'BROUILLON',
      steps:entry.steps.map((step)=>({image:step.image,icon:'check',title:step.title,description:step.description}))
    };
  }
  if(seen.size!==50 || Object.keys(all).length!==50)
    throw Error('V3 source catalogue is incomplete; expected exactly 50 distinct references');
  return all;
})());
export function reviewedV3GuideFor(code:string,slug:string):ReviewedV3Guide|null{
  const guide=reviewed[code];
  if(!guide)return null;
  if(guide.slug!==slug || guide.code!==code)
    throw Error('V3 illustration/product mismatch: '+code+'/'+slug);
  if(guide.steps.length!==6 || guide.steps.some((s,i)=>s.image!==i+1))
    throw Error('Invalid V3 step sequence for '+code);
  return guide;
}
