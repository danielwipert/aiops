#!/usr/bin/env python3
"""
Build the manifesto PDF from the source docx, styled to match the site
(warm ivory, Besley / Source Serif 4 / Archivo, claret accents).

Usage:  python tools/build_manifesto_pdf.py
Output: AI-Operations-Management.pdf at the repo root.

Requires: python-docx, and Google Chrome (for the print engine).
Regenerate this whenever the source docx changes.
"""
import os, re, html, tempfile, subprocess, sys
import docx

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCX = os.path.join(REPO, "planning", "AI Operations Management 7.10.2026.docx")
OUT  = os.path.join(REPO, "AI-Operations-Management.pdf")
CHROME_CANDIDATES = [
    r"C:/Program Files/Google/Chrome/Application/chrome.exe",
    r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
    r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
]

CSS = """
:root{--paper:#F7F0E4;--ink:#201A12;--ink-soft:#6B6152;--claret:#8E1D33;--claret-900:#4E0E18;--line:#D9CCB4;
--display:'Besley',Georgia,serif;--serif:'Source Serif 4',Georgia,serif;--sans:'Archivo','Segoe UI',sans-serif;}
@page{size:letter;margin:0.9in 1.15in;}
*{box-sizing:border-box;margin:0;padding:0;}
html{background:#F7F0E4;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{background:#F7F0E4;color:var(--ink);font-family:var(--serif);font-size:11.5pt;line-height:1.62;
-webkit-print-color-adjust:exact;print-color-adjust:exact;text-rendering:optimizeLegibility;}
.title-page{min-height:8.1in;display:flex;flex-direction:column;justify-content:center;break-after:page;}
.eyebrow{font-family:var(--sans);font-size:9pt;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--claret-900);}
.title-rule{width:46pt;height:3px;background:var(--claret);margin-bottom:20pt;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
.title{font-family:var(--display);font-weight:800;font-size:41pt;line-height:1.0;letter-spacing:-.025em;margin:14pt 0 10pt;}
.subtitle{font-family:var(--display);font-style:italic;font-weight:400;font-size:20pt;letter-spacing:-.01em;color:var(--claret);}
.byline{font-family:var(--sans);font-size:10.5pt;letter-spacing:.02em;color:var(--ink-soft);margin-top:30pt;}
.byline strong{color:var(--ink);font-weight:700;}
section+section{margin-top:22pt;}
.sec-head{break-after:avoid;break-inside:avoid;margin-bottom:12pt;padding-top:14pt;border-top:1px solid var(--line);}
.sec-num{font-family:var(--sans);font-size:8.5pt;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--claret-900);}
h2{font-family:var(--display);font-weight:600;font-size:21pt;line-height:1.14;letter-spacing:-.01em;margin-top:5pt;}
p{margin-bottom:9pt;orphans:2;widows:2;}
.thesis{font-style:italic;color:var(--claret-900);font-weight:600;}
.closer{font-family:var(--display);font-size:16pt;font-weight:600;line-height:1.25;letter-spacing:-.01em;margin-top:12pt;color:var(--claret-900);}
.method{margin-top:20pt;padding-top:14pt;border-top:1px solid var(--line);font-style:italic;font-size:10pt;color:var(--ink-soft);}
"""

def esc(t): return html.escape(t, quote=False)

def build_html():
    d = docx.Document(DOCX)
    paras = d.paragraphs
    title, subtitle = paras[0].text.strip(), paras[1].text.strip()
    body, open_sec = [], False
    for p in paras[3:]:
        style = p.style.name if p.style else ""
        t = p.text.strip()
        if not t:
            continue
        if style == "Heading 1":
            m = re.match(r"^(\d+)\.\s+(.*)$", t)
            num = m.group(1).zfill(2) if m else ""
            htext = m.group(2) if m else t
            if open_sec:
                body.append("</section>")
            body.append("<section>"); open_sec = True
            body.append(f'<div class="sec-head"><p class="sec-num">{num}</p><h2>{esc(htext)}</h2></div>')
        else:
            para = esc(t).replace("Cost accrues by default; value accrues by design.",
                                  '<em class="thesis">Cost accrues by default; value accrues by design.</em>')
            if t.startswith("AI Operations Management. The discipline of the flow"):
                body.append(f'<p class="closer">{para}</p>')
            elif t.startswith("A note on method"):
                body.append(f'<p class="method">{para}</p>')
            else:
                body.append(f"<p>{para}</p>")
    if open_sec:
        body.append("</section>")
    fonts = ("https://fonts.googleapis.com/css2?family=Besley:ital,wght@0,400;0,600;0,800;1,400"
             "&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400"
             "&family=Archivo:wght@400;600;700&display=swap")
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>AI Operations Management</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts}" rel="stylesheet"><style>{CSS}</style></head><body>
<div class="title-page"><div class="title-rule"></div>
<p class="eyebrow">The founding argument &middot; 2026</p>
<h1 class="title">{esc(title)}</h1>
<p class="subtitle">{esc(subtitle)}</p>
<p class="byline"><strong>Daniel S. Wipert</strong><br>On the economics of business AI adoption</p></div>
{chr(10).join(body)}
</body></html>"""

def main():
    chrome = next((c for c in CHROME_CANDIDATES if os.path.exists(c)), None)
    if not chrome:
        sys.exit("Chrome/Edge not found; edit CHROME_CANDIDATES.")
    html_doc = build_html()
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html_doc); tmp = f.name
    try:
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        "--virtual-time-budget=8000", f"--print-to-pdf={OUT}",
                        "file:///" + tmp.replace("\\", "/")], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    finally:
        os.unlink(tmp)
    print("Wrote", OUT)

if __name__ == "__main__":
    main()
