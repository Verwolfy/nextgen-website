#!/usr/bin/env python3
"""Generate INTERNAL, print-ready FENEK TDS and SDS layout specimens.

Examples:
  python scripts/render_fenek_document_skeleton.py --sku BOND-C1T --out /tmp/fenek-specimens
  chromium --headless --no-sandbox --print-to-pdf=/tmp/example.pdf file:///tmp/fenek-specimens/FT_FR.html

No product-specific performance, hazard classification or FDS is issued.
Outputs are deliberately outside the Astro public/ directory.
"""
import argparse
import base64
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SDS_SECTIONS = {
    "fr": ["Identification du produit et de l'entreprise", "Identification des dangers",
           "Composition/informations sur les composants", "Premiers secours",
           "Mesures de lutte contre l'incendie", "Mesures en cas de dispersion accidentelle",
           "Manipulation et stockage", "Contrôles de l'exposition/protection individuelle",
           "Propriétés physiques et chimiques", "Stabilité et réactivité",
           "Informations toxicologiques", "Informations écologiques",
           "Considérations relatives à l'élimination", "Informations relatives au transport",
           "Informations réglementaires", "Autres informations"],
    "ar": ["تعريف المنتج والمورّد", "تحديد المخاطر", "التركيب والمعلومات عن المكونات",
           "الإسعافات الأولية", "مكافحة الحرائق", "التعامل مع الانسكابات العرضية",
           "المناولة والتخزين", "التحكم بالتعرض والحماية الشخصية",
           "الخصائص الفيزيائية والكيميائية", "الثبات والتفاعلية",
           "المعلومات السمية", "المعلومات البيئية",
           "التخلص من النفايات", "معلومات النقل", "المعلومات التنظيمية", "معلومات أخرى"],
    "en": ["Identification of the product and supplier", "Hazards identification",
           "Composition/information on ingredients", "First-aid measures",
           "Fire-fighting measures", "Accidental release measures",
           "Handling and storage", "Exposure controls/personal protection",
           "Physical and chemical properties", "Stability and reactivity",
           "Toxicological information", "Ecological information",
           "Disposal considerations", "Transport information",
           "Regulatory information", "Other information"],
}
COPY = {
    "fr": {
        "company": "NEXT GENERATION BUILDING SOLUTIONS",
        "ft": "FICHE TECHNIQUE", "fds": "FICHE DE DONNÉES DE SÉCURITÉ",
        "status": "MODÈLE DE PRÉSENTATION — NON ÉMIS / NON VALIDÉ",
        "reference": "Référence", "range": "Gamme", "revision": "Révision",
        "kind": "Nature du produit", "applications": "Domaines d'application",
        "technical": "Caractéristiques à vérifier", "conditions": "Conditions de mise en œuvre",
        "consumption": "Consommation et conditionnements", "safety": "Sécurité et traçabilité",
        "value": "Données du produit", "test": "Essais et rapports NextGen nécessaires",
        "procedure": "Méthode propre à cette formulation à valider",
        "quantity": "Consommation et dosages à établir par essais",
        "pack": "Formats du catalogue, à confirmer", "source": "Source",
        "source_value": "Description éditoriale FENEK uniquement",
        "hse": "Composition, classification et FDS propres au produit à établir",
        "note": "Ce spécimen ne remplace pas une fiche technique validée ou une FDS.",
        "fds_field": "Données à compléter à partir de la formulation réelle et de l'évaluation HSE.",
    },
    "ar": {
        "company": "حلول البناء للجيل القادم",
        "ft": "النشرة الفنية", "fds": "صحيفة بيانات السلامة",
        "status": "نموذج تنسيق — غير صادر وغير معتمد",
        "reference": "المرجع", "range": "المجموعة", "revision": "المراجعة",
        "kind": "نوع المنتج", "applications": "مجالات الاستخدام",
        "technical": "خصائص تتطلب التحقق", "conditions": "شروط التطبيق",
        "consumption": "الاستهلاك والعبوات", "safety": "السلامة والتتبع",
        "value": "بيانات المنتج", "test": "اختبارات وتقارير NextGen مطلوبة",
        "procedure": "طريقة خاصة بهذه التركيبة تحتاج إلى اعتماد",
        "quantity": "يحدد الاستهلاك والجرعات باختبارات خاصة",
        "pack": "عبوات الكتالوج المقترحة تحتاج إلى تأكيد", "source": "المصدر",
        "source_value": "الوصف التعريفي في كتالوج FENEK فقط",
        "hse": "يجب تحديد التركيب والتصنيف وصحيفة السلامة الخاصة بالمنتج",
        "note": "هذا النموذج لا يحل محل نشرة فنية معتمدة أو صحيفة بيانات سلامة.",
        "fds_field": "تستكمل البيانات بناءً على التركيبة الفعلية وتقييم السلامة المختص.",
    },
    "en": {
        "company": "NEXT GENERATION BUILDING SOLUTIONS",
        "ft": "TECHNICAL DATA SHEET", "fds": "SAFETY DATA SHEET",
        "status": "LAYOUT SPECIMEN — NOT ISSUED / NOT APPROVED",
        "reference": "Reference", "range": "Product range", "revision": "Revision",
        "kind": "Product type", "applications": "Application areas",
        "technical": "Technical properties to verify", "conditions": "Application conditions",
        "consumption": "Consumption and packaging", "safety": "Safety and traceability",
        "value": "Product information", "test": "NextGen test evidence required",
        "procedure": "Procedure to be validated for this formulation",
        "quantity": "Dosage and coverage to be established by product tests",
        "pack": "Proposed catalogue formats, subject to confirmation", "source": "Source",
        "source_value": "FENEK editorial catalogue description only",
        "hse": "Actual composition, classification and product SDS to be established",
        "note": "This specimen does not replace an approved technical data sheet or SDS.",
        "fds_field": "To be completed from actual formulation and product-specific HSE evaluation.",
    },
}
STYLE = """
@page {size:A4;margin:15mm 15mm 19mm}
@page {@bottom-right{content:"Page " counter(page) " / " counter(pages);
    font:8pt sans-serif;color:#6a8198}}
*{box-sizing:border-box}
body{font:10pt/1.5 "DejaVu Sans",sans-serif;color:#15324f}
body[dir="rtl"]{font-family:"Amiri","DejaVu Sans",serif;line-height:1.7}
.header{display:flex;gap:22px;align-items:center;min-height:90px}
.logo{width:126px;max-height:90px;object-fit:contain}
.vertical{height:65px;border-inline-start:2px solid #0c315a}
.brand{font-size:15pt;line-height:1.25;font-weight:800;color:#082b4c;flex:1}
.slants{width:50px;height:78px;transform:skew(-28deg);
    background:linear-gradient(to right,#0b3159 0 47%,white 47% 63%,#07965b 63%)}
.rule{height:4px;background:linear-gradient(to right,#10385d 0 44%,white 44% 47%,#078e5b 47% 60%,white 60% 63%,#10385d 63%)}
.hero{text-align:center;padding:22px 0 15px}
.hero h1{display:inline-block;margin:0;padding:8px 25px;background:#0d335a;
    color:white;font-size:20pt;letter-spacing:.025em;transform:skew(-11deg)}
.hero h1 span{display:inline-block;transform:skew(11deg)}
.issue{text-align:center;font-size:8pt;color:#647d8e;padding:4px 0 14px}
.meta{display:grid;grid-template-columns:1fr 1fr;gap:7px 15px;margin:0 0 20px}
.meta div{background:#eef2f5;padding:7px 10px;border-radius:5px}
.meta b{display:inline-block;width:90px;color:#102b49}
.title{background:#0d365d;color:white;font-weight:750;padding:7px 11px;margin:16px 0 0;break-after:avoid}
.table{width:100%;border-collapse:collapse;table-layout:fixed;margin:0 0 6px}
.table td{padding:8px 11px;border:1px solid #d0dce5;vertical-align:top;overflow-wrap:anywhere}
.table tr:nth-child(even){background:#edf2f5}
.table td:first-child{width:35%;font-weight:bold}
.note{background:#eff4f7;border-inline-start:3px solid #07975c;margin:17px 0;
    padding:9px 11px;font-size:8.8pt;color:#50697b}
.sdssec{break-inside:avoid;margin:9px 0}
.sdssec h2{font-size:9.5pt;background:#0e385d;color:white;
    margin:0;padding:7px 11px}
.sdssec p{border:1px solid #dbe3e8;margin:0;padding:7px 11px;font-size:9pt}
.footer{border-top:2px solid #10385b;padding:10px 0;margin-top:20px;
    font-size:8.5pt;color:#587083}
@media print {.sdssec,.title{break-inside:avoid}}
"""


def esc(value):
    return html.escape(str(value), quote=True)


def tr(title, rows):
    table = "".join("<tr><td>" + esc(k) + "</td><td>" + esc(v) + "</td></tr>"
                    for k, v in rows)
    return '<section><div class="title">' + esc(title) + \
           '</div><table class="table">' + table + "</table></section>"


def render(product, lang, kind, logo):
    text = COPY[lang]
    detail = product["contenu"][lang]
    formats = ", ".join(item["format"] for item in product["conditionnements"])
    title = text["ft"] if kind == "FT" else text["fds"]
    meta = [(text["reference"], product["nom"]),
            (text["revision"], "T0 / VISUAL"),
            (text["range"], product["gamme"].upper()),
            (text["value"], text["status"])]
    head = ('<div class="header"><img class="logo" src="' + logo +
            '"/><div class="vertical"></div><strong class="brand">' +
            esc(text["company"]) + '</strong><div class="slants"></div></div>' +
            '<div class="rule"></div><div class="hero"><h1><span>' +
            esc(title) + '</span></h1></div><div class="issue">' +
            esc(text["status"]) + '</div><div class="meta">' +
            "".join("<div><b>" + esc(k) + "</b>" + esc(v) + "</div>"
                    for k, v in meta) + '</div>')
    if kind == "FT":
        body = tr(text["kind"], [(text["reference"], product["nom"]),
                                 (text["kind"], detail["accroche"]),
                                 (text["applications"], "; ".join(detail["usages"]))])
        body += tr(text["technical"], [(text["value"], text["test"])])
        body += tr(text["conditions"], [(text["value"], text["procedure"])])
        body += tr(text["consumption"], [(text["value"], text["quantity"]),
                                        (text["pack"], formats or text["pack"])])
        body += tr(text["safety"], [(text["value"], text["hse"]),
                                   (text["source"], text["source_value"])])
    else:
        body = "".join('<section class="sdssec"><h2>' + str(i).zfill(2) +
                       " · " + esc(name) + '</h2><p>' + esc(text["fds_field"]) +
                       '</p></section>'
                       for i, name in enumerate(SDS_SECTIONS[lang], 1))
    body += '<div class="note">' + esc(text["note"]) + '</div>'
    body += '<div class="footer">NEXTGEN  ·  ' + \
            'contact@nextgen-buildingsolutions.com</div>'
    return ('<!doctype html><html lang="' + lang + '"><head><meta charset="utf-8"/>' +
            '<title>' + esc(product["nom"] + " - " + title) +
            '</title><style>' + STYLE + '</style></head><body dir="' +
            ('rtl' if lang == 'ar' else 'ltr') + '">' + head + body +
            '</body></html>')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    parser.add_argument("--sku", default="BOND-C1T")
    args = parser.parse_args()
    output = Path(args.out).resolve()
    forbidden = [ROOT / "public", ROOT / "dist", ROOT / "src"]
    if any(output == x or x in output.parents for x in forbidden):
        parser.error("Refusing to generate unapproved documents in a public source folder")
    output.mkdir(parents=True, exist_ok=True)
    products = json.loads((ROOT / "src/data/catalogue-projets.json").read_text(encoding="utf-8"))
    product = next((p for p in products if p["code"] == args.sku), None)
    if product is None:
        parser.error("Unknown SKU " + args.sku)
    if product["certifie"] or product["commercialise"]:
        parser.error("Catalogue status changed: review the release rules before generation")
    logo_file = ROOT / "supports/assets/Logo1.jpg"
    logo = "data:image/jpeg;base64," + base64.b64encode(logo_file.read_bytes()).decode("ascii")
    for lang in ("fr", "ar", "en"):
        for kind in ("FT", "FDS"):
            target = output / (kind + "_" + lang.upper() + ".html")
            target.write_text(render(product, lang, kind, logo), encoding="utf-8")
            print(target)


if __name__ == "__main__":
    main()
