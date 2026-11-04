# Lot 51 — Conditionnement unique FENEK-BOND : sac 25 kg

Date : 2026-11-04
Source : confirmation explicite de l'utilisateur : « Pour tous les produit en sac le conditionnement c'est 25 kg (gamme Fenek-Bond) ».

## Décision enregistrée

Les **16 produits de la gamme FENEK-BOND** sont présentés en **sac de 25 kg seulement**. Les anciennes propositions de **5 et 10 kg** sont retirées du catalogue et donc des pages et exports alimentés par ce catalogue.

Le format de vente est confirmé par l'utilisateur. **Ce n'est pas une confirmation d'une fabrication, disponibilité commerciale, certification, homologation d'étiquette ou conformité HSE**.

## Code et référentiel modifiés

- `src/data/catalogue-projets.json` : `conditionnements` réduit à une entrée `{"format":"Sac 25 kg","poids_net":25,"unite":"SAC"}` pour chaque référence de gamme `bond`.
- `docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json` : emballage sac 25 kg, source et date de confirmation ; `validation_commerciale_emballage` et `validation_production_emballage` demeurent `EN ATTENTE`, `sku_erp_a_creer=false`.
- `tests/test_lot51_bond_25kg_conditionnement.py` : contrôle strict des 16 formats et des garde-fous.
- Les **34 autres références** conservent leurs hypothèses d'emballage sans modification.
- Aucune donnée Supabase, ERP, certification, FDS ni état de commercialisation n'a été changée.

## Validation trilingue

Les pages `/fr/documentation/…`, `/en/documentation/…`, `/ar/documentation/…` et leurs exports A4 utilisent les `conditionnements` de la source centrale. Les fiches commerciales affichent donc « Sac 25 kg » pour FENEK-BOND. Les mentions « visuel indicatif » restent valables pour la maquette, les matières d'emballage et l'étiquetage.

## Suite

1. Vérifier les CI sur PR et sur `main`, puis fusionner si vertes.
2. Recueillir le conditionnement **FENEK-FLOW AC** (produit suivant dans l'ordre des 50). Actuellement proposés mais **non confirmés** : bidon 5 L, bidon 20 L, fût 200 L et IBC 1 000 L.
3. Continuer produit par produit ; seuls les emballages explicitement confirmés peuvent remplacer les propositions éditoriales.

Cette note sert de référence pour reprendre le projet dans une autre discussion.
