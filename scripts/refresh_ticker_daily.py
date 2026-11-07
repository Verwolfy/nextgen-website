#!/usr/bin/env python3
"""Daily official FX quotations for NextGen, without unverified editorial invention.

Runs in GitHub Actions only. Never contacts third parties from visitor browsers.
"""
from __future__ import annotations
import argparse
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import sys

import requests

ROOT = Path(__file__).resolve().parents[1]
TICKER = ROOT / "src/data/nextgen-ticker.ts"
BANK_URL = "https://www.bank-of-algeria.dz/taux-de-change-journalier/"
DAY = re.compile(r"(?<!\d)(\d{4}[-/]\d{2}[-/]\d{2}|\d{2}[-/]\d{2}[-/]\d{4})(?!\d)")
RATE = re.compile(r"^\s*\d{2,3}[,.]\d{2,5}\s*$")
CURRENCY = re.compile(r"^(USD|EUR)$", flags=re.IGNORECASE)


class RatesTableParser(HTMLParser):
    """Read table cells with stdlib, excluding script and style text."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tables: list[list[list[str]]] = []
        self.active: list[list[str]] | None = None
        self.row: list[str] | None = None
        self.cell: list[str] | None = None
        self.ignore = 0
        self.visible_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in ("script", "style"):
            self.ignore += 1
            return
        if self.ignore:
            return
        if tag == "table":
            self.active = []
        elif tag == "tr" and self.active is not None:
            self.row = []
        elif tag in ("td", "th") and self.row is not None:
            self.cell = []

    def handle_data(self, data: str) -> None:
        if self.ignore or not data.strip():
            return
        self.visible_text.append(data)
        if self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag in ("script", "style"):
            self.ignore = max(0, self.ignore - 1)
            return
        if self.ignore:
            return
        if tag in ("td", "th") and self.cell is not None and self.row is not None:
            self.row.append(" ".join(" ".join(self.cell).split()))
            self.cell = None
        elif tag == "tr" and self.row is not None and self.active is not None:
            if self.row:
                self.active.append(self.row)
            self.row = None
        elif tag == "table" and self.active is not None:
            self.tables.append(self.active)
            self.active = None


def parse_date(value: str) -> date | None:
    m = DAY.search(value)
    if not m:
        return None
    token = m.group(1).replace("/", "-")
    try:
        if len(token) == 10 and token[4] == "-":
            return date.fromisoformat(token)
        return datetime.strptime(token, "%d-%m-%Y").date()
    except ValueError:
        return None


def parse_amount(value: str) -> Decimal | None:
    candidate = value.replace("\u00a0", "").strip()
    if not RATE.fullmatch(candidate):
        return None
    try:
        amount = Decimal(candidate.replace(",", "."))
    except InvalidOperation:
        return None
    return amount if Decimal("50") < amount < Decimal("300") else None


def extract_bank_rates(html: str, today: date) -> tuple[date, dict[str, Decimal]]:
    parser = RatesTableParser()
    parser.feed(html)
    options: list[tuple[date, dict[str, Decimal]]] = []
    for table in parser.tables:
        currency_rows: dict[str, list[str]] = {}
        dates: list[date] = []
        for row in table:
            if not row:
                continue
            code = row[0].strip().upper()
            if CURRENCY.fullmatch(code):
                currency_rows[code] = row[1:]
            else:
                in_row = [d for cell in row for d in [parse_date(cell)] if d]
                if in_row and not dates:
                    dates = in_row
        if not dates or not all(k in currency_rows for k in ("EUR", "USD")):
            continue
        for idx, dt in enumerate(dates):
            if not date(2025, 1, 1) <= dt <= today:
                continue
            vals = {
                code: parse_amount(cells[idx]) if idx < len(cells) else None
                for code, cells in currency_rows.items()
            }
            if vals.get("EUR") is not None and vals.get("USD") is not None:
                options.append((dt, {"EUR": vals["EUR"], "USD": vals["USD"]}))
    if not options:
        # Official template fallback: only adjacent date / distinct ISO currencies.
        visible = " ".join(parser.visible_text)
        dates = [d for m in DAY.finditer(visible) for d in [parse_date(m.group(1))] if d and d <= today]
        if dates:
            latest = max(dates)
            pair: dict[str, Decimal] = {}
            for code in ("EUR", "USD"):
                matches = re.findall(
                    rf"(?<![A-Za-z]){code}\s+(\d{{2,3}}[.,]\d{{2,5}})(?!\d)",
                    visible, flags=re.IGNORECASE)
                if matches:
                    amount = parse_amount(matches[0])
                    if amount is not None:
                        pair[code] = amount
            if len(pair) == 2:
                options.append((latest, pair))
    if not options:
        raise ValueError("No unambiguous dated USD/EUR quotation found on official page")
    dt, rates = max(options, key=lambda result: result[0])
    if (today - dt).days > 5:
        raise ValueError(f"Official rates too old: {dt.isoformat()} (today {today.isoformat()})")
    if not (rates["EUR"] > rates["USD"]):
        raise ValueError("Unusual EUR/USD ordering; publication blocked")
    return dt, rates


def _rate_copy(code: str, amount: Decimal, published: date) -> dict[str, str]:
    display = f"{amount:.4f}"
    stamp = published.strftime("%d/%m")
    day_label = published.strftime("%d %b")
    foreign = display.replace(".", ",")
    ar_currency = "يورو/دينار" if code == "EUR" else "دولار/دينار"
    return {
        "fr": f"{code}/DZD : {foreign} DA, cotation officielle du {stamp}",
        "ar": f"{ar_currency}: {display} دج، السعر الرسمي {stamp}",
        "en": f"{code}/DZD: {display} DZD, official quotation {day_label}",
    }


def rewrite_rate_record(content: str, code: str, rate: Decimal, published: date) -> str:
    ident = "eur-dzd" if code == "EUR" else "usd-dzd"
    start = published.isoformat()
    expiry = (published + timedelta(days=7)).isoformat()
    copy = _rate_copy(code, rate, published)
    regex = re.compile(
        rf"(?P<full>\{{\s*id:'{re.escape(ident)}',category:'economy',published:'[^']+',expires:'[^']+',source:'Banque d’Algérie',"
        rf"\s*sourceUrl:'https://www\.bank-of-algeria\.dz/taux-de-change-journalier/',\s*text:\{{fr:'[^']*',ar:'[^']*',en:'[^']*'\}},\s*\}})",
        flags=re.MULTILINE)
    replacement = (
        "{\n"
        f"    id:'{ident}',category:'economy',published:'{start}',expires:'{expiry}',source:'Banque d’Algérie',\n"
        "    sourceUrl:'https://www.bank-of-algeria.dz/taux-de-change-journalier/',\n"
        f"    text:{{fr:'{copy['fr']}',ar:'{copy['ar']}',en:'{copy['en']}'}},\n"
        "  }")
    updated, count = regex.subn(lambda _: replacement, content)
    if count != 1:
        raise ValueError(f"Expected exactly one editorial record {ident}, got {count}")
    return updated


def current_bank_publication(content: str) -> date:
    dates = re.findall(r"id:'(?:eur|usd)-dzd',category:'economy',published:'(\d{4}-\d{2}-\d{2})'", content)
    if len(dates) != 2 or dates[0] != dates[1]:
        raise ValueError("Currency records missing or have inconsistent dates")
    return date.fromisoformat(dates[0])


def expiring_editorial_items(content: str, today: date, horizon: int = 7) -> list[dict[str, str]]:
    result = []
    regex = re.compile(r"id:'([^']+)',category:'(btph|innovation)',published:'(\d{4}-\d{2}-\d{2})',expires:'(\d{4}-\d{2}-\d{2})'")
    for ident, category, published, expiry in regex.findall(content):
        d = date.fromisoformat(expiry)
        if d <= today + timedelta(days=horizon):
            result.append({"id": ident, "category": category, "published": published,
                           "expires": expiry, "remaining_days": str((d - today).days)})
    return result


def run(args: argparse.Namespace) -> int:
    today = date.fromisoformat(args.today) if args.today else datetime.now(timezone.utc).date()
    current = TICKER.read_text(encoding="utf-8")
    report: dict = {
        "checked_at_utc": today.isoformat(), "official_source": BANK_URL,
        "status": "no_update", "editorial_expiring": expiring_editorial_items(current, today),
        "previous_official_date": current_bank_publication(current).isoformat(),
    }
    if args.fixture:
        html = Path(args.fixture).read_text(encoding="utf-8")
    else:
        try:
            response = requests.get(
                BANK_URL, timeout=20,
                headers={"User-Agent": "NextGenEditorialCheck/1.0 (+github.com/Verwolfy/nextgen-website)"})
            response.raise_for_status()
            if response.url.rstrip("/") != BANK_URL.rstrip("/"):
                raise ValueError("Unexpected redirect away from official quotation page")
            html = response.text
        except (requests.RequestException, ValueError) as exc:
            report.update(status="source_unavailable", reason=f"{type(exc).__name__}: {str(exc)[:160]}")
            print(f"::warning::Official exchange rate source unavailable: {report['reason']}")
            return finish(report, args.report)
    try:
        rate_date, rates = extract_bank_rates(html, today)
        if rate_date < current_bank_publication(current):
            raise ValueError("Official data older than published values; avoiding rollback")
        changed = current
        for code in ("EUR", "USD"):
            changed = rewrite_rate_record(changed, code, rates[code], rate_date)
        categories = re.findall(r"category:'(btph|economy|innovation)'", changed)
        if (categories.count("btph"), categories.count("economy"), categories.count("innovation")) != (5, 2, 1):
            raise ValueError("News editorial quota changed unexpectedly")
        report.update(status="updated" if changed != current else "unchanged",
                      official_date=rate_date.isoformat(),
                      official_rates={code: format(val, ".4f") for code, val in rates.items()})
        if not args.dry_run and changed != current:
            TICKER.write_text(changed, encoding="utf-8")
    except (ValueError, InvalidOperation) as exc:
        report.update(status="validation_rejected", reason=f"{type(exc).__name__}: {str(exc)[:170]}")
        print(f"::warning::Official exchange rate not published: {report['reason']}")
    return finish(report, args.report)


def finish(report: dict, path: str | None) -> int:
    message = json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2)
    print(message)
    if path:
        output = Path(path)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(message + "\n", encoding="utf-8")
    return 0 if report["status"] != "validation_rejected" else 2


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--report", help="Private audit JSON path")
    p.add_argument("--fixture", help="Offline HTML for integration testing")
    p.add_argument("--today", help="UTC ISO date override for deterministic tests")
    p.add_argument("--dry-run", action="store_true", help="Do not modify ticker source")
    return run(p.parse_args())


if __name__ == "__main__":
    sys.exit(main())
