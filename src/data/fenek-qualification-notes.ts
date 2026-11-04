/**
 * Critères éditoriaux contextualisés pour 50 fiches FENEK, 3 langues.
 * Les archives PDF fournies décrivent des références tierces : ces critères
 * sont des points à qualifier, pas des performances ni des valeurs FENEK.
 * Aucun dosage, certification, classification de danger ou norme n'est transféré.
 * Conditionnements et fiches produit officiels restent soumis à confirmation.
 */
import type {Lang} from './site';
type L=Record<Lang,string>;
const qualification:Record<string,L>={
  "BOND-C1T":{fr:"Contrôler l’adhérence, le support et la maniabilité du mortier pendant la pose.",en:"Check adhesion, substrate condition and mortar workability during tiling.",ar:"التحقق من الالتصاق وحالة السطح وقابلية تشغيل الملاط أثناء تركيب البلاط."},
  "BOND-C1TE":{fr:"Vérifier le temps ouvert sur les carreaux et supports prévus.",en:"Verify open time on the intended tiles and substrates.",ar:"التحقق من زمن التشغيل المفتوح على البلاط والأسطح المستهدفة."},
  "BOND-C2FT":{fr:"Évaluer la prise et l’adhérence avant toute indication de mise en service rapide.",en:"Assess setting and adhesion before any fast-service claim.",ar:"تقييم الشك والالتصاق قبل اعتماد أي ادعاء بشأن سرعة الاستعمال."},
  "BOND-C2TE":{fr:"Documenter le comportement à la pose, l’adhérence et le temps ouvert.",en:"Document installation behaviour, adhesion and open time.",ar:"توثيق سلوك التركيب والالتصاق وزمن التشغيل المفتوح."},
  "BOND-C2TE-S1":{fr:"Qualifier la déformabilité et l’adaptation aux mouvements du support par essais.",en:"Qualify deformability and accommodation of substrate movement through testing.",ar:"تقييم قابلية التشوه والتكيف مع حركة السطح من خلال الاختبارات."},
  "BOND-CG1":{fr:"Vérifier la largeur des joints, leur remplissage et l’aspect après nettoyage.",en:"Check joint width, filling and appearance after cleaning.",ar:"فحص عرض الفواصل وملئها والمظهر بعد التنظيف."},
  "BOND-CG2WA":{fr:"Évaluer le comportement à l’eau et l’abrasion sur des éprouvettes représentatives.",en:"Evaluate water exposure and abrasion behaviour on representative specimens.",ar:"تقييم سلوك الفواصل تجاه الماء والتآكل على عينات ممثلة."},
  "BOND-CT-C25-F5":{fr:"Contrôler la planéité, la fluidité et les conditions de recouvrement du sol.",en:"Check flatness, flow and conditions before covering the floor.",ar:"فحص استواء الأرضية والسيولة وشروط التغطية اللاحقة."},
  "BOND-GP-CSII":{fr:"Examiner le support de maçonnerie et l’adhérence de l’enduit courant.",en:"Examine masonry substrates and adhesion of general-purpose render.",ar:"فحص أسطح البناء والتصاق اللياسة ذات الاستعمال العام."},
  "BOND-GR-HR":{fr:"Vérifier le remplissage des volumes, les conditions de scellement et la résistance.",en:"Check void filling, grouting conditions and strength.",ar:"التحقق من ملء الفراغات وظروف التثبيت والمقاومة."},
  "BOND-M10":{fr:"Qualifier la maniabilité du mortier et la résistance des assemblages maçonnés.",en:"Qualify mortar workability and masonry joint strength.",ar:"تقييم قابلية تشغيل الملاط ومقاومة وصلات البناء."},
  "BOND-M5":{fr:"Contrôler la cohésion du mortier et la régularité des joints maçonnés.",en:"Check mortar cohesion and uniformity of masonry joints.",ar:"فحص تماسك الملاط وانتظام فواصل البناء."},
  "BOND-OC-CSIII":{fr:"Étudier la préparation de façade, l’épaisseur et la tenue de l’enduit.",en:"Study façade preparation, thickness and render performance.",ar:"دراسة تحضير الواجهة والسماكة وأداء اللياسة."},
  "BOND-R2":{fr:"Délimiter la réparation non structurelle et contrôler l’adhérence au béton préparé.",en:"Define non-structural repairs and check adhesion to prepared concrete.",ar:"تحديد نطاق الإصلاح غير الإنشائي وفحص الالتصاق بالخرسانة المحضرة."},
  "BOND-R3":{fr:"Évaluer la profondeur de réparation et les performances mécaniques requises.",en:"Assess repair depth and required mechanical performance.",ar:"تقييم عمق الإصلاح والخصائص الميكانيكية المطلوبة."},
  "BOND-R4":{fr:"Contrôler la stabilité du mortier frais et les exigences d’une réparation sollicitée.",en:"Check fresh mortar stability and demanding repair requirements.",ar:"فحص ثبات الملاط الطري ومتطلبات الإصلاح تحت الأحمال."},
  "FLOW-AC":{fr:"Mesurer les temps de prise sur la formulation béton réellement retenue.",en:"Measure setting times on the actual selected concrete mix.",ar:"قياس أزمنة الشك على خلطة الخرسانة المختارة فعليًا."},
  "FLOW-AE":{fr:"Contrôler la teneur en air et ses effets sur la cohésion du béton.",en:"Measure air content and its effect on concrete cohesion.",ar:"قياس محتوى الهواء وتأثيره على تماسك الخرسانة."},
  "FLOW-CI":{fr:"Définir l’exposition des armatures et le protocole de vérification anticorrosion.",en:"Define reinforcement exposure and corrosion-protection test protocol.",ar:"تحديد تعرض حديد التسليح وبروتوكول اختبار الحماية من التآكل."},
  "FLOW-CURE":{fr:"Vérifier la couverture et la protection du béton frais contre la dessiccation.",en:"Check coverage and drying protection of fresh concrete.",ar:"فحص تغطية الخرسانة الطرية وحمايتها من الجفاف."},
  "FLOW-LAT":{fr:"Évaluer l’adhérence des mortiers modifiés et la compatibilité avec les liants.",en:"Assess modified mortar bonding and binder compatibility.",ar:"تقييم التصاق الملاط المعدل والتوافق مع المواد الرابطة."},
  "FLOW-RT":{fr:"Documenter l’effet sur la prise et le maintien d’ouvrabilité à température réelle.",en:"Document the effect on setting and workability retention at actual temperatures.",ar:"توثيق التأثير على الشك والحفاظ على قابلية التشغيل عند درجات الحرارة الفعلية."},
  "FLOW-SP-HR":{fr:"Mesurer la réduction d’eau et la consistance avec le ciment prévu.",en:"Measure water reduction and consistency with the specified cement.",ar:"قياس خفض الماء والقوام باستعمال الإسمنت المحدد."},
  "FLOW-SP-PF":{fr:"Vérifier l’ouvrabilité et les résistances précoces en cycle de préfabrication.",en:"Verify workability and early strengths in precast production.",ar:"التحقق من قابلية التشغيل والمقاومات المبكرة في التصنيع المسبق."},
  "FLOW-SP-RT":{fr:"Mesurer la conservation de consistance pendant transport et mise en place.",en:"Measure consistency retention during transport and placement.",ar:"قياس الحفاظ على القوام أثناء النقل والصب."},
  "FLOW-VMA":{fr:"Contrôler la stabilité et le risque de ségrégation des bétons très fluides.",en:"Check stability and segregation risk of highly flowable concrete.",ar:"فحص ثبات الخرسانة عالية السيولة وخطر الانفصال الحبيبي."},
  "FLOW-WP":{fr:"Évaluer le comportement du béton ou mortier traité face à l’eau.",en:"Assess water-related behaviour of the treated concrete or mortar.",ar:"تقييم سلوك الخرسانة أو الملاط المعالج تجاه الماء."},
  "FLOW-WR-N":{fr:"Vérifier réduction d’eau, consistance et résistance sur une même formule.",en:"Check water reduction, consistency and strength on the same mix.",ar:"التحقق من خفض الماء والقوام والمقاومة على الخلطة نفسها."},
  "PAINT-ENT-L":{fr:"Vérifier la planéité et la préparation du fond, l’adhérence et le recouvrement.",en:"Check surface levelling, preparation, adhesion and overcoating.",ar:"فحص استواء السطح وتحضيره والالتصاق وإعادة الطلاء."},
  "PAINT-FAC-EL":{fr:"Qualifier le comportement du film au droit des microfissures de façade.",en:"Qualify film behaviour over façade microcracks.",ar:"تقييم سلوك طبقة الطلاء فوق الشقوق الدقيقة في الواجهة."},
  "PAINT-FAC-M":{fr:"Évaluer l’adhérence et la tenue de l’aspect mat sur support extérieur.",en:"Assess adhesion and durability of the matt finish on exterior substrates.",ar:"تقييم الالتصاق وثبات المظهر المطفي على الأسطح الخارجية."},
  "PAINT-FAC-SX":{fr:"Mesurer résistance à l’eau et transmission de vapeur du système de façade.",en:"Measure water resistance and vapour transmission of the façade system.",ar:"قياس مقاومة الماء ونفاذ بخار الماء لنظام الواجهة."},
  "PAINT-INT-M":{fr:"Contrôler l’opacité et l’uniformité du fini mat sur supports intérieurs.",en:"Check hiding power and matt finish uniformity on interior surfaces.",ar:"فحص قوة التغطية وتجانس التشطيب المطفي على الأسطح الداخلية."},
  "PAINT-INT-S":{fr:"Vérifier la régularité du satiné et la compatibilité avec le support.",en:"Check satin sheen uniformity and substrate compatibility.",ar:"فحص تجانس المظهر الساتاني والتوافق مع السطح."},
  "PAINT-INT-WA":{fr:"Évaluer la résistance aux lavages et à l’abrasion humide par essais.",en:"Evaluate washing and wet-scrub resistance through tests.",ar:"تقييم مقاومة الغسل والفرك الرطب من خلال الاختبارات."},
  "PAINT-PRIM-A":{fr:"Vérifier l’accrochage du primaire et sa compatibilité avec la finition.",en:"Verify primer adhesion and compatibility with the topcoat.",ar:"التحقق من التصاق الطلاء التمهيدي وتوافقه مع طبقة التشطيب."},
  "PAINT-PRIM-FX":{fr:"Contrôler la consolidation des fonds poreux avant finition.",en:"Check consolidation of porous substrates before finishing.",ar:"فحص تثبيت الأسطح المسامية قبل التشطيب."},
  "PAINT-SOL-A":{fr:"Évaluer l’état du béton, l’adhérence et les exigences d’usage du sol.",en:"Assess concrete condition, adhesion and floor service requirements.",ar:"تقييم حالة الخرسانة والالتصاق ومتطلبات استخدام الأرضية."},
  "PAINT-TXT-F":{fr:"Vérifier la régularité du relief décoratif et la préparation du fond.",en:"Check decorative texture uniformity and substrate preparation.",ar:"فحص تجانس الملمس الزخرفي وتحضير السطح."},
  "PROOF-ACR-RF":{fr:"Vérifier la continuité, l’adhérence et les relevés de la membrane de toiture.",en:"Check roof membrane continuity, adhesion and upstands.",ar:"فحص استمرارية غشاء السقف والتصاقه وارتفاعات العزل."},
  "PROOF-CM-O1P":{fr:"Examiner le support minéral et la continuité de l’étanchéité sous carrelage.",en:"Examine mineral substrates and continuity of waterproofing beneath tiles.",ar:"فحص السطح المعدني واستمرارية العزل المائي تحت البلاط."},
  "PROOF-CM-O2P":{fr:"Contrôler les composants du système, sa souplesse et ses raccords.",en:"Check system components, flexibility and junction detailing.",ar:"فحص مكونات النظام ومرونته وتفاصيل الوصلات."},
  "PROOF-EP-ANC":{fr:"Qualifier le support et la résistance d’ancrage par essais.",en:"Qualify substrate and anchor strength by testing.",ar:"تقييم السطح ومقاومة التثبيت من خلال الاختبارات."},
  "PROOF-EP-INJ":{fr:"Définir la géométrie des fissures et contrôler leur remplissage par injection.",en:"Define crack geometry and verify filling by injection.",ar:"تحديد هندسة الشقوق والتحقق من ملئها بالحقن."},
  "PROOF-EP-PRIM":{fr:"Vérifier l’humidité du fond et la compatibilité avec les couches de résine.",en:"Check substrate moisture and compatibility with resin layers.",ar:"فحص رطوبة السطح والتوافق مع طبقات الراتنج."},
  "PROOF-EP-SB":{fr:"Évaluer les surfaces d’assemblage et le comportement de la liaison collée.",en:"Assess joining surfaces and bonded joint performance.",ar:"تقييم أسطح التجميع وسلوك الوصلة اللاصقة."},
  "PROOF-EP-SR":{fr:"Contrôler planéité, primaire et contraintes du revêtement de sol.",en:"Check flatness, primer and floor coating service demands.",ar:"فحص الاستواء والطبقة التمهيدية ومتطلبات طلاء الأرضية."},
  "PROOF-PU-1K":{fr:"Qualifier l’adhérence et la continuité d’une membrane liquide de toiture.",en:"Qualify adhesion and continuity of the liquid roof membrane.",ar:"تقييم التصاق واستمرارية غشاء السقف السائل."},
  "PROOF-PU-INJ":{fr:"Évaluer le débit d’eau et le comportement de la résine dans la fissure.",en:"Assess water flow and resin behaviour inside the crack.",ar:"تقييم تدفق الماء وسلوك الراتنج داخل الشق."},
  "PROOF-PU-SEAL":{fr:"Définir la géométrie du joint, les mouvements et l’adhérence aux lèvres.",en:"Define joint geometry, movement and adhesion to joint faces.",ar:"تحديد هندسة الفاصل والحركات والالتصاق بجوانبه."}
};
export const FENEK_QUALIFICATION_CODES=Object.freeze(Object.keys(qualification));
export const qualificationFor=(code:string,lang:Lang):string=>{
  const row=qualification[code];
  if(!row)throw new Error('Missing qualification editorial entry for '+code);
  return row[lang];
};
