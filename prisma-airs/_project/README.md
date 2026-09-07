# Prisma AIRS AI Gateway — Docs Project

Working directory for the Prisma AIRS AI Gateway documentation initiative described in
[`prisma-airs-docs-mintlify-handoff-v2.md`](./prisma-airs-docs-mintlify-handoff-v2.md).

The `.html` file is a styled render of the same brief — no additional content.

## Layout

```
prisma-airs/
├── _project/      planning and control artifacts (this folder) — .md, never built
└── *.mdx          published pages for the "Prisma AIRS" docs.json version
```

`_project/` is excluded from the Mintlify build by the repo-root `.mintignore`.

That exclusion is load-bearing, and the reason is worth stating: **Mintlify parses `.md` as
well as `.mdx`, and omitting a file from `docs.json` navigation does not keep it out of the
build or out of the public exports** (`llms.txt` / `llms-full.txt`). Handoff §2 warns about
exactly this — "A page absent from navigation is not necessarily private" — and it was
confirmed here the hard way: `mint validate` reported a parse error inside the handoff
markdown before `.mintignore` existed.

Anything added to `_project/` inherits the exclusion. Anything added elsewhere does not.

| File | Purpose | Handoff ref |
|---|---|---|
| [`00-capability-register.md`](./00-capability-register.md) | What access/capability is verified vs. pending. The gate on everything else. | §6, INIT 1 step 1 |
| [`01-reader-journeys.md`](./01-reader-journeys.md) | Six reader journeys mapped onto the existing corpus; coverage and gap register. | §2, §4 |
| [`02-page-contracts.md`](./02-page-contracts.md) | Page types bound to this repo's Mintlify components and style guide. | §2 |
| [`03-provenance-model.md`](./03-provenance-model.md) | Page manifest schema, claim→section dependency index, where it is stored. | §2, §3, §5 |
| [`04-operator-questions.md`](./04-operator-questions.md) | The §11 questions, narrowed to what could not be answered from the repo. | §11 |
| [`05-naming-rules.md`](./05-naming-rules.md) | Portkey → Prisma AIRS vocabulary rule; what renames and what must not. | §2 |
| [`06-changelog-contribution-path.md`](./06-changelog-contribution-path.md) | The docs→KB MCP round trip, piloted on release changelogs. | §4, §5 |
| [`07-reconciliation-loop.md`](./07-reconciliation-loop.md) | The standing KB↔docs loop: triage tiers, runtime shape, echo protection. | §5, §9, §10 |
| [`08-openapi-handoff.md`](./08-openapi-handoff.md) | Instructions for the agent building the new Prisma AIRS OpenAPI spec. | §3, §2 |
| [`09-handoff-v3-feedback.md`](./09-handoff-v3-feedback.md) | Feedback on the brief itself, from implementing against it. For v3. | all |
| [`releases/`](./releases/) | Per-release assertion files, emitted by the `update-changelog` skill. | §4 |

## Scope

Confirmed 2026-09-07: **the whole corpus is Prisma AIRS AI Gateway, rebranded in place.**
The other tabs are modules of it, not separate products.

Migration runs through a third `navigation.versions[]` entry in `docs.json`, `"Prisma AIRS"`,
sitting between `"Latest"` and `"Virtual Keys (Deprecated)"`. `"Latest"` remains first and
therefore remains the default version.

Pages join the Prisma AIRS version one at a time, and only after passing the grounding gate.
Its page count is the INIT 1 progress metric.

## Status

**INIT 1 step 1 is blocked.** No authenticated Prisma AIRS KB MCP access has been
demonstrated from this workspace. Under handoff §3 rule 2, no substantive product
assertion may be published without accepted KB support, so page authoring cannot begin.

Handoff §6 explicitly permits the work that *is* done here: "Proceed with page contracts,
editorial standards, and local structure while access is pending. Do not claim integrated
success until a real authorized read/contribution/publication round trip is demonstrated."

No such round trip has been demonstrated.

`prisma-airs/overview.mdx` exists as a scaffold and deliberately carries **no product
capability claims** — it is navigation and branding only, which is the only kind of page that
can be written before KB access. It must not be merged to live docs without documentation-owner
review (Q7).
