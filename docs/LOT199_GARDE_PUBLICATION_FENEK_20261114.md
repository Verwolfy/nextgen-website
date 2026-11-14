# Lot 199 — contrôle read-only de la publication des 50 guides FENEK

Date : 14 novembre 2026. **PR en brouillon ; aucune modification des médias, FT/FDS, pages commerciales ou déploiement.**

## Diagnostic vérifié

- GitHub `main` : `c1f7c32c3dba75bfa27621c5fb4286c75a85a5d3`.
- Site public `/deployment.json` : `69af52dfdc27fc17c80582acd168ada49efc435c` (écart de version).
- Galerie `/fr/avant-premiere/audit-50-illustrations/` : HTTP 404.
- PR #152 contient les descriptions des 234 scènes à harmoniser ; aucun visuel source brouillon n'est approuvé techniquement.
- Aucun accès authentifié aux logs Cloudflare Pages dans cette session. Ne pas deviner l'origine du blocage.

## Nouvelle commande d'audit

```sh
node --test tests/audit_fenek_live_release.test.mjs
node scripts/audit_fenek_live_release.mjs --expected-commit <SHA_COMPLET_MAIN>
node scripts/audit_fenek_live_release.mjs --expected-commit <SHA_COMPLET_MAIN> --full
```

La version courte exige : même SHA GitHub/production, galerie HTTP 200, exactement 50 produits identifiés, et six scènes officielles par produit avec chemins et SHA déclarés.

`--full` ajoute : vérification **du SHA-256 des 50 sprites WebP servis en public**, et vérification **des 150 pages FR/EN/AR** (identité, mappage de sprite, numéro des six étapes). Le script **échoue explicitement** au premier écart et n'utilise aucune clé privée. Des tests hors réseau vérifient le comportement bloquant et le cas nominal.

Le script **ne valide pas** la qualité artistique, l'exactitude des gestes, les FT/FDS, l'accessibilité en navigateur ni l'absence de cache obsolète sur tous les clients.

## Conditions pour déploiement

1. Obtenir les journaux Cloudflare Pages des commits en échec ; isoler et corriger la cause prouvée.
2. Exécuter `npm ci`, `npm run build` et les suites Python/Node sur la branche. Une CI en erreur **avant ses étapes** n'est pas une preuve d'échec du code.
3. Vérifier `/deployment.json` sur l'origine publique (commit réellement déployé).
4. Exécuter l'audit de publication ci-dessus en mode complet ; recueillir sorties, URLs, screenshots mobile/desktop.
5. Reprendre seulement ensuite la fabrication des 234 scènes, en gardant la double validation graphique et technique.

Suivi : [incident #154](https://github.com/Verwolfy/nextgen-website/issues/154) et [storyboards #152](https://github.com/Verwolfy/nextgen-website/pull/152).

## État de cette PR

Fichier de contrôle et tests ajoutés dans une branche isolée. Aucun média public remplacé, aucun push sur `main` et aucun déploiement déclenché. Validation complète du build et du site réel toujours à produire.


## Audit renforcé (reprise du 14/11/2026)

- Le script exige désormais **un véritable `--media:url(...)` par produit**, pas seulement un lien vers l'asset, ainsi que **la présence de six images rendues `data-v3-step` et de l'empreinte `data-v3-enhanced-hash`** sur chaque fiche.
- **10/10 tests unitaires réussis localement** sur la copie de travail Node 22 ; trois nouveaux tests adversariaux vérifient image seulement liée, hash trompeur et étape visuelle manquante alors que le texte est présent. Le run GitHub de cette branche **ne prouve pas encore** leur exécution distante.
- Contrôle direct de la galerie HTML de `main` et du manifeste JSON via le dépôt connecté : **50/50 volets, 50/50 références CSS de sprites attendues, 300/300 cases officielles et 0 écart structurel**. Cela ne prouve pas leur publication sur Cloudflare.
- Vérification du run Actions `43587810089` (commit `c07893f`) : le job `verify` a été enregistré comme `failure` en environ **une seconde**, avec `runner_id=0`, `steps=[]`, sans runner attribué et sans exécution de script visible. Cause de l'indisponibilité du runner encore **non établie**.
- Nouveau contrôle public : `/deployment.json` renvoie toujours `69af52d...` et la galerie renvoie **404**. Le blocage de publication est maintenu.
- En local, BOND-GR-HR possède désormais **trois candidats** étapes 1 à 3 (pas d'approbation). Deux générations de l'étape 4 ont été **rejetées** car elles présentaient des textes chiffrés/affirmations techniques non étayées. Ne jamais intégrer ces infographies.

### Continuation recommandée

1. Faire lever l'échec **avant attribution du runner** GitHub Actions par le propriétaire du compte GitHub, avec la bannière d'erreur détaillée et le statut Actions/facturation/limites dans les réglages (sans supposer la cause).
2. Obtenir l'accès lecture aux déploiements et logs Cloudflare Pages ; retrouver l'échec de publication exact (l'accès navigateur Cloudflare authentifié n'est pas connecté).
3. Relancer les tests `node --test`, les suites complètes, le build Astro, puis le `--full` en production après publication synchronisée.
4. Continuer les scènes GR-HR 4–6 **seulement sous forme de photos de chantier sans texte** ; rejeter toute génération ajoutant des quantités ou des normes non vérifiées ; validation graphique et FT/FDS avant activation.

---

## Reprise du 14 novembre 2026 — vérifications supplémentaires

### Verrou source, scènes visibles et automatisation

- Contrôle ajouté avant toute requête HTTP : **50 lignes exactes** dans le catalogue et dans le manifeste des médias, codes/slugs uniques et cohérents, empreintes SHA-256 hexadécimales, chemins WebP canoniques. Le mode rapide ne peut plus accepter des listes vides ou un manifeste tronqué.
- Analyse HTML de la galerie : chaque produit doit présenter six cellules distinctes contenant un élément `crop` avec la bonne position CSS, pas seulement six légendes.
- `package.json` : nouvelle commande `npm run check:illustrations` ; le `build` Astro/Cloudflare la lance en premier, sans accès réseau ni modification du site.
- **14/14 tests de la copie locale équivalente réussis** sous Node 22. La CI GitHub de cette branche reste à vérifier indépendamment. Cette validation ne vaut pas exécution du build Astro complet.

### Recette de production indépendante, sans modification

- Le site a retourné du HTML pour les **150/150 pages FR/EN/AR** (50 produits).
- Un contrôle détaillé, obtenu via extraction HTML publique pour **150/150 pages**, a confirmé **900 étapes**, **900 blocs d'image**, **900 références CSS** vers les bons sprites avec les bonnes empreintes déclarées, **0 écart structurel**.
- Quatre témoins (C1T, GR-HR, ACR-RF, FAC-M) vérifiés dans les trois langues ; aucun défaut structurel.
- Inspection navigateur de GR-HR : pages et sprite accessibles ; la capture ne permettait pas de confirmer la visibilité des six vignettes. L'HTML public fournit des `<details open>` et six éléments `data-v3-step` : **ne pas qualifier cette ambiguïté de panne CSS sans mesure navigateur complémentaire**.
- Ces inspections ne prouvent **pas** que les 50 fichiers WebP servis ont tous le SHA attendu en bytes, ni qu'ils sont correctement dessinés à l'écran mobile/desktop, ni que les procédures FT/FDS sont approuvées. Le mode `--full` prévu à cet effet reste à exécuter après la synchronisation du déploiement.

### Publication et incidents

- Dernier `main` vérifié : `c1f7c32c3dba75bfa27621c5fb4286c75a85a5d3` ; marqueur production toujours `69af52dfdc27fc17c80582acd168ada49efc435c` ; galerie en HTTP 404.
- GitHub Actions de la branche d'audit : les jobs échouent avant leurs étapes, sans logs d'exécution des tests accessibles ; aucune cause racine certifiée.
- Les nouvelles images GR-HR (trois scènes candidates en local) restent **non validées, non intégrées**. Deux essais de l'étape 4 avec chiffres inventés ont été rejetés.

**État : PR en BROUILLON, aucun merge ni déploiement réalisé.**
