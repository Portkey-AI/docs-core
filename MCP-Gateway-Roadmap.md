**MCP Gateway**

Detailed Capability Roadmap

# **Release Timeline**

MCP Gateway ships in three release waves, each building on the previous:

| GA Wave January 31, 2026 Core Governance | February Wave End of February Traffic Control | March Wave End of March Observability |
| :---: | :---: | :---: |

# **Authentication** (*who are you?*)

Verify user identity with enterprise-grade authentication mechanisms. Portkey supports multiple auth patterns to fit your existing identity infrastructure.

| Capability | What It Solves | Granularity | Release | Notes |
| :---- | :---- | :---: | :---: | :---- |
| **OAuth 2.1** | Modern OAuth with PKCE and enhanced security. Recommended for new implementations. | MCP Gateway | **GA** | — |
| **OAuth 2.0** | Standard OAuth flow for MCP server authentication. Compatible with most identity providers. | MCP Gateway | **GA** | — |
| **Bearer Token Auth** | Simple token-based authentication for MCP servers that don't require OAuth complexity. | MCP Gateway | **GA** | — |
| **Custom Auth** | Bring your own OAuth provider for MCP server authentication. Portkey acts as the identity broker. | MCP Gateway | **GA** | — |
| **User Identity Forwarding** | Propagate user identity through the entire request chain. MCP servers receive the original user context, not just a service account—enabling accurate attribution and downstream access control. | MCP Gateway / IDP | **GA** | — |
| **Webhooks for Authn** | Call your custom authentication endpoint during the auth flow. Full control over identity verification logic. | MCP Gateway | **Feb** |  |

# **Authorization** (*what can you access?*)

Control who can access which MCP servers, tools, and resources. Fine-grained permissions from workspace level down to individual tool operations.

| Capability | What It Solves | Granularity | Release | Notes |
| :---- | :---- | :---: | :---: | :---- |
| **Claim-Based Auth (Server)** | Authorize access based on JWT claims at the MCP server level. Route users to appropriate servers based on group membership. | MCP Server | **GA** | — |
| **Claim-Based Auth (Tool)** | Fine-grained authorization at the tool level based on JWT claims. Control tool access by user attributes. | Tool | **Feb** | — |
| **Webhooks for Authz** | Call your custom authorization service before each MCP request. Implement dynamic, context-aware access decisions | MCP Server | **Feb** |  |

# **Governance** (*what portkey will allow?*)

Protect your organization with policy enforcement for MCP tool calls.

| Capability | What It Solves | Granularity | Release | Notes |
| :---- | :---- | :---: | :---: | :---- |
| **User Access Control** | Define which users and teams can access which MCP servers through workspace-based permissions. | Workspace | **GA** | — |
| **Tool-Level Provisioning** | Within an MCP server, control which specific tools are accessible. Enable read operations while blocking write/modify. | Tool | **GA** | — |

# **Guardrails** (*what portkey will scan?*)

Protect your organization with input/output scanning

| Capability | What It Solves | Granularity | Release | Notes |
| :---- | :---- | :---: | :---: | :---- |
| **Guardrails on the MCP Gateway** | Input/output scanning for MCP tool calls. Detect and block sensitive data, PII, or policy violations. | MCP Server | **Feb** | — |
| **JWT Validation** | Validate JWT tokens against your JWKS endpoint. Configure issuer, audience, and claim requirements. | MCP Server | **Feb** | — |
| **Webhook/External Auth** | Call your custom authentication service for complex identity verification flows. | MCP Server | **Feb** | — |

# **Traffic Control** *(reliability)*

Build reliable MCP integrations with automatic failover, retries, and traffic management

| Capability | What It Solves | Granularity | Release | Notes |
| :---- | :---- | :---: | :---: | :---- |
| **Retries** | Automatic retry with configurable backoff for transient failures. Don't let intermittent issues break your agents. | MCP Server | **Feb** | — |
| **Timeouts** | Set maximum execution time for MCP tool calls. Prevent runaway operations from blocking your application. | MCP Server | **Feb** | — |
| **Circuit Breakers** | Automatically stop routing to failing MCP servers after threshold breaches. Configurable cooldown and recovery. | MCP Server | **Feb** | — |
| **Rate Limits** | Prevent abuse and control costs with rate limiting at user, team, MCP server, or tool level. | User, Team, Server, Tool | **Feb** | — |
| **Health Checks** | Proactive monitoring of MCP server availability. Know when servers are unhealthy before requests fail. | MCP Server | **March** | — |
| **Budgeting** | Set spending limits for MCP usage across users, teams, servers, or tools. Alert or block when thresholds are reached. | User, Team, Server, Tool | **Not planned** | — |
| **Failover** | Automatically route to backup MCP servers when primary fails. Configure fallback chains for critical tools. | MCP Server | **Not planned** | — |
| **Load Balancing / Canary** | Distribute traffic across MCP server instances with weighted routing. Gradually roll out new versions. | MCP Server | **Not planned** | — |

# **Observability & Analytics** *(visibility)*

Understand how your MCP servers are being used with detailed logging, tracing, and analytics.

| Capability | What It Solves | Granularity | Release | Notes |
| :---- | :---- | :---: | :---: | :---- |
| **Header Tracing** | Specify which request headers to include in logged traces. Useful for debugging and correlation. | Request | **Feb** | — |
| **OTEL Integration** | Export MCP Gateway telemetry to your OpenTelemetry collector. Integrate with your existing observability stack. | Gateway | **Feb** | — |
| **Payload Logging Control** | Enable or disable logging of request/response payloads per MCP server. Balance observability with data sensitivity. | MCP Server | **March** | — |
| **MCP-Specific Analytics** | Aggregate metrics for MCP server usage: which servers are called, which tools are invoked, latency distributions. | Server, Tool | **March** | — |
| **Unique User Metrics** | Accurate tracking of distinct users accessing MCP servers. Currently shows incorrect counts; will be fixed. | MCP Server | **March** | *Bug fix* |

# **Deployment & Integration** *(operations)*

Enterprise deployment patterns and integration points for managing MCP Gateway at scale.

| Capability | What It Solves | Granularity | Release | Notes |
| :---- | :---- | :---: | :---: | :---- |
| **API Coverage** | Programmatic access to all MCP Gateway configuration. Automate provisioning and governance at scale. | All | **Feb** | — |
| **Terraform Provider** | Infrastructure-as-code support for MCP Gateway. Manage configurations alongside your other infrastructure. | All | **Feb** | *End-to-end coverage* |
| **MCP Registry Import** | Import MCP servers from your existing internal registry. Sync server definitions rather than manual entry. | Org | **Not planned** | — |
| **API-to-MCP Generation** | Bring your existing API and Portkey will generate and host an MCP server for it, with end-to-end auth. | MCP Server | **Not planned** | — |

# **Deprecations & Out of Scope**

**SSE Transport:** The MCP committee is deprecating SSE (Server-Sent Events) transport in favor of HTTP streaming. Portkey will follow this direction and will not add SSE-specific features. Existing SSE support will be maintained for backward compatibility but is not recommended for new implementations.

—  
Questions about MCP Gateway? Contact vrushank.v@portkey.ai