# Lot BOND — FENEK-BOND C1TE — dossier de justification technique

**Consultation : 17 novembre 2026 · Vérification laboratoire/fabricant requise.**
Cette note interne accompagne `src/data/fenek-c1te-reference.ts`. Les marques et liens cités ici **ne sont pas affichés sur le site public**.

## Classe revendiquée uniquement dans la désignation

**EN 12004-1:2017, C1TE** — C = mortier-colle cimentaire, 1 = adhérence normale, T = glissement vertical réduit, E = temps ouvert prolongé. L'existence de « C1TE » dans le nom de catalogue autorise à expliquer la *signification de la classe*, mais **ne démontre pas** que la formulation FENEK remplit les exigences.

- **C1** : adhérence en traction initiale, après immersion, après chaleur et après gel/dégel : chacune au moins **0,5 N/mm²** ; essai de temps ouvert normal : adhérence au moins **0,5 N/mm² à 20 min**.
- **T** : glissement vertical **≤ 0,5 mm**.
- **E** : adhérence en traction **≥ 0,5 N/mm² après un temps ouvert de 30 min**, lors d'un essai normalisé. Ce seuil n'est **pas** un délai universel de pose en plein soleil ou sur un support poreux.

Source primaire de repérage : [EN 12004-1:2017, classement et exigences](https://www.iteh.fr/catalog/standards/cen/48998e72-43b4-4ab9-9385-a9399c2c4689/en-12004-1-2017). Les essais doivent suivre les méthodes citées par le texte officiel en vigueur, sur la formule réelle du fabricant.

## Comparables indépendants : au moins trois fabricants

| Fabricant / produit (marché propre au fabricant) | Gâchage | Consommation | Autres valeurs utiles | Source |
| --- | --- | --- | --- | --- |
| Sika — SikaCeram-125 Easy Fix IN (C1TE) | 20–25 % d'eau en masse, soit **5–6,25 L/25 kg** à titre de conversion | env. **3–5,5 kg/m²** sur lits 3 à 5 mm | ouvert **>30 min** ; ajustement ~25 min (+27 °C) ; utilisation ≥180 min (+27 °C) | [Sika — page fabricant](https://ind.sika.com/en/construction/tile-installationsystems/tile-adhesives/sikaceram-125-easyfixin.html) |
| Mapei — Tixobond White (C1TE) | Ratio non retenu faute de source accessible à cette consultation | **1,2 kg/m²/mm** | ouvert **30 min** ; utilisation **>8 h** ; sol jointoyable ~24 h selon la documentation de ce produit | [Catalogue technique Mapei, section Tixobond](https://cdnmedia.mapei.com/docs/librariesprovider34/line-technical-documentation-documents/general-catalogue-mapei-januari-2020.pdf?sfvrsn=628fa371_8) |
| Weber / Saint-Gobain — weberset 303 (C1TE) | gris **26–29 %**, blanc **27–30 %**, soit **6,5–7,5 L/25 kg** comme équivalence mathématique | **2,9–7,2 kg/m²** selon format, épaisseur et double encollage | ouvert **30 min** ; ajustement **10 min** ; DPU env. **3 h** | [Weber — fiche produit](https://www.hk.weber/files/hk/2019-12/TDS%20weberset%20303%20-%20Product%20Sheet.pdf) |

**Lecture et limites :** les rapports d'eau, délais de prise et temps d'ajustement dépendent des formulations. Les conversions au sac de 25 kg ne sont **pas des consignes de gâchage FENEK**. Sur le site, afficher des plages de **famille** séparées du tableau des seuils **normatifs**, puis renvoyer à la FT applicable pour les gestes mettant en jeu la qualité de l'ouvrage. Les plages de consommation présentées sont approximatives et mélangent des peignes/épaisseurs différents ; elles sont utiles pour une comparaison éditoriale, pas pour une commande chantier.

## Métadonnées et traitements

- Source de vérité des chiffres : `docs/INTERNE-validation-donnees.csv`. Chaque ligne contient marque, URL, date de consultation, type et statut **« à valider par le fabricant/laboratoire »**.
- Fiche de présentation FR/AR/EN : `src/data/fenek-c1te-reference.ts` et `src/components/FenekC1TEPilot.astro`.
- Illustration : sprite C1TE existant, identité et SHA-256 toujours vérifiés ; la suppression de l'étiquette HTML `BROUILLON` est **éditoriale uniquement**.
- PDF : mise en page A4 d'Astro, export script hors réseau `scripts/export_c1t_pdfs.py`, six langues-fichiers sur deux références.
- Documents demandables : la FT/FDS **ne sont ni publiées ni fabriquées** par ce lot.

## Conditions avant fusion et commercialisation

1. Confirmer la classification C1TE de la **formulation réelle** par laboratoire compétent ; documenter les essais exigés par EN 12004-1/2.
2. Confirmer, ou retirer de la fiche si non validés, tous les usages, formats, dosages, temps de prise, températures et supports.
3. Relire français, arabe standard moderne et anglais de la fiche et du PDF.
4. Vérifier sur mobile, desktop, RTL et impression, sans modifier les 48 autres fiches.
5. Conserver `noindex` tant que la communication réglementaire ou commerciale et les documents associés n'ont pas été validés.
