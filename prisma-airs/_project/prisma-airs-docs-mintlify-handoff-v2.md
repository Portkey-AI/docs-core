---
title: "Prisma AIRS AI Gateway — Docs on Mintlify"
subtitle: "Implementation handoff: excellent product docs, connected to the KB"
version: "2.0"
status: "Ready for implementation; live KB contracts to verify"
date: "2026-09-07"
audience: "Docs implementation agent and documentation owners"
---

# Prisma AIRS AI Gateway — Docs on Mintlify {.unnumbered}

> **IMPLEMENTER DIRECTIVE**  
> Build excellent public product documentation for Prisma AIRS AI Gateway on Mintlify. Consume accepted public knowledge from the Prisma AIRS KB and contribute engineering-originated changes through its MCP server. Deliver INIT 1: usable, published documentation. Deliver INIT 2: continuous bidirectional reconciliation. Mintlify supplies the documentation platform. Do not build hosting, rendering, search, or preview infrastructure. Do not take responsibility for other products, shared namespaces, or collisions; the operator handles those concerns.

## 0. Controlling decisions

This version supersedes the infrastructure-heavy docs handoff v1. The scope is exclusively Prisma AIRS AI Gateway. This is a build brief, not an authored product corpus: it makes no claims about AI Gateway behavior that the implementation agent may publish without retrieving accepted KB support.

Confirmed requirements:

- Audience: public customers and developers.
- Platform: Mintlify, using its native experience, serving, and publishing facilities.
- Knowledge: the existing Prisma AIRS KB; no separate docs truth store.
- Eligibility: any accepted, public-approved KB knowledge that serves a relevant docs page.
- Authoring: engineering may originate knowledge in docs or the KB.
- Contributions: docs factual changes and engineering changelogs initiate KB proposals through MCP.
- Synchronization: both directions, with provenance, conflict handling, and recovery.
- Scope exclusions: other products, namespace coordination, product switching, and cross-product migration.
- Live KB verification is explicitly deferred to implementation; it does not block this handoff or local scaffolding.

Recommended defaults, to distinguish from confirmed requirements:

- Generate and validate proposals automatically; initially require human approval for public publication.
- Keep contradictions under the KB's existing human-review policy.
- Prefer durable repository revisions for detecting authored changes; use Mintlify publication status to verify public delivery.
- Reuse existing KB tasks, sandboxes, credentials, model routing, event handling, and scheduling where supported.
- Begin with English unless the operator specifies otherwise.

MUST denotes a required boundary. SHOULD denotes a strong recommendation. DEFAULT denotes an implementation starting point. Record consequential deviations and ask the operator before changing knowledge authority, public approval, or MCP boundaries.

## 1. Ownership

| Owner | Responsibility |
|---|---|
| Mintlify | Documentation rendering, serving, native components, platform navigation, previews, and publishing facilities |
| Docs agent | Reader journeys, information architecture, page composition, examples, editorial quality, configuration, and documentation validation |
| KB | Claims, evidence, authority, acceptance, public scope, freshness, and contradiction resolution |
| Integration tasks | Change detection, dependency tracking, MCP submissions, review tracking, reconciliation, and audit |
| Operator | Access, publication owners, supplied placement in Mintlify, and operational choices outside this product scope |

Mintlify owns the platform mechanism; the docs agent still configures the experience and verifies that the resulting pages work. Platform delegation does not delegate factual accuracy or knowledge acceptance.

The earlier requirement to deploy the docs surface entirely on GCP is superseded by the Mintlify decision. Any small custom integration should first reuse the existing KB infrastructure. Do not introduce another cloud deployment merely because v1 listed one.

## 2. Model — documentation designed around reader tasks

The Model plane describes pages, reader journeys, navigation, examples, dependencies, and editorial ownership. Canon, Practice, and Pulse remain KB freshness metadata, not mandatory public navigation.

### Reader journeys

Build a coverage map for these journeys, adjusting page labels to the verified product:

1. Understand what the gateway does and when to use it.
2. Complete a first successful integration.
3. Configure a supported capability for a concrete task.
4. Operate and troubleshoot the integration.
5. Look up an exact contract, parameter, error, or limitation.
6. Understand a shipped change and any required action.

Do not assume the product has a feature because a familiar gateway does. Missing KB support becomes a knowledge-gap task, not plausible filler.

### Page contracts

| Page type | Required content contract |
|---|---|
| Overview/concept | Purpose, mechanism, boundaries, applicability, next useful task |
| Quickstart | Prerequisites, minimal steps, complete working example, expected result, verification, next step |
| How-to guide | One goal, environment/version, steps, checks, failure cases |
| API/reference | Exact versioned contract, parameters, types, defaults, errors, examples |
| Operations | Procedure, prerequisites, verification, recovery/rollback where applicable |
| Troubleshooting | Recognizable symptom, diagnostic steps, supported causes and remedies |
| Changelog | Release identity/date, applicability, what changed, migration impact |
| Example | Dependencies, complete runnable code, expected behavior, supported version |

### Writing and experience requirements

- Lead with the reader's goal and the shortest useful answer.
- Keep concepts separate from procedures and reference details; connect them with purposeful links.
- Make prerequisites and environment assumptions explicit before commands.
- Use copyable, complete examples with safe placeholders; never include real credentials.
- Explain how the reader knows a step worked.
- Prefer native Mintlify components; use custom presentation only for a specific reader need.
- Use callouts for actionable constraints, not decoration.
- Keep language precise, direct, and consistent with a controlled product vocabulary.
- Make headings, navigation labels, and page descriptions specific enough to support discovery.
- Avoid internal KB terminology in the public reading flow unless it helps the customer.
- Validate mobile layouts, keyboard navigation, links, code presentation, and relevant search behavior through Mintlify's actual output.

### Identity and provenance

Every page requires a stable ID, assigned route, page type, owner, applicability, lifecycle state, and source revision. Track claims at section/assertion granularity. A change to one fact should not rewrite unrelated editorial work.

Illustrative private manifest; adapt to actual KB identifiers:

```yaml
schema: docs.page.v2
page_id: docs.ai-gateway.example-guide
route: "operator-assigned-page-route"
type: guide
owner: "docs-owner"
applies_to: "explicit-supported-version-or-environment"
docs_revision: "git-sha"
kb_revision: "immutable-kb-revision"
sections:
  - id: example-section
    assertions:
      - id: assertion-1
        claim_refs:
          - id: "accepted-claim-id"
            revision: "claim-revision-or-digest"
    generated_by: "task-id"
    reviewed_by: "review-reference"
publication:
  build_id: "publication-id"
  policy_revision: "policy-revision"
```

Keep operational manifests private and outside Mintlify's public exports. A page absent from navigation is not necessarily private. Do not rely on navigation omission to protect evidence, review notes, or internal IDs.

Maintain a rebuildable claim-to-section dependency index and an eligible-knowledge coverage ledger. Each eligible claim is used, awaiting placement, blocked, or intentionally omitted with a reason. Eligibility does not require one page per claim.

## 3. Knowledge boundary — supplied by the KB

The docs system may store prose and editorial structure. It does not independently accept product facts.

Required rules:

1. All KB reads and writes use its approved MCP interface. No direct corpus Git, index, database, or evidence bucket access.
2. Every substantive published assertion must have applicable accepted KB support. This includes numbers, defaults, limits, instructions, prerequisites, code assumptions, and claimed outputs.
3. Claim ID existence is insufficient: the cited claims must support the assertion's actual meaning and scope.
4. Recheck public eligibility and current claim status before publication, not only at generation time.
5. No invented content to fill gaps. Record a blocked section or contribute a source through MCP.
6. Public rendering, search, downloads, examples, metadata, and enabled machine-readable exports must exclude private material.
7. Generated documentation cannot become independent corroboration of its own source claims.
8. KB acceptance and docs publication are separate state transitions.

Visible source citations are an editorial choice; full private provenance is mandatory. Non-substantive headings and connective prose do not need claim IDs. Code execution tests complement factual support; they do not establish unrestricted product guarantees.

## 4. Tasks — the docs agent's actual work

| Task | Input | Reviewable output |
|---|---|---|
| Plan coverage | Reader journeys and public KB inventory | Navigation/page map and knowledge gaps |
| Compose page | Page contract and accepted KB slice | MDX proposal and assertion manifest |
| Update affected sections | Changed claim revisions and dependency map | Minimal patch preserving editorial work |
| Improve reader experience | Review findings and permitted feedback | Navigation, prose, example, or layout proposal |
| Contribute factual edit | Engineering-authored semantic delta | KB MCP task handle and tracked disposition |
| Process release | Authorized changelog/release observation | KB contribution and impacted-page proposals |
| Validate publication | Proposed revision and current KB policy | Gate report and publication readiness |
| Reconcile | KB revisions, docs revisions, publication status | Applied/no-op/conflict/blocked/failed ledger |

Use the KB's task and sandbox system where it supports these operations. The docs agent should receive a public-approved slice and an output workspace. It must not gain unrestricted internal knowledge simply because its output will later be filtered.

### KB → docs

1. Receive an accepted-change event or discover a revision difference through reconciliation.
2. Obtain authoritative claim state through MCP and evaluate eligibility.
3. Find affected sections and evaluate placement for new eligible claims.
4. Pin KB and docs base revisions; produce a scoped MDX/configuration patch.
5. Validate support, scope, applicability, examples, links, and Mintlify rendering.
6. Open a reviewable proposal and follow publication policy.
7. Recheck base revisions and public eligibility before publishing.
8. Confirm Mintlify publication success and record the public revision.

### Docs → KB

1. Observe a durable, review-ready authored revision or an engineering release event.
2. Compare against the common base and classify editorial, factual, generated, or mixed changes.
3. Submit original factual deltas and provenance through MCP automatically.
4. Track the handle through acceptance, rejection, or conflict.
5. Reconcile affected docs after acceptance; preserve a visible review case otherwise.

Avoid submissions on every keystroke. Editorial-only changes need no factual mutation or freshness update. Human edits of generated text must retain generated ancestry while contributing the new factual delta.

### Engineering changelogs

Docs-native engineering changelogs can originate new knowledge: author the release entry, automatically submit its facts through MCP, and publish under the agreed gates after acceptance.

An already-published engineering release is an observation to ingest, not proof of prior KB acceptance. Preserve release ID, author, date, applicability, source revision, digest, and correction history. Use it to propose current guide/reference updates without silently rewriting the historical release.

DEFAULT: normal docs publication waits for KB acceptance. If the operator wants docs-native releases to publish first, encode that as an explicit release-only policy exception; it must not silently weaken grounding for all pages.

## 5. Minimal integration — continuous reconciliation

Mintlify publishing does not itself establish semantic synchronization with the KB. Retain only the integration machinery needed for dependable effects, preferably inside existing KB task facilities.

| Mechanism | Purpose |
|---|---|
| Authenticated events | Promptly identify durable changes |
| Private dependency manifests | Locate affected pages and sections |
| Task/disposition ledger | Track contributions, proposals, retries, and review |
| Provenance and content digests | Distinguish originals, generated echoes, and mixed edits |
| Revision checks | Prevent overwriting newer human work |
| Periodic reconciliation | Recover missed events and incomplete runs |

Prefer repository events for authored revisions and Mintlify status for publication confirmation. A successful commit is not proof that readers received the update. Verify actual event/API availability before selecting adapters; do not invent a Mintlify outbound webhook.

If KB events are unavailable, use approved MCP revision enumeration or snapshot/diff polling. If neither exists, record the missing capability for the KB owner. Never bypass MCP to create a change feed.

### Proposed event fields

```json
{
  "event_id": "unique-id",
  "origin": "kb|docs|engineering-release",
  "origin_kind": "human|generated|mixed",
  "actor": "authenticated-principal",
  "correlation_id": "logical-change-id",
  "causation_id": "preceding-event-or-null",
  "base_revision": "common-base",
  "revision": "immutable-revision",
  "affected_ids": ["page-or-claim-id"],
  "content_digest": "sha256",
  "generated_from": ["claim-revision"],
  "occurred_at": "timestamp"
}
```

This is an illustrative contract. Authenticate the source; origin fields cannot grant authority. Persist receipt before acknowledgment. Use idempotency keys and conditional side effects so duplicate delivery creates one logical contribution, proposal, or publication.

### Loop and conflict rules

| Case | Required disposition |
|---|---|
| Unchanged generated docs return through ingestion | Echo/no-op; no new evidence or verification bump |
| Human changes generated factual prose | Submit the semantic delta with ancestry preserved |
| Formatting/spelling-only edit | Editorial change; no factual KB update |
| KB changes; docs facts unchanged | Propose affected-section update |
| Both sides change compatibly | Reconcile references and preserve editorial work |
| Both sides change incompatibly | Named review; no last-write-wins overwrite |
| Page deleted | Remove publication/dependencies, not KB knowledge |
| Public permission revoked | Urgent withdrawal under approved policy |
| Old event arrives late | Stale/historical disposition; no freshness rollback |

The existing docs-ingestion pipeline must preserve generated ancestry too. Otherwise recrawling public Mintlify pages could undo loop protection. Treat this as an integration acceptance requirement.

Every change ends as applied, no-op, excluded, pending review, conflict, blocked, or failed. Reconciliation compares KB state, source revisions, dependency manifests, and publication status; an empty queue is not sufficient evidence of synchronization.

## 6. Mintlify configuration and resources

Use the operator-provided Mintlify workspace, repository, and assigned product scope. The agent should configure the permitted documentation surface and native components, not solve placement outside it.

Required resources are access and capabilities, not new infrastructure deployments:

- Mintlify project/repository access and the assigned edit scope.
- Native MDX/component and navigation configuration.
- Existing preview, review, build, and publishing workflow.
- Authenticated KB MCP service identity with appropriate public-read and contribution permissions.
- Existing execution/harness/model routing for docs tasks, where available.
- Private provenance/dependency storage and durable sync state through existing facilities.
- Engineering source registrations and reviewer ownership.
- Existing event/scheduler facilities and operational visibility for the small integration.

Do not build a custom frontend, search engine, hosting stack, CDN, preview service, or broad Terraform deployment for docs. If a native feature falls short, describe the reader problem and propose the smallest remedy before adding custom machinery.

### Implementation-stage capability checks

Verify MCP authentication, stable claim/revision reads, public approval/status fields, pagination/change discovery, contribution format, task status, grounding facilities, and provenance preservation. Map logical operations to actual tool variants; earlier brief examples are not evidence of deployed endpoints.

Verify the supplied Mintlify workflow: allowed files, configuration ownership, local/branch preview, required checks, publication authority, and deployment-status observation. The current brief does not claim authenticated inspection of either live system.

Proceed with page contracts, editorial standards, and local structure while access is pending. Do not claim integrated success until a real authorized read/contribution/publication round trip is demonstrated.

## 7. Publication quality gates

Before publication, require:

1. Valid page and manifest schemas, stable IDs, assigned routes, and ownership.
2. Accepted, applicable support for every substantive assertion, with semantic support assessment.
3. Current public eligibility, including changed permissions after proposal creation.
4. No private data in public artifacts, metadata, enabled exports, or build outputs exposed by Mintlify.
5. Supported example assumptions, syntax checks, and appropriate runnable tests.
6. Working links/anchors and coherent next steps.
7. Mintlify preview review for desktop/mobile, keyboard navigation, code blocks, and page-specific layouts.
8. Base-revision checks protecting concurrent human edits.
9. Required editorial approval and verified public deployment status.

Use dedicated approved test accounts for external API examples with bounded cost. Do not perform destructive or customer-state tests. If credentials are unavailable, distinguish static validation from a live execution test.

Model evaluation is fallible. Keep reviewed golden cases for unsupported numbers, omitted conditions, stronger certainty, wrong citations, and version mismatch. A human approval does not waive deterministic scope or security failures.

## 8. INIT 1 — excellent AI Gateway docs on Mintlify

### Objective

Deliver a usable, grounded first publication with an effective reader experience. Content is obtained from the KB during implementation; this brief defines the process and quality bar, not feature descriptions.

### Sequence

1. Inspect supplied Mintlify and KB access; record verified capabilities and missing integrations.
2. Map supported reader journeys and eligible knowledge; create a coverage and gap register.
3. Define page contracts, writing conventions, IDs, dependency manifests, and publication rules.
4. Configure navigation and native components within the assigned scope.
5. Build a representative vertical slice: a quickstart, concept, guide, reference, troubleshooting page, and release example where KB support exists.
6. Validate customer tasks, factual support, examples, links, and actual Mintlify rendering.
7. Implement a review-triggered contribution path for an engineering factual draft through MCP.
8. Expand approved coverage, publish through Mintlify, and demonstrate publication recovery using supported workflows.

Missing knowledge should produce a contribution or research request to the KB. Do not turn INIT 1 into a parallel bulk source-ingestion project or copy unsupported source prose directly into public pages.

### Exit criteria

- [ ] Published AI Gateway docs serve agreed reader journeys within the supplied Mintlify scope.
- [ ] A representative first-use journey succeeds with the documented prerequisites and steps.
- [ ] Every substantive published assertion has applicable accepted KB support.
- [ ] Navigation, links, code presentation, mobile experience, and applicable discovery behavior are validated.
- [ ] Private provenance and section dependencies are complete and recoverable.
- [ ] An engineering factual draft can submit through MCP and track to a KB disposition.
- [ ] Publication status is verified, not inferred from a repository merge.
- [ ] Knowledge gaps and any unexecuted live tests are explicitly recorded.
- [ ] No custom docs-serving infrastructure was introduced.

## 9. INIT 2 — bidirectional synchronization

### Sequence

1. Run shadow impact analysis: receive events and calculate expected effects without automatic publication.
2. Enable a small KB-to-docs canary; generate minimal section proposals and review their fidelity.
3. Enable engineering-originated docs contributions, including a changelog, editorial-only change, and human edit of generated text.
4. Add periodic reconciliation, durable retry, conflict routing, and missed-event recovery.
5. Verify generated ancestry survives the existing docs-ingestion connector.
6. Run replay, fault, conflict, scope, and publication tests.
7. Expand coverage and approve operating cadence, owners, budgets, and escalation.

DEFAULT: retain human publication review. Auto-publication is a later, explicit choice for narrowly defined change classes after measured quality; contradictions must not be silently auto-resolved.

### Exit criteria

- [ ] KB changes reach every affected section or have explicit dispositions.
- [ ] New eligible knowledge without dependencies is evaluated for placement.
- [ ] Engineering facts/releases enter KB through MCP and track to acceptance, rejection, or conflict.
- [ ] Generated echoes create no independent evidence or verification refresh.
- [ ] Mixed edits preserve ancestry and contribute only original semantic changes.
- [ ] Duplicate, out-of-order, and missed events converge safely.
- [ ] Conflicting human and KB changes preserve both revisions for review.
- [ ] Withdrawal and publication recovery recheck current public eligibility.
- [ ] Reconciliation accounts for proposals, accepted revisions, and actually published revisions separately.
- [ ] Owners can diagnose stalled synchronization without inspecting agent conversations.

## 10. Verification and operations

| Test | Required result |
|---|---|
| One claim affects several pages | Every dependent section updates; unrelated editorial text survives |
| New claim has no page | Coverage evaluation and placement/omission recorded |
| Permission revoked while draft waits | Publication blocked by current-policy check |
| Generated docs recrawled | No false corroboration or repeating task chain |
| Engineer changes a generated sentence | Original delta submitted with provenance |
| KB rejects correction | Review case remains visible; unsupported draft does not publish |
| Release changes current behavior | Historical release preserved; current guides updated through accepted claims |
| Duplicate event or crash after side effect | One logical contribution/proposal/publication |
| Human edit during generation | Revision check prevents overwrite |
| Missing webhook | Reconciliation discovers and processes the gap |
| Valid citation with unsupported meaning | Grounding gate rejects or narrows assertion |
| Publication fails after merge | Ledger reports failure/pending delivery, not success |
| Rollback points to now-restricted claims | Revalidation blocks unsafe restoration |

Track event-to-proposal time, KB acceptance time, human-review time, publication lag, conflicts, stale dependencies, knowledge gaps, failures, and task cost separately. Reuse existing observability facilities.

Runbooks must cover KB unavailability, failed contribution handles, missed events, conflicts, failed Mintlify publication, rejected grounding, public-scope withdrawal, and replay/recovery. Scope withdrawal needs an approved urgent procedure using available Mintlify controls; do not leave it behind ordinary editorial review. Record any limitations on cache/export removal rather than promising deletion from third-party copies.

## 11. Operational questions and implementation handoff

Ask only what remains needed after inspecting configured access:

- Which Mintlify project/repository and files constitute the assigned AI Gateway scope?
- What are the live KB MCP contract, service identity, and event/reconciliation capabilities?
- Who owns factual review, editorial publication, conflicts, and urgent withdrawal?
- What authoritative engineering specifications and release inputs are registered with the KB?
- Which supported versions, environments, languages, and reader journeys are launch-critical?
- What publication policy applies to engineering changelogs that originate in docs?
- Which existing task/scheduler facilities, budgets, and notifications should the integration reuse?

Do not ask the operator to reconsider Mintlify, public audience, KB authority, two-way authoring, namespace placement, or other products. Do not ask for secrets in chat; use normal configured access.

Required deliverables:

1. Reader-journey map, navigation, page contracts, and coverage/gap register.
2. AI Gateway MDX/configuration changes within the supplied Mintlify scope.
3. Private provenance manifests and claim-to-section dependency model.
4. MCP consumer/contributor integration and minimal reconciliation tasks.
5. Grounding, examples, rendering, and publication validation evidence.
6. INIT 1 and INIT 2 exit reports, operating notes, and unresolved limitations.

Start by proving one relationship end to end: retrieve accepted public KB knowledge, create a grounded Mintlify page proposal, receive a human factual change, contribute it through MCP, and reconcile the accepted result. Scale coverage after that path is trustworthy.

## 12. Platform references and change record

Use current official Mintlify documentation for configuration syntax and workflow details. The pages below were checked during the design discussion; re-check them during implementation rather than treating their behavior as a deployed-project guarantee.

- [Navigation and page organization](https://www.mintlify.com/docs/organize/navigation)
- [GitHub repository integration](https://www.mintlify.com/docs/deploy/github)
- [Publishing and review workflow](https://www.mintlify.com/docs/editor/publish)

Version 2 removes the custom docs platform build, cross-product/namespace work, migration assumptions, and broad infrastructure provisioning from version 1. It retains reader-oriented modeling, KB-only knowledge authority, grounding, original engineering contributions, provenance, and bidirectional reconciliation.

The assignment is excellent Prisma AIRS AI Gateway documentation on Mintlify. All engineering choices should be assessed against that outcome.
