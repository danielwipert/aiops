#!/usr/bin/env python3
"""
Shared PDF print helper for the AIOM build scripts.

print_pdf(html, out, footer) renders HTML to a full-bleed PDF using the local
Chrome print engine (root-background propagation gives edge-to-edge color), then
stamps a centered footer onto every page with PyMuPDF. This two-step approach is
deliberate: Chrome cannot produce BOTH a full-bleed background AND a live
per-page footer (displayHeaderFooter suppresses the background bleed, and
position:fixed only paints page 1 under --headless=new), so the footer is added
afterward.

Requires: Google Chrome (print engine) and PyMuPDF (fitz).
"""
import os, sys, tempfile, subprocess
import fitz

CHROME_CANDIDATES = [
    r"C:/Program Files/Google/Chrome/Application/chrome.exe",
    r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
    r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
]
FOOTER_SIZE = 7.2
FOOTER_COLOR = (0.42, 0.38, 0.32)   # ink-soft #6B6152
FOOTER_UP_FROM_BOTTOM = 34          # points from the page's bottom edge


def _chrome():
    c = next((c for c in CHROME_CANDIDATES if os.path.exists(c)), None)
    if not c:
        sys.exit("Chrome/Edge not found; edit CHROME_CANDIDATES in tools/pdf_common.py.")
    return c


def _stamp_footer(path, text):
    # Base-14 Helvetica has no em dash; use a hyphen for the stamped copy.
    text = text.replace("—", "-")
    doc = fitz.open(path)
    try:
        for page in doc:
            r = page.rect
            tw = fitz.get_text_length(text, fontname="helv", fontsize=FOOTER_SIZE)
            x = (r.width - tw) / 2
            y = r.height - FOOTER_UP_FROM_BOTTOM
            page.insert_text((x, y), text, fontname="helv",
                             fontsize=FOOTER_SIZE, color=FOOTER_COLOR)
        doc.save(path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    finally:
        doc.close()


def print_pdf(html_doc, out_path, footer_text=None):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html_doc)
        tmp = f.name
    try:
        subprocess.run([_chrome(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        "--virtual-time-budget=12000", f"--print-to-pdf={out_path}",
                        "file:///" + tmp.replace("\\", "/")], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    finally:
        os.unlink(tmp)
    if footer_text:
        _stamp_footer(out_path, footer_text)
    print("Wrote", out_path)
