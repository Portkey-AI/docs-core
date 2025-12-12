# Group 2 Migration Plan: LLM Provider Integration Pages

## ✅ STATUS: PHASES 1 & 2 COMPLETE

> **Last Updated:** November 28, 2025  
> **Phase 1 (High-Priority):** ✅ Complete  
> **Phase 2 (Special Cases):** ✅ Complete  
> **Phase 3 (Remaining Providers):** Pending

---

## Overview

**Group:** LLM Provider Integration Pages (Priority: HIGH)  
**Location:** `integrations/llms/*.mdx`  
**Total Files:** ~50+ provider pages  
**Goal:** Replace Virtual Keys references with Model Catalog approach, standardize code examples, and maintain backwards compatibility.

---

## Scope

### Files to Migrate

**High Priority (Most Used):**
- `integrations/llms/openai.mdx` - ~1200 lines, complex (org/project IDs)
- `integrations/llms/anthropic.mdx` - ~1300 lines
- `integrations/llms/azure-openai/azure-openai.mdx` - Special case (multiple deployments)
- `integrations/llms/bedrock/aws-bedrock.mdx` - Special case (AWS assumed role)
- `integrations/llms/vertex-ai.mdx` - Special case (GCP)
- `integrations/llms/gemini.mdx`
- `integrations/llms/mistral-ai.mdx`
- `integrations/llms/cohere.mdx`

**Medium Priority:**
- All other provider pages in `integrations/llms/*.mdx` (~40+ files)

**Special Cases:**
- Azure OpenAI: Multiple deployments per provider
- AWS Bedrock: Amazon assumed role support
- Vertex AI: GCP-specific authentication
- Self-hosted/BYOLM: Custom host configuration

---

## Common Patterns to Find & Replace

### Pattern 1: "Create Virtual Key" Sections

**Find:**
```markdown
## Creating your Virtual Key
1. Navigate to Virtual Keys...
2. Create a virtual key...
```

**Replace with:**
```markdown
## Add Provider in Model Catalog

1. Go to [**Model Catalog → Add Provider**](https://app.portkey.ai/model-catalog/providers)
2. Select **[Provider Name]**
3. Enter your API key/credentials
4. (Optional) Add **Custom Host** for self-hosted/dedicated endpoints
5. Name your provider (e.g., `[provider-slug]`)

<Card title="Complete Setup Guide" icon="book" href="/product/model-catalog">
  See all setup options and detailed configuration instructions
</Card>
```

**Note:** Custom base URLs are configured in Model Catalog during provider setup, not via runtime parameters like `custom_host`/`customHost` in code.

### Pattern 2: Code Examples with `virtual_key`

**Find:**
```python
portkey = Portkey(
    api_key="PORTKEY_API_KEY",
    virtual_key="PROVIDER"  # or provider="@PROVIDER"
)
```

**Replace with (Show One, Mention Other in Callout):**
```python
portkey = Portkey(api_key="PORTKEY_API_KEY")

response = portkey.chat.completions.create(
    model="@openai-prod/gpt-4o",  # Provider + model together
    messages=[{"role": "user", "content": "Hello!"}]
)
```

<Note>
**Tip:** You can also set `provider="@openai-prod"` in `Portkey()` and use just `model="gpt-4o"` in the request.
</Note>

**For backwards compatibility:**
```markdown
<Note>
**Legacy support:** The `virtual_key` parameter still works for backwards compatibility. Use `model="@provider-slug/model-name"` format for new code.
</Note>
```

**Important for cURL:**
The `x-portkey-provider` header must use the `@` prefix format (e.g., `@anthropic-prod`), not the plain provider name:
```bash
# ✅ Correct
-H "x-portkey-provider: @anthropic-prod"

# ❌ Wrong
-H "x-portkey-provider: anthropic"
```

### Pattern 3: References to Virtual Keys in Text

**Find:**
- "virtual key" → "provider" or "AI provider"
- "Create a virtual key" → "Add a provider"
- "Your virtual key" → "Your provider slug"
- "Virtual Keys system" → "Model Catalog"

**Examples:**
- ❌ "Add it to Portkey to create your Anthropic virtual key"
- ✅ "Add it to Portkey to create your Anthropic provider"

- ❌ "secure management of your LLM API keys through a virtual key system"
- ✅ "secure management of your LLM API keys through Model Catalog"

### Pattern 4: Links to Virtual Keys Documentation

**Find:**
```markdown
[Virtual Keys](/product/ai-gateway/virtual-keys)
```

**Replace with:**
```markdown
[Virtual Keys](/product/ai-gateway/virtual-keys) (Learn how Portkey's virtual key system works)
```

Or if context is about setup:
```markdown
[Model Catalog](/product/model-catalog) (Set up providers and manage credentials)
```

---

## Migration Checklist (Per Page)

For each provider page, verify:

- [ ] **Provider slug note** - Remove `<Note>Provider Slug: xyz</Note>` at the top (it's now set in Model Catalog, not needed upfront)
- [ ] **Introduction section** - Update to mention Model Catalog instead of virtual keys
- [ ] **Setup section** - Replace "Create Virtual Key" with "Add Provider" pattern
- [ ] **Code examples** - Update to use model prefix format (`@provider/model`)
- [ ] **SDK examples** - Remove `virtual_key` parameter, use model prefix
- [ ] **Quick Start section** - Include Portkey SDK (Python/JS) + OpenAI SDK (Python/JS) + cURL examples
- [ ] **cURL examples** - Update headers if needed
- [ ] **Config examples** - Update to use model in `override_params`
- [ ] **Provider-specific features** - Keep as-is, but update references
- [ ] **Links** - Update links to point to Model Catalog where appropriate
- [ ] **Backwards compatibility** - Add note about legacy `virtual_key` support

---

## Sample Migration: Anthropic Page

### Before:
```markdown
### 2. Initialize Portkey with the Virtual Key

To use Anthropic with Portkey, [get your Anthropic API key from here](https://console.anthropic.com/settings/keys), then add it to Portkey to create your Anthropic virtual key.

```python
portkey = Portkey(
    api_key="PORTKEY_API_KEY",
    provider="@PROVIDER"   # Replace with your virtual key for Anthropic
)
```
```

### After:
```markdown
### 2. Add Provider in Model Catalog

1. Go to [**Model Catalog → Add Provider**](https://app.portkey.ai/model-catalog/providers)
2. Select **Anthropic**
3. **If credentials exist:** Choose from dropdown
   **If creating new:** Enter your [Anthropic API key](https://console.anthropic.com/settings/keys)
4. Name your provider (e.g., `anthropic-prod`)

<Info>
**Quick tip:** If your org admin already set up credentials, just select them - no API keys needed!
</Info>

### 3. Use in Your Code

```python
from portkey_ai import Portkey

portkey = Portkey(api_key="PORTKEY_API_KEY")

response = portkey.chat.completions.create(
    model="@anthropic-prod/claude-3-sonnet",  # Provider + model together
    messages=[{"role": "user", "content": "Hello!"}]
)
```

<Note>
**Tip:** You can also set `provider="@anthropic-prod"` in `Portkey()` and use just `model="claude-3-sonnet"` in the request.
</Note>

---

## Special Cases

### 1. OpenAI (Org & Project IDs)

**Current:** Section on "Using Virtual Keys" with org/project ID fields

**Migration:**
- Keep the org/project ID functionality explanation
- Update to reference "Add Provider" instead of "Create Virtual Key"
- Update code examples to use model prefix format
- Keep the Frame/image showing the UI

**Location:** Lines ~1040-1068 in `openai.mdx`

### 2. Azure OpenAI (Multiple Deployments)

**Current:** Explains managing multiple Azure deployments under one virtual key

**Migration:**
- Update to explain multiple deployments under one provider
- Keep deployment alias functionality
- Update code examples

### 3. AWS Bedrock (Assumed Role)

**Current:** Special setup for Amazon assumed role

**Migration:**
- Keep assumed role setup instructions
- Update to reference "Add Provider" instead of "Create Virtual Key"
- Update code examples

### 4. Self-Hosted/BYOLM

**Current:** Custom host configuration in virtual key creation

**Migration:**
- Update to explain custom host in "Add Provider" flow (set in Model Catalog UI, not in code)
- **Do NOT** include code examples with `custom_host`/`customHost` parameters
- Custom base URLs are configured once in Model Catalog, then used automatically
- See `integrations/llms/vllm.mdx` and `integrations/llms/local-ai.mdx` as reference patterns

---

## Phased Approach

### Phase 1: High-Priority Pages (Week 1)
1. ✅ **Anthropic** - Simple, good template
2. ✅ **OpenAI** - Complex (org/project IDs), most used
3. ✅ **Gemini** - Standard case
4. ✅ **Mistral AI** - Standard case

**Goal:** Establish pattern, get user feedback

### Phase 2: Special Cases (Week 2)
1. ✅ **Azure OpenAI** - Multiple deployments
2. ✅ **AWS Bedrock** - Assumed role
3. ✅ **Vertex AI** - GCP authentication

**Goal:** Handle edge cases, refine approach

### Phase 3: Remaining Providers (Week 3-4)
1. Batch update remaining ~40+ provider pages
2. Use established patterns
3. Automated find/replace where possible

**Goal:** Complete migration

---

## Quality Checks

After migrating each page:

1. **Verify links work** - All internal links should resolve
2. **Check code examples** - All code should be runnable
3. **Test backwards compatibility** - Legacy `virtual_key` examples should still work
4. **Consistency** - Same pattern across all pages
5. **Provider-specific content** - Keep unique features, just update references
6. **SDK reference link** - Use `/api-reference/sdk/list` (NOT `/api-reference/portkey-sdk-client`)

---

## Questions to Resolve

1. **Provider-specific setup steps:** Should we keep provider-specific credential instructions (e.g., "Get your OpenAI API key from...") or make it generic?

2. **Provider slug examples:** Should we standardize provider slug examples (e.g., always use `@provider-prod`) or keep provider-specific names?

3. **Special features:** How much provider-specific setup detail should we keep vs. linking to Model Catalog?

4. **Images/Frames:** Should we update screenshots showing "Virtual Keys" UI to show "Model Catalog" UI?

---

## Next Steps

~~1. **Review this plan** - Get alignment on approach~~ ✅  
~~2. **Start with Anthropic** - Simple case, establish pattern~~ ✅  
~~3. **Get feedback** - Review first migration before proceeding~~ ✅  
~~4. **Iterate** - Refine approach based on feedback~~ ✅  
~~5. **Scale** - Apply to remaining pages~~ ✅ (Phase 1 & 2 complete)

### Remaining Work (Phase 3)
- [ ] Batch update remaining ~40+ provider pages using established patterns
- [ ] Consider automated find/replace for common patterns

---

## Resources

- **Template:** See `MASTER_MIGRATION_GUIDE.md` Part 3, Pattern 4
- **Code Examples:** See `MASTER_MIGRATION_GUIDE.md` Part 3, Patterns 1-3
- **Writing Style:** See `WRITING_STYLE_GUIDE.md`
- **Model Catalog Reference:** `/product/model-catalog`

---

## Completion Summary

### Phase 1 Completed Pages ✅
| Page | Status | Notes |
|------|--------|-------|
| `anthropic.mdx` | ✅ Complete | Model Catalog references, `@provider/model` format |
| `openai.mdx` | ✅ Complete | Includes org/project ID support, backwards compat note |
| `gemini.mdx` | ✅ Complete | Standard migration |
| `mistral-ai.mdx` | ✅ Complete | Standard migration |
| `cohere.mdx` | ✅ Complete | Standard migration |

### Phase 2 Completed Pages ✅
| Page | Status | Notes |
|------|--------|-------|
| `azure-openai/azure-openai.mdx` | ✅ Complete | Multiple deployments, removed Provider Slug note |
| `bedrock/aws-bedrock.mdx` | ✅ Complete | Assumed role links updated to Model Catalog path |
| `vertex-ai.mdx` | ✅ Complete | GCP auth, Quick Start with `@vertex-ai/model` format |

### Verification Checks Passed
- [x] No remaining `Provider Slug.` notes in migrated pages
- [x] No `virtual_key` references (except backwards compat notes)
- [x] Model Catalog terminology used consistently
- [x] `@provider/model` format in code examples
- [x] Links updated from virtual-keys paths to model-catalog paths

