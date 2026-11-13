# Lot 194 — audit public des 50 modes d'emploi et galerie des 300 scènes

Date : 13 novembre 2026 · Marque : FENEK / NextGen Building Solutions · Site : https://nextgen-buildingsolutions.com/

## Résultat des vérifications avant la création de la galerie

1. **150/150 fiches publiques FR/EN/AR accessibles** via consultation live du site, par lots de dix produits (50 références par langue).
2. **148/150 fiches : six titres égaux au référentiel de notices**. Les **2 exceptions sont BOND-C1T et BOND-C1TE en anglais**, dont les titres publics utilisent depuis l'origine une rédaction éditoriale distincte. Les deux pages restent accessibles; ce n'est pas une erreur de lien média prouvée.
3. **50/50 références** présentes dans `src/data/catalogue-projets.json`, `fenek-v3-manuals.json`, `fenek-enhanced-artwork.json`.
4. **50/50 SHA-256 des médias WebP sur main identiques** aux empreintes de l'audit visuel du lot 186 (aucun changement graphique occulté depuis).
5. **11 planches de niveau A** proches du modèle FENEK-BOND C1T, **3 de niveau B** intermédiaire (façades), **36 de niveau C** pictogrammes simplifiés. Cela concerne le **niveau graphique** : la présence, l'empreinte et la résolution d'une image ne suffisent pas à démontrer la qualité de représentation d'un geste.
6. **42 médias WebP distincts pour 50 produits**, cinq groupes d'images communes (13 références). Une scène partagée n'est pas systématiquement fausse, mais les instructions spécifiques doivent être vérifiées.
7. Le build **Cloudflare Pages** exécuté au lot 193 comportait un contrôle Node `verify_fenek_deployment.mjs`, réussi, vérifiant 50 WebP avec SHA et dimensions, 150 pages et les trois médias premium provisoires. Les quatre workflows GitHub Actions classiques demeurent bloqués avant exécution des tests.

## Rapport par gamme

| Gamme | Produits | Qualité A | Qualité B | Qualité C | À harmoniser |
|---|---:|---:|---:|---:|---:|
| BOND | 16 | 11 | 0 | 5 | 5 |
| PROOF | 11 | 0 | 0 | 11 | 11 |
| FLOW | 12 | 0 | 0 | 12 | 12 |
| PAINT | 11 | 0 | 3 | 8 | 11 |
| **Total** | **50** | **11** | **3** | **36** | **39** |

## Inventaire individuel des médias de production

| # | Produit | Classe visuelle | Partage le média avec | Candidat premium disponible |
|---:|---|:---:|---|---|
| 1 | [BOND-C1T](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-c1t/) | A | — | Ancien WebP conservé |
| 2 | [BOND-C1TE](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-c1te/) | A | — | Ancien WebP conservé |
| 3 | [BOND-C2FT](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-c2ft/) | A | — | Ancien WebP conservé |
| 4 | [BOND-C2TE](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-c2te/) | A | — | Ancien WebP conservé |
| 5 | [BOND-C2TE-S1](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-c2te-s1/) | A | — | Ancien WebP conservé |
| 6 | [BOND-CG1](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-cg1/) | A | — | Ancien WebP conservé |
| 7 | [BOND-CG2WA](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-cg2wa/) | A | — | Ancien WebP conservé |
| 8 | [BOND-CT-C25-F5](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-ct-c25-f5/) | A | — | Ancien WebP conservé |
| 9 | [BOND-R2](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-r2/) | A | — | Ancien WebP conservé |
| 10 | [BOND-R3](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-r3/) | A | BOND-R4 | Ancien WebP conservé |
| 11 | [BOND-R4](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-r4/) | A | BOND-R3 | Ancien WebP conservé |
| 12 | [BOND-GR-HR](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-gr-hr/) | C | — | Ancien WebP conservé |
| 13 | [BOND-GP-CSII](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-gp-csii/) | C | — | Ancien WebP conservé |
| 14 | [BOND-OC-CSIII](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-oc-csiii/) | C | — | Ancien WebP conservé |
| 15 | [BOND-M5](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-m5/) | C | — | Ancien WebP conservé |
| 16 | [BOND-M10](https://nextgen-buildingsolutions.com/fr/documentation/fenek-bond-m10/) | C | — | Ancien WebP conservé |
| 17 | [PROOF-CM-O1P](https://nextgen-buildingsolutions.com/fr/documentation/fenek-proof-cm-o1p/) | C | — | 1 scène brouillon (étape 1) |
| 18 | [PROOF-CM-O2P](https://nextgen-buildingsolutions.com/fr/documentation/fenek-proof-cm-o2p/) | C | — | Ancien WebP conservé |
| 19 | [PROOF-PU-1K](https://nextgen-buildingsolutions.com/fr/documentation/fenek-proof-pu-1k/) | C | — | 1 scène brouillon (étape 5) |
| 20 | [PROOF-ACR-RF](https://nextgen-buildingsolutions.com/fr/documentation/fenek-proof-acr-rf/) | C | — | V4: 6 scènes brouillon |
| 21 | [PROOF-EP-PRIM](https://nextgen-buildingsolutions.com/fr/documentation/fenek-proof-ep-prim/) | C | — | Ancien WebP conservé |
| 22 | [PROOF-EP-SR](https://nextgen-buildingsolutions.com/fr/documentation/fenek-proof-ep-sr/) | C | — | Ancien WebP conservé |
| 23 | [PROOF-EP-SB](https://nextgen-buildingsolutions.com/fr/documentation/fenek-proof-ep-sb/) | C | — | Ancien WebP conservé |
| 24 | [PROOF-EP-INJ](https://nextgen-buildingsolutions.com/fr/documentation/fenek-proof-ep-inj/) | C | — | Ancien WebP conservé |
| 25 | [PROOF-EP-ANC](https://nextgen-buildingsolutions.com/fr/documentation/fenek-proof-ep-anc/) | C | — | Ancien WebP conservé |
| 26 | [PROOF-PU-INJ](https://nextgen-buildingsolutions.com/fr/documentation/fenek-proof-pu-inj/) | C | — | Ancien WebP conservé |
| 27 | [PROOF-PU-SEAL](https://nextgen-buildingsolutions.com/fr/documentation/fenek-proof-pu-seal/) | C | — | Ancien WebP conservé |
| 28 | [FLOW-WR-N](https://nextgen-buildingsolutions.com/fr/documentation/fenek-flow-wr-n/) | C | FLOW-SP-HR | Ancien WebP conservé |
| 29 | [FLOW-SP-HR](https://nextgen-buildingsolutions.com/fr/documentation/fenek-flow-sp-hr/) | C | FLOW-WR-N | Ancien WebP conservé |
| 30 | [FLOW-SP-RT](https://nextgen-buildingsolutions.com/fr/documentation/fenek-flow-sp-rt/) | C | FLOW-SP-PF, FLOW-RT, FLOW-AC | Ancien WebP conservé |
| 31 | [FLOW-SP-PF](https://nextgen-buildingsolutions.com/fr/documentation/fenek-flow-sp-pf/) | C | FLOW-SP-RT, FLOW-RT, FLOW-AC | Ancien WebP conservé |
| 32 | [FLOW-RT](https://nextgen-buildingsolutions.com/fr/documentation/fenek-flow-rt/) | C | FLOW-SP-RT, FLOW-SP-PF, FLOW-AC | Ancien WebP conservé |
| 33 | [FLOW-AC](https://nextgen-buildingsolutions.com/fr/documentation/fenek-flow-ac/) | C | FLOW-SP-RT, FLOW-SP-PF, FLOW-RT | Ancien WebP conservé |
| 34 | [FLOW-AE](https://nextgen-buildingsolutions.com/fr/documentation/fenek-flow-ae/) | C | — | Ancien WebP conservé |
| 35 | [FLOW-WP](https://nextgen-buildingsolutions.com/fr/documentation/fenek-flow-wp/) | C | — | Ancien WebP conservé |
| 36 | [FLOW-VMA](https://nextgen-buildingsolutions.com/fr/documentation/fenek-flow-vma/) | C | — | Ancien WebP conservé |
| 37 | [FLOW-CI](https://nextgen-buildingsolutions.com/fr/documentation/fenek-flow-ci/) | C | — | Ancien WebP conservé |
| 38 | [FLOW-CURE](https://nextgen-buildingsolutions.com/fr/documentation/fenek-flow-cure/) | C | — | Ancien WebP conservé |
| 39 | [FLOW-LAT](https://nextgen-buildingsolutions.com/fr/documentation/fenek-flow-lat/) | C | — | Ancien WebP conservé |
| 40 | [PAINT-INT-M](https://nextgen-buildingsolutions.com/fr/documentation/fenek-paint-int-m/) | C | PAINT-INT-S, PAINT-INT-WA | Ancien WebP conservé |
| 41 | [PAINT-INT-S](https://nextgen-buildingsolutions.com/fr/documentation/fenek-paint-int-s/) | C | PAINT-INT-M, PAINT-INT-WA | Ancien WebP conservé |
| 42 | [PAINT-INT-WA](https://nextgen-buildingsolutions.com/fr/documentation/fenek-paint-int-wa/) | C | PAINT-INT-M, PAINT-INT-S | Ancien WebP conservé |
| 43 | [PAINT-FAC-M](https://nextgen-buildingsolutions.com/fr/documentation/fenek-paint-fac-m/) | B | — | Ancien WebP conservé |
| 44 | [PAINT-FAC-EL](https://nextgen-buildingsolutions.com/fr/documentation/fenek-paint-fac-el/) | B | — | Ancien WebP conservé |
| 45 | [PAINT-FAC-SX](https://nextgen-buildingsolutions.com/fr/documentation/fenek-paint-fac-sx/) | B | — | Ancien WebP conservé |
| 46 | [PAINT-PRIM-A](https://nextgen-buildingsolutions.com/fr/documentation/fenek-paint-prim-a/) | C | PAINT-PRIM-FX | Ancien WebP conservé |
| 47 | [PAINT-PRIM-FX](https://nextgen-buildingsolutions.com/fr/documentation/fenek-paint-prim-fx/) | C | PAINT-PRIM-A | Ancien WebP conservé |
| 48 | [PAINT-TXT-F](https://nextgen-buildingsolutions.com/fr/documentation/fenek-paint-txt-f/) | C | — | Ancien WebP conservé |
| 49 | [PAINT-SOL-A](https://nextgen-buildingsolutions.com/fr/documentation/fenek-paint-sol-a/) | C | — | Ancien WebP conservé |
| 50 | [PAINT-ENT-L](https://nextgen-buildingsolutions.com/fr/documentation/fenek-paint-ent-l/) | C | — | Ancien WebP conservé |

## Correspondances d'images partagées

1. BOND-R3 ; BOND-R4.
2. FLOW-WR-N ; FLOW-SP-HR.
3. FLOW-SP-RT ; FLOW-SP-PF ; FLOW-RT ; FLOW-AC.
4. PAINT-INT-M ; PAINT-INT-S ; PAINT-INT-WA.
5. PAINT-PRIM-A ; PAINT-PRIM-FX.

Tous les 50 WebP restent conservés en `public/images/application-upgraded/`. Les médias premium supplémentaires sont des **propositions non approuvées** : ACR-RF V4 six scènes 1620×720, PU-1K une scène étape 5, CM-O1P une scène étape 1. Les deux autres produits du sous-lot PROOF (PU-1K, CM-O1P, CM-O2P) restent à **2/18 scènes nouvelles**, donc **16 scènes manquantes** dans ce sous-lot. Plus largement, harmoniser les 39 produits implique jusqu'à **234 scènes de chantier** à reprendre ; les huit scènes candidates disponibles doivent elles-mêmes faire l'objet d'une revue technique et graphique.

## Nouvel outil de contrôle visuel

Page ajoutée au dépôt, **non indexée**, route :
`https://nextgen-buildingsolutions.com/fr/avant-premiere/audit-50-illustrations/`.

- Sections BOND (16), PROOF (11), FLOW (12), PAINT (11).
- Pour chaque produit : volet déroulant, six découpes du WebP source, titres français exacts, qualité A/B/C, SHA-256, lien vers ses trois fiches FR/EN/AR et vers le média source.
- Références BOND-C1T et PROOF-ACR-RF ouvertes au chargement pour comparer immédiatement le standard et le pictogramme.
- Candidats graphiques disponibles (6 ACR + 1 PU-1K + 1 CM-O1P) visibles dans les fiches correspondantes, **sans modifier les procédures produit**.
- 50 volets, 300 scènes historiques, 6 scènes V4 ACR et 2 images individuelles supplémentaires ; 308 images HTML et 3 groupes de prévisualisation.
- `noindex,nofollow,noarchive`, pas de JavaScript ni formulaire. Groupes et produits accessibles au clavier. Images répétées à URL identique, chargement différé.
- Garde-fou `scripts/verify_fenek_deployment.mjs` renforcé : il bloque maintenant le build Cloudflare si la galerie manque ou n'a plus 50 produits, 306 cases, 3 ensembles candidats, ou si un couple code/slug/SHA diverge.

## État réel et prochaines actions

**Une galerie de revue n'est pas une amélioration photographique**. L'utilisateur peut examiner les scènes dans le site, mais les niveaux B/C restent à optimiser. Ne pas déclarer les 39 produits mis au niveau C1T sur la seule base de cette galerie.

Ordre recommandé :
1. **Lot 195 — PROOF** : terminer les 16 scènes manquantes du sous-lot PU-1K, CM-O1P, CM-O2P ; puis les autres références PROOF 11/11. Une vraie scène isolée, sans texte inventé, par étape.
2. **Lot 196 — BOND** : cinq références insuffisantes ; maintenir les 11 planches de niveau A.
3. **Lot 197 — FLOW** : 12 produits ; éviter les scènes génériques recyclées, notamment les quatre produits ayant le même WebP.
4. **Lot 198 — PAINT** : huit références niveau C, puis les trois façades niveau B.
5. **Lot 199 — revue globale** : contrôle graphique de chacune des 300 scènes, cohérence des gestes par FT/FDS approuvées, 150 pages FR/EN/AR, responsive 390px et desktop, RTL arabe, et activation par produit seulement après validation.

**Publication** : fusionner une petite PR séparée sur `main`, contrôler le check Cloudflare Pages et `/deployment.json` avec le SHA exact, puis ouvrir la galerie publique et inspecter les images. Aucun remplacement de notice ou de certification autorisé tant que FT/FDS et QA visuelles n'ont pas été approuvées. La grande PR #140 demeure brouillon, les 47 SVG éditoriaux ne sont pas au niveau graphique C1T.

**Limite de la vérification** : les 150 pages ont été consultées pour leur présence et six titres. Les classifications graphiques proviennent de l'inspection manuelle antérieure des 50 WebP du main ; les 50 SHA n'ayant pas changé, elles restent applicables. L'audit des couleurs, mains, outils et scènes en 300 captures d'écran indépendantes n'a pas été exécuté et ne doit pas être présenté comme terminé.
