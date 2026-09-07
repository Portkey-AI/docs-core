# Page contracts

Handoff §2, bound to this repository's actual Mintlify components and to
[`writing-style-guide.md`](../writing-style-guide.md).

Where the handoff and the style guide overlap they agree: lead with the goal, cut hedging,
show rather than tell. Where they differ, the handoff's *content* requirements are additive —
they say what must be present, not how to phrase it. Both apply.

## Common frontmatter

```yaml
---
title: "Imperative or noun phrase, specific enough to be discoverable"
description: "One sentence. Appears in search and social cards."
---
```

Additional keys in use in this repo: `mode: "wide"` (full-bleed pages), `icon`, `sidebarTitle`.

Applicability (`applies_to`, per §2) has **no public frontmatter home yet**. Two options —
decide before authoring: an explicit in-page `<Info>` callout, or a private manifest field
only. Do not invent a `docs.json`-unknown frontmatter key; Mintlify will not validate it.

## Contracts

### Overview / concept

Required: purpose · mechanism · boundaries · applicability · next useful task.

- Open with what it is and the problem it solves — no video, no CTA above the fold.
- State boundaries explicitly, including what the gateway does *not* do. This is the most
  commonly skipped element and the one J1 most needs.
- End with `<CardGroup>` linking the next concrete task, not a feature index.

### Quickstart

Required: prerequisites · minimal steps · complete working example · expected result ·
verification · next step.

- Prerequisites before the first command, always. Account type, credentials needed, install.
- `<Steps>` for the sequence; `<CodeGroup>` for language variants (style guide: `CodeGroup`,
  not `Tabs`).
- Examples must be complete and runnable with safe placeholders. Never a real credential.
- **Verification is mandatory and most often missing.** Show the expected output, or a check
  the reader can run. "How does the reader know it worked?"
- One next step. Not a menu.

### How-to guide

Required: one goal · environment/version · steps · checks · failure cases.

- One goal per page. If the title needs "and", split the page.
- Failure cases are part of the contract, not an appendix — what goes wrong and what to do.

### API / reference

Required: exact versioned contract · parameters · types · defaults · errors · examples.

- Generated from OpenAPI where possible. See gap G5.1 — the spec lives in a separate repo and
  its relationship to KB authority is unresolved.
- Every default and every limit is a claim-bearing assertion requiring KB support.

### Operations

Required: procedure · prerequisites · verification · recovery/rollback where applicable.

- Rollback is not optional for anything that changes production routing or credentials.

### Troubleshooting

Required: recognizable symptom · diagnostic steps · supported causes and remedies.

- Head each section with the symptom **as the reader would describe it** ("requests aren't
  failing over"), not as the system would ("fallback target resolution").
- Only list causes the KB supports. Speculative causes are §3 rule 5 violations.

### Changelog

Required: release identity/date · applicability · what changed · migration impact.

- Existing tooling: `.claude/skills/update-changelog/SKILL.md`,
  `.cursor/commands/document-a-release.md`. Extend these rather than replacing them.
- Historical entries are immutable (§4). Corrections append; they do not rewrite.

### Example

Required: dependencies · complete runnable code · expected behavior · supported version.

## Component conventions

Verified in use in this repo:

| Need | Component |
|---|---|
| Multiple languages, same example | `<CodeGroup>` — **not** `<Tabs>` |
| Sequential procedure | `<Steps>` / `<Step>` |
| Navigation to next task | `<Card>`, `<CardGroup>` |
| Collapsible detail, FAQs | `<Accordion>`, `<AccordionGroup>` |
| Screenshots, diagrams | `<Frame>` |
| Actionable constraint | `<Note>` `<Warning>` `<Info>` `<Check>` — for constraints, not decoration (§2) |
| Reused block | MDX snippet import from `snippets/` |

Prefer native components (§2). If one falls short, describe the reader problem and propose the
smallest remedy before adding custom machinery — do not reach for raw HTML or `style.css`.

## Code examples

Per the style guide, non-negotiable: K&R braces, 4-space indent, simple objects on one line,
no trailing commas in Python, language-correct comment syntax, every block titled so
`CodeGroup` renders a usable tab label.

## Grounding discipline (§3)

Needs a claim reference: numbers, defaults, limits, instructions, prerequisites, code
assumptions, claimed outputs.

Does not: headings, connective prose, editorial framing.

Two failure modes the gate must catch, both worse than a missing citation because they look
correct:

1. A valid claim ID cited for an assertion it does not actually support (§3 rule 3).
2. An assertion stated with more certainty or broader scope than its claim carries.

## Pre-publication checklist

Condensed from §7. Full gate list lives there.

- [ ] Frontmatter valid; page registered in `docs.json`; route assigned; owner recorded
- [ ] Every substantive assertion has accepted, applicable KB support
- [ ] Public eligibility re-checked **now**, not at draft time
- [ ] No private material in the page, its metadata, or in `llms.txt` / `llms-full.txt`
- [ ] Examples syntax-checked; runnable tests run, or the omission recorded
- [ ] Links and anchors resolve; next step is coherent
- [ ] `mint dev` preview reviewed on desktop and mobile; code blocks and keyboard nav checked
- [ ] Base-revision check — no concurrent human edit overwritten
- [ ] Editorial approval recorded; deployment status **verified**, not inferred from merge
