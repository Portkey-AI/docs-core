# Reader journeys and coverage register

Handoff §2. Six journeys, mapped onto the corpus that exists today in `docs.json`
(version "Latest").

The corpus is large — roughly 1,200 page entries across 7 tabs. This is not a greenfield
build. The realistic INIT 1 shape is **re-grounding and re-framing an existing corpus**, not
authoring one.

Coverage key: **Strong** = pages exist and cover the journey. **Partial** = pages exist but
have identified holes. **Thin** = little dedicated content.

---

## J1 — Understand what the gateway does and when to use it

Coverage: **Partial**

| Existing | Route |
|---|---|
| What is Portkey? | `introduction/what-is-portkey` |
| Feature overview | `introduction/feature-overview` |
| AI Gateway concept index | `product/ai-gateway` |
| Feature comparison | `product/product-feature-comparison` |
| Open source | `product/open-source` |

Gaps:

- **G1.1 — No product identity page for Prisma AIRS AI Gateway.** The entry page is titled
  "What is Portkey?", opens on a Portkey product-walkthrough video, and closes with a
  "give us a star" CTA and a Discord link. A reader arriving from Palo Alto Networks
  channels lands on a different product's name.
- **G1.2 — Product boundary undocumented.** Nothing states where the AI Gateway ends and the
  rest of Prisma AIRS begins (Strata Cloud Manager, AI Runtime Security, Common Services).
  Handoff §2 requires "boundaries" in every overview/concept contract.
- **G1.3 — "When to use it" is absent.** Feature lists exist; applicability guidance does not.

## J2 — Complete a first successful integration

Coverage: **Partial**

| Existing | Route |
|---|---|
| Make your first request | `introduction/make-your-first-request` |
| Model Catalog setup | `product/model-catalog`, `product/model-catalog/integrations` |
| README / contributing | `README` |

Gaps:

- **G2.1 — Onboarding path assumes `app.portkey.ai` signup.** If Prisma AIRS customers
  onboard through a Strata Cloud Manager tenant, the documented first step is wrong for the
  target audience. Blocking for the INIT 1 exit criterion "a representative first-use journey
  succeeds with the documented prerequisites and steps."
- **G2.2 — No verification step.** Handoff quickstart contract requires "expected result,
  verification." Needs an audit of the existing page against that contract.
- **G2.3 — Two live onboarding models.** The deprecated "Virtual Keys" navigation version is
  still published alongside Model Catalog. A new reader can land on either.

## J3 — Configure a supported capability for a concrete task

Coverage: **Strong** — this is the corpus's best-developed area.

`product/ai-gateway/*` (configs, fallbacks, automatic-retries, circuit-breaker,
load-balancing, conditional-routing, cache-simple-and-semantic, canary-testing,
request-timeouts, custom-hosts, multimodal-capabilities/*, files, batches, fine-tuning),
plus `product/guardrails/*`, `product/model-catalog/*`, `product/mcp-gateway/*`,
`product/agent-gateway/*`, `product/prompt-engineering-studio/*`,
`product/observability/*`, `product/administration/*` (20 enforcement how-tos).

Gaps:

- **G3.1 — Grounding is unknown, not absent.** Every one of these pages carries substantive
  assertions (defaults, limits, precedence rules) with no claim references. Under §3 they are
  all unsupported until reconciled against the KB. This is the single largest item of INIT 1
  work by volume.
- **G3.2 — No applicability metadata.** Pages do not state supported version, which §2
  "Identity and provenance" requires. *Narrowed 2026-09-07 (Q12): environment is not part of
  this gap. Launch covers managed and hybrid, product behaviour is deployment-invariant, and
  applicability is therefore version-only.*

## J4 — Operate and troubleshoot the integration

Coverage: **Thin** — the weakest journey.

| Existing | Route |
|---|---|
| Common errors and resolutions | `support/common-errors-and-resolutions` |
| Help Center articles (2) | `help-center/mcp-gateway-troubleshooting`, `help-center/you-do-not-have-enough-permissions` |
| Prometheus metrics | `self-hosting/prometheus-metrics` |
| Cache behavior | `self-hosting/cache-behavior` |
| Hybrid deployment guides | `self-hosting/hybrid-deployments/*` |

Gaps:

- **G4.1 — No per-capability troubleshooting.** Reliability features (fallbacks, retries,
  circuit breaker, load balancing) have configuration pages but no "it isn't behaving as
  expected" path — the symptom→diagnosis→remedy contract from §2.
- **G4.2 — No day-2 operations pages** under the Docs tab: key rotation runbook, budget
  breach response, provider outage response, guardrail false-positive triage.
- **G4.3 — Troubleshooting content is split** across `support/`, `help-center/`, and
  `self-hosting/` with no single entry point.

## J5 — Look up an exact contract, parameter, error, or limitation

Coverage: **Strong**

Gateway APIs tab (18 groups, OpenAPI-backed) and Admin APIs tab (20 groups), plus
`api-reference/sdk/*`. Kept in sync by `.github/workflows/openapi-validate.yml` against the
external `Portkey-AI/openapi` repo.

Gaps:

- **G5.1 — Reference truth lives in a second repo.** *Partly resolved 2026-09-07 (Q6): a new
  OpenAPI repository will be supplied and is the source for Prisma AIRS API reference;
  `Portkey-AI/openapi` is Portkey-corpus tooling and is not inherited.* What remains open is
  the grounding status, not the source: the new spec is either ingested into the KB or carries
  a recorded exemption under §3 rule 1. Settle when the repo arrives — API reference is a large
  body of substantive assertions and the easiest place for grounding to lapse unnoticed.
- **G5.2 — Limits and errors are not consolidated.** No single rate-limit / quota / error-code
  reference; the information is distributed across feature pages.

## J6 — Understand a shipped change and any required action

Coverage: **Partial**

Changelog tab: Monthly Summary (3), Enterprise Releases (5), Product Releases (1),
SDK Releases (2). Tooling already exists: `.claude/skills/update-changelog/SKILL.md` and
`.cursor/commands/document-a-release.md`.

Gaps:

- **G6.1 — Changelog contract compliance unaudited.** §2 requires release identity/date,
  applicability, what changed, and migration impact. Existing entries need to be checked
  against that.
- **G6.2 — This is the natural INIT 2 pilot.** Handoff §4 makes docs-native engineering
  changelogs the canonical docs→KB origination path, and the release-authoring workflow
  already exists here. It is the cheapest place to prove the MCP contribution round trip.

---

## Cross-cutting gaps

- **X1 — Dual product vocabulary.** "Portkey" is the product name throughout the prose;
  "Prisma AIRS" appears only in the PANW logo, one CTA snippet, and deployment/enterprise
  pages. Handoff §2 requires "a controlled product vocabulary." A naming decision and a
  term-by-term rule (what is renamed vs. what stays, e.g. `portkey_ai`, `PORTKEY_*` headers,
  `api.portkey.ai`) is a prerequisite for authoring, not a cleanup task afterwards.
- **X2 — Deprecated version still published.** "Virtual Keys (Deprecated)" is a full second
  navigation version. Decide whether it is in the assigned AI Gateway scope.
- **X3 — Public exports.** `llms.txt` / `llms-full.txt` are enabled. §3 rule 6 and §7 gate 4
  require these to be checked for private material before any publication.
- **X4 — Legacy `virtual_key_old/` directory** exists in the tree; confirm it is unreferenced.

## Contradictions to resolve with the KB

Not findings — questions. Sourced from the internal RFP knowledge file, which is explicitly
**not** KB-accepted knowledge (see `00-capability-register.md`). Each needs a KB answer
before the affected page can be republished.

1. **Identity.** The RFP knowledge states SSO/SCIM for Prisma AIRS AI Gateway are delivered
   by Strata Cloud Manager / Common Services IAM, and that
   `product/enterprise-offering/org-management/sso` and `.../scim/*` are "not applicable"
   for customer-facing use. Those pages are currently published. If accurate, this is a
   published-and-wrong condition affecting ~6 pages, not a gap.
2. **Tenancy hierarchy.** RFP knowledge describes four enforcing tiers
   (Organisation → Department → Team → User/Application); the docs describe organizations and
   workspaces. Reconcile.
3. **Module naming.** RFP knowledge uses licensing labels (Enterprise, Agent Gateway,
   Observability Suite, Guardrails Engine, Model Catalog, Prompt Studio) that partly but not
   exactly match the navigation groups. Confirm which vocabulary is public.

## Proposed vertical slice (INIT 1 step 5)

One page per contract type, chosen to exercise the full pipeline on the narrowest surface —
and chosen so that every one of them is blocked on something worth discovering early:

| Contract | Candidate | Why this one |
|---|---|---|
| Concept | `product/ai-gateway` | Forces the J1 boundary and X1 naming decisions |
| Quickstart | `introduction/make-your-first-request` | Forces the G2.1 onboarding-path answer |
| How-to | `product/ai-gateway/fallbacks` | Self-contained, high-traffic, dense in claim-bearing defaults |
| Reference | one Gateway API endpoint | Forces the G5.1 OpenAPI-vs-KB authority question |
| Troubleshooting | new: fallbacks not triggering | Net-new page; proves the gap→contribution path |
| Changelog | next real release | Proves the docs→KB contribution path with existing tooling |
