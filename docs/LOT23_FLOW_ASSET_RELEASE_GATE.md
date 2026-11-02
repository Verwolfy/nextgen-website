# Lot 23 — Passage des 12 WebP FENEK-FLOW de l’archive à GitHub

Date : 2 novembre 2026. **Statut : barrière d’intégration prête ; octets binaires non encore transférés dans GitHub.**

## Résultat du contrôle local

Archive de la conversation `NextGen_FENEK_FLOW_12_packshots_lot21.zip`, 1 826 488 octets de contenu décompressé. Douze références, 12 grands WebP 1120×1120 et 12 vignettes 560×560. **24/24 empreintes SHA256 de l’archive vérifiées** ; aucune répétition d’empreinte. Les photos montrent des maquettes de bidons 20 L en proportions naturelles ; **les données techniques visibles sur les étiquettes ne sont pas certifiées**. Le visuel `WR-N` a été inspecté en taille 1120×1120, comporte correctement « WR-N » ; l’ancienne hypothèse « SP-HR » était une lecture erronée d’une miniature.

## Modifications de qualité intégrées au dépôt

- `scripts/check_flow_packshots_built.py` : sans images FLOW, imprime explicitement `SKIP` et exige l’absence de copies périmées dans `dist` ; à partir du premier WebP FLOW, exige immédiatement les 24 fichiers, les 24 SHA256, les dimensions attendues, leur copie intacte vers `dist` et leur utilisation dans les 12 cartes + 12 détails pour chacune des 3 langues (72 usages).
- Les deux CI Astro/sécurité et Chromium exécutent le contrôle après compilation. Une PR ne modifiant *que les images binaires* déclenche désormais aussi Chromium (nouvel élément `public/images/catalogue-projects/**` dans les chemins surveillés).
- `scripts/check_browser_pages.py` : une fois les fichiers présents, inspecte les 12 vignettes FLOW sur mobile, leurs dimensions de décodage 560×560 et `object-fit:contain` ; vérifie le détail WR-N en 1120×1120 et prend des captures FR/AR/EN. Aucun faux succès quand le fichier manque.
- `tests/test_lot23_flow_release_gate.py` : assure la présence du garde-fou GitHub Actions et des vérifications locales.
- `scripts/create_flow_packshots_pr.sh` : à lancer depuis un **Codespace GitHub authentifié** après avoir déposé le ZIP dans `/tmp/` ; un seul appel vérifie les images, exécute les tests et la compilation, crée une branche assets, pousse 24 fichiers et ouvre automatiquement une PR GitHub. Ne publie rien sur Cloudflare.

## Pourquoi pas déjà sur GitHub ?

La session de travail accède au ZIP **dans le conteneur local** et au dépôt **via un connecteur GitHub qui n’accepte que le texte ou une chaîne base64**. Le conteneur ne peut pas résoudre le nom `github.com`, et le connecteur ne peut pas lire directement les octets binaires du conteneur. Les actions connectées ne peuvent donc pas réaliser ici le transfert direct des 24 WebP sans mécanisme d’échange externe non autorisé. Éviter de proclamer une intégration d’image réussie alors que le répertoire `public/images/catalogue-projects/` n’existe pas encore sur le `main` distant.

## Import via GitHub Codespaces

1. Ouvrir le dépôt privé `Verwolfy/nextgen-website` → **Code → Codespaces** ; démarrer un Codespace sur `main`.
2. Télécharger l’archive depuis la conversation, la déposer par glisser-déposer dans le terminal/explorateur du Codespace sous `/tmp/NextGen_FENEK_FLOW_12_packshots_lot21.zip` (ou un autre chemin absolu).
3. Exécuter :

```bash
bash scripts/create_flow_packshots_pr.sh /tmp/NextGen_FENEK_FLOW_12_packshots_lot21.zip
```

4. La PR est créée ; les deux workflows doivent être verts, et les captures mobiles contrôlées avant fusion.
5. Après fusion, vérifier `main` et le domaine **uniquement si le déploiement Cloudflare est explicitement autorisé et protégé**, sans changer les indicateurs techniques d’homologation.

## Critères d'acceptation

- 12 codes FLOW distincts, **24 fichiers** committés, aucune image manquante ou corrompue.
- `python scripts/install_flow_packshots.py --verify` puis `python scripts/check_flow_packshots_built.py` après compilation : PASS.
- Navigateur : 12/12 vignettes visibles, WR-N correct, ratio non étiré sur mobile, pages FR/AR/EN.
- Zéro produit certifié publié dans `public/data/products.json` ; aucune modification Supabase/ERP, prix, FT/FDS, formulaires, DNS, secrets, Cloudflare Access ou Pages.

## Suite

Après cette PR de contrôle qualité, importer les 24 WebP avec le script de Codespaces, fusionner la PR des assets seulement si 2/2 CI vertes, puis examiner les captures sans attribuer un score arbitraire « 9/10 ».
