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
10. **Both API tabs ship in Phase 1**, generated from the existing remote OpenAPI spec. Only the new Prisma AIRS spec is deferred to Phase 2 — the tabs themselves are not. Prompt operations are excluded by tag filter, not by editing the spec.
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

**Gateway APIs**
- Ships in Phase 1, bound to the **existing** remote spec at `docs.json` → `api.openapi`. What moves to Phase 2 is the replacement spec, not the tab.
- Generate operation pages via group-level `openapi` in `docs.json`. **None of the 219 stub `.mdx` files are carried over** — only the hand-written reference pages.
- Remove the SDK group.
- Exclude prompt endpoints.

**Admin APIs**
- Ships in Phase 1. Same generation model and same existing spec as Gateway APIs.
- Remove the Prompts, Prompt Partials, Prompt Labels and Prompt Collections groups.
- Everything else unchanged.

**Changelog**
- Remove Monthly Summary, Product Releases, SDK Releases.
- Drop the Enterprise Releases group; keep Enterprise Gateway and Data Service only.

**Help Center**
- Articles, unchanged.
- Support — Common Errors and Resolutions only. Remove Upgrade to Model Catalog, How to Contribute, Contact Us, Developer Forum, December '23 Migration.

**Not carried over**
- Cookbooks.

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

**API reference**
- Bind the generated API pages to the new Prisma AIRS OpenAPI specification in place of the current remote spec.
- Operation page titles, ordering and grouping move into the spec via `x-mint`, since there are no stub files to carry them.

---

## Phase 3 — Assets

- Prisma AIRS / Palo Alto Networks screenshot set captured and added back to the pages stripped in Phase 1.
- Logo lockup and any brand-specific visual elements.
- Diagrams redrawn where they carry Portkey branding.
