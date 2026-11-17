import type {Lang} from './site';
import {c2tes1Copy} from './fenek-c2tes1-reference';

export type OtherMetric={key:string;kind:'referentiel'|'famille';label:Record<Lang,string>;value:string};
export type OtherRaw={code:string;group:string;standard:string;intro:Record<Lang,string>;requirements:string[][];family:string[][]};
export type OtherRecord={code:string;short:string;group:string;standard:string;requirements:OtherMetric[];family:OtherMetric[];copy:Record<Lang,typeof c2tes1Copy.fr>};
type Guide={prep:Record<Lang,string[]>;apply:Record<Lang,string[]>;substrates:Record<Lang,string[]>;safety:Record<Lang,string[]>};
const baseSafety:Record<Lang,string[]>={
 fr:['Consulter la fiche de données de sécurité de la formulation livrée.','Porter les protections adaptées et maîtriser les projections.','Récupérer les déchets sans rejet vers les évacuations.'],
 ar:['راجع صحيفة بيانات السلامة الخاصة بالتركيبة الموردة.','استعمل معدات الحماية المناسبة ومنع الرذاذ.','اجمع المخلفات دون تصريفها في شبكات المياه.'],
 en:['Read the safety data sheet for the supplied formulation.','Use suitable PPE and control splashes or dust.','Collect waste without releasing it into drainage.']
};
const contexts:Record<string,{fr:string[];ar:string[];en:string[]}>={
 'proof-membrane':{
 fr:['Contrôler pente, cohésion, humidité et fissures du support.','Traiter relevés, raccords, traversées et zones sensibles avec les accessoires du système.','Appliquer les couches prescrites, vérifier les consommations et respecter les délais de recouvrement.'],
 ar:['افحص الميول وتماسك ورطوبة وتشققات السطح.','عالج الزوايا والوصلات والفتحات بملحقات النظام المتوافق.','طبق الطبقات المقررة وافحص الاستهلاك واحترم فترات إعادة الطلاء.'],
 en:['Check falls, soundness, moisture and cracking of the substrate.','Detail upstands, penetrations, joints and vulnerable points with system accessories.','Apply specified coats, control spread rate and respect recoat times.']
 },
 'proof-cement':{
 fr:['Vérifier support cimentaire sain, planéité et humidification compatible.','Renforcer angles, joints et pénétrations conformément au système sous carrelage.','Respecter l’épaisseur sèche, les temps de cure et la compatibilité de la colle à carrelage.'],
 ar:['تحقق من تماسك واستواء السطح الإسمنتي وترطيبه المناسب.','عزز الزوايا والفواصل والاختراقات حسب نظام العزل تحت البلاط.','احترم السماكة النهائية وزمن المعالجة وتوافق لاصق البلاط.'],
 en:['Check sound cementitious substrate, flatness and compatible dampening.','Reinforce corners, joints and penetrations for the under-tile system.','Respect dry thickness, cure and compatible tile adhesive selection.']
 },
 'proof-anchor':{
 fr:['Vérifier béton fissuré/non fissuré, entraxes et distances aux rives selon calcul.','Forer puis nettoyer les trous selon l’agrément du système de résine et les outils prescrits.','Injecter avec mélangeur adapté, installer l’élément et attendre la polymérisation avant charge.'],
 ar:['تحقق من نوع الخرسانة والمسافات والحواف وفق الحسابات الهندسية.','اثقب ونظف الثقوب حسب تقييم نظام الراتنج والأدوات المحددة.','احقن بالخلاط المناسب وثبت العنصر وانتظر التصلب قبل التحميل.'],
 en:['Check cracked/uncracked concrete, edge distances and spacing against design.','Drill and clean holes using the approved anchor system process.','Inject with proper mixer, place the anchor and wait for full cure before loading.']
 },
 'proof-epoxy':{
 fr:['Contrôler résistance, rugosité, humidité et propreté du béton.','Vérifier rapport de mélange, température du support et point de rosée.','Appliquer dans le temps de vie en pot et contrôler la cure avant service.'],
 ar:['افحص مقاومة وخشونة ورطوبة ونظافة الخرسانة.','تحقق من نسبة الخلط ودرجة حرارة السطح ونقطة الندى.','طبق خلال فترة التشغيل وافحص التصلب قبل الاستعمال.'],
 en:['Check concrete strength, profile, moisture and cleanliness.','Verify mix ratio, substrate temperature and dew point.','Apply within pot life and check curing before service.']
 },
 'proof-injection':{
 fr:['Diagnostiquer fissure active ou stable et origine des venues d’eau.','Mettre en place les injecteurs, colmater les fuites en surface si prévu.','Injecter à la pression qualifiée et contrôler le remplissage et les reprises.'],
 ar:['شخّص حركة الشقوق ومصدر تسرب المياه.','ثبت منافذ الحقن وأغلق التسرب السطحي عند الحاجة.','احقن بالضغط المعتمد وافحص الامتلاء وإعادة الحقن.'],
 en:['Diagnose moving or dormant cracks and water ingress source.','Install injection ports and surface sealing where required.','Inject at qualified pressure and verify filling and reinjection requirements.']
 },
 'proof-sealant':{
 fr:['Vérifier largeur, profondeur, mouvement et état des lèvres du joint.','Installer fond de joint et primaire seulement si prescrits.','Extruder en continu, lisser sans contamination et protéger pendant cure.'],
 ar:['افحص عرض وعمق الفاصل وحركته ونظافة حوافه.','ركب حشوة خلفية وبرايمر عند الحاجة حسب النشرة.','ضع الماستيك بشكل متواصل ونعمه واحمه أثناء المعالجة.'],
 en:['Check joint width, depth, movement and clean joint flanks.','Use backing rod and primer only if prescribed.','Extrude continuously, tool the sealant and protect during curing.']
 },
 'flow-admixture':{
 fr:['Identifier le ciment, les granulats, la classe de béton et les performances recherchées.','Réaliser des gâchées comparatives avec une formulation témoin documentée.','Mesurer consistance, prise, air et résistances selon les essais adaptés.'],
 ar:['حدد الإسمنت والركام ونوع الخرسانة والخصائص المستهدفة.','أجر خلطات مقارنة مع خلطة مرجعية موثقة.','قس التشغيلية وزمن الشك والهواء والمقاومة بالاختبارات المناسبة.'],
 en:['Identify cement, aggregates, concrete class and performance targets.','Run comparative trial batches against a documented control mix.','Measure workability, setting, air and strengths with suitable tests.']
 },
 'flow-cure':{
 fr:['Finir le béton et vérifier l’absence d’eau de ressuage avant pulvérisation.','Choisir le procédé et le taux d’application validés pour l’ouvrage.','Contrôler la continuité du film et la compatibilité des revêtements ultérieurs.'],
 ar:['أنهِ سطح الخرسانة وتحقق من زوال ماء النزف قبل الرش.','اختر طريقة الرش ومعدل التغطية وفق التعليمات المعتمدة.','افحص استمرارية الطبقة وتوافق الطلاء اللاحق.'],
 en:['Finish concrete and allow bleeding water to clear before spraying.','Select the approved application method and coverage for the work.','Check film continuity and compatibility with later coatings.']
 },
 'flow-latex':{
 fr:['Contrôler la cohésion, la rugosité et l’humidité du support.','Préparer le pont d’adhérence ou le mortier modifié selon la formule qualifiée.','Appliquer dans la fenêtre d’adhérence et assurer la cure appropriée.'],
 ar:['افحص تماسك وخشونة ورطوبة السطح.','جهز طبقة الربط أو المونة المعدلة وفق التركيبة المؤهلة.','طبق ضمن فترة الالتصاق المناسبة مع المعالجة المطلوبة.'],
 en:['Assess substrate soundness, profile and moisture.','Prepare bonding slurry or modified mortar to the qualified recipe.','Place within the bonding window and cure appropriately.']
 },
 'paint-interior':{
 fr:['Vérifier fonds propres, secs, cohésifs et sans anciennes peintures non adhérentes.','Reboucher, poncer et appliquer le primaire correspondant à l’absorption.','Appliquer les couches et respecter la ventilation et les délais de séchage.'],
 ar:['تحقق من نظافة وجفاف وتماسك الأسطح وإزالة الطلاء الضعيف.','عالج العيوب وصنفر واستعمل البرايمر حسب امتصاص السطح.','طبق الطبقات مع التهوية واحترام فترات الجفاف.'],
 en:['Ensure clean, dry, sound walls free of loose old coatings.','Fill and sand defects; prime to match substrate suction.','Apply specified coats with ventilation and adequate drying times.']
 },
 'paint-exterior':{
 fr:['Contrôler l’état de façade, fissures, humidité et anciennes peintures.','Traiter les défauts, appliquer le système de primaire compatible.','Respecter les conditions météo, l’épaisseur de film et la reprise entre passes.'],
 ar:['افحص الواجهة والتشققات والرطوبة والدهانات القديمة.','عالج العيوب واستعمل نظام الأساس المتوافق.','احترم الطقس وسماكة الطلاء وفترات إعادة التطبيق.'],
 en:['Assess façade condition, cracks, moisture and existing coatings.','Repair defects and use the compatible primer system.','Respect weather limits, film build and recoat intervals.']
 },
 'paint-primer':{
 fr:['Contrôler la nature du support, cohésion, absorption et propreté.','Tester l’accrochage sur zone pilote et adapter la préparation.','Appliquer uniformément puis respecter le séchage avant finition.'],
 ar:['افحص نوع السطح وتماسكه وامتصاصه ونظافته.','اختبر الالتصاق على مساحة صغيرة واضبط التحضير.','طبق البرايمر بالتساوي وانتظر الجفاف قبل التشطيب.'],
 en:['Check substrate type, strength, absorbency and cleanliness.','Run a trial patch and adjust the surface preparation.','Prime evenly and allow full drying before topcoating.']
 },
 'paint-floor':{
 fr:['Diagnostiquer béton, humidité résiduelle, laitance et contamination.','Préparer mécaniquement et tester l’adhérence du système proposé.','Appliquer primaire et finition selon le trafic prévu et les délais de cure.'],
 ar:['افحص رطوبة الخرسانة والطبقة السطحية والتلوث.','جهز ميكانيكياً واختبر الالتصاق بالنظام المختار.','طبق الأساس والطلاء حسب الحركة المتوقعة ومواعيد المعالجة.'],
 en:['Inspect concrete moisture, laitance and contamination.','Mechanically prepare and test adhesion of the proposed system.','Prime and topcoat to the intended traffic and curing programme.']
 },
 'paint-paste':{
 fr:['Vérifier la cohésion et la planéité du support, réparer les défauts majeurs.','Appliquer l’enduit en couches appropriées sans surcharge.','Laisser sécher, poncer et dépoussiérer avant peinture.'],
 ar:['افحص تماسك واستواء السطح وعالج العيوب الكبيرة.','طبق المعجون على طبقات مناسبة دون سماكة مفرطة.','اتركه يجف ثم صنفر ونظف قبل الطلاء.'],
 en:['Check substrate soundness and flatness and repair major defects.','Apply filling compound in suitable layers without excessive build.','Dry, sand and remove dust before painting.']
 }
};
const groupSafety:Record<string,Record<Lang,string[]>>={
 'proof-epoxy':{fr:['Porter gants imperméables et lunettes ; éviter tout contact avec résines non polymérisées.','Ventiler la zone ; respecter les contraintes des composants A et B.','Consulter la FDS et éliminer les emballages souillés selon les règles locales.'],
 ar:['استخدم قفازات مقاومة ونظارات وتجنب ملامسة الراتنج قبل التصلب.','هوِّ المنطقة واحترم تعليمات المكونين A وB.','راجع صحيفة السلامة وتخلص من العبوات الملوثة بشكل صحيح.'],
 en:['Wear chemical-resistant gloves and goggles; avoid skin contact with uncured resin.','Ventilate and follow separate A/B component safety requirements.','Consult the SDS and dispose of contaminated packaging appropriately.']},
 'proof-injection':{fr:['Contrôler la pression d’injection et protéger les intervenants contre les projections.','Manipuler la résine avec lunettes, gants et ventilation appropriée.','Consulter la FDS et gérer les effluents et résidus sous contrôle.'],
 ar:['راقب ضغط الحقن واحم العاملين من الرذاذ.','استخدم القفازات والنظارات والتهوية المناسبة.','اتبع صحيفة السلامة وتحكم في المخلفات والسوائل.'],
 en:['Control injection pressure and protect operators from pressurized splashes.','Handle resin with eye protection, gloves and suitable ventilation.','Follow the SDS and control waste and effluents.']}
};
const metric=(rows:string[][],kind:OtherMetric['kind']):OtherMetric[]=>rows.map((row,i)=>{
 if(row.length!==4)throw Error('Metric needs FR/AR/EN/value');
 return {key:kind+'-'+(i+1),kind,label:{fr:row[0],ar:row[1],en:row[2]},value:row[3]};
});
export function buildOtherRecords(definitions:OtherRaw[]):Record<string,OtherRecord>{
 return Object.fromEntries(definitions.map(record=>{
   const {code,group,standard,intro}=record;
   const context=contexts[group];
   if(!context||!code.match(/^(PROOF|FLOW|PAINT)-/))throw Error('Unrecognized family: '+code);
   const short=code.split('-').slice(1).join('-');
   const requirements=metric(record.requirements,'referentiel');
   const family=metric(record.family,'famille');
   if(!requirements.length||family.length<3)throw Error('Insufficient technical comparison: '+code);
   const copy=Object.fromEntries((['fr','ar','en'] as const).map(lang=>{
    const name='FENEK-'+code.replace('-', ' ');
    const labels=lang==='fr'?{
      sheet:'Fiche produit — ',technical:'Référentiels et critères de vérification — ',
      family:'Repères de produits comparables',uses:'Domaine d’emploi',substrates:'Préparation et supports',
      consumption:'Indications comparatives de produits documentés',comparison:'Références de la même famille',
      note:'Les valeurs documentaires ne remplacent pas la qualification de la formulation ni le dimensionnement du système.'
    }:lang==='ar'?{
      sheet:'بطاقة المنتج — ',technical:'المراجع الفنية ونقاط التحقق — ',family:'مؤشرات من منتجات مقارنة',
      uses:'مجال الاستعمال',substrates:'التحضير والسطح',
      consumption:'بيانات مقارنة من منتجات موثقة',comparison:'منتجات من العائلة نفسها',
      note:'لا تغني المعلومات المرجعية عن اعتماد التركيبة أو التصميم الهندسي للنظام.'
    }:{
      sheet:'Product sheet — ',technical:'Reference methods and qualification checks — ',
      family:'Documented comparable-product references',uses:'Intended field of use',substrates:'Substrates and preparation',
      consumption:'Comparative parameters from documented products',comparison:'Related products in this family',
      note:'Documentary references do not replace formulation qualification or system engineering.'
    };
    const steps=context[lang],lead=intro[lang];
    return [lang,{
      ...c2tes1Copy[lang],
      pageTitle:name+' | '+lead,
      metaDescription:lead+' — '+standard,
      sheetTitle:labels.sheet+name,
      lead,
      techTitle:labels.technical+standard,
      familyTitle:labels.family,
      usesTitle:labels.uses,
      substratesTitle:labels.substrates,
      consumptionTitle:labels.consumption,
      comparisonTitle:labels.comparison,
      comparisonNote:labels.note,
      benefits:[lead,requirements[0].label[lang]+': '+requirements[0].value,labels.note],
      uses:[lead,steps[0],steps[2]],
      substrates:[steps[0],steps[1],steps[2]],
      preparation:[steps[0],steps[1],steps[2]],
      conditions:[steps[1],steps[2],lang==='fr'?'Valider l’application sur une zone témoin avant généralisation.':lang==='ar'?'اختبر التطبيق على مساحة نموذجية قبل التعميم.':'Validate the process on a test area before full-scale application.'],
      safety:(groupSafety[group]?.[lang]||baseSafety[lang])
    }];
   })) as Record<Lang,typeof c2tes1Copy.fr>;
   return [code,{...record,short,requirements,family,copy}];
 }));
}
