# Lot 17 — Libellés de section FR/AR/EN restants

Date : 1er novembre 2026. Lot complémentaire à la PR #11.

## Constat sur les captures CI du lot 16

Sur la page arabe d'accueil, l'étiquette de la section des familles FENEK affichait toujours `FENEK COLLECTION` en anglais. Sur la galerie 3D, l'étiquette `NextGen · Design study` restait également en anglais. Le reste de la navigation RTL était correctement construit et les posters 3D sont visibles.

## Corrections

- `src/pages/[lang]/index.astro` : légende localisée `Collection FENEK` (FR), `فئات FENEK` (AR), `FENEK collection` (EN), affichage `dir="auto"`. Le **nom de marque** FENEK est conservé tel quel.
- `src/pages/[lang]/emballages.astro` : `NextGen · Étude de conception` (FR), `NextGen · تصاميم أولية` (AR), `NextGen · Design study` (EN). NextGen est un nom de marque non traduit.
- `scripts/check_browser_pages.py` : assertions des deux libellés arabes sur les pages desktop/mobile.
- `tests/test_lot17_arabic_eyebrows.py` : tests sources, conservation des réserves commerciales et du catalogue `[]`.

## Limites et validations

- Aucune modification d'asset/packaging, donnée commerciale ou ERP; aucun Cloudflare, DNS, RLS, secret ou déploiement.
- Les textes intégrés aux étiquettes des maquettes 3D restent en partie en anglais, car ils font partie des visuels de simulation non contractuels, non des textes localisés du site.
- Tester les deux workflows de PR avant merge puis le SHA `main`.
- Relecture par un professionnel arabophone de la construction recommandée avant communication contractuelle.
