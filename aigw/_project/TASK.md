# TASK.md — Prisma AIRS AI Gateway docs build-out

Working file for the current push: writing `.mdx` pages into `prisma-airs/`, wiring navigation
in `docs.json`, and everything downstream of that.

**How this file works.** Section 1 is what I established by reading the repo — you do not need
to restate any of it. Section 2 is what I need *from you*; answer inline under each question.
Section 3 is yours to fill with the navigation skeleton and the task list. Section 4 is the
working agreement I will follow unless you overwrite it.

Companion documents, already read, not duplicated here:
[`README.md`](./README.md) (canonical brief and decisions),
[`prisma-airs-docs-mintlify-handoff-v2.md`](./prisma-airs-docs-mintlify-handoff-v2.md) (source brief),
[`openapi-handoff.md`](./openapi-handoff.md), [`brainstorm.md`](./brainstorm.md).

Created 2026-09-15. Branch: `docs/prisma-airs-updates` (PR #1075 umbrella).

---

## 1. Established — do not re-explain

**Current state of the Prisma AIRS surface.** One published page, `aigw/overview.mdx`,
a deliberate scaffold with zero product-capability claims. It is registered in `docs.json` under
`navigation.versions[]` → `"Prisma AIRS"` → tab `"Docs"` → group `"Introduction"`, a single-entry
group sitting between "Latest" and "Virtual Keys (Deprecated)". "Latest" stays first and stays
the default.

**What I will carry over from the brief without asking.** Naming rules (product names rename,
functional identifiers never do — packages, classes, env vars, `x-portkey-*` headers, hostnames,
config keys, `operationId`s, repo names); no global find-and-replace, ever; no
`prisma-airs-cta` snippet inside this version; `<CodeGroup>` not `<Tabs>`; the per-type page
contracts, with boundaries on concept pages and verification on quickstarts treated as required
rather than optional; deployment invariance, so no managed-vs-hybrid page forks; `_project/`
stays build-excluded via the repo-root `.mintignore`, and anything I add outside it is public.

**Standing prohibition I will respect.** Do not modify non-Prisma-AIRS docs. Defects in the
Portkey-branded corpus are out of scope by construction, not backlogged.

**The one thing that has to be resolved before I write a single substantive page.** The brief
says page authoring is blocked: §3 rule 2 forbids publishing substantive assertions without
accepted KB support, Q2 (KB endpoint) is parked, and rule 7 says published docs never
corroborate their own claims. Your request — mirror the Portkey AI Gateway docs for Prisma
AIRS — is mostly re-expression of the existing corpus, which rule 7 and "re-ground, do not
inherit" specifically rule out as a source. **That is Q0 below.** I am not asking you to
re-argue it; I am asking you to state which regime is in force so I do not either stall on a
gate you have lifted or publish under one you have not.

---

## 2. Context I need from you

### Q0 — Grounding regime (blocking for substantive pages, nothing else)

Which is true for this push? Pick one and say it plainly:

- **(a) Gate lifted, you are the source.** You review for factual accuracy; I write from the
  existing corpus plus your direction. Rule 7 stands down for this initiative and the README's
  "Status" section gets rewritten to say so.
  Vrushank - Yes, we are lifting the gate for this TASK.
- **(b) Gate lifted for a named page set only** — e.g. structural, navigational and conceptual
  pages — while numbers, defaults, limits and code contracts still wait for the KB.
  Vrushank - No, everything is fair game and we will drive changes for everything that I propose.
- **(c) Gate stands, KB access is arriving.** Give me the endpoint/auth and I work behind it.
Vrushank - For now, no - we will exclusively work on this docs repo only.

Also: if (a) or (b), do manifests and the claim ledger still get produced, or are they parked
with the loop until KB access lands? I would rather park them than write provenance that points
at nothing.

**Your answer:**

### Q1 — Mirroring fidelity

"Mirroring the Portkey AI Gateway docs" can mean several quite different jobs. Which?

- Structural clone — same routes, same page set, renamed and re-toned.
- Curated subset — a deliberately smaller Prisma AIRS surface, chosen page by page.
- Restructure — Portkey content as raw material for a navigation tree you have redesigned.

If it is the third, Section 3 is where the tree goes and it overrides everything.

Vrushank - Curated subset with minor restructure. But it will be in phases. Phase 1: Just curated subset. Phase 2: Minor resturcture.

**Your answer:**

### Q2 — Route shape and the version-vs-product question

Every Prisma AIRS page today lives under `prisma-airs/`. At scale, do pages stay under that one
prefix (`prisma-airs/product/ai-gateway/fallbacks`), or do they mirror the Portkey tree at the
repo root inside the version?

Vrushank - They will only stay under prisma-airs. Every page will be mirrored. However, before we begin I want you to change the route and the folder name to "aigw"

The README flags the revisit trigger as **route stability, not page count** — moving from
`navigation.versions[]` to `products` or `tabs` later rewrites every route and needs a redirect
per published page. This push is exactly the "first substantial batch" that makes the switch
expensive. So: stay on `versions[]`, or switch now, before the routes acquire inbound links?

Vrushank - We absolutely do not intent to do rewrites. We will publish a completely new set of docs, mdx under the "aigw" folder, mirroring the current structure at root broadly, with a new OpenAPI reference then the one we use there.

**Your answer:**

### Q3 — Batch scope and sequencing

How much is landing in this push, and in what order? Name the first slice concretely — the
smallest set you would actually want reviewed and merged together. I will work in that unit and
keep `mint validate` green at every commit.

Phase 1: We will carry over - Docs, Integrations, Gateway APIs, Admin APIs, Changelog, Help Center - AS IS,  WITHOUT A SINGLE LINE OF CHANGE.

**Your answer:**

### Q4 — Product vocabulary conflicts

Two unresolved from the README, both of which will show up in the first ten pages I write and
both of which are cheap to answer now and expensive to change later:

- **Tenancy.** The RFP knowledge file describes Organisation → Department → Team →
  User/Application. The docs describe organizations and workspaces. Which vocabulary is public?

Vrushank - It is ONLY Organisation --> Workspace --> User/Machine

- **Licensing / module labels.** Enterprise, Agent Gateway, Observability Suite, Guardrails
  Engine, Model Catalog, Prompt Studio — these only partly match the navigation groups. Are
  these public names I should use as group headings, or internal ones?

Vrushank - For now, we will push everything as is in Phase 1. 

Also confirm: management plane is **Strata Cloud Manager** in prose, and onboarding runs through
it rather than through `app.portkey.ai` — but the existing quickstarts are all `app.portkey.ai`.
What URL, console name, and first-run flow do the Prisma AIRS quickstarts describe?

Vrushank - Good call out. We will change everything to Strata Cloud Manager of course. Park it for Phase 2.

**Your answer:**

### Q5 — Code samples, endpoints, and credentials

The naming rule says hostnames and headers do not change, so samples keep `api.portkey.ai`,
`PORTKEY_API_KEY`, `x-portkey-*`. Confirm that holds for Prisma AIRS pages, or give me the
substitutes. If there is a Prisma AIRS base URL or an SCM-issued key format, I need it before
writing any quickstart, because that is the one thing a reader copies verbatim.

Vrushank - We should change some of these - retire Portkey_API_Key and only use the standard Authorization header. x-portkey-* headers actually stay as they are, and importantly, the SaaS AI Gateway on SCM is hosted on aigw.portkey.ai/v1 everything else remains the same. Similarly, the MCP Gateway is on the same path but on aigw.portkey.ai/m and agent gateway is aigw.portkey.ai/agent - remember this is all Phase 2.

**Your answer:**

### Q6 — Assets

New pages will want images. Is there a Prisma AIRS / Palo Alto screenshot set and logo lockup
to draw from, or do Prisma AIRS pages ship text-only for now? Reusing Portkey-branded product
screenshots under a Prisma AIRS heading is the obvious wrong answer; I want to know which right
answer you want.

Vrushank - Phase 3. Remove ALL screenshot images as part of Phase 1 though.

**Your answer:**

### Q7 — Review and merge mechanics

Everything lands on `docs/prisma-airs-updates` as one growing PR, or one PR per slice off that
branch? And do you want me to commit as I go, or stage work and let you review before each
commit?

Vrushank - Everything lands on that same PR.

**Your answer:**

### Q8 — Anything the repo cannot tell me

Launch date or external commitment driving the schedule; audiences or customers these pages are
for; anything explicitly out of bounds. Free-form.

Vrushank - No you have everything.

**Your answer:**

---

## 3. Structure and tasks — yours

> Add the navigation skeleton and the task list here. The README reserves both to you
> ("Launch scope and navigation skeleton are reserved to Vrushank … Do not propose a navigation
> tree or page inventory"), so I have left this genuinely empty rather than seeding it with a
> guess. Any format is fine — a tree, a table, a checklist. I will work top to bottom unless
> you mark priorities.

### 3.1 Navigation skeleton

PHASE 1:

- Docs
  - Introduction
    - Welcome (renamed from What is Portkey?)
    - Simple Request (renamed from Make Your First Request)
    - Features (renamed from Portkey Features)
  - Product
    - Observability
    - AI Gateway
    - Model Catalog
    - MCP Gateway
    - Agent Gateway
    - Coding Agents
    - Guardrails
    - Administration
    - Enterprise Offering
    REMOVE: Prompt Studio, Open Source, Feature Comparison
    Change: Self-hosting section will move to its own new section. Support will fully move under Help Center
- Integrations
  - Everything will stay as is
- Self-Hosting
  - Remove top-level "Hydrid Deployments" grouping. Rename "Architecture" to "Overview"
  - REMOVE: FIPS-Compliant Images and Air-gapped Deployments section altogether. 
- Gateway APIs 
  - Remove SDKs section. Everything else remains as is. 
- Admin APIs
  - Everything stays as is
- Changelog
  - REMOVE: Monthly summary, Product Releases, SDK Releases
  - REmove "Enterprise Releases" as a group and keep Enterprise Gateway and Data Service only.
- Help Center
  - Support
    - Remove: Upgrade to Model Catalog, How to Contribute, Contact Us, Developer Forum, December '23 Migration. Only keep Common Errors and Resolutions
    - Keep: Articles as is.

### 3.2 Task list

- Create a new FINAL_TASK.md file with ONLY PHASE 1 Scope, PHASE 2 Scope, PHASE 3 Scope, and nothing ELSE. At the top, in very short bullet points note a few of the core directives you have understood and EVERY ASSUMPTION YOU HAVE MADE, add it under a separate ASSUMPTIONS module at the top.

---

## 4. Working agreement

Unless you say otherwise, for every page I write:

1. Frontmatter valid, page registered in `docs.json`, route matching the Q2 decision.
2. `mint validate` run and green before I report a slice done — it exits non-zero on warnings,
   so a clean run is the real check. `mint broken-links` on any slice that adds cross-links.
3. Page contract satisfied for the page's type; boundaries on concepts, verification on
   quickstarts.
4. Code samples complete and runnable, safe placeholders, never a real credential, every block
   titled so `CodeGroup` renders a usable tab label.
5. No edits outside `prisma-airs/`, `docs.json`, and `aigw/_project/` without asking.
6. No global find-and-replace. The migration unit is a page.
7. I flag rather than invent. A fact I cannot source becomes a question in this file, not a
   confident sentence on a page.

Vrushank - Yes this all sounds good.

I will keep this file current as decisions land, and fold anything durable back into
[`README.md`](./README.md) so the canonical document stays canonical.
