# NextGen — Lot 128 — Modes d'emploi V3, référence 2/50 : BOND-C1TE

Date : 11 novembre 2026. Dépôt `Verwolfy/nextgen-website`.

## Source et correspondance
- ZIP utilisateur `NEXTGEN_modes_emploi_V3.zip`, dossier `fenek-bond-c1te`, `index.csv` : `BOND-C1TE` / `FENEK-BOND C1TE`.
- Correspondance avec le catalogue NextGen : `code=BOND-C1TE`, `slug=fenek-bond-c1te`, famille BOND, colle carrelage à temps ouvert allongé.
- Six panneaux visuels et titres bilingues AR/FR vérifiés individuellement : préparer, EPI, eau prescrite sans chiffre, repos/remalaxage sous condition de FT, peigne cranté, pose dans le temps ouvert validé.
- C1TE est distinct de C1T (dernier panneau « Poser avant la fin du temps ouvert ») : code et URL du WebP non interchangeables.

## Intégration
- Sprite : `public/images/application-v3/fenek-bond-c1te-steps.webp`, 2160×1440, 229446 octets, SHA-256 `0d4ea8e4b5fc7ec44e3b772f470aeffa81cc50009b2f724d0420c89fd8cd58ce`.
- Registre `src/data/fenek-v3-reviewed.ts` : deuxième entrée sous contrôles stricts code/slug.
- FR/AR/EN, RTL, mobile pleine largeur, thème nuit, informations non certifiées.
- Tests de HTML et smoke Cloudflare : 150 guides toujours présents, six images spécifiques pour les 2 références contrôlées, 48 autres non modifiées.
- Chromium : contrôle C1TE de la fiche, de son URL, de la taille et de la langue.

## Validation requise
Les sources du ZIP signalent statut **BROUILLON** : classe et temps ouvert non certifiés, quantité d'eau/sac et repos non déterminés par le LABO, sécurité/FDS à confirmer. Aucune valeur chiffrée de temps ouvert n'est affichée. Pas de changement Supabase.
