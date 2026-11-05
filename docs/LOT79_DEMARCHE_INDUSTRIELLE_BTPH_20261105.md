# Lot 79 — Nouvelle démarche industrielle NextGen (BTPH)

Date : 2026-11-05. Dépôt : `Verwolfy/nextgen-website`.

## Source et intention

L'utilisateur a fourni `demarche-nextgen.html` avec une présentation trilingue FR/AR/EN en trois cartes, badges, illustrations SVG et CTA. Il a demandé de conserver l'esprit visuel tout en recentrant l'approche sur une **entreprise de production BTPH** plutôt qu'une entreprise de simple conseil.

## Résultat éditorial

**Notre démarche industrielle** :
1. **Concevoir pour le terrain** : besoins des chantiers, développement des solutions et choix des familles de produits.
2. **Produire avec méthode** : matières premières, fabrication, conditionnement et contrôles à définir et valider selon les références.
3. **Distribuer et accompagner** : disponibilité, distributeurs, applicateurs et documentation vérifiée avant diffusion.

Les mêmes intentions sont traduites en arabe et en anglais.

## Modifications du site

- `src/data/editorial.ts` : approche FR/AR/EN + surtitre, 3 groupes de thèmes, CTA et réserve de validation.
- `src/components/AboutStory.astro` : 3 cartes illustrées sur la page À propos ; conservation de la présentation initiale et de la mascotte ; design sombre compatible mobile et arabe RTL ; lien de contact réel.
- `public/images/approche/01-concevoir.svg` : étude chantier.
- `public/images/approche/02-produire.svg` : installation de production, mélange et conditionnement.
- `public/images/approche/03-distribuer.svg` : entrepôt, palettes, transport et vérifications.
- `tests/test_lot79_manufacturing_approach.py` : test des 3 langues, des illustrations locales, et des garde-fous d'information.

Le site contient ses propres routes /fr/, /ar/, /en/ ; aucun widget JavaScript de langue séparé n'est introduit. La variante HTML autonome `demarche-nextgen-production.html` est disponible dans la conversation.

## Limites et validation

- Éviter les assertions non étayées de laboratoire opérationnel, certifications qualité, FT/FDS approuvées, performances ou capacités industrielles précises.
- La démarche est une **orientation de production** et n'établit pas un statut technique/commercial approuvé pour les 50 fiches catalogue.
- Pas de changement DNS, Cloudflare, Access, `noindex`, Supabase, ERP, catalogue, prix, fiches techniques ni collecte.
- L'intégration GitHub n'est pas une preuve de déploiement Cloudflare.

## Reprise

1. Vérifier les deux CI sur PR (Astro/sécurité et Chromium).
2. Corriger tout échec, fusionner avec vérification du SHA de branche.
3. Vérifier les deux CI de `main` après fusion et journaliser leur résultat.
4. En lecture seule, contrôler la version réellement servie par Cloudflare sans modifier l'accès public ; obtenir preuves R&D/Qualité/HSE avant toute publication de valeurs techniques.
