# Capability register

INIT 1 step 1: "Inspect supplied Mintlify and KB access; record verified capabilities and
missing integrations."

Status key: **Verified** = observed directly in this workspace. **Assumed** = inferred from
repo contents, not exercised. **Unverified** = no evidence either way. **Blocked** = attempted
and failed.

Last updated: 2026-09-07.

## Mintlify platform

| Capability | Status | Evidence |
|---|---|---|
| Mintlify project exists and is repo-backed | Verified | `docs.json` (4123 lines, `$schema: mintlify.com/docs.json`), `theme: mint` |
| Local preview toolchain | Verified | `package.json` → `mint@^4.2.38`, `mintlify@^4.0.563`, `npm run dev` |
| Navigation model | Verified | `navigation.versions[]` → 2 versions ("Latest", "Virtual Keys (Deprecated)") → 7 and 4 tabs → groups → pages |
| Native components in active use | Verified | `CodeGroup`, `Card`, `Accordion`/`AccordionGroup`, `Frame`, `Check`, MDX snippet imports |
| Snippet mechanism | Verified | `snippets/` incl. `prisma-airs-cta.mdx`, imported into pages |
| OpenAPI-backed reference | Verified | `docs.json` → `api.openapi` reads `Portkey-AI/openapi` master `openapi.yaml`; 219 pages bind to operations via `openapi: <method> <path>` frontmatter. `mint validate` fetches and checks it (`OpenAPI definition is valid`). **Portkey-corpus only** — Q6 (2026-09-07) assigns Prisma AIRS API reference to a new repository, not yet supplied |
| OpenAPI CI validation | **Not working** — corrected 2026-09-07 | `.github/workflows/openapi-validate.yml` runs `openapi-spec-validator openapi.yaml` against the docs-core root, where no such file exists; `gh run list` shows no run history. It also names a different artifact from the remote spec `docs.json` actually reads. An earlier entry cited this workflow as evidence of a verified capability — it is not. Out of scope to fix (Portkey corpus); the new spec repo owns its own validation. See [`08-openapi-handoff.md`](./08-openapi-handoff.md) |
| Machine-readable exports enabled | Verified | Footer links `llms.txt` and `llms-full.txt` — **relevant to §3 rule 6**: these are public exports and must be checked for private material |
| Redirects, SEO, contextual, metadata config | Verified | present as `docs.json` top-level keys |
| Strict build validation | Verified | `mint validate` (CLI 4.2.876, installed globally) — exits non-zero on warnings; full corpus passes |
| Build exclusion mechanism | Verified | repo-root `.mintignore`, gitignore syntax. **Mintlify parses `.md` as well as `.mdx`, and navigation omission does not exclude a file from the build or from public exports.** Defaults also ignore `.git`, `.github`, `.claude`, `.agents`, `.idea`, `node_modules`, `README.md` |
| Additional CLI checks available | Verified | `mint broken-links`, `mint a11y`, `mint test` (runnable code blocks), `mint export`, `mint format` — all unexercised so far; relevant to §7 gates 5, 6, 7 |
| Branch/PR preview and required checks | Assumed | repo has PR-merge history (`create-split-prs.sh`, merge commits); the actual Mintlify GitHub App config is not visible from the working tree |
| Publication authority (who can deploy) | Unverified | not determinable from the repo |
| Deployment-status observation API | Unverified | handoff §5 warns: do not invent a Mintlify outbound webhook. Not investigated. |
| Assigned AI Gateway edit scope | **Unverified** | see [`04-operator-questions.md`](./04-operator-questions.md) Q1 — the whole repo is currently in scope by default, which the handoff does not sanction |

Note: mintlify.com could not be fetched from this session (network egress denied), so platform
behavior above is grounded in this repository and in the locally installed CLI rather than in
current Mintlify documentation. Re-check syntax and workflow details against the live docs
during implementation, per handoff §12.

### Outstanding platform hygiene

Non-page files sit at the repo root inside the build scope and are **not** currently in
`.mintignore`: `writing-style-guide.md`, `MCP-Gateway-Roadmap.md`, `create-split-prs.sh`,
plus stray images (`Addcree.png`, `Screenshot2025-07-21at5.39.59PM.png`). They parse without
error, so they raise no warning, but they are inside the build and therefore potentially
inside the public exports. Worth a decision — deliberately left alone here because excluding
them changes existing published output and is outside the AI Gateway docs scope.

## Prisma AIRS KB

| Capability | Status | Evidence |
|---|---|---|
| KB MCP endpoint configured | **Unverified** | no KB MCP server is configured for this project |
| MCP authentication / service identity | **Unverified** | — |
| Stable claim + revision reads | **Unverified** | — |
| Public approval / status fields | **Unverified** | — |
| Pagination and change discovery | **Unverified** | — |
| Contribution (docs→KB) format | **Unverified** | — |
| Task status tracking | **Unverified** | — |
| Grounding facilities | **Unverified** | — |
| Provenance preservation through the existing docs-ingestion connector | **Unverified** | handoff §5 makes this an integration acceptance requirement |
| KB change events | **Unverified** | — |

One MCP server, `mcp-gateway`, is configured for this session and **failed to connect**
(`CONNECT_TIMEOUT`, 30s). Its name matches Portkey's own MCP Gateway product documented in
`product/mcp-gateway/`, so it is most likely the product's gateway, not the Prisma AIRS KB.
That should be confirmed rather than assumed — if it *is* the KB path, the timeout is the
single highest-priority unblock.

## Consequence

Handoff §3 rule 2 requires accepted KB support for every substantive published assertion —
numbers, defaults, limits, instructions, prerequisites, code assumptions, claimed outputs.
Rule 5 forbids invented content to fill gaps.

With zero verified KB reads, the compliant set of actions is: page contracts, editorial
standards, coverage mapping, provenance modelling, and local structure. That is what this
folder contains. Page authoring starts when a KB read is demonstrated.

## Sources deliberately *not* treated as KB

- `~/.claude/skills/rfp/knowledge/prisma-airs-ai-gateway.md` — internal RFP knowledge base.
  Rich and directly on-topic, but it is a sales artifact, not accepted public KB knowledge.
  Useful only for generating *questions* to put to the KB. See
  [`01-reader-journeys.md`](./01-reader-journeys.md) §"Contradictions to resolve".
- The existing published corpus. Handoff §3 rule 7: generated documentation cannot become
  independent corroboration of its own source claims. Existing Portkey pages are prior
  authored prose of unknown provenance, not evidence.
