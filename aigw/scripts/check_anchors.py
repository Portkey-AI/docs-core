#!/usr/bin/env python3
"""Check that every in-repo anchor link under aigw/ points at a heading that exists.

`mint broken-links` resolves pages and stops there. It does not look at the fragment, so a
link to a section that was renamed or deleted stays green forever. Phase 2's UK rebrand
renamed headings without updating the links into them -- `#guardrail-behavior-on-the-gateway`
has been dead since then and nothing noticed. The spelling sweep on 2026-09-18 renamed five
more headings, which is what prompted writing this.

    python3 aigw/scripts/check_anchors.py            # report, exit 1 on anything unlisted
    python3 aigw/scripts/check_anchors.py --all      # include the KNOWN baseline in output

ON SLUGS: this does not reimplement Mintlify's slugifier, because getting it wrong invents
failures. Headings and link fragments are compared with every non-alphanumeric character
removed, so `can-t-connect` and `cant-connect`, or `reasoning--thinking` and
`reasoning-thinking`, are treated as the same anchor. Punctuation disagreements are where a
hand-rolled slugifier and a real one part company; word disagreements are where documentation
actually breaks. Only the second kind is reported. The cost is that a genuine
punctuation-only break would be missed, which is the right trade -- it is invisible to a
reader anyway, since the browser scrolls to nothing either way and they see the top of a page
that does contain their section.
"""

import re
import sys
import pathlib
import collections

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = ROOT.parent

# Anchors that are broken and are not ours to fix in passing. Each needs a destination
# decision, not a correction -- the section it wanted is gone rather than renamed. A
# shrinking baseline: an entry that stops matching anything fails the check, same as the
# endpoint check, so these cannot quietly rot once someone resolves them.
KNOWN = {
    # Inherited. "3. Enterprise Governance" does not exist in the Latest version of these
    # pages either, so the links arrived broken; we did not break them. 24 links, 14 pages.
    "3-enterprise-governance": "section absent upstream too -- needs a destination",
    "enterprise-governance": "section absent upstream too -- needs a destination",
    # Sections removed by our own phases, with the links into them left behind.
    "auto-instrumentation": "SDK feature removed in Phase 3",
    "access-control-management": "section gone from list-of-guardrail-checks",
    "supported-integrations": "section gone from opentelemetry",
    "integration-approaches": "section gone from openai-agents-ts",
    "processing-pdfs-with-claude": "section gone from anthropic",
    "batches": "changelog links at a #batches heading the page never had",
    # Ambiguous: more than one heading could be meant, so guessing would be inventing.
    "portkey-batch-api-mode": "three links; 'AI Gateway Custom Batching' vs 'Provider Batch "
                              "API Mode' -- the text says provider-agnostic and immediate, "
                              "which points at Custom, but confirm before repointing",
    "legacy-single-provider-with-api-key": "'Single Provider with Provider API Key' or "
                                           "'Legacy: Single Provider with Virtual Key'",
    "how-to-enable-request-tracing": "traces.mdx has 'Enabling Tracing' and 'Why Use Tracing'",
    "using-reasoning_effort-parameter": "gemini.mdx does not mention reasoning_effort at all, "
                                        "so 'Extended Thinking' is the nearest heading but "
                                        "not the promised content -- ask product",
}


def key(s):
    """Compare on letters and digits only -- see ON SLUGS above."""
    return re.sub(r"[^a-z0-9]", "", s.lower())


def slug(heading):
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    h = re.sub(r"[`*_]", "", h).strip()
    h = re.sub(r"[^a-z0-9\s-]", "", h.lower()).strip()
    return re.sub(r"-+", "-", h.replace(" ", "-"))


def headings(path):
    out, fence = set(), False
    for line in path.read_text().splitlines():
        if line.strip().startswith(("```", "~~~")):
            fence = not fence
            continue
        if fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            out.add(slug(m.group(2)))
    return out


def main():
    show_all = "--all" in sys.argv
    pages = {}
    for p in sorted(ROOT.rglob("*.mdx")):
        if "_project" in p.parts:
            continue
        pages["/" + str(p.relative_to(REPO).with_suffix(""))] = headings(p)

    broken, listed = [], collections.Counter()
    link = re.compile(r"\]\((/[^)#\s]*)?#([A-Za-z0-9][A-Za-z0-9_-]*)\)")
    for p in sorted(ROOT.rglob("*.mdx")):
        if "_project" in p.parts:
            continue
        here = "/" + str(p.relative_to(REPO).with_suffix(""))
        for i, line in enumerate(p.read_text().splitlines(), 1):
            for m in link.finditer(line):
                target, anchor = m.group(1) or here, m.group(2)
                if target not in pages:
                    continue  # page-level; mint broken-links already owns this
                if key(anchor) in {key(h) for h in pages[target]}:
                    continue
                if anchor in KNOWN:
                    listed[anchor] += 1
                    if not show_all:
                        continue
                broken.append((f"{p.relative_to(REPO)}:{i}", f"{target}#{anchor}",
                               KNOWN.get(anchor)))

    real = [b for b in broken if b[2] is None]
    print(f"{sum(len(v) for v in pages.values())} headings across {len(pages)} pages")
    print(f"{sum(listed.values())} broken anchors carried as KNOWN "
          f"({len(listed)} distinct)")

    stale = set(KNOWN) - set(listed)
    if real:
        print(f"\n{len(real)} anchor link(s) point at a heading that does not exist:\n")
        for where, what, _ in real:
            print(f"  {where}\n      {what}")
        print("\nEither the heading was renamed -- fix the link -- or the section is gone,\n"
              "in which case it needs a destination and belongs in KNOWN with a reason.")
    if stale:
        print("\nKNOWN entries that matched nothing. The section came back or the link is\n"
              "gone -- delete the entry either way:")
        for a in sorted(stale):
            print(f"  {a}")
    if show_all and listed:
        print("\nKNOWN, for reference:")
        for a, n in listed.most_common():
            print(f"  {n:3d}  {a} -- {KNOWN[a]}")
    if not real and not stale:
        print("\nEvery anchor link under aigw/ resolves to a real heading.")
    return 1 if (real or stale) else 0


if __name__ == "__main__":
    sys.exit(main())
