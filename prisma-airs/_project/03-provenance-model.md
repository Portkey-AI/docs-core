# Provenance and dependency model

Handoff §2 ("Identity and provenance"), §3, §5.

## Requirement

Every page carries a stable ID, assigned route, page type, owner, applicability, lifecycle
state, and source revision. Claims are tracked at **section/assertion** granularity so that
a change to one fact patches one section instead of rewriting the page.

## Privacy constraint — decide before writing any manifest

Handoff §2: "Keep operational manifests private and outside Mintlify's public exports. A page
absent from navigation is not necessarily private."

This repo has `llms.txt` and `llms-full.txt` **enabled** (footer links in `docs.json`). Those
are full-corpus public exports. Manifests must therefore not live in page frontmatter and not
live under a built path.

**Verified 2026-09-07:** "not built" is narrower than it sounds. Mintlify processes `.md` as
well as `.mdx`, and omission from `docs.json` navigation does **not** exclude a file — this
was confirmed by `mint validate` raising a parse error inside a planning `.md` file that no
navigation entry referenced.

The actual exclusion mechanism is a repo-root **`.mintignore`** (gitignore syntax; Mintlify
also always ignores `.git`, `.github`, `.claude`, `.agents`, `.idea`, `node_modules`, and
`README.md`). It now excludes `prisma-airs/_project/`.

So the rule for manifests is: excluded by `.mintignore`, or stored outside the repo. Choosing
an unreferenced path or a non-`.mdx` extension is **not** sufficient protection.

Recommended storage, in preference order:

1. **KB-side.** Store manifests in the KB's own task/state facility via MCP. Best fit for
   §6's "reuse existing infrastructure" and avoids a second truth store entirely. Depends on
   unverified KB capabilities.
2. **Sibling private repo.** Keyed by `page_id`, joined on route.
3. **Gitignored local path** (`prisma-airs/.provenance/`) for the vertical slice only, as a
   temporary measure. Requires a `.gitignore` entry — not added yet, since nothing generates
   manifests until KB access exists.

Do not use the repo's existing `private/` directory: despite the name it is tracked in git,
and `private/catch-anthropic-errors.mdx` is a real `.mdx`.

## Page manifest

Adapted from the handoff's illustrative schema. Field names for KB identifiers
(`claim_refs`, revision format) are placeholders until the live MCP contract is read.

```yaml
schema: docs.page.v2
page_id: docs.ai-gateway.fallbacks
route: "product/ai-gateway/fallbacks"     # matches the docs.json entry
type: guide                                # concept|quickstart|guide|reference|operations|troubleshooting|changelog|example
owner: "docs-owner"
applies_to: "supported-version-or-environment"
lifecycle: draft                           # draft|review|published|withdrawn
docs_revision: "git-sha"
kb_revision: "immutable-kb-revision"
sections:
  - id: how-fallbacks-trigger
    assertions:
      - id: a1
        text_digest: "sha256-of-the-asserted-sentence"
        claim_refs:
          - id: "accepted-claim-id"
            revision: "claim-revision-or-digest"
    generated_by: "task-id"
    origin_kind: generated                 # human|generated|mixed
    reviewed_by: "review-reference"
publication:
  build_id: "publication-id"
  policy_revision: "policy-revision"
  published_revision: "actually-served-revision"
```

**`applies_to` is narrower than it looks (Q12, 2026-09-07).** Launch environments are managed
and hybrid, and product behaviour is **deployment-invariant** — the same capabilities behave
the same way on both. So `applies_to` carries version applicability, not environment
applicability. There are no environment-variant page sets, no per-environment claim fan-out,
and the coverage ledger stays one-dimensional. Deployment is described plainly on the pages
where it is genuinely the subject, and nowhere else. Do not reintroduce environment branching
into the manifest without a specific, recorded reason: it multiplies the claim space and every
downstream index with it.

`published_revision` is deliberately separate from `docs_revision`. Handoff §5: "A successful
commit is not proof that readers received the update," and §9 requires reconciliation to
account for proposals, accepted revisions, and published revisions **separately**.

`text_digest` per assertion is what makes the §5 loop rules work — it distinguishes an
unchanged generated echo (no-op) from a human edit of generated prose (submit the semantic
delta, preserve ancestry).

## Dependency index

Rebuildable, derived from the manifests. Never hand-maintained.

```
claim_id -> [ {page_id, section_id, assertion_id, claim_revision_seen} ]
```

Drives KB→docs: an accepted claim change yields the exact set of sections to patch.

Rebuildability matters more than durability — if it can be regenerated from manifests plus
KB reads, a corrupted or missing index is a recoverable condition rather than an outage.

## Coverage ledger

The inverse view. Every eligible public KB claim is in exactly one state:

| State | Meaning |
|---|---|
| `used` | Cited by at least one published assertion |
| `awaiting-placement` | Eligible, no page yet — needs a coverage decision |
| `blocked` | Placement identified, publication gated on something |
| `omitted` | Intentionally not documented, **with a recorded reason** |

Eligibility does not require one page per claim (§2). The ledger exists so that "we chose not
to document this" is distinguishable from "we missed this."

## Disposition ledger

Handoff §5: every change ends as `applied`, `no-op`, `excluded`, `pending-review`, `conflict`,
`blocked`, or `failed`. Nothing ends as "done" implicitly.

Two rules worth stating separately because they are the ones that silently break:

- **Idempotency.** Duplicate event delivery must produce one logical contribution, proposal,
  or publication. Persist receipt before acknowledgment; use idempotency keys on all
  side-effecting operations.
- **An empty queue is not evidence of synchronization** (§5). Periodic reconciliation compares
  KB state, source revisions, manifests, and publication status regardless of queue depth.

## Bootstrapping the existing corpus

~1,200 pages exist with no manifests and unknown provenance.

Do not backfill by asserting that current prose is supported. Handoff §3 rule 7 forbids
treating published documentation as corroboration of its own claims.

Sequence:

1. Manifests exist only for pages that have been through the grounding gate.
2. Every other page is implicitly `unverified` — tracked as a count, not as a manifest.
3. Re-grounding proceeds journey by journey, highest-traffic first, per
   [`01-reader-journeys.md`](./01-reader-journeys.md).
4. The `unverified` count is an INIT 1 reporting metric. It will not reach zero in INIT 1, and
   the exit report should say so plainly rather than scoping the corpus down to hide it.
