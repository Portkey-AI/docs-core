# Release assertion files

One YAML file per release, written by step 4a of the `update-changelog` skill.

Filename: `<repo-short>@<tag>.yaml` — e.g. `gateway-enterprise-node@v2.21.0.yaml`.

## What these are

The discrete product facts a release establishes, separated from the prose that describes
them. Two jobs:

1. **Today** — a review artifact. A reviewer can check *what the release claims* without
   re-reading the changelog wording, and can see which existing facts it invalidated.
2. **Once KB MCP access exists** — the payload for the docs→KB contribution (step 4b). See
   [`../06-changelog-contribution-path.md`](../06-changelog-contribution-path.md).

## Why they live here and not in `changelog/`

`changelog/*.mdx` is built and published by Mintlify. These live under `_project/`, which the
repo-root `.mintignore` excludes from the build and therefore from `llms.txt` /
`llms-full.txt`.

The `.yaml` extension is not what protects them — Mintlify processes `.md` too, and an
unreferenced path is still a built path. `.mintignore` is the mechanism.

They are not secret — everything in them becomes public in the changelog entry anyway. They
are simply not *pages*.

## Field reference

See the template in `.claude/skills/update-changelog/SKILL.md`, step 4a.

The field that carries the most weight is `supersedes`. Net-new capabilities are easy; the
expensive case is a release that quietly changes a documented default, because nothing in the
release notes flags that a guide is now wrong. `supersedes` plus `affects` is the record of
that, and it is what the claim→section dependency index will eventually replace with a
deterministic lookup.

## Backfill

Not required. These start with the next release. Existing changelog entries are not
retro-fitted — under handoff §3 rule 7, published prose is not evidence of its own facts, so
a backfill would be inventing assertions rather than recording them.
