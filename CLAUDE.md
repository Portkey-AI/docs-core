# Portkey Docs Repository

This repository contains the documentation for [Portkey AI](https://portkey.ai), hosted at https://portkey.ai/docs. Built using [Mintlify](https://mintlify.com).

## Quick Start

```bash
npm install -g mint
mint dev
```

## Repository Structure

### Configuration

- **`docs.json`** - Main Mintlify configuration file. Defines the entire docs layout including navigation, tabs, groups, and page hierarchy. This is the source of truth for the documentation structure.
- **`package.json`** - Node.js dependencies for local development

### Main Documentation Folders

#### `/introduction/`
Getting started content:
- `what-is-portkey.mdx` - Overview of Portkey
- `make-your-first-request.mdx` - Quick start guide
- `feature-overview.mdx` - Feature summary

#### `/product/`
Core product documentation organized by feature:
- **`/observability/`** - Logs, traces, analytics, feedback, metadata, OpenTelemetry
- **`/ai-gateway/`** - Universal API, configs, caching, fallbacks, retries, load balancing, multimodal capabilities
- **`/model-catalog/`** - Model integrations, budget limits, rate limits, workspace/model provisioning
- **`/mcp-gateway/`** - MCP Gateway quickstart, architecture, deployment, hub
- **`/prompt-engineering-studio/`** - Prompt playground, library, versioning, API
- **`/guardrails/`** - Guardrail checks, PII redaction, embedding guardrails
- **`/administration/`** - Org-level configurations, enforcing metadata, guardrails, budgets
- **`/enterprise-offering/`** - Org management, SSO, SCIM, access control, KMS, audit logs, OTel

#### `/integrations/`
Third-party integrations:
- **`/llms/`** - LLM provider integrations (OpenAI, Anthropic, Gemini, Vertex AI, Azure, Bedrock, Ollama, 50+ more)
- **`/agents/`** - Agent framework integrations (OpenAI Agents, Claude Agent SDK, LangChain, CrewAI, AutoGen, etc.)
- **`/libraries/`** - Library integrations (Cursor, Claude Code, Cline, LangChain, etc.)
- **`/guardrails/`** - Guardrail provider integrations (Aporia, Bedrock Guardrails, etc.)
- **`/tracing-providers/`** - Observability integrations (Langfuse, Arize, Phoenix, etc.)
- **`/mcp-clients/`** - MCP client integrations (Claude, Cursor, VS Code)
- **`/mcp-servers/`** - MCP server integrations (GitHub, Notion, Playwright, etc.)
- **`/vector-databases/`** - Vector DB integrations (Milvus, Qdrant)
- **`/cloud/`** - Cloud platform integrations
- **`/plugins/`** - Plugin integrations

#### `/api-reference/`
API documentation:
- **`/inference-api/`** - Gateway API reference (chat, completions, embeddings, images, audio, files, batches, fine-tuning, assistants)
- **`/admin-api/`** - Admin API reference
  - `/control-plane/` - Configs, integrations, virtual keys, prompts, API keys, analytics
  - `/data-plane/` - Logs, feedback
- **`/sdk/`** - SDK documentation (Python, Node.js, C#)

#### `/guides/`
How-to guides and tutorials:
- **`/getting-started/`** - Onboarding guides
- **`/integrations/`** - Integration-specific guides
- **`/prompts/`** - Prompt engineering guides
- **`/use-cases/`** - Use case implementations
- **`/whitepapers/`** - In-depth technical documents

#### `/self-hosting/`
Self-hosting documentation:
- **`/hybrid-deployments/`** - AWS (EKS, Marketplace), GCP, Azure deployment guides
- `prometheus-metrics.mdx` - Metrics configuration

#### `/enterprise/`
Enterprise-specific documentation (pricing, security, support, POC info)

#### `/changelog/`
Release notes and updates:
- **`/2024/`**, **`/2025/`** - Yearly changelogs
- SDK changelogs (`python-sdk-changelog.mdx`, `node-sdk-changelog.mdx`)
- Component changelogs (backend, frontend, helm-chart, etc.)

#### `/support/`
Help and support pages:
- Common errors and resolutions
- Migration guides
- Contact information

### Assets

#### `/images/`
Image assets organized by documentation section:
- `/product/` - Product screenshots
- `/llms/` - LLM provider logos
- `/integrations/` - Integration screenshots
- `/guides/` - Guide illustrations
- etc.

#### `/snippets/`
Reusable MDX snippets for documentation

### Other Files

- **`README.mdx`** - Contributing guide (also rendered in docs)
- **`/virtual_key_old/`** - Deprecated/archived content (legacy virtual keys docs)
- **`/.github/workflows/`** - CI/CD workflows

## Documentation Tabs

The docs are organized into these main tabs (defined in `docs.json`):

1. **Docs** - Main documentation (Introduction, Product, Self-Hosting, Support)
2. **Integrations** - All third-party integrations
3. **Gateway APIs** - Inference API reference
4. **Admin APIs** - Admin/Control plane API reference

## Adding New Pages

1. Create an `.mdx` file in the appropriate folder
2. Add frontmatter with `title` and optional `description`
3. Add the page path to `docs.json` in the correct navigation group
4. Run `mint dev` to preview

## File Naming Conventions

- Use kebab-case for file names: `my-new-page.mdx`
- Index pages for sections are named after the section: `observability.mdx` (not `index.mdx`)
- Sub-features go in folders: `/observability/logs.mdx`

## Common Patterns

- Provider-specific docs follow: `/integrations/llms/{provider}.mdx`
- Sub-features are nested: `/integrations/llms/openai/files.mdx`
- API endpoints follow OpenAPI structure in `/api-reference/`
