# Group 3 Migration Plan: Library Integration Pages & Gateway Feature Pages

## Overview

**Group:** Library Integration Pages (Group 3) + Gateway Feature Pages (Group 4)  
**Location:** `integrations/libraries/*.mdx` and `product/ai-gateway/*.mdx`  
**Total Files:** ~20+ library pages + 6 gateway feature pages  
**Goal:** Replace Virtual Keys references with Model Catalog approach, use concise "Add Provider" pattern, and maintain backwards compatibility.

---

## Scope

### Group 3: Library Integration Pages

**Files to Migrate:**

**High Priority (Most Used):**
- `integrations/libraries/langchain-python.mdx` - **Reference file** (comprehensive)
- `integrations/libraries/langchain-js.mdx` - Similar to Python version
- `integrations/libraries/openai-compatible.mdx` - Generic OpenAI-compatible projects
- `integrations/libraries/llama-index-python.mdx` - Popular framework
- `integrations/libraries/dspy.mdx` - Framework integration

**Already Updated:**
- ✅ `integrations/libraries/cursor.mdx` - Can be used as reference for the new pattern

**Medium Priority (Tools/IDEs):**
- `integrations/libraries/cline.mdx`
- `integrations/libraries/roo-code.mdx`
- `integrations/libraries/zed.mdx`
- `integrations/libraries/claude-code.mdx`
- `integrations/libraries/github-copilot.mdx`

**Lower Priority:**
- `integrations/libraries/autogen.mdx`
- `integrations/libraries/instructor.mdx`
- `integrations/libraries/microsoft-semantic-kernel.mdx`
- `integrations/libraries/n8n.mdx`
- `integrations/libraries/openwebui.mdx`
- `integrations/libraries/anythingllm.mdx`
- `integrations/libraries/langflow.mdx`
- `integrations/libraries/librechat.mdx`
- Plus 10+ other tool integration pages

### Group 4: Gateway Feature Pages

**Files to Migrate:**
- `product/ai-gateway/batches.mdx`
- `product/ai-gateway/load-balancing.mdx`
- `product/ai-gateway/fallbacks.mdx`
- `product/ai-gateway/circuit-breaker.mdx`
- `product/ai-gateway/canary-testing.mdx`
- `product/ai-gateway/automatic-retries.mdx`

---

## Common Patterns to Find & Replace

### Pattern 1: Virtual Key Terminology in Text

**Find:**
- "virtual key" → "provider" or "AI provider"
- "Create a virtual key" → "Add a provider"
- "Your virtual key" → "Your provider slug"
- "Virtual Keys system" → "Model Catalog"
- "using Virtual Keys" → "using Model Catalog"
- "Secure Virtual Keys" → "Secure Provider Management"

**Examples:**

❌ **Before:**
> "Securely manage LLM provider API keys using Portkey Virtual Keys in your Langchain setup."

✅ **After:**
> "Securely manage LLM provider API keys through Model Catalog in your Langchain setup."

---

❌ **Before:**
> "Switch LLMs by changing the `virtual_key` in `createHeaders`"

✅ **After:**
> "Switch LLMs by changing the `provider` in `createHeaders`"

---

### Pattern 2: Code Examples with `virtual_key`

**Find (in Langchain/Library code):**
```python
portkey_headers = createHeaders(
    api_key=PORTKEY_API_KEY,
    virtual_key="anthropic-key"  # or provider="anthropic"
)
```

**Replace with:**
```python
portkey_headers = createHeaders(
    api_key=PORTKEY_API_KEY,
    provider="@anthropic"  # Provider slug with @ prefix
)
```

**Key Points:**
- Remove `virtual_key` parameter
- Use `provider="@provider-slug"` format
- Add note about legacy `virtual_key` support

---

### Pattern 3: Setup Sections → Concise "Add Provider" Pattern

**Find (Long setup sections):**
```markdown
1. **Create Anthropic Virtual Key:** In Portkey, add your Anthropic API key and get the Virtual Key ID.
2. Navigate to Virtual Keys page...
3. Click "Add Key"...
```

**Replace with (Concise pattern):**
```markdown
### Add Provider

1. Go to [**Model Catalog → Add Provider**](https://app.portkey.ai/model-catalog/providers)
2. Select **[Provider Name]**
3. Choose existing credentials or create new by entering your API keys
4. Name your provider (e.g., `anthropic-prod`)

<Card title="Complete Setup Guide →" href="/product/model-catalog">
  See all setup options, code examples, and detailed instructions
</Card>
```

**Key Points:**
- Keep it to 4 steps max
- Use "Choose existing credentials or create new" (conditional in one line)
- Link to Model Catalog for detailed options
- Use Card component for visual emphasis

---

### Pattern 4: Config Examples

**Find:**
```json
{
  "targets": [{
    "virtual_key": "openai-key",
    "override_params": { "model": "gpt-4" }
  }]
}
```

**Replace with:**
```json
{
  "targets": [{
    "override_params": { "model": "@openai-prod/gpt-4" }
  }]
}
```

**Alternative (if showing provider separately):**
```json
{
  "targets": [{
    "provider": "@openai-prod",
    "override_params": { "model": "gpt-4" }
  }]
}
```

---

### Pattern 5: Links to Virtual Keys Documentation

**Find:**
```markdown
[Virtual Keys](/product/ai-gateway/virtual-keys)
```

**Replace with (Context-dependent):**

**If discussing how the system works:**
```markdown
[Virtual Keys](/product/ai-gateway/virtual-keys) (Learn how Portkey's API key system works)
```

**If discussing setup:**
```markdown
[Model Catalog](/product/model-catalog) (Set up providers and manage credentials)
```

---

## Migration Strategy by File Type

### Type A: Framework Integrations (Langchain, LlamaIndex, DSPy)

**Pattern:** These show how to use Portkey with a framework

**Migration Steps:**
1. Update intro to mention Model Catalog instead of Virtual Keys
2. Replace verbose setup sections with concise "Add Provider" pattern
3. Update code examples to use `provider="@provider-slug"`
4. Update multi-LLM examples (Anthropic, Gemini, etc.)
5. Keep backwards compatibility note
6. Remove redundant explanations - link to Model Catalog

**Reference:** `langchain-python.mdx` (our main reference)

---

### Type B: Tool/IDE Integrations (Cursor, Cline, Roo Code, etc.)

**Pattern:** These show step-by-step UI-based setup with enterprise features

**Migration Steps:**
1. Use `<Steps>` component for structured setup
2. Some files use older "Create Integration" pattern - update to "Add Provider"
3. Update to concise 4-step pattern
4. Update config examples
5. Keep enterprise governance sections (budget limits, etc.)

**Reference:** `cursor.mdx` (already updated, good pattern)

**Note:** Some tool integrations (like `cline.mdx`, `openai-compatible.mdx`) still use the old "Create an Integration" pattern in their setup. We need to update these to the concise "Add Provider" pattern.

---

### Type C: Gateway Feature Pages (Fallbacks, Load Balancing, etc.)

**Pattern:** These explain gateway features with config examples

**Migration Steps:**
1. Update config examples to use `model="@provider/model"` format
2. Replace `virtual_key` references in configs
3. Update text references to Virtual Keys
4. Keep feature explanations as-is
5. Update code examples where providers are referenced

**Note:** Focus on config examples - that's where most Virtual Keys references appear

---

## Detailed Migration Checklist (Per Page)

### For Library Integration Pages:

- [ ] **Introduction** - Update to mention Model Catalog instead of Virtual Keys
- [ ] **Setup section** - Replace with concise "Add Provider" pattern (4 steps max)
- [ ] **Basic usage code** - Update to use `provider="@provider-slug"` (no `virtual_key`)
- [ ] **Multi-LLM examples** - Update all provider examples (Anthropic, Gemini, etc.)
- [ ] **Config examples** - Update to use `model="@provider/model"` or `provider="@provider"`
- [ ] **Terminology** - Replace "virtual key" with "provider" throughout text
- [ ] **Links** - Update links to point to Model Catalog where appropriate
- [ ] **Backwards compatibility** - Add note about legacy `virtual_key` support
- [ ] **Card components** - Use Card for linking to Model Catalog (not just inline links)
- [ ] **Remove redundancy** - Don't explain all methods; link to Model Catalog

### For Gateway Feature Pages:

- [ ] **Config examples** - Update all configs to use recommended format
- [ ] **Code examples** - Update any code that references providers
- [ ] **Text references** - Replace "virtual key" with "provider"
- [ ] **Links** - Update Virtual Keys links where appropriate
- [ ] **Feature explanations** - Keep as-is (focus on the feature)

---

## Sample Migration: Langchain Python Page

### ✅ COMPLETED - Reference Implementation (FINAL)

**File:** `integrations/libraries/langchain-python.mdx`

### Key Discovery: Ultra-Simplified 3-Parameter Pattern

After analyzing Langchain's latest positioning (agents-first, `init_chat_model()` introduction), we discovered the **simplest possible pattern**:

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="@openai-prod/gpt-4o",       # Provider slug from Model Catalog
    base_url="https://api.portkey.ai",
    api_key="PORTKEY_API_KEY"          # Your Portkey API key
)
```

**Why this works:**
- Provider slug is embedded in model string (`@openai-prod/gpt-4o`)
- Portkey extracts provider from the model string
- No need for `createHeaders()` or `default_headers` for basic usage
- Only 3 parameters needed!

### Final Document Structure

1. **Quick Start** (3-parameter pattern, working code immediately)
2. **Why Add Portkey** (value prop with CardGroup - emphasize unique features)
3. **Setup** (4 steps: install, add provider, get API key, use in code)
4. **Switching Providers** (just change model string)
5. **Using with Langchain Agents** ⭐ **PROMINENT** - Main use case
6. **Works With All Features** (streaming, tools - brief)
7. **Dynamic Model Selection** ⭐ **NEW** - Conditional routing via configs
8. **Advanced Features via Configs** (brief mention with link)
9. **Embeddings & Prompt Management** (keep short)
10. **Migration from Direct OpenAI** (before/after comparison)

### What We Removed (Based on Feedback)

❌ **Removed detailed sections on:**
- Fallbacks, retries, load balancing, semantic caching (verbose examples)
- Each getting their own section with configs
- Repetitive "Advanced Features" sections

✅ **Consolidated to:**
- One "Advanced Features via Configs" section
- Brief mention with link to relevant pages
- Focus on the unique value props

### What We Emphasized (Based on User Needs)

✅ **Agent flows** - Now prominent with full example
- Using `create_agent` with tools
- What gets logged (every step, tool call, costs)
- Visual showing traces

✅ **Dynamic Model Selection** - Featured as unique capability
- Conditional routing via Portkey configs
- Cost optimization examples
- Model specialization by task
- All tracked automatically

✅ **Migration path** - Clear before/after
- Direct OpenAI → Portkey (3 parameter changes)
- Emphasize "minimal changes"

### Key Insights from Final Revision:

1. **Langchain positioning changed significantly:**
   - Now agents-first (not just chains)
   - Introduced `init_chat_model()` for model switching
   - Both `ChatOpenAI` and `init_chat_model()` are officially supported
   - Our docs should reflect this evolution

2. **Ultra-simple pattern wins:**
   - 3 parameters (`model`, `base_url`, `api_key`)
   - No `createHeaders()` in basic examples
   - Only show `createHeaders()` for advanced features (configs)

3. **Focus on unique differentiators:**
   - Dynamic model selection via conditional routing
   - Agent observability (full traces)
   - Not generic features everyone has

4. **Document structure follows user journey:**
   - Quick Start FIRST (no UI friction)
   - Value prop SECOND (prove it's worth setup)
   - Setup THIRD (after they're convinced)
   - Advanced features LAST (progressive disclosure)

5. **Dynamic routing is a hero feature:**
   - Langchain's `config={"configurable": {...}}` doesn't work with Portkey
   - Use Portkey's conditional routing with metadata instead
   - More powerful: server-side logic, full tracking
   - Positioned as unique capability

6. **Avoid confusing patterns:**
   - Don't show Langchain's `configurable` pattern (doesn't work with `@provider/model`)
   - Use Portkey's actual API (conditional routing)
   - Be accurate to how Portkey actually works

#### 1. **Setup Section (Step 2 → Steps 2-3)**
**Before:**
```markdown
### 2. Basic Setup: `ChatOpenAI` with Portkey
[Long explanation with provider API keys]
```

**After:**
```markdown
### 2. Add Provider in Model Catalog
[Concise 4-step pattern with Card link]

### 3. Basic Setup: `ChatOpenAI` with Portkey
[Simplified code using provider slug]
```

**Key Changes:**
- Split setup into two clear steps
- Added concise "Add Provider" pattern (4 steps)
- Removed need for provider API keys in code
- Changed `api_key=PROVIDER_API_KEY` to `api_key="portkey"` (placeholder)
- Updated `provider="openai"` to `provider="@openai-prod"` (with @ prefix)
- Added Card component linking to Model Catalog

#### 2. **CardGroup Section**
**Before:**
```markdown
<Card title="Secure Virtual Keys">
  <p>...using Portkey Virtual Keys...</p>
</Card>
```

**After:**
```markdown
<Card title="Secure Provider Management">
  <p>...through Model Catalog...</p>
</Card>
```

#### 3. **Multi-LLM Integration Section**
**Before:**
- Verbose "Create Virtual Key" instructions
- Used `provider="@anthropic"` (generic)
- Mentioned "Virtual Keys" throughout

**After:**
- Concise "Add Provider" pattern with Card link
- Uses `provider="@anthropic-prod"` (specific slug example)
- Replaced "Virtual Keys" with "Model Catalog"
- Added backwards compatibility note
- Simplified code examples (removed placeholder comments about Virtual Keys)

#### 4. **Config Examples (Caching & Reliability)**
**Before:**
```json
{
  "provider":"@your_openai_virtual_key_id",
  "override_params": { "model": "gpt-4o" }
}
```

**After:**
```json
{
  "override_params": { "model": "@openai-prod/gpt-4o" }
}
```

**Key Changes:**
- Use model prefix format in configs
- Remove separate `provider` field when using model prefix
- Updated fallback config to use model prefix for both targets

#### 5. **Secure Provider Management Section (formerly "Secure Virtual Keys")**
**Before:**
```markdown
## 6. Secure Virtual Keys

Portkey's [Virtual Keys](/product/ai-gateway/virtual-keys) are vital...
- Store API keys in vault. Code uses Virtual Key IDs.
- Switch providers by changing `virtual_key`
```

**After:**
```markdown
## 6. Secure Provider Management

Portkey's [Model Catalog](/product/model-catalog) provides secure...
- Store API keys in vault. Code uses provider slugs.
- Switch providers by changing `provider`
```

#### 6. **All Code Examples**
**Changed throughout:**
- `api_key="placeholder_key"` → `api_key="portkey"`
- `provider="@openai"` → `provider="@openai-prod"` (specific examples)
- Added backwards compatibility note after multi-LLM section

### Lessons Learned & Pattern Changes:

1. **3-parameter pattern is the foundation:**
   ```python
   model = ChatOpenAI(
       model="@provider-slug/model-name",
       base_url="https://api.portkey.ai",
       api_key="PORTKEY_API_KEY"
   )
   ```
   - Use this everywhere as the primary pattern
   - Only show `createHeaders()` when needed for configs

2. **Agents-first approach:**
   - Langchain is now primarily about agents
   - Show agent integration prominently (not buried)
   - Include `create_agent` example early
   - Explain what gets logged (tool calls, steps, costs)

3. **De-emphasize generic features:**
   - Don't have separate sections for fallbacks, caching, retries
   - Consolidate to "Advanced Features via Configs" with link
   - Focus space on unique differentiators

4. **Feature dynamic model selection:**
   - This is unique to Portkey
   - Use conditional routing (not Langchain's `configurable`)
   - Show practical use cases (cost optimization, task routing)
   - Emphasize automatic tracking

5. **Quick Start must work immediately:**
   - NO "go to UI first" friction
   - Show working code at top
   - Setup steps come AFTER they see value
   - Prove it works before asking for setup

6. **Value prop before setup:**
   - CardGroup with benefits right after Quick Start
   - Emphasize unique capabilities (dynamic routing, agent observability)
   - Make them want to do the setup

7. **Migration focus:**
   - Most users migrating from direct OpenAI
   - Show clear before/after (3 parameter changes)
   - Emphasize "works with existing code"

8. **Be accurate about capabilities:**
   - Don't show patterns that don't actually work
   - Use Portkey's real APIs (conditional routing, not Langchain configurable)
   - Link to correct documentation

### Quality Checklist Results:

- ✅ Terminology consistent (no "virtual key" in new instructions)
- ✅ Concise setup (4 steps, links to Model Catalog)
- ✅ Code examples updated (use `provider="@slug"`)
- ✅ Config examples updated (use model prefix format)
- ✅ Links correct (point to Model Catalog)
- ✅ Backwards compatibility noted
- ✅ Card components used
- ✅ Writing style (direct, concise)
- ✅ No redundancy (linked to Model Catalog for details)

---

## Special Cases

### Case 1: Langchain Python - Multiple Provider Examples

**Current:** Has separate examples for Anthropic, Vertex AI, etc. with verbose setup

**Migration:**
- Use concise "Add Provider" pattern for each
- Show the code difference (just change `provider` and `model`)
- Link to provider-specific pages for details

### Case 2: Tool/IDE Integrations with Screenshots

**Current:** Some have screenshots showing "Virtual Keys" or "Create Integration" UI

**Migration:**
- Update text references
- Keep screenshots (UI updates separately)
- Add notes if screenshots show old UI

### Case 3: Config-Heavy Pages (Caching, Reliability)

**Current:** Config examples use `virtual_key` in targets

**Migration:**
- Update all config JSON examples
- Show recommended format (`model="@provider/model"`)
- Add note about legacy `virtual_key` support

---

## Phased Approach

### Week 1: High-Priority Library Pages
1. **Langchain Python** - Reference file, establish pattern
2. **Langchain JS** - Similar to Python
3. **OpenAI Compatible** - Generic pattern
4. **LlamaIndex Python** - Popular framework

**Goal:** Establish clear pattern for library integrations

### Week 2: Tool/IDE Integration Pages
1. **Cline** - Update from old "Create Integration" pattern
2. **Roo Code** - Similar to Cline
3. **Zed** - IDE integration
4. **Claude Code** - Tool integration
5. **GitHub Copilot** - Tool integration

**Goal:** Update tool integrations to consistent pattern

### Week 3: Gateway Feature Pages + Remaining Libraries
1. **Gateway Features** - All 6 pages (config updates)
2. **Remaining Libraries** - Autogen, Instructor, n8n, etc.

**Goal:** Complete all Group 3 & 4 migrations

---

## Key Patterns from Master Guide

### Concise "Add Provider" Pattern (Use Everywhere)

```markdown
### Add Provider

1. Go to [**Model Catalog → Add Provider**](https://app.portkey.ai/model-catalog/providers)
2. Select **[Provider Name]**
3. Choose existing credentials or create new by entering your API keys
4. Name your provider (e.g., `provider-prod`)

<Card title="Complete Setup Guide →" href="/product/model-catalog">
  See all setup options, code examples, and detailed instructions
</Card>
```

### Code Examples (Show Recommended Method Only)

```python
from portkey_ai import Portkey, PORTKEY_GATEWAY_URL, createHeaders

portkey_headers = createHeaders(
    api_key=PORTKEY_API_KEY,
    provider="@anthropic-prod"
)

# Use with library
client = SomeLibrary(
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=portkey_headers
)
```

### Backwards Compatibility Note

```markdown
<Note>
**Legacy support:** The `virtual_key` parameter still works for backwards compatibility. Use `provider="@provider-slug"` format for new code.
</Note>
```

---

## Writing Style Guidelines

From `WRITING_STYLE_GUIDE.md`:

1. **Be direct** - "Add providers" not "You can add providers"
2. **Use imperatives** - Start with action verbs
3. **Focus on actions** - Show what to do, not what's possible
4. **Keep it concise** - Every word should serve a purpose
5. **Say less, show more** - Use code examples, not long explanations
6. **Link to details** - Don't repeat everything; link to Model Catalog

**Pattern Simplifications:**
- ❌ "If you want to use Anthropic, you need to create a virtual key"
- ✅ "To use Anthropic, add a provider in Model Catalog"

- ❌ "You can switch providers by changing the virtual key parameter"
- ✅ "Switch providers by changing the `provider` parameter"

---

## Quality Checks

After migrating each page:

1. **Terminology consistent** - No "virtual key" in new instructions
2. **Concise setup** - 4 steps max, links to Model Catalog for details
3. **Code examples updated** - Use `provider="@slug"`, not `virtual_key`
4. **Config examples updated** - Use recommended format
5. **Links correct** - Point to Model Catalog or Virtual Keys (with context)
6. **Backwards compatibility** - Note added where legacy support exists
7. **Card components** - Use for Model Catalog links (visual emphasis)
8. **Writing style** - Direct, concise, action-oriented
9. **No redundancy** - Don't explain all methods; link instead

---

## Template: Library Integration Page (Updated)

```markdown
---
title: "[Library Name]"
description: "Add Portkey's enterprise features to [Library]—observability, reliability, and cost control."
---

[Brief intro: What Library does + What Portkey adds in 1-2 lines]

## Quick Start

Add Portkey with 3 parameters:

```[language]
from [library] import ChatModel

model = ChatModel(
    model="@openai-prod/gpt-4o",       # Provider slug from Model Catalog
    base_url="https://api.portkey.ai",
    api_key="PORTKEY_API_KEY"
)

response = model.invoke("Hello")
```

<Frame caption="All requests now appear in Portkey logs">
    <img src="/images/libraries/[library]-logs.gif"/>
</Frame>

That's it! You now get:
- ✅ Full observability (costs, latency, logs)
- ✅ Dynamic model selection per request
- ✅ Automatic fallbacks and retries
- ✅ Budget controls per team/project

## Why Add Portkey to [Library]?

[Library] handles [what it does]. Portkey adds production features:

<CardGroup cols={2}>
  <Card title="Enterprise Observability" icon="chart-line">
    Every request logged with costs, latency, tokens. Team-level analytics.
  </Card>
  <Card title="Dynamic Model Selection" icon="shuffle">
    Route queries to different models based on complexity or task type.
  </Card>
  <Card title="Production Reliability" icon="shield-check">
    Automatic fallbacks, retries, load balancing—configured once, works everywhere.
  </Card>
  <Card title="Cost & Access Control" icon="dollar-sign">
    Budget limits per team. Rate limiting. Centralized credential management.
  </Card>
</CardGroup>

## Setup

### 1. Install Packages

```sh
[installation commands]
```

### 2. Add Provider in Model Catalog

1. Go to [**Model Catalog → Add Provider**](https://app.portkey.ai/model-catalog/providers)
2. Select your provider (OpenAI, Anthropic, Google, etc.)
3. Choose existing credentials or create new by entering your API keys
4. Name your provider (e.g., `openai-prod`)

<Card title="Complete Model Catalog Guide →" href="/product/model-catalog">
  Set up budgets, rate limits, and manage credentials
</Card>

### 3. Get Portkey API Key

Create your Portkey API key at [app.portkey.ai/api-keys](https://app.portkey.ai/api-keys)

### 4. Use in Your Code

Replace your existing initialization:

```[language]
# Before (direct to provider)
model = ChatModel(
    model="gpt-4o",
    api_key="PROVIDER_API_KEY"
)

# After (via Portkey)
model = ChatModel(
    model="@openai-prod/gpt-4o",
    base_url="https://api.portkey.ai",
    api_key="PORTKEY_API_KEY"
)
```

**That's the only change!** All existing code works unchanged.

## Switching Between Providers

Just change the model string:

```[language]
# OpenAI
model = ChatModel(model="@openai-prod/gpt-4o", ...)

# Anthropic
model = ChatModel(model="@anthropic-prod/claude-sonnet-4", ...)

# Google
model = ChatModel(model="@google-prod/gemini-2.0-flash", ...)
```

## [Primary Use Case Section]

[If agents: Show agent example prominently]
[If RAG: Show RAG pipeline]
[If chains: Show chain example]

## Works With All [Library] Features

✅ [Feature 1] - Brief description  
✅ [Feature 2] - Brief description  
✅ [Feature 3] - Brief description

[Show 1-2 quick examples if needed]

## Dynamic Model Selection

[Show conditional routing example with practical use case]

<Card title="Conditional Routing Guide →" href="/product/ai-gateway/conditional-routing">
  Learn more about dynamic routing patterns
</Card>

## Advanced Features via Configs

For production features like fallbacks, caching, and load balancing, use Portkey Configs:

```[language]
from portkey_ai import createHeaders

model = ChatModel(
    model="@openai-prod/gpt-4o",
    base_url="https://api.portkey.ai",
    api_key="PORTKEY_API_KEY",
    default_headers=createHeaders(config="pc_your_config_id")
)
```

<Card title="Learn About Configs →" href="/product/ai-gateway/configs">
  Fallbacks, retries, caching, load balancing, and more
</Card>

## Migration from Direct [Provider]

[Show before/after with emphasis on minimal changes]

## Next Steps

<CardGroup cols={2}>
  <Card title="Model Catalog" href="/product/model-catalog">
    Set up providers and budgets
  </Card>
  <Card title="Configs" href="/product/ai-gateway/configs">
    Configure fallbacks and routing
  </Card>
  <Card title="Observability" href="/product/observability">
    Track costs and performance
  </Card>
  <Card title="Guardrails" href="/product/guardrails">
    Add PII detection and filtering
  </Card>
</CardGroup>
```

---

## Next Steps

1. **Review this plan** - Get alignment on approach
2. **Start with Langchain Python** - Establish pattern ✅ DONE
3. **Apply to Langchain JS** - Similar pattern
4. **Update other frameworks** - LlamaIndex, DSPy, etc.
5. **Update tool integrations** - Cline, Roo Code, etc.

---

## What NOT to Do (Critical Mistakes to Avoid)

Based on the Langchain migration, avoid these mistakes:

### ❌ Don't Show Patterns That Don't Work

**BAD:**
```python
# This doesn't work with Portkey's @provider/model format
model = init_chat_model(...)
response = model.invoke(
    "query",
    config={"configurable": {"model": "@openai-prod/gpt-4o"}}  # ❌ Wrong
)
```

**GOOD:**
```python
# Use Portkey's actual conditional routing
model = ChatOpenAI(
    ...,
    default_headers=createHeaders(config=config_id)
)
response = model.invoke(
    "query",
    config={"metadata": {"complexity": "simple"}}  # ✅ Correct
)
```

### ❌ Don't Have Separate Sections for Each Feature

**BAD Structure:**
- ## Fallbacks (with long config examples)
- ## Retries (with long config examples)  
- ## Caching (with long config examples)
- ## Load Balancing (with long config examples)

**GOOD Structure:**
- ## Advanced Features via Configs
  - Brief mention with link to feature pages
  - One example showing createHeaders with config
  - Focus on unique value props instead

### ❌ Don't Bury the Main Use Case

**BAD:**
- Quick Start
- Setup
- Multi-LLM Examples
- Caching
- Fallbacks
- **Agents** (buried at bottom)

**GOOD:**
- Quick Start
- Setup
- **Using with [Library] Agents/Main Feature** (prominent)
- Works With All Features
- Advanced Features via Configs

### ❌ Don't Show Setup Before Value

**BAD:**
1. Install packages
2. Add Provider in Model Catalog (sends user away immediately)
3. Get API key
4. Use in code
5. Why use Portkey? (too late)

**GOOD:**
1. Quick Start (working code immediately)
2. Why Add Portkey? (prove value)
3. Setup (now they're motivated)
4. Main use case

### ❌ Don't Use Verbose Setup Patterns

**BAD:**
> 1. Navigate to Model Catalog
> 2. Click on Integrations tab
> 3. Find your provider in the list
> 4. Click "Connect"
> 5. In the modal dialog, enter...
> 6. Click "Next Step"
> 7. On the provisioning page...

**GOOD:**
> 1. Go to Model Catalog → Add Provider
> 2. Select provider
> 3. Choose existing credentials or create new
> 4. Name your provider
> 
> <Card link>Complete Setup Guide</Card>

### ❌ Don't Duplicate Everything From Model Catalog

**BAD:**
- Explaining all three methods to use providers
- Showing all config options
- Detailed credential management
- Budget limits setup (belongs in Model Catalog docs)

**GOOD:**
- Show the simplest method (3-parameter pattern)
- Link to Model Catalog for all options
- Keep library page focused on library integration

---

## Resources

- **Master Guide:** `MASTER_MIGRATION_GUIDE.md`
- **Writing Style:** `WRITING_STYLE_GUIDE.md`
- **Reference (Provider):** `integrations/llms/anthropic.mdx` (Group 2)
- **Reference (Library):** `integrations/libraries/langchain-python.mdx` (Group 3)
- **Reference (Tool):** `integrations/libraries/cursor.mdx` (Already updated)
- **Model Catalog Page:** `/product/model-catalog`

---

## Questions to Resolve

1. **Screenshots showing "Virtual Keys" UI:** Keep as-is or add notes? (Recommend: Keep with note if needed)

2. **Langchain-specific patterns:** Should we keep the detailed sections (Multi-LLM, Caching, Reliability) or simplify? (Recommend: Simplify, link to features)

3. **Tool integrations with enterprise sections:** These are already quite detailed - keep structure or simplify? (Recommend: Keep structure, update terminology)

4. **Config examples in gateway pages:** Show all three methods or just recommended? (Recommend: Just recommended, link to Model Catalog)

