#!/usr/bin/env python3
"""Verify the Prisma AIRS page set survives a navigation restructure.

Phase 6 rewrites 146 navigation entries by hand. Two things can go wrong silently:
a page drops out of the tree and becomes an orphan file, or a navigation entry
survives with no file behind it. Neither fails `mint validate` loudly enough.

This asserts three invariants:

  1. Every navigation entry resolves to a file on disk.
  2. Every .mdx under aigw/ (excluding _project/) is reachable from the tree.
  3. The page set matches the recorded baseline, except for entries listed in
     the retirement ledger with a reason.

Run with --write-baseline once before the restructure, then on every commit.
"""

import argparse
import json
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
DOCS = os.path.join(ROOT, "docs.json")
BASELINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nav_baseline.json")
LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nav_retirement_ledger.json")

VERSION = "Prisma AIRS"


def nav_pages():
    """Every page path in the Prisma AIRS version, in tree order."""
    docs = json.load(open(DOCS))
    version = next(v for v in docs["navigation"]["versions"] if v["version"] == VERSION)
    found = []

    def walk(node):
        for page in node.get("pages", []):
            if isinstance(page, str):
                found.append(page)
            else:
                walk(page)

    for tab in version["tabs"]:
        for group in tab.get("groups", []):
            walk(group)
    return found


def disk_pages():
    """Every .mdx under aigw/, excluding the build-excluded _project/."""
    found = []
    for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, "aigw")):
        dirnames[:] = [d for d in dirnames if d not in ("_project", "scripts")]
        for name in filenames:
            if name.endswith(".mdx"):
                path = os.path.join(dirpath, name)
                found.append(os.path.relpath(path, ROOT)[: -len(".mdx")])
    return found


def is_alias(page):
    """True if the page is a 4-line frontmatter `url:` stub rather than prose."""
    path = os.path.join(ROOT, page + ".mdx")
    if not os.path.exists(path):
        return False
    return bool(re.search(r"^url:", open(path).read(), re.M))


def load(path, default):
    return json.load(open(path)) if os.path.exists(path) else default


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-baseline", action="store_true",
                        help="record the current page set as the baseline")
    args = parser.parse_args()

    nav = nav_pages()
    disk = disk_pages()

    if args.write_baseline:
        json.dump({"pages": sorted(nav)}, open(BASELINE, "w"), indent=2)
        print(f"baseline written: {len(nav)} pages")
        return 0

    failures = []

    # A page may legitimately appear in two navigation locations — Mintlify renders
    # one URL either way, and slice 6.7 does it on purpose for gateway-registration.
    # Report rather than fail, so an accidental one is still visible.
    duplicates = sorted({p for p in nav if nav.count(p) > 1})

    missing = [p for p in nav if not os.path.exists(os.path.join(ROOT, p + ".mdx"))]
    if missing:
        failures.append(("navigation entry has no file", missing))

    orphans = sorted(set(disk) - set(nav))
    if orphans:
        failures.append(("file is unreachable from navigation", orphans))

    baseline = set(load(BASELINE, {"pages": []})["pages"])
    ledger = load(LEDGER, {})
    if baseline:
        gone = sorted(baseline - set(nav) - set(ledger))
        if gone:
            failures.append(("page left the tree with no ledger entry", gone))
        stale = sorted(p for p in ledger if p in nav)
        if stale:
            failures.append(("ledger lists a page that is still in the tree", stale))

    aliases = [p for p in nav if is_alias(p)]

    for title, items in failures:
        print(f"FAIL: {title}", file=sys.stderr)
        for item in items:
            print(f"    {item}", file=sys.stderr)

    if failures:
        return 1

    if duplicates:
        print(f"note: {len(duplicates)} page(s) listed in two navigation locations")
        for page in duplicates:
            print(f"    {page}")

    print(f"OK: {len(nav)} navigation entries, {len(aliases)} aliases, "
          f"{len(ledger)} retired, no orphans")
    return 0


if __name__ == "__main__":
    sys.exit(main())
