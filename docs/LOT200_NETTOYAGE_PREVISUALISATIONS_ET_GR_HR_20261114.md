# Lot 200 — Nettoyage non destructif des fiches illustrées NextGen

Date : **14 novembre 2026** — Référence graphique : FENEK-BOND C1T. Base factuelle : audit des 50 guides du 13/11/2026.

## Objectif et état

- **50 produits / 300 étapes** officiels ; 11 séries A, 3 intermédiaires B, 36 pictogrammes C ; 39 séries à harmoniser.
- Cinq groupes de sprites partagent des SHA-256 ; **la suppression automatique est interdite** avant preuve que les références ne sont plus actives.
- Le site public était encore sur `69af52dfdc27fc17c80582acd168ada49efc435c` alors que `main` était sur `c1f7c32c3dba75bfa27621c5fb4286c75a85a5d3` ; galerie d'audit HTTP 404 lors du dernier contrôle. Incident : #154.
- **Aucun visuel généré n'est approuvé FT/FDS. Aucun ancien sprite actif n'a été supprimé, déplacé ou remplacé dans ce lot.**

## Modification de code (branche isolée)

`src/components/FenekApplicationGuide.astro` n'importe ni n'insère plus **FenekAcrRfDraftPreview** ni **FenekProofPartialDraft** dans les **fiches produit officielles**. Ces candidats doivent rester dans les pages de revue isolées `noindex`, distinctes des six gestes officiels. Les assets candidats existants restent dans GitHub, sans suppression.

Conservation stricte : références code+slug exactes, marqueur de statut BROUILLON, fichier source officiel, sprites WebP de repli, six titres et descriptions trilingues, avertissements FT/FDS et lien haute résolution C1T.

Test dédié : `node --test tests/lot200_official_artwork_isolation.test.mjs`.

## Nouvelle planche candidate BOND-GR-HR — non publiée

Une planche de six scènes a été assemblée **localement** à partir des scènes générées en présence de l'utilisateur : WebP 3×2, **1620×720**, SHA-256 `8ad9273c8f79ebd3b41f09a65787a3b2e2853e0043abbfe7f901a084f219809a`, 222 430 octets. Les six images sources WebP 960×640 et le logo utilisateur original sont inclus dans l'archive fournie dans la conversation `NextGen_GR_HR_6_scenes_lot200_v2_brouillon_2026-11-14.zip`.

**Important : ce fichier binaire n'est pas présent dans GitHub.** L'ajouter au manifeste de production serait un lien cassé ; ne pas le référencer dans `src/data/fenek-enhanced-artwork.json` avant upload réel, contrôle SHA, validation FT/FDS et build complet.

| Étape | Geste source | État visuel | Motif |
|---:|---|---|---|
| 1 | Nettoyer et étancher le coffrage | À revoir | Nettoyage visible, étanchéité non démontrée |
| 2 | Humidifier puis évacuer l’eau libre | À revoir | Gestes visibles, vérification technique requise |
| 3 | Porter les EPI et gâcher selon fiche | À revoir | Outillage et procédé à vérifier |
| 4 | Couler en continu d’un seul côté | À revoir | Continuité et méthode produit à vérifier |
| **5** | **Contrôler le remplissage sans ségrégation** | **À revoir** | L'image V2 montre désormais l'observation du remplissage sans lissage ; la non-ségrégation n'est pas vérifiable par cette photo |
| 6 | Protéger les surfaces pendant la cure | À revoir | Protection visible, procédure produit à vérifier |

Autres réserves : marquages générés sur les EPI non certifiés comme logo officiel ; style photographique à comparer à C1T semi-réaliste. **0/6 images validées visuellement, 0/6 techniquement.**

## Ordre de nettoyage et remplacement pour chaque produit

1. Figer les six gestes provenant des notices FR/EN/AR et identifier tous les anciens assets liés à leur slug.
2. Générer/revoir six scènes exactes, appliquer uniquement le vrai logo client hors rendu génératif et contrôler le standard C1T.
3. Vérifier les six gestes par rapport aux FT/FDS propres à la référence.
4. Placer les images dans `public/images/application-premium/` avec SHA-256 et validation par produit, **sans toucher au repli officiel**.
5. Exécuter tests des identités, WebP, dimension, pages en 3 langues, et contrôle navigateur mobile/desktop.
6. Basculer une seule référence officielle après validation et publication contrôlée. Confirmer le SHA public du déploiement.
7. **Seulement ensuite** recenser les fichiers sans aucune référence (code, build, CSS, prévisualisations, versions et repli), proposer leur suppression dans une PR distincte. Aucune suppression irréversible sans autorisation.

## Blocages

- Incident Cloudflare #154 non résolu.
- CI GitHub Actions échoue sans lancement de job (aucun test complet GitHub prouvé).
- GR-HR : la scène 5 a été remplacée dans le brouillon V2. Le contrôle de la non-ségrégation et les autres gestes exigent encore FT/FDS approuvées.

## Reprise

1. Exécuter le test ciblé du lot 200 dans Node 22 ; confirmer sur GitHub Actions.
2. Confirmer la pertinence technique de la scène 5, harmoniser les marquages/logo sur les six scènes ; double validation.
3. Résoudre le déploiement pour voir réellement les nettoyages des aperçus officiels.
4. Refaire le même lot pour BOND-GP-CSII et les 37 autres références à harmoniser.
5. Mettre à jour un journal daté et les SHA de chaque lot ; **ne jamais déclarer les 39 séries corrigées avant preuve**.

**Mise à jour du 14/11/2026** : la scène 5 V2 est désormais une inspection visuelle, pas un talochage. L'archive V2 et son manifeste SHA résident dans la conversation, **pas dans GitHub**. Les approbations restent toutes à `false`.
