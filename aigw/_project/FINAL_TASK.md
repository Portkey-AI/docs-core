# FINAL_TASK.md — Prisma AIRS AI Gateway docs

## Directives understood

- Grounding gate is **lifted** for this initiative. Vrushank is the source and the factual reviewer. Manifests, claim ledger and the reconciliation loop are **parked**.
- Work stays inside this docs repo. No KB, no external source.
- `prisma-airs/` is renamed to **`aigw/`** — folder, route, and `_project/` with it. The `docs.json` version label stays the string `"Prisma AIRS"`.
- Nothing in the Latest version is modified. No global find-and-replace.
- **Phase 1 copies pages as-is.** Phase 2 restructures and rebrands. Phase 3 does assets.
- Tenancy vocabulary is **Organisation → Workspace → User/Machine**. Nothing else.
- Everything lands on `docs/prisma-airs-updates` (PR #1075).

## Assumptions

Judgements not stated by Vrushank. Correct any that are wrong.

1. **"Without a single line of change" governs page body prose**, and is overridden only by the four Phase-1 edits named below: nav removals and renames, image removal, link rewriting, and the minimum needed to keep `mint validate` green.
2. **Internal links are rewritten** to `/aigw/...` where the target page exists inside the aigw version. Links whose target was not carried over keep pointing at the root route, which resolves to the Latest version.
3. **Self-Hosting becomes its own top-level tab** in the aigw version, peer to Docs and Integrations — that is what "its own new section" means.
4. **Support moves under the Help Center tab** as a group named "Support", holding only `common-errors-and-resolutions`. Articles is unchanged.
5. **Changelog keeps Enterprise Gateway and Data Service as direct pages**, with the "Enterprise Releases" group wrapper dropped rather than renamed.
6. **"Remove ALL screenshot images"** means every image reference and its `<Frame>` wrapper is deleted from aigw pages; surrounding prose stays, and no "image removed" placeholder is left behind.
7. **Introduction renames are frontmatter only** — `title` and `sidebarTitle`. File paths mirror the root (`aigw/introduction/what-is-portkey.mdx`).
8. **Images stay in the shared `/images/` tree.** No duplicated `aigw/images/` — moot in Phase 1 since images are removed, relevant from Phase 3.
9. **Redirects are not added** for aigw routes. These are new URLs with no inbound links.
10. **Phase 1 wires no OpenAPI binding at all.** The remote spec cannot be read from this environment, so generation is deferred entirely; Vrushank supplies the spec locally for Phase 2.
11. **`mint validate` green is the definition of done** for each slice, `mint broken-links` on any slice that adds cross-links.

---

## Phase 1 — Carry over

Copy the Docs, Integrations, Gateway APIs, Admin APIs, Changelog and Help Center surfaces into `aigw/` as-is, then apply the structural deletions below. No rebranding, no prose edits. Roughly 450 hand-copied pages, plus generated API pages.

**Preparation**
- Rename `prisma-airs/` → `aigw/`, `_project/` included; update `.mintignore` to `aigw/_project/` and fix relative paths inside the planning docs.
- Fork `/snippets/` into an aigw-owned snippet set for the pages that import them. The shared root snippets are Portkey-branded and belong to the Latest version — they are not edited.
- Rewrite the `"Prisma AIRS"` version block in `docs.json` against the tree below.

**Docs**
- Introduction — Welcome (was What is Portkey?), Simple Request (was Make Your First Request), Features (was Portkey Features).
- Product — Observability, AI Gateway, Model Catalog, MCP Gateway, Agent Gateway, Coding Agents, Guardrails, Administration, Enterprise Offering.
- Product removals — Prompt Studio, Open Source, Feature Comparison.
- Self-Hosting leaves the Docs tab. Support leaves the Docs tab.

**Integrations**
- Everything, unchanged.

**Self-Hosting** (new top-level tab)
- Drop the "Hybrid Deployments" grouping level; its pages sit directly in the tab.
- Rename Architecture → Overview.
- Remove FIPS-Compliant Images and the Air-Gapped Deployments (Legacy) section.

**Gateway APIs and Admin APIs**
- Both tabs ship in Phase 1 carrying **only their hand-written reference pages** — Gateway APIs keeps its API Reference group (introduction, agentic usage, supported providers, authentication, headers, error codes, response schema, config object, OpenAPI specification); Admin APIs keeps introduction and error.
- **No operation pages.** None of the 219 stub `.mdx` files are carried over, and no OpenAPI binding is wired. Operation pages arrive in Phase 2, generated from the local spec.
- Remove the SDK group.

**Changelog**
- Remove Monthly Summary, Product Releases, SDK Releases.
- Drop the Enterprise Releases group; keep Enterprise Gateway and Data Service only.

**Help Center**
- Articles, unchanged.
- Support — Common Errors and Resolutions only. Remove Upgrade to Model Catalog, How to Contribute, Contact Us, Developer Forum, December '23 Migration.

**Not carried over**
- Cookbooks.
- All API operation pages.

**Also applied**
- Every link to Prompt Studio removed from aigw pages, since the product surface is not carried over: 50 `<Card>` blocks deleted, 16 prose links unwrapped to plain text, 2 emptied `<CardGroup>`s removed. Covers both `/product/prompt-engineering-studio` and the legacy `/product/prompt-library` routes.

**Applies to every carried page**
- Remove all screenshot images.
- Rewrite internal links per assumption 2.
- Leave `PORTKEY_API_KEY`, `x-portkey-*`, `api.portkey.ai` and all product naming exactly as they are.

---

## Phase 2 — Restructure and rebrand

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

**API reference** — narrow scope
- Generate operation pages for Gateway APIs and Admin APIs from the **local** OpenAPI spec Vrushank supplies, via group-level `openapi` in `docs.json`. No stub `.mdx` files.
- Exclude prompt endpoints, and the Admin API Prompts / Prompt Partials / Prompt Labels / Prompt Collections groups.
- Operation page titles, ordering and grouping live in the spec via `x-mint`, since there are no stub files to carry them.
- Repoint the `api-reference` links still resolving to the Latest version.

---

## Phase 3 — Assets and broader API scope

**API reference — broader scope**
- Everything beyond the narrow Phase 2 generation: full spec coverage, `x-mint.mcp` decisions, playground configuration, overlays.

**Assets**
- Prisma AIRS / Palo Alto Networks screenshot set captured and added back to the pages stripped in Phase 1.
- Logo lockup and any brand-specific visual elements.
- Diagrams redrawn where they carry Portkey branding.
