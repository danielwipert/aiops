#!/usr/bin/env python3
"""
Build the "Head of AI Operations — Role Standard" PDF from the authored content
below, styled to match the manifesto / specification PDFs (warm ivory, Besley /
Source Serif 4 / Archivo, claret accents). Companion to the AI Operations
Specification v1.0; content is synthesized from the Specification (§17 The Role,
§16 The First 365 Days, §11 KPI Catalog, §13 Organization) in the discipline's
voice. Edit CONTENT below and re-run.

Usage:  python tools/build_role_standard_pdf.py
Output: Head-of-AI-Operations-Role-Standard.pdf at the repo root.

Requires: PyMuPDF and Google Chrome (for the print engine).
"""
import os, html
from pdf_common import print_pdf

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT  = os.path.join(REPO, "Head-of-AI-Operations-Role-Standard.pdf")
FOOTER = ("Head of AI Operations — Role Standard · "
          "Companion to the AI Operations Specification v1.0 · Daniel S. Wipert")

TITLE = "Head of AI Operations"
SUBTITLE = "The executive specification for the discipline's owner"

# Required reconciliation note (Specification §17 titles the role "Head";
# §17.5 / Section 17 also references "Director of AI Operations" by scale).
SCALE_NOTE = ("The title scales with organization size: Director of AI Operations in "
              "mid-size enterprises, Head or VP of AI Operations at scale.")

# Each section: (number, title, blocks). A block is one of:
#   ("p",   text)                     paragraph
#   ("sub", text)                     sub-heading
#   ("ul",  [items])                  bullet list
#   ("dl",  [(term, desc), ...])      term / description list
#   ("note", text)                    claret callout
CONTENT = [
    ("01", "Position Summary", [
        ("p", "The Head of AI Operations is accountable for transforming AI from isolated tools and pilots into a scalable, governed, economically legible enterprise operating capability. The role owns the AI portfolio lifecycle, the governance and evaluation regime, the economics, adoption, and the measurement system."),
        ("p", "It is judged on business outcomes: cost, cycle time, throughput, quality, revenue, and audited risk posture. Engineering builds AI; this role ensures AI improves the operations and economics of the enterprise."),
        ("note", "Reports to the Chief Operating Officer. " + SCALE_NOTE),
    ]),
    ("02", "Why This Role Exists", [
        ("p", "Every wave of technology has produced an operations discipline once its flow reached scale. Enterprise IT produced IT Operations and ITIL. Software delivery produced DevOps and Site Reliability Engineering. Cloud spend produced FinOps. In each case the flow arrived first, informal management became too costly, and a discipline was named to run it."),
        ("p", "Enterprise AI is now at that point on the arc. The capability is everywhere; the value is not, because most organizations collect all of the cost, which accrues by default, and an unknown fraction of the value, which accrues only by design. The gap is not a technology problem. It is an operations problem, and it needs a single accountable owner."),
    ]),
    ("03", "The Mandate (First Year)", [
        ("p", "The mandate is the standing set of functions the role owns. In the first year it resolves to a concrete deliverable set."),
        ("ul", [
            "Build the complete enterprise AI inventory and the fully loaded spend picture.",
            "Establish the operating model: lifecycle, gates, intake, and the governance constitution, with executive sign-off.",
            "Deliver two to three governed production workflows with measured deltas against frozen baselines.",
            "Stand up the evaluation regime, golden sets, faithfulness measurement, and per-stage error accounting, on all consequential workflows.",
            "Implement unit economics and showback with Finance; run the first routing reviews and capture the savings.",
            "Deliver the measurement system through to the board page.",
            "Reach a governed, measured maturity level by day 365, evidenced.",
        ]),
    ]),
    ("04", "Core Responsibilities", [
        ("p", "Six areas of standing responsibility. Each is a recurring function, owned and measured, not a one-time project."),
        ("dl", [
            ("Portfolio & Operating Model", "Run one inventory and one lifecycle for every AI initiative, embedded SaaS features and shadow patterns included. Own the stage gates, the published intake criteria, and the governance constitution, and hold exactly one accountable owner per workflow."),
            ("Workflow Redesign", "Locate value in the workflow, not the model. Map processes as they actually run, redesign around the constraint, and measure gains end-to-end against baselines frozen at intake."),
            ("Governance, Reliability & Evaluation", "Run the evaluation regime: versioned golden sets, faithfulness measurement, and per-stage error accounting. Match the control architecture to the cost of an undetected error, from light logging on tolerant work to independent generator and verifier separation on the near-zero-tolerance class."),
            ("Economics", "Make AI economically legible. Meter the fully loaded cost per workflow execution, price in verification, retries, and review labor, attribute every unit of spend to a workflow and a business unit, and run the quarterly route reviews that turn model choice into a procurement decision."),
            ("Adoption & Change", "Convert shadow AI into governed capability on a paved road, using amnesty rather than enforcement. Treat adoption as design, not decree, and measure real completed use, not logins."),
            ("Measurement & Reporting", "Deliver the measurement system at three altitudes, from the operational panel to the monthly executive dashboard to the board page. Never publish a number the function cannot defend under audit."),
        ]),
    ]),
    ("05", "How the Role Is Measured", [
        ("p", "A discipline is its metrics. The measurement system groups into four families, each answering one plain executive question. Every metric names the way it can be gamed and the counter; a sample follows."),
        ("dl", [
            ("Value & economics — “Is it worth it?”", "AI ROI against frozen intake baselines, with Finance co-signing the numerator; fully loaded cost per workflow execution, trended monthly; and time-to-ROI per workflow."),
            ("Operational performance — “Is it working?”", "Production deployment rate and median days from pilot to production; end-to-end cycle-time reduction against baseline; and SLO attainment inside the error budget."),
            ("Adoption — “Is it used?”", "Adoption measured on completed executions, not logins; depth of use reported by median and quartile, not mean; and shadow-AI reduction with conversion into sanctioned equivalents."),
            ("Governance & risk — “Is it safe?”", "Measured error rate against golden sets with confidence bounds; human review rate against each workflow's class policy, with the earned-reduction log; and incident rate with mean time to contain and resolve."),
        ]),
    ]),
    ("06", "Competency Profile", [
        ("p", "The role is a translation role before it is a technical one. The load-bearing competencies:"),
        ("dl", [
            ("Operations leadership (10–15+ years)", "Has owned cross-functional outcome accountability at scale, in supply chain, customer operations, risk operations, or transformation. Has held a number that mattered."),
            ("AI systems literacy", "Can read an architecture, interrogate an evaluation, and hold the workflow-versus-agent trade-off with engineers. A builder, not only a reader."),
            ("Reliability & governance instinct", "Thinks in error rates, control limits, audit trails, and disclosure, and treats “how do you know it is right?” as the first question, not a compliance afterthought."),
            ("Financial fluency", "Builds unit-cost models, defends an ROI methodology to a CFO, and manages a vendor portfolio and its contracts."),
            ("Translation", "Speaks risk officer, CFO, engineer, and frontline operator natively, in the same meeting. This is the load-bearing skill of the role."),
            ("Change leadership", "Has moved real organizations through operating-model change, and understands adoption as design, not decree."),
        ]),
    ]),
    ("07", "Ideal Background", [
        ("p", "The strongest candidates are operations leaders who have built AI systems, not AI engineers who have observed operations. The hard problems of the role, accountability design, cross-functional coordination, unit economics, adoption, and governance that survives audit, are twenty-year operations problems wearing a new technical surface. The technical fluency is trainable and verifiable. The operator judgment is the scarce input."),
        ("p", "Candidates who have personally built governed, evaluated, multi-model AI pipelines, even at small scale, should be weighted heavily. They have run the entire discipline in miniature and know where it bites."),
        ("note", "The profile in one line: fifteen years of owning operational outcomes, plus demonstrated hands-on fluency with modern AI systems, plus a coherent reliability philosophy."),
    ]),
    ("08", "Reporting, Team, and Path", [
        ("sub", "Reporting line"),
        ("p", "The role reports to the Chief Operating Officer. The reasoning is structural, not political: AI Operations is accountable in operational and financial outcomes across functions, and the COO already owns cross-functional outcome accountability. Reporting into Engineering converts the function back into MLOps, where accountability for the artifact displaces accountability for the outcome. Reporting into IT frames AI as a support service to be ticketed rather than an operating capability to be run. The reporting line is a statement about what kind of thing the enterprise believes AI is."),
        ("sub", "Team shape"),
        ("p", "A thin central hub owns standards, portfolio control, audit, intelligence, and policy. Workflow ownership is embedded in the business units. The hub's leverage is standards, not throughput, and its headcount scales with the portfolio's tolerance-class mix, not its raw workflow count."),
        ("sub", "Career path"),
        ("p", "Head of AI Operations, to VP of AI Operations, to Chief AI Officer or COO. The role is, structurally, COO training for the AI-era enterprise, because it rehearses the same portfolio: cross-functional outcomes, economics, risk, and change."),
    ]),
    ("09", "The First 365 Days", [
        ("p", "Sequenced so that every phase funds the credibility of the next. The organizing principle: show a measured win early, and never publish a number the function cannot defend under audit."),
        ("dl", [
            ("Days 1–30 · See the whole board", "Build the portfolio inventory, every initiative, tool, embedded feature, and known shadow pattern, with owner, workflow, spend, and tolerance class. Assemble the first fully loaded spend picture with Finance. The readout is usually the first time anyone has seen the whole board, and it alone typically justifies the role."),
            ("Days 31–90 · First governed wins", "Take two or three workflows through the full lifecycle gates with committed owners and frozen baselines. Debug the gates, not just the workflows. Launch a public intake with published criteria and a visible queue."),
            ("Days 91–180 · Production and proof", "Pass the first workflows through the production gate and publish measured deltas against frozen baselines. Run the first eval-driven route review and capture the routing savings, usually the fastest hard-dollar win. Begin monthly executive dashboards and the first independent audit."),
            ("Days 181–365 · Scale the system, not the headcount", "Expand the portfolio through the proven lifecycle. Implement showback with Finance and publish unit-cost trends. Codify the paved road so routine use is self-service against hub standards. Deliver the year-one board readout as an investment case, not a budget ask."),
        ]),
    ]),
    ("10", "Normative Requirements (AIOPS-ROLE)", [
        ("p", "The Specification's binding requirements for the role and its reporting line:"),
        ("ul", [
            "AIOPS-ROLE-01 (MUST). The enterprise MUST designate a single accountable executive for AI Operations with a cross-functional mandate spanning engineering, finance, risk, and the business lines.",
            "AIOPS-ROLE-02 (MUST). The role MUST be judged on business outcomes, cycle time, cost per unit, throughput, quality, revenue, and audited risk posture, not on technology outputs.",
            "AIOPS-ORG-01 (SHOULD / MUST NOT). The function SHOULD report to the Chief Operating Officer; it MUST NOT report into Engineering or IT.",
        ]),
        ("p", "The full 57-requirement standard, with parts, appendices, and conformance levels, is set out in the AI Operations Specification v1.0."),
    ]),
]

CSS = """
:root{--paper:#F7F0E4;--ink:#201A12;--ink-soft:#6B6152;--claret:#8E1D33;--claret-900:#4E0E18;--line:#D9CCB4;--line-strong:#C9B896;
--display:'Besley',Georgia,serif;--serif:'Source Serif 4',Georgia,serif;--sans:'Archivo','Segoe UI',sans-serif;}
@page{size:letter;margin:0.9in 1.1in 0.95in;}
*{box-sizing:border-box;margin:0;padding:0;}
html{background:#F7F0E4;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{background:#F7F0E4;color:var(--ink);font-family:var(--serif);font-size:11pt;line-height:1.6;
-webkit-print-color-adjust:exact;print-color-adjust:exact;text-rendering:optimizeLegibility;}
.title-page{min-height:8.6in;display:flex;flex-direction:column;justify-content:center;break-after:page;}
.title-rule{width:46pt;height:3px;background:var(--claret);margin-bottom:20pt;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
.eyebrow{font-family:var(--sans);font-size:9pt;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--claret-900);}
.title{font-family:var(--display);font-weight:800;font-size:40pt;line-height:1.02;letter-spacing:-.025em;margin:14pt 0 10pt;}
.subtitle{font-family:var(--display);font-style:italic;font-weight:400;font-size:19pt;letter-spacing:-.01em;color:var(--claret);}
.byline{font-family:var(--sans);font-size:10.5pt;letter-spacing:.02em;color:var(--ink-soft);margin-top:30pt;}
.byline strong{color:var(--ink);font-weight:700;}
section{break-inside:auto;}
.sec-head{break-inside:avoid;break-after:avoid;margin:22pt 0 10pt;padding-top:12pt;border-top:1px solid var(--line);}
.sec-head.first{margin-top:0;padding-top:0;border-top:none;}
.sec-num{font-family:var(--sans);font-size:8.5pt;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--claret-900);}
h2{font-family:var(--display);font-weight:600;font-size:20pt;line-height:1.14;letter-spacing:-.01em;margin-top:4pt;}
.sub{font-family:var(--sans);font-weight:700;font-size:10pt;letter-spacing:.03em;color:var(--claret-900);margin:12pt 0 4pt;break-after:avoid;}
p{margin-bottom:8pt;orphans:2;widows:2;}
ul{margin:2pt 0 9pt 0;padding-left:0;list-style:none;}
li{position:relative;padding-left:16pt;margin-bottom:5pt;break-inside:avoid;}
li::before{content:'';position:absolute;left:3pt;top:.6em;width:4pt;height:4pt;background:var(--claret);border-radius:50%;
-webkit-print-color-adjust:exact;print-color-adjust:exact;}
dl{margin:4pt 0 9pt;}
.dl-row{break-inside:avoid;margin-bottom:8pt;}
.dl-row dt{font-family:var(--sans);font-weight:700;font-size:10pt;letter-spacing:.01em;color:var(--ink);margin-bottom:2pt;}
.dl-row dd{margin:0;color:var(--ink);}
.note{background:#EFE6D4;border-left:3px solid var(--claret);border-radius:0 6px 6px 0;padding:12pt 16pt;margin:12pt 0;
font-family:var(--serif);font-style:italic;font-size:10.5pt;line-height:1.5;color:var(--claret-900);break-inside:avoid;
-webkit-print-color-adjust:exact;print-color-adjust:exact;}
"""

def esc(t): return html.escape(t, quote=False)

def render_blocks(blocks):
    out = []
    for kind, val in blocks:
        if kind == "p":
            out.append(f"<p>{esc(val)}</p>")
        elif kind == "sub":
            out.append(f'<p class="sub">{esc(val)}</p>')
        elif kind == "note":
            out.append(f'<div class="note">{esc(val)}</div>')
        elif kind == "ul":
            items = "".join(f"<li>{esc(i)}</li>" for i in val)
            out.append(f"<ul>{items}</ul>")
        elif kind == "dl":
            rows = "".join(f'<div class="dl-row"><dt>{esc(t)}</dt><dd>{esc(d)}</dd></div>' for t, d in val)
            out.append(f"<dl>{rows}</dl>")
    return "\n".join(out)

def build_html():
    secs = []
    for i, (num, title, blocks) in enumerate(CONTENT):
        first = " first" if i == 0 else ""
        secs.append(
            f'<section><div class="sec-head{first}"><p class="sec-num">{num}</p>'
            f'<h2>{esc(title)}</h2></div>\n{render_blocks(blocks)}</section>'
        )
    fonts = ("https://fonts.googleapis.com/css2?family=Besley:ital,wght@0,400;0,600;0,800;1,400"
             "&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400"
             "&family=Archivo:wght@400;600;700&display=swap")
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Head of AI Operations — Role Standard</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts}" rel="stylesheet"><style>{CSS}</style></head><body>
<div class="title-page"><div class="title-rule"></div>
<p class="eyebrow">Role Standard · Companion to the Specification v1.0</p>
<h1 class="title">{esc(TITLE)}</h1>
<p class="subtitle">{esc(SUBTITLE)}</p>
<p class="byline"><strong>Daniel S. Wipert</strong><br>AI Operations Management · 2026</p></div>
{chr(10).join(secs)}
</body></html>"""

def main():
    print_pdf(build_html(), OUT, FOOTER)

if __name__ == "__main__":
    main()
