# NextGen — Lot 126 — Remplacement définitif de la maquette CM-O2P et contrôle Supabase

Date : 11 novembre 2026. Référence : `FENEK-PROOF CM-O2P` / `PROOF-CM-O2P`.

## Demande utilisateur
Sur la page de catalogue, remplacer la maquette qui affiche encore **KIT 30 KG** et l'ancien badge « sac 30 kg + bidon 10 kg ». Vérifier toutes les mentions des masses dans le site et la BDD Supabase. Le sac doit contenir **20 kg**, le bidon **10 kg** et le kit complet **30 kg**.

## Diagnostic et origine du décalage
- La PR #126 du lot 125 avait déjà mis à jour les libellés et intégré une maquette SVG corrigée avec une superposition de texte, mais une capture du site montrait encore une ancienne version.
- Le site Astro utilise le catalogue statique `src/data/catalogue-projets.json`, et non une requête Supabase à chaque affichage.
- Le besoin est donc de fournir une nouvelle image avec une adresse différente (anti-cache), de vérifier toutes les pages et de synchroniser **uniquement** les métadonnées de présentation en base.
- Le nouveau média est dérivé de la maquette corrigée du client puis harmonisé pour afficher sans ambiguïté **SAC 20 KG** sur le sac et **10 KG** sur le bidon. Aucune autre masse n'a été changée.
- Le product packshot n'est pas une étiquette réglementaire certifiée.

## GitHub — réalisé sur branche
Branche : `fix/lot126-cm-o2p-maquette-20kg-supabase-20261111`

- `public/images/maquettes/fenek-proof-cm-o2p-sac-20kg-v2.webp` : image optimisée 640×640, 40 494 octets, SHA-256 `552f3f850fca117410d0268265f5f7db8c4506dcbc93620ba07529657ea291b7`.
- `src/lib/catalogue-projets.ts` : seul le code `PROOF-CM-O2P` pointe vers cette nouvelle image, sur catalogue, fiche produit et A4 imprimable. L'ancien `maquette-37.webp` et la surimpression SVG historique restent archivés.
- `src/pages/[lang]/catalogue/[slug].astro` : texte alternatif explicite FR, AR, EN.
- `src/data/catalogue-projets.json` : contient déjà `Kit : sac 20 kg + bidon 10 kg` depuis la PR #126. Les traductions affichent le total 30 kg sans le confondre avec le sac.
- `docs/catalogue-interne/audit_visuels_proof_11_20261105.json` : traçabilité du visuel actif et des versions archivées.
- `tests/test_lot125_cm_o2p_20kg.py`, `tests/test_lots76_78_audit_deploiement_visuels.py`, `scripts/check_built_pages.py`, `scripts/check_browser_pages.py` : conformité de la maquette, des trois langues, de la fiche et de l'index, sans retour à l'ancien 30 kg.
- `scripts/check_live_production.py` : contrôle post-déploiement Cloudflare de la maquette SHA-256 et des libellés sur catalogue et fiche FR/AR/EN.

## Supabase production — réalisé / vérifié
Projet `erp-mortier` (ID `wenydirqtmkywbxbxfal`).
- Ligne `public.site_produits` : `pf_id='PROOF-CM-O2P'` ; `contenu.conditionnements_provisoires` synchronisé avec `sac_kg=20`, `bidon_kg=10`, `masse_totale_kg=30` ; `image_url='/images/maquettes/fenek-proof-cm-o2p-sac-20kg-v2.webp'`.
- État de contrôle : `publie=false`, `produit_reel_confirme=false`, `fiche_technique_validee=false`.
- Aucun texte obsolète « sac 30 kg » dans les données JSON de cette ligne.
- `public.site_products` est une vue filtrée et ne retourne aucune ligne CM-O2P non publiée (normal).
- `public.site_demandes` : aucune demande historique avec l'ancien conditionnement CM-O2P.
- `public.sku_conditionnement` : **SKU ERP `NG-SKU-PROOF-CM-O2P-KIT-NQ` toujours actif** avec le libellé `Kit résine - composition et contenance non définies`, `poids_net=NULL`. Ce n'est pas une valeur erronée 30 kg, mais un SKU non qualifié. **Ne pas modifier cet enregistrement commercial actif ni attribuer un poids ERP sans qualification et validation industrielle/commerciale**.

## Validation technique
- Tests unitaires, build Astro, Pagefind, fichier WebP et impression FR/AR/EN doivent réussir.
- Après fusion GitHub, attendre le résultat de `NextGen - Cloudflare live production smoke (read-only)`, qui exige le bon SHA avant de vérifier les pages publiées.
- Ne pas déclarer le déploiement Cloudflare réussi sans preuve.
- Les 49 autres références et les politiques RLS/ERP ne changent pas.

## Reprise
1. Vérifier les CI GitHub de la PR.
2. Corriger si nécessaire ; fusionner sur `main` après tests réussis.
3. Contrôler le premier run Cloudflare post-fusion et les pages `/fr/catalogue/fenek-proof-cm-o2p/`, `/ar/catalogue/fenek-proof-cm-o2p/`, `/en/catalogue/fenek-proof-cm-o2p/`.
4. Faire valider séparément le packaging industriel avant toute publication d'une vraie FT/FDS ou activation du SKU ERP.
