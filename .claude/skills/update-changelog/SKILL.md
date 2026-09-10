---
name: update-changelog
description: Add a release entry to a Portkey changelog file (enterprise gateway, backend, frontend, SDKs, helm chart, etc.) from a GitHub release URL or version tag, and update related documentation when new features warrant it.
---

# Update Portkey Changelog

This skill drives the workflow for adding a new release entry to one of the changelog files under `docs-core/changelog/` based on a GitHub release. It also looks for documentation pages that need to be updated for new user-facing features.

## Usage

```
/update-changelog <RELEASE_URL_OR_TAG> [--repo <OWNER/REPO>] [--changelog <FILE>]
```

Examples:

```
/update-changelog https://github.com/Portkey-AI/gateway-enterprise-node/releases/tag/v2.9.0
/update-changelog v1.13.0 --repo Portkey-AI/albus --changelog backend.mdx
```

If only a tag is provided, infer the repo from the changelog file (see mapping below) or ask the user.

## Repo ↔ Changelog file mapping

| Changelog file | GitHub repo | Notes |
|---|---|---|
| `enterprise.mdx` | `Portkey-AI/gateway-enterprise-node` | Enterprise Gateway |
| `open-source.mdx` | `Portkey-AI/gateway` | OSS Gateway |
| `backend.mdx` | `Portkey-AI/albus` | Control plane |
| `frontend.mdx` | `Portkey-AI/luna` | Dashboard UI |
| `data-service.mdx` | `Portkey-AI/data-service` | Air-gapped data service |
| `helm-chart.mdx` | `Portkey-AI/helm-chart` | Helm charts |
| `python-sdk-changelog.mdx` | `Portkey-AI/portkey-python-sdk` | Python SDK |
| `node-sdk-changelog.mdx` | `Portkey-AI/portkey-node-sdk` | Node SDK |

If the user does not specify a target file, ask which changelog to update.

## Workflow

### 1. Fetch the release notes

```bash
gh release view <TAG> --repo <OWNER/REPO>
```

This returns the title, body, and the auto-generated PR list. Capture the publish date — use it as the `description` attribute on the `<Update>` block (format `YYYY-MM-DD`, in the user's preferred timezone — local date is fine).

### 2. Read the existing changelog file

Read the target file end-to-end (or at least the first 200 lines) to:
- Match the existing tone and section conventions (e.g., `### Provider Updates`, `### Fixes and Improvements`)
- Confirm the current top entry's version and the format used for the `sidebarTitle` frontmatter (e.g., `"Enterprise Gateway [2.8.0]"`)
- Check if any prior entries warned about deprecations or planned changes that this release follows up on

### 3. Triage the PR list

The release body lists every merged PR. Bucket each PR into:

- **Highlight** — new providers, new endpoints, new guardrails, major features, security-relevant fixes (call them out individually)
- **Provider update** — single-provider behavior changes
- **Fixes and Improvements** — small bug fixes, dependency bumps, internal cleanup
- **Skip** — chore/CI/refactor/docs PRs with no user impact (e.g., "remove redundant env", "audit fix", internal-only test changes)

For PRs with empty bodies, fetch additional context only when the title is ambiguous:

```bash
gh pr view <NUM> --repo <OWNER/REPO> --json title,body
```

Don't fetch every PR — most titles are clear. Batch the unclear ones in parallel `gh pr view` calls.

### 4. Find relevant documentation for every entry

**Always link to documentation.** For every entry — feature, provider update, or fix — search for the most relevant existing doc page and link to it inline. If there's no page specifically for the new thing, link to the nearest umbrella page so readers know how to use the surrounding feature.

Examples of "nearest umbrella" linking:
- New guardrail partner with no dedicated page → link `/product/guardrails` so users can see how to configure any guardrail
- New LLM provider with no dedicated page → link `/integrations/llms` (the provider landing)
- New unified-API parameter with no dedicated section → link the relevant API reference page (e.g., `/api-reference/inference-api/responses/responses`)
- New env var → link the closest self-hosting / feature page that already documents related env vars

For each entry, run a quick search before writing the bullet:

```bash
# Provider features
find docs-core/integrations/llms -iname "*<provider>*"
grep -r "<feature-keyword>" docs-core/integrations/llms/<provider>* docs-core/product/

# Guardrails
find docs-core/integrations/guardrails -iname "*<guardrail>*"

# Config / API features
grep -rn "<param-name>" docs-core/product/ai-gateway/ docs-core/api-reference/
```

Match the link style used in the previous 2-3 entries of the target file — usually `[Feature Documentation](/path)` on its own line below the description, or the feature name wrapped as a link.

If existing doc text is now stale because of this release, **update it** — don't just add the changelog entry. Common cases:

- **Config schema change** (new field on targets, strategy, etc.) → update **both**:
  - `product/ai-gateway/configs.mdx` (narrative)
  - `api-reference/inference-api/config-object.mdx` (schema table)
- **Provider behavior change** (new param support, new auth mode, fix) → update the relevant `integrations/llms/<provider>.mdx` section if it's now wrong or incomplete
- **New env var** → mention in the changelog entry; usually no separate doc page exists, but check `self-hosting/` if it's deployment-related
- **New parameter on a unified API** → check the API reference pages under `api-reference/inference-api/`

If a doc page **doesn't yet exist** for the feature, do NOT auto-create one — these are typically larger tasks (e.g., new provider pages need `docs.json` navigation updates). Instead, **flag it in the final summary** so the user can scope a follow-up. Cases that usually warrant a new page:

- New LLM provider → `integrations/llms/<provider>.mdx`
- New guardrail partner → `integrations/guardrails/<name>.mdx`
- New API endpoint → `api-reference/inference-api/<endpoint>.mdx`

**Never write a `[Docs](...)` link without verifying the file exists.** Broken links erode trust in the changelog.

### 4a. Extract factual assertions

Before writing any prose, write down the discrete facts the release establishes. Save to
`prisma-airs/_project/releases/<repo-short>@<tag>.yaml`.

This is the input to the KB contribution step (added once KB MCP access exists — see
`prisma-airs/_project/README.md`, "Changelog contribution path"). Until then it stands on its own as
a review artifact: it makes the release's factual content inspectable separately from how it
was worded.

```yaml
release:
  id: "gateway-enterprise-node@v2.21.0"
  repo: "Portkey-AI/gateway-enterprise-node"
  date: "2026-08-14"
  source_revision: "<git-sha of the tag>"
assertions:
  - id: r1
    text: "<one factual statement, stated plainly>"
    kind: new-capability        # new-capability|behavior-change|default-change|fix|deprecation
    applies_to: "<version or environment the fact holds for>"
    supersedes: []              # existing facts this invalidates; [] if net-new
    affects: []                 # doc routes carrying the superseded fact
```

Rules:

- **One assertion per fact, not per PR.** A PR can establish several facts, and several PRs
  can establish one. Bucket by fact.
- **State the fact, not the change to the docs.** ✅ `"Default request timeout is 60s"` —
  ❌ `"Updated the timeout section"`.
- **`supersedes` is the field that matters.** A release that changes a default doesn't only
  add a fact, it invalidates one. That invalidation is what identifies stale pages. Populate
  it by searching for the current documented value:
  ```bash
  grep -rn "<old-value-or-param>" product/ api-reference/ self-hosting/
  ```
  Put whatever routes that finds into `affects`.
- **`kind: fix` assertions usually have empty `supersedes`** — a bug fix restores documented
  behavior rather than changing it. If a fix *does* change documented behavior, it is a
  `behavior-change`, not a fix.
- **Skip non-facts.** Dependency bumps, CI changes, and internal refactors produce no
  assertions even when they produce changelog lines.

### 5. Write the changelog entry

Insert a new `<Update>` block immediately after the frontmatter, **above** the previous top entry. Pattern:

```mdx
<Update label="X.Y.Z" description="YYYY-MM-DD">

## vX.Y.Z
---

### Highlight Section Title

Description...

[Optional Documentation link](/path/to/doc)

### Provider Updates

- **Provider**: Specific change
- **Provider**: Specific change

### Fixes and Improvements

- **Area**: Specific fix (one line each)
- **Security**: CVE links if applicable

</Update>
```

Notes on style:
- Use `## vX.Y.Z` followed by `---` as the in-body header (matches existing entries)
- Wrap version-blocking warnings in `<Warning>` callouts — used for things like "Deploy data-service v1.7.0+ before upgrading"
- Use `<Note>` for compatibility notes (e.g., "Requires Backend v1.13.0 or higher for Air Gapped deployments")
- **Be succinct, not verbose.** One sentence per fix; one short paragraph per feature. Cut adverbs, hedges, and "Previously, X was Y" framing unless the contrast is the actual fix
- **Always link.** Every section should end with `[Documentation](/path)` — a specific page if one exists, the nearest umbrella page otherwise. Don't write a section without a link
- Don't link to docs you haven't verified — use `find` / `Read` to confirm the path
- Group provider-specific bullets under `### Provider Updates`; one-off provider features can have their own `###` heading
- **Security dependency bumps**: don't name the package or CVE. Use the generic line `- Updated dependencies to patch security vulnerabilities.` Reserve named entries for actual functional fixes
- **Don't include refactor-only / internal-only PRs** even when their titles sound functional (e.g., "plugin id case-insensitive lookup" can refer to internal map keys, not user behavior). When in doubt, skip — don't write something that misrepresents the change

### 6. Update the `sidebarTitle`

In the frontmatter, update:

```yaml
sidebarTitle: "<Product Name> [<NEW_VERSION>]"
```

### 7. Apply documentation updates flagged in step 4 — as a separate change

A release produces **two outputs on two different clocks.** Do not merge them into one commit.

| Output | Mutability | Ships when |
|---|---|---|
| The `<Update>` changelog entry | **Immutable once published.** Corrections append a new entry; they never rewrite the old one. | With the release |
| Patches to guides / reference / API pages | Mutable — normal doc content | Once the facts are confirmed |

The reason: the changelog entry is a dated observation of what shipped. It stays true forever,
even after the behavior it describes changes again. A guide states current behavior, so it
has to keep changing. Rewriting a historical release entry to match the current guide destroys
the record of what a customer running that version actually got.

So:

- **Separate commits.** Changelog entry first, guide patches second. Separate PRs if the
  guide patches are large or need a different reviewer.
- Make the smallest possible edit to each guide — one new section, one new table row.
- Cross-link from the changelog entry to the updated doc.
- If a guide patch turns out to be wrong, fix the guide. **Never** edit the shipped
  `<Update>` block to match.
- Drive the patch list from `affects` in the step 4a assertion file, not from memory.

Once KB MCP access exists, step 4b (submit assertions to the KB) slots in here, and the guide
patches additionally wait on KB acceptance while the changelog entry does not. See
`prisma-airs/_project/README.md` under "Changelog contribution path".

### 8. Report back

End with a summary:
- Version added and the changelog file path
- The assertion file path, and the assertion count broken down by `kind`
- Any assertions with a non-empty `supersedes` — these are the facts that made existing docs stale, and they are the ones most likely to be missed
- Any docs updated (with file paths), noted as a **separate change** from the changelog entry
- Any **flagged** docs that the user should consider creating (new providers, new guardrails, new endpoints) — these are typically larger tasks involving `docs.json`

## Tips

- **Always link.** Every entry gets a doc link — specific page when one exists, nearest umbrella page otherwise (e.g., a new guardrail with no dedicated page links `/product/guardrails`)
- **Be succinct.** One sentence per fix; one short paragraph per feature. Cut filler — readers skim changelogs.
- **Run `gh release view` and `Read changelog/<file>.mdx` in parallel** — they're independent
- **Batch unclear `gh pr view` calls in parallel** — never fetch them serially
- **Use the existing entries as a style guide** — if the previous 3 entries all use a specific phrasing for "fixed X for Y", match it
- **Don't invent PRs** — only write about what's in the release body. If a PR's effect is unclear from the title, fetch its body before writing the bullet
- **Date conversion**: GitHub release `published_at` is UTC. The convention in these changelogs is local date — use the user's local date if obvious, otherwise the date in the release tag's title

## Common Pitfalls

❌ Don't write changelog entries without a doc link
✅ Link the specific page when it exists, the nearest umbrella page otherwise (new Lakera guardrail with no page → link `/product/guardrails`; new BytePlus provider with no page → link `/integrations/llms`)

❌ Don't claim docs links that don't exist
✅ Verify with `find` / `Read` before adding `[Docs](...)` links — broken links erode trust

❌ Don't pad entries with "Previously, X was Y. Now, X is Z." or hedging like "It's now possible to..."
✅ One sentence per fix, one short paragraph per feature. Lead with the change.

❌ Don't skip the `sidebarTitle` update — readers see this in the nav
✅ Always bump it to the new version

❌ Don't create new integration / guardrail / API reference pages silently
✅ Flag them in the summary so the user can scope a follow-up task

❌ Don't include every PR — chore/CI/refactor PRs without user impact belong on the cutting room floor
✅ Skip ruthlessly; the changelog is for users, not contributors

❌ Don't edit a previously published `<Update>` block to reflect current behavior
✅ Historical entries are immutable. A later release changed things — say so in the later entry. The old entry stays true for the version it describes

❌ Don't ship the changelog entry and the guide patches as one commit
✅ Two outputs, two clocks (see step 7). The entry is a dated record; the guides state current behavior

❌ Don't write assertions that describe the documentation ("updated the timeout section")
✅ Write the fact itself ("default request timeout is 60s") — assertions are product facts, not edit logs
