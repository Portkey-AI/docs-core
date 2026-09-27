#!/usr/bin/env python3
"""Apply the spec repo's navigation fragment to the API groups in docs.json.

The division of ownership: the spec repo owns which tag is in which group and
which operations are in it, and publishes exactly that as `docs-navigation.json`.
We own where those groups hang in the tabs. So this replaces the `pages` array of
each named group wholesale and touches nothing else -- not tabs, not versions, not
guides, not theming, not the order groups sit in within a tab.

Operations are named explicitly, one `"METHOD /path"` string per page. A group
carrying `openapi.source` with nothing narrowing it autogenerates the entire
document, which is what the old `"tag"` key did: `tag` is not in Mintlify's
navigation schema, so it was ignored and all 42 groups rendered all 187
operations. There is a check below for it coming back.

Usage:
    aigw/scripts/sync_api_nav.py                 compare only; non-zero on any difference
    aigw/scripts/sync_api_nav.py --apply         write docs.json
    aigw/scripts/sync_api_nav.py --from PATH     read the fragment from a local checkout

Bare is the pull-request check. `--apply` runs on a schedule or on a dispatch from
the spec repo and opens a pull request, so a spec change lands as a reviewable diff
rather than a silent overwrite.
"""

import argparse
import json
import os
import sys
import urllib.request
from collections import OrderedDict

FRAGMENT_URL = ("https://raw.githubusercontent.com/PaloAltoNetworks/openapi/"
                "refs/heads/main/docs-navigation.json")

DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "docs.json")

# Ours, not theirs. The fragment ships `directory: api-reference`; the Prisma AIRS
# version serves the whole tree one level down. The source URL is the same document
# Mintlify already fetches.
SOURCE = OrderedDict([
    ("source", "https://raw.githubusercontent.com/PaloAltoNetworks/openapi/"
               "refs/heads/main/openapi.yaml"),
    ("directory", "aigw/api-reference"),
])


def load_fragment(path):
    if path:
        with open(path) as fh:
            return json.load(fh)
    req = urllib.request.Request(FRAGMENT_URL, headers={"User-Agent": "curl/8"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def walk_groups(groups, path=()):
    """Yield (parent_list, index, group, path) for every group dict in the tree."""
    for i, item in enumerate(groups):
        if not isinstance(item, dict) or "group" not in item:
            continue
        here = path + (item["group"],)
        yield groups, i, item, here
        yield from walk_groups(item.get("pages", []), here)


def all_groups(docs):
    for version in docs.get("navigation", {}).get("versions", []):
        for tab in version.get("tabs", []):
            yield from walk_groups(tab.get("groups", []))


def build_pages(frag_group):
    """The `pages` array a docs.json group should hold, from the fragment's group."""
    pages = []
    for sub in frag_group["pages"]:
        pages.append(OrderedDict([
            ("group", sub["group"]),
            ("openapi", OrderedDict(SOURCE)),
            ("pages", list(sub["pages"])),
        ]))
    return pages


def is_spec_backed(group):
    """True if the group's own pages are generated from the spec."""
    return any(isinstance(p, dict) and "openapi" in p
               for p in group.get("pages", []))


def describe(expected, actual, name):
    """Lines describing how `actual` differs from `expected`. Empty if identical."""
    if expected == actual:
        return []
    out = ["%s:" % name]
    exp = OrderedDict((g["group"], g) for g in expected)
    act = OrderedDict((g["group"], g) for g in actual
                      if isinstance(g, dict) and "group" in g)
    for sub in exp:
        if sub not in act:
            out.append("    + %-34s %d operation(s), absent here"
                       % (sub, len(exp[sub]["pages"])))
    for sub in act:
        if sub not in exp:
            out.append("    - %-34s not in the fragment" % sub)
    for sub in exp:
        if sub in act and exp[sub] != act[sub]:
            have = act[sub].get("pages", [])
            want = exp[sub]["pages"]
            if "tag" in act[sub]:
                out.append("    ~ %-34s carries a `tag` key; %d operation(s) unnamed"
                           % (sub, len(want)))
            elif have != want:
                added = [p for p in want if p not in have]
                gone = [p for p in have if p not in want]
                out.append("    ~ %-34s %d added, %d removed"
                           % (sub, len(added), len(gone)))
                for p in added[:5]:
                    out.append("        + %s" % p)
                for p in gone[:5]:
                    out.append("        - %s" % p)
            else:
                out.append("    ~ %-34s openapi block differs" % sub)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--apply", action="store_true",
                    help="write docs.json instead of only comparing")
    ap.add_argument("--from", dest="source", metavar="PATH",
                    help="read docs-navigation.json from a local path")
    ap.add_argument("--docs", default=DOCS, metavar="PATH",
                    help="the docs.json to read and write (default: this repo's)")
    args = ap.parse_args()

    fragment = load_fragment(args.source)
    with open(args.docs) as fh:
        docs = json.load(fh, object_pairs_hook=OrderedDict)

    errors, diffs = [], []

    frag_by_name = OrderedDict((g["group"], g) for g in fragment["groups"])

    # Case 1: a group we publish with nowhere in docs.json to live. Someone has to
    # choose the tab; this script will not choose one.
    #
    # Matching is by name *and* by the group already being spec-backed. Name alone
    # is ambiguous: the Docs tab has its own "Administration" and "Observability"
    # groups of hand-written pages, and those are not ours to overwrite.
    targets = {}
    for name in frag_by_name:
        found = [(lst, i, g, p) for lst, i, g, p in all_groups(docs)
                 if g["group"] == name and is_spec_backed(g)]
        if not found:
            errors.append("fragment group %r has no spec-backed group of that name in "
                          "docs.json -- place it in a tab by hand, then re-run" % name)
        elif len(found) > 1:
            errors.append("fragment group %r matches %d groups in docs.json: %s"
                          % (name, len(found),
                             "; ".join(" > ".join(p) for _, _, _, p in found)))
        else:
            targets[name] = found[0]

    # Case 2: a spec-backed group here that the fragment does not mention -- a
    # dropped tag, about to render nothing.
    for _, _, group, path in all_groups(docs):
        if is_spec_backed(group) and group["group"] not in frag_by_name:
            errors.append("%s is spec-backed but the fragment does not mention it "
                          "-- dropped upstream, about to render nothing"
                          % " > ".join(path))

    for name, (lst, i, group, path) in targets.items():
        expected = build_pages(frag_by_name[name])
        lines = describe(expected, group.get("pages", []), " > ".join(path))
        if lines:
            diffs.extend(lines)
        if args.apply and not errors:
            new = OrderedDict(group)
            new["pages"] = expected
            new.pop("tag", None)
            lst[i] = new

    # Case 3: a `tag` key on a group that also carries `openapi`. Not in Mintlify's
    # navigation schema, so it is ignored and the group autogenerates the whole
    # document. Checked last, so that in --apply mode it reports only the ones the
    # rewrite did not already remove -- i.e. ones outside a synced group.
    for _, _, group, path in all_groups(docs):
        if "openapi" in group and "tag" in group:
            errors.append("stray `tag` key on %s -- renders every operation "
                          "in the document" % " > ".join(path))

    for e in errors:
        print("error: %s" % e, file=sys.stderr)
    for line in diffs:
        print(line)

    if errors:
        return 2

    if args.apply:
        with open(args.docs, "w") as fh:
            json.dump(docs, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        total = sum(len(s["pages"]) for g in fragment["groups"] for s in g["pages"])
        print("wrote docs.json: %d group(s), %d tag(s), %d operation(s)"
              % (len(targets),
                 sum(len(g["pages"]) for g in fragment["groups"]),
                 total))
        return 0

    if diffs:
        print("\ndocs.json differs from the fragment. Run with --apply to sync.")
        return 1
    print("in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
