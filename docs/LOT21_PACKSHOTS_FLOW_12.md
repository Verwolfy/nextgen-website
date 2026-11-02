# Lot 21 — Préparation de l'intégration de 12 maquettes réalistes FENEK-FLOW

Date 2026-11-02. **Pas de déploiement Cloudflare ni de validation technique.**

## Provenance et correction

- Douze visuels indépendants FENEK-FLOW (WR-N, SP-HR, SP-RT, SP-PF, RT, AC, AE, WP, VMA, CI, CURE, LAT) sont disponibles dans un ZIP local `NextGen_FENEK_FLOW_12_packshots_lot21.zip` créé depuis les images de la conversation.
- **Correction QA importante :** une ancienne association utilisait le même rendu `SP-HR` pour `WR-N`. Le visuel source `WR-N` a été récupéré dans `ghostwriter_images/generated/a_crisp_photorealistic_studio_product_shot_on_a_s_2_batch_2.png`, reconnaissable au badge `WR-N`; l'archive comporte désormais **12 SHA256 distincts**.
- Les formats `Bidon 20 L` existent pour **12/12 références** dans `src/data/catalogue-projets.json`. Cela ne garantit pas la disponibilité commerciale ni la précision de l'étiquette.
- Chaque image a été convertie sans déformation en WebP 1120×1120 + vignette 560×560, bandeau visible « CONCEPT VISUEL — NON CONTRACTUEL ». Les caractéristiques photoréalistes des images générées doivent être comprises comme simulées, pas certifiées.

## Modifications GitHub

- `src/lib/catalogue-projets.ts` contient `conceptPackshot()` : utilise une image dédiée uniquement si le fichier exact existe dans `public/images/catalogue-projects/`, uniquement pour les références FLOW avec format `Bidon 20 L`. Sinon conserve la maquette générique. **Les WebP ne sont pas encore présents sur la branche distante à ce stade.**
- Grille Catalogue et détail utilisent respectivement les variantes `-card.webp` et `.webp` ; styles `object-fit: contain` et ratio 1:1 pour empêcher les bidons écrasés ou recadrés.
- Mention dédiée FR/AR/EN lorsque le visuel spécifique est présent, indiquant la nécessité de revoir étiquettes, caractéristiques et conditionnements avant impression/vente.
- `scripts/install_flow_packshots.py` vérifie la composition du ZIP (12 slugs, 24 images WebP, SHA256, chemins stricts) **avant toute installation** dans la copie locale du repo.
- `tests/test_lot21_flow_packshots.py` vérifie présence du fallback et des avertissements et absence d'altération du catalogue officiel.

## Pour finaliser l'intégration effective

1. Télécharger le ZIP depuis la conversation et cloner la branche GitHub ou main une fois PR fusionnée.
2. `python scripts/install_flow_packshots.py /chemin/NextGen_FENEK_FLOW_12_packshots_lot21.zip`.
3. `git add public/images/catalogue-projects && git commit -m "assets(site): 12 packshots FENEK-FLOW" && git push` sur une **nouvelle branche de PR**.
4. Vérifier les 2 pipelines GitHub Astro/sécurité et Chromium, puis examiner manuellement les captures FR/AR/EN à 390/320 px. Les images utilisées par les pages ne changent qu'après présence réelle des fichiers à la compilation.

L'outil GitHub connecté ici peut modifier des fichiers texte mais ne reçoit pas directement les octets WebP créés dans le conteneur. C'est pourquoi les assets binaires ne sont pas déclarés à tort « publiés ». Le ZIP fourni est prêt, mais leur envoi vers GitHub reste à effectuer.

## Limites

- Noindex, formulaires et leads inactifs ; pas de modification Supabase, ERP, SQL/RLS, secrets, DNS ou Cloudflare.
- `public/data/products.json` reste `[]`; 50 références sont présentées uniquement comme projets éditoriaux.
- Ne pas utiliser d'étiquettes imprimées ou de mentions normatives générées par IA sans contrôle juridique et technique. Aucun score graphique « 9/10 » objectivement démontré.
