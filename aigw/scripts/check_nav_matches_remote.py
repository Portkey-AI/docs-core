#!/usr/bin/env python3
"""Verify every navigation `tag` in docs.json exists in the remote spec, and vice versa.

docs.json's navigation is generated from the spec repo's local docs-navigation.json,
but Mintlify fetches the spec from the public raw URL on main. Those two can drift:
a tag dropped upstream leaves an empty navigation group, and a tag added upstream
goes unrendered. This catches both. Run it after every wire_openapi_nav.py.
"""

import json
import os
import sys
import urllib.request

import yaml

DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "docs.json")


def nav_tags():
    docs = json.load(open(DOCS))
    version = next(v for v in docs["navigation"]["versions"]
                   if v["version"] == "Prisma AIRS")
    found, source = set(), None

    def walk(groups):
        nonlocal source
        for g in groups:
            if isinstance(g, dict):
                if "tag" in g and "openapi" in g:
                    found.add(g["tag"])
                    cfg = g["openapi"]
                    source = cfg["source"] if isinstance(cfg, dict) else cfg
                walk(g.get("pages", []))

    for tab in version["tabs"]:
        walk(tab.get("groups", []))
    return found, source


tags, source = nav_tags()
if not source:
    sys.exit("no generated openapi groups found in docs.json")
print("nav tags   : %d" % len(tags))
print("spec source: %s" % source)

req = urllib.request.Request(source, headers={"User-Agent": "curl/8"})
with urllib.request.urlopen(req, timeout=60) as r:
    spec = yaml.safe_load(r.read().decode("utf-8", "replace"))

used = set()
for item in (spec.get("paths") or {}).values():
    for method, op in item.items():
        if method.lower() in ("get", "post", "put", "delete", "patch"):
            used.update(op.get("tags") or [])
print("spec tags  : %d in use" % len(used))

empty = sorted(tags - used)
missing = sorted(used - tags)
for t in empty:
    print("  EMPTY GROUP  %-40s in docs.json, absent from the spec" % t)
for t in missing:
    print("  UNRENDERED   %-40s in the spec, absent from docs.json" % t)

if empty or missing:
    sys.exit("drift: %d empty group(s), %d unrendered tag(s)" % (len(empty), len(missing)))
print("in sync")
