# Lots 195–198 — plan de réalisation source par source de 234 scènes C1T

Date : 13 novembre 2026 — état **BROUILLON, NON GÉNÉRÉ / NON APPROUVÉ**.

## Portée de l'harmonisation graphique

Sur les 50 produits FENEK publiés, 11 illustrations de la gamme BOND atteignent déjà un rendu semi-réaliste comparable à FENEK-BOND C1T. **39 références** doivent encore être harmonisées : cinq BOND, onze PROOF, douze FLOW, huit peintures PAINT en pictogrammes et trois façades PAINT intermédiaires.

| Lot | Gamme | Références | Scènes à harmoniser | Scènes candidates non approuvées | Scènes encore inexistantes |
|---:|---|---:|---:|---:|---:|
| 195 | BOND | 5 | 30 | 0 | 30 |
| 196 | PROOF | 11 | 66 | 8 | 58 |
| 197 | FLOW | 12 | 72 | 0 | 72 |
| 198 | PAINT | 11 | 66 | 0 | 66 |
| **Total** | | **39** | **234** | **8** | **226** |

Pour **PROOF-PU-1K + PROOF-CM-O1P + PROOF-CM-O2P**, le sous-lot spécifique reste à **2/18 candidats** ; les six autres candidats disponibles sont ceux du pilote ACR-RF, toujours BROUILLON et non validés par FT/FDS.

## Livrables source en GitHub

- `docs/LOT195_198_39_PRODUITS_234_SCENES_STORYBOARDS_20261113.json` : **39 produits × 6 scènes**, chaque entrée comprenant **titre et description officiels du projet en FR/EN/AR**, geste attendu, contraintes visuelles, cadrage 3:2, absence de chiffres/logos/performance, média de repli et empreinte, statut génération/validation, liste de contrôle.
- `tests/test_lot195_198_all39_source_shotlists.py` : vérifie l'identité produit, la correspondance aux notices, les 234 scènes et les huit candidats non approuvés.
- Aucun fichier binaire nouveau n'est inventé ou réputé généré par ces documents. Les huit candidats restent à examiner et ne doivent pas être mis en mode d'emploi officiel.

## Méthode de production imposée

1. **Une seule image indépendante par scène**, paysage **3:2**, résolution source cible 960×640 minimum, sans texte/numéro/caption/logo ni photographie de marque ou de seau inventée. Cadrage photographique semi-réaliste au niveau de FENEK-BOND C1T.
2. Représenter **exactement le geste de la notice source**, sans transformer un produit cimentaire, PU, peinture ou adjuvant en geste générique d'un autre métier.
3. **Rejeter entièrement** les infographies multi-produits, tableaux, tableaux de bord et images contenant de faux « site vérifié », dosages, durées, normes ou marques. Plusieurs générations précédentes échouaient sur ces critères.
4. Après réception d'une image acceptable : revue graphique (mains, EPI, matériaux, outils, perspective, singularité du geste), puis vérification technique avec **FT/FDS approuvées** avant tout passage en `visualApproved:true` et `technicalApproved:true`.
5. Assembler **six véritables images** dans une planche WebP **3×2 de 1620×720**, calculer SHA-256, transférer binaire Git et relire le SHA côté dépôt. Conserver l'ancienne planche comme repli.
6. Publier une avant-première isolée `noindex` / `BROUILLON`, comparer à C1T sur le site, inspecter mobile 390px / desktop et FR/EN/AR, puis activer seulement avec les deux accords séparés et la recette CI Cloudflare.
7. Traiter en priorité les groupes dont plusieurs références partagent un même WebP : R3/R4 BOND, WR-N/SP-HR FLOW, SP-RT/SP-PF/RT/AC FLOW, INT-M/INT-S/INT-WA PAINT, PRIM-A/PRIM-FX PAINT.

## Blocage indépendant : publication de la galerie des 50 produits

L'audit des **150/150 pages FR/EN/AR** est terminé : 148 pages avec six titres correspondant exactement aux notices, exceptions de rédaction EN C1T/C1TE. Les 50 médias WebP de `main` ont des SHA inchangés depuis l'évaluation visuelle précédente (11 A, 3 B, 36 C).

Une galerie globale de revue visuelle a été fusionnée : `public/fr/avant-premiere/audit-50-illustrations/index.html` (PR #149), puis correction PR #150, puis optimisation HTML PR #151. **Les builds Cloudflare de PR #149 et #150 ont échoué** ; la publication de la PR #151 n'était pas confirmée à la rédaction, son check Cloudflare n'était pas présent. Le site public restait sur le commit stable `69af52dfdc27fc17c80582acd168ada49efc435c`, galerie 404. Les logs Cloudflare demandent une session autorisée. Ne pas déclarer la galerie publiée avant `Cloudflare Pages success`, le SHA public exact dans `/deployment.json` et la vérification navigateur des 50 volets.

**Cette nouvelle branche de storyboards est indépendante**, en PR brouillon ; aucune fusion ni nouveau déploiement Cloudflare ne doit être tenté tant que l'incident de la galerie n'est pas isolé.

## Conditions de réussite de l'ensemble des lots

- 50 produits avec un média de qualité visuelle homogène équivalent à C1T, pas seulement 50 fichiers existants.
- 300 gestes, chacun distinct et source-conforme, descriptions visibles dans les trois langues ; source FT/FDS approuvée pour les performances et pratiques.
- Aucun asset remplacé sans original conservé et signature SHA reconnue.
- Audit visuel réellement fait par produit sur le site (captures, crops, résolution, RTL, responsive) et recette Cloudflare/CI exécutée.
- Données comptables/ERP non concernées. Les sorties génératives contenant des affirmations de conformité du site sont exclues.
