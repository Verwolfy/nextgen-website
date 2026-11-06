# Lot 109 — Bouton de pause affecté au fil d'actualités, 6 novembre 2026

## Demande et résultat
L'utilisateur demande que le bouton rond sous la vidéo mette en pause/reprenne le bandeau des actualités au lieu du film Nexo/Geno.

## Détails
- FR/AR/EN : aria-label contextualisés, icônes Ⅱ / ▶ et aria-pressed synchronisés.
- Le bouton commande uniquement le `animation-play-state` de la piste des nouvelles.
- Le film original continue de fonctionner indépendamment : silencieux, lazy-load, pause automatique hors viewport/onglet masqué, pas d'autoplay en Data Saver ou reduced motion ; le bouton du ticker n'active plus manuellement la vidéo.
- Pause au survol et au focus conservée ; mode reduced motion : aucune animation du ticker et bouton masqué car sans utilité.
- Si aucune actualité datée n'est active, bouton masqué.
- Les informations restent non cliquables, les dates et sources inchangées, mouvement arabe de gauche à droite préservé.

## Contrôle
Unités régressions + Playwright sur mobile FR/AR/EN, mode reduced motion, Data Saver, contrôle état `aria-pressed`, bouton ne déclenchant pas la vidéo ; build sécurité, Chromium et Lighthouse avant fusion.

## Règles
Noindex, Cloudflare Access, DNS, formulaires inactifs, produits provisoires, vidéo originale et PR draft #50 inchangés. Vérifier le commit de publication Cloudflare après la fusion.
