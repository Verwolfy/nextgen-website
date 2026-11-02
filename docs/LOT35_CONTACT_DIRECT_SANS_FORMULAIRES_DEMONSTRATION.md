# Lot 35 — Remplacer les formulaires de démonstration par des contacts directs

Date : 2026-11-02. Suite du nettoyage éditorial trilingue, issue #33.

## Diagnostic
Les pages publiques `/{fr|ar|en}/contact/` et `/{fr|ar|en}/distributeurs/` contiennent un volet « formulaire de démonstration — envoi désactivé », avec champs toujours désactivés. Cette interface peut être prise pour une fonctionnalité en panne ou une version de préproduction.

## Correction
- Le gabarit `src/pages/[lang]/[section].astro` n'affiche plus `LeadForm.astro` sur ces six pages.
- Chaque page conserve trois liens directement exploitables : courriel `mailto:`, WhatsApp `wa.me`, téléphone `tel:`. Aucun formulaire de collecte, aucun script de suivi et aucune transmission automatique aux bases de données ne sont ajoutés.
- Le lien « distributeur » pointe sur `#contact-direct` et le bouton redondant de formulaire a été retiré.
- Les composants internes désactivés demeurent archivés dans le dépôt, sans être compilés dans les pages publiques.

## Contrôles
- `scripts/check_built_pages.py` : absence des classes `lead-preview` et `lead-panel` et trois canaux par langue.
- `scripts/check_browser_pages.py` : desktop/mobile FR/AR/EN, liens externes présents et aucun formulaire ni champ caché.
- `tests/test_lot14_contact_journey.py`, `tests/test_editorial_hubs.py` : les routes publiques utilisent bien le contact direct, sans montages des formulaires.
- Les 150 fiches catalogue restent inchangées depuis le lot 34, ainsi que les rendus GLB/WebP, les données ERP/Supabase, les clés Cloudflare et les règles de noindex.

## Limites
Ces liens utilisent les coordonnées publiées par NextGen mais **ne prouvent pas que les messages sont reçus**, ni que le devis en ligne est disponible. Vérifier le fonctionnement du numéro/e-mail avec l'entreprise avant toute promesse de délai. Les mentions légales restent soumises à finalisation. Ne pas inventer une fonctionnalité de collecte active.
