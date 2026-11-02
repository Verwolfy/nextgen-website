# Lot 25 — Dix sacs FENEK-BOND réalistes, exacts et révisables

Date : 2 novembre 2026. **Aucune publication Cloudflare ni conformité technique.**

## Résultat du lot dans la conversation

Dix images pleine résolution **1280×1280**, dix variantes cartes **560×560** en WebP, préparées à partir d'un rendu photoréaliste existant d'un sac souple NextGen 25 kg. Les étiquettes ont été composées en texte vectoriel précis pour éviter les fautes des générations d'images qui proposaient des produits absents du référentiel.

| Code | Produit et usage conceptuel |
|---|---|
| BOND-C1T | Mortier-colle cimentaire, carrelage intérieur |
| BOND-C1TE | Mortier-colle, temps ouvert (concept) |
| BOND-C2FT | Mortier-colle, prise rapide (concept) |
| BOND-C2TE | Mortier-colle, pose carrelage |
| BOND-C2TE-S1 | Mortier-colle, concept déformable |
| BOND-CG1 | Mortier de jointoiement, joints de carrelage |
| BOND-CG2WA | Mortier de jointoiement, zones humides (concept) |
| BOND-CT-C25-F5 | Mortier de ragréage, préparation des sols |
| BOND-GP-CSII | Enduit cimentaire, murs |
| BOND-GR-HR | Mortier de calage, platines et ancrages |

**Source de vérité** : dix premières références `bond` de `src/data/catalogue-projets.json`. Les dix proposent tous `Sac 25 kg` dans les conditionnements de travail. Les étiquettes portent `MAQUETTE NON CONTRACTUELLE`, n'affichent aucun dosage, résultat laboratoire, numéro de certification, code réglementaire ou adresse inventée. Le design est simulé, pas une photo de lots fabriqués.

## Archive et contrôles

- Archive fournie à l'utilisateur : `NextGen_FENEK_BOND_10_packshots_lot25.zip`.
- `bond-packshots-manifest.json` embarqué ; 20 noms de fichiers, 20 empreintes SHA256 distinctes ; WebP VP8, dimensions validées.
- Planche visuelle : `nextgen_bond_first10_quality_review.jpg`.
- La qualité imprimable 9/10 **n'est pas démontrée** ; une revue de matériaux, typographie physique et étiquettes en situation est requise avant impression.

## Changements GitHub

- `src/lib/catalogue-projets.ts` : cherche une image spécifique pour BOND Sac 25 kg **et** FLOW Bidon 20 L, uniquement si ses deux variantes de fichiers existent ; fallback générique conservé.
- `scripts/bond-packshots-approved.json` : 20 empreintes attendues, format 25 kg et liste des 10 codes exacts.
- `scripts/install_bond_packshots.py` : valide ZIP, chemins, hash et dimensions **avant toute écriture**.
- `scripts/check_bond_packshots_built.py` : 0 asset = SKIP explicite ; un asset déclenche l'obligation de 20/20 et 60/60 usages dans les cartes et fiches FR/AR/EN.
- Les deux workflows GitHub testent le lot BOND, sans désactiver les tests FLOW.
- `scripts/check_browser_pages.py` contrôle 10 images 560×560 sur mobile (si présentes), et la fiche C1T en 1280×1280 avec `object-fit:contain`.
- `tests/test_lot25_bond_packshots.py` et `scripts/create_bond_packshots_pr.sh`.

## Import effectif restant dans GitHub

Le connecteur GitHub en cours sait modifier des fichiers UTF-8, mais ne dispose pas du contenu binaire du ZIP local : **ne pas annoncer que ces 20 WebP sont déjà dans GitHub**, contrairement aux 24 FLOW intégrés au lot 24.

Après fusion de cette PR code et 2 CI vertes :
1. Ouvrir un GitHub Codespace sur `main` du dépôt privé.
2. Télécharger l'archive depuis la conversation et l'uploader vers `/tmp/NextGen_FENEK_BOND_10_packshots_lot25.zip`.
3. Exécuter : `bash scripts/create_bond_packshots_pr.sh /tmp/NextGen_FENEK_BOND_10_packshots_lot25.zip`.
4. Le script importera, vérifiera, compilera et créera une PR d'assets (20 WebP) ; fusionner après 2/2 CI réussies et inspection visuelle.
5. Cloudflare public et validation technique restent deux jalons distincts non déclenchés.

## Garde-fous

Catalogue de 50 projets : pas de tarifs, formules/dosages, normes/homologation, FDS non approuvée, ni modification Supabase/ERP/SQL/RLS, DNS, Cloudflare ou collecte CRM.
