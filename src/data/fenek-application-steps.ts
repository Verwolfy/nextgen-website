import type { Lang } from './site';

/**
 * Lot 121 — editorial application walkthroughs for 50 provisional references.
 * This is NOT a product technical data sheet. Stages are adapted from the draft
 * catalogue method, generic trade manuals and product-family practice.
 * No quantities, times, temperatures, certified claims or mixing ratios.
 */
type L = Record<Lang,string>;
export type ApplicationStep = { title:L; detail:L; icon:string; image?:number };
const l=(fr:string,ar:string,en:string):L=>({fr,ar,en});
const s=(icon:string,frT:string,frD:string,arT:string,arD:string,enT:string,enD:string,image?:number):ApplicationStep=>
  ({icon,title:l(frT,arT,enT),detail:l(frD,arD,enD),...(image?{image}:{})});

const tile:ApplicationStep[]=[
 s('brush','Préparer le support','Vérifier la solidité et la planéité ; enlever poussière, laitance et résidus. Prévoir le primaire adapté si nécessaire.',
   'تحضير السطح','التحقق من المتانة والاستواء وإزالة الغبار والبقايا، وتحديد طبقة الأساس عند الحاجة.',
   'Prepare substrate','Check soundness and flatness; remove dust and residues. Select a compatible primer if required.',1),
 s('water','Préparer le gâchage','Mesurer uniquement la quantité d’eau prescrite par la fiche FENEK validée, puis incorporer la poudre.',
   'تحضير ماء الخلط','قياس كمية الماء طبقًا للنشرة الفنية المعتمدة ثم إضافة المسحوق.',
   'Prepare mixing water','Measure only the water quantity specified in an approved FENEK sheet before adding powder.',2),
 s('mix','Malaxer','Mélanger mécaniquement jusqu’à une pâte régulière, sans grumeaux ; ne pas improviser un dosage.',
   'الخلط','الخلط ميكانيكيًا حتى الحصول على عجينة متجانسة دون كتل، دون تخمين الجرعة.',
   'Mix to consistency','Mechanically mix until uniform and lump-free; never guess a mixing ratio.',3),
 s('clock','Respecter le temps de repos','Laisser mûrir puis remalaxer seulement si la procédure du produit le prévoit ; respecter la durée validée.',
   'احترام فترة الانتظار','ترك الخليط ثم إعادة خلطه فقط إذا نصت نشرة المنتج على ذلك، مع احترام المدة المعتمدة.',
   'Observe rest time','Allow a rest and remix only when required by that product’s approved procedure.',4),
 s('trowel','Étaler au peigne','Étaler la colle sur le support avec une taloche crantée adaptée au format et au taux de transfert recherché.',
   'فرد اللاصق بالمشط','توزيع اللاصق بمجرفة مسننة مناسبة لحجم البلاط والتغطية المطلوبة.',
   'Comb adhesive','Use a suitable notched trowel for the tile size and required transfer.',5),
 s('tile','Poser et contrôler','Poser dans le temps ouvert validé, vérifier le transfert au dos du carreau et la planéité. Protéger avant jointoiement.',
   'تركيب البلاط والتحقق','التركيب خلال زمن الفتح المعتمد والتحقق من تغطية ظهر البلاطة والاستواء والحماية قبل الترويبة.',
   'Set and inspect tiles','Set within the approved open time; inspect tile-back coverage and flatness, and protect before grouting.',6)
];
const patterns:Record<string,ApplicationStep[]>={
 tile,
 grout:[
  s('brush','Préparer les joints','Vérifier la prise du mortier-colle et retirer les résidus des interstices.','تحضير الفواصل','فحص تصلب اللاصق وتنظيف الفراغات.','Prepare joints','Confirm the adhesive has set and clear joint spaces.'),
  s('mix','Préparer le mortier','Respecter le mode de préparation et l’eau prescrits par la future FT validée.','إعداد ملاط الفواصل','اتباع تعليمات الخلط وكمية الماء في النشرة المعتمدة.','Mix grout','Follow the approved grout preparation and water instructions.'),
  s('trowel','Garnir en diagonale','Remplir les joints avec une raclette en caoutchouc, sans laisser de vides.','ملء الفواصل قطريًا','ملء الفواصل بأداة مطاطية دون فراغات.','Fill diagonally','Fill joints with a rubber float, avoiding voids.'),
  s('water','Nettoyer et protéger','Nettoyer à l’éponge bien essorée suivant le stade de prise approprié. Préserver le joint pendant son durcissement.','التنظيف والحماية','التنظيف بإسفنجة معصورة حسب تصلب المنتج وحماية الفواصل.','Clean and protect','Use a well-wrung sponge at the suitable setting stage and protect the grout.')
 ],
 leveller:[
  s('brush','Examiner la dalle','Contrôler résistance, humidité, planéité et fissures avant ragréage.','فحص الأرضية','فحص المقاومة والرطوبة والاستواء والتشققات.','Inspect floor','Check strength, moisture, flatness and cracks.'),
  s('shield','Choisir le primaire','Déterminer le primaire selon la porosité et la compatibilité du support.','اختيار مادة الأساس','تحديد المادة التمهيدية حسب المسامية والتوافق.','Select primer','Match primer to substrate porosity and compatibility.'),
  s('mix','Mélanger le ragréage','Gâcher selon la formule validée, sans rajouter d’eau après le début de prise.','خلط ملاط التسوية','اتباع تركيبة الخلط المعتمدة دون إضافة الماء بعد بدء التصلب.','Mix compound','Follow the approved mix; do not retemper a setting batch.'),
  s('level','Couler et égaliser','Répartir régulièrement, désaérer si la FT le prescrit, puis protéger jusqu’au recouvrement autorisé.','الصب والتسوية','توزيع المزيج وتفريغ الهواء حسب النشرة وحمايته حتى التغطية.','Pour and level','Spread evenly, de-air if specified and protect until overcoating is approved.')
 ],
 render:[
  s('brush','Préparer la maçonnerie','Débarrasser la façade des zones friables ; vérifier absorption, joints et cohésion.','تحضير الجدار','إزالة الأجزاء الضعيفة وفحص امتصاص السطح والفواصل.','Prepare masonry','Remove friable areas and assess substrate absorption and joints.'),
  s('water','Conditionner le fond','Humidifier ou appliquer un primaire selon le système et la porosité du support.','تجهيز السطح','الترطيب أو وضع أساس حسب النظام والمسامية.','Condition substrate','Dampen or prime according to the system and substrate porosity.'),
  s('mix','Préparer l’enduit','Mélanger selon la procédure propre à la référence ; contrôler l’homogénéité.','إعداد اللياسة','الخلط حسب التعليمات الخاصة بالمرجع وفحص التجانس.','Mix render','Use the reference-specific procedure and check consistency.'),
  s('trowel','Appliquer et finir','Régler l’épaisseur et la texture selon le chantier, puis assurer la cure adaptée.','التطبيق والتشطيب','ضبط السماكة والملمس وتنفيذ المعالجة اللازمة.','Apply and finish','Control thickness and finish, then provide appropriate curing.')
 ],
 masonry:[
  s('brush','Préparer les éléments','Choisir les blocs adaptés, contrôler assises et état des éléments.','تحضير وحدات البناء','اختيار الكتل وفحص صفوف البناء وحالتها.','Prepare units','Choose suitable units and check coursing and condition.'),
  s('mix','Préparer le mortier','Gâcher à la consistance spécifiée par la FT et les exigences du chantier.','خلط المونة','تحضير القوام حسب النشرة ومتطلبات الورشة.','Mix mortar','Mix to the approved consistency for the job.'),
  s('trowel','Monter les rangs','Poser lit et joints verticaux avec épaisseur conforme au projet.','بناء الصفوف','تنفيذ طبقات الملاط والفواصل حسب المشروع.','Lay courses','Lay bed and perpend joints to the project requirements.'),
  s('check','Contrôler l’ouvrage','Vérifier aplomb, niveau, remplissage et protection de la maçonnerie fraîche.','فحص البناء','التحقق من الشاقول والاستواء وملء الفواصل والحماية.','Check masonry','Verify plumb, level, filled joints and protection.')
 ],
 bedding:[
  s('brush','Préparer le scellement','Examiner vides, ancrages, support et étanchéité du coffrage.','تحضير التثبيت','فحص الفراغات والمراسي والسطح والقالب.','Prepare voids','Inspect void geometry, anchors, substrate and form tightness.'),
  s('mix','Préparer le coulis','Utiliser uniquement la consistance et les quantités validées pour ce mortier.','تحضير ملاط الملء','اتباع القوام والكميات المعتمدة.','Mix grout','Use only the approved consistency and quantities.'),
  s('level','Remplir sans poche d’air','Faire progresser le coulis suivant le plan de calage ; vérifier la continuité.','الملء دون فراغات','ملء الفراغات بحسب خطة التثبيت والتحقق من الاستمرارية.','Fill continuously','Place per approved grouting plan and inspect continuity.'),
  s('shield','Curer et contrôler','Protéger le scellement et vérifier la résistance avant mise en charge.','المعالجة والفحص','حماية الملاط والتحقق من المقاومة قبل التحميل.','Cure and check','Protect the grout and verify strength before loading.')
 ],
 repair:[
  s('brush','Délimiter le béton à reprendre','Enlever le béton altéré ; qualifier l’état des armatures et l’adhérence du fond.','تحديد المنطقة المتضررة','إزالة الخرسانة التالفة وفحص حديد التسليح والسطح.','Remove unsound concrete','Remove defective concrete and assess reinforcement and substrate.'),
  s('shield','Traiter les interfaces','Préparer les armatures et le support selon le système de réparation approuvé.','معالجة الحديد والسطح','تحضير التسليح والسطح وفق نظام الإصلاح المعتمد.','Prepare interfaces','Treat reinforcement and substrate per the approved repair system.'),
  s('mix','Préparer le mortier','Gâcher selon la FT validée et vérifier la compatibilité avec l’épaisseur de reprise.','خلط ملاط الإصلاح','الخلط حسب النشرة وفحص ملاءمة السماكة.','Mix repair mortar','Follow the approved sheet and confirm lift thickness suitability.'),
  s('trowel','Reprofiler et protéger','Appliquer selon la technique retenue, compacter et assurer la cure.','إعادة التشكيل والحماية','التطبيق والدمك والمعالجة حسب الطريقة المعتمدة.','Place and protect','Apply and compact according to the repair method; cure appropriately.')
 ],
 admixture:[
  s('beaker','Définir la formulation','Examiner ciment, granulats, eau et autres adjuvants ; prévoir des essais de convenance.','تحديد الخلطة','فحص الإسمنت والركام والماء والإضافات والتجارب التمهيدية.','Plan mix trials','Review cement, aggregate, water and companion admixtures.'),
  s('water','Valider le dosage','Déterminer la dose uniquement par FT validée et essais sur la formule réelle.','التحقق من الجرعة','تحديد الجرعة وفق النشرة المعتمدة والتجارب على الخلطة الفعلية.','Validate dosage','Determine dose only from an approved sheet and actual mix trials.'),
  s('mix','Incorporer et homogénéiser','Définir point d’introduction et durée de mélange selon procédé et compatibilité.','الإضافة والخلط','تحديد وقت الإضافة وفترة الخلط حسب النظام والتوافق.','Dose and mix','Confirm the dosing point and mixing duration for the process.'),
  s('check','Mesurer les effets','Contrôler les propriétés du béton frais et durci pertinentes pour la référence.','قياس النتائج','اختبار خصائص الخرسانة الطرية والمتصلبة الملائمة للمنتج.','Test performance','Verify relevant fresh and hardened concrete properties.')
 ],
 cure:[
  s('brush','Contrôler la finition','Attendre l’état de surface approprié après mise en œuvre du béton.','فحص حالة السطح','التحقق من جاهزية سطح الخرسانة بعد التشطيب.','Check surface readiness','Confirm the appropriate concrete finish state.'),
  s('beaker','Valider le produit','Vérifier compatibilité avec revêtements ultérieurs et consommation autorisée.','التحقق من التوافق','فحص توافق المنتج مع الطبقات اللاحقة ومعدل الاستهلاك.','Confirm compatibility','Review later coatings and approved application coverage.'),
  s('spray','Pulvériser uniformément','Former une protection continue sans zones omises selon la FT.','الرش المنتظم','تشكيل طبقة حماية متواصلة وفق النشرة.','Spray uniformly','Create a continuous film according to the approved sheet.'),
  s('shield','Protéger et surveiller','Éviter les dégradations et contrôler les conditions de cure.','الحماية والمراقبة','منع تلف الطبقة ومراقبة المعالجة.','Protect and monitor','Protect the treatment and review curing conditions.')
 ],
 latex:[
  s('brush','Préparer l’interface','Nettoyer, rendre cohérent et conditionner le support.','تحضير الواجهة','تنظيف السطح والتأكد من تماسكه وتهيئته.','Prepare interface','Clean and condition a sound substrate.'),
  s('beaker','Choisir la méthode','Déterminer si la résine sert de pont d’adhérence ou de modificateur de mortier.','اختيار الاستخدام','تحديد استعمال الراتنج كطبقة ربط أو مضاف للملاط.','Choose usage','Determine bonding coat versus mortar modification.'),
  s('mix','Préparer le système','Contrôler dilution, liants et délais uniquement via la procédure validée.','تحضير النظام','التحقق من التخفيف والمواد الرابطة والمدة حسب النشرة.','Prepare system','Confirm dilution, binders and working times from approved instructions.'),
  s('check','Tester l’adhérence','Vérifier le contact et la compatibilité du mortier appliqué.','فحص الالتصاق','التحقق من الالتصاق وتوافق الملاط.','Check adhesion','Inspect bond and compatibility.')
 ],
 paint:[
  s('brush','Assainir la surface','Retirer poussière, anciennes couches non adhérentes et défauts. Vérifier humidité du fond.','تنظيف السطح','إزالة الغبار والطلاءات الضعيفة وفحص الرطوبة.','Prepare surface','Remove loose coats, dust and defects; check moisture.'),
  s('shield','Choisir la sous-couche','Adapter le primaire à la nature du fond et à la peinture retenue.','اختيار الأساس','اختيار المادة التمهيدية المتوافقة مع السطح والطلاء.','Select primer','Match primer with substrate and chosen coating.'),
  s('roller','Appliquer le revêtement','Homogénéiser puis appliquer avec l’outil compatible, suivant le schéma validé.','تطبيق الطلاء','خلط المنتج وتطبيقه بالأداة المناسبة حسب النظام المعتمد.','Apply coating','Stir and apply using a compatible tool and approved coating schedule.'),
  s('check','Vérifier la finition','Contrôler uniformité, recouvrement et protection pendant le séchage.','فحص التشطيب','التحقق من التجانس والتغطية والحماية أثناء الجفاف.','Inspect finish','Check uniformity, coverage and drying protection.')
 ],
 primer:[
  s('brush','Nettoyer le fond','Vérifier cohésion, porosité, farinage et humidité.','تنظيف السطح','التحقق من التماسك والمسامية والتطبش والرطوبة.','Prepare substrate','Check soundness, porosity, chalking and moisture.'),
  s('beaker','Vérifier la dilution','Utiliser le produit prêt à l’emploi ou dilué uniquement selon la FT.','التحقق من التخفيف','استعمال المنتج كما هو أو تخفيفه فقط حسب النشرة.','Check dilution','Use neat or diluted only as specified by the approved sheet.'),
  s('roller','Appliquer régulièrement','Traiter toute la surface sans coulures ni manques.','التطبيق المنتظم','تغطية كاملة دون تسييل أو مناطق ناقصة.','Apply evenly','Cover consistently with no runs or missed areas.'),
  s('check','Contrôler avant finition','Vérifier adhérence et délai de recouvrement prescrits.','الفحص قبل التشطيب','فحص الالتصاق ووقت التغطية حسب النشرة.','Inspect before coating','Confirm adhesion and approved overcoating stage.')
 ],
 putty:[
  s('brush','Préparer le mur','Dépoussiérer, traiter fissures et parties détachées.','تحضير الجدار','إزالة الغبار ومعالجة التشققات والأجزاء الضعيفة.','Prepare wall','Remove dust, address cracks and unsound areas.'),
  s('trowel','Lisser par passes','Appliquer au couteau ou à la lame avec épaisseur adaptée.','التسوية بطبقات','التطبيق بالسكين مع التحكم في السماكة.','Skim coats','Apply with a filling knife at suitable thickness.'),
  s('clock','Attendre le séchage','Respecter le délai validé avant intervention suivante.','انتظار الجفاف','احترام مدة الجفاف المعتمدة.','Allow drying','Observe the approved drying time.'),
  s('brush','Poncer et inspecter','Vérifier la planéité, retirer la poussière avant impression.','الصنفرة والفحص','فحص الاستواء وإزالة الغبار قبل الطلاء التمهيدي.','Sand and inspect','Check smoothness and remove dust before priming.')
 ],
 texture:[
  s('brush','Uniformiser le support','Réparer les défauts et sélectionner une impression compatible.','توحيد السطح','معالجة العيوب واختيار أساس مناسب.','Prepare base','Correct defects and select a compatible primer.'),
  s('mix','Homogénéiser le produit','Respecter la préparation de la future FT, sans ajout non prévu.','تجانس المنتج','تحضير المادة حسب النشرة دون إضافات غير معتمدة.','Prepare finish','Follow the approved preparation without unlisted additives.'),
  s('trowel','Créer le relief','Déposer et structurer avec l’outil correspondant à la finition recherchée.','تشكيل الملمس','توزيع المادة وتشكيل النمط بالأداة المناسبة.','Form texture','Spread and structure using the selected finishing tool.'),
  s('check','Vérifier les raccords','Surveiller régularité de teinte, raccords et protection contre la pluie.','فحص الوصلات','فحص اللون والملمس والحماية من المطر.','Inspect texture','Check consistency, joins and weather protection.')
 ],
 membrane:[
  s('brush','Diagnostiquer le support','Vérifier adhérence, fissures, humidité et reliefs de toiture.','فحص السطح','فحص الالتصاق والشقوق والرطوبة وتفاصيل السقف.','Assess substrate','Review adhesion, cracks, moisture and roof details.'),
  s('shield','Traiter les points singuliers','Prévoir relevés, évacuations, raccords et renforts selon le système.','معالجة التفاصيل','تحضير الحواف والمصارف والوصلات والتدعيم حسب النظام.','Detail junctions','Plan upstands, drains, interfaces and reinforcements.'),
  s('roller','Former la membrane','Appliquer des couches continues selon la procédure et les conditions validées.','تشكيل الغشاء','وضع طبقات متصلة حسب الإجراء والشروط المعتمدة.','Apply membrane','Lay continuous coats per approved system requirements.'),
  s('check','Contrôler la continuité','Vérifier absence de trous et cure avant exposition à l’eau.','فحص الاستمرارية','التأكد من خلو الغشاء من الفجوات قبل التعرض للماء.','Inspect continuity','Check for pinholes and protect until suitable exposure.')
 ],
 cementproof:[
  s('brush','Préparer le support minéral','Contrôler cohésion, fissures et humidité adaptée au système.','تحضير السطح المعدني','التحقق من التماسك والتشققات والرطوبة المناسبة.','Prepare mineral base','Assess soundness, cracks and suitable surface moisture.'),
  s('shield','Renforcer les interfaces','Traiter angles, relevés et traversées selon le complexe prévu.','تدعيم الزوايا','معالجة الزوايا والاختراقات والوصلات حسب النظام.','Detail junctions','Treat corners, penetrations and transitions.'),
  s('mix','Préparer les composants','Respecter la nature mono/bi-composante et le rapport validé.','تحضير المكونات','اتباع نظام المكون الواحد أو المكونين والنسب المعتمدة.','Prepare components','Confirm single/two-component system and approved mixing ratio.'),
  s('roller','Appliquer et protéger','Réaliser une couverture continue selon les couches et temps de cure prescrits.','التطبيق والحماية','وضع طبقة متصلة وفق مراحل المعالجة المعتمدة.','Apply and protect','Build continuous coverage and protect to the specified cure.')
 ],
 resin:[
  s('brush','Qualifier le support','Vérifier résistance, humidité, rugosité et propreté.','فحص السطح','قياس المقاومة والرطوبة والخشونة والنظافة.','Qualify substrate','Check strength, moisture, profile and cleanliness.'),
  s('beaker','Contrôler composants et sécurité','Identifier systèmes, ratios, durée de travail et ventilation selon FT/FDS approuvées.','فحص المكونات والسلامة','تحديد المكونات والنسب والسلامة والتهوية من النشرة المعتمدة.','Check components and safety','Verify components, ratios, working time and ventilation per approved TDS/SDS.'),
  s('mix','Préparer le mélange','Homogénéiser avec un équipement adapté et sans ratios supposés.','إعداد المزيج','الخلط بأداة مناسبة دون تخمين النسب.','Mix accurately','Use suitable tools and validated mixing proportions only.'),
  s('check','Appliquer et inspecter','Réaliser la méthode propre au système puis vérifier continuité et cure.','التطبيق والفحص','التنفيذ حسب النظام والتحقق من الاستمرارية والتصلب.','Apply and inspect','Follow the chosen system and check continuity and cure.')
 ],
 injection:[
  s('brush','Diagnostiquer la fissure','Identifier stabilité, largeur, humidité et débit éventuel ; faire qualifier les travaux.','تشخيص التشقق','فحص الاستقرار والعرض والرطوبة وتسرب الماء بواسطة مختص.','Assess crack','Determine movement, geometry, moisture and any ingress with a specialist.'),
  s('shield','Préparer les points d’injection','Définir packers, obturation, équipement et sécurité selon un protocole validé.','تحضير نقاط الحقن','تحديد نقاط الحقن والمعدات والحماية حسب بروتوكول معتمد.','Plan injection points','Specify ports, sealing, equipment and safety protocol.'),
  s('beaker','Préparer la résine','Contrôler composants et réaction ; ne pas extrapoler de ratio d’une autre résine.','تحضير الراتنج','فحص التفاعل والمكونات دون استعارة نسب منتج آخر.','Prepare resin','Validate components and reaction; do not transfer ratios from other resins.'),
  s('check','Injecter sous contrôle','Suivre le plan d’injection conçu par un professionnel, puis vérifier le résultat.','الحقن مع المراقبة','تنفيذ خطة الحقن بواسطة مختص والتحقق من النتيجة.','Inject under control','Use the specialist-designed procedure and verify outcome.')
 ],
 anchor:[
  s('shield','Dimensionner l’ancrage','Faire valider le support, les charges et les caractéristiques de la fixation.','تصميم التثبيت','اعتماد السطح والأحمال ومواصفات المراسي.','Design anchor','Validate substrate, loading and fixing specification.'),
  s('brush','Préparer le forage','Respecter diamètre, profondeur et nettoyage du forage validés pour le système.','تحضير الثقب','اتباع القطر والعمق والتنظيف المعتمد.','Prepare borehole','Use approved drilling geometry and hole-cleaning procedure.'),
  s('beaker','Préparer la cartouche','Vérifier produits, mélangeur statique, purge initiale et sécurité selon FT.','تجهيز الخرطوشة','فحص المكونات والفوهة والتخلص من الخليط الأولي حسب النشرة.','Prepare cartridge','Verify cartridge, mixing nozzle, initial purge and safety per TDS.'),
  s('check','Poser et contrôler','Mettre en place la tige et attendre le durcissement validé avant charge.','تركيب المرساة','تركيب القضيب وانتظار التصلب المعتمد قبل التحميل.','Install and check','Insert the fixing and verify approved cure before loading.')
 ],
 sealant:[
  s('brush','Préparer les lèvres','Nettoyer et vérifier l’adhérence sur les matériaux du joint.','تحضير جانبي الفاصل','تنظيف جانبي الفاصل وفحص الالتصاق.','Prepare joint faces','Clean and verify adhesion to both sides.'),
  s('shield','Définir le fond de joint','Adapter le fond de joint et le primaire si prescrits ; préserver la géométrie.','تحضير حشو الفاصل','اختيار حشو خلفي وطبقة أساس عند الحاجة.','Set joint backing','Choose backer and primer if specified, maintaining geometry.'),
  s('trowel','Extruder sans vides','Appliquer le mastic de manière continue dans les joints préparés.','ملء الفاصل','تطبيق المادة باستمرار ودون فراغات.','Apply sealant','Extrude continuously into prepared joints without voids.'),
  s('check','Lisser et protéger','Lisser avant formation de peau et respecter le temps de cure validé.','التنعيم والحماية','تنعيم السطح قبل تكوّن الغشاء واحترام التصلب.','Tool and protect','Finish before skin formation and protect during curing.')
 ],
 resinfloor:[
  s('brush','Préparer le sol','Contrôler état du béton, humidité et résistance.','تحضير الأرضية','فحص الخرسانة والرطوبة والمقاومة.','Prepare floor','Check concrete condition, moisture and strength.'),
  s('shield','Appliquer le primaire','Sélectionner le primaire et vérifier sa compatibilité au système.','تطبيق الأساس','اختيار المادة التمهيدية المتوافقة مع النظام.','Prime surface','Select the compatible primer.'),
  s('mix','Préparer la résine','Valider ratio A/B, temps utile, éventuelles charges et sécurité.','خلط الراتنج','التحقق من نسب المكونات والمدة والمواد المضافة والسلامة.','Mix resin','Verify component ratio, working time, fillers and safety.'),
  s('level','Répartir et contrôler','Étaler selon le système ; surveiller bulles, épaisseur, cure et remise en service.','التوزيع والفحص','فرد الطبقة وفحص الفقاعات والسماكة والمعالجة.','Spread and inspect','Control spreading, air release, thickness and cure.')
 ]
};
export const applicationModeByCode:Readonly<Record<string,keyof typeof patterns>>={
 'BOND-C1T':'tile','BOND-C1TE':'tile','BOND-C2FT':'tile','BOND-C2TE':'tile','BOND-C2TE-S1':'tile',
 'BOND-CG1':'grout','BOND-CG2WA':'grout','BOND-CT-C25-F5':'leveller',
 'BOND-GP-CSII':'render','BOND-GR-HR':'bedding','BOND-M10':'masonry','BOND-M5':'masonry','BOND-OC-CSIII':'render',
 'BOND-R2':'repair','BOND-R3':'repair','BOND-R4':'repair',
 'FLOW-AC':'admixture','FLOW-AE':'admixture','FLOW-CI':'admixture','FLOW-CURE':'cure',
 'FLOW-LAT':'latex','FLOW-RT':'admixture','FLOW-SP-HR':'admixture','FLOW-SP-PF':'admixture',
 'FLOW-SP-RT':'admixture','FLOW-VMA':'admixture','FLOW-WP':'admixture','FLOW-WR-N':'admixture',
 'PAINT-ENT-L':'putty','PAINT-FAC-EL':'paint','PAINT-FAC-M':'paint','PAINT-FAC-SX':'paint',
 'PAINT-INT-M':'paint','PAINT-INT-S':'paint','PAINT-INT-WA':'paint',
 'PAINT-PRIM-A':'primer','PAINT-PRIM-FX':'primer','PAINT-SOL-A':'paint','PAINT-TXT-F':'texture',
 'PROOF-ACR-RF':'membrane','PROOF-CM-O1P':'cementproof','PROOF-CM-O2P':'cementproof',
 'PROOF-EP-ANC':'anchor','PROOF-EP-INJ':'injection','PROOF-EP-PRIM':'resin','PROOF-EP-SB':'resin',
 'PROOF-EP-SR':'resinfloor','PROOF-PU-1K':'membrane','PROOF-PU-INJ':'injection','PROOF-PU-SEAL':'sealant'
};
if(Object.keys(applicationModeByCode).length!==50)throw Error('Application guide must map all 50 codes');
export const applicationStepsFor=(code:string,lang:Lang)=> {
 const mode=applicationModeByCode[code];
 if(!mode)throw Error('Application guide missing for '+code);
 return patterns[mode].map(step=>({
  title:step.title[lang],description:step.detail[lang],icon:step.icon,image:step.image??null
 }));
};
export const isTileAdhesive=(code:string)=>applicationModeByCode[code]==='tile';
