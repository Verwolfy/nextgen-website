# Lot 66 — FENEK-PROOF EP-ANC : 600 mL (type d’emballage à confirmer)

Date : 2026-11-05. Dépôt : `Verwolfy/nextgen-website`.

## Réponse reçue

À la demande de conditionnement du produit **FENEK-PROOF EP-ANC**, l’utilisateur a répondu : **« 600 ML »**.

**Seule la contenance nominale de 600 mL est confirmée.** L’utilisateur n’a pas précisé s’il s’agit d’une cartouche, d’un tube, d’un kit, d’un bidon ou d’un autre conditionnement. Aucun de ces types ne doit être déduit de la fiche générique. Le conditionnement précédent « Kit résine - Contacter nous pour plus d'informations » était une hypothèse éditoriale.

## Réalisations

1. `src/data/catalogue-projets.json` : pour `PROOF-EP-ANC` uniquement :
   `conditionnements=[{"format":"600 mL — emballage à préciser","poids_net":null,"unite":"NON CONFIRMÉ"}]`.
   Statut : `presentation_provisoire`, `certifie=false`, `commercialise=false`.
2. `mode_fr_preparatoire` de EP-ANC : référence à la **cartouche** non confirmée remplacée par des contrôles préalables à l’application, les dimensions et procédures restant soumises aux données techniques FENEK.
3. `docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json` : volume 600 mL confirmé, nature d’emballage, masse, matière d’emballage, nombre de composants et validations commerciales/industrielles non confirmés. Pas de SKU ERP.
4. `src/lib/catalogue-projets.ts` : formats d’affichage :
   - FR : `600 mL — emballage à préciser`
   - EN : `600 mL — packaging type to be confirmed`
   - AR : `600 مل — نوع العبوة قيد التحديد`
5. Tests anciens `tests/test_lot54_proof_packaging_contact.py` et `tests/test_lot65_cm_o2p_packaging.py` ajustés pour l’état actuel.
6. Test dédié `tests/test_lot66_ep_anc_600ml.py` : cohérence des 50 références, validation provisoire de EP-ANC, 5 kits en attente, localisation FR/EN/AR et fiches exportées.

Le site et les PDFs imprimables consomment les conditionnements de la source centrale, via `packagingLabelFor()`. Les 49 autres produits ne sont pas modifiés.

## Progression PROOF — État actualisé

- `PROOF-CM-O2P` : kit provisoire **sac 30 kg + bidon 10 kg** ; composant A/B pas validé (lot 65).
- `PROOF-EP-ANC` : **600 mL**, emballage physique inconnu (lot 66).
- `PROOF-PU-SEAL` : cartouche **300 mL**, confirmé (lot 56).
- `PROOF-ACR-RF`, `PROOF-CM-O1P`, `PROOF-PU-1K` : seaux **5 kg et 20 kg**.
- **5 produits** sans contenance définie : `PROOF-EP-INJ`, `PROOF-EP-PRIM`, `PROOF-EP-SB`, `PROOF-EP-SR`, `PROOF-PU-INJ`.

Le choix « 600 mL » ne constitue pas un feu vert pour la production, la commercialisation, les fiches techniques ou les FDS.

## Reprise automatique conseillée

1. Contrôler la PR du lot 66, fusionner dans `main` si les workflows compilation + sécurité et Chromium FR/AR/EN réussissent.
2. Vérifier les mêmes workflows déclenchés sur `main`.
3. Ne pas modifier Cloudflare, les DNS, le domaine public (choix confirmé au lot 63), les protections `noindex`, Supabase ou l’ERP.
4. **Question suivante prioritaire :** confirmer le **type d’emballage de FENEK-PROOF EP-ANC 600 mL**, puisqu’il est encore inconnu. Les précédents cas PU-SEAL montrent que la contenance et l’emballage doivent être validés séparément.
5. Ensuite, demander le conditionnement de `FENEK-PROOF EP-INJ`, puis les quatre autres références encore sans contenance.
6. Ne pas inventer d’informations de composition chimique, performances, certifications ni ratios à partir de fiches tiers.

Ce document sert de relais complet pour la prochaine discussion.
