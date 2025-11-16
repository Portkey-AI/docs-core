# Master Migration Guide: Virtual Keys → Model Catalog

## Overview

367 files contain references to Virtual Keys. This guide provides everything needed to systematically migrate all documentation from Virtual Keys to Model Catalog.

**Goal:** Migrate all pages to use Model Catalog patterns while maintaining backwards compatibility notes where needed.

---

## Part 1: Core Messaging Principles

### The Simple Analogy

**Think of it like a password manager:**

1. **Store credentials once** (Integration) = Save your OpenAI API key in a password vault
2. **Use it in your workspace** (Provider) = Saved login appears in your workspace  
3. **Call specific models** (Model) = Use `@provider-slug/model-name` in your code

**For workspace users:** You only need to know step 2 and 3. Add a provider, use it in code.

**For org admins:** You manage step 1 (store credentials) and share them with workspaces (which become Providers).

### Key Simplifications

**Language Changes:**
- ❌ "Create an Integration at the organization level"
- ✅ "Store your credentials once, share everywhere"

- ❌ "Provision an Integration to workspaces"
- ✅ "Share credentials with workspaces"

- ❌ "AI Provider created from Integration"
- ✅ "Workspace sees it as a Provider they can use"

**Focus on User Actions, Not System Architecture:**
- ❌ "Integrations are stored at the org level"
- ✅ "Store credentials once, use in multiple workspaces"

### Messaging Principles

1. **Use analogies** - "Like a password vault" is more intuitive than "credential storage system"
2. **Focus on outcomes** - "Share with multiple workspaces" not "provision to workspaces"
3. **Explain the shortcut** - "Creating new credentials here automatically creates a workspace-linked integration"
4. **Reduce jargon** - "Credentials" instead of "Integration" in user-facing text where possible
5. **Show the flow** - "Credentials → Providers → Models" visual hierarchy

### Terminology Guide (Simplified)

| Term | When to Use | Simple Explanation |
|------|-------------|-------------------|
| **Provider** | Always | What you use in your code. Has a slug like `@openai-prod` |
| **Integration** | Org admin docs only | Where credentials are stored. Can be shared or workspace-only |
| **Credentials** | User-facing | API keys, auth details |
| **Model** | Always | The AI model you call |

**For most users:** You only need to know about **Providers**. Add a provider, use it in code with `@provider-slug/model-name`.

**For org admins:** **Integrations** store credentials. When you share an Integration with workspaces, they see it as a Provider.

### Progressive Disclosure Principle

**Core Principle:** Show users only what they need to know, when they need to know it.

**For Workspace Users (Model Catalog Page):**
- **Hide "Integration" concept entirely.** Focus on what they do, not how it works.
- **Don't mention:**
  - "Integration"
  - "inherits"
  - "workspace-only Integration"
  - Technical implementation details
- **Just say:** "Add provider, use it in code"

**Example - Model Catalog Page Content:**
```markdown
## AI Providers

AI Providers are what you use in your code. Each provider has:
- A unique slug (e.g., `@openai-prod`)
- Securely stored credentials
- Budget and rate limits
- Access to specific models

**To add a provider:**
1. Go to Model Catalog → AI Providers → Add Provider
2. Select your AI service
3. **If credentials exist:** Choose from dropdown
   **If creating new:** Enter your API keys
4. Name your provider

That's it! Use `@provider-slug/model-name` in your code.
```

**For Org Admins (Integrations Page):**
- **Lead with the "why" not the "how"**
- **Explain the benefit:** Save time, control access, set limits
- **Explain the flow:** Integration → Provider (simple, one-way)
- **Mention workspace-only as a footnote, not upfront**

**Example - Integrations Page Content:**
```markdown
## Integrations

**What are Integrations?** A place to store credentials once and share them with multiple workspaces.

**Why use them?**
- Save time: Store API keys once, use in many workspaces
- Control access: Decide which workspaces can use which credentials
- Set limits: Different budgets/rate limits per workspace

**How it works:**
1. Store credentials here (creates an Integration)
2. Share with workspaces (they see it as a Provider in their Model Catalog)
3. Each workspace can use the same credentials with different limits

**Two ways to create:**
- **Shared:** Store here and share with multiple workspaces (recommended)
- **Workspace-only:** Created automatically when workspace users add providers with new credentials
```

**For API Users (Upgrade Guide):**
- **Focus on the action, not the architecture**
- **Lead with the common case:** `POST /providers`
- **Explain difference in one sentence**
- **Give simple rule of thumb**

**Example - API Upgrade Guide Content:**
```markdown
## Creating Providers via API (Virtual Key Equivalent)

**To create a provider in a workspace (like old virtual key):**

Use `POST /providers` - this creates what you use in your code.

```python
# Create provider using existing credentials
provider = portkey.providers.create(
    workspace_id="workspace-123",
    name="openai-prod",
    integration_id="integration-456"  # Use existing credentials
)

# Create provider with new credentials
provider = portkey.providers.create(
    workspace_id="workspace-123",
    name="openai-dev",
    provider="openai",
    credentials={"api_key": "sk-..."}  # Creates credentials automatically
)
```

**What's the difference?**
- `POST /integrations` - Store credentials (for org admins who want to share)
- `POST /providers` - Create provider in workspace (what you use in code)

**Simple rule:** Most users just need `POST /providers`. Use `POST /integrations` only if you're an org admin sharing credentials across workspaces.
```

**Note:** UI auto-creates Integration when creating provider with new credentials. API requires explicit `POST /integrations` first, then `POST /providers` references it.

### Key Simplification Principles

1. **Hide complexity from workspace users**
   - Don't mention "Integration" in Model Catalog page
   - Don't explain inheritance
   - Just: "Add provider, use in code"

2. **Progressive disclosure**
   - Workspace users: Just Providers
   - Org admins: Integrations + Providers
   - API users: Both endpoints with simple rule

3. **Focus on actions, not architecture**
   - "Store credentials and share" not "Create Integration at org level"
   - "Add provider to workspace" not "Create Provider that inherits from Integration"

4. **Use analogies consistently**
   - Password vault = Integration (credential storage)
   - Saved login = Provider (what you use)

5. **One concept at a time**
   - Don't explain shared vs workspace-only upfront
   - Don't explain inheritance upfront
   - Only when user needs to know

### Recommended Content Updates

**Model Catalog page:** Remove all mentions of "Integration" and "inherits". Focus on what users do, not how the system works.

**Integrations page:** Lead with benefits, explain flow simply. Mention workspace-only as a footnote, not upfront.

**Upgrade guide:** Focus on common case (`POST /providers`). Give simple rule of thumb.

---

## Part 2: File Groups for Migration

### Group 1: Core Product Pages (Priority: HIGH)
**Files to update:**
- `product/ai-gateway/virtual-keys.mdx` - Main Virtual Keys page (needs complete rewrite)
- `product/ai-gateway/virtual-keys/budget-limits.mdx`
- `product/ai-gateway/virtual-keys/rate-limits.mdx`
- `product/ai-gateway/virtual-keys/bedrock-amazon-assumed-role.mdx`
- `product/model-catalog.mdx` - ✅ Already updated
- `product/model-catalog/integrations.mdx` - ✅ Already updated
- `product/ai-gateway.mdx`
- `introduction/feature-overview.mdx`
- `support/upgrade-to-model-catalog.mdx` - ✅ Already updated

**Migration Strategy:**
- Rewrite `virtual-keys.mdx` as comprehensive guide (see Part 4)
- Update budget-limits and rate-limits to reference Model Catalog
- Update feature overview to mention Model Catalog

---

### Group 2: LLM Provider Integration Pages (Priority: HIGH)
**Pattern:** All files in `integrations/llms/*.mdx`

**Key files:**
- `integrations/llms/openai.mdx`
- `integrations/llms/anthropic.mdx`
- `integrations/llms/azure-openai/azure-openai.mdx`
- `integrations/llms/bedrock/aws-bedrock.mdx`
- `integrations/llms/vertex-ai.mdx`
- Plus 50+ other provider pages

**Migration Strategy:**
- Replace "Create a Virtual Key" sections with concise "Add Provider" pattern
- Update code examples to use model prefix format
- Keep backwards compatibility notes where `virtual_key` header still works
- Standardize the pattern across all provider pages

---

### Group 3: Library Integration Pages (Priority: MEDIUM)
**Pattern:** All files in `integrations/libraries/*.mdx`

**Key files:**
- `integrations/libraries/langchain-python.mdx`
- `integrations/libraries/openai-compatible.mdx`
- `integrations/libraries/cursor.mdx` - ✅ Already updated
- `integrations/libraries/cline.mdx`
- Plus 15+ other library pages

**Migration Strategy:**
- Update setup steps to use concise "Add Provider" pattern
- Update code examples to use provider slugs
- Keep backwards compatibility where needed

---

### Group 4: Gateway Feature Pages (Priority: MEDIUM)
**Files:**
- `product/ai-gateway/batches.mdx`
- `product/ai-gateway/load-balancing.mdx`
- `product/ai-gateway/fallbacks.mdx`
- `product/ai-gateway/circuit-breaker.mdx`
- `product/ai-gateway/canary-testing.mdx`
- `product/ai-gateway/automatic-retries.mdx`

**Migration Strategy:**
- Update examples to use `model="@provider/model"` in configs
- Replace `virtual_key` references with provider slugs
- Update config examples

---

### Group 5: Guides and Tutorials (Priority: MEDIUM)
**Files:**
- `guides/getting-started/getting-started-with-ai-gateway.mdx`
- `guides/prompts/llama-prompts.mdx`
- `guides/integrations/arize-portkey.mdx`
- `guides/use-cases/*.mdx` (multiple files)

**Migration Strategy:**
- Update step-by-step instructions
- Replace Virtual Keys references with Model Catalog
- Update code examples

---

### Group 6: API Reference (Priority: LOW - Backwards Compatible)
**Files:**
- `api-reference/inference-api/headers.mdx`
- `api-reference/inference-api/config-object.mdx`
- `api-reference/admin-api/control-plane/virtual-keys/*.mdx`

**Migration Strategy:**
- Keep `virtual_key` header documented (backwards compatible)
- Add Model Catalog examples alongside
- Mark Virtual Keys API as deprecated but functional

---

### Group 7: Tracing Provider Integrations (Priority: LOW)
**Files:**
- `integrations/tracing-providers/traceloop.mdx`
- `integrations/tracing-providers/phoenix.mdx`
- `integrations/tracing-providers/langsmith.mdx`
- Plus 5+ other tracing provider pages

**Migration Strategy:**
- Update examples to use Model Catalog
- Minor updates needed

---

### Group 8: Enterprise/Admin Pages (Priority: MEDIUM)
**Files:**
- `product/administration/configure-virtual-key-access-permissions.mdx`
- `product/enterprise-offering/access-control-management.mdx`
- `product/observability/cost-management.mdx`

**Migration Strategy:**
- Update to reference Model Catalog permissions
- Update access control examples

---

### Group 9: Changelog/Historical (Priority: LOW)
**Files:**
- `changelog/*.mdx` (multiple files)
- `support/portkeys-december-migration.mdx`

**Migration Strategy:**
- Keep as historical reference
- Add notes about Model Catalog migration where relevant

---

## Part 3: Concise Patterns and Templates

### Core Principle
**Keep each page concise. Show the simplest path, link to detailed docs for all options.**

---

### Pattern 1: "Add Provider" Setup (CONCISE)

**Standard pattern - use in ALL pages:**

```markdown
### Add Provider

1. Go to [**Model Catalog → Add Provider**](https://app.portkey.ai/model-catalog/providers)
2. Select **[Provider Name]**
3. **If credentials exist:** Choose from dropdown
   **If creating new:** Enter your API keys
4. Name your provider (e.g., `openai-prod`)

<Info>
**Quick tip:** If your org admin already set up credentials, just select them - no API keys needed!
</Info>

<Card title="Complete Setup Guide" icon="book" href="/product/model-catalog">
  See all setup options, code examples, and detailed instructions
</Card>
```

**Key Points:**
- Keep it to 4 steps
- Show both paths but keep it brief
- Link to Model Catalog page for all detailed options
- Emphasize the simpler path (credentials exist)

---

### Pattern 2: Code Examples (CONCISE)

**Show the recommended method, link to Model Catalog for all options:**

```markdown
## Using [Provider] in Your Code

Use the model prefix format:

```python
from portkey_ai import Portkey

portkey = Portkey(api_key="PORTKEY_API_KEY")

response = portkey.chat.completions.create(
    model="@openai-prod/gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

<Card title="All Code Examples" icon="code" href="/product/model-catalog#using-provider-models">
  See alternative methods: provider header, legacy virtual_key, and more
</Card>
```

**Key Point:** Show the recommended method only, link to Model Catalog for all options.

**All Three Methods (for reference - only show in Model Catalog page):**

1. **Model Prefix (Recommended):** `model="@openai-prod/gpt-4o"`
2. **Provider Header:** `provider="@openai-prod"` + `model="gpt-4o"`
3. **Legacy Virtual Key:** `virtual_key="openai-prod"` (backwards compatible)

---

### Pattern 3: Config Examples (CONCISE)

**Show the recommended method, link to Model Catalog for all options:**

```markdown
## Using in Configs

Specify provider and model in `override_params`:

```json
{
  "targets": [{
    "override_params": {
      "model": "@openai-prod/gpt-4o"
    }
  }]
}
```

<Card title="Config Examples" icon="settings" href="/product/model-catalog#3-specify-provider-in-the-config">
  See all config methods and multi-provider strategies
</Card>
```

**Key Point:** Show the recommended method only, link to Model Catalog for all options.

**All Three Methods (for reference - only show in Model Catalog page):**

1. **Model in override_params (Recommended):** `override_params: { model: "@provider/model" }`
2. **Provider in target:** `provider: "@provider"` + `override_params: { model: "model-name" }`
3. **Legacy virtual_key:** `virtual_key: "provider-slug"` (backwards compatible)

---

### Pattern 4: Complete Provider Page Template

**Use this template for all provider-specific pages:**

```markdown
---
title: "[Provider Name]"
description: "Integrate [Provider] with Portkey's AI Gateway"
---

With Portkey, use [Provider] with features like fast AI gateway, caching, observability, prompt management, and more, while securely managing your API keys through Model Catalog.

## Setting Up [Provider]

### Add Provider

1. Go to **Model Catalog → AI Providers → Add Provider**
2. Select **[Provider Name]**
3. **If credentials exist:** Choose from dropdown
   **If creating new:** Enter your API keys
4. Name your provider (e.g., `openai-prod`)

<Info>
**Quick tip:** If your org admin already set up credentials, just select them - no API keys needed!
</Info>

<Card title="Complete Setup Guide" icon="book" href="/product/model-catalog">
  See all setup options, code examples, and detailed instructions
</Card>

## Using [Provider] in Your Code

Use the model prefix format:

```python
from portkey_ai import Portkey

portkey = Portkey(api_key="PORTKEY_API_KEY")

response = portkey.chat.completions.create(
    model="@openai-prod/gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

<Card title="All Code Examples" icon="code" href="/product/model-catalog#using-provider-models">
  See alternative methods: provider header, legacy virtual_key, and more
</Card>

## [Provider-Specific Features]

[Add provider-specific content here]
```

---

### Pattern 5: Library Integration Template

**For library integration pages (LangChain, OpenAI-compatible, etc.):**

```markdown
## Setting Up Portkey

### Add Provider

1. Go to **Model Catalog → AI Providers → Add Provider**
2. Select your provider
3. **If credentials exist:** Choose from dropdown
   **If creating new:** Enter your API keys
4. Name your provider (e.g., `openai-prod`)

<Info>
**Quick tip:** If your org admin already set up credentials, just select them - no API keys needed!
</Info>

<Card title="Complete Setup Guide" icon="book" href="/product/model-catalog">
  See all setup options, including sharing credentials across workspaces
</Card>

### Use with [Library Name]

[Library-specific integration code using model prefix format]
```

---

## Part 4: Key Patterns to Replace

### Pattern 1: "Create Virtual Key" → "Add Provider"

**Before:**
```markdown
1. Navigate to Virtual Keys page
2. Click "Add Key"
3. Select provider and enter API key
```

**After (Use concise pattern from Part 3):**
```markdown
1. Go to Model Catalog → AI Providers → Add Provider
2. Select the AI service (OpenAI, Anthropic, etc.)
3. **If credentials exist:** Choose from dropdown
   **If creating new:** Enter your API keys
4. Name your provider and save
```

**Key Point:** Only step 3 differs - if credentials exist, just select. If not, create new ones.

---

### Pattern 2: Code Examples

**Before:**
```python
portkey = Portkey(
    api_key="PORTKEY_API_KEY",
    virtual_key="openai-key"
)
```

**After (Recommended):**
```python
portkey = Portkey(api_key="PORTKEY_API_KEY")

response = portkey.chat.completions.create(
    model="@openai-prod/gpt-4o",  # Provider + model together
    messages=[...]
)
```

**Alternative (Provider Header):**
```python
portkey = Portkey(
    api_key="PORTKEY_API_KEY",
    provider="@openai-prod"  # Provider with @ symbol
)

response = portkey.chat.completions.create(
    model="gpt-4o",  # Just the model name
    messages=[...]
)
```

**Legacy (Backwards Compatible):**
```python
# Still works, but not recommended for new code
portkey = Portkey(
    api_key="PORTKEY_API_KEY",
    virtual_key="openai-prod"  # Legacy format (no @)
)
```

---

### Pattern 3: Config Examples

**Before:**
```json
{
  "targets": [{
    "virtual_key": "openai-key"
  }]
}
```

**After (Recommended):**
```json
{
  "targets": [{
    "override_params": {
      "model": "@openai-prod/gpt-4o"  // Provider + model together
    }
  }]
}
```

**Alternative (Provider in target):**
```json
{
  "targets": [{
    "provider": "@openai-prod",  // Provider with @ symbol
    "override_params": {
      "model": "gpt-4o"  // Just the model name
    }
  }]
}
```

**Legacy (Backwards Compatible):**
```json
{
  "targets": [{
    "virtual_key": "openai-prod"  // Legacy format (no @)
  }]
}
```

---

### Common Replacements Table

| Old Pattern | New Pattern |
|------------|-------------|
| "Create a Virtual Key" | "Add Provider in Model Catalog" |
| "Navigate to Virtual Keys page" | "Go to Model Catalog → AI Providers" |
| "Enter your API key" | "Choose existing credentials or create new ones" |
| `virtual_key="openai-key"` | `model="@openai-prod/gpt-4o"` (recommended) |
| `virtual_key` in config | `override_params: { model: "@provider/model" }` (recommended) |
| "Virtual Key slug" | "Provider slug" (with @ prefix) |

---

## Part 5: Virtual Keys Page Rewrite

### Proposed Content for `product/ai-gateway/virtual-keys.mdx`

1. **Introduction**
   - What Virtual Keys were (historical context)
   - Evolution to Model Catalog
   - Backwards compatibility

2. **How API Keys Work in Portkey**
   - Portkey API Key vs Provider Credentials
   - Authentication flow
   - Security model

3. **How Model Catalog Works**
   - Credentials → Providers → Models hierarchy
   - Organization-level vs workspace-level
   - Inheritance model

4. **Credential Storage**
   - How credentials are stored (encrypted vaults)
   - Security measures
   - Key rotation

5. **Budget Limits**
   - Setting budget limits
   - Cost-based vs token-based
   - Workspace-level budgets
   - Alert thresholds

6. **Rate Limits**
   - Request-based limits
   - Token-based limits
   - Time windows (minute/hour/day)

7. **Model Access Control**
   - Model provisioning (allow-lists)
   - Workspace-level access
   - User-level restrictions via API keys
   - Model whitelist guardrail

8. **Model Rules Guardrail**
   - What Model Rules are
   - How to configure
   - Use cases
   - Examples

9. **Migration Guide**
   - Quick reference: Virtual Keys → Model Catalog
   - Code examples comparison
   - Common patterns

10. **Backwards Compatibility**
    - Using `virtual_key` header (still works)
    - Legacy configs
    - Migration timeline

**Note:** The Virtual Keys page (`product/ai-gateway/virtual-keys.mdx`) has been updated with comprehensive content covering API keys, credentials, budgets, rate limits, and model access control.

---

## Part 6: Migration Phases

### Phase 1: Foundation (Week 1) ✅
- ✅ Create comprehensive Virtual Keys page
- ✅ Update core product pages (Group 1)
- ✅ Create migration templates
- ✅ Merge duplicate integrations page

### Phase 2: Provider Pages (Week 2-3)
- Update all LLM provider integration pages (Group 2)
- Standardize format across all providers
- Update code examples

### Phase 3: Library Integrations (Week 4)
- Update library integration pages (Group 3)
- Update gateway feature pages (Group 4)

### Phase 4: Guides & Enterprise (Week 5)
- Update guides and tutorials (Group 5)
- Update enterprise/admin pages (Group 8)

### Phase 5: Cleanup (Week 6)
- Update API reference (Group 6)
- Update tracing providers (Group 7)
- Final review and consistency check

---

## Part 7: Checklists

### Checklist for Each Page

- [ ] Concise "Add Provider" flow (4 steps, conditional step 3)
- [ ] Recommended code method shown (model prefix)
- [ ] Recommended config method shown (model in override_params)
- [ ] Link to Model Catalog for all detailed options
- [ ] Quick tip about existing credentials
- [ ] Consistent terminology (credentials, providers, models)
- [ ] Page stays focused and scannable (no long sections on all methods)
- [ ] Backwards compatibility noted where `virtual_key` still works

### Quality Checklist

- [ ] Uses password manager analogy where helpful
- [ ] Focuses on user outcomes, not system architecture
- [ ] Reduces jargon (uses "credentials" instead of "Integration" where appropriate)
- [ ] Shows simplest path first
- [ ] Links to detailed docs for all options
- [ ] Follows writing style guide (direct, concise, Bun-style)
- [ ] Hides "Integration" concept from workspace users (Model Catalog pages)
- [ ] Applies progressive disclosure (right information for right audience)
- [ ] Focuses on actions, not architecture
- [ ] Introduces one concept at a time
- [ ] For org admins: Leads with benefits, not technical details

---

## Part 8: Where to Link

**Anchor Links in Model Catalog:**
- **Setup details:** `/product/model-catalog#adding-an-ai-provider`
- **Code examples:** `/product/model-catalog#using-provider-models`
- **Provider header:** `/product/model-catalog#using-provider-header`
- **Config examples:** `/product/model-catalog#3-specify-provider-in-the-config`
- **Credentials management:** `/product/model-catalog/integrations`
- **Complete guide:** `/product/model-catalog`

---

## Part 9: Important Notes

- **Model Rules Guardrail**: Need more information from user about this feature
- **Backwards Compatibility**: Keep `virtual_key` header documented but mark as legacy
- **Consistency**: Use same patterns across all pages
- **User Experience**: Make migration feel seamless, not disruptive
- **One Source of Truth**: Detailed docs live in Model Catalog page - don't repeat everywhere
- **API Workflow**: Via API, `POST /providers` requires `integration_id` (must create Integration first). Via UI, creating provider with new credentials auto-creates workspace-only Integration.
- **Model Control**: Model lists are tied to Integrations - admins enable/disable models at Integration level, all Providers inherit that list

---

## Quick Reference: Key Principles

1. **Simplified flow:** "If credentials exist, just select. If not, create new ones."
2. **Show recommended method:** Model prefix format in code, model in override_params in configs
3. **Link to details:** Don't show all three methods everywhere - link to Model Catalog
4. **Clear recommendation:** "Use model prefix format - it's explicit and keeps everything in one place"
5. **Backwards compatible:** "Legacy virtual_key still works, but not recommended for new code"
6. **Password manager analogy:** "Store credentials once, use everywhere"
7. **Keep it concise:** 4 steps max, scannable, focused
8. **Progressive disclosure:** Hide "Integration" from workspace users, reveal for org admins only
9. **Focus on actions:** "Store credentials and share" not "Create Integration at org level"
10. **One concept at a time:** Don't explain inheritance, shared vs workspace-only upfront

---

**Ready to start migrating?** Begin with Group 2 (LLM Provider Integration Pages) using the templates in Part 3.

