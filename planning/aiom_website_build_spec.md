# AI Operations Management — Website Build Spec (Claude Code Handoff)

**Project:** Launch site for the AI Operations Management manifesto
**Owner:** Daniel Wipert
**Status:** High-fidelity prototype complete (`aiom_site.html`, included in repo). Next phase: port to production stack.
**Date:** 2026-07-10

---

## 1. What this site is

A category-defining editorial microsite launching **AI Operations Management** as a new business discipline. It is a serious intellectual field launch: not a SaaS landing page, not a personal blog, not documentation.

Central claim:

> Companies know how to buy software. They do not yet know how to operate AI as a high-volume flow of usage, records, cost, and value.

Core argument arc (the page follows this order): category error → flow problem → historical rhyme → triple flow → five functions → boundary setting (what this is not) → diagnostic (the Monday Test) → field invitation.

The one idea the reader must leave with:

> Cost accrues by default; value accrues by design.

Target reader: senior operators, executives, finance and strategy leaders moving from AI experimentation to production. Desired reaction: "This names something I have been seeing but could not yet organize."

---

## 2. Decisions locked (do not relitigate)

1. **Tagline:** "The Discipline of the Flow" is the public tagline for the site (hero, SEO title, OG image). The manifesto document's subtitle ("A Discipline of AI Consumption") is a separate matter; the site uses Flow. "Consumption" appears as a first-paragraph concept, not the flag.
2. **Visual mood:** Warm ivory editorial (Stripe Press / FT feel). Accent: claret/oxblood, quietly echoing the owner's FT lineage.
3. **Build path:** Single-file HTML prototype first (done), then port to Next.js + TypeScript + Tailwind + Framer Motion + MDX, deployed on Vercel. Framer/Webflow are rejected; this is a long-term intellectual platform.
4. **Signature element:** The site meters itself (Section 4 below). This is the one bold move. Everything else stays quiet and disciplined. Do not add additional decorative animation.
5. **Interactive triple-flow diagram** encodes the cost/value asymmetry in its animation: cost line fills automatically and continuously; value appears only as bracketed captures at a drawn boundary.

---

## 3. Design system (as implemented in prototype)

### Color tokens

```css
--paper:      #F7F0E4;  /* warm ivory background */
--paper-deep: #EFE4D1;
--paper-card: #FBF6EC;  /* card surfaces */
--ink:        #201A12;  /* warm near-black; also the dark section bg */
--ink-soft:   #6B6152;  /* secondary text */
--claret:     #8E1D33;  /* primary accent: usage flow, CTAs, principles */
--amber:      #A8741F;  /* cost flow accent */
--line:       #D9CCB4;  /* hairlines */
--line-strong:#B9A987;
```

Dark-section (Monday Test, meter panel) supporting values: `#2A2318` card bg, `#3A332A` borders, `#CFC5B2` body text, `#D98A9B` claret-on-dark labels, `#8A7F6C` muted.

### Typography

- **Display: Besley** (Google Fonts). A Clarendon revival, the letterforms of ledgers, railways, and freight manifests. Chosen because it is literally supply-chain-era typography, grounding the editorial feel in the argument itself. Weights: 400 (italic for subtitles/claims), 600 (section titles), 800 (hero, function numbers).
- **Body prose: Source Serif 4**, 1.125rem / 1.78 line height. Long-form essay reads in serif.
- **UI/labels: Archivo** 400–700. Nav, eyebrows, cards, diagram labels, the meter. Eyebrows: 0.72rem, 600, letter-spacing 0.16em, uppercase.
- Tabular numerals (`font-variant-numeric: tabular-nums`) everywhere numbers tick.

### Layout

- Prose column max 680px, centered. Diagrams break out to ~1000px. Page container 1120px.
- Sections separated by 1px hairlines, 104px vertical padding.
- Sticky nav appears with ivory blur after 40px scroll. Mobile menu collapses.
- Scroll reveals: `.rv` class + IntersectionObserver, single fade-up, unobserved after firing. Restrained.

### Voice rules for ALL site copy (hard constraints)

- **No em dashes. Anywhere.** Use commas, semicolons, or split sentences.
- No humor, no irony in manifesto-register copy. FT / Economist / serious field memo voice.
- Preferred vocabulary: operational consumption, usage flow, record flow, cost exposure, value boundary, captured value, usage-aware budgeting, allocation discipline, production AI, management discipline.
- Banned vocabulary: AI revolution, game-changing, unlock, magic, superintelligence, autonomous everything.
- **Non-disclosure principle:** the private formal system behind the manifesto must never be exposed. Never use publicly: DAG, theorem, lemma, proposition, axiom, proof path, locked registry, dependency graph, proof system, formal traceability. Translations: theorem → operating principle; proof path → rationale; dependency graph → underlying research; locked registry → research base. Approved framing: "part of a broader research project on the economics of business AI adoption."

---

## 4. The signature: the self-metering page

**Concept.** The site does not merely describe the flow; it is one. A persistent meter logs the reader's own session as a stream of consumption events with notional cost, live, from arrival. Cost accrues whether the reader does anything deliberate or not. Value stays at zero until the reader completes the Monday Test, the single bounded, deliberate act on the page, at which point one captured-value event registers inside brackets. The reader enacts "cost accrues by default; value accrues by design" instead of reading it.

**Why it is defensible:** no other site can justify this mechanic; it is the thesis made mechanical. It is also cheap (fully client-side) and privacy-clean, which itself reinforces the record-flow argument.

### Meter UI

- Fixed pill, bottom-right: pulsing claret dot + `N events · ¤0.0000`. Ink-dark on ivory so it reads on every section.
- Tap to expand an ink-dark panel: consumption events count, cost accrued, value captured (greyed, in brackets `⟨ ¤0.0000 ⟩`), a thesis line, a scrolling ledger (newest first, capped at 30 rows, each row: elapsed mm:ss, label, cost), and a footer.
- Footer copy (verbatim): "All metering is client-side and notional. No records leave this page. The records are yours, which is rather the point."
- Currency is **¤, the generic currency sign**: deliberately denominated in no one's currency, honest about being notional. 4 decimal places.

### Event sources and notional costs

| Event | Cost (¤) | Notes |
|---|---|---|
| Page load | 0.0006 | First ledger entry |
| Idle tick | 0.0002 | Every 7s while tab visible; the "by default" beat |
| Section entered | 0.0006 | First entry per section, IntersectionObserver 0.25 |
| Scroll depth 25/50/75/100% | 0.0004 | Once each |
| Function card tapped | 0.0008 | Delegated listener |
| Diagnostic question answered | 0.0008 | Delegated listener |

### Value capture

- Trigger: Monday Test result appears (prototype watches `#quizResult` gaining class `show` via MutationObserver; fires once).
- Effect: value set to **¤0.0500** (calibrated to be roughly 2–3× a full read-through's accrued cost; value must visibly exceed cost). Ledger gets a claret capture row: `VALUE BOUNDARY DRAWN · Monday Test completed · +¤0.0500`. Value row lights up claret. Thesis line flips from "Cost accrues by default." to "Value accrues by design." Pill flashes claret once.

### Narrative tie-ins (in page copy)

- Flow Problem section includes: "This page is metering itself as you read it. Every scroll, tap, and idle second since you arrived has been logged in the corner as a consumption event, each carrying cost. Nothing you have done so far has registered value."
- Monday Test intro includes: "It is also the only act on this page that registers captured value."

### Calibration knobs (owner may still tune)

- Idle tick interval (currently 7000ms).
- Captured value amount (currently 0.0500).

---

## 5. Page inventory (as built in `aiom_site.html`)

Single page, anchor navigation. Nav: Manifesto · The Flow · The Functions · Field Notes · About · **The Monday Test** (claret CTA button).

1. **Hero** (`#top`): eyebrow "A founding manifesto · 2026"; H1 "AI Operations Management"; italic sub "The Discipline of the Flow"; lede (the central claim); CTAs "Read the Manifesto" (→ #manifesto) and "Take the Monday Test" (→ #monday). Background: three slow SVG flow lines drawing on load (claret solid = usage, ink dashed = records, amber = cost/value) with drifting event dots; legend beneath CTAs.
2. **The Category Error** (`#manifesto`): prose; split comparison table (Software Access vs AI Operations: seat/usage event, license/model call, renewal/workflow dependency, fixed budget/cost exposure, vendor admin/value uncertainty); **Operating Principle 1: Access is not operation.**
3. **The Flow Problem** (`#flow`): prose incl. meter tie-in; centered pull quote "Cost accrues *by default*. Value accrues *by design*." (claret italics); **Principle 2: The record flow makes the usage flow governable.**
4. **The Historical Rhyme** (`#history`): three-panel progression (Goods Flow → Supply Chain Management; Cloud Spend Flow → FinOps; AI Usage Flow → AI Operations Management, third panel highlighted); **Principle 3: Scale turns informal use into an operating problem.**
5. **The Triple Flow** (`#tripleflow`): the diagram. Three tracks (usage claret / records ink-dashed / cost-value amber), four stage nodes each. Usage stages carry small-caps sublabels: source, convert, deliver, realize. Track lines animate in sequence on scroll (`.armed` class); the cost line fills only to ~68% by design; claret brackets fade in around the "Value boundary" node last. Diagram note explains the asymmetry. **Principle 4: Cost and value do not behave symmetrically.**
6. **The Five Functions** (`#functions`): five interactive cards (Sourcing; Planning & Budgeting; Metering & Attribution; Allocation & Routing; Value-Boundary Management), each with Besley number, question in italic serif, short explanation. Tapping a card highlights its governed stage nodes in the diagram via `data-hot` → `data-seg` matching (mapping: 1→source,deploy; 2→budget,expose; 3→logs,attrib,vis; 4→workflow,deploy; 5→boundary,return). Tap again to clear. **Principle 5: The discipline exists only when the functions are owned.**
7. **What This Is Not** (`#boundaries`): territory map (AIOM center in claret; AI Governance above; FinOps left; MLOps right; AIOps below, each with its one-line question); four "Not X" prose blocks.
8. **The Monday Test** (`#monday`): full section inverts to ink-dark. Five questions (visibility, attribution, cost, allocation, value), each Yes (1) / Partly (0.5) / No (0). Result appears once all five answered: 0–1.5 "You are running the flow in the dark." / 2–3 "Partial visibility, not yet a discipline." / 3.5–4.5 "Emerging AI Operations Management." / 5 "A disciplined AI Operations foundation." Score bar animates. No email capture. Completing the test triggers the meter's value capture.
9. **Field Notes** (`#notes`): three "coming soon" cards: Access Price Is Not Total Cost (Cost & Pricing); Productivity Is Not ROI (ROI & Productivity); Capability Is Not Economic Suitability (Model Selection).
10. **About** (`#about`): Daniel Wipert bio (operations and supply chain leader focused on the economics of business AI adoption; fifteen years across warehouse operations, logistics, production planning, vendor management, risk operations, executive operating cadence). CTAs: Get in touch (mailto placeholder) + Download the manifesto PDF (placeholder link).
11. **Footer:** copyright + "Cost accrues by default. Value accrues by design."

### Accessibility and performance floor (already met; do not regress)

- `prefers-reduced-motion`: all animations disabled, diagram and flow lines render in final state.
- Keyboard: function cards and quiz options are real `<button>`s; visible claret focus rings; quiz result is `aria-live="polite"`; meter pill has `aria-expanded`/`aria-controls`.
- Semantic headings, single H1. Mobile: nav collapses, comparison table stacks, diagram goes 2-column, meter shrinks. No images, no video; everything is CSS/SVG. Lighthouse target 90+.

---

## 6. Port plan (Next.js)

Target structure (from original site spec):

```text
/app
  page.tsx                 ← the single-page experience
  manifesto/page.tsx       ← full manifesto as MDX + PDF download
  field-notes/page.tsx
  about/page.tsx
/components
  Hero.tsx  SectionNav.tsx  FlowDiagram.tsx  PrincipleCard.tsx
  FunctionCards.tsx  BoundaryMap.tsx  MondayTest.tsx
  SessionMeter.tsx         ← NEW: the signature component
  FieldNoteCard.tsx  Footer.tsx
/content
  manifesto.mdx
  field-notes/*.mdx
/lib
  mondayTest.ts  meter.ts  constants.ts
```

Porting notes:

- `SessionMeter.tsx`: client component; context or a tiny event bus so any component can emit `consume(label, cost)`. Keep the MutationObserver approach OR have MondayTest call a `captureValue()` function directly (cleaner in React).
- All meter state is in-memory only. No localStorage, no analytics events for the meter (the footer copy promises this).
- FlowDiagram + FunctionCards share highlight state (lift to parent or context), replacing the prototype's `data-hot`/`data-seg` DOM matching.
- Framer Motion may replace the CSS scroll animations, but keep the restraint: one reveal pattern, the diagram sequence, the capture moment. Nothing else moves.
- SEO: title "AI Operations Management: The Discipline of the Flow"; meta description "AI Operations Management is the discipline of managing AI as a business flow: usage, records, cost, allocation, and captured value in production workflows." OG image: editorial graphic, three flow lines, title + subtitle, no robots/brains/gradients.

---

## 7. Open items

1. **Manifesto PDF**: generate from manifesto v1.1 docx AFTER a voice pass. Known issues in v1.1: two additions that break the manifesto's own voice rules ("It is called being a sucker... This is capitalism, after all"; the OpenRouter/PMT stock-market aside) and a typo ("sprialin chaos"). The v1.0 phrasings of those passages were stronger. Also reconcile the docx subtitle with the site tagline.
2. Real contact method (currently `mailto:hello@example.com` placeholder).
3. Domain, deployment, OG image asset.
4. Field Notes: write the three launch notes as public operating principles (never as theorem references).
5. Owner calibration pass on meter (idle interval, capture amount) after feeling the live rhythm.
6. Hero "Read the Manifesto" CTA currently anchors to the argument; once `/manifesto` exists it should point there.

---

## 8. Success criteria

A first-time executive reader understands: why AI is not software access; why production AI behaves like a flow; what the discipline is; its five functions; how it differs from AIOps/FinOps/MLOps/governance; and what five questions their organization should answer on Monday. They leave with one line: **cost accrues by default; value accrues by design.** And they watched it happen to themselves in the corner of the page.
