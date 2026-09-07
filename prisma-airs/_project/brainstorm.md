# Brainstorm: what the Prisma AIRS AI Gateway docs should feel like

A design brainstorm, not a decision. Written 2026-09-07 alongside
[`brainstorm.html`](./brainstorm.html), a wireframe of the same ideas.

**Scope note.** Launch scope and the navigation skeleton are yours to design. So this is about
*presentation* — chrome, typography, page archetypes, component discipline, and the Mintlify
capability surface you have to design against. Where structure appears it is a worked example
to react to, not a proposal to adopt. Every label in the wireframe is a placeholder; none is a
grounded product claim.

Everything about Mintlify below was verified against the installed CLI **4.2.876** and the
current `docs.json`. Web access is blocked from this workspace, so treat version-specific
details as accurate for this CLI and worth confirming before relying on the fine points.

---

## 1. Four readers who want four different first pages

| Reader | Arrives asking | Fails when | Reads like |
|---|---|---|---|
| **Developer** | "How do I route a call through this?" | The first code block is 40 lines and needs a console visit first | Skims to the code, copies, runs, leaves |
| **Gateway admin** | "How do I provision, budget, and rotate safely?" | The page describes a feature instead of a procedure | Follows steps literally, needs to know it worked |
| **Security / governance owner** | "What can I enforce, and what evidence do I get?" | Controls are scattered across guardrails, admin, and enterprise sections | Wants coverage, not tutorials |
| **Evaluator / architect** | "What is this, where does it sit, what doesn't it do?" | Boundaries are missing and every page is a how-to | Reads three pages and forms a verdict |

These four cannot share a landing page that is a table of contents. A table of contents serves
whoever already knows the vocabulary — which is none of them on day one.

**The observation that should drive the design:** all four ask a variant of the same question —
*does this do what I need, and how fast can I see it for myself?* That is one design problem,
not four.

## 2. Three organising bets

### Bet 1 — the home page is a decision surface, not a directory

One screen, four doors, each labeled by intent rather than by artifact type. "Send your first
request" beats "Quickstart"; "Enforce a policy across every model" beats "Guardrails". Each
door leads to a path that reaches something **verifiable** in about two minutes — a response
body, a blocked request, a log entry, a diagram.

The measure of the home page is not how much it links to. It is how many readers reach a proof
without a second decision.

### Bet 2 — show the data path, everywhere

This is a product that sits *in* the request path. That is the whole mental model, and it is
spatial. One canonical diagram — request → policy evaluation → provider → response, with
observability tapping the middle — rendered light and dark, reused on every concept page with
the current subject highlighted.

"You are here" orientation is the single highest-leverage asset on a docs site for an
inline-infrastructure product, and it is cheap: one SVG pair, authored once. The corpus today
has 997 `<Frame>` instances, almost all product screenshots. Screenshots age badly and orient
nobody; one diagram does more work than a hundred of them.

Corollary: it is also the honest way to state boundaries. Anything outside the box on the
diagram is something the gateway does not do, shown rather than claimed.

### Bet 3 — treat the AI agent as a first-class reader

Mintlify gives you `llms.txt`, `llms-full.txt`, per-page markdown served to agents,
`markdown.instructions` (custom guidance appended to every agent-facing page), and
`contextual.options` for open-in-Claude / MCP / Cursor / VS Code. Currently four of those
options are enabled and `markdown.instructions` is unset.

For a product whose users are *building agents*, docs that agents consume well is both
on-brand and genuinely differentiating. Most vendor docs treat this as an export checkbox.
Concretely: set `markdown.instructions` to state the naming rule (the `PORTKEY_*` identifiers
that survive rebranding), the base URL, and the fact that examples use placeholder
credentials — so an agent reading one page in isolation does not hallucinate a rename.

This also feeds back into grounding. `llms-full.txt` is where an ungrounded assertion does the
most damage, because it is read without the surrounding page to qualify it.

---

## 3. The aesthetic levers, verified

Current value versus what I would reach for. All confirmed present in this CLI's schema.

| Lever | Now | Thought |
|---|---|---|
| `theme` | `mint` | Nine exist: `mint`, `maple`, `palm`, `willow`, `linden`, `almond`, `aspen`, `luma`, `sequoia`. Worth screenshotting all nine before defaulting. Theme changes chrome geometry, not just colour — cheapest large visual change available. |
| `colors` | primary/light/dark all `#0891B2` | **A real defect, not a preference.** `light` renders on dark backgrounds and `dark` on light; setting all three identical means neither mode gets a contrast-adapted accent. Needs the PANW palette with a genuinely lighter and darker variant. |
| `logo` | Portkey + PANW lockup, light/dark | Replace with the Prisma AIRS lockup. Set `logo.href` deliberately — the product page, not the docs home. |
| `fonts` | unset (system) | Splits into `heading` and `body`. PANW brand typography here is a large, cheap identity win; self-hosted `woff2` is supported, so no Google Fonts dependency. |
| `icons` | unset (`fontawesome`) | `lucide` and `tabler` are available. Lucide's lighter stroke reads better next to a security brand than FontAwesome's solid glyphs. Purely taste — but the corpus has 567 `<Icon>` uses, so it is a visible taste. |
| `background` | `{ decoration: "gradient" }` | `gradient` \| `grid` \| `windows`, plus a light/dark `image` pair. `grid` suits infrastructure products; gradient reads consumer-SaaS. |
| `styling.eyebrows` | `breadcrumbs` | Keep. With four reader paths, position matters more than section name. |
| `styling.codeblocks` | `system` | Accepts a named Shiki theme. Pinning one (rather than following light/dark) makes code the strongest fixed element on every page. Worth trying `dark` — permanently dark code blocks against a light page is a strong, deliberate look. |
| `banner` | Portkey webinar, dismissible | Types are `info` \| `warning` \| `critical` with a colour override. Reserve it: a banner that always says something says nothing. Real use is a migration notice or an incident. |
| `navbar` | 3 links, no primary | `primary` supports a typed button. One CTA — console sign-in, most likely. Typed `github` / `discord` link variants render properly rather than as text. |
| `footer` | socials + link columns | Already has a "For LLMs" column pointing at `llms.txt`. Genuinely good; keep it and make it more prominent. |
| `search.prompt` | unset | Free personality with zero cost. "Search the gateway docs…" beats the default. |
| `contextual.options` | copy, view, chatgpt, claude | Add `mcp`, `add-mcp`, `cursor`, `vscode`, and `download-spec` on API pages. `download-pdf` matters more than it looks — security reviewers circulate PDFs. |
| `thumbnails` | unset | Controls social/OG cards: appearance, background image, font family. Every shared docs link is currently an unbranded auto-card. Cheap, high visibility. |
| `interaction.drilldown` | `true` | Keep. Expanding a group lands on its overview instead of nothing. |
| `markdown.instructions` | unset | See bet 3. Probably the most underused key in the whole schema. |
| `api.params.expanded` | unset (`closed`) | Consider `all` on core endpoints. Collapsed parameters hide exactly what a developer came to read. `api.params.post` adds "post pills" to `ParamField` from arbitrary spec keys — a hook for surfacing `x-airs-*` metadata inline. |
| `seo.indexing` | `navigable` | Correct. Only navigable pages get indexed. |

### Navigation primitives available

The top level of `navigation` accepts exactly one of: `products`, `languages`, `versions`,
`tabs`, `dropdowns`, `anchors`, `groups`, `pages`. This repo uses `versions` — three of them,
which is why Prisma AIRS currently sits as a peer of "Latest" and "Virtual Keys (Deprecated)".

That was the right *insertion* while scaffolding. It is probably the wrong *destination*, since
Prisma AIRS is not a version of Portkey docs — it is the product. Worth deciding early: a
version switcher labelled "Prisma AIRS" quietly frames the whole corpus as a variant.

Rough shape of the tradeoff, for whichever you design toward:

- **`products`** — strongest separation, own sidebar and identity per product. Right if AI
  Gateway, MCP Gateway and Prompt Studio are sold and adopted separately.
- **`tabs`** — one product, several surfaces (Docs / API / Integrations). What Latest uses,
  with seven tabs, which is two or three too many.
- **`anchors`** — persistent icon rail beside the sidebar. Good for the two or three
  destinations every reader eventually needs (API reference, changelog, status).
- **`dropdowns`** — compact, hides structure. Best when the reader already knows the map.
- **`versions`** — reserve for actual product versions.

Groups also accept `openapi`, `tag`, `directory`, `expanded` and `icon`, which is how the API
reference stops being 219 hand-written stubs — see [`openapi-handoff.md`](./openapi-handoff.md).

---

## 4. Component discipline

Measured across the current corpus:

```
3005 <Card>      2166 <Tab>      997 <Frame>     842 <Accordion>    810 <Note>
 707 <Tabs>       686 <Step>     611 <CodeGroup>  567 <Icon>        517 <CardGroup>
 356 <Info>       267 <Update>   203 <Steps>      172 <AccordionGroup>
 122 <Warning>    118 <ResponseField>  93 <ParamField>  48 <Check>  43 <Expandable>
  40 <Tip>         4 <Tooltip>     1 <Columns>
```

Three things jump out.

**Card soup.** 3005 cards is roughly 2.5 per page. Cards are a navigational affordance; used
everywhere they become visual noise and the reader stops seeing them. Rule worth adopting: a
`<CardGroup>` appears at most twice per page — once as a hub, once as next steps — and never
as a substitute for prose.

**707 `<Tabs>` against 611 `<CodeGroup>`.** The style guide already says `CodeGroup` for
language variants, and the corpus does the opposite about half the time. `Tabs` hides content
from in-page search and from the agent-facing markdown; `CodeGroup` is understood as language
selection and syncs across the page. Worth enforcing in review rather than restating.

**Underused and worth reaching for:** `<Columns>` (once, in the whole corpus), `<Expandable>`
for nested response objects, `<Update>` for changelog entries — and `<Check>` at 48 uses, which
is the tell that quickstarts are skipping the verification step the page contract requires.
"How do you know it worked" deserves a distinct visual.

**One anti-pattern to name:** `<Accordion>` at 842 uses is often prose hidden because the page
is too long. Collapsing content does not shorten a page, it just makes it unsearchable by eye.
Accordions are for genuinely optional detail — alternate platforms, deep error tables.

**Also worth a linter, not a fix:** `product/ai-gateway.mdx` has `gsidebarTitle:` in its
frontmatter — a typo that has silently done nothing for however long. Mintlify ignores unknown
keys, so frontmatter mistakes are invisible. That is a good argument for validating frontmatter
against the page-contract schema in CI rather than trusting review.

---

## 5. Page archetypes

Six shapes cover almost everything. Wireframes for each are in `brainstorm.html`.

**Home** — the decision surface from bet 1. `mode: "custom"` or `"wide"`, no sidebar, four
intent doors above the fold, the data-path diagram below, then a strip of "if you only read
three pages" for evaluators.

**Quickstart** — prerequisites as a `<Check>` list before any command; one `<CodeGroup>`
carrying the full runnable example in each language, not a fragment per step; a **verification
block** that is visually distinct and shows the actual expected output; exactly one next step.
The current corpus's quickstarts mostly end at "you made a request" with nothing to compare
against.

**Concept** — the data-path diagram with this subject highlighted, then mechanism, then a
boundaries section that is a *required heading* and not an afterthought. Boundaries are the
most-skipped element of the page contract and the most valuable to evaluators.

**API reference** — generated from the spec, three-column with a persistent request/response
panel. `expanded: "all"` on core endpoints. The `<Panel>` slot is currently unused anywhere in
the corpus and it is exactly what an API page wants.

**Admin runbook** — the archetype the corpus is missing entirely. Not a feature page:
`<Steps>` with a verification per step, a rollback section, and a "what breaks if you get this
wrong" callout. Key rotation, budget breach, provider failover, guardrail false-positive
triage. Admins are the reader most poorly served today.

**Troubleshooting** — indexed by the symptom *as a reader would type it*, not by subsystem.
`<Accordion>` earns its place here: one per symptom, expanded on anchor link, so a support
engineer can send a deep link.

---

## 6. What I would deliberately not do

- **No dashboard screenshots as primary explanation.** They are the fastest-rotting asset on
  the site and they orient nobody who has not already logged in. Diagrams for mechanism,
  screenshots only for "click this specific thing".
- **No feature-per-page inventory as the top-level structure.** It reads as a price sheet and
  serves the org chart rather than the reader.
- **No permanent marketing banner.** Spending the one attention slot on something evergreen
  means it is unavailable when something urgent happens — which is exactly §10's withdrawal
  scenario.
- **No custom React until a native component has been ruled out.** The handoff is explicit, and
  the component inventory above shows there is a lot of unused native surface first.
- **No inherited prose, however good it looks.** Restating the rule because a redesign is
  precisely when "we'll just restyle the existing pages" becomes tempting.

## 7. Sequencing

Cheap and independent of KB access — could ship this week:

1. Colours (fix the light/dark defect), logo, fonts, favicon, theme choice.
2. `search.prompt`, `thumbnails`, `contextual.options`, `markdown.instructions`.
3. Retire the inherited banner; leave the slot empty.
4. The data-path diagram, light and dark. One asset, largest single effect.
5. Component rules written into the page contracts and enforced in review.

Blocked on your skeleton: navigation primitive, tab count, home page composition.

Blocked on KB access (Q2): every word of body copy on every page.

Worth noting the ordering is deliberate — the visual identity work is entirely ungrounded-safe,
because none of it makes a product claim. It is the one substantial thing that can proceed at
full speed while authoring is blocked.

## 8. Open questions for you

1. **Version or product?** Should Prisma AIRS stay a `versions[]` entry, or become the site —
   with Portkey-branded content retired or moved? This determines whether readers see a version
   switcher, and it is the largest presentation decision on the list.
2. **Brand latitude.** How closely must this track PANW brand — exact palette and type, or a
   docs-appropriate interpretation?
3. **Is there a console sign-in URL** worth a navbar primary button at launch?
4. **Do security reviewers need PDF export?** `download-pdf` is one line, but it changes how
   pages should be written — a page assuming hover states and live links reads badly on paper.
5. **Do the four readers above match how the product is actually sold?** I derived them from
   the corpus and the RFP artifact, which is a sales document rather than a KB source, so this
   is the assumption most likely to be wrong and cheapest to correct now.
