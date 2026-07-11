#!/usr/bin/env python3
"""
Build the Field Note article pages under field-notes/ from the content below,
styled with the site stylesheet. Run after editing a note's text.

Usage: python tools/build_field_notes.py
"""
import os, html

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(REPO, "field-notes")

# Each note: number, category, slug, title, dek, body (list of ('p'|'principle', text)),
# end (a serifed sign-off; {LINK} is replaced with the manifesto link).
NOTES = [
    {
        "num": "01", "cat": "Cost & Pricing", "slug": "access-price-is-not-total-cost",
        "title": "Access Price Is Not Total Cost",
        "dek": "The number on the invoice is the entry fee, not the running cost. What an organization pays to gain access to AI is the smallest, most visible part of what AI costs to operate.",
        "body": [
            ("p", "Every organization can find its AI spend on a subscription line or a monthly invoice. That figure is real, and it is also the least informative number in the whole account. It records the price of access. It does not record the cost of operation, and at production scale the two diverge by an order of magnitude."),
            ("p", "Access is an idea inherited from software. You buy a seat, you pay a renewal, and the marginal cost of the hundredth use is effectively zero. Production AI does not behave that way. Every model call, every retry, every step in an agent loop, and every review a person performs on the output is a consumption event with a cost that travels with the work. The invoice shows what was bought. It does not show what is being run."),
            ("p", "The fully loaded cost of a unit of AI work is assembled from parts that rarely sit on the same line. There is the direct cost of the calls, which multiplies quietly as retries and multi-step agents turn one request into many. There is the gateway and the infrastructure around it. There is the human time spent reviewing, correcting, and supervising output that cannot yet be trusted unattended. There is the cost of rework when the output is wrong, and the cost of the failure it causes when the error is not caught. None of these appear on the access line, and together they usually exceed it."),
            ("p", "Flat pricing widens the gap by design. A subscription converts a variable cost into a fixed one on the buyer's books while leaving it variable on the provider's. An AI provider carrying real, variable delivery cost against fixed subscription revenue holds a position that does not clear, and it resolves the way such positions always resolve: through meters, tiers, rate limits, priority access, and repricing. The flat rate an organization plans around today is a pricing artifact, not an economic constant, and the correction arrives on the provider's schedule, not the buyer's."),
            ("principle", "The operating principle is narrow and strict. Evaluate AI on the fully loaded cost of a unit of work, not on the price of access. What an organization pays to get in is not what it pays to run."),
            ("p", "This is not a case for spending less. It is a case for knowing what is spent. An organization that budgets against the access line is not managing its cost. It is managing the one number the provider chose to make visible, while the consumption that determines its actual exposure accumulates, unmeasured, beneath it."),
        ],
        "end": "Access price is the visible fraction. The consumption underneath it is the economic reality, and it answers to the same discipline as any other flow: measured, attributed, and owned. Cost accrues by default. {LINK}",
    },
    {
        "num": "02", "cat": "ROI & Productivity", "slug": "productivity-is-not-roi",
        "title": "Productivity Is Not ROI",
        "dek": "A productivity story is the easiest thing to tell about AI and the hardest thing to bank. Saved time is not a return until someone captures it.",
        "body": [
            ("p", "The most common claim made for AI inside organizations is a productivity claim. The model drafts in seconds what took an hour. The assistant makes the team faster. The developers report that they ship more. These statements are usually true, and they are almost never returns."),
            ("p", "A return requires that a specific benefit be captured, somewhere, net of what it cost to produce. Saved time is not captured value on its own. Time freed from one task becomes value only if the freed capacity is redeployed to work the business can monetize, or if a cost is actually removed. Time that fans out into more slack, more meetings, or more output no one needed is a productivity story with no line in the accounts. The hour was saved. Nothing was captured."),
            ("p", "The distinction is not pedantic. Cost enters the flow automatically: every call, every review, every retry accrues whether or not anyone decides it should. Value does not. It appears only where someone draws a boundary around a specific piece of the business, this workflow, this period, this measured outcome, and answers a plain question honestly: what did this cost, and what did it return, net. Outside such a boundary a value claim floats free of any test, and untested claims default to the optimistic reading."),
            ("p", "A productivity gain becomes a return the moment it crosses a boundary that someone owns. A role that is not backfilled. A queue that is cleared, releasing the revenue that was waiting behind it. A vendor line that actually falls. A cycle time that shortens in a way a customer pays for. Each of these is a captured benefit with a name against it. The difference between this and a team that feels faster is the difference between a return and a feeling."),
            ("principle", "The operating principle: require every AI value claim to name its boundary. Where is the benefit captured, over what period, measured how, net of what cost, and who is accountable for the answer. A claim that cannot name its boundary is a productivity story, not a return."),
            ("p", "This is where most AI programs quietly lose money. They collect one hundred percent of the cost, which accrues by default, and an unknown fraction of the value, which accrues only by design. The gap between the two is invisible on any dashboard that measures usage. It is visible only at a boundary someone was accountable for drawing, and in most organizations no one is."),
        ],
        "end": "Productivity is the story. Captured value is the return, and it exists only at a boundary someone owns. Value accrues by design. {LINK}",
    },
    {
        "num": "03", "cat": "Model Selection", "slug": "capability-is-not-economic-suitability",
        "title": "Capability Is Not Economic Suitability",
        "dek": "The most capable model is not automatically the correct one. Choosing it is an economic decision wearing the costume of a technical one.",
        "body": [
            ("p", "When an organization selects a model, the reflex is to reach for the most capable one available, the model at the top of the benchmarks. The reflex feels responsible. It is usually an error, and an expensive one, because it answers an economic question with a technical ranking."),
            ("p", "Capability and economic suitability are distinct properties. Capability is what a model can do in the abstract, measured against a leaderboard. Suitability is whether a given model is the correct instrument for a given piece of work once the work's real requirements are brought inside the evaluation: the accuracy the task actually needs, the latency it can tolerate, the reliability it demands, and the value at stake if it is wrong. A model can lead every benchmark and still be the wrong choice for the task in front of it."),
            ("p", "There are two failure modes, and organizations run both at once. The first is overpaying: routing high-volume, low-stakes work to premium capacity that clears a bar the work never required. This is pure cost exposure with no marginal value, repeated across every request. The second is underpaying: starving low-volume, high-stakes work of the capability it genuinely needs, and accepting a value risk that dwarfs the saving. Both are allocation failures, and both come from treating model choice as a single ranking rather than a match between work and capacity."),
            ("p", "The correct model for a task is the least expensive capacity that reliably clears the task's actual requirements. For a classification running millions of times a day, that is rarely the frontier model. For a decision that carries real consequence and runs rarely, it may cost more than the frontier model alone, wrapped in the verification that a single model does not provide. The benchmark cannot tell you which case you are in, because the benchmark does not know your cost, your latency, or your value at stake."),
            ("principle", "The operating principle: match work to capacity on economic terms. Sourcing is procurement, not a technology ranking. The question is never which model is best. It is which model is correct for this work, at this volume, at this level of consequence, at this cost."),
            ("p", "This is a discipline performed deliberately and on a schedule, not a decision made once when a new model launches. Capability changes monthly. The economics of a task change with its volume and its stakes. An organization that chooses once, by benchmark, is not sourcing. It is buying the finest grade of everything and calling it diligence."),
        ],
        "end": "Capability is a leaderboard. Suitability is an economic decision, and the most capable model is not automatically the correct model. {LINK}",
    },
]

def esc(t): return html.escape(t, quote=False)

FONTS = ("https://fonts.googleapis.com/css2?family=Besley:ital,wght@0,400;0,600;0,800;1,400"
         "&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400"
         "&family=Archivo:wght@400;500;600;700&display=swap")

def render(note, others):
    body = []
    for kind, text in note["body"]:
        if kind == "principle":
            body.append(f'<p class="note-principle">{esc(text)}</p>')
        else:
            body.append(f"<p>{esc(text)}</p>")
    link = '<a href="../index.html#manifesto">Read the manifesto &rarr;</a>'
    end = esc(note["end"]).replace("{LINK}", link)
    more = []
    for o in others:
        more.append(f'<a href="{o["slug"]}.html"><span class="nm-cat">{esc(o["cat"])}</span>'
                    f'<span class="nm-title">{esc(o["title"])}</span></a>')
    more_html = "".join(more)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(note['title'])} &middot; AI Operations Management</title>
<meta name="description" content="{esc(note['dek'])}">
<meta property="og:type" content="article">
<meta property="og:title" content="{esc(note['title'])} &middot; AI Operations Management">
<meta property="og:description" content="{esc(note['dek'])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/site.css">
</head>
<body>
<div class="masthead-rule" aria-hidden="true"></div>
<nav id="nav" class="stuck" aria-label="Field note navigation">
  <div class="nav-inner">
    <a class="brand" href="../index.html#top">AI Operations <span>Management</span></a>
    <a class="note-back" href="../index.html#notes">&larr; Field Notes</a>
  </div>
</nav>
<article class="note">
  <div class="wrap">
    <div class="prose">
      <header class="note-head">
        <p class="note-eyebrow">Field Note {note['num']} &middot; {esc(note['cat'])}</p>
        <h1 class="note-title">{esc(note['title'])}</h1>
        <p class="note-dek">{esc(note['dek'])}</p>
        <p class="note-meta">Daniel Wipert &middot; 2026</p>
      </header>
      {chr(10).join(body)}
      <div class="note-end"><p>{end}</p></div>
      <nav class="note-more" aria-label="More field notes">
        <p class="nm-label">More field notes</p>
        {more_html}
      </nav>
    </div>
  </div>
</article>
<footer>
  <div class="foot-inner">
    <p>&copy; 2026 Daniel Wipert &middot; AI Operations Management</p>
    <p class="foot-invite">A discipline is being named. You are early.</p>
  </div>
</footer>
</body>
</html>
"""

def main():
    os.makedirs(OUTDIR, exist_ok=True)
    for note in NOTES:
        others = [o for o in NOTES if o["slug"] != note["slug"]]
        path = os.path.join(OUTDIR, note["slug"] + ".html")
        open(path, "w", encoding="utf-8").write(render(note, others))
        print("wrote", path)

if __name__ == "__main__":
    main()
