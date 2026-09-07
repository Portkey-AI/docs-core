# Product naming and vocabulary rules

Status: **approved 2026-09-07** (Q3). Approval covers the rule below *and* the four items in
"Unresolved" — those are settled as written unless revisited.

Scope confirmed 2026-09-07: the whole corpus is Prisma AIRS AI Gateway, rebranded in place.
The other tabs are modules of it, not separate products.

## Where these rules came from

The renaming line is drawn from `~/.claude/skills/rfp/knowledge/prisma-airs-ai-gateway.md`,
which already defines it for customer-facing sales copy. That file is an internal sales
artifact, **not** KB-accepted knowledge — so it is being used here for a *naming convention*,
which is an operator/branding decision, and not for any product capability claim.

Naming is the one area where the KB is not the authority. Everything else still is.

## The rule

### Renames

| Current | Use |
|---|---|
| "Portkey" (as the product) | **Prisma AIRS AI Gateway** |
| "Portkey" (subsequent mentions in a page) | **the gateway** or **AI Gateway** |
| "Portkey AI" | **Prisma AIRS AI Gateway** |
| Management/admin plane | **Strata Cloud Manager** |
| Company references | **Palo Alto Networks** |

First mention on a page uses the full product name. After that, "the gateway" reads better
than repeating four words — this matters given the style guide's brevity rules.

### Never renamed

These are functional identifiers. Renaming them breaks working code, and a doc that breaks
copy-paste is worse than a doc with a legacy name in it.

| Kind | Examples |
|---|---|
| Python package / import | `portkey_ai`, `from portkey_ai import Portkey` |
| Node package / import | `portkey-ai`, `import Portkey from 'portkey-ai'` |
| Class and constructor names | `Portkey(...)`, `createHeaders`, `PORTKEY_GATEWAY_URL` |
| Environment variables | `PORTKEY_API_KEY`, `PORTKEY_*` |
| HTTP headers | `x-portkey-api-key`, `x-portkey-provider`, `x-portkey-*` |
| Hostnames | `api.portkey.ai`, `app.portkey.ai` |
| Config keys and JSON fields | as shipped |
| Repo names in changelogs | `Portkey-AI/gateway`, `Portkey-AI/albus`, … |

Rule of thumb: **if a reader would type it or a machine would parse it, it does not change.**
If a reader only reads it, it does.

### Module labels

The RFP knowledge file uses licensing labels that only partly match the current navigation.
Which vocabulary is public is Q3's open sub-question — do not apply these until confirmed.

| Licensing label | Closest current nav group |
|---|---|
| Prisma AIRS AI Gateway — Enterprise | Product → AI Gateway, Enterprise Offering |
| Prisma AIRS Agent Gateway | Product → Agent Gateway |
| Prisma AIRS Observability Suite | Product → Observability |
| Prisma AIRS Guardrails Engine | Product → Guardrails |
| Prisma AIRS Model Catalog | Product → Model Catalog |
| Prisma AIRS Prompt Studio | Product → Prompt Studio |

Note the gaps in both directions: MCP Gateway and Administration have no licensing label
listed, and the labels do not name Self-Hosting. Resolve before applying.

## Previously unresolved — approved as written, 2026-09-07

Each of these was flagged as needing a decision. All four are approved as described; the
reasoning is kept because it is what a future reader will need in order to revisit them.

1. **Open-source Gateway identity.** `product/open-source` and `changelog/open-source`
   document the OSS Gateway, which is a genuinely separate, publicly-named project. Does it
   keep the Portkey name? Probably yes, but it needs saying.
2. **Community CTAs.** Discord, `git.new/ai-gateway-docs` "give us a star", the developer
   forum, `support@portkey.ai`. These are Portkey-community properties embedded in pages —
   including the current entry page. Keep, replace with PANW support channels, or serve
   differently per version?

   Related and already decided: the **`prisma-airs-cta` snippet is not used in the Prisma AIRS
   version at all.** It announces the Portkey → Prisma AIRS transition, which is redundant on
   pages that are already Prisma AIRS. It stays where it is on the Latest-version pages.
3. **Certifications and metrics.** `introduction/what-is-portkey` states ISO 27001 / SOC 2 /
   GDPR / HIPAA, "25M requests daily", "99.99% uptime", "20-40ms" latency. Under the new
   parent these are claims about a different legal entity. All are substantive assertions
   requiring KB support anyway — flagged here because rebranding makes them wrong-by-default
   rather than merely unverified.
4. **Status page.** `status.portkey.ai` — same question as the hostnames, but reader-facing.

## Applying it

Do not run a global find-and-replace. The identifier list above guarantees it would break
code samples, and the corpus is ~1,200 pages.

The migration unit is a page, and the trigger is the grounding gate:

1. A page is re-grounded against the KB.
2. It is rewritten under these naming rules and the
   [page contracts](./02-page-contracts.md).
3. It is added to the **Prisma AIRS** version in `docs.json` and gets a manifest.
4. The Latest-version page stays as-is until the AIRS version is complete enough to swap.

This is why the naming rule had to be settled before authoring rather than after: every page
that passes the gate is written once, under the final vocabulary.
