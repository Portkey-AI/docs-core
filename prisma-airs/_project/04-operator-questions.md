# Operator questions

Handoff §11: "Ask only what remains needed after inspecting configured access."

Everything answerable from the repository has been answered in
[`00-capability-register.md`](./00-capability-register.md). What follows could not be.

Per §11, these are **not** on the table and are not asked: the choice of Mintlify, the public
audience, KB factual authority, two-way authoring, namespace placement, or other products.
No secrets in chat — use normally configured access.

---

## Answered — 2026-09-07

| # | Answer |
|---|---|
| **Q1** Scope | **(a)** The whole corpus is Prisma AIRS AI Gateway, rebranded in place. Other tabs are modules of it, not separate products. |
| **Q2** KB / MCP | Still open. Endpoint to be supplied. **This remains the blocker on all page authoring.** |
| **Q3** Naming rule | Approved as proposed in [`05-naming-rules.md`](./05-naming-rules.md), including the four items that document could not settle. |
| **Q7** Owners | Vrushank Vyas owns all four roles: factual review, editorial publication, conflicts, and urgent withdrawal. |
| **Q8** Virtual Keys version | **Keep as is.** Do not touch. |
| **Q9** Changelog publication policy | Approved: the release-only exception is correct. Changelog entries publish on the release schedule; guide and reference patches wait for KB acceptance. |

Standing instruction, 2026-09-07: **do not modify non-Prisma-AIRS docs.** Pre-existing issues
found while working — 66 broken links across 48 files, non-page files at the repo root inside
the build scope — are accepted as-is and are not to be fixed as part of this initiative.

Also decided: **the `prisma-airs-cta` snippet is not used anywhere in the Prisma AIRS version.**
It announces the Portkey → Prisma AIRS transition, which is redundant on pages that are already
Prisma AIRS.

Deferred by agreement: `mint a11y` and `mint test` will be adopted later.

---

## Blocking — nothing can be authored until Q2 is answered

Answered questions below are retained rather than deleted: the reasoning is why the answer
means what it means, and it is worth keeping next to the decision.

### Q1. What is the assigned Prisma AIRS AI Gateway scope in this repository?

> **ANSWERED 2026-09-07 — (a), whole corpus rebranded in place.** Retained for the reasoning.

This repo is the full Portkey documentation set: 2 navigation versions, 7 tabs, ~1,200 pages,
covering AI Gateway, MCP Gateway, Agent Gateway, Model Catalog, Prompt Studio, Guardrails,
Observability, Administration, Enterprise, and Self-Hosting.

The handoff scopes the work to "Prisma AIRS AI Gateway" and excludes other products. Those two
facts do not line up on their own. Which is it:

- **(a)** The whole repo *is* Prisma AIRS AI Gateway, rebranded in place — the other tabs are
  modules of it, not other products.
- **(b)** Only `product/ai-gateway/*` plus its onboarding and API surface is in scope; MCP
  Gateway, Agent Gateway, Prompt Studio etc. are separate products under §0's exclusion.
- **(c)** A new, separate Mintlify project — this repo stays as Portkey docs.

The internal RFP knowledge file leans toward **(a)** (it lists Agent Gateway, Observability,
Guardrails, Model Catalog and Prompt Studio as *modules* of Prisma AIRS AI Gateway), but that
is a sales artifact, not an operator instruction.

Everything downstream depends on this: coverage map, naming rules, page inventory, and how
much of the corpus needs re-grounding.

### Q2. Where is the Prisma AIRS KB, and what is the MCP contract?

No KB MCP server is configured for this project. Needed: endpoint, service identity, and the
tool contract for claim reads, public-approval/status fields, change discovery, contributions,
and task status.

The one MCP server configured here, `mcp-gateway`, timed out on connect and appears by name to
be Portkey's own MCP Gateway product rather than the KB. Please confirm either way.

Until this is answered, handoff §3 rule 2 blocks all page authoring.

### Q3. What is the product naming rule?

> **ANSWERED 2026-09-07 — approved as proposed.** Retained for the reasoning.

"Portkey" is the product name throughout the published prose. Needed: the term-by-term rule,
specifically what stays unchanged. The RFP knowledge file already draws this line for
customer-facing sales copy — confirm whether the same line applies to docs:

- Product name in prose → "Prisma AIRS AI Gateway"
- Functional identifiers unchanged → `portkey_ai`, `PORTKEY_*` headers, `api.portkey.ai`,
  `app.portkey.ai`, `x-portkey-*`
- Management plane → "Strata Cloud Manager"

Also: what happens to the open-source Gateway's identity, the Discord/GitHub community CTAs,
and `support@portkey.ai`?

---

## Near-term — needed before the vertical slice publishes

### Q4. What is the onboarding path for a Prisma AIRS customer?

`introduction/make-your-first-request` starts at `app.portkey.ai` signup. If AIRS customers
arrive through a Strata Cloud Manager tenant, the quickstart is wrong for the target reader
and the INIT 1 first-use exit criterion cannot pass. Which path is documented — or both?

### Q5. Is the SSO/SCIM documentation currently wrong?

The RFP knowledge file states that identity for Prisma AIRS AI Gateway is delivered by Strata
Cloud Manager / Common Services IAM and that `product/enterprise-offering/org-management/sso`
and `.../scim/*` are "not applicable." Those pages are live today.

If that is accurate this is published-and-incorrect content, not a documentation gap, and it
should be triaged ahead of new authoring. Needs a KB answer, not an RFP answer.

### Q6. Does the OpenAPI spec count as KB-accepted knowledge?

API reference is generated from `Portkey-AI/openapi` (external repo, validated in CI). Handoff
§3 rule 1 makes the KB the sole factual authority. Either the spec is ingested into the KB, or
it needs an explicit recorded exemption. Which?

### Q7. Who owns factual review, editorial publication, conflicts, and urgent withdrawal?

> **ANSWERED 2026-09-07 — all four roles: Vrushank Vyas.**

Four roles in the handoff, currently unassigned. Urgent withdrawal (§10) in particular needs a
named owner and an approved procedure that does not sit behind ordinary editorial review.

### Q8. Is the deprecated "Virtual Keys" navigation version in scope?

> **ANSWERED 2026-09-07 — keep as is, do not touch.**

It is a complete second published version. Keep, freeze, or retire?

---

## Deferred — needed for INIT 2, not INIT 1

- ~~**Q9.**~~ **ANSWERED 2026-09-07.** Release-only exception approved: changelog entries
  publish on the release schedule; guide and reference patches wait for KB acceptance.
- **Q10.** Which task/scheduler facilities, budgets, and notification channels should the
  reconciliation integration reuse? §6 says reuse existing; none are visible from here.
- **Q11.** Does the existing docs-ingestion pipeline preserve generated ancestry? §5 makes
  this an acceptance requirement — without it, recrawling published pages defeats loop
  protection.
- **Q12.** Launch-critical versions, environments (managed / hybrid / air-gapped), and
  languages. §0 DEFAULT is English only.
