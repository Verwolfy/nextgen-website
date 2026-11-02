import type { Lang,Range } from './site';
export const catalogueCopy:Record<Lang,{
  title:string;lead:string;status:string;intro:string;count:string;view:string;concept:string;
  format:string;unknownFormat:string;application:string;procedure:string;sourceProcedure:string;
  sourceNote:string;back:string;pictureNote:string;packshotNote:string;quote:string;rangeNav:string;
  review:string;methodTitle:string;methodDisclaimer:string;revision:string;
}>={
fr:{
 title:'Catalogue des 50 références',lead:'50 références FENEK acceptées pour présentation éditoriale. Les caractéristiques et consignes restent provisoires jusqu’aux vérifications techniques.',
 status:'Présentation de projet · Non homologué',intro:'Retrouvez les familles, descriptions, formats envisagés et modes d’emploi de travail. Les fiches pourront être révisées.',count:'références',view:'Consulter la fiche',concept:'Projet FENEK',
 format:'Conditionnements envisagés',unknownFormat:'Format à préciser',application:'Description du produit',procedure:'Déroulement indicatif',sourceProcedure:'Mode d’emploi source (brouillon français)',sourceNote:'Les mentions « valeur à confirmer » nécessitent des essais. Ne pas utiliser ce texte comme instruction de chantier.',
 back:'Retour au catalogue',pictureNote:'Illustration générique d’emballage : elle ne reproduit pas l’étiquette ni le format exact de cette référence.',packshotNote:'Maquette graphique propre à cette référence : étiquette, mentions techniques et conditionnement à confirmer avant impression ou commercialisation.',quote:'Voir les contacts',rangeNav:'Explorer par gamme',
 review:'Aucune certification, performance, dosage ni disponibilité commerciale n’est attestée par cet accord éditorial.',methodTitle:'Étapes de préparation à confirmer',methodDisclaimer:'Les consignes détaillées doivent être vérifiées avec une fiche technique propre à la référence avant usage.',revision:'Contenu révisable. Les données du laboratoire prévaudront une fois validées.'
},
ar:{
 title:'كتالوج يضم 50 مرجعًا',lead:'50 مرجعًا من مجموعات FENEK أُجيز عرضها تعريفيًا. تظل المواصفات وتعليمات الاستخدام أولية إلى حين اعتمادها فنيًا.',
 status:'عرض أولي · غير معتمد فنيًا',intro:'تصفّح المجموعات والمنتجات المقترحة وعبواتها وخطوات استخدامها الأولية. يمكن مراجعة المعلومات وتعديلها لاحقًا.',count:'مرجعًا',view:'عرض التفاصيل',concept:'تصور منتج',
 format:'العبوات المقترحة',unknownFormat:'لم يُحدّد حجم العبوة بعد',application:'وصف المنتج',procedure:'خطوات استخدام استرشادية',sourceProcedure:'نص طريقة الاستعمال الأصلي بالفرنسية (مسودة)',sourceNote:'تتضمن المسودة الفرنسية قيمًا لم تُحدّد بعد. لا تُستخدم تعليمات تنفيذ في موقع العمل.',
 back:'العودة إلى الكتالوج',pictureNote:'صورة توضيحية عامة للعبوة، ولا تمثل الشكل أو الملصق النهائي لهذا المرجع.',packshotNote:'تصميم توضيحي خاص بهذا المرجع. يجب مراجعة الملصق والمعلومات التقنية وحجم العبوة قبل التصنيع أو التسويق.',quote:'وسائل التواصل',rangeNav:'تصفح حسب المجموعة',
 review:'الموافقة على العرض لا تعني اعتماد الأداء أو الجرعات أو المطابقة أو توافر المنتج للبيع.',methodTitle:'خطوات أولية قابلة للمراجعة',methodDisclaimer:'يجب الرجوع إلى النشرة الفنية المعتمدة الخاصة بكل منتج قبل الاستخدام الفعلي.',revision:'يمكن تحديث هذا المحتوى لاحقًا وفقًا لنتائج التجارب والاعتمادات الفنية.'
},
en:{
 title:'Catalogue of 50 references',lead:'50 FENEK references approved for editorial presentation. Technical details and instructions remain provisional pending product-specific review.',
 status:'Concept presentation · Not certified',intro:'Explore the proposed ranges, descriptions, packaging formats and draft working methods. Content may be updated later.',count:'references',view:'Explore concept',concept:'FENEK concept',
 format:'Proposed packaging',unknownFormat:'Packaging format to be defined',application:'Product description',procedure:'Indicative workflow',sourceProcedure:'Original French instructions (draft)',sourceNote:'The French draft contains values not yet established by testing. It is not an instruction for site use.',
 back:'Back to catalogue',pictureNote:'Generic packaging illustration: not the final label or necessarily the exact format of this product.',packshotNote:'Product-specific visual concept: label, technical statements and packaging must be reviewed before printing or sale.',quote:'Contact channels',rangeNav:'Browse by range',
 review:'Editorial approval does not establish certification, performance, dosage or commercial availability.',methodTitle:'Preparation steps pending review',methodDisclaimer:'Follow a product-specific, approved technical datasheet before any actual application.',revision:'This content can be revised as laboratory and technical validation progresses.'
}
};
export const guideKey=(code:string):string=>{
 if(code.startsWith('BOND-C'))return 'tile';
 if(code.startsWith('BOND-R'))return 'repair';
 if(code.startsWith('PROOF-EP-INJ')||code.startsWith('PROOF-PU-INJ'))return 'injection';
 if(code.startsWith('PROOF-EP')||code.startsWith('PROOF-PU'))return 'resin';
 if(code.startsWith('FLOW-'))return 'admixture';
 if(code.startsWith('PAINT-'))return 'paint';
 return 'mortar';
};
const methods:Record<Lang,Record<string,readonly string[]>>={
fr:{
 tile:['Contrôler le support et sa compatibilité avec le système envisagé.','Préparer et mélanger seulement selon les proportions qui seront établies par la fiche technique.','Appliquer et respecter les temps de travail et de cure après validation de la méthode.'],
 repair:['Contrôler la stabilité du béton et la préparation des zones à réparer.','Définir la préparation du mélange et l’épaisseur admissible par essais.','Protéger la réparation et vérifier les conditions de cure prescrites.'],
 injection:['Identifier la zone à traiter et les conditions de sécurité.','Définir le matériel d’injection et les paramètres applicables dans une procédure approuvée.','Contrôler l’intervention selon les résultats d’essais et la notice validée.'],
 resin:['Examiner la propreté, l’humidité et la compatibilité du support.','Respecter le ratio de mélange ou le mode de préparation indiqué dans une fiche validée.','Appliquer puis respecter les conditions et délais de recouvrement confirmés.'],
 admixture:['Vérifier la compatibilité avec les matériaux et la formulation du chantier.','Déterminer le dosage et le moment d’incorporation à partir d’essais de convenance.','Contrôler le béton ou le mortier frais puis les performances requises.'],
 paint:['Préparer le support et vérifier l’adéquation du primaire.','Déterminer la dilution, les couches et les outils sur une fiche technique approuvée.','Respecter les conditions d’application et les délais de séchage validés.'],
 mortar:['Préparer le support et vérifier l’application prévue.','Définir le gâchage, l’épaisseur et les conditions de mise en œuvre par essais.','Contrôler les délais et la cure prévus par la documentation approuvée.']
},
ar:{
 tile:['افحص حالة السطح ومدى ملاءمته لنظام اللصق المقترح.','لا تُحدّد كمية الماء أو طريقة الخلط إلا وفق نشرة فنية معتمدة بعد التجارب.','تُراجع طريقة الفرد وأزمنة العمل والتصلب قبل أي استعمال فعلي.'],
 repair:['تحقّق من سلامة الخرسانة وطريقة تجهيز المناطق المراد إصلاحها.','تُحدّد نسبة الخلط والسماكة المسموح بها بعد الاختبارات.','تُراجع شروط المعالجة والحماية وفق التعليمات المعتمدة.'],
 injection:['حدّد موضع المعالجة وتحقّق من شروط السلامة اللازمة.','يُختار جهاز الحقن ومعايير التشغيل بناءً على إجراء فني معتمد.','تُراقب نتائج التنفيذ وفق الاختبارات والنشرة المعتمدة.'],
 resin:['افحص نظافة السطح ورطوبته ومدى توافقه مع المادة.','تُعتمد نسب خلط المكونات وطريقة التجهيز فقط بعد المراجعة الفنية.','تُراجع طريقة التطبيق وأزمنة إعادة الطلاء أو التصلب قبل الاستخدام.'],
 admixture:['تحقّق من توافق المادة المضافة مع الأسمنت والركام وخلطة المشروع.','تُحدّد الجرعة ومرحلة الإضافة باختبارات الملاءمة.','تُراجع خصائص الخرسانة أو الملاط الطازج ونتائج الاختبارات المطلوبة.'],
 paint:['نظّف السطح وافحص ملاءمة الطلاء التمهيدي له.','تُحدّد نسبة التخفيف وعدد الطبقات والأدوات بالنشرة الفنية المعتمدة.','تُراجع ظروف التطبيق وفترات الجفاف قبل الاستعمال.'],
 mortar:['جهّز السطح وفق طبيعة التطبيق المقترح.','تُحدّد نسبة ماء الخلط والسماكة وطريقة التنفيذ بعد الاختبارات.','تُراجع مدد التشغيل والمعالجة وفق الوثائق الفنية المعتمدة.']
},
en:{
 tile:['Check the substrate and its suitability for the proposed tile-laying system.','Set water ratio and mixing method only after review in a product-specific technical sheet.','Confirm application method, working time and curing period before use.'],
 repair:['Inspect concrete stability and preparation requirements.','Confirm mixing proportions and admissible layer thickness through testing.','Check protective measures and curing according to approved guidance.'],
 injection:['Identify the area for treatment and relevant safety conditions.','Specify injection equipment and parameters in an approved procedure.','Review treatment results according to testing and the approved datasheet.'],
 resin:['Check substrate cleanliness, moisture and material compatibility.','Use component ratios and preparation methods only after technical approval.','Confirm application and recoating or curing intervals before use.'],
 admixture:['Verify compatibility with cement, aggregates and the intended mix.','Determine dosage and addition stage through suitability tests.','Check fresh concrete or mortar properties and required test outcomes.'],
 paint:['Prepare the substrate and verify suitable primers.','Confirm dilution, coating layers and tools in an approved technical sheet.','Respect reviewed application conditions and drying intervals.'],
 mortar:['Prepare the substrate for the intended application.','Confirm mixing water, layer thickness and application conditions by testing.','Check working and curing intervals in approved documentation.']
}
};
export const guidance=(lang:Lang,code:string):readonly string[]=>methods[lang][guideKey(code)]??methods[lang].mortar;
