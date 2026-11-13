# Lot 191 — candidats PROOF visibles dans les fiches produits (13 novembre 2026)

**But :** poursuivre les modes d'emploi graphiques de qualité C1T, avec une livraison visible sur le site, sans transformer une proposition générée en procédure technique approuvée.

## Résultat de la continuation
La génération d'une nouvelle scène de malaxage PU-1K a produit un tableau infographique comprenant des durées/vitesses et des faux marquages non approuvés. **Sortie rejetée, non transmise dans GitHub et non publiée.** Le nombre de scènes premium exploitables reste **2/18** pour ce sous-lot.

Pour rendre les deux scènes existantes plus faciles à examiner, nous avons ajouté un aperçu graphique directement dans deux fiches : 
- **PROOF-PU-1K**, scène candidate **5/6** : application uniforme de la membrane au rouleau.
- **PROOF-CM-O1P**, scène candidate **1/6** : nettoyage/humidification du support, sans eau stagnante à vérifier techniquement.
- **PROOF-CM-O2P**, **0/6** : aucune image candidate ajoutée.

La nouvelle section apparaît **avant les 6 pictogrammes publiés**, qui restent intacts, en FR, EN et AR. Elle est marquée `BROUILLON` et indique clairement que les FT/FDS approuvées sont nécessaires. Un lien renvoie à la comparaison avant/après du lot 190.

## Fichiers modifiés
1. `src/components/FenekProofPartialDraft.astro` (nouveau) : une image unique par référence précise, responsive, traduction FR/EN/AR, avertissement de non-approbation.
2. `src/components/FenekApplicationGuide.astro` : intégration strictement conditionnée au code **ET** au slug des deux produits ; aucun changement d'image dans les six étapes officielles ni impact sur les autres 48 références.
3. `scripts/check_application_guides.py` : contrôle post-build de 150 fiches, contrôle de l'unique image candidate sur chacune des deux références en trois langues, SHA-256 du média, absence d'image premium sur les autres produits.
4. `tests/test_lot191_proof_partial_previews.py` (nouveau) : tests des deux WebP, des codes, du caractère Brouillon, des localisations et du maintien des six étapes.

Les deux fichiers WebP étaient **déjà dans main** grâce à PR #144 : 
- `public/images/application-premium/fenek-proof-pu-1k-scene-05-candidate-v1.webp` SHA-256 `f8a758381f5a510b03b9bd231700925d5a5b02935d264c2fdc47844915a6c14f`.
- `public/images/application-premium/fenek-proof-cm-o1p-scene-01-candidate-v1.webp` SHA-256 `079bde85ae3e331bd2c654d8299ccde2e26a2141dce349b610130c080902a622`.

## Limites et validation
- Les images sont de qualité semi-réaliste et déjà comparées visuellement au standard C1T, mais la justesse des gestes, de l'eau libre et des EPI reste à valider contre des FT/FDS réelles.
- **Ne pas prétendre que 18 scènes ont été produites** ; il reste 16 scènes.
- Les SVG schématiques de la PR #140 ne sont pas substitués aux médias existants.
- La CI GitHub Actions classique demeure en échec avant exécution ; seule une vérification du résultat Cloudflare Pages, du SHA public `deployment.json`, de la présence des images dans les fiches et une inspection navigateur réelle permettront de confirmer le déploiement.
- Aucun changement aux FT/FDS, logos officiels, normes, performances, dosages, durée, formulaire, données produit ni autres notices.

## Vérifications attendues après fusion
1. `https://nextgen-buildingsolutions.com/deployment.json` retourne le commit exact du nouveau merge.
2. Les pages `/fr/documentation/fenek-proof-pu-1k/`, `/en/documentation/fenek-proof-pu-1k/`, `/ar/documentation/fenek-proof-pu-1k/` affichent **une** scène V4 candidate 5/6 avant les six anciennes images.
3. Les trois langues des pages CM-O1P affichent **une** scène candidate 1/6 avant les six anciennes images.
4. Les pages CM-O2P et tous les autres produits n'affichent aucun aperçu partial.
5. Aucun échec HTTP image, perte de numérotation, débordement mobile/desktop, ni statut de validation technique trompeur.
6. Les images V4 restent expérimentales et ne remplacent aucune image de notice officielle.

## Prochain lot
Reprendre les 16 scènes restantes, une à une, sans recycler les photos de membrane pour des étapes distinctes. Priorité au malaxage **PU-1K sans eau**, à la préparation cimentaire monocomposant puis au mélange réellement distinct des deux composants CM-O2P. Conserver le statut `BROUILLON` tant que FT/FDS et contrôle technique ne sont pas disponibles.
