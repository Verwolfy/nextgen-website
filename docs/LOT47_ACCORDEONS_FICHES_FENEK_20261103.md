# Lot 47 — Fiches produits FENEK avec accordéons : étude et exécution

**Date :** 3 novembre 2026  
**Dépôt :** `Verwolfy/nextgen-website`  
**Branche :** `feat/lot47-fenek-accordion-documentation-20261103`

## Demande utilisateur

Reproduire le principe d'une page technique à quatre rubriques cliquables, d'après des captures de produit professionnel : Aperçu / Détails produits / Application / Documents. Les informations secondaires s'ouvrent dans des accordéons. Remplir les sections des références FENEK en s'inspirant de l'étude documentaire trilingue fournie antérieurement.

## Vérifications des sources

- Le modèle public de référence fournit bien des sections : utilisation, avantages, emballage, informations produit, caractéristiques, environnement et sécurité, conditions d'application, consommation, étapes d'application et documents.
- Archives reçues dans la conversation et auditées antérieurement : 108 PDF français (190 pages), 171 PDF anglais (241 pages) et 86 PDF arabes (186 pages), soit **365 PDF et 617 pages**.
- Rubriques récurrentes relevées : désignation, description, domaines d'emploi, propriétés, données mesurées, préparation/application, dosage/consommation, conditionnement/stockage et sécurité/FDS.
- Les sources ne décrivent pas des formulations, rapports d'essais ou FDS de NextGen ; elles servent ici de trame éditoriale et de glossaire technique. Certaines versions linguistiques divergent sur les poids, les ratios ou les unités. Pas de transfert de chiffres ou allégations vers FENEK.
- Ni les textes complets ni les images des sociétés sources ne sont republiés ; aucune marque tierce n'apparaît dans les pages statiques générées.

## Implémentation

1. `src/data/fenek-guides.ts` : synthèse rédactionnelle **24 profils métiers** couvrant les 50 codes FENEK. Chaque profil possède ses sujets techniques et points de contrôle en français, arabe et anglais ; un guide par famille (BOND/FLOW/PAINT/PROOF) ajoute préparation, choix du procédé, contrôles, consommation et sécurité. Les valeurs sont des **critères à examiner**, pas des résultats de laboratoire NextGen.
2. `src/pages/[lang]/documentation/[slug].astro` : en-tête référence, visuel exact, points clés, navigation à quatre ancres ; **8 accordéons** natifs `<details>/<summary>` :
   - Détails produits : Environnement et sécurité ; Information produit ; Information technique.
   - Application : Conditions d'application ; Consommation et dosage ; Étapes d'application.
   - Documents : Fiche produit (impression / PDF navigateur) ; dossier technique et FDS (demande via contact/email).
3. `src/styles/site.css` : design sobre et accessible, signes +/−, focus clavier, défilement horizontal des onglets sur mobile, ajustements RTL, styles A4.
4. Lors de l'impression, les accordéons s'ouvrent automatiquement puis retrouvent leur état précédent.
5. `scripts/check_built_pages.py`, `scripts/check_browser_pages.py`, `tests/test_lot47_documentation_accordions.py`, et tests historiques mis à jour : chaque page est présente, aucune marque tierce, pas d'invention de valeurs techniques, utilisation clavier, impression, absence de collecte.

## Portée et limites

- Les 150 pages correspondent aux 50 références × trois langues. Les références restent des **présentations de gamme** non encore certifiées et non commercialisées selon `src/data/catalogue-projets.json`.
- **Aucune valeur de consommation, dose, épaisseur, résistance, temps d'ouverture, classement normatif ou FDS officielle propre à FENEK n'est attribuée** sans justification.
- Le bouton « PDF » utilise la fonction d'impression du navigateur pour la fiche produit. Il ne prétend pas télécharger une FT ou FDS approuvée inexistante.
- Les données quantitatives doivent être ajoutées à un futur enregistrement maître FENEK avec essais et relecture des trois langues.
- Préserver `noindex,nofollow`, le refus de robots, `public/data/products.json=[]`, les URL existantes et les 46 images WebP de conception utilisées par le catalogue.
- Pas d'action Supabase, ERP, CRM, données juridiques, ni modification de l'historique Git.

## Prochaines étapes

- Exécuter `verify`, `smoke` et `Cloudflare Pages` sur le commit exact de la PR ; inspecter les journaux si échec.
- Fusionner `main` seulement après réussite des contrôles.
- Revérifier les tests et Cloudflare après fusion ; noter que le contrôle HTTP indépendant du domaine peut être bloqué dans l'environnement.
- À réception de données industrielles signées : associer formule, FDS, résultats et conditions spécifiques au produit ; générer alors des FT officielles versionnées.
