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

## How the docs should consume it — do not repeat the current pattern

Everything in this section was verified against the installed `mint` CLI **4.2.876** by reading
`@mintlify/validation` schemas and `@mintlify/common` / `@mintlify/scraping` type definitions.
Web access is blocked from this workspace, so it was not read from Mintlify's own
documentation — treat it as accurate for this CLI version and worth confirming against their
docs before relying on the finer points.

### What this repo does today, and why not to copy it

219 hand-written `.mdx` stub files, each one binding to a single operation by frontmatter:

```yaml
---
title: "Chat"
openapi: post /chat/completions
---
```

Each is separately listed in `docs.json` navigation, and several carry a manually pasted
snippet import. Adding an endpoint means writing a file and editing navigation. This is the
"inefficient way" — it is 219 files of hand-maintained coupling.

Consequence while it lasts: **method+path is the join key.** Renaming a path silently unbinds a
page — it still builds, it just stops rendering an operation. A path change is a docs migration,
not a spec edit.

### What to build instead

`groupSchema` accepts `openapi`, `asyncapi`, `tag`, `directory` and `expanded` alongside
`pages`. Putting `openapi` on a navigation **group** makes Mintlify generate a page per
operation:

```json
{
  "group": "Endpoints",
  "openapi": {
    "source": "https://raw.githubusercontent.com/<org>/<spec-repo>/main/openapi.yaml",
    "directory": "api-reference",
    "overlays": ["overlays/docs-prose.yaml"]
  }
}
```

No stub files, no per-endpoint navigation entries, no join key to keep in sync. `tag` on a
group filters operations into it, so tag structure in the spec becomes navigation structure.

Only HTTPS sources are accepted; HTTP requires the CLI's `--local-schema` flag.

### Overlays are the important find

`openapi.overlays` takes **OpenAPI Overlay documents, applied in order**. From the schema's own
description: *"An empty array disables all overlays for this specification, including
auto-discovered ones"* — so Mintlify auto-discovers overlay files as well as honouring explicit
ones.

This solves a problem the rest of this handoff could only work around. The spec can stay a
clean engineering artifact holding structure, while documentation prose lives in a **separate
overlay document** applied at build time:

| Artifact | Owner | Content | Review |
|---|---|---|---|
| `openapi.yaml` | Engineering | Paths, schemas, types, required, enums, security | API review |
| `overlays/docs-prose.yaml` | Docs | `summary`, `description`, examples, tag prose | **Grounding gate** |

That is *inherit the shape, re-ground the prose* expressed as two files instead of as a
discipline. The grounding gate applies to the overlay, which is small and entirely prose, and
engineering can ship structural changes without touching a single grounded assertion.

Strong recommendation: adopt this split from the start. Retrofitting it means unpicking prose
from a spec that has already merged them.

### `x-mint`, the vendor extension

Operations and schemas accept an `x-mint` object. Verified fields:

| Field | Effect |
|---|---|
| `metadata` | Page meta tags — becomes generated-page frontmatter |
| `content` | Extra MDX injected into the generated page |
| `pre` / `post` | MDX before and after the generated body |
| `href` | Override the generated page URL |
| `groups` | Assign the operation to navigation groups |
| `playground` | `{ expand }` — playground display |
| `mcp` | `{ enabled, name, description }` — expose the operation as an MCP tool |

Also available: `x-hidden` and `x-excluded` on operations, and `x-mint-enum` on schemas for
enum display names.

Two notes. `x-mint.content` / `pre` / `post` remove the last real reason to keep stub files —
per-endpoint custom prose no longer requires one. And `x-mint.mcp` is worth a deliberate
decision rather than a default, since it determines which operations become agent-callable
tools; that is a product surface, not a docs setting.

Everything under `x-mint` that is prose is **published documentation** and inherits the
grounding rule. Prefer putting it in the overlay.

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

## Authority: the spec is a second trusted source — recorded exemption

**Decided 2026-09-07 (Q6).** The OpenAPI specification is a **key source of trusted knowledge
that sits outside the KB corpus.** It is not subordinate to the KB and is not merely an
ingestion input.

This is a deliberate deviation from handoff §3 rule 1, which names the KB the *sole* factual
authority, and it is written here as the explicit recorded exemption that Q6 asked for. It is
scoped to the API specification. It does not weaken grounding anywhere else, and it must not be
cited as precedent for a second exemption.

The operating rules:

1. **Two trusted sources, one truth.** The spec and the KB are both authoritative in their
   domains. Neither silently overrides the other.
2. **Conflicts are resolved by maintainers.** Never automatically, never last-write-wins. This
   is the same principle §5 already applies to KB conflicts, extended to the spec.
3. **They must stay in sync, and drift from *either* side is raised.** Drift is a defect
   regardless of which artifact moved. There is no "authoritative" side to fall back on.
4. **Sync is bidirectional and webhook-driven.** A spec change fires a webhook to the KB; a KB
   change fires a webhook to the spec repository.

### What this changes downstream

[`07-reconciliation-loop.md`](./07-reconciliation-loop.md) was designed as a two-node loop, KB
↔ docs. It is now **three-node**: KB ↔ spec ↔ docs. Three consequences, recorded there:

- Drift detection needs a KB↔spec comparison, not only KB↔docs.
- Webhooks on both sides give the loop real push triggers, so polling becomes the backstop
  rather than the mechanism.
- A KB↔spec contradiction is a maintainer decision with no diff to review — structurally the
  same as tier 3, and it inherits tier 3's handling.

### What it means for this repository

Keep populating `x-airs-provenance`. Its purpose shifts slightly but does not go away: it is no
longer only "which KB claim supports this description," it is also the **join key that makes
drift detectable**. Without a claim reference on an operation, nothing can tell that the KB
moved and the spec did not.

## Still open

**Q2, KB access.** Not yet available from the docs workspace, and the webhook contract in both
directions depends on it. Until then, description authoring is blocked exactly as page
authoring is. Structural work — paths, schemas, types, overlay split, provenance scaffolding,
CI — is unblocked and is the right thing to do first.

## Suggested order

1. Structure only. Paths, methods, schemas, types, required, enums, security. Verified against
   the running API, not against the old spec.
2. CI that validates, with run history.
3. **Split prose into an overlay** from the first commit — `openapi.yaml` for structure,
   `overlays/docs-prose.yaml` for everything a reader reads. Cheap now, painful later.
4. `x-airs-provenance` scaffolding on every operation, `claims` empty.
5. Naming pass over prose fields — titles and tag descriptions. Leave `description` empty
   rather than porting.
6. Tag structure, deliberately: tags become navigation groups under the group-level `openapi`
   config, so tag design is information architecture.
7. **Stop.** Descriptions wait for the KB.

Steps 1–6 need no KB access and are worth doing now. Step 7 is where the handoff comes back.

Two things to hand back rather than decide: the `tags[].name` question above, and which
operations should carry `x-mint.mcp` — that one is a product surface decision.
