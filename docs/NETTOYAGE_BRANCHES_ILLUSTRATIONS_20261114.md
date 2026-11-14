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
