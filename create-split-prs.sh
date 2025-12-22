#!/bin/bash
# Script to split PR #597 into 7 smaller, focused PRs
# Run from the repo root directory

set -e

SOURCE_BRANCH="modal-catalog-migration"
BASE_BRANCH="main"

echo "🚀 Model Catalog Migration - PR Split Script"
echo "============================================"
echo ""

# Ensure we're on the right branch and up to date
git fetch origin

# PR 1: Foundation & Migration Context
create_pr_1() {
    echo "📦 Creating PR 1: Foundation & Migration Context..."
    git checkout $BASE_BRANCH
    git pull origin $BASE_BRANCH
    git checkout -b migration/01-foundation
    
    git checkout $SOURCE_BRANCH -- \
        GROUP_2_MIGRATION_PLAN.md \
        GROUP_3_MIGRATION_PLAN.md \
        GROUP_5_MIGRATION_PLAN.md \
        MASTER_MIGRATION_GUIDE.md \
        WRITING_STYLE_GUIDE.md \
        docs.json \
        images/claude-icon.svg 2>/dev/null || true
    
    git add -A
    git commit -m "docs: Add Model Catalog migration foundation and context"
    git push -u origin migration/01-foundation
    
    gh pr create \
        --title "Model Catalog Migration 1/7: Foundation & Context" \
        --body "$(cat <<'EOF'
## Model Catalog Migration - Foundation

### What's changing
New documentation files explaining the migration strategy from Virtual Keys to Model Catalog.

### Files changed (7)
- `MASTER_MIGRATION_GUIDE.md` - Complete migration guide
- `GROUP_*_MIGRATION_PLAN.md` - Detailed plans per group
- `WRITING_STYLE_GUIDE.md` - Documentation standards
- `docs.json` - Navigation cleanup
- `images/claude-icon.svg` - New asset

### Review checklist
- [ ] Migration strategy is sound
- [ ] Patterns are documented clearly
- [ ] Navigation structure makes sense

### Risk: 🟢 Low
New files only, no breaking changes.

### Part of
Model Catalog Migration - Split from #597 for easier review
EOF
)"
    echo "✅ PR 1 created"
}

# PR 2: Quick Wins - Minor Changes
create_pr_2() {
    echo "📦 Creating PR 2: Quick Wins - Minor Changes..."
    git checkout $BASE_BRANCH
    git pull origin $BASE_BRANCH
    git checkout -b migration/02-quick-wins
    
    git checkout $SOURCE_BRANCH -- \
        api-reference/inference-api/authentication.mdx \
        api-reference/sdk/c-sharp.mdx \
        api-reference/sdk/node.mdx \
        changelog/2025/apr.mdx \
        enterprise/hybrid2.mdx \
        guides/getting-started/a-b-test-prompts-and-models.mdx \
        guides/getting-started/function-calling.mdx \
        guides/getting-started/return-repeat-requests-from-cache.mdx \
        guides/getting-started/trigger-automatic-retries-on-llm-failures.mdx \
        guides/ted-ai-hack-24.mdx \
        guides/use-cases/openai-computer-use.mdx \
        guides/use-cases/smart-fallback-with-model-optimized-prompts.mdx \
        guides/use-cases/track-costs-using-metadata.mdx \
        integrations/agents/agno-ai.mdx \
        integrations/agents/autogen.mdx \
        integrations/agents/langgraph.mdx \
        integrations/agents/livekit.mdx \
        integrations/agents/openai-swarm.mdx \
        integrations/agents/pydantic-ai.mdx \
        integrations/libraries/anthropic-computer-use.mdx \
        integrations/libraries/dspy.mdx \
        integrations/llms/azure-openai/azure-openai.mdx \
        integrations/llms/bedrock/aws-bedrock.mdx \
        integrations/llms/bedrock/batches.mdx \
        integrations/llms/bedrock/files.mdx \
        integrations/llms/bedrock/prompt-caching.mdx \
        integrations/llms/byollm.mdx 2>/dev/null || true
    
    git add -A
    git commit -m "docs: Minor terminology updates for Model Catalog migration"
    git push -u origin migration/02-quick-wins
    
    gh pr create \
        --title "Model Catalog Migration 2/7: Quick Wins - Minor Updates" \
        --body "$(cat <<'EOF'
## Model Catalog Migration - Quick Wins

### What's changing
Small terminology updates (<30 lines each) - Virtual Key → Provider references, link fixes.

### Files changed (27)
- API Reference: 3 files
- Guides: 8 files  
- Integrations: 16 files

### Review checklist
- [ ] Terminology updates are consistent
- [ ] Links point to correct pages
- [ ] No functionality changes

### Risk: 🟢 Low
Minor text changes only.

### Part of
Model Catalog Migration - Split from #597 for easier review
EOF
)"
    echo "✅ PR 2 created"
}

# PR 3: LLM Provider Integrations
create_pr_3() {
    echo "📦 Creating PR 3: LLM Provider Integrations..."
    git checkout $BASE_BRANCH
    git pull origin $BASE_BRANCH
    git checkout -b migration/03-llm-providers
    
    git checkout $SOURCE_BRANCH -- \
        integrations/llms/ai21.mdx \
        integrations/llms/anthropic.mdx \
        integrations/llms/anyscale-llama2-mistral-zephyr.mdx \
        integrations/llms/aws-sagemaker.mdx \
        integrations/llms/azure-foundry.mdx 2>/dev/null || true
    
    git add -A
    git commit -m "docs: Update LLM provider integrations for Model Catalog"
    git push -u origin migration/03-llm-providers
    
    gh pr create \
        --title "Model Catalog Migration 3/7: LLM Provider Integrations" \
        --body "$(cat <<'EOF'
## Model Catalog Migration - LLM Providers

### What's changing
Provider setup instructions rewritten to use Model Catalog pattern.

### Files changed (5)
- `integrations/llms/anthropic.mdx` - Major rewrite
- `integrations/llms/ai21.mdx`
- `integrations/llms/anyscale-llama2-mistral-zephyr.mdx`
- `integrations/llms/aws-sagemaker.mdx`
- `integrations/llms/azure-foundry.mdx`

### Review checklist
- [ ] "Add Provider" section uses 4-step flow
- [ ] Code examples use `model="@provider-slug/model-name"`
- [ ] Links point to `/product/model-catalog`
- [ ] Backwards compatibility note for `virtual_key`

### Risk: 🟡 Medium
Core provider pages - heavily referenced.

### Part of
Model Catalog Migration - Split from #597 for easier review
EOF
)"
    echo "✅ PR 3 created"
}

# PR 4: AI Tools & Apps
create_pr_4() {
    echo "📦 Creating PR 4: AI Tools & Apps..."
    git checkout $BASE_BRANCH
    git pull origin $BASE_BRANCH
    git checkout -b migration/04-ai-tools
    
    git checkout $SOURCE_BRANCH -- \
        integrations/libraries/cursor.mdx \
        integrations/libraries/cline.mdx \
        integrations/libraries/claude-code.mdx \
        integrations/libraries/codex.mdx \
        integrations/libraries/github-copilot.mdx \
        integrations/libraries/goose.mdx \
        integrations/libraries/roo-code.mdx \
        integrations/libraries/zed.mdx \
        integrations/libraries/anythingllm.mdx \
        integrations/libraries/janhq.mdx \
        integrations/libraries/librechat.mdx \
        integrations/libraries/openwebui.mdx \
        integrations/libraries/langflow.mdx \
        integrations/libraries/n8n.mdx \
        integrations/libraries/tooljet.mdx \
        integrations/libraries/mindsdb.mdx \
        integrations/libraries/mongodb.mdx \
        integrations/libraries/supabase.mdx \
        integrations/libraries/promptfoo.mdx \
        integrations/libraries/instructor.mdx \
        integrations/libraries/openai-compatible.mdx \
        integrations/libraries/openai-agent-builder.mdx \
        integrations/libraries/openai-agent-builder-python.mdx 2>/dev/null || true
    
    git add -A
    git commit -m "docs: Update AI tools integrations for Model Catalog"
    git push -u origin migration/04-ai-tools
    
    gh pr create \
        --title "Model Catalog Migration 4/7: AI Tools & Apps" \
        --body "$(cat <<'EOF'
## Model Catalog Migration - AI Tools & Apps

### What's changing
Setup instructions for AI coding tools and platforms updated to Model Catalog.

### Files changed (23)
**AI Coding Tools:** Cursor, Cline, Claude Code, Codex, GitHub Copilot, Goose, Roo Code, Zed
**AI Platforms:** AnythingLLM, Jan, LibreChat, Open WebUI
**Low-code:** Langflow, n8n, ToolJet
**Other:** MindsDB, MongoDB, Supabase, Promptfoo, Instructor

### Review checklist
- [ ] Base URL consistently `https://api.portkey.ai/v1`
- [ ] Provider setup uses Model Catalog flow
- [ ] Headers include `x-portkey-api-key`
- [ ] Setup steps are consistent across tools

### Risk: 🟡 Medium
Popular tools - users follow these guides closely.

### Part of
Model Catalog Migration - Split from #597 for easier review
EOF
)"
    echo "✅ PR 4 created"
}

# PR 5: Framework Integrations
create_pr_5() {
    echo "📦 Creating PR 5: Framework Integrations..."
    git checkout $BASE_BRANCH
    git pull origin $BASE_BRANCH
    git checkout -b migration/05-frameworks
    
    git checkout $SOURCE_BRANCH -- \
        integrations/libraries/langchain-python.mdx \
        integrations/libraries/langchain-js.mdx \
        integrations/libraries/llama-index-python.mdx \
        integrations/libraries/vercel.mdx 2>/dev/null || true
    
    git add -A
    git commit -m "docs: Update framework integrations for Model Catalog"
    git push -u origin migration/05-frameworks
    
    gh pr create \
        --title "Model Catalog Migration 5/7: Framework Integrations ⚠️" \
        --body "$(cat <<'EOF'
## Model Catalog Migration - Framework Integrations

### ⚠️ HIGH TRAFFIC PAGES - Review Carefully

### What's changing
Core framework integrations updated - these pages get heavy traffic.

### Files changed (4)
- `integrations/libraries/langchain-python.mdx` (+371/-275)
- `integrations/libraries/langchain-js.mdx` (+377/-181)
- `integrations/libraries/llama-index-python.mdx` (+273/-714)
- `integrations/libraries/vercel.mdx` (+171/-187)

### Review checklist
- [ ] Import statements are correct
- [ ] Portkey initialization matches current SDK
- [ ] All code examples are syntactically correct
- [ ] Provider slug format `@provider/model` used correctly
- [ ] Examples can be copy-pasted and run

### Risk: 🟠 Higher
Most referenced integration pages - code must be correct.

### Part of
Model Catalog Migration - Split from #597 for easier review
EOF
)"
    echo "✅ PR 5 created"
}

# PR 6: Agent Frameworks
create_pr_6() {
    echo "📦 Creating PR 6: Agent Frameworks..."
    git checkout $BASE_BRANCH
    git pull origin $BASE_BRANCH
    git checkout -b migration/06-agents
    
    git checkout $SOURCE_BRANCH -- \
        integrations/agents/openai-agents.mdx \
        integrations/agents/openai-agents-ts.mdx \
        integrations/agents/crewai.mdx \
        integrations/agents/strands.mdx \
        integrations/agents/llama-agents.mdx \
        integrations/agents/langchain-agents.mdx \
        integrations/agents/bring-your-own-agents.mdx \
        integrations/agents/control-flow.mdx \
        integrations/agents/phidata.mdx 2>/dev/null || true
    
    # Handle file deletion
    git rm integrations/agents/strands-backup.mdx 2>/dev/null || true
    
    git add -A
    git commit -m "docs: Update agent framework integrations for Model Catalog"
    git push -u origin migration/06-agents
    
    gh pr create \
        --title "Model Catalog Migration 6/7: Agent Frameworks" \
        --body "$(cat <<'EOF'
## Model Catalog Migration - Agent Frameworks

### What's changing
Agent framework integrations (CrewAI, Strands, OpenAI Agents, etc.) updated.

### Files changed (10)
**Major rewrites:**
- `openai-agents.mdx` (+284/-997)
- `openai-agents-ts.mdx` (+244/-741)
- `crewai.mdx` (+145/-632)
- `strands.mdx` (+150/-506)

**Medium changes:**
- `llama-agents.mdx`, `langchain-agents.mdx`
- `bring-your-own-agents.mdx`, `control-flow.mdx`, `phidata.mdx`

**Deleted:**
- `strands-backup.mdx` (cleanup)

### Review checklist
- [ ] Agent initialization uses Portkey client correctly
- [ ] Tracing/observability setup is documented
- [ ] Multi-provider configs use new format
- [ ] Handoff patterns documented correctly

### Risk: 🟡 Medium
Growing adoption area - important to get right.

### Part of
Model Catalog Migration - Split from #597 for easier review
EOF
)"
    echo "✅ PR 6 created"
}

# PR 7: Guides & Tutorials
create_pr_7() {
    echo "📦 Creating PR 7: Guides & Tutorials..."
    git checkout $BASE_BRANCH
    git pull origin $BASE_BRANCH
    git checkout -b migration/07-guides
    
    git checkout $SOURCE_BRANCH -- \
        api-reference/inference-api/config-object.mdx \
        guides/getting-started/getting-started-with-ai-gateway.mdx \
        guides/getting-started/101-on-portkey-s-gateway-configs.mdx \
        guides/getting-started/image-generation.mdx \
        guides/getting-started/llama-3-on-groq.mdx \
        guides/getting-started/tackling-rate-limiting.mdx \
        guides/integrations/groq.mdx \
        guides/integrations/vercel-ai.mdx \
        guides/integrations/arize-portkey.mdx \
        guides/integrations/langchain.mdx \
        guides/integrations/llama-3-on-portkey-+-together-ai.mdx \
        guides/integrations/mixtral-8x22b.mdx \
        guides/use-cases/setup-openai-greater-than-azure-openai-fallback.mdx \
        guides/use-cases/build-an-article-suggestion-app-with-supabase-pgvector-and-portkey.mdx \
        guides/use-cases/comparing-top10-lmsys-models-with-portkey.mdx \
        guides/use-cases/deepseek-r1.mdx \
        guides/use-cases/enforcing-json-schema-with-anyscale-and-together.mdx \
        guides/use-cases/fallback-from-sdxl-to-dall-e-3.mdx \
        guides/use-cases/few-shot-prompting.mdx \
        guides/use-cases/how-to-use-openai-sdk-with-portkey-prompt-templates.mdx \
        guides/use-cases/librechat-web-search.mdx \
        guides/use-cases/run-portkey-on-prompts-from-langchain-hub.mdx \
        guides/prompts/build-a-chatbot-using-portkeys-prompt-templates.mdx \
        guides/prompts/llama-prompts.mdx 2>/dev/null || true
    
    git add -A
    git commit -m "docs: Update guides and tutorials for Model Catalog"
    git push -u origin migration/07-guides
    
    gh pr create \
        --title "Model Catalog Migration 7/7: Guides & Tutorials" \
        --body "$(cat <<'EOF'
## Model Catalog Migration - Guides & Tutorials

### What's changing
Step-by-step guides and tutorials updated for Model Catalog flow.

### Files changed (24)
**Getting Started (Major):**
- `getting-started-with-ai-gateway.mdx` (+584/-998) - Core onboarding guide
- `101-on-portkey-s-gateway-configs.mdx`
- `image-generation.mdx`, `llama-3-on-groq.mdx`, `tackling-rate-limiting.mdx`

**Integration Guides:**
- `groq.mdx`, `vercel-ai.mdx`, `arize-portkey.mdx`, `langchain.mdx`
- `llama-3-on-portkey-+-together-ai.mdx`, `mixtral-8x22b.mdx`

**Use Cases:** 10 files
**Prompts:** 2 files
**API Reference:** `config-object.mdx`

### Review checklist
- [ ] Step numbers match actual UI flow
- [ ] Code snippets use new `@provider/model` format
- [ ] Links to Model Catalog are correct
- [ ] Screenshots/examples are current

### Risk: 🟡 Medium
User-facing tutorials - important for onboarding.

### Part of
Model Catalog Migration - Split from #597 for easier review
EOF
)"
    echo "✅ PR 7 created"
}

# Main execution
echo "Which PR would you like to create?"
echo "1) Foundation & Context"
echo "2) Quick Wins"
echo "3) LLM Providers"
echo "4) AI Tools & Apps"
echo "5) Frameworks"
echo "6) Agents"
echo "7) Guides"
echo "a) All PRs"
echo ""
read -p "Enter choice (1-7 or a): " choice

case $choice in
    1) create_pr_1 ;;
    2) create_pr_2 ;;
    3) create_pr_3 ;;
    4) create_pr_4 ;;
    5) create_pr_5 ;;
    6) create_pr_6 ;;
    7) create_pr_7 ;;
    a)
        create_pr_1
        create_pr_2
        create_pr_3
        create_pr_4
        create_pr_5
        create_pr_6
        create_pr_7
        ;;
    *) echo "Invalid choice" ;;
esac

echo ""
echo "🎉 Done! Check your PRs at: https://github.com/Portkey-AI/docs-core/pulls"
