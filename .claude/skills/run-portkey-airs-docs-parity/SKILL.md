---
name: run-portkey-airs-docs-parity
description: Check and drive Portkey vs Prisma AIRS (aigw/) docs parity. Use when asked to sync aigw, find root doc changes not yet mirrored into aigw/, run the aigw parity/anchor/prose-endpoint checks, start the Mintlify preview, or screenshot a root page next to its aigw twin.
---

The repo has two doc trees: the Portkey root tree (`product/`, `integrations/`, ...) and the Prisma AIRS copy under `aigw/`. Engineering edits the root tree, so `aigw/` drifts. Drive parity work with `.claude/skills/run-portkey-airs-docs-parity/driver.mjs`. It has three subcommands: `drift` finds unmirrored root changes, `checks` runs the aigw scripts and diffs them against a clean base, and `shots` screenshots both renderings from `mint dev`.

Run everything from the repo root. Artifacts go to `/tmp/aigw-parity/`.

## Prerequisites

Tested on macOS with Node 26, Python 3, Google Chrome installed, and `mint` on PATH (`npm i -g mint`). `shots` drives the system Chrome through `playwright-core`, installed once outside the repo so `package.json` stays untouched:

```bash
mkdir -p ~/.cache/aigw-parity-driver && cd ~/.cache/aigw-parity-driver && npm init -y >/dev/null && npm i playwright-core@1.49.1 --silent
```

`drift` and `checks` need only `git`, `node` and `python3`. Run `git fetch origin` first: both default to `origin/main`.

## Run (agent path)

### 1. What needs syncing: `drift`

```bash
node .claude/skills/run-portkey-airs-docs-parity/driver.mjs drift --since 8d6c87ad --to origin/main
node .claude/skills/run-portkey-airs-docs-parity/driver.mjs drift --to HEAD -v
```

Without `--since`, the driver takes the sync point from the newest commit whose message contains `docs(aigw): sync Portkey-side changes` and `up to <sha>`. **Keep writing "up to <sha>" in sync commit messages** or auto-detection breaks. It scans root `.mdx` changes (excluding `aigw/`, `changelog/`, `api-reference/`, `virtual_key_old/` and `mintlify/`). It prints one line per commit and file:

| verdict | meaning |
|---|---|
| `MIRRORED` / `MIRRORED (removal)` | every substantive added line (or deletion) is already in the aigw twin |
| `PARTIAL n/m` | some lines are missing. Often intentional rewording; check with `-v` |
| `MISSING 0/m` | nothing ported |
| `... removed line(s) still in aigw` | root deleted text that aigw still has |
| `NEW PAGE, no aigw twin` / `NO aigw twin` | needs a new aigw page and a `docs.json` entry, or a deliberate skip |
| `ROOT PAGE DELETED, aigw twin still exists` | root removed the page; decide whether aigw drops it too (and its nav entry) |
| `MIRRORED (page deleted in both)` | root deleted the page and aigw has no twin |
| `SUPERSEDED` | a later commit in the range changed these root lines again; the later commit is the one to port |

`-v` prints each added line it couldn't find in aigw. Comparing against `--to HEAD` after porting is the self-check. The only remaining PARTIALs should be deliberate rewording.

### 2. Checks against a clean base: `checks`

```bash
node .claude/skills/run-portkey-airs-docs-parity/driver.mjs checks
```

This runs `aigw/scripts/check_nav_page_parity.py`, `check_anchors.py` and `check_prose_endpoints.py` on the working tree, then again on a temporary `git worktree` of `--base` (default `origin/main`). It prints the diff for each script and removes the worktree when done. `check_anchors` and `check_prose_endpoints` exit 1 on `main` today because of stale KNOWN entries. That's the baseline: **judge by the diff, not the exit code.** The driver exits 1 only if a script fails here but passes on base, or crashes.

### 3. Rendered comparison: `shots`

Start the preview in the background, logging to the path the driver reads:

```bash
mkdir -p /tmp/aigw-parity && mint dev --no-open > /tmp/aigw-parity/mint.log 2>&1   # run in background
grep -q 'preview ready' /tmp/aigw-parity/mint.log && grep -o 'localhost:[0-9]*' /tmp/aigw-parity/mint.log | tail -1
```

With a warm Mintlify cache the preview was ready in about 11s. Then pass root-tree page paths (no `.mdx`, no `aigw/` prefix):

```bash
node .claude/skills/run-portkey-airs-docs-parity/driver.mjs shots product/ai-gateway/decisions-api product/model-catalog/workload-identity-federation
node .claude/skills/run-portkey-airs-docs-parity/driver.mjs shots product/model-catalog/workload-identity-federation --top
```

For each page it loads `/<page>` and `/aigw/<page>` and prints the `h1` along with `OK`, `404` (the aigw twin is missing or not in nav) or `FAIL` (no `<h1>` rendered within `--wait` seconds, default 120, or the page errored). It writes `/tmp/aigw-parity/shots/<page__path>.{root,aigw}.png`. `--top` captures only the first 1400×1000 viewport. Use it for checking nav, title and breadcrumbs, because full-page shots of long pages run to 7000+ px and come out unreadable when viewed. The port comes from `mint.log`; override it with `--port N`. Exit code 1 if any page 404s, fails or throws.

Stop the preview by stopping the background task (or `Ctrl-C` in a terminal).

## Porting workflow this supports

1. `drift` lists the work.
2. Port each change into `aigw/<same path>` using the aigw wording: `aigw.portkey.ai`, `Authorization: Bearer` in curl, the `/aigw/` link prefix, "the AI Gateway" instead of Portkey, UK spelling in prose, no Portkey SDK sections, and Strata Cloud Manager links instead of `app.portkey.ai`.
3. Large rewrites where `git apply --directory=aigw` fails: 3-way merge with `git merge-file --theirs -p aigw/<f> <root-before> <root-after>`, then reapply the wording above.
4. `drift --to HEAD -v`, then `checks`, then `shots` on every touched page.

## Gotchas

- **Port 3000 is often taken** by another `mint dev`. Mintlify silently moves to 3001 and so on, and only the log says which. `shots` reads the port from `/tmp/aigw-parity/mint.log`, so log to exactly that path or pass `--port`.
- **One long-lived Chrome dies after a few full-page captures** (`page.goto: Target page, context or browser has been closed` on the third page). The driver launches a fresh browser for every page. Don't "optimise" that back to a shared browser.
- **`git apply --directory=aigw` never applies cleanly.** Every hunk's context differs in wording ("Portkey" vs "The AI Gateway", `/aigw/` links). Go straight to `git merge-file`.
- **`merge-file --theirs` brings back content aigw deliberately removed.** In the Nov 2026 sync it restored the `/prompts/{promptId}/completions` rows (Prompt Studio is banned in aigw) and replaced aigw's own `/aigw/api-reference/...` links with root ones. Read the whole diff afterwards.
- **Some engineers now mirror their own changes into aigw** (Prometheus, Bedrock and the performance page did in Oct 2026). `drift` shows them as `MIRRORED`, so don't port them twice.
- **PARTIAL is expected where aigw has only curl**: `03abe08f` stays `PARTIAL 1/4` because root's Python and Node SDK `model=` lines have no aigw counterpart, and aigw's curl uses `@provider-slug/` model prefixes.
- **The `drift` matcher is case-sensitive and keeps punctuation inside tokens**, so `apiKey` → `api_key`, `max-tokens` → `max_tokens` and URL-only fixes all show up. It normalises only the known tree differences: Portkey/AI Gateway naming (case-insensitive), `organisation`/`behaviour`, the `/aigw/` prefix on internal links, `app.portkey.ai/...` vs Strata Cloud Manager URLs (same console link), and `PORTKEY_API_KEY`/`AIGW_API_KEY`/`API_KEY` placeholders. Each commit is judged against where root ended up, so lines a later commit replaced are skipped. Lines of 20+ normalised characters may match anywhere in the twin; shorter ones (`"max_age": 300`, `## Azure OpenAI`) must equal a whole twin line. Restructured tables, rewritten sentences and pages at a different aigw path (e.g. `/aigw/product/policies/budget-limits`) still show as PARTIAL, and an unported page with lots of shared JSON keys can show a low `PARTIAL n/m` rather than `MISSING`.
- **Zsh doesn't word-split `$VAR`.** `for f in $FILES` runs once with the whole string. Use an array (`F=(a b); for f in $F`) when scripting over files.

## Troubleshooting

- **`check_prose_endpoints.py` → `URLError ... CERTIFICATE_VERIFY_FAILED: self-signed certificate in certificate chain`**: corporate TLS interception. `checks` exports the macOS keychain CAs to `/tmp/aigw-parity/cas.pem` and sets `SSL_CERT_FILE` automatically. When running the script by hand, do the same: `security find-certificate -a -p /Library/Keychains/System.keychain /System/Library/Keychains/SystemRootCertificates.keychain > /tmp/aigw-parity/cas.pem; SSL_CERT_FILE=/tmp/aigw-parity/cas.pem python3 aigw/scripts/check_prose_endpoints.py`.
- **`check_nav_page_parity` on base reports `file is unreachable from navigation` for your new page**: you compared using `git stash`, which leaves untracked files in place. `checks` uses a real worktree for this reason.
- **`No sync commit on origin/main says "up to <sha>"`**: the last sync isn't merged yet, or its message lacked "up to". Pass `--since <sha>`, which is recorded in the sync PR description.
- **`playwright-core missing`**: run the Prerequisites install line. The driver resolves it from `~/.cache/aigw-parity-driver`.
- **`shots` prints `FAIL ... no <h1> rendered within Ns`**: the page shell loaded but the doc content never rendered; check `mint.log` for errors. The screenshot is still saved. Use `--wait 10` to fail fast when probing.
- **`shots` prints `FAIL ... page.goto: net::ERR_CONNECTION_REFUSED`**: the preview isn't up yet, or is on another port. Check `mint.log` for `preview ready` and the port.
