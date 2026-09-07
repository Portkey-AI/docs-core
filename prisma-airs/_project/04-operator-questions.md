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
| **Q4** Onboarding path | Onboarding is through **Strata Cloud Manager**. The documented detail waits for the KB — not an operator call. |
| **Q5** SSO/SCIM correctness | **Moot.** Those pages are Portkey-docs content. Prisma AIRS docs are built by re-grounding, not by inheriting. |
| **Q6** OpenAPI spec | A **new OpenAPI repo** will be supplied and is the source for Prisma AIRS API reference. The current `Portkey-AI/openapi` is not. |
| **Q11** Generated ancestry | Confirmed as a **hard prerequisite**, not INIT 2 hardening. Ingestion must refuse generated-ancestry content as corroborating evidence. |
| **Q12** Environments | **Managed and hybrid.** Product behaviour does **not** vary by deployment — see the note below. Language scope unchanged (English). |
| **Q13** Change discovery | Downgraded to a performance detail. Reconcile against manifests; treat a cursor as an optional read-narrowing optimization. |

Standing instruction, 2026-09-07: **do not modify non-Prisma-AIRS docs.** Pre-existing issues
found while working — 66 broken links across 48 files, non-page files at the repo root inside
the build scope — are accepted as-is and are not to be fixed as part of this initiative.

Generalized 2026-09-07, from the Q5 answer: **defects in the Portkey-branded corpus are out of
scope entirely.** Not deferred, not backlogged — out of scope. Prisma AIRS pages are produced
by re-grounding against the KB, so a wrong statement in a Latest-version page is never
inherited and never needs fixing on the way through. Do not open triage work against it.

**Deployment invariance (Q12).** The product behaves the same whether managed or hybrid.
Deployment is described plainly where it is relevant and is not a variant axis for content.
The consequence for [`03-provenance-model.md`](./03-provenance-model.md): `applies_to` does not
need to fan out per environment, there are no environment-variant page sets, and the coverage
ledger stays one-dimensional. This is a large simplification — do not reintroduce environment
branching without a specific reason.

**Launch scope is reserved.** Vrushank hand-designs the docs skeleton, reusing and improving
the Portkey structure. Do not propose a navigation tree or page inventory. Come back for it.

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

> **ANSWERED 2026-09-07 — Strata Cloud Manager, with the detail deferred to the KB.**
> Onboarding runs through SCM. The specifics of the documented path are a KB question, not an
> operator one, and are not to be inferred from the existing `app.portkey.ai` quickstart.

`introduction/make-your-first-request` starts at `app.portkey.ai` signup, which is a
Portkey-corpus artifact and is not inherited.

### Q5. Is the SSO/SCIM documentation currently wrong?

> **MOOT 2026-09-07.** The pages in question belong to the Portkey-branded corpus. Prisma AIRS
> documentation is produced by re-grounding against the KB, not by inheriting and correcting
> existing prose, so a wrong statement there is never carried forward. No triage required.
>
> Generalizes: see the out-of-scope rule in the answered section above.

### Q6. Does the OpenAPI spec count as KB-accepted knowledge?

> **ANSWERED 2026-09-07 — a new OpenAPI repository will be supplied and is the source for
> Prisma AIRS API reference.** `Portkey-AI/openapi`, which currently feeds `docs.json`'s
> `api.openapi` setting, is Portkey-corpus tooling and is not the Prisma AIRS source.

Still to settle when that repo arrives, because the answer names a source rather than a
grounding status: is the new spec **ingested into the KB** so its assertions are accepted
knowledge, or does it carry a **recorded exemption** as an authored artifact under §3 rule 1?
Either is coherent. Leaving it unstated is not — API reference is a large body of substantive
assertions, and it is the easiest place for grounding to lapse without anyone noticing.

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
  **Open and under active discussion** — a proposal is recorded in
  [`07-reconciliation-loop.md`](./07-reconciliation-loop.md#q10--scheduler-budgets-and-notifications).
  The substantive item is not the scheduler but the single-owner review queue.
- ~~**Q11.**~~ **ANSWERED 2026-09-07 — hard prerequisite, confirmed.** Ingestion must mark
  crawled documentation as generated and the confidence model must refuse it as corroborating
  evidence. Preservation of the metadata alone is insufficient; refusal is the requirement. The
  reconciliation loop must not run against production KB until this is verified. Verification
  is a KB-team question and rides with Q2.
- ~~**Q12.**~~ **ANSWERED 2026-09-07.** Managed and hybrid. Product behaviour is deployment-
  invariant. English only. Launch scope and skeleton reserved to Vrushank.
- ~~**Q13.**~~ **ANSWERED 2026-09-07 — downgraded.** Reconcile against the manifests
  regardless of what the KB offers; `claim_revision_seen` is already the stored previous
  snapshot. A cursor, if one exists, narrows which claims to re-read and is never the source of
  truth — §5's "an empty queue is not evidence of synchronization" applies to cursors, since a
  cursor is a queue. Rationale in
  [`07-reconciliation-loop.md`](./07-reconciliation-loop.md#kb--docs).
