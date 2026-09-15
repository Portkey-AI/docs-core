# PLAN.md — Prisma AIRS AI Gateway docs

Scope by phase. Completed work is struck through. The running checklist is
[`TODO.md`](./TODO.md); the canonical decision history is [`README.md`](./README.md).

**Status:** Phase 1 complete (2026-09-15, commits `b8a2b656` and `4dafb315`). Phase 2 is blocked
on the local OpenAPI specification.

## Directives understood

- Grounding gate is **lifted** for this initiative. Vrushank is the source and the factual reviewer. Manifests, claim ledger and the reconciliation loop are **parked**.
- Work stays inside this docs repo. No KB, no external source.
- ~~`prisma-airs/` is renamed to **`aigw/`** — folder, route, and `_project/` with it. The `docs.json` version label stays the string `"Prisma AIRS"`.~~
- Nothing in the Latest version is modified. No global find-and-replace.
- **Phase 1 copies pages as-is.** Phase 2 restructures and rebrands. Phase 3 does assets and the broader API surface.
- Tenancy vocabulary is **Organisation → Workspace → User/Machine**. Nothing else.
- Everything lands on `docs/prisma-airs-updates` (PR #1075).

## Assumptions

Judgements not stated by Vrushank. Correct any that are wrong. Those marked *held* were exercised in Phase 1 without issue.

1. *held* — **"Without a single line of change" governs page body prose**, and is overridden only by the four Phase-1 edits named below: nav removals and renames, image removal, link rewriting, and the minimum needed to keep `mint validate` green.
2. *held* — **Internal links are rewritten** to `/aigw/...` where the target page exists inside the aigw version. Links whose target was not carried over keep pointing at the root route, which resolves to the Latest version.
3. *held* — **Self-Hosting is its own top-level tab**, peer to Docs and Integrations.
4. *held* — **Support sits under the Help Center tab** as a group named "Support", holding only `common-errors-and-resolutions`. Articles is unchanged.
5. *held* — **Changelog keeps Enterprise Gateway and Data Service as direct pages**, with the "Enterprise Releases" group wrapper dropped rather than renamed.
6. *held* — **"Remove ALL screenshot images"** means every image reference and its `<Frame>` wrapper is deleted; surrounding prose stays, no placeholder is left behind. Frames wrapping an `<iframe>` or `<video>` are kept.
7. *held* — **Introduction renames are frontmatter only** (`title`, `sidebarTitle`). File paths mirror the root.
8. **Images stay in the shared `/images/` tree.** No duplicated `aigw/images/` — relevant from Phase 3.
9. **Redirects are not added** for aigw routes. These are new URLs with no inbound links.
10. *held* — **Phase 1 wires no OpenAPI binding at all.** The remote spec cannot be read from this environment, so generation is deferred entirely; Vrushank supplies the spec locally for Phase 2.
11. *held* — **`mint validate` green is the definition of done** for each slice, `mint broken-links` on any slice that adds cross-links.

---

## ~~Phase 1 — Carry over~~ ✅ Complete

429 pages across 7 tabs. Navigation and disk agree exactly: no orphaned files, no nav entries without a file. `mint validate` green.

**Preparation**
- ~~Rename `prisma-airs/` → `aigw/`, `_project/` included; update `.mintignore` to `aigw/_project/` and fix relative paths inside the planning docs.~~ Exclusion verified with a deliberately malformed probe file.
- ~~Fork `/snippets/` into an aigw-owned snippet set for the pages that import them.~~ Forked to `snippets/aigw/`, which is where Mintlify resolves snippets from. Shared Portkey snippets untouched.
- ~~Rewrite the `"Prisma AIRS"` version block in `docs.json`.~~

**Docs** — 149 pages
- ~~Introduction — Welcome (was What is Portkey?), Simple Request (was Make Your First Request), Features (was Portkey Features).~~
- ~~Product — Observability, AI Gateway, Model Catalog, MCP Gateway, Agent Gateway, Coding Agents, Guardrails, Administration, Enterprise Offering.~~
- ~~Product removals — Prompt Studio, Open Source, Feature Comparison.~~
- ~~Self-Hosting and Support leave the Docs tab.~~

**Integrations** — 253 pages
- ~~Everything, unchanged.~~

**Self-Hosting** — 11 pages, new top-level tab
- ~~Drop the "Hybrid Deployments" grouping level; its pages sit directly in the tab.~~
- ~~Rename Architecture → Overview.~~
- ~~Remove FIPS-Compliant Images and the Air-Gapped Deployments (Legacy) section.~~

**Gateway APIs and Admin APIs** — 9 and 2 pages
- ~~Both tabs carry **only their hand-written reference pages** — Gateway APIs keeps its API Reference group (introduction, agentic usage, supported providers, authentication, headers, error codes, response schema, config object, OpenAPI specification); Admin APIs keeps introduction and error.~~
- ~~**No operation pages.** None of the 219 stub `.mdx` files carried over, no OpenAPI binding wired.~~
- ~~Remove the SDK group.~~

**Changelog** — 2 pages
- ~~Remove Monthly Summary, Product Releases, SDK Releases.~~
- ~~Drop the Enterprise Releases group; keep Enterprise Gateway and Data Service only.~~

**Help Center** — 3 pages
- ~~Articles, unchanged.~~
- ~~Support — Common Errors and Resolutions only.~~

**Not carried over**
- ~~Cookbooks.~~
- ~~All API operation pages.~~

**Applied to every carried page**
- ~~Remove all screenshot images.~~ 523 references and their `<Frame>` wrappers; 3 Frames wrapping iframes kept.
- ~~Rewrite internal links per assumption 2.~~ 1,807 repointed to `/aigw/`.
- ~~Drop the `prisma-airs-cta` snippet.~~ Removed from all 416 importers.
- ~~Remove every link to Prompt Studio.~~ 50 `<Card>` blocks deleted, 16 prose links unwrapped, 2 emptied `<CardGroup>`s removed. Covers the legacy `/product/prompt-library` route, clearing 32 inherited broken links.
- ~~Leave `PORTKEY_API_KEY`, `x-portkey-*`, `api.portkey.ai` and all product naming exactly as they are.~~

---

## Phase 2 — Restructure and rebrand

Blocked on the local OpenAPI specification for the API reference work. Everything else can start.

**Naming**
- Product → Prisma AIRS AI Gateway on first mention, then the gateway / AI Gateway. Company → Palo Alto Networks. Management plane → Strata Cloud Manager.
- Functional identifiers never change: packages, imports, classes, constructors, config keys, JSON fields, `operationId`s, schema names, changelog repo names.
- `x-portkey-*` headers stay exactly as they are.

**Endpoints and auth**
- Retire `PORTKEY_API_KEY`; authenticate with the standard `Authorization` header.
- SaaS AI Gateway on SCM: `aigw.portkey.ai/v1`.
- MCP Gateway: `aigw.portkey.ai/m`.
- Agent Gateway: `aigw.portkey.ai/agent`.
- Everything else about the request contract is unchanged.

**Onboarding**
- Quickstarts and first-run flows move from `app.portkey.ai` to Strata Cloud Manager.

**Structure**
- Minor navigation restructure on top of the Phase 1 tree.
- Decide the licensing / module labels (Enterprise, Agent Gateway, Observability Suite, Guardrails Engine, Model Catalog, Prompt Studio) as public group headings or internal-only.
- Apply Organisation → Workspace → User/Machine throughout.

**API reference — narrow scope**
- Generate operation pages for Gateway APIs and Admin APIs from the **local** OpenAPI spec Vrushank supplies, via group-level `openapi` in `docs.json`. No stub `.mdx` files.
- Exclude prompt endpoints, and the Admin API Prompts / Prompt Partials / Prompt Labels / Prompt Collections groups.
- Operation page titles, ordering and grouping live in the spec via `x-mint`.
- Repoint the 185 `api-reference` links still resolving to the Latest version.

---

## Phase 3 — Assets and broader API scope

**API reference — broader scope**
- Everything beyond the narrow Phase 2 generation: full spec coverage, `x-mint.mcp` decisions, playground configuration, overlays.

**Assets**
- Prisma AIRS / Palo Alto Networks screenshot set captured and added back to the pages stripped in Phase 1.
- Logo lockup and any brand-specific visual elements.
- Diagrams redrawn where they carry Portkey branding.

**Inherited link debt**
- Roughly 76 pre-existing broken links copied in from the Portkey corpus (`integrations` 34, `product` 25, `self-hosting` 6, plus the legacy `provider-endpoints` and `portkey-endpoints` prefixes). Out of scope by "re-ground, do not inherit", but they now sit inside `aigw/` and will report against us in `mint broken-links`.
