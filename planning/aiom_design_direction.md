# AI Operations Management — Design Direction

**Purpose:** Define the visual and experiential direction for the AIOM microsite, grounded in *Refactoring UI* (Wathan & Schoger) and *Laws of UX* (Yablonski). This supersedes the prototype's look; the prototype (`aiom_site.html`) remains a structural reference, not the final design.
**Date:** 2026-07-10
**Reconciles with:** `aiom_website_build_spec.md` (locked decisions §2, design system §3, the self-metering signature §4). Nothing here contradicts those; it deepens them.

---

## 0. What "wow" means here (the reframe)

The owner's goal: a reader opens the page and goes *wow*. Both books, read closely, point to the same conclusion about what that reaction is made of for a **serious field-launch manifesto** — and what it is *not*.

- It is **not** parallax, gradients, 3D, scroll-jacking, or decorative motion. For an FT/Economist/Stripe-Press register aimed at finance and strategy executives, those read as a startup landing page and *lower* credibility. Jakob's Law is explicit: novelty in form is friction; the reader already owns a strong mental model for "serious essay," and violating it costs trust.
- It **is** two things working together:
  1. **Craft so precise it reads as expensive** (the entire thesis of *Refactoring UI*). The Aesthetic–Usability Effect means this craft is *load-bearing*: beautiful typographic setting makes the argument itself feel more rigorous and trustworthy in the first ~50ms, before a word is read. For a discipline that hasn't yet earned its authority, the craft buys the credibility on credit.
  2. **One unforgettable, self-referential peak** (the Peak–End Rule). The page enacts its own thesis: it meters the reader's session as cost accruing *by default*, and value stays at zero until the reader completes the single deliberate act. The "wow" is a peak of *recognition* — "I just did the thing the essay is about" — not spectacle.

**The unifying concept: _the document that meters itself._** A quiet, rigorously-crafted editorial artifact whose one bold move is that it is *also an instance of the flow it describes*. Everything below serves that: maximal restraint everywhere so the single signature detonates.

---

## PART A — The craft system (from *Refactoring UI*)

The rule for every decision below: **supercharge what's already there; add almost nothing.** Separation comes from spacing and two paper tones, not boxes and shadows.

### A1. Color — build ramps in HSL, keep the warmth

Work in HSL so related colors are related in code. The locked tokens sit on a coherent warm axis (~34–39°) with claret as the lone 348° note. Build full ramps up front; never lighten/darken ad hoc. Saturation must *rise* toward both light and dark extremes or the ivory goes dead-grey.

- **Warm ink/paper ramp** (hue ~34–38°): `#201A12` ink → `hsl(34,22%,22%)` → `#6B6152` ink-soft → `hsl(37,15%,55%)` → `#D9CCB4` line → `#FBF6EC` paper-card → `#F7F0E4` paper. Three text colors maximum (ink / ink-soft / one lighter step). Never a fourth.
- **Claret ramp** (base `hsl(348,66%,34%)`): a `900 hsl(350,70%,18%)` for claret *text* on paper, a `100 hsl(346,45%,93%)` faint tint for one pull-quote panel. Rotate ≤3° as it darkens.
- **Amber** (`hsl(37,69%,39%)`) shares the greys' warm axis — a strict *second* accent only (e.g. the meter's active/cost state).
- **Contrast-flip rule:** never white text on a claret/amber field for anything body-level. Use claret-900 text on claret-100 tint. Solid claret is reserved for the masthead rule and the one link underline.
- **Never rely on color alone** (colorblind-safe *and* it makes the meter feel like a real instrument): the cost signal always carries a number + label, not just a hue.

**Consciously avoid:** gradients of any kind (even subtle → SaaS), semantic multi-accent tag colors.

### A2. Typography — the highest-leverage craft on the page

- **Type scale:** hand-picked, in rem/px, never em (nesting drifts). Non-linear steps.
- **Body:** Source Serif 4, 1.125rem / 1.78, in the 680px column ≈ ~72 chars/line — the top of the safe 45–75 range, and 1.78 is the correct line-height for that near-max measure. **Hold 680px; do not widen.**
- **Besley headlines:** pull line-height down to ~1.0–1.15 and apply slight negative tracking (−0.01 to −0.02em). A Clarendon face at default spacing looks generic; tightened, it looks *commissioned*. This is one of the two or three highest-ROI moves on the page.
- **Archivo uppercase eyebrows:** *add* tracking (+0.08–0.12em). Untracked all-caps is the #1 amateur tell; fixing it is what makes the ledger/manifest voice land.
- **Numbers:** Archivo `tabular-nums`, right-aligned everywhere they tick (the meter especially), so decimals stack and the live figure never jitters.
- **Links in prose:** ink text + a thin claret custom underline offset just below the baseline. Not every link needs a color; reserve solid claret fill for nothing.
- Left-align body; a one-line centered Besley deck is fine, longer centered text is not. No justified/hyphenated body (rivers on the web).

### A3. Spacing & layout — restraint as the system

- **Non-linear spacing scale**, e.g. `4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192`. Section padding comes from the *top* of the scale, deliberately, not eyeballed.
- **Ambiguous-spacing rule** (the single highest-leverage spacing move): always more space *around* a group than *within* it. Concretely, ~64–96px above a section heading vs ~24px below it, so headings bind to their body, not float between sections.
- Hold the three hard max-widths: prose 680 / diagram 1000 / container 1120. Max-widths, never fluid percentages. Don't fill the screen; a narrow measure in a wide page is correct.
- Since our only separators are 1px `--line` hairlines, spacing does *all* the grouping — budget it carefully.

### A4. Depth — flat, via paper tones + overlap + hairlines (never blur)

- The two paper tokens *are* the depth system: `--paper-card #FBF6EC` on `--paper #F7F0E4` already reads as gently raised. No shadow needed.
- For more lift: a 1px `--line` hairline, or at most a **solid zero-blur** offset in low-alpha ink. Never a blurred elevation shadow.
- **Overlap for layering:** let a 1000px diagram or a pull-quote slab cross a hairline divider. Overlap is the one register-appropriate depth move — it reads as considered layout, not effect.
- **Consciously avoid** the entire blurred drop-shadow / elevation system (dropdown/modal/attention shadows) — all read as app chrome.

### A5. Finishing touches — a tiny, ruthless budget

The book's "add flare" menu is mostly a trap for this register. Our entire flair budget is **three moves**:
1. **One hairline-thin claret rule across the very top of the whole layout.** Instant FT/Economist masthead authority; near-zero effort; probably the single highest craft-per-effort move available.
2. **The custom claret link underline** (A2).
3. **One promoted pull-quote** — *"cost accrues by default; value accrues by design."* — as a Besley slab breaking to the 1000px width.

- **Corners:** square to near-square (0–2px radius). Generous radius = playful = wrong. Serious/formal = sharp.
- **Empty states count:** the meter at `¤0.0000` on load *is* an empty state — design it as a deliberate, elegant zero.
- **Consciously avoid:** icon/emoji bullet lists (SaaS feature-page tell), repeating background patterns, decorative shapes/maps, "selectable card" radios, playful multi-color controls.

### A6. Images — prefer none

An FT-register launch carries entirely on Besley + hairlines + ivory. If any figure is needed, **draw it at display size** in the hairline/ink line style (the triple-flow diagram, the territory map) — never shrink exported screenshots. No hero photography with overlays.

---

## PART B — The experience system (from *Laws of UX*)

### B1. Spend the entire novelty + singularity budget on TWO elements

Jakob's Law (be radically conventional in form) + Von Restorff (only the different thing is remembered, and *restraint* is required or emphasis self-dilutes). The reading spine — anchor nav, long-form scroll, pull-quotes — must be dead-conventional editorial, precisely so the two singular elements detonate:

1. **The self-metering pill.**
2. **The one pull-quote** (the thesis line).

Everything else near-monochrome and quiet. The idea is radical; the *reading experience* should feel like something the reader already trusts.

### B2. Peak–End architecture

The page is consciously built around two remembered moments:
- **Peak = the value-capture.** When the Monday Test completes and value ticks `0 → ¤0.0500`, the thesis becomes *felt*. Engineer this as the single most crafted beat on the page. This is the "wow."
- **End = the field invitation.** Recency makes the ending stick — close on agency and membership plus the leave-with line, never on the meter's running cost.
- **Guard the negative peak:** the cost meter is a low-grade negative signal by design. Keep it calm, modest, factual, non-blinking — operational transparency, never a guilt trip, or negativity bias will over-weight it.

### B3. The two-clock asymmetry (Doherty Threshold + purposeful friction)

The meter runs two clocks that pull opposite directions *on purpose*, and the contrast is the argument felt in the body:
- **Passive cost ticks < 400ms** of the triggering action (scroll, dwell, section entry) so metering feels live and causal — this is what makes "cost accrues by default" viscerally true.
- **The value-capture is deliberately NOT instant.** A short, weighted, purposeful beat (well within the 10s ceiling) so the one deliberate act feels *earned*, not a cheap increment. Speed for passive cost; gravity for deliberate value.
- **Diagram:** each step resolves < 400ms, whole reveal within a few seconds. Animate only to make a relationship legible, never for spectacle.

### B4. Minimize interactive choice (Hick's Law), maximize prose

Push richness into *prose* (unlimited, linear, self-paced); keep *interactive* choice minimal.
- **Nav:** mirror the narrative beats but present as a single linear reading path with an implied "keep going" default, not eight equal-weight jumps.
- **Monday Test:** a tiny, consistent answer set (3-point band), never a 7-point grid; large, well-spaced targets (Fitts's); three labeled result bands, not a raw score.
- Don't oversimplify to abstraction — **label the diagram's flows** (bare glyphs increase load).

### B5. Chunking, not counting (Miller's Law)

"Five functions," "three flows," "five questions" are chunking problems, not magic numbers. Group each into clearly-distinct visual chunks scannable in one pass. Present the diagram's three flows as three visually distinct chunks so working memory holds "three related things," not a tangle.

### B6. Progressive enhancement is doctrine (Postel's Law + Tesler's Law)

- The essay, the diagram (static fallback), and the five functions must be **fully readable with no JS**. The meter and live Monday-Test scoring are the *enhancement layer*, not load-bearing. A skeptical exec on a locked-down corporate browser still gets the whole argument.
- The Monday Test is the one input surface: liberal input — any order, partial answers, no gating, no scolding, no email, reveal result only when all five are in.
- **Tesler:** the discipline is genuinely complex; don't fake-simplify it into slogans. Absorb the complexity into the *artifacts* (the diagram holds the systemic relationships; the Monday Test compresses a real diagnostic into five answerable questions) so the reader doesn't carry it. The seven-word thesis is maximal, honest compression of the irreducible core.

### B7. The pill must be typographically native (Von Restorff / banner-blindness)

Bottom-right is a Fitts-perfect corner (an "infinite target") **but** it is exactly where cookie banners, chat widgets, and ads live — trained readers tune out chips there on sight. Resolve by rendering the meter as **part of the essay's own typography** (same faces, editorial, ledger-tape feel), so it reads as *the document metering itself*, not third-party chrome. Quiet low-frequency tick; no attention-grabbing motion.

---

## PART C — Ethics as a feature (Laws of UX, Ch. 12)

The book's final chapter is a catalog of behavior-shaping tricks this site must credibly refuse — and can, uniquely, *say* it refuses:

- **No** intermittent variable rewards, infinite scroll/loops, autoplay. The page is finite and bounded with a clear end; the one reward (value capture) is singular, predictable, reader-initiated.
- **No** vanity metrics, manufactured social obligation, or reciprocity loops.
- **No** manipulative defaults, pre-checked consents, or forced actions. The Monday Test is strictly opt-in.
- **Good friction, embraced:** the Monday Test is deliberate friction that promotes self-diagnosis — the kind the book endorses.
- Success metric is comprehension and a considered decision, **not** time-on-site or DAU.

**The meter is the ethical inverse of the dark pattern.** Dark patterns *hide* the extraction and manufacture compulsion; this mechanic turns operational transparency onto the medium itself and is **privacy-clean**: computed locally, no third-party analytics, no server logging, nothing leaves the device; the reader can see and clear their own session. The line the page thereby earns the right to print (already in spec §4): *"All metering is client-side and notional. No records leave this page. The records are yours, which is rather the point."* In a launch aimed at skeptical executives, **naming what you refuse to do** is itself the most trust-building, memorable move available — and only a page built on this thesis can honestly make it.

---

## PART D — The "wow through craft" shortlist (build priorities)

Highest-leverage moves, in rough priority. If we do only these well, the page reads as bespoke and serious:

1. **One hairline claret rule across the top of the layout** — masthead authority. *(A5)*
2. **Tighten Besley** (line-height ~1.05, −0.015em tracking); **track out Archivo caps** (+0.1em). *(A2)*
3. **Build every color as a warm HSL ramp**, saturation rising at the extremes, so the ivory reads warm and expensive. *(A1)*
4. **Depth from the two paper tones + overlap + hairlines only** — zero drop shadows. *(A4)*
5. **Hold the 680px measure + asymmetric section spacing** (much more space above a heading than below). *(A2, A3)*
6. **Editorial links, not buttons**; the only solid claret is the top rule. *(A2, A5)*
7. **The meter as a precision instrument, typographically native:** tabular right-aligned figures, an elegant `¤0.0000` empty state, label beside the number, quiet tick. *(A5, B7)*
8. **Engineer the value-capture as the page's crafted peak** with a deliberate weighted beat (the two-clock asymmetry), and **close on the field invitation** as the sticky end. *(B2, B3)*

### Global "consciously avoid" list
Gradients; blurred/elevation drop shadows; hero photos with overlays; decorative patterns/shapes/maps; icon-bullet feature lists; generous border radius; saturated multi-accent semantic color; justified body text; high-contrast solid SaaS buttons; any decorative animation; anything that makes the bottom-right pill read as a third-party widget.
