# Lot 190 — deux scènes semi-réalistes de revue, suite du lot 187

13 novembre 2026 — **BROUILLON GRAPHIQUE / NON APPROUVÉ FT-FDS**.

## Contexte et but
L'audit des 50 produits montrait 11 médias de qualité A proche de FENEK-BOND C1T, 3 de niveau B et 36 pictogrammes de niveau C. Le pilote ACR-RF du lot 189 a été publié dans la fiche produit comme une prévisualisation de six nouvelles scènes, sans supprimer l'ancienne notice. Le lot 187 prévoit 18 nouvelles scènes sur trois autres PROOF.

Lors de cette continuation, la génération d'une nouvelle scène de malaxage a produit une fausse capture produit contenant des durées/vitesses non approuvées. Elle a été rejetée et **jamais importée**. Plusieurs scènes d'application au rouleau très semblables n'ont pas été réutilisées pour compléter artificiellement les six étapes.

## Candidats produits réellement et uniquement réalisés
| Produit | Étape | Média de revue | SHA-256 | SHA Git (blob) |
|---|---|---|---|---|
| PROOF-PU-1K | 5 : Appliquer uniformément la membrane | `public/images/application-premium/fenek-proof-pu-1k-scene-05-candidate-v1.webp` | `f8a758381f5a510b03b9bd231700925d5a5b02935d264c2fdc47844915a6c14f` | `a359218737731377067ca669d8042f97a7a826d4` |
| PROOF-CM-O1P | 1 : Nettoyer et humidifier sans eau stagnante | `public/images/application-premium/fenek-proof-cm-o1p-scene-01-candidate-v1.webp` | `079bde85ae3e331bd2c654d8299ccde2e26a2141dce349b610130c080902a622` | `5451d13321c05d5352bbf60cef0a9241046aaf0e` |

Les deux images 960×640 sont des propositions générées, cadrées en 3:2 et marquées d'un badge numéroté avec bordure navy/vert. Les visuels ont été relus en local, puis transférés comme blobs binaires GitHub. Les SHA de blob ont été comparés avec les calculs Git locaux.

**Attention aux FT/FDS :** le support montré pour CM-O1P a une apparence humide ; la présence d'eau libre est à vérifier, ainsi que la pertinence de l'outil. L'application au rouleau PU-1K et les EPI doivent également être confirmés par les fiches validées. Aucune conclusion de compatibilité ou conformité produit n'est exprimée.

## Page de revue du lot
`public/fr/avant-premiere/lot187-proof/index.html`, route prévue :
`https://nextgen-buildingsolutions.com/fr/avant-premiere/lot187-proof/`.

- Deux comparaisons avant/après, limitées chacune à une seule étape exacte.
- PROOF-CM-O2P : 0/6 nouvelle scène, explicitement déclaré.
- Visuel actuel affiché à côté du candidat via le sprite WebP original, jamais remplacé.
- Mentions `Brouillon graphique`, `non approuvé`, `noindex,nofollow,noarchive`, aucun script ou formulaire.
- La publication ne modifie aucun mode d'emploi officiel, aucune page produit, aucune API/identité/logo.

## État d'avancement
- **2 scènes candidats sur 18** du lot 187.
- PROOF-PU-1K : 1/6, PROOF-CM-O1P : 1/6, PROOF-CM-O2P : 0/6.
- **16 scènes restantes** à générer et à revoir individuellement. Des sorties répétées ou comportant des valeurs techniques non sourcées sont à rejeter.
- Après fusion, vérifier le check Cloudflare Pages, `/deployment.json`, l'accès réel aux deux WebP et la mise en page dans un navigateur desktop/mobile. Ne pas prétendre cela réussi tant que les observations ne sont pas enregistrées.
- La grande PR #140 demeure brouillon/non fusionnée, et la CI GitHub Actions générale peut toujours échouer avant exécution. Ne pas forcer la fusion de cette PR.

## Suite recommandée
Priorité : créer pour PU-1K les cinq scènes restantes (support sec, EPI/ventilation, homogénéisation SANS eau, primaire conditionnel, points singuliers) ; pour CM-O1P les cinq restantes (EPI, gâchage selon FT, armature, couches croisées, cure avant pose) ; puis les six scènes CM-O2P (mélange A+B explicite). Ne pas utiliser de fausses photos de marque, ni timings/dosages inventés.
