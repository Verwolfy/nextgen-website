# Lot 192 — agrandissement natif pour la revue des candidats PROOF

Date : **13 novembre 2026**. Projet NextGen Building Solutions, dépôt `Verwolfy/nextgen-website`.

## Résultat
La génération ciblée des scènes suivantes a échoué à plusieurs reprises : l'outil a produit des infographies présentant des dosages, des durées, des logos et emballages fictifs, au lieu de photos isolées de gestes. **Aucun de ces fichiers n'a été importé ni approuvé**. L'avancement réel reste **2/18** scènes proposées, donc **16 scènes manquantes**, à valider individuellement.

Pour améliorer la revue des deux images déjà présentes sur les fiches produits :
- **PROOF-PU-1K étape 5** : `/images/application-premium/fenek-proof-pu-1k-scene-05-candidate-v1.webp`, 960×640, SHA-256 `f8a758381f5a510b03b9bd231700925d5a5b02935d264c2fdc47844915a6c14f`.
- **PROOF-CM-O1P étape 1** : `/images/application-premium/fenek-proof-cm-o1p-scene-01-candidate-v1.webp`, 960×640, SHA-256 `079bde85ae3e331bd2c654d8299ccde2e26a2141dce349b610130c080902a622`.

Le composant `src/components/FenekProofPartialDraft.astro` ajoute maintenant un lien trilingue **« Ouvrir cette illustration en haute résolution »** (EN, FR, AR) vers `candidate.src`, avec `target="_blank"`, `rel="noopener noreferrer"`, `aria-label` spécifique et contour de focus clavier visible. Le lien de comparaison complète du lot 187/190 est conservé.

La page produit contient toujours ses **six illustrations historiques** après le candidat brouillon. Aucune valeur technique inventée, aucun logo ni procédé validé n'est introduit par cette modification.

## Tests et code
- `scripts/check_application_guides.py` exige désormais dans chaque fiche construite l'ancre exacte `href="<chemin du candidat>"` et les attributs de sécurité, en plus du contrôle SHA du WebP et des six étapes officielles.
- `tests/test_lot192_proof_candidate_zoom.py` vérifie les libellés en 3 langues, le lien vers la bonne image, les attributs de sécurité, le focus clavier et les conditions de confidentialité/brouillon.
- Ciblage : uniquement `PROOF-PU-1K` et `PROOF-CM-O1P` ; `PROOF-CM-O2P` reste à **0/6**, sans aperçu.

## Conditions de sortie
1. Fusionner uniquement la petite PR du lot 192 sans incorporer la grande PR #140 de 47 SVG simplifiés.
2. Contrôler le check **Cloudflare Pages success**, puis le marqueur public `https://nextgen-buildingsolutions.com/deployment.json` sur le SHA fusionné.
3. Vérifier les fiches FR/AR/EN des deux produits, la présence du lien de zoom, l'ouverture des WebP en 960×640, le chargement des 6 anciens pictogrammes, et l'absence de fuite vers d'autres produits.
4. Vérifier idéalement le lien et les zones d'activation à largeur mobile 390px et le RTL arabe ; ne pas déclarer ce contrôle réalisé sans preuve.
5. Les images sont **BROUILLON** : la validation FT/FDS des gestes, EPI et matières reste nécessaire avant toute publication comme procédure officielle.
6. Reprendre les 16 scènes manquantes avec une méthode qui permet de produire réellement une scène isolée à la fois et d'éviter les infographies parasites. Ne pas recycler les trois images invalides générées lors de cette passe.

**CI :** les jobs GitHub Actions généraux restent en échec précoce. La réussite du pipeline Cloudflare Pages est un contrôle distinct, non une validation de toutes les tests Python/Astro.
