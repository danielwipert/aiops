#!/usr/bin/env python3
"""
Build the AI Operations Specification PDF from the source docx, styled to match
the manifesto PDF (warm ivory, Besley / Source Serif 4 / Archivo, claret accents).
Faithful reproduction: Parts I-VII, appendices, all 57 normative requirements,
and every table. No content edits.

Usage:  python tools/build_spec_pdf.py
Output: AI-Operations-Specification-v1.pdf at the repo root.

Requires: python-docx, and Google Chrome (for the print engine).
"""
import os, html, tempfile, subprocess, sys
import docx
from docx.oxml.ns import qn
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCX = os.path.join(REPO, "planning", "AI_Operations_Specification_v1 (1) (1).docx")
OUT  = os.path.join(REPO, "AI-Operations-Specification-v1.pdf")
FOOTER = "AI Operations Specification v1.0 · Daniel S. Wipert"
PRINTER = os.path.join(REPO, "tools", "pdf", "html_to_pdf.js")

CSS = """
:root{--paper:#F7F0E4;--ink:#201A12;--ink-soft:#6B6152;--claret:#8E1D33;--claret-900:#4E0E18;--line:#D9CCB4;--line-strong:#C9B896;
--display:'Besley',Georgia,serif;--serif:'Source Serif 4',Georgia,serif;--sans:'Archivo','Segoe UI',sans-serif;}
@page{size:letter;margin:0;}
*{box-sizing:border-box;margin:0;padding:0;}
html{background:#F7F0E4;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{background:#F7F0E4;color:var(--ink);font-family:var(--serif);font-size:10.5pt;line-height:1.55;
-webkit-print-color-adjust:exact;print-color-adjust:exact;text-rendering:optimizeLegibility;}
.title-page{min-height:8.4in;display:flex;flex-direction:column;justify-content:center;break-after:page;}
.title-rule{width:46pt;height:3px;background:var(--claret);margin-bottom:20pt;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
.title{font-family:var(--display);font-weight:800;font-size:40pt;line-height:1.0;letter-spacing:-.025em;margin:14pt 0 12pt;text-transform:uppercase;}
.subtitle{font-family:var(--display);font-style:italic;font-weight:400;font-size:18pt;letter-spacing:-.01em;color:var(--claret);line-height:1.2;}
.byline{font-family:var(--sans);font-size:10.5pt;letter-spacing:.02em;color:var(--ink-soft);margin-top:30pt;}
.byline strong{color:var(--ink);font-weight:700;}
.byline .meta{font-size:9pt;margin-top:5pt;letter-spacing:.05em;}
h1{font-family:var(--display);font-weight:800;font-size:27pt;line-height:1.08;letter-spacing:-.02em;
break-before:page;break-after:avoid;margin-bottom:6pt;padding-bottom:8pt;border-bottom:2px solid var(--claret);color:var(--claret-900);}
h1.first{break-before:auto;}
h2{font-family:var(--display);font-weight:600;font-size:16.5pt;line-height:1.16;letter-spacing:-.01em;
break-after:avoid;margin:20pt 0 8pt;padding-top:10pt;border-top:1px solid var(--line);}
h3{font-family:var(--sans);font-weight:700;font-size:10.5pt;letter-spacing:.02em;
break-after:avoid;margin:14pt 0 5pt;color:var(--claret-900);}
p{margin-bottom:7.5pt;orphans:2;widows:2;}
strong{font-weight:700;}
ul{margin:0 0 9pt 0;padding-left:0;list-style:none;}
li{position:relative;padding-left:15pt;margin-bottom:4.5pt;break-inside:avoid;}
li::before{content:'';position:absolute;left:3pt;top:.62em;width:3.5pt;height:3.5pt;background:var(--claret);border-radius:50%;
-webkit-print-color-adjust:exact;print-color-adjust:exact;}
table{width:100%;border-collapse:collapse;margin:10pt 0 13pt;font-size:8.6pt;line-height:1.4;break-inside:auto;}
thead{display:table-header-group;}
th{background:var(--claret);color:#F7F0E4;font-family:var(--sans);font-weight:600;font-size:7.8pt;letter-spacing:.04em;
text-align:left;padding:5pt 7pt;vertical-align:top;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
td{border:1px solid var(--line-strong);padding:5pt 7pt;vertical-align:top;}
tr{break-inside:avoid;}
tbody tr:nth-child(even){background:#EFE6D4;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
"""

def esc(t): return html.escape(t, quote=False)

def iter_blocks(doc):
    body = doc.element.body
    for child in body.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, doc)
        elif isinstance(child, CT_Tbl):
            yield Table(child, doc)

def is_listed(p):
    try:
        return p._p.pPr is not None and p._p.pPr.numPr is not None
    except Exception:
        return False

def render_runs(p):
    out = []
    for r in p.runs:
        t = esc(r.text)
        if not t:
            continue
        if r.bold:
            t = "<strong>" + t + "</strong>"
        if r.italic:
            t = "<em>" + t + "</em>"
        out.append(t)
    return "".join(out) or esc(p.text)

def render_table(tb):
    rows = tb.rows
    out = ["<table>"]
    for ri, row in enumerate(rows):
        cells, prev = [], None
        for c in row.cells:
            txt = c.text.strip()
            if cells and txt == prev:   # collapse horizontally-merged repeats
                continue
            prev = txt
            cells.append(txt)
        tag = "th" if ri == 0 else "td"
        cellhtml = "".join(f"<{tag}>{esc(x).replace(chr(10),'<br>')}</{tag}>" for x in cells)
        if ri == 0:
            out.append(f"<thead><tr>{cellhtml}</tr></thead><tbody>")
        else:
            out.append(f"<tr>{cellhtml}</tr>")
    out.append("</tbody></table>")
    return "".join(out)

def build_html():
    d = docx.Document(DOCX)
    title = subtitle = author = date = ""
    body = []
    in_list = False
    first_h1_done = False

    def close_list():
        nonlocal in_list
        if in_list:
            body.append("</ul>")
            in_list = False

    for blk in iter_blocks(d):
        if isinstance(blk, Table):
            close_list()
            body.append(render_table(blk))
            continue
        p = blk
        style = p.style.name if p.style else ""
        t = p.text.strip()
        if not t:
            continue
        if style == "Title":
            title = t; continue
        if style == "Subtitle":
            subtitle = t; continue
        if style == "Author":
            author = t; continue
        if style == "Date":
            date = t; continue
        if style == "Heading 1":
            close_list()
            cls = "" if first_h1_done else ' class="first"'
            first_h1_done = True
            body.append(f"<h1{cls}>{esc(t)}</h1>")
        elif style == "Heading 2":
            close_list()
            body.append(f"<h2>{esc(t)}</h2>")
        elif style == "Heading 3":
            close_list()
            body.append(f"<h3>{esc(t)}</h3>")
        elif is_listed(p):
            if not in_list:
                body.append("<ul>"); in_list = True
            body.append(f"<li>{render_runs(p)}</li>")
        else:
            close_list()
            body.append(f"<p>{render_runs(p)}</p>")
    close_list()

    fonts = ("https://fonts.googleapis.com/css2?family=Besley:ital,wght@0,400;0,600;0,800;1,400"
             "&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400"
             "&family=Archivo:wght@400;600;700&display=swap")
    # Author name shown as the full formal byline (matches the docx source).
    author_disp = "Daniel S. Wipert"
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>AI Operations Specification v1.0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts}" rel="stylesheet"><style>{CSS}</style></head><body>
<div class="title-page"><div class="title-rule"></div>
<p class="byline" style="margin:0 0 4pt;letter-spacing:.2em;text-transform:uppercase;font-size:9pt;font-weight:600;color:#4E0E18;">Enterprise Standard</p>
<h1 class="title" style="border:none;color:var(--ink);padding:0;break-before:auto;">{esc(title)}</h1>
<p class="subtitle">{esc(subtitle)}</p>
<p class="byline"><strong>{esc(author_disp)}</strong><br><span class="meta">{esc(date)}</span></p></div>
{chr(10).join(body)}
</body></html>"""

def main():
    html_doc = build_html()
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html_doc); tmp = f.name
    try:
        subprocess.run(["node", PRINTER, tmp, OUT, FOOTER], check=True)
    finally:
        os.unlink(tmp)
    print("Wrote", OUT)

if __name__ == "__main__":
    main()
