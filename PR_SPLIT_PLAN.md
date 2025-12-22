# PR Split Plan for Model Catalog Migration

## Summary

Splitting PR #597 (191 files) into **7 focused PRs** organized by:
1. **Change complexity** - How much review effort needed
2. **Content type** - What pattern to look for
3. **Risk level** - How critical to get right

---

## PR 1: Foundation & Migration Context
**Files:** 7 | **Risk:** 🟢 Low | **Review time:** ~10 min

**What changed:** New documentation files explaining the migration strategy.

**Reviewer focus:** _"Is the migration strategy sound? Are patterns documented clearly?"_

```
GROUP_2_MIGRATION_PLAN.md          (new)
GROUP_3_MIGRATION_PLAN.md          (new)
GROUP_5_MIGRATION_PLAN.md          (new)
MASTER_MIGRATION_GUIDE.md          (new)
WRITING_STYLE_GUIDE.md             (new)
docs.json                          (nav cleanup)
images/claude-icon.svg             (new asset)
```

**Merge first** - Provides context for all other PRs.

---

## PR 2: Quick Wins - Minor Terminology Updates
**Files:** 29 | **Risk:** 🟢 Low | **Review time:** ~15 min

**What changed:** Small updates (<30 lines) - terminology fixes, link updates, minor code tweaks.

**Reviewer focus:** _"Are Virtual Key → Provider terminology updates correct?"_

```
# API Reference (3 files)
api-reference/inference-api/authentication.mdx    (+4)
api-reference/sdk/c-sharp.mdx                     (+25/-21)
api-reference/sdk/node.mdx                        (+7/-10)

# Config & Changelog (2 files)
changelog/2025/apr.mdx                            (+1/-1)
enterprise/hybrid2.mdx                            (+6/-5)

# Guides - Minor fixes (6 files)
guides/getting-started/a-b-test-prompts-and-models.mdx
guides/getting-started/function-calling.mdx
guides/getting-started/return-repeat-requests-from-cache.mdx
guides/getting-started/trigger-automatic-retries-on-llm-failures.mdx
guides/ted-ai-hack-24.mdx
guides/use-cases/openai-computer-use.mdx
guides/use-cases/smart-fallback-with-model-optimized-prompts.mdx
guides/use-cases/track-costs-using-metadata.mdx

# Integrations - Minor fixes (11 files)
integrations/agents/agno-ai.mdx
integrations/agents/autogen.mdx
integrations/agents/langgraph.mdx
integrations/agents/livekit.mdx
integrations/agents/openai-swarm.mdx
integrations/agents/pydantic-ai.mdx
integrations/libraries/anthropic-computer-use.mdx
integrations/libraries/dspy.mdx

# LLM Providers - Minor fixes (7 files)
integrations/llms/azure-openai/azure-openai.mdx
integrations/llms/bedrock/aws-bedrock.mdx
integrations/llms/bedrock/batches.mdx
integrations/llms/bedrock/files.mdx
integrations/llms/bedrock/prompt-caching.mdx
integrations/llms/byollm.mdx
```

**Can rubber-stamp** - All follow same simple pattern.

---

## PR 3: LLM Provider Integrations
**Files:** 5 | **Risk:** 🟡 Medium | **Review time:** ~20 min

**What changed:** Provider setup instructions rewritten to use Model Catalog pattern.

**Reviewer focus:** _"Do all providers follow the same 'Add Provider' pattern? Are code examples using `@provider/model` format?"_

```
integrations/llms/ai21.mdx                        (+116/-75)
integrations/llms/anthropic.mdx                   (+449/-1152) ⚠️ Major rewrite
integrations/llms/anyscale-llama2-mistral-zephyr.mdx (+115/-314)
integrations/llms/aws-sagemaker.mdx               (+149/-143)
integrations/llms/azure-foundry.mdx               (+225/-227)
```

**Pattern to verify:**
- [ ] "Add Provider" section uses 4-step flow
- [ ] Code examples use `model="@provider-slug/model-name"`
- [ ] Links point to `/product/model-catalog`

---

## PR 4: AI Tools & Apps (Cursor, Cline, Claude Code, etc.)
**Files:** 24 | **Risk:** 🟡 Medium | **Review time:** ~30 min

**What changed:** Setup instructions for AI coding tools updated to Model Catalog.

**Reviewer focus:** _"Are setup steps consistent across all AI tools? Do base URLs and configs match?"_

```
# AI Coding Tools (Major rewrites)
integrations/libraries/cursor.mdx                 (+107/-341)
integrations/libraries/cline.mdx                  (+141/-334)
integrations/libraries/claude-code.mdx            (+125/-236)
integrations/libraries/codex.mdx                  (+131/-282)
integrations/libraries/github-copilot.mdx         (+105/-207)
integrations/libraries/goose.mdx                  (+134/-296)
integrations/libraries/roo-code.mdx               (+143/-298)
integrations/libraries/zed.mdx                    (+150/-284)

# AI Platforms
integrations/libraries/anythingllm.mdx            (+135/-278)
integrations/libraries/janhq.mdx                  (+130/-279)
integrations/libraries/librechat.mdx              (+100/-292)
integrations/libraries/openwebui.mdx              (+159/-457)

# Low-code/No-code
integrations/libraries/langflow.mdx               (+110/-333)
integrations/libraries/n8n.mdx                    (+105/-337)
integrations/libraries/tooljet.mdx                (+84/-250)

# Databases & Testing
integrations/libraries/mindsdb.mdx                (+47/-40)
integrations/libraries/mongodb.mdx                (+34/-32)
integrations/libraries/supabase.mdx               (+55/-51)
integrations/libraries/promptfoo.mdx              (+67/-160)

# Other
integrations/libraries/instructor.mdx             (+107/-133)
integrations/libraries/openai-compatible.mdx      (+189/-354)
integrations/libraries/openai-agent-builder.mdx   (+158/-693)
integrations/libraries/openai-agent-builder-python.mdx (+152/-689)
```

**Pattern to verify:**
- [ ] Base URL consistently `https://api.portkey.ai/v1`
- [ ] Provider setup uses Model Catalog flow
- [ ] Headers include `x-portkey-api-key`

---

## PR 5: Framework Integrations (LangChain, LlamaIndex, Vercel)
**Files:** 4 | **Risk:** 🟠 Higher | **Review time:** ~25 min

**What changed:** Core framework integrations - these are heavily used, code examples critical.

**Reviewer focus:** _"Are code examples correct and tested? Do imports match current SDK versions?"_

```
integrations/libraries/langchain-python.mdx       (+371/-275) ⚠️ Heavy use
integrations/libraries/langchain-js.mdx           (+377/-181) ⚠️ Heavy use
integrations/libraries/llama-index-python.mdx     (+273/-714) ⚠️ Heavy use
integrations/libraries/vercel.mdx                 (+171/-187)
```

**Pattern to verify:**
- [ ] Import statements are correct
- [ ] Portkey initialization matches current SDK
- [ ] All code examples are runnable
- [ ] Provider slug format `@provider/model` used correctly

---

## PR 6: Agent Frameworks
**Files:** 10 | **Risk:** 🟡 Medium | **Review time:** ~25 min

**What changed:** Agent framework integrations (CrewAI, Strands, OpenAI Agents, etc.)

**Reviewer focus:** _"Are multi-agent patterns documented correctly? Do tracing examples work?"_

```
# Major rewrites
integrations/agents/openai-agents.mdx             (+284/-997) ⚠️ Major
integrations/agents/openai-agents-ts.mdx          (+244/-741) ⚠️ Major
integrations/agents/crewai.mdx                    (+145/-632)
integrations/agents/strands.mdx                   (+150/-506)
integrations/agents/llama-agents.mdx              (+92/-190)
integrations/agents/langchain-agents.mdx          (+105/-166)

# Medium changes
integrations/agents/bring-your-own-agents.mdx     (+84/-132)
integrations/agents/control-flow.mdx              (+79/-135)
integrations/agents/phidata.mdx                   (+81/-126)

# Cleanup
integrations/agents/strands-backup.mdx            (deleted)
```

**Pattern to verify:**
- [ ] Agent initialization uses Portkey client correctly
- [ ] Tracing/observability setup is documented
- [ ] Multi-provider configs use new format

---

## PR 7: Guides & Tutorials
**Files:** 21 | **Risk:** 🟡 Medium | **Review time:** ~30 min

**What changed:** Step-by-step guides and tutorials updated for Model Catalog flow.

**Reviewer focus:** _"Does the user journey make sense? Are screenshots/examples current?"_

```
# Getting Started (Major)
guides/getting-started/getting-started-with-ai-gateway.mdx (+584/-998) ⚠️ Core guide
guides/getting-started/101-on-portkey-s-gateway-configs.mdx (+40/-99)
guides/getting-started/image-generation.mdx        (+34/-112)
guides/getting-started/llama-3-on-groq.mdx         (+27/-67)
guides/getting-started/tackling-rate-limiting.mdx  (+25/-49)

# Integration Guides
guides/integrations/groq.mdx                       (+40/-193)
guides/integrations/vercel-ai.mdx                  (+50/-163)
guides/integrations/arize-portkey.mdx              (+31/-46)
guides/integrations/langchain.mdx                  (+32/-64)
guides/integrations/llama-3-on-portkey-+-together-ai.mdx (+9/-33)
guides/integrations/mixtral-8x22b.mdx              (+19/-79)

# Use Cases
guides/use-cases/setup-openai-greater-than-azure-openai-fallback.mdx (+47/-159)
guides/use-cases/build-an-article-suggestion-app-with-supabase-pgvector-and-portkey.mdx
guides/use-cases/comparing-top10-lmsys-models-with-portkey.mdx
guides/use-cases/deepseek-r1.mdx
guides/use-cases/enforcing-json-schema-with-anyscale-and-together.mdx
guides/use-cases/fallback-from-sdxl-to-dall-e-3.mdx
guides/use-cases/few-shot-prompting.mdx
guides/use-cases/how-to-use-openai-sdk-with-portkey-prompt-templates.mdx
guides/use-cases/librechat-web-search.mdx
guides/use-cases/run-portkey-on-prompts-from-langchain-hub.mdx

# Prompts
guides/prompts/build-a-chatbot-using-portkeys-prompt-templates.mdx
guides/prompts/llama-prompts.mdx
```

**Pattern to verify:**
- [ ] Step numbers match actual UI
- [ ] Code snippets use new `@provider/model` format
- [ ] Links to Model Catalog are correct

---

## Recommended Merge Order

```
1. PR 1: Foundation        → Sets context, no risk
2. PR 2: Quick Wins        → Builds momentum, easy reviews
3. PR 3: LLM Providers     → Core functionality
4. PR 5: Frameworks        → High-traffic pages (review carefully!)
5. PR 4: AI Tools          → Broad but consistent pattern
6. PR 6: Agents            → Growing adoption
7. PR 7: Guides            → Can iterate post-merge
```

---

## Creating the PRs

### Option A: Cherry-pick from current branch

```bash
# For each PR, create a branch and cherry-pick relevant files
git checkout main
git pull origin main
git checkout -b migration/01-foundation

# Copy specific files from the migration branch
git checkout modal-catalog-migration -- \
  GROUP_2_MIGRATION_PLAN.md \
  GROUP_3_MIGRATION_PLAN.md \
  GROUP_5_MIGRATION_PLAN.md \
  MASTER_MIGRATION_GUIDE.md \
  WRITING_STYLE_GUIDE.md \
  docs.json \
  images/claude-icon.svg

git add -A
git commit -m "docs: Add Model Catalog migration foundation"
gh pr create --title "Model Catalog Migration 1/7: Foundation" --body "..."
```

### Option B: Use git subtree split (if commits are organized)

If your commits are already organized by group (which they appear to be from git log), you can create PRs by commit ranges.

---

## PR Description Template

Use this template for each PR:

```markdown
## Model Catalog Migration - [Category Name]

### What's changing
[Brief description of the changes in this PR]

### Files changed
- X files in `[directory]`
- Change type: [terminology updates / code examples / full rewrite]

### Review checklist
- [ ] "Add Provider" sections follow 4-step pattern
- [ ] Code examples use `@provider-slug/model-name` format
- [ ] Links point to `/product/model-catalog`
- [ ] Backwards compatibility note included where `virtual_key` still works

### Testing
- [ ] Verified links work
- [ ] Code examples are syntactically correct

### Part of
Model Catalog Migration (#597) - Split for easier review
```

---

## Questions?

- **Why 7 PRs?** Balance between review overhead and focus. Each PR is ~15-30 min review.
- **Can we merge out of order?** PRs 2-7 can merge in any order after PR 1.
- **What about conflicts?** Each PR touches different files, so conflicts are unlikely.
