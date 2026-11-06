# Lot 105 — Évolution lumineuse de l'accueil NextGen

Validation : « ok » après présentation comparative FLASO INFO / NextGen V3.

## Périmètre
- Conserver l'identité bleu nuit, vert menthe et la typographie actuelles de NextGen.
- Sur le hero de l'accueil uniquement : éclaircir la zone droite avec un dégradé bleu nuit → vert profond → cyan, ajouter un liseré fin vert/cyan/bleu et améliorer le contraste des accents.
- Inverser le sens du dégradé pour l'arabe RTL ; variante mobile plus sombre pour préserver la lisibilité.
- Aucun visuel FLASO reproduit et aucune nouvelle police ou ressource externe ; changements CSS uniquement.

## Invariants
Logo NextGen, lecteur Nexo/Geno, fil d'informations lot 104, liens, thèmes, préférences de mouvement, page catalogue, couleurs des quatre gammes FENEK, noindex, formulaires inactifs et 50 références provisoires inchangés.

## Validation / mise en ligne
CI build/sécurité + tests Chromium + Lighthouse sur le SHA final avant fusion, puis contrôles post-fusion. Les CI GitHub n'attestent pas à elles seules que Cloudflare a publié le dernier SHA ; vérifier Pages et HTTP pour l'état réel.
