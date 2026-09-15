# TODO.md — Prisma AIRS AI Gateway docs

Running checklist. Scope and rationale live in [`PLAN.md`](./PLAN.md); the canonical decision
history is [`README.md`](./README.md).

Branch `docs/prisma-airs-updates`, PR #1075. Last updated 2026-09-15.

---

## Phase 1 — Carry over ✅ Complete

Commits `b8a2b656` and `4dafb315`. 429 pages, 7 tabs, `mint validate` green.

- [x] ~~Rename `prisma-airs/` → `aigw/`, `_project/` included~~
- [x] ~~Update `.mintignore` to `aigw/_project/` and verify exclusion with a malformed probe file~~
- [x] ~~Fix `prisma-airs/` path references in the planning docs and the update-changelog skill~~
- [x] ~~Rebuild the `"Prisma AIRS"` version block in `docs.json`~~
- [x] ~~Docs tab — Introduction (3) and Product (146), minus Prompt Studio, Open Source, Feature Comparison~~
- [x] ~~Rename Introduction pages — Welcome, Simple Request, Features~~
- [x] ~~Integrations tab — 253 pages, unchanged~~
- [x] ~~Self-Hosting tab — promoted to top level, Hybrid Deployments level removed, Architecture → Overview, FIPS and Air-Gapped removed~~
- [x] ~~Gateway APIs tab — 9 hand-written reference pages, SDK group dropped~~
- [x] ~~Admin APIs tab — introduction and error~~
- [x] ~~Changelog tab — Enterprise Gateway and Data Service only~~
- [x] ~~Help Center tab — Articles, plus Support holding Common Errors and Resolutions~~
- [x] ~~Retire the `overview.mdx` scaffold~~
- [x] ~~Strip all 523 images and their `<Frame>` wrappers, keeping the 3 that wrap iframes~~
- [x] ~~Drop `prisma-airs-cta` from all 416 importers~~
- [x] ~~Fork remaining snippets to `snippets/aigw/`~~
- [x] ~~Repoint 1,807 internal links to `/aigw/`~~
- [x] ~~Remove every Prompt Studio link — 50 Cards, 16 prose links, 2 emptied CardGroups~~
- [x] ~~Fix the 4 validation warnings caused by the image strip~~

---

## Phase 2 — Restructure and rebrand

**Blocked:** the API reference items need the local OpenAPI spec from Vrushank. Everything else is ready to start.

**Naming**
- [ ] Product → Prisma AIRS AI Gateway on first mention, then the gateway / AI Gateway
- [ ] Company → Palo Alto Networks
- [ ] Management plane → Strata Cloud Manager
- [ ] Verify no functional identifier was touched — packages, imports, classes, config keys, JSON fields, `operationId`s, schema names, changelog repo names
- [ ] Confirm `x-portkey-*` headers left intact

**Endpoints and auth**
- [ ] Retire `PORTKEY_API_KEY` in favour of the standard `Authorization` header
- [ ] Base URL → `aigw.portkey.ai/v1` for the SaaS AI Gateway on SCM
- [ ] MCP Gateway → `aigw.portkey.ai/m`
- [ ] Agent Gateway → `aigw.portkey.ai/agent`

**Onboarding**
- [ ] Move quickstarts and first-run flows from `app.portkey.ai` to Strata Cloud Manager

**Structure**
- [ ] Minor navigation restructure on top of the Phase 1 tree
- [ ] Decide licensing / module labels as public headings or internal-only
- [ ] Apply Organisation → Workspace → User/Machine throughout

**API reference — narrow scope** *(blocked on spec)*
- [ ] Wire group-level `openapi` in `docs.json` against the local spec
- [ ] Exclude prompt endpoints and the Admin API Prompts / Prompt Partials / Prompt Labels / Prompt Collections groups
- [ ] Set operation page titles, ordering and grouping via `x-mint` in the spec
- [ ] Repoint the 185 `api-reference` links still resolving to the Latest version

---

## Phase 3 — Assets and broader API scope

**API reference — broader scope**
- [ ] Full spec coverage beyond the narrow Phase 2 generation
- [ ] `x-mint.mcp` — decide which operations become agent-callable tools
- [ ] Playground configuration and overlays

**Assets**
- [ ] Capture the Prisma AIRS / Palo Alto Networks screenshot set
- [ ] Restore images to the pages stripped in Phase 1
- [ ] Logo lockup and brand-specific visual elements
- [ ] Redraw diagrams that carry Portkey branding

**Inherited link debt**
- [ ] Clean the ~76 pre-existing broken links copied in from the Portkey corpus
- [ ] Decide what to do with the 33 links pointing at content dropped by design (guides 25, support 8)

---

## Appendix — intake decision record

The questions that set this work up, with Vrushank's answers as given. Preserved because these
are the source of the decisions in `PLAN.md`; nothing here is an open question.

**Q0 — Grounding regime.** Gate lifted for this task; everything is fair game. Work stays in this
docs repo only. Manifests and the claim ledger are parked.

**Q1 — Mirroring fidelity.** Curated subset with minor restructure, in phases. Phase 1 curated
subset, Phase 2 minor restructure.

**Q2 — Route shape.** Pages stay under one prefix, renamed from `prisma-airs` to `aigw`. No
rewrites of existing routes — a completely new set of docs under `aigw/`, mirroring the current
structure broadly, with a new OpenAPI reference. Version label stays "Prisma AIRS".

**Q3 — Batch scope.** Phase 1 carries Docs, Integrations, Gateway APIs, Admin APIs, Changelog and
Help Center as-is, without a single line of change.

**Q4 — Product vocabulary.** Tenancy is only Organisation → Workspace → User/Machine. Licensing
labels: push everything as-is in Phase 1. Strata Cloud Manager rename parked for Phase 2.

**Q5 — Code samples and endpoints.** Retire `PORTKEY_API_KEY`, use the standard `Authorization`
header. `x-portkey-*` headers stay as they are. SaaS AI Gateway on SCM is `aigw.portkey.ai/v1`,
MCP Gateway `aigw.portkey.ai/m`, Agent Gateway `aigw.portkey.ai/agent`. All Phase 2.

**Q6 — Assets.** Phase 3. Remove all screenshot images as part of Phase 1.

**Q7 — Review and merge.** Everything lands on the same PR.

**Q8 — Anything else.** Nothing further.

**Later amendments.** Cookbooks dropped. Prompt Studio removed from Docs, Admin APIs and Gateway
APIs alike. Snippets forked rather than shared. Narrow API scope moved to Phase 2 and broader
scope to Phase 3, once it emerged that the remote spec is unreadable from this environment and a
local spec would be supplied instead.

---

## Working agreement

1. Frontmatter valid, page registered in `docs.json`, route under `aigw/`.
2. `mint validate` run and green before a slice is reported done. `mint broken-links` on any slice that adds cross-links.
3. Page contract satisfied for the page's type; boundaries on concepts, verification on quickstarts.
4. Code samples complete and runnable, safe placeholders, never a real credential, every block titled so `CodeGroup` renders a usable tab label.
5. No edits outside `aigw/`, `docs.json`, `snippets/aigw/`, and `.mintignore` without asking.
6. No global find-and-replace. The migration unit is a page.
7. Flag rather than invent. A fact that cannot be sourced becomes a question here, not a confident sentence on a page.
