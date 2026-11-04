"""Lot 60 — controles de langue et theme: apparence, persistence, RTL, no-js."""
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class PreferencesTests(unittest.TestCase):
    def test_layout_includes_one_shared_control_and_prepaint_init(self):
        layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf8")
        self.assertIn("import '../styles/theme.css';",layout)
        self.assertIn("<ColorSchemeInit />",layout)
        self.assertIn("<HeaderPreferences lang={lang} suffix={suffix} languageLabel={t.languageLabel} />",layout)
        self.assertNotIn('<div class="locale"',layout)
        self.assertIn("hreflang",layout)
        self.assertIn("noindex,nofollow",layout)

    def test_language_picker_has_native_fallback_and_correct_labels(self):
        source=(ROOT/"src/components/HeaderPreferences.astro").read_text(encoding="utf8")
        for token in (
            '<details class="language-choice"', "<summary aria-label={languageLabel}",
            "languages.map(", "aria-current={l===lang?'page':undefined}",
            "Français", "العربية", "English", "dir=\"auto\"",
            "data-language-choice", "event.key==='Escape'",
        ):
            self.assertIn(token,source,token)
        self.assertNotIn("window.location=",source)

    def test_switch_has_early_state_and_safe_local_storage(self):
        init=(ROOT/"src/components/ColorSchemeInit.astro").read_text(encoding="utf8")
        control=(ROOT/"src/components/HeaderPreferences.astro").read_text(encoding="utf8")
        for expected in ("is:inline","localStorage.getItem('nextgen-color-theme')","prefers-color-scheme: dark","root.dataset.theme","root.style.colorScheme"):
            self.assertIn(expected,init,expected)
        for expected in ('role="switch"','aria-checked="false"',"localStorage.setItem(themeKey,next)","query.addEventListener('change'","setAttribute('aria-checked'"):
            self.assertIn(expected,control,expected)

    def test_night_palette_covers_content_but_print_remains_white(self):
        css=(ROOT/"src/styles/theme.css").read_text(encoding="utf8")
        for selector in ('.header-preferences','.theme-switch','.language-choice-options',
                         ':root[data-theme="dark"] .header',':root[data-theme="dark"] .card',
                         ':root[data-theme="dark"] .catalogue-filters',
                         ':root[data-theme="dark"] .concept-product-card',
                         ':root[data-theme="dark"] .fenek-product-page',
                         ':root[data-theme="dark"] .fenek-doc-accordion',
                         ':root[data-theme="dark"] .lead-field input',
                         '@media print','prefers-reduced-motion:reduce','max-width:380px'):
            self.assertIn(selector,css,selector)
        self.assertIn("print-color-adjust:exact",css)
        self.assertNotIn("filter:invert",css)
        self.assertNotIn("https://",css)

if __name__=="__main__":
    unittest.main()
