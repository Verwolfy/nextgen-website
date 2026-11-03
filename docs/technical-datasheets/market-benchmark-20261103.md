# FENEK — Benchmark technique externe et preuves manquantes (03/11/2026)

**INTERNE — NON APPROUVÉ — NE PAS PUBLIER LES VALEURS COMME CARACTÉRISTIQUES FENEK.**

## Résultat de l'étude
Les trois archives reçues comprennent 365 PDF de fiches techniques, 617 pages, mais **aucune FDS/SDS distincte**. Les chiffres recensés sont propres à des produits Granitex et à des fabricants publics, Sika, Mapei, Saint-Gobain Weber, Henkel Ceresit et Fosroc. Le rapprochement de deux fournisseurs peut confirmer l'existence d'une plage de marché, mais **jamais confirmer la performance ni la formulation d'un produit NextGen**.

La recette industrielle exacte (pourcentages matière première, tolérances) n'est généralement pas révélée par une fiche technique publique. Les descriptifs « ciment/polymères », « solution de polycarboxylates », « résine acrylique » ou « époxy A/B » désignent une famille chimique, pas une formule NextGen.

## Exemples vérifiés, jamais attribués à NextGen

| Référence tierce | Donnée propre au tiers | Divergence / limite |
|---|---|---|
| GRANIPAN F10 FR | ≈ 2 kg/m²/mm, sac 25 kg | AR annonce 40 kg |
| MEDAPLAST SP40 FR | 0,6–2,5 % masse ciment | Conditionnements différents EN/AR |
| MEDAPOXY PRIMER | FR 350–450 vs EN 300–400 g/m² | Versions non concordantes |
| SikaCeram-205 Nigeria | 5,5–6 L d'eau par 25 kg | Autres pays Sika affichent des données différentes |
| Keraflex Mapei UK | 5–5,4 L eau par 20 kg (gris) | Formule Mapei différente |
| Ceresit CM11 Henkel MEA | 5–5,5 L eau par 25 kg | Classe et preuve Henkel uniquement |
| Sika ViscoCrete-20 HE GCC | 0,2–0,8 % et 1–2 % masse ciment selon emploi | Dosage final soumis aux essais béton |
| Mapelastic Smart Mapei | ≈ 1,6 kg/m²/mm | Membrane bicomposant propre à Mapei |
| Elastocolor Paint Mapei | 0,2–0,4 kg/m²/couche | Peinture de façade spécifique |

## Composition qualitative fabricant, PAS formulation de NextGen

- SikaCeram-205 : poudre cimentaire modifiée par polymères, selon la fiche Sika Nigeria.
- Ceresit CM11 : ciment, charges minérales et modifiants, selon Henkel MEA.
- Sika ViscoCrete-20 HE : solution aqueuse de polycarboxylates modifiés, selon Sika GCC.
- Mapelastic Smart : liants cimentaires, granulats fins, additifs et polymères en dispersion, selon Mapei.
- Elastocolor Paint : résine acrylique en dispersion aqueuse, selon Mapei.

Ces dénominations ne décrivent pas la recette industrielle exacte, les pourcentages ou les matières premières autorisées de FENEK.

## Fichiers annexes
- `market-values.csv` : 27 mesures/paramètres de tiers, source exacte, réserve et marquage `DONNEE_TIERS_SEULEMENT`.
- `market-crosswalk-50.csv` : comparaison d'orientation des **50 SKU**, analogies de famille seulement. Les 50 ont `BLOQUE`.
- Les 150 fiches sous `drafts/` ne sont pas enrichies de valeurs tierces et ne sont pas publiables.

## Étapes avant validation des FT FENEK
1. Formule réelle et versions des matières premières, spécifications et lot pilote signés R&D.
2. Programme d'essais par famille BOND/FLOW/PROOF/PAINT et rapport signé par SKU.
3. Mesure de dosage/consommation en conditions réelles définies (support, épaisseur, température, ciment).
4. Conditionnements, stockage, durée de conservation confirmés par production.
5. **FDS NextGen distincte**, établie depuis la composition réelle et revue HSE.
6. Classe normative seulement si méthode et résultats l'attestent ; codes (C1T, R3, etc.) ne suffisent pas.
7. Figer valeurs maîtresses, traduire FR/AR/EN, vérifier les nombres, unités et mise en page RTL.
8. Validation R&D + Qualité + HSE + Juridique avant PDF officiel et diffusion.

## Liens officiels des fabricants
- SikaCeram-205 Nigeria : https://nga.sika.com/en/construction/building-finishing/cementitious-tileadhesive/high-performancetileadhesivec2teclass/sikaceram-205.html
- Keraflex Mapei UK : https://cdnmedia.mapei.com/docs/librariesprovider12/products-documents/1_00106_keraflex_en-gb_c667fd8afef34404b2717baabec0c34c.pdf?sfvrsn=a52ad23e_0
- Ceresit CM11 Henkel MEA : https://dm.henkel-dam.com/is/content/henkel/TDS_CERESIT-CM-11_EN_MEA
- webercol flex Saint-Gobain France : https://www.fr.weber/pose-du-carrelage/les-colles-en-poudre-mortiers-colles/webercol-flex
- Sika ViscoCrete-20 HE GCC : https://gcc.sika.com/en/construction/concrete/water-reducers/pce-based-super-plasticizers/sika-viscocrete-20he.html
- Mapelastic Smart Mapei : https://cdnmedia.mapei.com/docs/librariesprovider17/products-documents/1_02013_mapelastic-smart_en_afe12a9717534cecb7bf575e6388968b.pdf?sfvrsn=b9cf5de3_0
- Elastocolor Paint Mapei : https://cdnmedia.mapei.com/docs/librariesprovider21/products-documents/1_elastocolor-paint_329-7-2017_226442349f50406dabd770ac8def7a3e.pdf?sfvrsn=df468b48_0
- Auramix 400 Fosroc : https://www.fosroc.com/product/show/auramix-400

**Ne pas fusionner cette PR de brouillons dans main public avant approbation industrielle. Aucune FDS NextGen ni formulation réelle vérifiée n'a été fournie.**
