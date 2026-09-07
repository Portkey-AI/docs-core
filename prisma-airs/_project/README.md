# Prisma AIRS AI Gateway — docs project

The canonical working document for the initiative described in
[`prisma-airs-docs-mintlify-handoff-v2.md`](./prisma-airs-docs-mintlify-handoff-v2.md).
Everything not published lives here. One file, so facts are stated once.

Companion: [`openapi-handoff.md`](./openapi-handoff.md) — kept separate only because it is
handed to a different agent building a different repository.

Last updated 2026-09-07.

---

## Status

**Page authoring is blocked.** No authenticated Prisma AIRS KB access exists from this
workspace, and §3 rule 2 forbids publishing substantive assertions without accepted KB support.

§6 permits what has been done instead: "Proceed with page contracts, editorial standards, and
local structure while access is pending. Do not claim integrated success until a real
authorized read/contribution/publication round trip is demonstrated." **No such round trip has
been demonstrated.**

Shipped so far: this document, the OpenAPI handoff, a `.mintignore`, a "Prisma AIRS" navigation
version in `docs.json`, `prisma-airs/overview.mdx` as a scaffold carrying **no product
capability claims**, and release-assertion extraction in
`.claude/skills/update-changelog/SKILL.md`.

---

## Ground rules

The constraints everything else derives from. Each is stated here and not repeated.

**Grounding.** Every substantive published assertion — numbers, defaults, limits, instructions,
prerequisites, code assumptions, claimed outputs — needs accepted KB support. Headings,
connective prose and editorial framing do not. No invented content fills a gap (rule 5).

**Rule 7.** Published documentation is never corroboration of its own claims. This is the most
important line in the brief. It is why the reconciliation loop is a divergence detector rather
than an autonomous writer, and why the existing corpus is not evidence of anything.

**Re-ground, do not inherit.** Prisma AIRS pages are produced from KB claims, not by rebranding
existing prose. Consequence: **defects in the Portkey-branded corpus are out of scope
entirely** — not deferred, not backlogged. 66 broken links, unverifiable compliance and uptime
claims, possibly-wrong SSO/SCIM pages: none are inherited, so none need fixing. Do not open
triage against them. Standing instruction: **do not modify non-Prisma-AIRS docs at all.**

**Build exclusion.** Navigation omission provides *zero* exclusion — Mintlify parses `.md` as
well as `.mdx`, and an unreferenced path is still a built path that reaches `llms.txt` and
`llms-full.txt`. The only mechanism is the repo-root `.mintignore`, which excludes
`prisma-airs/_project/`. Anything added here inherits it; anything added elsewhere does not.
This was learned the hard way — see [Feedback for the brief](#feedback-for-the-brief).

**Two trusted sources.** The KB is primary. The OpenAPI specification is a second trusted
source outside the KB corpus, under a scoped recorded exemption to rule 1. Details under
[Decisions](#decisions).

---

## Decisions

| # | Decision | Date |
|---|---|---|
| Q1 | **Scope:** the whole corpus is Prisma AIRS AI Gateway, rebranded in place. Other tabs are modules of it, not separate products. | 2026-09-07 |
| Q2 | **KB endpoint:** still open. Parked at operator's call. **Blocks all page authoring.** | — |
| Q3 | **Naming rule:** approved as written below. | 2026-09-07 |
| Q4 | **Onboarding:** through Strata Cloud Manager. Documented detail waits for the KB — not an operator call, and not to be inferred from the existing `app.portkey.ai` quickstart. | 2026-09-07 |
| Q5 | **SSO/SCIM correctness:** moot. Portkey-corpus content, never inherited. | 2026-09-07 |
| Q6 | **OpenAPI:** a new repository is the source. The spec is a **second trusted source outside the KB corpus** — see below. | 2026-09-07 |
| Q7 | **Owners:** Vrushank Vyas holds factual review, editorial publication, conflicts, urgent withdrawal. | 2026-09-07 |
| Q8 | **Virtual Keys version:** keep as is, do not touch. | 2026-09-07 |
| Q9 | **Changelog publication:** release-only exception approved. Entries publish on the release schedule; guide and reference patches wait for KB acceptance. | 2026-09-07 |
| Q10 | **Loop infrastructure:** largely settled — see [Reconciliation loop](#reconciliation-loop). Two items of workflow config remain. | 2026-09-07 |
| Q11 | **Generated ancestry:** hard prerequisite. Ingestion must *refuse* generated-ancestry content as corroborating evidence. Verification rides with Q2. | 2026-09-07 |
| Q12 | **Environments:** managed and hybrid. **Product behaviour is deployment-invariant.** English only. | 2026-09-07 |
| Q13 | **Change discovery:** downgraded to a performance detail — reconcile against manifests regardless of contract shape. | 2026-09-07 |

**Launch scope and navigation skeleton are reserved to Vrushank**, who is hand-designing them,
reusing and improving the Portkey structure. Do not propose a navigation tree or page
inventory.

**Deferred by agreement:** `mint a11y` and `mint test` adopted later.

### The OpenAPI exemption (Q6)

The specification is a key source of trusted knowledge sitting *outside* the KB corpus —
co-equal with the KB, not subordinate and not merely an ingestion input.

This is a deliberate deviation from §3 rule 1's "sole factual authority," scoped to the API
specification, recorded rather than assumed precisely so it cannot be cited as precedent for a
second exemption.

1. Two trusted sources, one truth. Neither silently overrides the other.
2. Conflicts are resolved by **maintainers** — never automatically, never last-write-wins.
3. Both stay in sync; **drift from either side is raised.** There is no authoritative side to
   fall back on.
4. Sync is **bidirectional and webhook-driven**: a spec change notifies the KB, a KB change
   notifies the spec repository.

### Deployment invariance (Q12)

Managed and hybrid behave identically, so `applies_to` carries **version** applicability only.
No environment-variant page sets, no per-environment claim fan-out, one-dimensional coverage
ledger. Deployment is described plainly where it is genuinely the subject and nowhere else.
Do not reintroduce environment branching without a specific recorded reason — it multiplies the
claim space and every index downstream.

---

## Open items

- **Q2 — KB endpoint, identity, tool contract.** Needs the tool surface: claim reads, public
  eligibility fields, change discovery, contribution submission, task status. Parked.
- **Q11 verification.** Ask for the field name and the code path where the confidence model
  reads ancestry and declines the content. "We preserve the metadata" is a passing answer to
  the wrong question.
- **Tier-3 default assignee** and the **self-reporting health check** — two lines of workflow
  config, decided when the loop is built.
- **`tags[].name`** in the new spec: simultaneously display text and reference key. Flagged for
  a human, not decided.
- **`x-mint.mcp` coverage** — which operations become agent-callable tools is a product surface
  decision.

The configured `mcp-gateway` MCP server times out on connect (`CONNECT_TIMEOUT`, 30s). Its name
matches Portkey's own MCP Gateway product, so it is probably not the KB — but confirm rather
than assume. If it *is* the KB path, that timeout is the highest-priority unblock.

---

## Platform facts

Verified in this workspace against `docs.json` and the installed `mint` CLI **4.2.876**.
mintlify.com is unreachable from here (WebSearch blocked by org policy, no WebFetch, curl
denied), so this is grounded in the repository and the CLI rather than in Mintlify's own
documentation. Re-check the finer points during implementation.

| Capability | Status | Evidence |
|---|---|---|
| Navigation model | Verified | `navigation.versions[]` → tabs → groups → pages. A third version, "Prisma AIRS", now sits between "Latest" and "Virtual Keys (Deprecated)". "Latest" stays first, so it stays default. |
| Strict validation | Verified | `mint validate` exits non-zero on warnings |
| Build exclusion | Verified | repo-root `.mintignore`, gitignore syntax. Defaults also ignore `.git`, `.github`, `.claude`, `.agents`, `.idea`, `node_modules`, `README.md` |
| Public exports enabled | Verified | footer links `llms.txt`, `llms-full.txt` — rule 6 applies |
| Group-level OpenAPI | Verified | `groupSchema` accepts `openapi`, `asyncapi`, `tag`, `directory`, `expanded` alongside `pages` — generates a page per operation, no stub files |
| OpenAPI overlays | Verified | `openapi.overlays` takes Overlay documents applied in order; auto-discovered as well as explicit |
| `x-mint` extension | Verified | `metadata`, `content`, `pre`/`post`, `href`, `groups`, `playground.expand`, `mcp{enabled,name,description}`; plus `x-hidden`, `x-excluded`, `x-mint-enum` |
| Current API reference wiring | Verified | 219 `.mdx` stubs binding by `openapi: <method> <path>` frontmatter — the legacy pattern, being replaced |
| OpenAPI CI | **Not working** | `.github/workflows/openapi-validate.yml` validates `openapi.yaml` at the docs-core root, which does not exist; no run history; names a different artifact from the remote spec `docs.json` reads. The real check today is `mint validate`. Out of scope to fix. |
| Other CLI checks | Verified, unexercised | `mint broken-links`, `a11y`, `test`, `export`, `format` |
| Publication authority, deploy-status API | Unverified | not determinable from the repo; §5 warns against inventing a Mintlify outbound webhook |

**KB capabilities are entirely unverified** — endpoint, auth, claim reads, eligibility fields,
change discovery, contribution format, task status, ancestry preservation. Nothing has been
exercised.

**Not treated as KB knowledge:** `~/.claude/skills/rfp/knowledge/prisma-airs-ai-gateway.md` is
an internal sales artifact, useful only for generating questions; and the existing published
corpus, per rule 7.

**Left alone deliberately:** non-page files inside the build scope at the repo root
(`writing-style-guide.md`, `MCP-Gateway-Roadmap.md`, `create-split-prs.sh`, two stray images).
They parse cleanly so they raise no warning, but they are inside the public exports. Excluding
them changes existing published output, which is out of scope.

---

## Naming rules

Drawn from the RFP knowledge file's convention. Naming is the one area where the KB is not the
authority — it is an operator and branding decision. Everything else still is.

**Renamed:** "Portkey" / "Portkey AI" as the product → **Prisma AIRS AI Gateway** on first
mention, then **the gateway** or **AI Gateway**. Management plane → **Strata Cloud Manager**.
Company → **Palo Alto Networks**.

**Never renamed** — functional identifiers. A doc that breaks copy-paste is worse than one with
a legacy name in it.

| Kind | Examples |
|---|---|
| Packages and imports | `portkey_ai`, `portkey-ai`, `from portkey_ai import Portkey` |
| Classes, constructors, constants | `Portkey(...)`, `createHeaders`, `PORTKEY_GATEWAY_URL` |
| Environment variables | `PORTKEY_API_KEY`, `PORTKEY_*` |
| HTTP headers | `x-portkey-api-key`, `x-portkey-provider`, `x-portkey-*` |
| Hostnames | `api.portkey.ai`, `app.portkey.ai` |
| Config keys, JSON fields, `operationId`s, schema names | as shipped |
| Repo names in changelogs | `Portkey-AI/gateway`, `Portkey-AI/albus`, … |

> **If a reader would type it or a machine would parse it, it does not change.** If a reader
> only reads it, it does.

**Also decided:** the `prisma-airs-cta` snippet is **not used anywhere in the Prisma AIRS
version.** It announces the Portkey → Prisma AIRS transition, which is redundant on pages that
are already Prisma AIRS. It stays on Latest-version pages.

**Approved as written:** the open-source Gateway keeps its own identity; community CTAs
(Discord, `git.new/ai-gateway-docs`, `support@portkey.ai`, `status.portkey.ai`) stay as they
are; the compliance and uptime claims on `introduction/what-is-portkey` are Portkey-corpus and
not inherited.

**Never run a global find-and-replace.** The identifier list guarantees it breaks code samples
across ~1,200 pages. The migration unit is a page, and the trigger is the grounding gate.

---

## Page contracts

Bound to this repo's components and [`writing-style-guide.md`](../../writing-style-guide.md).
Where the handoff and the style guide overlap they agree; where they differ the handoff's
requirements are additive — what must be present, not how to phrase it.

| Type | Required elements |
|---|---|
| Concept | purpose · mechanism · **boundaries, including what it does not do** · applicability · next task |
| Quickstart | prerequisites before the first command · minimal steps · complete runnable example · **verification** · one next step |
| How-to | one goal · environment/version · steps · checks · **failure cases** |
| Reference | exact versioned contract · parameters · types · defaults · errors · examples |
| Operations | procedure · prerequisites · verification · **rollback** where production routing or credentials change |
| Troubleshooting | symptom *as the reader would describe it* · diagnostics · supported causes and remedies |
| Changelog | release identity/date · applicability · what changed · migration impact |
| Example | dependencies · complete runnable code · expected behaviour · supported version |

The two most commonly skipped elements are **boundaries** on concept pages and **verification**
on quickstarts. "How does the reader know it worked?" is part of the contract.

Only list troubleshooting causes the KB supports; speculative causes violate rule 5.

**Components.** `<CodeGroup>` for language variants — never `<Tabs>`. `<Steps>` for procedures,
`<Card>`/`<CardGroup>` for next actions, `<Accordion>` for collapsible detail, `<Frame>` for
images, `<Note>`/`<Warning>`/`<Info>`/`<Check>` for actionable constraints rather than
decoration. Prefer native components; propose the smallest remedy before adding custom
machinery.

**Code style.** K&R braces, 4-space indent, simple objects on one line, no trailing commas in
Python, language-correct comments, every block titled so `CodeGroup` renders a usable tab label.
Complete and runnable with safe placeholders. Never a real credential.

**Applicability has no public frontmatter home.** Decide before authoring: an in-page `<Info>`
callout, or a private manifest field only. Do not invent a frontmatter key Mintlify will not
validate.

### Pre-publication checklist

- [ ] Frontmatter valid; page registered in `docs.json`; route assigned; owner recorded
- [ ] Every substantive assertion has accepted, applicable KB support
- [ ] Public eligibility re-checked **now**, not at draft time
- [ ] No private material in the page, its metadata, or the public exports
- [ ] Examples syntax-checked; runnable tests run or the omission recorded
- [ ] Links and anchors resolve; next step is coherent
- [ ] `mint dev` reviewed on desktop and mobile
- [ ] Base-revision check — no concurrent human edit overwritten
- [ ] Editorial approval recorded; deployment status **verified**, not inferred from merge

Two failure modes the gate must catch, both worse than a missing citation because they look
correct: a valid claim ID cited for an assertion it does not support, and an assertion stated
with more certainty or broader scope than its claim carries.

---

## Provenance model

Claims are tracked at **section/assertion** granularity so a changed fact patches one section
rather than rewriting a page.

Manifests must not live in page frontmatter or under a built path. Storage, in preference
order: KB-side via MCP (best fit for §6, avoids a second truth store); a sibling private repo;
or a gitignored local path for the vertical slice only. Not the repo's existing `private/`
directory — despite the name it is tracked, and contains a real `.mdx`.

```yaml
schema: docs.page.v2
page_id: docs.ai-gateway.fallbacks
route: "product/ai-gateway/fallbacks"
type: guide                        # concept|quickstart|guide|reference|operations|troubleshooting|changelog|example
owner: "docs-owner"
applies_to: "supported-version"    # version only — see deployment invariance
lifecycle: draft                   # draft|review|published|withdrawn
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
    origin_kind: generated          # human|generated|mixed
    reviewed_by: "review-reference"
publication:
  build_id: "publication-id"
  policy_revision: "policy-revision"
  published_revision: "actually-served-revision"
```

`published_revision` is deliberately separate from `docs_revision`. §5: "A successful commit is
not proof that readers received the update." Without the split there is no way to express
*merged but readers still see the old page*.

`text_digest` distinguishes an unchanged generated echo (no-op) from a human edit of generated
prose (submit the semantic delta, preserve ancestry).

### Dependency index

```
claim_id -> [ {page_id, section_id, assertion_id, claim_revision_seen} ]
```

Derived from manifests, never hand-maintained. This — not the agent, not the scheduler — is
what makes the loop possible: without it, "a claim changed" means re-reading ~1,200 pages and
guessing relevance; with it, a dictionary lookup returns the exact section set.

**It is a free byproduct of the grounding gate and prohibitively expensive to retrofit.** When
a page passes the gate the claim IDs are already known — that is what the gate checked. Writing
them to the manifest then costs nothing; reconstructing them later is indistinguishable from
inventing provenance.

Two consequences. **Loop coverage equals migrated-page count** — unmigrated pages have no
manifests, so no claim change can point at them; the Prisma AIRS version's page count is
simultaneously the INIT 1 progress metric and the INIT 2 coverage metric. And the index is
**rebuildable rather than durable**, so a corrupted index is recoverable, not an outage — do
not add durability engineering to it.

### Ledgers

**Coverage** — every eligible public KB claim is in exactly one state: `used`,
`awaiting-placement`, `blocked`, or `omitted` *with a recorded reason*. The ledger exists so
"we chose not to document this" is distinguishable from "we missed it."

**Disposition** — every change ends as `applied`, `no-op`, `excluded`, `pending-review`,
`conflict`, `blocked`, or `failed`. Nothing ends as "done" implicitly.

| From | Event | To |
|---|---|---|
| — | Tier 0 detected | `no-op` |
| — | Tier 1/2 PR opened | `pending-review` |
| `pending-review` | merged **and published revision confirmed** | `applied` |
| `pending-review` | closed unmerged, reason recorded | `excluded` |
| — | Contradiction detected | `conflict` |
| — | Accepted but public eligibility absent | `blocked` |
| any | Submission or run error | `failed` (retry on the same idempotency key) |

**Idempotency:** duplicate delivery must produce one logical contribution. Persist receipt
before acknowledgment. **An empty queue is not evidence of synchronization** — periodic
reconciliation compares KB state, source revisions, manifests and publication status regardless
of queue depth. That principle generalises to cursors and webhook deliveries alike.

### Bootstrapping

~1,200 pages exist with no manifests. Do not backfill — rule 7 forbids treating current prose
as support for its own claims. Manifests exist only for pages that passed the gate; everything
else is implicitly `unverified`, tracked as a count. That count will not reach zero in INIT 1,
and the exit report should say so plainly rather than scoping the corpus down to hide it.

---

## Reconciliation loop

**Not a self-updating docs set.** Rule 7 means an agent that both authors a claim and accepts
it has closed a loop with no external truth inside it — every iteration reinforces whatever the
first got wrong, and nothing can detect that. §5 forbids last-write-wins from the other side.

So the agent is a **divergence detector that opens pull requests**. It never merges, never
pushes to `main`, never force-pushes, never publishes. Blast radius is an open PR.

### Topology: KB ↔ spec ↔ docs

Three nodes, since the spec became a co-equal trusted source. Drift is **symmetric** — the loop
raises a divergence regardless of which artifact moved; "the spec is newer" is not a
resolution. Resolution is **always human**: a KB↔spec contradiction has no diff to review, so
it inherits tier-3 handling. Webhooks on both sides make polling the backstop rather than the
mechanism — but keep scheduled reconciliation, because a missed delivery is exactly as silent
as a missed cursor event. Webhooks reduce latency; reconciliation establishes truth.

The join key for spec drift is `x-airs-provenance` on the operation. Without a claim reference
there, nothing can observe that the KB moved and the spec did not.

For KB↔docs: **reconcile against the manifests, always.** `claim_revision_seen` already *is*
the previous snapshot, so there is no second store to build and no cursor-vs-snapshot fork to
choose. If a cursor exists, use it only to narrow which claims to re-read. Cost is bounded by
coverage, not by KB size.

### Triage tiers

If every change needs a careful human read, review fatigue ends the loop in weeks. Volume has
to be absorbed unevenly.

| Tier | Trigger | Action | Human |
|---|---|---|---|
| **0 — echo** | Revision changed, normalized digest identical | Update `claim_revision_seen`. No PR. | None |
| **1 — substitution** | Single templated slot: limit, default, version string, enum member | Auto-PR, one-value diff, body quotes both claims and the claim ID | Merge only |
| **2 — rewrite** | Behaviour change, new capability, deprecation | Draft PR: stale sections marked, claims quoted verbatim, prose labeled a proposal | Factual then editorial review |
| **3 — conflict** | Claim retracted; two accepted claims contradict; eligibility revoked | **No PR.** Issue with a default assignee, disposition `conflict` or `blocked` | §10 withdrawal path |

Tier assignment is mechanical — a digest and manifest comparison. Ambiguity escalates; nothing
is demoted by inference; there is no path from tier 3 to a pull request.

Tier 0 carries most of the volume and its value is entirely in what it does *not* generate.
Tier 3 gets under-designed: a release changing a documented default **contradicts an accepted
claim by construction**. That is the normal path, not an edge case, which is why `supersedes`
in the release-assertion block matters more than any other field — a tier-3 event arriving as
an untagged tier-2 event silently publishes a contradiction.

### Runtime (Q10)

**Scheduler:** GitHub Actions cron invoking `claude -p`, with `repository_dispatch` for
webhooks. The output artifact is a pull request, so the scheduler should live where the
artifact lives; anything else moves credentials across a boundary for no gain. Revisit only if
the KB endpoint is unreachable from GitHub-hosted runners — a network question for Q2.
A long-lived daemon buys nothing: the work is bursty and event-shaped.

**Budgets:** three ceilings per run — claims examined, PRs opened, hard token budget. On
breach: stop, alert, resume next run. Safe *because* of the idempotency key — a partial run is
replayable, so a budget stop costs latency rather than correctness.

**Notifications:** tier 3 opens a **GitHub issue**, not a message. A `conflict` is a decision
not yet made, so it needs a durable work item with an owner and a close state. A chat ping
scrolls away and orphans the ledger entry.

**Safety:** idempotency key `(claim_id, claim_digest, page_id, section_id)`; persist the
watermark *after* the PR exists so a crash re-does rather than skips; a kill switch checked at
the top of every run; a rate ceiling so a bulk re-import touching 400 claims alerts instead of
opening 400 PRs; no self-merge, no `main` write, no force-push, stated in the workflow
permissions block and not only in prose.

**Review capacity is not a problem** — an earlier draft claimed it was, reasoning from Q7's
single-owner assignment, and that was wrong. Tier 1 is a string comparison against a quoted
claim; tier 2 is ordinary docs review. The repo's last fifteen merges had ~8 distinct reviewers
and no `CODEOWNERS`; review happens anyway. What survives is narrower: tier-3 issues have no
forcing function the way a blocking PR does, so they need a **default assignee**.

### Echo contamination

The failure mode most likely to cause real damage and the only one invisible from inside the
loop. Published pages get crawled; if generated documentation re-enters the KB as evidence, the
agent confirms its own prior output, confidence rises, and drift compounds with no error
anywhere.

`origin_kind` and `generated_by` in the manifest are half the mechanism. The other half is
ingestion **refusing** generated-ancestry content as corroborating evidence. Preservation is
not the requirement — metadata nothing acts on changes no outcome. Confirmed a **hard
prerequisite** (Q11): the loop does not run against production KB until that code path has been
seen.

### Instrumentation

| Metric | Why |
|---|---|
| **Staleness budget** — sections whose `claim_revision_seen` lags the KB, bucketed by age | Primary health signal. Should oscillate, not climb. |
| Open handles by age | Catches a submission accepted then forgotten |
| Tier distribution per run | A tier-2 spike usually means a KB re-import, not a product change |
| Runs since last successful KB read | Distinguishes "nothing changed" from "we stopped looking" |
| Open tier-3 issue age | The one queue with no forcing function |
| `conflict` count, never aggregated away | Each is a decision not yet made |

Do not assume anyone reads a dashboard. Wire thresholds into a **self-reporting health check**:
when one is breached, the loop opens an issue about itself. A PR queue is structurally incapable
of reporting that the loop stopped opening PRs — "no PRs this week" reads identically to healthy
and to broken.

### Build order

Ordered by blast radius, not difficulty.

1. **On Q2.** Read the claim and change-discovery contract.
2. **On Q11.** Verify ingestion refuses generated ancestry. Do not run against production KB
   until then.
3. Dependency index as a grounding-gate output — worth doing even if the loop is never built,
   since it makes manual impact analysis deterministic.
4. Tier 0 only, in report mode: detect and log, create nothing. Real data, zero blast radius.
5. Tier 1 auto-PRs behind the rate ceiling and kill switch.
6. Tier 2 draft PRs; tier 3 issues with a default assignee.
7. Self-reporting health check.
8. Reconciliation sweep for stale handles.

Tier 2 is the most interesting to build and should be built last.

---

## Changelog contribution path

The INIT 2 pilot, because changelogs are the one place docs legitimately *originate* knowledge
(§4) rather than consuming it — so the contribution direction is exercised without an authority
conflict. The facts are small, dated and discrete; the workflow already exists in
`.claude/skills/update-changelog/SKILL.md`; and an append-only historical entry has low blast
radius in a way a wrong quickstart does not.

**Done.** Step 4a emits an assertion file per release to `_project/releases/<repo>@<tag>.yaml`:

```yaml
release:
  id: "gateway-enterprise-node@v2.21.0"
  repo: "Portkey-AI/gateway-enterprise-node"
  date: "2026-08-14"
  source_revision: "<git-sha of the tag>"
assertions:
  - id: r1
    text: "<one factual statement, stated plainly>"
    kind: new-capability      # new-capability|behavior-change|default-change|fix|deprecation
    applies_to: "<version this holds for>"
    supersedes: []            # empty if net-new
    affects: []
```

One assertion per *fact*, not per PR. State the fact, not the edit. `supersedes` is the field
that matters: a release that changes a default does not merely add a fact, it invalidates one,
and that invalidation is what marks existing pages stale. These are review artifacts today and
the docs→KB payload once MCP access exists. Nothing is backfilled — rule 7 again.

**Done.** Step 7 split into two outputs on two clocks: the `<Update>` changelog entry is
**immutable** once published (corrections append), while guide and reference patches are
mutable and gated normally. Separate commits.

**Publication policy (Q9).** The §4 default — publication waits for KB acceptance — would make
the changelog lag every release by the KB review latency. §4 permits an explicit release-only
exception, and it is approved: **changelog entries publish on the release schedule** with the
KB proposal submitted simultaneously; **guide and reference patches wait for acceptance, no
exception.** Narrow, and scoped to a page type whose content is inherently a dated observation
rather than a standing product claim.

**Remaining.** Step 4b — MCP submission with idempotency on release id + digest, provenance
(`origin: engineering-release`, `origin_kind: human`, authenticated actor, source revision),
receipt persisted before acknowledgment. And replacing step 4's grep-based doc-impact search
with the dependency index; `affects` is the manual stand-in until then.

---

## Known gaps

The detailed journey-by-journey route inventory has been dropped — Vrushank is hand-designing
the skeleton, which supersedes it. What survives is the gap register.

- **Grounding is unknown, not absent.** Every existing feature page carries defaults, limits
  and precedence rules with no claim references. Under §3 they are all unsupported until
  reconciled. This is the largest item of INIT 1 work by volume.
- **No applicability metadata.** Pages state no supported version. (Environment is *not* part
  of this gap — see deployment invariance.)
- **Troubleshooting is the weakest surface.** Reliability features have configuration pages but
  no symptom→diagnosis→remedy path; no day-2 operations pages (key rotation, budget breach,
  provider outage, guardrail false-positive triage); content split across `support/`,
  `help-center/` and `self-hosting/` with no single entry point.
- **Limits and errors are not consolidated.** No single rate-limit / quota / error-code
  reference.
- **Changelog contract compliance unaudited** against §2's required elements.

**To put to the KB, not findings:** the RFP knowledge file describes a four-tier tenancy
hierarchy (Organisation → Department → Team → User/Application) where the docs describe
organizations and workspaces; and it uses licensing labels (Enterprise, Agent Gateway,
Observability Suite, Guardrails Engine, Model Catalog, Prompt Studio) that only partly match
the navigation groups. Confirm which vocabulary is public before applying either.

---

## Feedback for the brief

From implementing against v2. Ordered by cost incurred. Fold into the next revision rather than
keeping as a separate versioned document.

**1. §2's privacy warning is too soft, and it caused the failure it warns about.** "A page
absent from navigation is not necessarily private" reads as *usually is, with exceptions*. The
truth is binary: navigation omission provides **no** exclusion. I believed the soft reading,
wrote it into three planning documents, and put the brief itself inside the build scope —
`mint validate` caught it on a parse error. Every planning artifact here was headed for
`llms-full.txt`. Name `.mintignore` as the mechanism, and prescribe verifying exclusion with a
deliberately malformed file in the excluded path: "no error" is a weak signal unless you first
confirm the tool *would* have errored.

**2. "Sole factual authority" does not survive contact.** The spec turned out to be a second
trusted source the KB does not own. The brief has no vocabulary for this, so the exemption,
symmetric-drift rule and maintainer conflict procedure were invented mid-flight, and the loop
was redesigned from two-node to three. Replace rule 1 with a **trusted source register** —
enumerated sources, each with a domain, owner and conflict procedure, KB still primary. The
single-authority framing actively encourages treating a second source as a violation to
minimise rather than an architecture to design.

**3. Preserving generated ancestry is not the requirement; refusing it is.** §5 asks for
preservation, rule 7 states the principle, and the brief never connects them. As written, an
implementer can satisfy both completely and still ship a system where documentation silently
corroborates itself. State the enforcement point: rule 7 is enforced at ingestion, and
acceptance requires demonstrating the code path that reads the ancestry field and declines the
content. Lowest cost so far, highest consequence — the failure raises confidence while lowering
accuracy, so it looks like health from inside.

**4. No "establish platform capabilities" step.** "Mintlify is the platform, build no
infrastructure" is correct and saved real work, but it never says *find out what the platform
already does before designing around it.* So the structure/prose split was designed as an
authoring discipline before `openapi.overlays` turned up, which implements it natively as two
files with two owners. A native implementation beats a documented discipline every time. The
same gap produced the `.mintignore` failure.

**5. Nothing addresses the disposition of an existing corpus.** The brief reads as though the
docs are being created from nothing; ~1,200 pages already existed under another brand, and
everything was blocked until the operator ruled. Add a required per-corpus choice, and note
that **re-ground, do not inherit** takes legacy defects out of scope by construction rather
than by triage. Worth more than any other single day-one answer.

**6. The scoped-exception mechanism is used twice and named zero times.** §4's release-only
policy exception is a general construct presented as a one-off; the OpenAPI exemption needed
the identical shape. Name it once — scope, rationale, review date, explicit non-precedence.

**7. "Factual review" is described as a role when it is often a mechanical check.** This led me
to the review-bottleneck error above. Distinguish assertions needing **judgement** from those
verifiable by **comparison**; only the former needs a named owner, and the latter is a
well-formed PR body, which is tooling rather than staffing.

**8. Smaller.** The useful progress metric turned out to be *pages past the gate*, which is
also loop coverage — name it. §6's "proceed while access is pending" envelope is far larger
than it sounds and worth stating explicitly, since underestimating it delays undependent work.
§9's reconciliation accounting is two-party and needs to generalise to N sources. And prompt
early for environment invariance: it is a large simplification when true, and assuming variance
is expensive.

### What held up

Worth keeping while fixing the above. **Rule 7** is the best idea in the brief and should not
be softened. **"Ask only what remains needed after inspecting configured access"** produced
better questions than a standard intake, because it forced the repository to be read first.
**The disposition ledger's insistence that nothing ends implicitly** matters most for the states
nobody plans for — `conflict` and `blocked` are the normal path once releases start changing
defaults. And **"an empty queue is not evidence of synchronization"** generalised further than
written: it covers cursors and webhook deliveries, and it is why scheduled reconciliation
survives push triggers on both sides.

---

## Layout

```
prisma-airs/
├── _project/
│   ├── README.md                                   this file — the canonical doc
│   ├── openapi-handoff.md                          instructions for the spec-repo agent
│   ├── brainstorm.md + brainstorm.html             presentation design brainstorm + wireframe
│   ├── prisma-airs-docs-mintlify-handoff-v2.md     the source brief
│   └── releases/                                   per-release assertion YAML (generated)
└── overview.mdx                                    published — the Prisma AIRS version seed
```

`_project/` is excluded from the build by the repo-root `.mintignore`. Release assertion files
live here rather than in `changelog/` because they are not pages — they are not secret, since
everything in them becomes public in the changelog entry anyway.
