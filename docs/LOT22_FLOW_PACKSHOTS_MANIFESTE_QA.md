# Lot 22 — Contrôle de correspondance et manifeste FENEK-FLOW (12 références)

Date : 2 novembre 2026. **Lot de contrôle qualité, sans transfert des octets WebP ni déploiement Cloudflare.**

## État vérifié
- Source : archive de la conversation `NextGen_FENEK_FLOW_12_packshots_lot21.zip`, 1,8 Mo.
- Contenu réel : 12 visuels complets WebP 1120×1120, 12 vignettes WebP 560×560 et un manifeste avec empreintes SHA256 et 12 slugs distincts ; tous les en-têtes RIFF/WEBP et dimensions ont été contrôlés.
- `FENEK-FLOW WR-N` : une lecture trop rapide de la planche réduite avait suggéré à tort une étiquette « SP-HR ». **Inspection de la source et de son WebP en grand format : les deux portent correctement « WR-N » et « Plastifiant réducteur d’eau ».** Ne pas rejeter cette image par erreur.
- Les 12 images restent des **simulations de bidons 20 L** issues d'images générées. Le visuel peut mentionner des propriétés techniques non validées : **aucune homologation ni conformité de produit ne peut être déduite de l'étiquette**.

## Changements GitHub
1. `scripts/flow-packshots-approved.json` : 24 empreintes SHA256 immuables des sources examinées ; dimensions exigées. Ce manifeste est le point de contrôle indépendant du ZIP.
2. `scripts/install_flow_packshots.py` : vérifie les 12 slugs et 24 chemins, l'égalité SHA256 à la liste approuvée, les dimensions, signatures WebP et tailles avant d'écrire un seul fichier. `--verify` permet de contrôler les fichiers déjà copiés.
3. `src/lib/catalogue-projets.ts` : affiche un packshot spécifique **uniquement si les deux tailles du produit existent**, sinon image générique ; aucun lien d'image cassé après un import partiel.
4. `tests/test_lot21_flow_packshots.py` et `tests/test_lot22_approved_flow_images.py` : contrôles de structure, référentiels, conditionnements ERP, intégrité et absence de publication technique. Si les assets binaires sont absents du dépôt, le test d'intégrité des fichiers est explicitement marqué *skipped* au lieu de prétendre les avoir vérifiés dans GitHub.

## Transfert restant
Le connecteur GitHub de cette conversation sait créer des fichiers UTF-8 et des blobs à partir de chaînes, **pas consommer directement le ZIP binaire qui réside dans le conteneur local**. L'environnement Git local ne résout pas `github.com` et ne possède pas de jeton GitHub. En conséquence, les **24 fichiers WebP ne sont pas poussés**, et les pages du site continuent d'afficher le fallback 3D existant.

Pour importer depuis une machine authentifiée disposant de l'archive :
```bash
git clone git@github.com:Verwolfy/nextgen-website.git
cd nextgen-website
git checkout -b assets/flow-12-packshots
python scripts/install_flow_packshots.py /chemin/NextGen_FENEK_FLOW_12_packshots_lot21.zip
python scripts/install_flow_packshots.py --verify
python -m unittest discover -s tests -v
npm ci && npm run build
git add public/images/catalogue-projects/
git commit -m "assets(site): 12 packshots FENEK-FLOW contrôlés"
git push -u origin assets/flow-12-packshots
```
Ouvrir une PR, attendre deux CI vertes, fusionner puis seulement après protection Access et autorisations de publication envisager un déploiement Cloudflare.

## Invariants
- Les 50 fiches du catalogue gardent le statut **présentation provisoire**.
- `public/data/products.json=[]` ; pas de tarifs, normes, dosages ou certificats ajoutés.
- Aucun changement ERP/Supabase, secrets, Cloudflare, DNS, formulaires ou politique d'accès.
- La qualité 9/10 et l'affichage sur un site déployé restent à évaluer après intégration des vrais fichiers.
