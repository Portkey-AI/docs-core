#!/usr/bin/env bash
#
# Mirror the Prisma AIRS OpenAPI specification into this repository.
#
# We cannot point docs.json at the Palo Alto Networks GitHub organisation, so
# aigw/airs-openapi.yaml is a committed mirror rather than a remote fetch. This
# script is the only supported way to refresh it.
#
# The mirror is flattened: overlays/docs-prose.yaml is applied at sync time so
# the docs build consumes a single self-contained file. Structure and prose stay
# split in the source repository, which is where that split earns its keep.
#
# Usage:
#   aigw/_project/sync-openapi.sh [path-to-spec-repo]
#
# The mirror is generated. Never hand-edit aigw/airs-openapi.yaml — fix the
# source repository and re-run this.

set -euo pipefail

SPEC_REPO="${1:-$HOME/Documents/Projects/openapi/openapi}"
DOCS_REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
MIRROR="$DOCS_REPO/aigw/airs-openapi.yaml"

if [[ ! -d "$SPEC_REPO/.git" ]]; then
  echo "error: no git repository at $SPEC_REPO" >&2
  echo "       pass the spec repo path as the first argument" >&2
  exit 1
fi

branch=$(git -C "$SPEC_REPO" rev-parse --abbrev-ref HEAD)
if [[ "$branch" != "main" ]]; then
  echo "error: spec repo is on '$branch', not main" >&2
  echo "       we mirror main only; check it out and re-run" >&2
  exit 1
fi

if [[ -n "$(git -C "$SPEC_REPO" status --porcelain)" ]]; then
  echo "error: spec repo has uncommitted changes" >&2
  echo "       a mirror of a dirty tree is not reproducible; commit or discard first" >&2
  exit 1
fi

python="$SPEC_REPO/.venv/bin/python"
[[ -x "$python" ]] || python=python3

sha=$(git -C "$SPEC_REPO" rev-parse HEAD)

"$python" "$SPEC_REPO/scripts/apply_overlay.py" \
  "$SPEC_REPO/openapi.yaml" \
  "$SPEC_REPO/overlays/docs-prose.yaml" \
  -o "$MIRROR"

echo
echo "mirrored $sha -> aigw/airs-openapi.yaml"
git -C "$DOCS_REPO" --no-pager diff --stat -- aigw/airs-openapi.yaml || true
echo
echo "Commit with the source SHA in the message so drift stays traceable:"
echo "  docs(aigw): sync airs-openapi.yaml from openapi@${sha:0:7}"
