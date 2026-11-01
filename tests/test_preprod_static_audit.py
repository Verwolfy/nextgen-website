"""Offline structural tests for NextGen Pages preview preflight."""
from pathlib import Path
import importlib.util
import pytest

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/"scripts"/"preprod_static_audit.py"
SPEC=importlib.util.spec_from_file_location("preprod_audit",PATH)
M=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)

def test_headers_require_noindex(tmp_path):
    p=tmp_path/"_headers"
    p.write_text("/*\n  X-Robots-Tag: noindex, nofollow, noarchive\n")
    with pytest.raises(AssertionError):
        M.inspect_headers(p)

def test_headers_accept_exact_policy(tmp_path):
    p=tmp_path/"_headers"
    p.write_text("/*\n"+"".join(f"  {k}: {v}\n" for k,v in M.EXPECTED_HEADERS.items()))
    M.inspect_headers(p)

def test_any_unsafe_page_is_refused(tmp_path):
    p=tmp_path/"index.html"
    p.write_text('<html lang="ar" dir="ltr"><meta name="robots" content="noindex"><form></form></html>')
    with pytest.raises(AssertionError):
        M.inspect_page(p,"ar")

def test_generated_form_is_blocked(tmp_path):
    p=tmp_path/"index.html"
    p.write_text('<html lang="fr" dir="ltr"><meta name="robots" content="noindex"><form></form></html>')
    with pytest.raises(AssertionError):
        M.inspect_page(p,"fr")

def test_safe_localized_page(tmp_path):
    p=tmp_path/"index.html"
    p.write_text('<html lang="en" dir="ltr"><meta name="robots" content="noindex"></html>')
    M.inspect_page(p,"en")
