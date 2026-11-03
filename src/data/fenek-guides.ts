import type { Lang, Range } from './site';

type L = Record<Lang,string>;
type Profile = { focus: L; checks: L; };
const l=(fr:string, ar:string, en:string):L=>({fr,ar,en});

/**
 * Technical topic synthesis from the structure of the 365 user-supplied FR/AR/EN
 * reference PDFs: fields to consider, NEVER measured FENEK characteristics.
 * The named FENEK catalogue supplies identity, positioning and applications.
 */
const topics:Record<string,Profile> = {
  tile:{
    focus:l('Mortier-colle pour le carrelage ; les propriétés à documenter incluent l’adhérence, le temps ouvert et le comportement à la pose.',
      'ملاط لاصق للبلاط؛ تشمل الخصائص التي ينبغي توثيقها الالتصاق وزمن الفتح والسلوك أثناء التركيب.',
      'Tile-setting adhesive mortar; characteristics to document include adhesion, open time and installation behaviour.'),
    checks:l('Type de carreaux, nature et planéité du support, dimensions, usage intérieur ou extérieur et conditions du chantier.',
      'نوع البلاط وطبيعة السطح واستواؤه وأبعاده والاستعمال الداخلي أو الخارجي وظروف الورشة.',
      'Tile type, substrate condition and flatness, dimensions, interior or exterior use, and site conditions.')
  },
  grout:{
    focus:l('Mortier pour joints de carrelage ; les points de contrôle comprennent la largeur des joints, la résistance à l’usure et à l’eau.',
      'ملاط لملء فواصل البلاط؛ تشمل نقاط الفحص عرض الفواصل ومقاومة التآكل والماء.',
      'Tile grout; relevant checks include joint width, wear resistance and water exposure.'),
    checks:l('Géométrie des joints, état de prise du revêtement, propreté des bords et contraintes d’entretien.',
      'أبعاد الفواصل واكتمال تماسك البلاط ونظافة الحواف ومتطلبات الصيانة.',
      'Joint dimensions, tile setting completion, edge cleanliness and maintenance requirements.')
  },
  leveller:{
    focus:l('Mortier de ragréage ou d’égalisation des sols ; critères à caractériser : planéité, fluidité, épaisseur et délai de recouvrement.',
      'ملاط لتسوية الأرضيات؛ تشمل معايير التقييم الاستواء والسيولة والسماكة ومدة الانتظار قبل التغطية.',
      'Floor-levelling mortar; key parameters are flatness, flow, layer thickness and time before covering.'),
    checks:l('Support porteur, cohésion superficielle, humidité, dénivelés et nature du revêtement ultérieur.',
      'قدرة السطح على التحمل وتماسكه ورطوبته وفروق المناسيب ونوع الغطاء النهائي.',
      'Load-bearing substrate, surface cohesion, moisture, unevenness and subsequent floor finish.')
  },
  render:{
    focus:l('Enduit de protection ou de finition des parois ; paramètres à étudier : adhérence, absorption d’eau et résistance mécanique.',
      'لياسة حماية أو تشطيب للجدران؛ تشمل الخصائص الواجب تقييمها الالتصاق وامتصاص الماء والمقاومة الميكانيكية.',
      'Protective or finishing wall render; relevant parameters include adhesion, water absorption and mechanical resistance.'),
    checks:l('Maçonnerie ou béton support, état des joints, exposition climatique et système de finition envisagé.',
      'سطح البناء أو الخرسانة وحالة الفواصل والتعرض للعوامل الجوية ونظام التشطيب المقترح.',
      'Masonry or concrete substrate, joint condition, weather exposure and the proposed finish system.')
  },
  masonry:{
    focus:l('Mortier de maçonnerie ; points de contrôle : consistance, résistance, adhérence aux éléments et durabilité du joint.',
      'ملاط للبناء؛ تشمل نقاط التقييم القوام والمقاومة والالتصاق بعناصر البناء ومتانة الفواصل.',
      'Masonry mortar; key checks are consistency, strength, bond to masonry units and joint durability.'),
    checks:l('Type de blocs ou briques, épaisseur de joint, support, humidité et prescriptions du chantier.',
      'نوع الكتل أو الطوب وسماكة الفواصل والسطح والرطوبة ومتطلبات المشروع.',
      'Block or brick type, joint thickness, substrate, moisture and project requirements.')
  },
  bedding:{
    focus:l('Mortier de calage et de scellement ; contrôles usuels : remplissage, stabilité volumique et résistance après durcissement.',
      'ملاط للملء والتثبيت؛ تشمل الفحوص المعتادة اكتمال الملء والثبات الحجمي والمقاومة بعد التصلب.',
      'Bedding and grouting mortar; relevant checks are cavity filling, dimensional stability and hardened strength.'),
    checks:l('Dimensions et profondeur des vides, support, accès à la zone de scellement et charges prévues.',
      'أبعاد وعمق الفراغات والسطح وإمكانية الوصول إلى موضع التثبيت والأحمال المتوقعة.',
      'Void depth and geometry, substrate, access to the grouting area and anticipated loads.')
  },
  repair:{
    focus:l('Mortier destiné à la réparation du béton ; propriétés à évaluer : adhérence, retrait, résistances et compatibilité du support.',
      'ملاط لإصلاح الخرسانة؛ تُقيّم فيه قوة الالتصاق والانكماش والمقاومة والتوافق مع السطح.',
      'Concrete repair mortar; relevant properties include adhesion, shrinkage, strength and substrate compatibility.'),
    checks:l('Étendue du défaut, béton sain, présence d’armatures, profondeur de réparation et exposition de l’ouvrage.',
      'حجم العيب وسلامة الخرسانة ووجود حديد التسليح وعمق الإصلاح وتعرّض المنشأة.',
      'Defect extent, sound concrete, reinforcement condition, repair depth and structure exposure.')
  },
  reducer:{
    focus:l('Adjuvant réducteur d’eau ou superplastifiant ; critères usuels : ouvrabilité, maintien de consistance et résistances du béton.',
      'مادة مضافة مخفضة للماء أو ملدن فائق؛ تشمل معايير التقييم قابلية التشغيل والحفاظ على القوام ومقاومة الخرسانة.',
      'Water-reducing or superplasticising admixture; typical parameters are workability, slump retention and concrete strength.'),
    checks:l('Nature du ciment, composition des granulats, rapport eau/liant, adjuvants associés et essais de convenance.',
      'نوع الإسمنت وتركيب الركام ونسبة الماء إلى الرابط والإضافات الأخرى واختبارات الملاءمة.',
      'Cement type, aggregate grading, water/binder ratio, other admixtures and concrete compatibility trials.')
  },
  setcontrol:{
    focus:l('Adjuvant modifiant la cinétique de prise ; critères : prise, ouvrabilité, température et évolution des résistances.',
      'مادة مضافة للتحكم في زمن الشك؛ تشمل المعايير الشك وقابلية التشغيل والحرارة وتطور المقاومة.',
      'Setting-control admixture; parameters include setting time, workability, temperature and strength development.'),
    checks:l('Formulation du ciment, temps de transport, température ambiante et compatibilité avec les autres adjuvants.',
      'تركيبة الإسمنت ومدة النقل ودرجة حرارة الجو والتوافق مع الإضافات الأخرى.',
      'Cement formulation, transport time, ambient temperature and admixture compatibility.')
  },
  air:{
    focus:l('Adjuvant entraîneur d’air ; les paramètres de référence sont le volume d’air entraîné, la stabilité et les résistances.',
      'مادة مضافة لإدخال الهواء؛ تشمل المعايير نسبة الهواء المحبوس وثباتها وتأثيرها في المقاومة.',
      'Air-entraining admixture; reference parameters are entrained-air content, stability and strengths.'),
    checks:l('Type de béton, mode de malaxage, temps de transport et contrôle de l’air du béton frais.',
      'نوع الخرسانة وطريقة الخلط ومدة النقل وقياس الهواء في الخرسانة الطرية.',
      'Concrete type, mixing method, transportation time and fresh-concrete air measurement.')
  },
  corrosion:{
    focus:l('Adjuvant à fonction inhibitrice de corrosion ; l’évaluation porte sur l’environnement et la protection des armatures.',
      'مادة مضافة موجهة للحد من تآكل التسليح؛ يركز تقييمها على البيئة المحيطة وحماية الحديد.',
      'Corrosion-inhibiting admixture category; evaluation focuses on exposure environment and reinforcement protection.'),
    checks:l('Exposition aux chlorures, enrobage des armatures, composition du béton et essais adaptés.',
      'التعرض للكلوريدات وسمك غطاء حديد التسليح وتركيبة الخرسانة والاختبارات الملائمة.',
      'Chloride exposure, reinforcement cover, concrete composition and suitable testing.')
  },
  cure:{
    focus:l('Produit de cure du béton ; points de référence : formation du film, rétention d’eau et compatibilité des traitements ultérieurs.',
      'منتج لمعالجة الخرسانة؛ تشمل المعايير تكوّن الغشاء والاحتفاظ بالماء والتوافق مع المعالجات اللاحقة.',
      'Concrete curing product; reference criteria include film formation, water retention and compatibility with later treatments.'),
    checks:l('État du béton frais, conditions d’évaporation, type de surface et traitements prévus après la cure.',
      'حالة الخرسانة الطازجة وظروف التبخر ونوع السطح والعمليات اللاحقة للمعالجة.',
      'Fresh-concrete state, evaporation conditions, surface type and treatments after curing.')
  },
  latex:{
    focus:l('Résine d’adhérence pour mortiers ; les points à documenter sont la liaison au support, la compatibilité et la résistance.',
      'راتنج لتحسين التصاق الملاط؛ تشمل الخصائص الالتصاق بالسطح والتوافق والمقاومة.',
      'Bonding resin for mortars; parameters to document include substrate bond, compatibility and strength.'),
    checks:l('État du support, système de mortier associé et délai entre couche de liaison et mortier.',
      'حالة السطح ونظام الملاط المستخدم والمدة بين طبقة الربط والملاط.',
      'Substrate condition, associated mortar system and timing between bonding coat and mortar.')
  },
  vma:{
    focus:l('Agent de viscosité pour béton ; propriétés à évaluer : stabilité, ségrégation et rhéologie à l’état frais.',
      'مادة للتحكم في لزوجة الخرسانة؛ تشمل الخصائص الثبات ومقاومة الانفصال والخواص الانسيابية في الحالة الطرية.',
      'Viscosity-modifying admixture; key properties are stability, segregation resistance and fresh-state rheology.'),
    checks:l('Proportions eau/fines, type de granulats, béton autoplaçant et essais d’écoulement.',
      'نسبة الماء إلى المواد الناعمة ونوع الركام والخرسانة ذاتية الدمك واختبارات الجريان.',
      'Water/fines content, aggregate type, self-compacting concrete and flow testing.')
  },
  waterproofmix:{
    focus:l('Adjuvant hydrofuge de masse ; l’étude porte sur l’absorption d’eau, l’étanchéité et la compatibilité du mélange.',
      'مادة مضافة لتقليل نفاذية الماء داخل الخلطة؛ يشمل التقييم امتصاص الماء والعزل والتوافق.',
      'Integral waterproofing admixture; evaluation concerns water absorption, resistance to penetration and mixture compatibility.'),
    checks:l('Granulométrie, teneur en liant, cure du béton et agressivité du milieu.',
      'التدرج الحبيبي ونسبة الرابط ومعالجة الخرسانة وشدة تعرضها للوسط.',
      'Grading, binder content, concrete curing and exposure conditions.')
  },
  paint:{
    focus:l('Revêtement de peinture pour parois ; critères usuels : rendement, adhérence, opacité et entretien de la finition.',
      'طلاء للجدران؛ تشمل معايير التقييم معدل التغطية والالتصاق وقوة الإخفاء وصيانة التشطيب.',
      'Wall paint coating; typical criteria are coverage, adhesion, opacity and finish maintenance.'),
    checks:l('Nature du fond, propreté, humidité, ancienne peinture et environnement intérieur ou extérieur.',
      'طبيعة السطح ونظافته ورطوبته والطلاء السابق والبيئة الداخلية أو الخارجية.',
      'Substrate nature, cleanliness, moisture, existing coatings and interior/exterior exposure.')
  },
  primer:{
    focus:l('Primaire ou fixateur de fond ; paramètres : pénétration, adhérence et compatibilité avec la couche suivante.',
      'طبقة أساس أو مثبت للسطح؛ تشمل المعايير النفاذية والالتصاق والتوافق مع الطلاء التالي.',
      'Primer or substrate consolidator; parameters include penetration, adhesion and compatibility with topcoats.'),
    checks:l('Porosité, farinage, humidité, alcalinité du fond et peinture de finition.',
      'مسامية السطح وتطبشه ورطوبته وقلويته ونوع طلاء التشطيب.',
      'Porosity, chalking, substrate moisture, alkalinity and planned topcoat.')
  },
  putty:{
    focus:l('Enduit de lissage en pâte ; critères : finesse, aptitude au ponçage, épaisseur et recouvrabilité.',
      'معجون تنعيم جاهز؛ تشمل المعايير نعومة السطح وقابلية الصنفرة والسماكة وإمكانية الطلاء بعده.',
      'Ready-mixed smoothing filler; parameters include fineness, sandability, thickness and overcoating.'),
    checks:l('Planéité du mur, trous ou fissures, porosité et finition choisie.',
      'استواء الجدار والثقوب والشقوق والمسامية ونوع التشطيب.',
      'Wall flatness, holes or cracks, porosity and selected finish.')
  },
  floorcoat:{
    focus:l('Revêtement de sol ; critères : adhérence, résistance à l’usure, trafic et entretien.',
      'طلاء للأرضيات؛ تشمل المعايير الالتصاق ومقاومة التآكل وحركة المرور والصيانة.',
      'Floor coating; parameters include adhesion, wear resistance, traffic and maintenance.'),
    checks:l('État et humidité du support, zones de circulation, nettoyage et conditions d’exposition.',
      'حالة السطح ورطوبته ومناطق المرور والتنظيف وظروف التعرض.',
      'Substrate condition and moisture, traffic areas, cleaning and exposure conditions.')
  },
  texture:{
    focus:l('Revêtement décoratif texturé ; critères : rendu, homogénéité du grain, adhérence et entretien.',
      'طلاء زخرفي ذو ملمس؛ تشمل المعايير المظهر وتجانس الحبيبات والالتصاق والصيانة.',
      'Decorative textured coating; criteria include appearance, texture uniformity, adhesion and maintenance.'),
    checks:l('Régularité du support, teinte, zone de raccord et technique de finition.',
      'انتظام السطح واللون ومناطق الوصل وطريقة التشطيب.',
      'Substrate regularity, shade, jointing areas and finishing technique.')
  },
  membrane:{
    focus:l('Système de protection contre l’eau ; critères : continuité, adhérence, épaisseur de film et traitement des points singuliers.',
      'نظام للحماية من الماء؛ تشمل المعايير استمرارية الطبقة والالتصاق وسماكة الغشاء ومعالجة التفاصيل.',
      'Water-protection system; criteria include continuity, adhesion, film thickness and detailing.'),
    checks:l('Support, fissures, relevés, traversées, joints, eau sous pression et destination de l’ouvrage.',
      'السطح والتشققات والحواف والاختراقات والفواصل وضغط الماء والغرض من المنشأة.',
      'Substrate, cracks, upstands, penetrations, joints, water pressure and structure purpose.')
  },
  epoxy:{
    focus:l('Système à base de résine ; critères : rapport de composants si applicable, adhérence, résistance et temps de travail.',
      'نظام يعتمد على الراتنج؛ تشمل المعايير نسبة المكونات عند الاقتضاء والالتصاق والمقاومة ومدة التشغيل.',
      'Resin-based system; key parameters are component ratio where relevant, adhesion, strength and working time.'),
    checks:l('Support, taux d’humidité, compatibilité chimique, usage prévu et conditions de ventilation.',
      'السطح ونسبة الرطوبة والتوافق الكيميائي والغرض من الاستخدام وظروف التهوية.',
      'Substrate, moisture content, chemical compatibility, intended use and ventilation.')
  },
  injection:{
    focus:l('Résine d’injection pour fissures ou venues d’eau ; critères : viscosité, réaction, injection et durcissement.',
      'راتنج لحقن الشقوق أو تسربات الماء؛ تشمل المعايير اللزوجة والتفاعل والحقن والتصلب.',
      'Injection resin for cracks or water ingress; criteria include viscosity, reaction, injection and curing.'),
    checks:l('Nature de la fissure, débit d’eau, accès aux points d’injection et protocole spécialisé.',
      'طبيعة الشق وتدفق الماء وإمكانية الوصول لنقاط الحقن والبروتوكول المتخصص.',
      'Crack type, water flow, injection point access and the specialist procedure.')
  },
  sealant:{
    focus:l('Mastic pour joints ; critères : déformation admissible, adhérence aux lèvres et compatibilité de support.',
      'معجون لسد الفواصل؛ تشمل المعايير الحركة المقبولة والالتصاق بحواف الفاصل والتوافق مع السطح.',
      'Joint sealant; criteria include allowable movement, adhesion to joint sides and substrate compatibility.'),
    checks:l('Largeur et profondeur du joint, support, fond de joint et mouvements attendus.',
      'عرض الفاصل وعمقه ونوع السطح والحشو الخلفي والحركة المتوقعة.',
      'Joint width and depth, substrate, backing material and anticipated movement.')
  },
};

const byRange:Record<Range,{before:L; method:L; after:L; quantity:L; safety:L}> = {
  bond:{
    before:l('Examiner la stabilité, la propreté, la cohésion et l’humidité du support. Définir le système de pose ou de réparation à partir du dossier technique du chantier.',
      'فحص ثبات السطح ونظافته وتماسكه ورطوبته وتحديد نظام التركيب أو الإصلاح بناءً على الملف الفني للمشروع.',
      'Assess substrate stability, cleanliness, cohesion and moisture. Select the installation or repair system from the project’s technical specification.'),
    method:l('Préparer et mélanger le matériau suivant la procédure propre à la référence ; appliquer avec les outils adaptés à l’usage identifié.',
      'تحضير المادة وخلطها وفق الإجراءات الخاصة بالمرجع وتطبيقها بالأدوات الملائمة للاستخدام المحدد.',
      'Prepare and mix according to the reference-specific procedure, then apply with tools suited to the intended use.'),
    after:l('Respecter les conditions de protection, de prise, de cure et de recouvrement indiquées dans les instructions définitives du produit.',
      'الالتزام بشروط الحماية والشك والمعالجة والتغطية اللاحقة وفق تعليمات المنتج النهائية.',
      'Observe the protection, setting, curing and overcoating conditions stated in the final product instructions.'),
    quantity:l('La quantité dépend du support, de la surface, de l’épaisseur et du mode d’application. Le taux chiffré ne peut être établi qu’à partir de la référence et d’un essai de convenance.',
      'تعتمد الكمية على السطح والمساحة والسماكة وطريقة التطبيق. ولا تُحدد قيمة رقمية إلا استنادًا إلى المرجع واختبار الملاءمة.',
      'Quantity depends on the substrate, area, thickness and application method. A numerical rate must come from the specific product and suitability trials.'),
    safety:l('Examiner la FDS du produit et les exigences de protection avant le gâchage et l’application.',
      'الاطلاع على صحيفة بيانات السلامة ومتطلبات الحماية قبل الخلط والتطبيق.',
      'Review the product SDS and protective requirements before mixing and application.')
  },
  flow:{
    before:l('Définir la formule béton/mortier, les matériaux, le temps de transport et les performances à contrôler.',
      'تحديد خلطة الخرسانة أو الملاط والمواد ومدة النقل والخصائص المطلوب ضبطها.',
      'Define the concrete/mortar mix, materials, transport time and properties to monitor.'),
    method:l('Vérifier la compatibilité avec le ciment et les autres adjuvants. Fixer l’ordre d’incorporation uniquement après essais de convenance.',
      'التحقق من التوافق مع الإسمنت والإضافات الأخرى وتحديد ترتيب الإضافة بعد اختبارات الملاءمة.',
      'Check compatibility with cement and other admixtures. Establish the addition sequence only after compatibility trials.'),
    after:l('Contrôler le béton ou mortier frais, puis les performances du matériau durci selon le plan d’essais.',
      'مراقبة الخرسانة أو الملاط في الحالة الطرية ثم أداء المادة بعد التصلب وفق خطة الاختبار.',
      'Check fresh concrete or mortar and then hardened material performance against the test plan.'),
    quantity:l('Le dosage se définit par essais sur une formulation précise. Il peut varier avec le ciment, la température et les autres composants ; aucune valeur universelle ne s’applique.',
      'تُحدد الجرعة بالاختبارات على خلطة محددة وقد تتغير حسب الإسمنت والحرارة والمكونات الأخرى؛ ولا توجد جرعة عامة صالحة للجميع.',
      'Dosage is established by trials on a defined mix. It varies with cement, temperature and other ingredients; there is no universal rate.'),
    safety:l('Consulter les données de sécurité propres à l’adjuvant et les exigences de stockage, manutention et incorporation.',
      'الاطلاع على بيانات السلامة الخاصة بالمادة المضافة ومتطلبات التخزين والمناولة والإضافة.',
      'Refer to the admixture-specific safety information and handling, storage and addition requirements.')
  },
  paint:{
    before:l('Vérifier l’état du support, sa propreté, son humidité, sa porosité et la compatibilité avec l’ancien système.',
      'فحص حالة السطح ونظافته ورطوبته ومسامه والتوافق مع الطلاء القديم.',
      'Inspect substrate condition, cleanliness, moisture, porosity and compatibility with existing coatings.'),
    method:l('Prévoir la préparation du fond, le primaire éventuel et le nombre de couches selon le système de peinture validé.',
      'تحديد تحضير السطح وطبقة الأساس عند الحاجة وعدد الطبقات حسب نظام الطلاء المعتمد.',
      'Plan substrate preparation, any necessary primer and the number of coats according to the validated coating system.'),
    after:l('Vérifier l’uniformité du rendu et respecter les délais de séchage et de remise en service propres au produit.',
      'التحقق من تجانس المظهر واحترام فترات الجفاف وإعادة الاستعمال الخاصة بالمنتج.',
      'Check finish uniformity and follow product-specific drying and return-to-service periods.'),
    quantity:l('Le rendement dépend notamment de la rugosité, du pouvoir absorbant, de la teinte et de l’épaisseur du film ; il doit être contrôlé sur support réel.',
      'يعتمد المردود على خشونة السطح وامتصاصه واللون وسماكة الغشاء، ويجب التحقق منه على سطح فعلي.',
      'Coverage depends on surface roughness, absorbency, colour and film thickness; it must be checked on the actual substrate.'),
    safety:l('Vérifier la compatibilité des produits, la ventilation requise et les dispositions de sécurité spécifiques à la formulation.',
      'التحقق من توافق المنتجات والتهوية اللازمة وإجراءات السلامة الخاصة بالتركيبة.',
      'Check product compatibility, ventilation needs and formulation-specific safety precautions.')
  },
  proof:{
    before:l('Identifier l’exposition à l’eau, les joints, fissures, relevés et traversées ; contrôler l’état du support.',
      'تحديد التعرض للماء والفواصل والشقوق والحواف والاختراقات وفحص حالة السطح.',
      'Identify water exposure, joints, cracks, upstands and penetrations; inspect substrate condition.'),
    method:l('Définir la préparation, les composants, les épaisseurs et la séquence d’application par un système d’étanchéité spécifiquement validé.',
      'تحديد التحضير والمكونات والسماكات وتسلسل التطبيق وفق نظام عزل مائي تم التحقق منه خصيصًا.',
      'Set preparation, components, thicknesses and application sequence using a specifically validated waterproofing system.'),
    after:l('Inspecter la continuité et les détails du système ; respecter la cure et les contrôles préalables à la mise en eau ou à l’exploitation.',
      'فحص استمرارية نظام العزل وتفاصيله واحترام مدة التصلب والفحوص قبل التعرض للماء أو التشغيل.',
      'Inspect system continuity and details; follow curing and checks before water exposure or service.'),
    quantity:l('La consommation dépend du procédé, de la porosité, du nombre de couches et de la géométrie. Seule une méthode validée pour la référence permet de fixer une valeur.',
      'يتوقف الاستهلاك على النظام والمسامية وعدد الطبقات وشكل السطح؛ ولا تُحدد قيمة إلا بطريقة معتمدة للمرجع.',
      'Consumption depends on the method, porosity, number of coats and geometry. Only the validated product method can establish a numerical rate.'),
    safety:l('Contrôler les exigences HSE, la ventilation, les composants éventuels et les limites d’exposition avant toute intervention.',
      'مراجعة متطلبات الصحة والسلامة والتهوية والمكونات المحتملة وحدود التعرض قبل العمل.',
      'Check HSE requirements, ventilation, any component system and exposure restrictions before work.')
  },
};
export const profileKeyFor = (code:string):string => {
  if(code.startsWith('BOND-')){
    if(/^BOND-C[12]/.test(code))return 'tile';
    if(code.startsWith('BOND-CG'))return 'grout';
    if(code.startsWith('BOND-CT'))return 'leveller';
    if(code.startsWith('BOND-GR'))return 'bedding';
    if(/^BOND-(GP|OC)/.test(code))return 'render';
    if(/^BOND-M/.test(code))return 'masonry';
    return 'repair';
  }
  if(code.startsWith('FLOW-')){
    if(/^FLOW-(SP|WR)/.test(code))return 'reducer';
    if(/^FLOW-(AC|RT)/.test(code))return 'setcontrol';
    const map:Record<string,string>={'AE':'air','CI':'corrosion','CURE':'cure','LAT':'latex','VMA':'vma','WP':'waterproofmix'};
    return map[code.slice(5)]??'reducer';
  }
  if(code.startsWith('PAINT-')){
    if(code.includes('PRIM'))return 'primer';
    if(code.includes('ENT-'))return 'putty';
    if(code.includes('SOL-'))return 'floorcoat';
    if(code.includes('TXT-'))return 'texture';
    return 'paint';
  }
  if(code.startsWith('PROOF-')){
    if(code.includes('INJ'))return 'injection';
    if(code.includes('SEAL'))return 'sealant';
    if(/(ACR|CM-|PU-1K)/.test(code))return 'membrane';
    return 'epoxy';
  }
  throw new Error('Unknown FENEK family: '+code);
};
export const guideFor = (code:string,range:Range,lang:Lang) => {
  const profile=topics[profileKeyFor(code)];
  if(!profile)throw new Error('Missing technical topic for '+code);
  const shared=byRange[range];
  return {
    focus:profile.focus[lang],checks:profile.checks[lang],
    before:shared.before[lang],method:shared.method[lang],after:shared.after[lang],
    quantity:shared.quantity[lang],safety:shared.safety[lang],
  };
};
