# Group 5 Migration Plan: Guides and Tutorials

## Overview

**Group:** Guides and Tutorials  
**Location:** `guides/*.mdx`  
**Total Files:** 25 files with "Virtual Key" mentions  
**Priority:** MEDIUM  
**Goal:** Update step-by-step instructions, replace Virtual Keys references with Model Catalog, update code examples.

---

## Files to Migrate

### Getting Started Guides (6 files)

| File | VK Mentions | Complexity |
|------|-------------|------------|
| `guides/getting-started/getting-started-with-ai-gateway.mdx` | 6 | High - Core onboarding |
| `guides/getting-started/llama-3-on-groq.mdx` | 2 | Low |
| `guides/getting-started/return-repeat-requests-from-cache.mdx` | 1 | Low |
| `guides/getting-started/trigger-automatic-retries-on-llm-failures.mdx` | 1 | Low |
| `guides/getting-started/a-b-test-prompts-and-models.mdx` | 1 | Low |
| `guides/getting-started/101-on-portkey-s-gateway-configs.mdx` | 3 | Medium |

### Integration Guides (5 files)

| File | VK Mentions | Complexity |
|------|-------------|------------|
| `guides/integrations/vercel-ai.mdx` | 4 | Medium |
| `guides/integrations/groq.mdx` | 4 | Medium |
| `guides/integrations/langchain.mdx` | 2 | Low |
| `guides/integrations/mixtral-8x22b.mdx` | 2 | Low |
| `guides/integrations/llama-3-on-portkey-+-together-ai.mdx` | 2 | Low |
| `guides/integrations/arize-portkey.mdx` | 1 | Low |

### Use Case Guides (11 files)

| File | VK Mentions | Complexity |
|------|-------------|------------|
| `guides/use-cases/fallback-from-sdxl-to-dall-e-3.mdx` | 5 | Medium |
| `guides/use-cases/setup-openai-greater-than-azure-openai-fallback.mdx` | 5 | Medium |
| `guides/use-cases/openai-computer-use.mdx` | 5 | Medium |
| `guides/use-cases/deepseek-r1.mdx` | 3 | Medium |
| `guides/use-cases/comparing-top10-lmsys-models-with-portkey.mdx` | 2 | Low |
| `guides/use-cases/librechat-web-search.mdx` | 1 | Low |
| `guides/use-cases/build-an-article-suggestion-app-with-supabase-pgvector-and-portkey.mdx` | 1 | Low |
| `guides/use-cases/enforcing-json-schema-with-anyscale-and-together.mdx` | 1 | Low |
| `guides/use-cases/smart-fallback-with-model-optimized-prompts.mdx` | 1 | Low |
| `guides/use-cases/how-to-use-openai-sdk-with-portkey-prompt-templates.mdx` | 1 | Low |
| `guides/use-cases/run-portkey-on-prompts-from-langchain-hub.mdx` | 1 | Low |

### Other Guides (2 files)

| File | VK Mentions | Complexity |
|------|-------------|------------|
| `guides/prompts/llama-prompts.mdx` | 14 | High |
| `guides/ted-ai-hack-24.mdx` | 1 | Low |

---

## Migration Patterns

### Pattern 1: Text Terminology Updates

**Find → Replace:**
- "virtual key" → "provider" (in context of what to use)
- "Virtual Key" → "provider" or "Model Catalog" (depending on context)
- "create a virtual key" → "add a provider"
- "your virtual key" → "your provider slug"
- "Virtual Keys page" → "Model Catalog"

### Pattern 2: Code Example Updates

**Before:**
```python
from portkey_ai import createHeaders

headers = createHeaders(
    api_key="PORTKEY_API_KEY",
    virtual_key="openai-xxx"
)
```

**After:**
```python
from portkey_ai import createHeaders

headers = createHeaders(
    api_key="PORTKEY_API_KEY",
    provider="@openai-prod"
)
```

### Pattern 3: Config Example Updates

**Before:**
```json
{
  "virtual_key": "openai-key",
  "override_params": { "model": "gpt-4" }
}
```

**After:**
```json
{
  "override_params": { "model": "@openai-prod/gpt-4" }
}
```

### Pattern 4: Setup Instructions

**Before:**
> 1. Go to the Virtual Keys page
> 2. Click "Add Key"
> 3. Enter your OpenAI API key
> 4. Copy the Virtual Key ID

**After:**
> 1. Go to [Model Catalog](https://app.portkey.ai/model-catalog)
> 2. Click "Add Provider"
> 3. Select OpenAI and enter your API key
> 4. Name your provider (e.g., `openai-prod`)

---

## Quick Reference Checklist

*Learnings from migrating `getting-started-with-ai-gateway.mdx`*

### Find & Replace (use `replace_all`)

| Find | Replace |
|------|---------|
| `virtualKey: "VIRTUAL_KEY"` | Remove, use `model="@provider-slug/model-name"` instead |
| `virtualKey: 'VIRTUAL_KEY'` | Remove, use `model="@provider-slug/model-name"` instead |
| `virtual_key = "VIRTUAL_KEY"` | Remove, use `model="@provider-slug/model-name"` instead |
| `provider="@VIRTUAL_KEY"` | `model="@provider-slug/model-name"` in request |
| `<Tabs>` | `<CodeGroup>` |
| `</Tabs>` | `</CodeGroup>` |
| `<Tab title="...">` | Delete (CodeGroup uses code fence titles) |
| `</Tab>` | Delete |
| `200+ LLMs` | `1,600+ LLMs` |

### Add Icons (use `replace_all`)

```
```python Python         →  ```python Python icon="python"
```javascript JavaScript →  ```javascript JavaScript icon="square-js"
```python OpenAI Python  →  ```python OpenAI Python icon="openai"
```javascript OpenAI JS  →  ```javascript OpenAI JS icon="openai"
```sh cURL               →  ```sh cURL icon="square-terminal"
```

### Code Example Structure

Every code example should have **5 tabs**:
1. `Python` (Portkey SDK) - `icon="python"`
2. `JavaScript` (Portkey SDK) - `icon="square-js"`
3. `OpenAI Python` - `icon="openai"`
4. `OpenAI JS` - `icon="openai"`
5. `cURL` - `icon="square-terminal"`

### Model Format

```python
# OLD
portkey = Portkey(api_key="PORTKEY_API_KEY", virtual_key="openai-key")
response = portkey.chat.completions.create(model="gpt-4o", ...)

# NEW
portkey = Portkey(api_key="PORTKEY_API_KEY")
response = portkey.chat.completions.create(model="@openai-prod/gpt-4o", ...)
```

### Sections to Include (if applicable)

- **Quick Start** - 5 SDK versions with Model Catalog setup
- **Add Provider in Model Catalog** - Link to `/product/model-catalog`
- **Using with OpenAI SDK** - Show base_url + api_key change
- **Using with Anthropic SDK** - Show `/messages` endpoint support
- **Supported Integrations** - Cards linking to integration categories
- **Next Steps** - Cards to related features

### Key Terminology

| Old | New |
|-----|-----|
| Virtual Key | Provider (in Model Catalog) |
| Create a Virtual Key | Add Provider |
| Virtual Keys page | Model Catalog |
| `virtual_key` parameter | `model="@slug/model"` format |

### Style Reminders

- Use `<CodeGroup>` not `<Tabs>`
- Keep examples concise (no repetitive variations)
- Link to detailed docs instead of explaining everything
- Update model names to current versions (`gpt-4o`, `claude-sonnet-4-5-20250929`)

---

## Migration Strategy

### Phase 1: High-Impact Guides (3 files)
These are core onboarding/reference guides:

1. **`getting-started-with-ai-gateway.mdx`** - Primary onboarding
2. **`101-on-portkey-s-gateway-configs.mdx`** - Config reference
3. **`llama-prompts.mdx`** - 14 mentions, likely needs significant updates

### Phase 2: Integration Guides (5 files)
Provider-specific integration tutorials:

1. `vercel-ai.mdx`
2. `groq.mdx`
3. `langchain.mdx`
4. `mixtral-8x22b.mdx`
5. `llama-3-on-portkey-+-together-ai.mdx`

### Phase 3: Use Case Guides (11 files)
Practical examples - mostly simple text updates:

- Start with higher-mention files (fallback guides, deepseek-r1)
- Batch process low-mention files (1 mention = usually just a link or passing reference)

### Phase 4: Remaining (2 files)
- `arize-portkey.mdx`
- `ted-ai-hack-24.mdx`

---

## Automation Opportunities

Many of these files likely have simple, repeatable patterns. Consider a script for:

1. **Text replacements:**
   - `virtual_key=` → `provider=`
   - `"virtual_key":` → `"provider":`
   - `Virtual Key` → `provider` (contextual)

2. **Link updates:**
   - `/product/ai-gateway/virtual-keys` → `/product/model-catalog` (when discussing setup)

3. **Manual review needed for:**
   - Config examples with multiple providers
   - Step-by-step UI instructions
   - Context-dependent terminology

---

## Quality Checklist (Per File)

- [ ] All `virtual_key` parameters updated to `provider`
- [ ] Config examples use `@provider-slug/model` format
- [ ] Setup instructions point to Model Catalog
- [ ] Links updated where appropriate
- [ ] Code examples work with new pattern
- [ ] No broken references to old UI elements

---

## Notes

- **Guides are tutorials** - Focus on making them work, not perfection
- **Many are dated** - Some guides reference old models/providers; update if easy, otherwise leave
- **Low-mention files** - Often just a passing reference; quick fix
- **High-mention files** - May need structural updates similar to library pages

---

## Progress Tracking

### Phase 1: High-Impact Guides
- [x] `guides/getting-started/getting-started-with-ai-gateway.mdx` ✅
- [x] `guides/getting-started/101-on-portkey-s-gateway-configs.mdx` ✅
- [x] `guides/prompts/llama-prompts.mdx` ✅

### Phase 2: Integration Guides
- [x] `guides/integrations/vercel-ai.mdx` ✅
- [x] `guides/integrations/groq.mdx` ✅
- [x] `guides/integrations/langchain.mdx` ✅
- [x] `guides/integrations/mixtral-8x22b.mdx` ✅
- [x] `guides/integrations/llama-3-on-portkey-+-together-ai.mdx` ✅
- [x] `guides/integrations/arize-portkey.mdx` ✅

### Phase 3: Use Case Guides
- [x] `guides/use-cases/fallback-from-sdxl-to-dall-e-3.mdx` ✅
- [x] `guides/use-cases/setup-openai-greater-than-azure-openai-fallback.mdx` ✅
- [x] `guides/use-cases/openai-computer-use.mdx` ✅
- [x] `guides/use-cases/deepseek-r1.mdx` ✅
- [x] `guides/use-cases/comparing-top10-lmsys-models-with-portkey.mdx` ✅
- [x] `guides/use-cases/librechat-web-search.mdx` ✅
- [x] `guides/use-cases/build-an-article-suggestion-app-with-supabase-pgvector-and-portkey.mdx` ✅
- [x] `guides/use-cases/enforcing-json-schema-with-anyscale-and-together.mdx` ✅
- [x] `guides/use-cases/smart-fallback-with-model-optimized-prompts.mdx` ✅
- [x] `guides/use-cases/how-to-use-openai-sdk-with-portkey-prompt-templates.mdx` ✅
- [x] `guides/use-cases/run-portkey-on-prompts-from-langchain-hub.mdx` ✅

### Phase 4: Other
- [x] `guides/getting-started/llama-3-on-groq.mdx` ✅
- [x] `guides/getting-started/return-repeat-requests-from-cache.mdx` ✅
- [x] `guides/getting-started/trigger-automatic-retries-on-llm-failures.mdx` ✅
- [x] `guides/getting-started/a-b-test-prompts-and-models.mdx` ✅
- [x] `guides/ted-ai-hack-24.mdx` ✅

---

## Related Groups Still Pending

After Group 5, these groups remain:

| Group | Description | Files |
|-------|-------------|-------|
| Group 6 | API Reference | `api-reference/inference-api/*.mdx`, SDK docs |
| Group 7 | Tracing Providers | `integrations/tracing-providers/*.mdx` (6 files) |
| Group 8 | Enterprise/Admin Pages | `product/enterprise-offering/*.mdx`, admin docs |

---

## Resources

- **Master Guide:** `MASTER_MIGRATION_GUIDE.md`
- **Writing Style:** `WRITING_STYLE_GUIDE.md`
- **Reference (Library):** `integrations/libraries/langchain-python.mdx`
- **Reference (LLM Provider):** `integrations/llms/anthropic.mdx`
- **Reference (Guide):** `guides/getting-started/getting-started-with-ai-gateway.mdx` ✅ Migrated
- **Model Catalog Page:** `/product/model-catalog`

