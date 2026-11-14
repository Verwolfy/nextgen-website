# Nettoyage GitHub NextGen — état et plan de consolidation (14 novembre 2026)

## Périmètre
Dépôt : `Verwolfy/nextgen-website`. Branche cible unique souhaitée : `main`.
Source : audit `NextGen_audit_50_illustrations_2026-11-13.md` joint à la conversation.

## Inventaire vérifié par le connecteur GitHub
- 126 branches distantes trouvées (deux pages de recherche : 100 + 26), dont `main`.
- 6 pull requests ouvertes : #38, #50, #131, #133, #140, #141.
- Une branche candidate ancienne (`feat/lot139-140-professional-paint-illustrations-20261112`) diverge de `main` : 146 commits en avance et 17 en retard. **Ne pas fusionner aveuglément.**
- Sur `main`, `src/data/fenek-enhanced-artwork.json` référence les WebP de `/images/application-upgraded/`. Le composant `src/components/FenekApplicationGuide.astro` les affiche, avec repli vers les guides V3.
- `package.json` lance actuellement `test:artwork-cleanup` et `check:illustrations` au build. Existence de `tests/lot200_official_artwork_isolation.test.mjs`.
- Tests non exécutés dans cette session ; aucun état de CI ou du déploiement actuel n'est attesté.

## Politique graphique issue de l'audit
- 11/50 bons rendus à préserver comme références visuelles (BOND-C1T et dix autres BOND).
- 3/50 rendus intermédiaires à reprendre (PAINT-FAC-M/EL/SX).
- 36/50 rendus insuffisants à remplacer, pas à retirer de la production avant remplacement validé.
- 39/50 nécessitent harmonisation. Les médias des 50 guides ne sont **pas** des fichiers inutilisés.
- Trois aperçus non intégrés : ACR-RF V4 (6/6), PU-1K (1/6), CM-O1P (1/6). Conserver hors publication jusqu'à validation visuelle et FT/FDS.
- Dans la PR #140, 47 SVG `public/images/application-professional/` sont schématiques et non approuvés ; ne pas les substituer aux médias existants.
- Les duplications de SHA-256 (42 sprites distincts pour 50 références) sont une piste de régénération produit par produit, pas une autorisation de supprimer un fichier référencé.

## Ordre opérationnel
1. Comparer chacune des 125 branches non-`main` avec `main` : avance/retard, commits uniques, état PR, fichiers, migrations, approbations et CI. Classer `fusionner`, `déjà intégré`, `archiver`, `bloqué`.
2. Ne fusionner que les ajouts uniques pertinents qui ne remplacent pas un guide officiel par un brouillon et ne réintroduisent pas d'anciennes maquettes. Rétablir les tests avant chaque fusion.
3. Établir un inventaire exhaustif des chemins sous `public/images/`, `src/assets/`, galeries de brouillon et scripts de génération. Vérifier les références dans le code, les manifestes et la chaîne de build, et la présence en production.
4. Retirer uniquement de `main` les médias **démontrés non référencés** et obsolètes ; garder les 50 sprites officiels et les éléments de référence graphiques en service. Vérifier build et routes FR/AR/EN.
5. Traiter les PR #38/#50/#131/#133/#140/#141 avant clôture ; les PR de brouillon ne sont pas à fusionner sans conditions.
6. Supprimer les branches distantes seulement après vérification qu'elles n'ont plus de contenu unique utile et qu'aucune PR ni déploiement ne dépend d'elles. Ne jamais forcer `main`.
7. Vérifier après intégration le SHA de `main`, les tests, puis le commit annoncé par `/deployment.json` sur le site public.

## Points bloquants
- La session n'a pas exécuté les tests Astro/Node ni obtenu une preuve CI verte.
- Le connecteur GitHub courant n'expose pas d'action de suppression des références de branches.
- Les fusions de PR brouillon ne sont pas approuvées techniquement.
- L'audit du 13/11 signale un déploiement public divergent de `main` ; revérification indispensable.

## Reprise
Priorité : comparaison exhaustive des branches, classement, puis nettoyage des médias morts après scan des dépendances. Ne pas déclarer la fusion ni les suppressions réalisées avant preuve GitHub.

## Mise à jour d'exécution — 14 novembre 2026

Comparaison Github `main...branche` réalisée pour **125/125** branches secondaires : **109 strictement derrière main (0 commit exclusif)**, **16 divergentes**. Ceci mesure l'ascendance des commits, non une revue de tous les effets métier.

**Suppression via interface GitHub :** le navigateur a annoncé la suppression de 23 branches déjà fusionnées. Un second inventaire GitHub a confirmé **103 branches restantes au total**, dont `main` (contre 126 initialement), et l'absence de trois branches échantillonnées parmi les 23 supprimées. **Aucune fusion nouvelle n'a été faite.**

### Les 16 branches divergentes à traiter individuellement

| Branche | Commits d'avance à la date du diagnostic | Position recommandée |
|---|---:|---|
| `diagnostic/cloudflare-domain-cache-20261102` | 10 | Audit diagnostic historique |
| `docs/fenek-tds-drafts-20261103` | 12 | Brouillons FT/FDS : ne pas publier sans validation |
| `feat/cloudflare-release-ready-20261101` | 2 | Examiner configuration et sécurité |
| `feat/lot7-browser-recette-20261101` | 4 | Tester pertinence CI |
| `feat/lot8-preproduction-gates-20261101` | 2 | Tester pertinence CI |
| `feat/lot9-access-gate-20261101` | 2 | Examiner verrouillage d'accès |
| `feat/lot60-theme-toggle-locale-menu-20261104` | 8 | Comparer UX actuelle |
| `feat/lot116-home-v4-video-clean-hero-20261107` | 12 | Comparer rendu vidéo |
| `feat/lot128-v3-product-by-product-20261111` | 16 | Vérifier guides produits |
| `feat/lot129-v3-50-guides-reconciled-20261111` | 4 | Vérifier guides produits |
| `feat/lot129-v3-guides-c2ft-20261111` | 9 | Vérifier guides produits |
| `feat/lot139-140-professional-paint-illustrations-20261112` | 146 | 47 SVG schématiques non approuvés, PR #140 ; pas de fusion brute |
| `fix/public-copy-cleanup-fr-ar-en-20261102` | 19 | Vérifier textes trilingues |
| `fix/public-editorial-residual-lot34-20261102` | 18 | Vérifier textes trilingues |
| `perf/v3-lots91-93-motion-a11y-mobile-20261105` | 7 | Comparer accessibilité/performance |
| `preview/lot186-acr-rf-20261112` | 3 | V4 non approuvée, PR #141 ; isoler hors production |

### Blocage restant

**86 branches** ont zéro commit d'avance et restent présentes ; elles peuvent être supprimées après confirmation des dépendances PR/CI. Les **16 branches divergentes** doivent être réconciliées par contenus, et non fusionnées sans discernement. Le connecteur GitHub ne propose pas la suppression des refs ; navigateur GitHub utilisable mais la suppression via UI est lente. Les tests Astro/Node et l'état déployé n'ont pas été attestés dans cette phase.

Prochaine opération : suppression sûre des 86 anciennes branches, revue et cherry-pick ciblé des 16 branches divergentes, puis tests avant toute suppression finale. Ne pas promettre une seule branche tant que GitHub n'en affiche pas une.

## Mise à jour — suppression supplémentaire de 12 branches déjà fusionnées (14 novembre 2026)

- Navigateur GitHub authentifié : 12 branches supplémentaires portant explicitement un statut « Merged pull request » ont été supprimées, avec confirmation nominative.
- Les PR fusionnées concernées sont : #103, #102, #99, #97, #96, #95, #94, #92, #91, #90, #89 et #88.
- Nouvel inventaire direct via API GitHub `/branches?per_page=100&page=1,2` : **91 branches au total, dont main, donc 90 secondaires restantes** ; deux branches supprimées vérifiées absentes de cette liste.
- Conjointement au lot précédent de 23 suppressions : **35 branches secondaires supprimées au total depuis l'inventaire initial de 126**. Les 16 branches divergentes sont conservées pour revue sélective.
- Aucun nouveau merge dans `main`, aucun média officiel effacé, aucun test de build certifié.
- **Blocage opérationnel** : crédit du navigateur connecté épuisé, donc autres suppressions via interface non poursuivies. Le connecteur GitHub ne dispose pas de la suppression de référence.

### Reprise prioritaire
Faire la revue technique et sélectionner les changements réellement utiles dans les 16 branches divergentes ; ensuite éliminer par lots les 90 branches secondaires en s'assurant qu'aucune PR ouverte ou workflow ne dépend de la branche. Réévaluer les compteurs à chaque lot car l'état GitHub évolue.

## 14 novembre 2026 — migration REST GitHub sans TinyFish

- API GitHub authentifiée : permissions du dépôt confirmées `admin=true`, `push=true` ; **91 branches**, dont `main`.
- Workflow temporaire ajouté sur `main` : `.github/workflows/cleanup-merged-branches-20261114.yml`, commit `13363869af84d266b2de7ba38e45ea24bc4bb47d`. Il appelle `GET /branches`, `GET /pulls`, `GET /compare/main...branche`, `GET /git/ref`, puis `DELETE /git/refs/heads/branche` uniquement si zéro commit d'avance, SHA inchangée et aucune PR ouverte.
- Exécution GitHub Actions [43607075314](https://github.com/Verwolfy/nextgen-website/actions/runs/43607075314) **FAILED avant toute étape** : job `132483915127`, `runner_id=0`, `steps=[]`, démarrage et échec en quelques secondes. Par conséquent **0 branche supprimée par cette tentative**.
- L'outil GitHub connecté peut interroger les endpoints REST en GET mais n'expose pas DELETE pour les refs. Les droits GitHub du compte ne changent pas cette limite de l'outil.
- Ne pas considérer le workflow comme exécuté. Corriger la disponibilité des runners/Actions ou exécuter le script par une voie REST authentifiée avec un jeton disposant de `Contents: write` ; **ne pas placer de jeton dans le dépôt ou cette conversation**.
- Aucun merge de branche divergente ni retrait d'illustration dans cette tentative.
