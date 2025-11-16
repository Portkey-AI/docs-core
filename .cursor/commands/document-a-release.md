# document-a-release

This is a systematic workflow for updating documentation when a new Gateway Enterprise Node release is published. It is a playbook that guides you through the process of updating documentation for a new release.

## Prerequisites

- Gateway Enterprise Node repository cloned locally at `~/workspace/gateway-enterprise-node`
- Documentation repository at `~/workspace/docs-core`
- Access to the git history of both repositories
- Clean working directory in docs-core (no uncommitted changes)

---

## Step 0: Confirm Release Version

**⚠️ IMPORTANT: Never assume the release version!**

**If the user has NOT specified a release version:**
- Ask: "Which release version would you like to run this workflow for?"
- Wait for confirmation before proceeding

**If the user HAS specified a version:**
- Confirm: "Running documentation update workflow for version X.X.X"
- Proceed with the workflow

**Optional: List available recent releases (if user is unsure):**
```bash
cd ~/workspace/gateway-enterprise-node
git fetch --tags
git tag --sort=-creatordate | head -10
```

---

## Step 1: Create Documentation Branch

**⚠️ CRITICAL: Always work in a separate branch!**

### Create a new branch in docs-core:
```bash
cd ~/workspace/docs-core

# Ensure you're on the latest main/master
git checkout main
git pull origin main

# Create a new branch for this release
git checkout -b docs/gateway-node-v<VERSION>
# Example: git checkout -b docs/gateway-node-v1.16.7
```

### Branch naming convention:
- Format: `docs/gateway-node-v<VERSION>`
- Examples:
  - `docs/gateway-node-v1.16.7`
  - `docs/gateway-node-v2.0.0`

**Action:** Confirm branch created and checked out

---

## Step 2: Extract Release Changes

Using the version specified in Step 0 (e.g., `v1.16.7`):

### Determine the previous version:
```bash
# Find the tag before the current release
cd ~/workspace/gateway-enterprise-node
git tag --sort=-creatordate | grep -A1 "v1.16.7" | tail -1
# This will show v1.16.6 (the previous version)
```

### Get commits in the release:
```bash
# Replace with your current and previous versions
git log v1.16.6..v1.16.7 --pretty=format:"%H %s"
```

### Identify PRs included:
```bash
git log v1.16.6..v1.16.7 --pretty=format:"%H %s" --merges
```

**Action:** List all PR numbers and their titles

---

## Step 3: Analyze Each PR

For each PR identified:

### View PR details:
```bash
git show <commit-hash> --stat
```

### View full code changes:
```bash
git show <commit-hash>
```

### Web search for context:
For PRs involving new providers, services, or API version changes:

```
# New provider/integration
Search: "<PROVIDER_NAME> API documentation models endpoints"
Search: "<PROVIDER_NAME> authentication methods"

# API version changes
Search: "<API_NAME> v2 changes migration guide"
Search: "<API_NAME> v2 new features vs v1"

# Standards support
Search: "<STANDARD_NAME> semantic conventions specification"
```

**When to search:**
- New provider integrations → Search for models, auth methods, features
- API version migrations → Search for what's new in the version
- Standards implementation → Search for the standard specification

### Document the PR:
Create a brief summary including:
- **PR Number & Title**
- **What Changed:** Technical description
- **Files Modified:** List of changed files
- **User Impact:** Does this affect user-facing behavior?
- **Web Research:** Key findings from searches (if applicable)

---

## Step 4: Determine Documentation Impact

For each PR, ask:

### ✅ **Requires Documentation Update** if:
- New features or capabilities added
- New supported formats, models, or providers
- Changed API parameters or behavior
- New configuration options
- Updated authentication methods
- Modified user-facing error messages
- **Changes to pricing/cost calculation logic** 🔥
- **Changes to observability data structures** 🔥
- **Support for industry standards** (OAuth, OIDC, OpenTelemetry semantics) 🔥
- **Changes to telemetry attributes** (logs, traces, metrics) 🔥

### ❌ **No Documentation Update** if:
- Internal refactoring with no user-facing changes
- Bug fixes that restore documented behavior
- Performance improvements (unless they change user-visible metrics)
- Internal caching/optimization changes
- Code cleanup or type updates
- Internal error handling improvements

### ⚠️ **CRITICAL: Don't Dismiss Too Quickly**

**Red Flags** - Always investigate deeply even if PR seems "internal":
- Words like: `pricing`, `cost`, `token`, `analytics`, `semantic`, `conventions`, `attribution`
- Changes to files with: `telemetry`, `metrics`, `openTelemetry`, `pricing`, `cost`
- PR titles with: `trace`, `span`, `observability`, `otel`

**Rule**: If a PR touches user-facing APIs, data structures, or adds standards support → Read the full code changes before deciding.

### 🤔 **Ask User When Unclear**

**If you encounter ambiguous cases, ask the user instead of making assumptions:**
- Infrastructure/deployment features (CORS, proxy, environment variables) - are these documented or internal-only?
- Parameter/feature location - if unsure which endpoint/API it belongs to, ask
- Documentation scope - if unclear whether a changelog item needs documentation, ask

**Action:** Create a decision matrix for each PR

---

## Step 5: Search for Affected Documentation

For PRs requiring updates, identify relevant docs:

### Search by topic:
```
# Use codebase search for semantic understanding
Query: "<feature/provider name> <capability> documentation"
Example: "Vertex AI audio formats supported"
```

### Search by file pattern:
```
# Find provider-specific docs
Pattern: **/<provider-name>*.mdx
Example: **/vertex*.mdx, **/azure*.mdx
```

### Search for specific terms:
```
# Use grep for exact matches
Pattern: "audio format", "supported formats", etc.
```

### Common documentation locations:
- `/integrations/llms/<provider>/` - Provider-specific guides
- `/product/ai-gateway/multimodal-capabilities/` - Feature-specific docs
- `/api-reference/` - API documentation
- `/changelog/` - Release notes

**Action:** List all potentially affected documentation files

---

## Step 6: Review and Update Documentation

### For each documentation file:

1. **Read the current content**
   - Understand the existing documentation structure
   - Identify sections that need updates

2. **Verify accuracy**
   - Cross-reference with code changes
   - Ensure consistency across related docs
   - Check for related docs that might also need updates
   - **Verify parameter/feature location**: Ensure parameters/features are documented under the correct endpoint/API (e.g., `conversation` and `modalities` belong to `/responses` endpoint, not `/chat/completions`)

3. **Update content**
   - Add new capabilities/formats
   - Update examples if needed
   - Maintain consistent tone and format
   - Be specific (avoid "etc." or vague descriptions)
   - **Use web search findings** to enrich documentation with actual provider/API details

4. **Check for consistency**
   - Similar features documented similarly?
   - Naming conventions consistent?
   - Links still valid?

5. **Update navigation** 🔥
   - **If creating a new page**, immediately update `docs.json`:
     ```bash
     # Add the page to the appropriate navigation group
     # Maintain alphabetical ordering
     ```
   - **Validation**: Verify alphabetical placement in the navigation array
   - **Common locations**:
     - LLM providers: `integrations.llms` array
     - Guardrails: `integrations.guardrails` array
     - Features: Appropriate product section

6. **Choose the correct documentation location**
   - **OpenTelemetry features** → `product/observability/opentelemetry.mdx`
   - **General tracing concepts** → `product/observability/traces.mdx`
   - **Provider integrations** → `integrations/llms/<provider>.mdx`
   - **Guardrails** → `product/guardrails/` or `integrations/guardrails/`
   - **Metrics** → `self-hosting/prometheus-metrics.mdx`
   - **Deployment/Infrastructure features** (CORS, proxy, environment variables) → `self-hosting/` or enterprise deployment docs
   - **API parameters** → Ensure parameters are added to the correct endpoint's parameter list

7. **Verify changelog completeness** 🔥
   - **After reviewing all PRs, cross-reference with changelog entries**
   - For each changelog item, verify it has corresponding documentation:
     - Check if user-facing features are documented in the appropriate location
     - Check if infrastructure/deployment features (CORS, proxy, etc.) need documentation
     - If a changelog item lacks documentation, **ask the user** whether documentation is needed or if it's internal/enterprise-only

**Action:** Make precise updates to documentation files

---

## Step 7: Validate Changes

### Run linter:
```
Check each updated file for linter errors
```

### Verify completeness:
- [ ] All new features documented?
- [ ] All examples accurate?
- [ ] All links working?
- [ ] Consistent formatting?
- [ ] No broken references?
- [ ] **New pages added to docs.json navigation?** 🔥
- [ ] **Content placed in the correct documentation file?** 🔥
- [ ] **Web search insights incorporated?** 🔥
- [ ] **Changelog entries verified** - Each changelog item checked for corresponding documentation 🔥
- [ ] **Parameters/features in correct endpoint** - Verified parameters belong to the right API endpoint 🔥
- [ ] **Unclear items discussed with user** - Asked user about ambiguous documentation needs (CORS, proxy, etc.) 🔥

### Enhanced validation checklist (NEW):

**For New Providers:**
- [ ] Provider slug documented
- [ ] Supported models listed (from web search)
- [ ] Authentication methods explained
- [ ] Custom configuration options documented
- [ ] Code examples in Python, Node.js, cURL
- [ ] Link to official provider documentation

**For New Metrics:**
- [ ] Metric name, type, and unit specified
- [ ] Business value clearly explained
- [ ] Query examples provided
- [ ] Correlation with related metrics explained
- [ ] Metric count updated in overview section

**For Standards Support:**
- [ ] Standard name and link to specification
- [ ] Supported attributes documented
- [ ] Example data provided
- [ ] Integration with existing features explained

### Review git diff:
```bash
cd ~/workspace/docs-core
git diff main
```

**Action:** Confirm all changes are intentional and accurate

---

## Step 8: Create Release Documentation

### Create release notes file:
```
/changelog/gateway-enterprise-node-v<VERSION>.mdx
```

Include:
- Release date
- Summary of changes
- Detailed PR descriptions
- User impact for each change
- Migration notes (if any)

### Create documentation update summary:
```
/changelog/gateway-enterprise-node-v<VERSION>-doc-updates.md
```

Include:
- List of PRs analyzed
- Documentation impact decision for each PR
- Files updated with before/after snippets
- Rationale for each decision
- Summary table

---

## Step 9: Review and Hand Off

### Final review:
```bash
cd ~/workspace/docs-core

# Review all changes made
git status

# View the diff
git diff
```

### Summary of changes:
- List all files modified
- Confirm all documentation is accurate
- Note any files created
- Highlight any important changes for review

**⚠️ STOP HERE**

**All documentation changes are complete. The files are ready for user review and editing.**

---

## Step 10: Reflect and Improve Workflow

**After completing the workflow, reflect on the process:**

### Ask yourself:
- Did we discover new edge cases?
- Were there ambiguities that slowed us down?
- Did we need to read code more/less than expected?
- Were there patterns that could be automated?
- Did we encounter new documentation structures?
- Were search strategies effective?

### Suggest to user:
"Based on this release review, I noticed [X]. We could improve this playbook by [Y]. Would you like me to update the playbook to include this improvement?"

**Examples of improvements:**
- New documentation file locations discovered
- New provider-specific patterns
- Better search queries for specific types of changes
- Additional decision criteria
- New validation steps

**Action:** Document learnings and update playbook if needed

---

## Quick Decision Tree

```
Start Workflow
    │
    ├─→ Release version specified?
    │   │
    │   ├─→ NO → Ask user for version
    │   │
    │   └─→ YES → Confirm version
    │
    ├─→ Create docs branch
    │   └─→ Checkout: docs/gateway-node-v<VERSION>
    │
    ├─→ Get PR list from gateway repo
    │
    ├─→ For each PR:
    │   │
    │   ├─→ Analyze code changes
    │   │   │
    │   │   ├─→ New provider/integration? → 🔥 WEB SEARCH for models/features
    │   │   │
    │   │   ├─→ API version change? → 🔥 WEB SEARCH for v2 changes
    │   │   │
    │   │   ├─→ Contains pricing/cost/token/telemetry? → 🔥 READ FULL CODE
    │   │   │
    │   │   └─→ Unclear? → Read code or ask user
    │   │
    │   ├─→ User-facing change?
    │   │   │
    │   │   ├─→ YES → Find relevant docs → Update
    │   │   │         │
    │   │   │         ├─→ New page created? → 🔥 UPDATE docs.json
    │   │   │         │
    │   │   │         └─→ Choose correct location (OTel vs Traces, etc.)
    │   │   │
    │   │   ├─→ NO → Document reason → Skip
    │   │   │
    │   │   └─→ UNSURE → 🔥 Check red flags (cost/token/telemetry) → Investigate
    │   │
    │   └─→ Next PR
    │
    ├─→ Validate all updates
    │   ├─→ Linter check
    │   ├─→ docs.json updated?
    │   └─→ Content in right location?
    │
    ├─→ Create release notes & summary
    │
    ├─→ Review changes & hand off to user
    │
    └─→ STOP: User reviews and edits
         │
         └─→ (Continue with Git Workflow Playbook)
```

---

## Checklist Template

Use this for each release:

```markdown
## Release v<VERSION> Documentation Review

**Release Date:** YYYY-MM-DD
**Previous Version:** v<PREV_VERSION>
**Current Version:** v<CURRENT_VERSION>
**Branch:** docs/gateway-node-v<VERSION>

### Setup
- [ ] Clean working directory confirmed
- [ ] Branch created: `docs/gateway-node-v<VERSION>`
- [ ] Working in correct branch

### PRs in This Release

- [ ] PR #XXX: <title>
  - Change: <description>
  - 🔥 Red Flags: pricing/cost/token/semantic? YES/NO
  - 🔍 Web Search: Did we search for provider/API details? YES/NO/N/A
  - Doc Impact: YES/NO
  - Reason: <explanation>
  - Files Updated: <list or "none">

- [ ] PR #YYY: <title>
  - Change: <description>
  - 🔥 Red Flags: pricing/cost/token/semantic? YES/NO
  - 🔍 Web Search: Did we search for provider/API details? YES/NO/N/A
  - Doc Impact: YES/NO
  - Reason: <explanation>
  - Files Updated: <list or "none">

### Documentation Files Updated

- [ ] `/path/to/file1.mdx` - <what was updated>
- [ ] `/path/to/file2.mdx` - <what was updated>

### Validation

- [ ] All updated files pass linter
- [ ] All new features documented
- [ ] All examples tested (conceptually)
- [ ] Cross-references updated
- [ ] 🔥 **docs.json updated for new pages**
- [ ] 🔥 **Web search conducted for providers/APIs**
- [ ] 🔥 **Content in correct documentation location**
- [ ] 🔥 **Red flag PRs fully investigated**
- [ ] Release notes created
- [ ] Summary document created
- [ ] Git diff reviewed
- [ ] Changes ready for user review

---

## Tips & Best Practices

1. **Start Broad, Then Narrow**
   - Search semantically first to understand scope
   - Then use specific file/pattern searches
   - Finally, grep for exact terms

2. **Be Specific in Documentation**
   - List all supported formats explicitly
   - Avoid vague terms like "etc." or "various"
   - Provide complete information

3. **Think Like a User**
   - Would a user need to know about this change?
   - Does it change how they use the product?
   - Does it expand or limit capabilities?

4. **Document the Decision**
   - Even when NOT updating docs, document why
   - Helps future reviewers understand reasoning
   - Creates institutional knowledge

5. **Check Related Docs**
   - Updates might be needed in multiple places
   - Provider docs, feature docs, API refs might all need updates
   - Look for "See also" type relationships

6. **Validate Cross-Provider Consistency**
   - If updating Vertex AI docs, check if Gemini docs need similar updates
   - Keep similar features documented similarly across providers

7. **When in Doubt: Read Code or Ask**
   - **Read the code** if PR description is unclear or mentions red flag keywords
   - **Read the actual code changes** (not just commit messages) to understand what changed
   - **Verify parameter/feature location** - Check which endpoint/API it belongs to before documenting
   - **Ask the user** if ambiguous about user-facing impact, documentation needs, or infrastructure features
   - **Never guess** - always verify when uncertain

8. **Verify Changelog Completeness**
   - After analyzing all PRs, cross-reference with changelog entries
   - For each changelog item, verify it has corresponding documentation
   - If documentation is missing, ask user if it's needed or internal-only
   - Distinguish between user-facing API changes and infrastructure/deployment changes

9. **Stop Before Committing**
   - This workflow focuses on making documentation changes only
   - Always stop and hand off to user for review
   - User may want to edit, refine, or adjust the documentation
   - Git operations (commit, PR, merge) are handled in a separate workflow

