# Changelog contribution path (docs → KB)

Handoff §4 "Engineering changelogs", §5, INIT 2 step 3.

## Why this is the right pilot

Handoff §11 closes with: "Start by proving one relationship end to end: retrieve accepted
public KB knowledge, create a grounded Mintlify page proposal, receive a human factual
change, contribute it through MCP, and reconcile the accepted result."

Changelogs are the cheapest place to prove that loop, for four reasons:

1. **They legitimately originate knowledge.** §4: "Docs-native engineering changelogs can
   originate new knowledge." Everywhere else in the corpus, docs consume KB facts. Here docs
   are allowed to produce them — so the contribution direction is exercised without an
   authority conflict.
2. **The facts are small, dated, and discrete.** A release entry is a bounded set of
   assertions with a natural identity (release tag + date), which makes provenance tractable.
3. **The workflow already exists here.** `.claude/skills/update-changelog/SKILL.md` and
   `.cursor/commands/document-a-release.md` (566 lines) already do release triage, doc-impact
   analysis, and entry authoring. The MCP step is an addition, not a rebuild.
4. **Low blast radius.** A changelog entry is append-only and historically scoped. Getting one
   wrong is recoverable in a way that a wrong quickstart is not.

## What the existing tooling already does

From `update-changelog/SKILL.md`:

| Step | What it does | Maps to |
|---|---|---|
| 1 | `gh release view` — fetch release notes, capture publish date | §4 "authorized changelog/release observation" |
| 3 | Triage PRs into highlight / provider update / fix / skip | Semantic delta classification |
| 4 | Find affected doc pages; update stale text | §4 "impacted-page proposals" — a manual dependency lookup |
| 5 | Write the `<Update>` block | Release entry authoring |
| 8 | Report back, flag pages that should exist | Knowledge-gap surfacing |

Step 4 is the notable one: it is already doing, by `grep`, exactly what the claim→section
dependency index is supposed to do deterministically. That is the natural upgrade path — the
index replaces the grep, and the skill's own instructions ("Never write a `[Docs](...)` link
without verifying the file exists") become a machine check rather than a discipline.

## What has to be added

Three new steps. None of them can be built until KB MCP access exists
([`00-capability-register.md`](./00-capability-register.md)), but the shape is determined by
the handoff regardless.

### New step 4a — extract factual assertions

After PR triage, before writing prose, emit the discrete facts the release establishes:

```yaml
release:
  id: "gateway-enterprise-node@v2.21.0"
  repo: "Portkey-AI/gateway-enterprise-node"
  date: "2026-08-14"
  source_revision: "git-sha"
  digest: "sha256"
assertions:
  - id: r1
    text: "<the factual statement, one per fact>"
    kind: new-capability        # new-capability|behavior-change|default-change|fix|deprecation
    applies_to: "<version or environment>"
    supersedes: ["<prior-claim-id>"]   # empty if net-new
```

`supersedes` is what makes step 4c work. A release that changes a default does not just add a
fact — it invalidates one, and that invalidation is what tells the dependency index which
existing pages are now stale.

### New step 4b — submit through MCP

Submit the assertions as a KB proposal. Retain the returned task handle.

Required properties, from §5:

- **Idempotent.** Keyed on `release.id` + `digest`. Re-running the skill on the same release
  produces one logical contribution, not a second proposal.
- **Provenance preserved.** `origin: engineering-release`, `origin_kind: human`, authenticated
  actor, source revision.
- **Receipt persisted before acknowledgment.** A crash after submit must not lose the handle.

### New step 4c — propose current-guide updates separately

§4 is explicit: an already-published release "is an observation to ingest, not proof of prior
KB acceptance," and it must be used "to propose current guide/reference updates without
silently rewriting the historical release."

So two outputs, never merged:

| Output | Mutability | Gate |
|---|---|---|
| The `<Update>` changelog entry | **Immutable** once published. Corrections append. | Release-entry policy |
| Patches to affected guides/reference | Mutable | Normal grounding gate — requires KB *acceptance* of the new claims |

This is the rule the current skill's step 7 ("apply documentation updates flagged in step 4")
does not yet distinguish. Today it edits guides in the same pass as the changelog. Under §4
those become two proposals on two different clocks.

## Publication policy — approved 2026-09-07

Handoff §4 DEFAULT: "normal docs publication waits for KB acceptance."

That default is a problem for changelogs specifically. Releases ship on engineering's
schedule; if the changelog entry cannot publish until the KB accepts its facts, the changelog
lags the release by the KB review latency.

§4 anticipates this and permits an exception: "If the operator wants docs-native releases to
publish first, encode that as an explicit release-only policy exception; it must not silently
weaken grounding for all pages."

Recommendation:

- **Changelog entry** — publishes on the release schedule, under an explicit release-only
  exception, with the KB proposal submitted at the same time.
- **Guide and reference patches** — wait for KB acceptance. No exception.

That keeps the exception narrow and scoped to a page type whose content is inherently a dated
observation rather than a standing product claim.

**Approved 2026-09-07** ([`04-operator-questions.md`](./04-operator-questions.md) Q9). This is
now the operating policy, not a recommendation. The exception is release-only: it does not
extend to any other page type, and §4 is explicit that it "must not silently weaken grounding
for all pages."

## Disposition tracking

Every submitted release lands in the ledger from
[`03-provenance-model.md`](./03-provenance-model.md):

| Disposition | Meaning |
|---|---|
| `applied` | KB accepted; affected guides patched |
| `no-op` | Facts already in the KB (a re-run, or engineering filed them directly) |
| `pending-review` | Handle open at the KB |
| `conflict` | KB holds a contradicting accepted claim — needs human review, per §5, never last-write-wins |
| `blocked` | Accepted but not publishable (e.g. public eligibility not granted) |
| `failed` | Submission error; retry with the same idempotency key |

`conflict` is the case worth designing for rather than treating as an edge case: a release
that changes a documented default *will* contradict the existing accepted claim. That is the
normal path, not the exceptional one, and the classification depends entirely on `supersedes`
being populated correctly in step 4a.

## Sequenced work

1. ✅ **Done.** Step 4a added to `.claude/skills/update-changelog/SKILL.md` — emits the
   assertion block to `prisma-airs/_project/releases/<repo>@<tag>.yaml` alongside the
   changelog entry. Useful on its own as a review artifact; makes the next release's facts
   inspectable independently of their wording.
2. ✅ **Done.** Step 7 split into two outputs on two clocks, with the immutability boundary
   stated in the skill and reinforced in its pitfalls list. Enforced by workflow now, by
   tooling later.
3. **On KB access.** Add step 4b, the MCP submission and handle tracking.
4. **On KB access.** Replace step 4's `grep`-based doc-impact search with the dependency
   index. Step 4a's `affects` field is the manual stand-in until then.
5. **INIT 2.** Add reconciliation: periodic sweep for releases with open or stale handles.

Steps 1 and 2 take effect on the **next release** — nothing is backfilled, per §3 rule 7.
