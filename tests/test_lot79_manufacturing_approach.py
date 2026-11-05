"""Lot 79: manufacturer-first NextGen approach in FR/AR/EN, illustrated safely."""
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class ManufacturingApproach(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.editorial=(ROOT/"src/data/editorial.ts").read_text(encoding="utf-8")
        cls.about=(ROOT/"src/components/AboutStory.astro").read_text(encoding="utf-8")

    def test_three_production_oriented_stages_in_all_languages(self):
        for stage in (
            "Concevoir pour le terrain","Produire avec méthode","Distribuer et accompagner",
            "تصميم حلول للميدان","تصنيع بمنهجية واضحة","التوزيع والمرافقة",
            "Design for the jobsite","Manufacture with purpose","Distribute and support",
        ):
            self.assertIn(stage,self.editorial)
        self.assertIn("aboutHighlights",self.editorial)
        self.assertIn("aboutCta",self.editorial)
        self.assertIn("aboutKicker",self.editorial)

    def test_images_are_local_vector_illustrations_not_external_loads(self):
        for number,slug in enumerate(("concevoir","produire","distribuer"),1):
            relative=f"images/approche/{number:02d}-{slug}.svg"
            self.assertIn("/"+relative,self.about)
            data=(ROOT/"public"/relative).read_text(encoding="utf-8")
            self.assertIn("<svg",data)
            self.assertIn("viewBox",data)
            for unsafe in ("<script","<foreignObject","onload=","http://www.w3.org/1999/xlink","<image"):
                self.assertNotIn(unsafe,data)
        self.assertIn('aria-labelledby="industrial-approach-heading"',self.about)
        self.assertIn("prefers-reduced-motion",self.about)

    def test_provisional_products_never_gain_unearned_certifications(self):
        for unsupported in (
            "formulé et contrôlé par notre laboratoire",
            "formulated and tested by our laboratory",
            "بطاقات تقنية مصادق عليها",
            "Validated data sheets",
        ):
            self.assertNotIn(unsupported,self.editorial)
        for required in ("validations requises","الموافقات اللازمة","required approvals"):
            self.assertIn(required,self.editorial)
        self.assertIn("edit.aboutNotice",self.about)
        self.assertIn("href={'/'+lang+'/contact/'}",self.about)
        self.assertNotIn("https://fonts.googleapis.com",self.about)

if __name__=="__main__":
    unittest.main()
