# Nexus Shield Integration (Sub-10ms Guardrail Proxy)

Nexus Shield provides in-RAM PII sanitization and security guardrails for Portkey-routed LLM requests with sub-10ms overhead.

## Usage with Portkey

You can route your requests through Nexus Shield by specifying its endpoint in your Portkey configuration or setting `base_url`.

```python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="PORTKEY_API_KEY",
    base_url="https://api.nexusshield.ai/v1",
    custom_headers={"X-API-Key": "nx_live_YOUR_KEY"},
)

response = portkey.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello, my phone is 555-0199"}],
)

print(response)
```

## Features

- **Sub-10ms Overhead:** Real-time RAM pattern evaluation before upstream LLM calls.
- **Zero-Log PII Redaction:** Sanitizes sensitive information without disk persistence.

## Get a Trial API Key

Register for a 14-day free trial at [api.nexusshield.ai](https://api.nexusshield.ai):

```bash
curl -X POST https://api.nexusshield.ai/v1/auth/register-trial \
  -H "Content-Type: application/json" \
  -d '{"email":"you@company.com"}'
```
