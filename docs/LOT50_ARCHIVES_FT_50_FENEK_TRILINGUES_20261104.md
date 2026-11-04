# Lot 50 — Enrichissement documentaire trilingue des 50 produits FENEK

> **Mise à jour du 4 novembre 2026 (lot 51).** Les 16 références BOND sont désormais en **sac 25 kg exclusivement**, confirmé par l'utilisateur. Les formats 5/10 kg ci-dessous décrivent l'ancien état du catalogue et ne sont plus proposés. Voir [Lot 51](LOT51_BOND_CONDITIONNEMENT_25KG_20261104.md). La validation industrielle reste en attente.

Date : 2026-11-04 · Statut : **présentations provisoires ; aucune FT/FDS approuvée**.

## Sources analysées

Trois archives fournies par l'utilisateur : **108 fiches PDF françaises (190 pages)**,
**171 anglaises (241 pages)** et **86 arabes (186 pages)**,
soit **365 fichiers / 617 pages** au total. Les fichiers anglais contiennent
des variantes et doublons ; l'extraction de certains textes arabes conserve
des ligatures et ordres de caractères irréguliers.

Le rapprochement par familles et thèmes a trouvé des analogies documentaires
pour **41 des 50 références en FR, 29 en EN et 28 en AR**. Ce sont des
**documents de fabricants tiers**, non des résultats de laboratoire
ou des formulations NEXTGEN.

Neuf références n'ont pas de correspondant thématique direct suffisant dans
ces archives : FLOW-CI, PAINT-ENT-L, PAINT-FAC-SX, PAINT-INT-M,
PAINT-INT-S, PAINT-INT-WA, PAINT-TXT-F, PROOF-PU-1K et PROOF-PU-INJ.

## Modifications site

- Contexte : src/data/fenek-application-context.ts — 24 profils de préparation et supports, disponibles en FR/EN/AR et utilisés par les 50 références.
- Données : src/data/fenek-qualification-notes.ts — 50 notes contextualisées
  propres au **thème de vérification** de chaque référence, chacune en
  FR, EN et AR. Ce sont des critères à étudier, pas des performances acquises.
- Page : src/pages/[lang]/documentation/[slug].astro — nouveau bloc
  « Critères à vérifier pour cette référence » dans « Informations techniques » et un bloc contextualisé de préparation dans « Conditions d’application » ;
  les 8 accordéons, les usages et les sections Application/Documents restent en place.
- Export A4 : src/components/FenekPrintableSheet.astro — bloc technique
  et préparation du support personnalisés dans le document de présentation provisoire ; logo et charte NEXTGEN conservés.
- Style : src/styles/site.css.
- Tests : tests/test_lot50_fenek_qualification_notes.py ;
  vérifications navigateur enrichies dans scripts/check_browser_pages.py.

## Règles éditoriales et risques

1. Autoriser la **reformulation professionnelle des catégories d'usage,
   supports, préparation et points de contrôle** lorsque la correspondance
   documentaire est plausible. Les notes sont présentées comme critères
   de qualification, jamais comme données mesurées.
2. **Ne pas** transférer les densités, dosages, résistances, temps de prise,
   composants, classes normatives, mentions de sécurité ou certificats
   des fabricants sources aux produits FENEK.
3. L'identifiant de gamme (p. ex. C1T, C2TE, R3) est une dénomination
   de catalogue **et ne prouve aucune conformité** à la norme associée.
4. L'arabe doit recevoir une relecture professionnelle sur PDF final :
   l'extraction PDF peut inverser l'ordre de certains mots.
5. Aucun fichier fournisseur n'est ajouté sous public/, src/ ou dist/
   pour être téléchargé ; les véritables FT/FDS ne sont pas publiées.
6. catalogue-projets.json, les drapeaux certifie=false,
   commercialise=false, les conditions noindex et les protections
   de publication sont préservés.

## Conditionnements : validation séquentielle utilisateur

Les **conditionnements candidats actuels** ne sont pas des données
de conditionnement définitivement approuvées :

- BOND (16 références) : sacs 5, 10 et 25 kg proposés.
- FLOW (12) : bidons 5/20 L, fûts 200 L, IBC 1 000 L proposés.
- PAINT (11) : seaux 5, 10, 20 kg proposés.
- PROOF : 3 références proposées en seaux 5/20 kg ; 7 en kits résine
  sans composition/poids net confirmés ; **PU-SEAL sans format**.
- Les 50 références demandent confirmation une par une.
- Pour les kits : composition A/B, contenance nette et unité de chaque
  composant ; pour les liquides : aucune conversion L -> kg sans densité validée.
- Ne pas écrire ces confirmations dans le catalogue ni dans Supabase
  avant réponse individuelle.

## Prochaines actions

1. Exécuter les workflows de vérification statique et navigateur
   en PR et sur le commit final main.
2. Inspecter l'export A4 FR/EN/AR pour la référence C1T ;
   confirmer l'absence de seconde page orpheline.
3. Recueillir, **dans l'ordre des 50 produits**, les confirmations de
   conditionnements de l'utilisateur, en commençant par **FENEK-BOND C1T**.
4. Obtenir les documents propres à la formulation NEXTGEN pour qualification,
   validation HSE et émission d'une FT/FDS officielle ultérieure.

Le rapport détaillé des noms de fichiers source et de leur rapprochement
aux 50 références est conservé en JSON d'audit hors des actifs publics.
