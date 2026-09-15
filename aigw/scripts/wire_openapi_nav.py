#!/usr/bin/env python3
"""Wire the generated OpenAPI navigation into the Prisma AIRS version of docs.json.

Idempotent: re-running replaces the generated groups rather than appending. The
tag list comes from the spec repo's docs-navigation.json, so a tag added there
lands here on the next run.

Usage: aigw/_project/wire_openapi_nav.py [path-to-spec-repo]
"""

import json
import os
import sys
from collections import OrderedDict

SPEC_REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser(
    "~/Documents/Projects/openapi/openapi")
DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "docs.json")

# The mirror is a local file, not a GitHub raw URL: we cannot point at the Palo
# Alto Networks organisation. Prose is already flattened in by sync-openapi.sh,
# so an empty overlay list also switches off Mintlify's overlay auto-discovery.
SOURCE = {
    "source": "/aigw/airs-openapi.yaml",
    "directory": "aigw/api-reference",
    "overlays": [],
}

# Which generated top-level group belongs on which tab. Inference is the data
# plane and keeps the Gateway APIs tab; everything else is control plane.
TAB_FOR_GROUP = {
    "Inference": "Gateway APIs",
    "Gateway Configuration": "Admin APIs",
    "Providers and Credentials": "Admin APIs",
    "MCP": "Admin APIs",
    "Administration": "Admin APIs",
    "Observability": "Admin APIs",
}

MARKER = "API Reference"  # the existing hand-written group, kept first


def build_groups(spec_nav):
    """Return {tab_name: [group, ...]} with the local source substituted in."""
    out = {tab: [] for tab in set(TAB_FOR_GROUP.values())}
    unknown = []
    for group in spec_nav["groups"]:
        tab = TAB_FOR_GROUP.get(group["group"])
        if tab is None:
            unknown.append(group["group"])
            continue
        pages = []
        for sub in group["pages"]:
            pages.append(OrderedDict([
                ("group", sub["group"]),
                ("openapi", dict(SOURCE)),
                ("tag", sub["tag"]),
            ]))
        out[tab].append(OrderedDict([("group", group["group"]), ("pages", pages)]))
    if unknown:
        raise SystemExit(
            "error: spec group(s) not mapped to a tab: %s\n"
            "       add them to TAB_FOR_GROUP and re-run" % ", ".join(unknown))
    return out


def main():
    spec_nav = json.load(open(os.path.join(SPEC_REPO, "docs-navigation.json")))
    generated = build_groups(spec_nav)

    with open(DOCS) as fh:
        docs = json.load(fh, object_pairs_hook=OrderedDict)

    version = next(v for v in docs["navigation"]["versions"]
                   if v["version"] == "Prisma AIRS")

    for tab in version["tabs"]:
        name = tab.get("tab")
        if name not in generated:
            continue
        # Keep the hand-written API Reference group, drop any previously
        # generated groups, then re-append. That is what makes this idempotent.
        kept = [g for g in tab["groups"] if g.get("group") == MARKER]
        tab["groups"] = kept + generated[name]
        total = sum(len(g["pages"]) for g in generated[name])
        print("%-14s %d group(s), %d tag(s)" % (name, len(generated[name]), total))

    with open(DOCS, "w") as fh:
        json.dump(docs, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print("wrote docs.json")


if __name__ == "__main__":
    main()
