# Feedback on the handoff brief, for v3

Written 2026-09-07, after implementing INIT 1's unblocked envelope against
[`prisma-airs-docs-mintlify-handoff-v2.md`](./prisma-airs-docs-mintlify-handoff-v2.md).

This is not a critique of the brief's judgement, most of which held up under contact. It is the
list of places where following it faithfully still produced a wrong result, or where a decision
had to be invented because the brief had no vocabulary for it.

Ordered by cost incurred, not by severity in the abstract.

---

## 1. §2's privacy warning is too soft, and it caused the failure it warns about

**The brief says:** "Keep operational manifests private and outside Mintlify's public exports.
A page absent from navigation is not necessarily private."

**What happened:** I read "not necessarily" as "usually is, with exceptions," wrote in three
separate planning documents that navigation omission was sufficient protection, and put the
brief itself into a path Mintlify builds. `mint validate` failed on a parse error inside it.
Every planning document in this project — including the operator questions and the naming
rules — was inside the public build scope and would have shipped into `llms-full.txt`.

**Why the wording is at fault:** on Mintlify, navigation omission provides *zero* exclusion.
Not "not necessarily" — none. Mintlify parses `.md` as well as `.mdx`, and an unreferenced path
is still a built path. The hedge implies a spectrum where there is a binary.

**For v3:** name the mechanism, do not gesture at the risk.

> Navigation omission provides no exclusion whatsoever. The only exclusion mechanism is a
> repo-root `.mintignore` (gitignore syntax). Verify exclusion by running the platform's own
> validation against a deliberately malformed file in the excluded path — if it does not
> error, the exclusion is real.

That last sentence is the part worth stealing. A negative claim about tooling should be
verified by a positive test, and "no error" is a weak signal unless you first confirm the tool
*would* have errored.

## 2. "Sole factual authority" does not survive contact — there are at least two trusted sources

**The brief says (§3 rule 1):** the KB is the sole factual authority.

**What happened:** the OpenAPI specification turned out to be a second trusted source, sitting
outside the KB corpus and co-equal with it — 219 pages of published assertions that the KB does
not own. The brief has no vocabulary for this, so we had to invent one mid-flight: a scoped,
recorded exemption, plus rules for symmetric drift and maintainer-resolved conflicts.

That in turn forced a redesign. The reconciliation loop was specified as two-node (KB ↔ docs)
and had to become three-node (KB ↔ spec ↔ docs), which changes drift detection, conflict
handling, and the trigger model.

**For v3:** replace "sole factual authority" with a **trusted source register** — an explicit,
enumerated list of authoritative sources, each with a domain, an owner, and a conflict
procedure. Keep the KB primary. But state up front that there may be others, and that adding
one is a recorded decision rather than an exception to a rule.

The single-authority framing is not merely incomplete. It actively encourages treating a second
source as a violation to be minimised rather than as an architecture to be designed, which is
the wrong instinct and produces worse systems.

## 3. Preserving generated ancestry is not the requirement — refusing it is

**The brief says (§5):** generated ancestry must be preserved end to end, as an acceptance
requirement.

**What happened:** while designing echo protection, it became clear that preservation alone
accomplishes nothing. Metadata that no consumer acts on changes no outcome. The requirement
that matters lives in *ingestion*: the confidence model must **refuse** generated-ancestry
content as corroborating evidence.

The brief states rule 7 (published docs are not corroboration of their own claims) on the docs
side, and states ancestry preservation on the pipeline side, but never connects them. As
written, an implementer can satisfy both requirements completely and still build a system where
documentation silently confirms itself.

**For v3:** state the enforcement point, not just the data requirement.

> Rule 7 is enforced at ingestion. Content carrying generated ancestry must be refused as
> corroborating evidence. Preservation of the ancestry field is necessary but not sufficient;
> acceptance requires demonstrating the code path that reads the field and declines the
> content.

This is the highest-consequence item on the list, even though it cost us the least so far — it
was caught in design rather than in production. The failure mode raises confidence while
lowering accuracy, so it is invisible from inside the system and looks like health.

## 4. There is no "establish platform capabilities" step, and the architecture depends on them

**The brief says:** Mintlify is the platform; build no hosting, rendering, search, or preview
infrastructure. Correct, and it saved real work.

**What happened:** but it never says *establish what the platform already does before designing
around it.* So I designed the structure/prose separation as an authoring **discipline** — a
rule humans follow — and wrote it up that way. Then, reading the installed CLI's schemas, I
found `openapi.overlays`: OpenAPI Overlay documents applied at build time, auto-discovered.
The platform does the separation natively, as two files with two owners and two review paths.

The discipline version and the native version are not equivalent. One depends on everyone
remembering; the other is structural. I rewrote the OpenAPI handoff.

The same gap produced the `.mintignore` failure in item 1, and left group-level `openapi`
config, `x-mint`, `x-hidden` and `x-mint-enum` undiscovered until late.

**For v3:** add an explicit early step — inventory the platform's capabilities and record them
in the capability register *before* designing authoring workflows. Note specifically that
platform features may already implement a governance requirement, and that a native
implementation beats a documented discipline every time.

## 5. Nothing addresses the disposition of an existing corpus

**The brief says:** nothing. It reads as though the documentation set is being created.

**What happened:** the repository already held ~1,200 published pages under a different brand.
Whether those are inherited-and-corrected, re-grounded from scratch, or abandoned is the single
most consequential decision in the project — it determines coverage, effort, naming strategy,
and whether existing defects are in scope. Everything was blocked on it until the operator
answered.

The answer, once given, was clean and worth recording as a pattern: **re-ground, do not
inherit.** Prisma AIRS pages are produced from KB claims, so a wrong statement in the legacy
corpus is never carried forward and never needs fixing. That single ruling took the legacy
corpus's defects — 66 broken links, unverifiable compliance and uptime claims, possibly
incorrect SSO/SCIM pages — entirely out of scope.

**For v3:** add a "**disposition of existing documentation**" section requiring an explicit
choice per corpus, and note that "re-ground, do not inherit" makes legacy defects out of scope
by construction rather than by triage. Getting this decided on day one is worth more than any
other single answer.

## 6. The scoped-exception mechanism is used twice but named zero times

**The brief says (§4):** if the operator wants docs-native releases to publish before KB
acceptance, "encode that as an explicit release-only policy exception; it must not silently
weaken grounding for all pages."

That is exactly right, and it is a *general mechanism* presented as a one-off. We then needed
the identical shape a second time for the OpenAPI spec's authority exemption, and had to
re-derive its properties: scoped, recorded, justified, non-precedential.

**For v3:** name it once as a first-class construct — a policy exception register with required
fields (scope, rationale, expiry or review date, explicit non-precedence) — and have §4 and the
trusted source register both reference it. Two instances is enough to justify the abstraction.

## 7. "Factual review" is described as a role when it is often a mechanical check

**The brief says (§11):** identify owners for factual review, editorial publication, conflict
resolution, and urgent withdrawal.

**What happened:** I carried "factual authority is one named person" into the reconciliation
loop design and concluded the review queue was a structural bottleneck. It is not. Most loop
events are one-value diffs where the pull request quotes the prior claim, the new claim, and
the claim ID — verification is a string comparison any maintainer performs. The repository
already sustains ~8 distinct reviewers with no bottleneck.

Mine to own, but the brief invites it by treating factual review as a role rather than as a
check whose cost varies by orders of magnitude.

**For v3:** distinguish assertions requiring **judgement** (does this claim mean what the prose
says) from assertions verifiable by **comparison** (does this value match the quoted claim).
Only the former needs a named owner. The latter needs a well-formed pull request body, which is
a tooling requirement rather than a staffing one.

## 8. Smaller notes

- **Coverage metric.** The exit criteria are journey-based, but the metric that proved actually
  useful is *pages that have passed the grounding gate* — which is simultaneously INIT 1
  progress and INIT 2 loop coverage, because unmigrated pages have no manifests and therefore
  cannot participate. Worth naming in v3 as the primary number.
- **The unblocked envelope.** §6 permits proceeding with contracts and standards while access
  is pending, but does not say how far that extends. It turned out to be a long way: page
  contracts, provenance schema, naming rules, triage tiering, CI, spec structure, and
  navigation scaffolding all landed with zero KB access. v3 could state the envelope
  explicitly, since underestimating it delays work that has no dependency.
- **§9's reconciliation accounting is two-party** (proposals, accepted revisions, published
  revisions). With a trusted source register it needs to generalise to N sources.
- **Environment variance.** The brief treats applicability as a per-page concern. In this
  product it collapsed entirely — behaviour is deployment-invariant, so applicability is
  version-only. v3 should prompt for this early: it is a large simplification when true, and
  the default assumption of variance is expensive.

---

## What held up well

Worth recording, so v3 does not lose it while fixing the above.

- **Rule 7** is the best idea in the brief. It is the reason the loop is a divergence detector
  rather than an autonomous writer, and it prevented an entire class of design error.
- **"Ask only what remains needed after inspecting configured access"** (§11) produced better
  questions than a standard intake would have, because it forced the repository to be read
  first.
- **The disposition ledger's insistence that nothing ends implicitly** turned out to matter most
  for the states nobody plans for — `conflict` and `blocked` — which are the normal path, not
  the exception, once releases start changing documented defaults.
- **§5's "an empty queue is not evidence of synchronization"** generalised further than it was
  written. It applies to cursors and to webhook deliveries, and it is the reason scheduled
  reconciliation survives even after push triggers exist on both sides.
