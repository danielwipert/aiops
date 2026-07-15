# Site Update Spec — danielwipert.github.io/aiops

**Scope:** Add "The Role" page + role standard PDF, add spec PDF download, fix one title inconsistency. Deliberately small — no redesign, no restyling, no new dependencies. Match the existing site exactly.

---

## Context

The site is the public home of AI Operations Management (the discipline). It currently hosts:

- `index.html` — the founding argument (Manifesto, The Flow, The Functions, Field Notes, About, The Monday Test)
- `AI-Operations-Management.pdf` — the downloadable manifesto
- `field-notes/*.html` — short analyses

Two artifacts named in the body of work are NOT yet on the site and need to be:

1. **AI Operations Specification v1.0** — 57-requirement enterprise standard (source: `AI_Operations_Specification_v1.docx`)
2. **Head of AI Operations — Role Standard** — executive role specification (source: `Head_of_AI_Operations_Job_Description.docx`)

Both source .docx files will be provided in the working directory.

---

## Task 1 — New page: `role/index.html` ("The Role")

A single new page presenting the role standard in the site's editorial voice.

### Requirements

- **Reuse the existing site's CSS, fonts, nav, and footer verbatim.** No new styles beyond what composition requires. The page must be indistinguishable in design language from `index.html`.
- **Add "The Role" to the top nav** on `index.html` and any other pages that share the nav (field notes pages if they carry it). Place it between "The Functions" and "Field Notes".
- **URL:** `/aiops/role/` (directory with `index.html`).

### Page structure (in order)

1. **Hero:** Title "The Role: Head of AI Operations". Subtitle: "The executive specification for the discipline's owner." One-line framing: every discipline that reached the executive level was eventually held by a named role — this page specifies it.
2. **Position summary** — adapt from the source docx Position Summary + "Why This Role Exists" sections. Keep it tight: 2–3 short paragraphs.
3. **The mandate** — the Core Responsibilities areas as a scannable grid or list (Portfolio & Operating Model, Workflow Redesign, Governance/Reliability/Evaluation, Economics, Adoption & Change, Measurement & Reporting). One or two sentences each, not the full bullet lists — the PDF carries the detail.
4. **How the role is measured** — the four KPI families (Value & economics, Operational performance, Adoption, Governance & risk) with 2–3 example KPIs each. Reuse the site's card/panel treatment if one exists.
5. **The first 365 days** — the four phases (Days 1–30, 31–90, 91–180, 181–365) as a timeline or stepped list, one line per phase.
6. **Reporting-line doctrine** — short section: reports to the COO; not Engineering, not IT, and why (artifact accountability vs. outcome accountability). This is a signature position — give it its own heading.
7. **Ideal background** — the one-liner: "fifteen years of owning operational outcomes, plus demonstrated hands-on fluency with modern AI systems, plus a coherent reliability philosophy." Include the "operations leaders who have built AI systems, not AI engineers who have observed operations" line.
8. **Download CTA:** "Download the Role Standard (PDF)" → `/aiops/Head-of-AI-Operations-Role-Standard.pdf`. Style identical to the manifesto download button.

### Voice rules

- Match the manifesto's register: declarative, short sentences, no marketing adjectives, no exclamation points.
- Reuse the site's established vocabulary: flow, boundary, attribution, "cost accrues by default; value accrues by design."
- Do not invent new claims. Everything on the page must trace to the source docx or the manifesto.

---

## Task 2 — Role Standard PDF

Produce `Head-of-AI-Operations-Role-Standard.pdf` from the source docx.

- Full document content, print-clean, consistent with the manifesto PDF's level of polish (simple, typographic, no decoration).
- **Required edit before export:** add a one-line title-scaling note near the top (after the "Reports to the Chief Operating Officer" line or in the Organization section): *"The title scales with organization size: Director of AI Operations in mid-size enterprises, Head or VP of AI Operations at scale."* This reconciles the spec's Section 17 ("Director of AI Operations") with this document's "Head of AI Operations" title.
- Footer on each page: `Head of AI Operations — Role Standard · Companion to the AI Operations Specification v1.0 · Daniel S. Wipert`

## Task 3 — Specification PDF

Produce `AI-Operations-Specification-v1.pdf` from the source docx.

- Full document, same print treatment as Task 2. Preserve the internal structure (Parts I–VII, appendices, tables).
- No content edits.

## Task 4 — Link the PDFs from `index.html`

- In the **About** section (which currently has "Download the manifesto (PDF)"), add two sibling links with identical styling: "Download the Specification v1.0 (PDF)" and "Download the Role Standard (PDF)".
- In the **Functions** or closing section, if there is a natural spot, one inline sentence linking to `/aiops/role/`: "The discipline's owner is specified in full: The Role." Skip if no clean insertion point exists — do not force it.

---

## Constraints

- **No framework, no build step, no npm.** Plain HTML/CSS/JS only, matching the existing repo.
- **No analytics or external requests added.** The site's "all metering is client-side" claim must stay true.
- Keep the existing live session meter untouched. If it is a shared script, the new page may include it as-is; do not modify its behavior.
- All internal links relative; site is served from the `/aiops/` project path on GitHub Pages — verify links work under that prefix.
- Mobile: the new page must be readable at 380px width using whatever responsive patterns the site already has.

## Acceptance checklist

- [ ] `/aiops/role/` renders, matches site design, nav works both directions
- [ ] Both PDFs download from the About section and from the role page CTA
- [ ] Title-scaling note appears in the role standard PDF
- [ ] Nav updated on all pages that share it
- [ ] No new external dependencies; no console errors
- [ ] Links verified under the `/aiops/` GitHub Pages prefix
