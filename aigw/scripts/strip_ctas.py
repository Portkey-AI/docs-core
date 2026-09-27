#!/usr/bin/env python3
"""Phase 5 — strip sales CTAs and support "reach out" trailers from aigw/.

Handles only the shapes that repeat verbatim across many pages. Anything it does
not recognise is left alone and reported, so it gets a hand edit instead of a
guess. Idempotent: running it twice changes nothing the second time.

Deliberately line-based rather than a whole-file regex. A global blank-line
collapse reflows spacing the corpus already had, which is hundreds of files of
diff noise for no change in rendered output — so each removal instead consumes
its own adjacent blank line and nothing else is touched.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT.parent
TARGETS = [ROOT, REPO / "snippets" / "aigw"]

# Standalone trailer paragraphs. Each is a whole line existing only to ask the
# reader to make contact; removing the line leaves the section coherent.
TRAILERS = [
    re.compile(p, re.IGNORECASE)
    for p in [
        r"^If you (?:face|encounter|run into) any (?:issues|problems)[^\n]*"
        r"(?:reach out|contact|email)",
        r"^\*{0,2}Need help\?\*{0,2}[^\n]*(?:reach out|contact)",
        r"^For (?:more help|further questions|questions about)[^\n]*"
        r"(?:reach out|reach us|contact)",
        r"^If you have any questions[^\n]*(?:reach out|contact)",
    ]
]

CARD_OPEN = re.compile(r"^\s*<Card title=\"(?:Book|Schedule) a Demo\"")
CARD_CLOSE = re.compile(r"^\s*</Card>\s*$")
HEADING = re.compile(r"^#{2,4} ")
RULE = re.compile(r"^-{3,}\s*$")

# Left for a hand edit: these need surrounding prose rewritten, not a line cut.
NEEDS_HAND_EDIT = re.compile(
    r"Interested\? Schedule a Call"
    r"|schedule a (?:quick call|consultation)"
    r"|Reach out to our team"
    r"|Book a call"
    r"|cal\.link",
    re.IGNORECASE,
)


def drop(lines, i):
    """Delete line i plus one adjacent blank, so no blank run is created."""
    del lines[i]
    if i < len(lines) and not lines[i].strip():
        del lines[i]
    elif i > 0 and not lines[i - 1].strip():
        del lines[i - 1]
        return i - 1
    return i


def strip_cards(lines):
    i = 0
    while i < len(lines):
        if CARD_OPEN.match(lines[i]):
            j = i
            while j < len(lines) and not CARD_CLOSE.match(lines[j]):
                j += 1
            del lines[i:j + 1]
            if i < len(lines) and not lines[i].strip():
                del lines[i]
            elif i > 0 and not lines[i - 1].strip():
                del lines[i - 1]
                i -= 1
            continue
        i += 1
    return lines


def strip_trailers(lines):
    i = 0
    while i < len(lines):
        if any(t.match(lines[i]) for t in TRAILERS):
            i = drop(lines, i)
            continue
        i += 1
    return lines


def empty_headings(lines):
    """Indices of headings whose body is blank up to the next heading, a
    horizontal rule, or EOF."""
    out = set()
    for i, line in enumerate(lines):
        if HEADING.match(line):
            rest = [x for x in lines[i + 1:] if x.strip()]
            if not rest or HEADING.match(rest[0]) or RULE.match(rest[0]):
                out.add(line.strip())
    return out


def drop_new_orphans(before, after):
    """Delete headings this run emptied.

    A "## Get Support" whose only content was the removed trailer is now a
    heading with no body. Headings already empty beforehand are pre-existing
    structure and are left alone.
    """
    orphaned = empty_headings(after) - empty_headings(before)
    if not orphaned:
        return after
    i = 0
    while i < len(after):
        if after[i].strip() in orphaned:
            i = drop(after, i)
            continue
        i += 1
    return after


def main() -> int:
    changed, flagged = [], []

    for target in TARGETS:
        for path in sorted(target.rglob("*.mdx")):
            if "_project" in path.parts:
                continue
            original = path.read_text()
            before = original.split("\n")
            lines = strip_trailers(strip_cards(list(before)))
            if lines != before:
                lines = drop_new_orphans(before, lines)

            text = "\n".join(lines)
            if text != original:
                path.write_text(text)
                changed.append(path.relative_to(REPO))
            if NEEDS_HAND_EDIT.search(text):
                flagged.append(path.relative_to(REPO))

    print(f"rewritten: {len(changed)}")
    for p in changed:
        print(f"  {p}")
    print(f"\nneeds a hand edit: {len(flagged)}")
    for p in flagged:
        print(f"  {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
