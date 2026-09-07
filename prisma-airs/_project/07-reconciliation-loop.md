# Continuous reconciliation loop (KB ↔ docs)

Handoff §5 ("Two-way synchronization"), §6, §9, §10. INIT 2.

Companion to [`06-changelog-contribution-path.md`](./06-changelog-contribution-path.md): that
document covers the docs→KB direction on one page type. This one covers the standing loop in
both directions, across the migrated corpus.

Status: **design only.** Nothing here is buildable until Q2 is answered, and one part of it
(echo protection) is unsafe to build until Q11 is answered. See
[`00-capability-register.md`](./00-capability-register.md).

## What this is not

It is not a self-updating documentation set, and the distinction is structural rather than
cautious.

Handoff §3 rule 7: published documentation is not corroboration of its own claims. An agent
that both authors a claim and accepts it has closed a loop with no external truth inside it —
every subsequent iteration reinforces whatever the first one got wrong, and nothing in the
system can detect that. §5 makes the same point from the other side by forbidding
last-write-wins on conflicts.

So the agent is a **divergence detector that opens pull requests**. It never merges, never
pushes to `main`, never force-pushes, and never publishes. Its entire blast radius is an open
PR. Every design decision below follows from holding that line.

## The precondition: the dependency index

The loop is not made possible by the agent or the scheduler. It is made possible by the
claim→section dependency index in
[`03-provenance-model.md`](./03-provenance-model.md#dependency-index):

```
claim_id -> [ {page_id, section_id, assertion_id, claim_revision_seen} ]
```

Without it, "an accepted claim changed" means re-reading ~1,200 pages and asking a model to
guess relevance. With it, it is a dictionary lookup returning an exact section set.

The property that matters operationally: **the index is a free byproduct of the grounding
gate, and prohibitively expensive to retrofit.** When a page passes the gate, the claim IDs it
rests on are already known — that is what the gate checked. Writing them to the `docs.page.v2`
manifest at that moment costs nothing. Reconstructing them later means inferring provenance,
which under rule 7 is indistinguishable from inventing it.

Two consequences worth stating plainly:

1. **Loop coverage equals migrated-page count.** Unmigrated pages have no manifests, so no
   claim change can point at them. They stay in the `unverified` bucket from §"Bootstrapping"
   in `03`. The Prisma AIRS version's page count is therefore simultaneously the INIT 1
   progress metric and the INIT 2 coverage metric — one number, both initiatives.
2. **The index is rebuildable, not durable.** It is derived from manifests plus KB reads. A
   corrupted index is a recoverable condition, not an outage. Do not add durability
   engineering to it.

## Triage tiers

If every KB change produces a pull request that needs a careful human read, review fatigue
ends the loop within weeks. The volume has to be absorbed unevenly, and the tiering is what
makes "always running" tolerable rather than exhausting.

| Tier | Trigger | Agent action | Human involvement |
|---|---|---|---|
| **0 — echo** | Claim revision changed; normalized text digest identical (formatting, punctuation, whitespace) | Update `claim_revision_seen` in the manifest. No PR. | None |
| **1 — substitution** | Claim maps to a single templated slot: a numeric limit, default value, version string, supported-model entry, enum member | Auto-PR. Diff is one value. Body quotes the old claim, the new claim, and the claim ID. | Merge only |
| **2 — rewrite** | Behavior change, new capability, deprecation, or any change touching prose structure | Draft PR. Stale sections marked, superseded and new claims quoted verbatim, proposed prose clearly labeled a proposal. | Factual review, then editorial (Q7: both Vrushank) |
| **3 — conflict** | Claim retracted or withdrawn; two accepted claims contradict; claim's public eligibility revoked | **No PR.** Alert only, plus disposition `conflict` or `blocked`. | §10 withdrawal path, outside ordinary editorial review |

Tier 0 is expected to carry most of the volume, and its value is entirely in what it does
*not* generate.

Tier 3 is the one that gets under-designed. A release that changes a documented default
*contradicts an accepted claim by construction* — that is the normal path through this system,
not an edge case. §5 is explicit that conflicts are never resolved last-write-wins. This is
also why `supersedes` in the step-4a assertion block
([`06`](./06-changelog-contribution-path.md#new-step-4a--extract-factual-assertions)) carries
more weight than any other field: a tier-3 event that arrives as an untagged tier-2 event
silently publishes a contradiction.

### Tier assignment is a gate, not a guess

The tier is decided by comparing claim digests and the manifest's assertion mapping — a
mechanical determination. Where the comparison is ambiguous, it escalates. A change is never
demoted to a lower tier by inference, and there is no path from tier 3 to a pull request.

## Runtime shape

Two watchers on independent clocks, converging on the shared disposition ledger.

### KB → docs

Poll KB change discovery, then resolve through the dependency index to a section set, then
tier, then act.

**Decided 2026-09-07 (Q13): reconcile against the manifests, always. A cursor is an
optimization, never the source of truth.**

An earlier draft treated cursor-vs-snapshot as a fork in the state model. It is not, for one
reason: **the previous snapshot already exists.** `claim_revision_seen` in the dependency index
is precisely that, and it has to be stored anyway for tier-0 digest comparison. There is no
second store to build and no fork to choose between.

So each run reads the current revision of every claim in the index and compares against what
the manifests already record. If the KB also exposes a cursor, use it to narrow *which* claims
to re-read — a performance win, nothing more.

The reason to prefer reconciliation even where a cursor exists is §5: "an empty queue is not
evidence of synchronization." A cursor **is** a queue, and a KB-side promise about completeness
and ordering. The events most likely to fall outside that promise — bulk re-imports, backfills,
manual claim edits, retractions — are exactly the ones that matter most, and a missed cursor
event is both silent and permanent. Snapshot reconciliation is self-healing: state is
re-derived from what is actually there, so anything missed corrects itself on the next pass.

Cost is bounded by coverage rather than by KB size, since only claims appearing in the
dependency index are read. While the migrated corpus is small, so is the read.

### docs → KB

Already half-specified. `update-changelog` step 4a emits the assertion file today; step 4b
submits it on KB access. The standing loop adds only a periodic sweep for releases whose
handles are open or stale — §5's "an empty queue is not evidence of synchronization."

### Where it runs

Recommendation: **a scheduled GitHub Action invoking `claude -p`**, with `repository_dispatch`
as a push path if the KB can emit webhooks. Poll as the fallback and the backstop.

The repo already uses Actions (`.github/workflows/openapi-validate.yml`), the pull request is
the natural output artifact, and the run log is an audit trail by default.

Rejected alternatives, with reasons rather than a survey:

- **Long-lived daemon.** Buys nothing. The work is bursty and event-shaped, and it adds a
  process to supervise plus a second place for state to live.
- **In-session scheduling.** Fine for prototyping the tier logic. Wrong for production: it
  dies with the session and leaves no durable audit trail.

### Safety properties

Non-negotiable, and each one maps to a specific failure this loop can otherwise produce:

- **Idempotency key** `(claim_id, claim_digest, page_id, section_id)`. Duplicate delivery
  produces one PR, not two.
- **Persist the watermark after the PR exists**, never before. A crash between the two must
  re-do work, not skip it. Re-doing is idempotent; skipping is silent data loss.
- **Kill switch.** One flag halts all automated PR creation, checked at the top of every run.
- **Rate ceiling.** A cap on PRs per run. A bulk KB re-import that touches 400 claims should
  trip the ceiling and alert, not open 400 pull requests.
- **No self-merge, no `main` write, no force-push.** Stated in the workflow's permissions
  block, not only in prose.

## Echo contamination

The failure mode most likely to cause real damage, and the only one on this page that is
invisible from inside the loop.

Published pages get crawled. If generated documentation re-enters the KB as evidence, the
agent confirms its own prior output, the confirmation raises confidence, and drift compounds
with no error surfacing anywhere. By the time it is noticed, the corrupted claims look
well-supported.

Handoff §5 requires generated ancestry to be preserved end to end, and the `docs.page.v2`
manifest already carries `origin_kind` and `generated_by` for exactly this. But the manifest
is only half the mechanism. The other half lives in the ingestion pipeline, which must
**refuse generated-ancestry content as corroborating evidence.**

**Confirmed a hard prerequisite, 2026-09-07 (Q11).** Not INIT 2 hardening, not a later
robustness pass. The loop does not run against production KB until this is verified.

Preservation is not the requirement — *refusal* is. "We keep the metadata" is a passing answer
to the wrong question: metadata that nothing acts on changes no outcome. What has to be
demonstrated is the code path where the confidence model reads the ancestry field and declines
to count the content as support. Ask for the field name and that path.

Ordinary bugs announce themselves. This one raises confidence while lowering accuracy, so by
the time it is visible the corrupted claims look well-supported.

## Ledger transitions

Every event lands in the disposition ledger from
[`03-provenance-model.md`](./03-provenance-model.md#disposition-ledger). Nothing ends as "done"
implicitly.

| From | Event | To |
|---|---|---|
| — | Tier 0 detected | `no-op` |
| — | Tier 1/2 PR opened | `pending-review` |
| `pending-review` | PR merged and published revision confirmed | `applied` |
| `pending-review` | PR closed unmerged, reason recorded | `excluded` |
| — | Contradiction detected | `conflict` |
| — | Accepted but public eligibility absent | `blocked` |
| any | Submission or run error | `failed` (retry on the same idempotency key) |

`applied` requires a confirmed **published** revision, not a merge. §5: "A successful commit is
not proof that readers received the update." This is why `03`'s manifest keeps
`published_revision` separate from `docs_revision` — without that split there is no way to
express the state where the fix is merged and readers are still reading the old page.

## Instrumentation

Add on day one, not after the first incident. The loop's characteristic failure is silent
stalling, so the metrics that matter are queue-shaped rather than event-shaped:

| Metric | Why |
|---|---|
| **Staleness budget** — sections whose `claim_revision_seen` is older than the KB's current revision, bucketed by age | The primary health signal. Should oscillate, not climb. |
| Open handles by age | Detects a review bottleneck before it becomes a correctness problem. |
| Tier distribution per run | A sudden tier-2 spike usually means a KB re-import, not a product change. |
| Runs since last successful KB read | Distinguishes "nothing changed" from "we stopped looking." Those look identical otherwise. |
| `conflict` count, never aggregated away | Each one is a human decision that has not been made yet. |

If the staleness budget grows monotonically, the loop is failing regardless of what every
other metric says. Learn that from a dashboard rather than from a customer.

## Sequenced work

1. **On KB access (Q2).** Read the claim-read and change-discovery contract. No longer gated on
   Q13 — reconciliation against manifests works against either contract shape.
2. **On Q11.** Verify ingestion *refuses* generated ancestry, not merely records it. Do not run
   the loop against production KB until that code path has been seen.
3. Build the dependency index as a grounding-gate output. This lands with the first migrated
   pages and is worth doing even if the loop is never built — it makes manual impact analysis
   deterministic.
4. Implement tier 0 only, in report mode: detect and log, create nothing. Runs against real
   data with zero blast radius and validates the digest comparison.
5. Add tier 1 auto-PRs behind the rate ceiling and the kill switch.
6. Add tier 2 draft PRs and tier 3 alerting.
7. Add the reconciliation sweep for stale handles (§5, §9).

Steps 4 through 6 are deliberately ordered by blast radius rather than by difficulty. Tier 2
is the most interesting to build and should be built last.

## Q10 — scheduler, budgets, and notifications

Handoff §6 says reuse existing infrastructure. Nothing is visible from this workspace, so this
is a proposal rather than a decision. Four separable pieces, and only the last one is
difficult.

**Scheduler — GitHub Actions cron.** The reflex is to reach for a PANW-internal scheduler on
§6 grounds, but the output artifact is a pull request. The scheduler should live where the
artifact lives; anything else moves credentials across a boundary for no gain. Revisit only if
the KB endpoint is unreachable from GitHub-hosted runners, which is a network question worth
asking alongside Q2.

**Budgets — three ceilings per run.** Claims examined, pull requests opened, and a hard token
budget. On breach: stop, alert, resume on the next run. This is safe specifically because of
the idempotency key — a partial run is replayable, so a budget stop costs latency rather than
correctness. That property is the return on designing idempotency in early.

**Notifications — a GitHub issue, not a message.** A tier-3 event lands as `conflict` in the
disposition ledger, which means a human decision that has not been made yet. That needs a
durable work item with an owner and a close state. A chat notification scrolls away and leaves
the ledger entry orphaned, which reproduces the exact "empty queue is not evidence" failure
§5 warns about. Mirror to a chat channel if one exists, but the issue is the record and the
issue's closure is what clears the ledger.

**The review queue — the actual open item.** Q7 assigns all four roles to one person. For a
bounded migration that is fine. For a loop that runs indefinitely it is a structural problem:
every tier-2 and tier-3 event requires one specific human, the queue grows whenever that person
is unavailable, and nothing in the metrics distinguishes a quiet week from nobody looking. The
"runs since last successful KB read" metric catches a stalled *agent*; it does not catch a
stalled *reviewer*.

Minimum viable fix, in preference order: a named backup for factual review; or an explicit
service-level target on queue age with the staleness budget alerting when it is breached; or,
weakest but better than nothing, a documented pause procedure so the loop is deliberately
stopped during known absences rather than quietly accumulating. Worth settling before the loop
goes live — it is cheap to arrange now and awkward to arrange during an incident.
