---
title: 'Ollama'
description: 'Integrate your locally hosted models on Ollama with Portkey'
---

**Portkey Provider Slug:** `ollama`

## Overview

Ollama offers integration of locally hosted models with Portkey. This document outlines the features, supported models, and integration methods available for Ollama through the Portkey platform.

## Quick Links

- [Ollama Website](https://ollama.com)
- [Documentation](https://ollama.com/library)
- [Community](https://portkey.ai/community)

## Supported Features

### Supported Models

| Type | Models |
|------|--------|
| Chat | Llama 3.1, Phi 3, Gemma, Mistral, Moondream, Code Llama, LlaVa |

[More models](https://github.com/ollama/ollama?tab=readme-ov-file#model-library)

### Unsupported Features

- **Generate**: Portkey does not support Ollama's models on the /generate route
- **Prompt Playground**: Prompt playground is not supported for Ollama models

## Integration Guide

### Chat Completions Call

<CodeGroup>

```python Python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="ollama"
)

response = portkey.chat.completions.create(
    model="llama2",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me about Llama 3.1."}
    ],
    custom_host="http://localhost:11434"
)
```

```js Node.js
import { Portkey } from "portkey-ai";

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "ollama"
});

const response = await portkey.chat.completions.create({
    model: "llama2",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "Tell me about Llama 3.1."}
    ],
    customHost: "http://localhost:11434"
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: ollama" \
-H "x-portkey-custom-host: http://localhost:11434" \
-d '{
  "model": "llama2",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me about Llama 3.1."}
  ]
}'
```

```python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="ollama",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.chat.completions.create(
    model="llama2",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me about Llama 3.1."}
    ],
    custom_host="http://localhost:11434"
)
```

```js OpenAI Node.js SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const client = new OpenAI({
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "ollama",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await client.chat.completions.create({
    model: "llama2",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "Tell me about Llama 3.1."}
    ],
    customHost: "http://localhost:11434"
});
```

</CodeGroup>

### Integration via Virtual Key

Coming soon...

### Prompt Playground

Coming soon...

## Explore Advanced Portkey Features

<CardGroup cols={2}>
  <Card title="Configure Routing" href="/docs/product/ai-gateway/routing">
    <img src="/api/placeholder/400/320" alt="Configure Routing" />
  </Card>
  <Card title="Add Metadata to Requests" href="/docs/product/observability/metadata">
    <img src="/api/placeholder/400/320" alt="Add Metadata to Requests" />
  </Card>
  <Card title="A/B Test Different Models" href="/docs/product/ai-gateway/load-balance">
    <img src="/api/placeholder/400/320" alt="A/B Test Different Models" />
  </Card>
  <Card title="Gain Insights to Requests" href="/docs/product/observability/traces">
    <img src="/api/placeholder/400/320" alt="Gain Insights to Requests" />
  </Card>
</CardGroup>