# Lot 56 — FENEK-PROOF PU-SEAL : cartouche 300 mL

Date : 2026-11-04. Dépôt : Verwolfy/nextgen-website.

## Décision utilisateur
La contenance de 300 mL avait été confirmée au lot 55. L'utilisateur vient de confirmer explicitement que le contenant physique est une **cartouche**.

## Application
- Produit concerné exclusivement : PROOF-PU-SEAL (FENEK-PROOF PU-SEAL).
- Fiche centrale : `src/data/catalogue-projets.json`, conditionnement `Cartouche 300 mL`, `poids_net=null`, `unite=CARTOUCHE`.
- Registre interne : `docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json`, unité de vente CARTOUCHE et format 300 mL, avec trace de la décision utilisateur.
- Localisation : `src/lib/catalogue-projets.ts`, FR `Cartouche 300 mL`, EN `300 mL cartridge`, AR `خرطوشة 300 مل`. Les fiches catalogue, les fiches documentation et les exports A4 utilisent le helper central `packagingLabelFor`.
- Tests : `tests/test_lot54_proof_packaging_contact.py` et `tests/test_lot55_pu_seal_300ml.py` actualisés.

## Précautions
La décision confirme l'emballage et son volume uniquement. Le poids, la densité, la matière de cartouche, les étiquettes, les certifications et les paramètres FDS restent non validés. Les produits sont toujours en statut `presentation_provisoire`, `certifie=false`, `commercialise=false`, `sku_erp_a_creer=false`. Aucune écriture Supabase ou ERP ni déploiement public n'est requis pour ce lot.

## État général des 50 références
- 16 FENEK-BOND : sacs 25 kg.
- 12 FENEK-FLOW : bidons 5/20 L, fûts 200 L, IBC 1 000 L.
- 11 FENEK-PAINT : seaux 5/10/20 kg.
- FENEK-PROOF : 3 références en seaux 5/20 kg, 7 en kits à composition et contenance à clarifier (message « Contacter nous pour plus d'informations »), PU-SEAL en cartouche 300 mL.

Les 50 références disposent de formats ou d'une invitation de contact, mais les sept kits ne sont pas confirmés en masse/volume. Ne pas considérer les FT/FDS comme réglementairement validées.

## Reprise
1. Vérifier et fusionner la PR du lot 56 si les workflows CI « Astro build + security checks » et « protected browser recipe » passent.
2. Vérifier les deux workflows post-fusion, puis tester le domaine hébergé lorsqu'un déploiement effectif est autorisé.
3. Pour les sept kits PROOF, recueillir les volumes, compositions A/B et emballages matériels réels, si disponibles.
4. Émission de FT/FDS officielles seulement après validation des formulations et des données techniques/HSE propres à NEXTGEN.
