# Handoff: the Prisma AIRS OpenAPI specification

For the agent building the new OpenAPI repository. Answers Q6's source question; the grounding
question stays open and is described below.

Context: `Portkey-AI/openapi` currently feeds this repo's API reference. It is Portkey-corpus
tooling. The new repository replaces it as the Prisma AIRS source.

## Read this first

**An OpenAPI specification is published documentation, not configuration.**

219 pages in this repo render directly from the spec. Every `summary`, `description`, example
and enum note in it becomes public prose on the docs site and in `llms.txt` / `llms-full.txt`.
So handoff §3 rule 2 applies to the spec exactly as it applies to a hand-written page: every
substantive assertion needs accepted KB support.

This is the easiest place in the whole corpus for grounding to lapse, because a spec does not
feel like writing. It feels like filling in fields.

## The trap: do not fork and rebrand

The obvious move is to clone `Portkey-AI/openapi`, rename things, and ship. That inherits every
ungrounded assertion in it, laundered through a new repository into a corpus that is supposed
to be re-grounded.

Handoff §3 rule 7: published documentation is not corroboration of its own claims. The existing
spec's descriptions are published documentation.

The line to hold — and this is the whole instruction in one sentence:

> **Inherit the shape. Re-ground the prose.**

| Carry over | Do not carry over |
|---|---|
| Paths and methods | `summary` |
| Schema structure, property names, types | `description`, at every level |
| `required` lists, enum *values* | Explanatory prose in examples |
| Status codes, error shapes | `info.description` |
| Security scheme definitions | Tag descriptions |
| Parameter names and locations | Any stated limit, default, or behaviour |

The distinction is not arbitrary. Everything in the left column is **machine-verifiable against
the running API** — send a request, compare the response, and the claim is settled without the
KB. Everything in the right column is an assertion about behaviour that only the KB can
support. The left column can be inherited *and tested*. The right column cannot be inherited at
all.

Where the KB does not yet support a description, **leave it empty**. An empty description
renders as a visible gap and shows up in coverage. A confident, plausible, wrong description is
invisible and will survive review. Empty beats invented, every time.

## The join key: method + path

Pages bind to operations through frontmatter:

```yaml
---
title: "Chat"
openapi: post /chat/completions
---
```

219 pages do this. **The method+path pair is the contract between the spec and the docs**, so
path stability is a documentation concern and not only an API design concern. Renaming a path
silently unbinds a page — the page still builds, it just stops rendering an operation.

If a path must change, it is a docs migration, not a spec edit. Flag those explicitly in the
handoff back.

## Naming rules

[`05-naming-rules.md`](./05-naming-rules.md) applies, and its rule of thumb — *if a reader
would type it or a machine would parse it, it does not change* — resolves unusually cleanly
here, because a spec is mostly machine-parsed.

**Never renamed:**

- `servers[].url` — `api.portkey.ai`
- Header parameters — `x-portkey-api-key`, `x-portkey-provider`, every `x-portkey-*`
- `operationId` values
- Component and schema names
- Property names, enum values
- Security scheme keys

**Rebranded:**

- `info.title` → `Prisma AIRS AI Gateway API`
- `info.description` and every `description` / `summary` — subject to grounding, so rewrite
  rather than translate
- Tag descriptions

**Judgement call, flag rather than decide:** `tags[].name`. Tag names are simultaneously
display text (they drive navigation grouping) and reference keys (operations point at them).
Renaming affects both. Raise it rather than choosing.

## Provenance: design the extension now

The spec has to participate in the claim→section dependency index
([`03-provenance-model.md`](./03-provenance-model.md)), or 219 pages become a hole in it. Use
OpenAPI's `x-` extension mechanism, per operation and per documented property:

```yaml
paths:
  /chat/completions:
    post:
      summary: ""            # empty until grounded
      x-airs-provenance:
        claims:
          - id: "accepted-claim-id"
            revision: "claim-revision-or-digest"
        origin_kind: human   # human|generated|mixed
        text_digest: "sha256-of-the-description"
```

Add the field shape from the start even while `claims` is empty. This is the same argument as
the dependency index itself: it costs nothing while authoring and is prohibitively expensive to
retrofit, because reconstructing which claim supported a description after the fact is
indistinguishable from inventing it.

`origin_kind` and `text_digest` are also what make echo protection work if any description is
ever machine-drafted. See [`07-reconciliation-loop.md`](./07-reconciliation-loop.md).

## One spec, no variants

Q12, 2026-09-07: launch covers managed and hybrid, and **product behaviour is
deployment-invariant.** Do not produce environment-variant specs or fork descriptions per
deployment. Multiple entries in `servers[]` are fine; divergent content is not.

## Validation is currently absent — the new repo should own it

Recorded because it contradicts an earlier entry in
[`00-capability-register.md`](./00-capability-register.md), now corrected.

`.github/workflows/openapi-validate.yml` in this repo runs
`openapi-spec-validator openapi.yaml` against the **docs-core repository root**, where no
`openapi.yaml` exists. `gh run list` shows no run history for the workflow at all. Meanwhile
`docs.json` reads the spec from
`raw.githubusercontent.com/Portkey-AI/openapi/refs/heads/master/openapi.yaml` — a completely
different artifact from the one CI names.

So there is no working spec validation in this repository today. The new repo should validate
in its own CI, on its own file, and prove it with a run history rather than a workflow file.

Note that `mint validate` in docs-core *does* fetch and check the remote spec — it reports
`OpenAPI definition is valid`. That is the real check today, and it lives on the docs side.

## Still open — do not assume either way

**Q6, grounding status.** Naming the source did not settle whether the new spec is *ingested
into the KB* so its assertions become accepted knowledge, or carries a *recorded exemption*
under §3 rule 1. Both are coherent; silence is not.

Build for ingestion regardless — populate `x-airs-provenance` — because that is the option
that keeps rule 1 intact, and it is a no-op if an exemption is granted later.

**Q2, KB access.** Not yet available from the docs workspace. Until it is, the same constraint
that blocks page authoring blocks description authoring. Structural work — paths, schemas,
types, provenance scaffolding, CI — is unblocked and is the right thing to do first.

## Suggested order

1. Structure only. Paths, methods, schemas, types, required, enums, security. Verified against
   the running API, not against the old spec.
2. CI that validates, with run history.
3. `x-airs-provenance` scaffolding on every operation, `claims` empty.
4. Naming pass over prose fields — titles and tag descriptions. Leave `description` empty
   rather than porting.
5. **Stop.** Descriptions wait for the KB.

Steps 1–4 need no KB access and are worth doing now. Step 5 is where the handoff comes back.
