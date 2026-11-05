# Lot 69 — FENEK-PROOF EP-PRIM : seau A 10 kg + seau B 3 kg

Date : 2026-11-05.

## Confirmation utilisateur

« seau A de 10 Kg et Seau B de 3 Kg » pour FENEK-PROOF EP-PRIM.

- Présentation : **kit composé d'un seau A de 10 kg et d'un seau B de 3 kg**.
- Masse nominale du contenu : **13 kg au total** (sans masse des emballages).
- Les lettres A/B identifient les contenants ; les natures chimiques respectives, le ratio de mélange technique et les performances ne sont pas validés par cette réponse.
- La valeur `poids_net` reste `null` dans le modèle catalogue pour éviter de représenter deux seaux comme un unique emballage de 13 kg ; la masse est détaillée dans le libellé.
- Les validations industrielles et commerciales demeurent **EN ATTENTE**.
- `presentation_provisoire`, `certifie=false`, `commercialise=false`, `sku_erp_a_creer=false`.

## Modifications

- `src/data/catalogue-projets.json` : conditionnement d'EP-PRIM.
- `docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json` : traçabilité de la confirmation et masses nominales.
- `src/lib/catalogue-projets.ts` : FR/EN/AR de l'emballage, commun aux pages produit, documents et fiches imprimables.
- Tests de non-régression lots 54, 65, 66, 68 + test dédié lot 69.

## À qualifier

Trois références PROOF restent sans quantité confirmée :
`PROOF-EP-SB`, `PROOF-EP-SR`, `PROOF-PU-INJ`.

Aucune création de SKU, aucune publication de FT/FDS validée, aucune mise à jour de Supabase, de l'ERP, de Cloudflare ou du domaine.
