---
title: 'Monster API'
description: 'Integrate Monster API LLMs into your applications with Portkey'
---

**Portkey Provider Slug:** `monsterapi`

## Overview

Monster API allows developers and enterprises to build LLM-powered applications. This document outlines the features, supported models, and integration methods available for Monster API through the Portkey platform.

## Quick Links

- [Monster API Website](https://monsterapi.ai/)
- [Pricing](https://monsterapi.ai/pricing)
- [Documentation](https://developer.monsterapi.ai/reference/generate_v1_generate_post)
- [Discord Community](https://discord.com/invite/mVXfag4kZN)

## Supported Features

### Supported Models

| Type | Models |
|------|--------|
| Chat Completions | google/gemma-2-9b-it, mistralai/Mistral-7B-Instruct-v0.2, meta-llama/Meta-Llama-3-8B-Instruct, microsoft/Phi-3-mini-4k-instruct |

[More models](https://llm.monsterapi.ai/docs)

### Unsupported Features

- **Image Generation**: Portkey does not support image generation models for Monster API
- **Speech**: Portkey does not support speech models for Monster API
- **Compare**: Portkey does not support compare models for Monster API
- **Prompt Playground**: Prompt playground is not supported for Monster API models

## Integration Guide

### Chat Completions Calls

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="monsterapi",
    Authorization="$PROVIDER_API_KEY"
)

response = portkey.chat.completions.create(
    model="google/gemma-2-9b-it",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
```

```Node node
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "monsterapi",
    Authorization: "$PROVIDER_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "google/gemma-2-9b-it",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: monsterapi" \
-H "Authorization: Bearer $PROVIDER_API_KEY" \
-d '{
  "model": "google/gemma-2-9b-it",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
  ]
}'
```

```Python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$PROVIDER_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="monsterapi",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.chat.completions.create(
    model="google/gemma-2-9b-it",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const client = new OpenAI({
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "monsterapi",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await client.chat.completions.create({
    model: "google/gemma-2-9b-it",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});
```

</CodeGroup>

### Integration via Virtual Key

1. **Generate a Virtual Key**
   Get your API key from Monster API and add it to Portkey to create a virtual key.

   You can get your Monster API key from the Monster API website [here](https://monsterapi.ai/).

   [Insert screenshot of virtual key generation process here]

2. **Using the Virtual Key**

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    virtual_key="$VIRTUAL_KEY"
)

response = portkey.chat.completions.create(
    model="google/gemma-2-9b-it",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
```

```Node node
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    virtualKey: "$VIRTUAL_KEY"
});

const response = await portkey.chat.completions.create({
    model: "google/gemma-2-9b-it",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-virtual-key: $VIRTUAL_KEY" \
-d '{
  "model": "google/gemma-2-9b-it",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
  ]
}'
```

```Python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$PROVIDER_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        api_key="$PORTKEY_API_KEY",
        virtual_key="$VIRTUAL_KEY"
    )
)

response = client.chat.completions.create(
    model="google/gemma-2-9b-it",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const client = new OpenAI({
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        apiKey: "$PORTKEY_API_KEY",
        virtualKey: "$VIRTUAL_KEY"
    })
});

const response = await client.chat.completions.create({
    model: "google/gemma-2-9b-it",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});
```

</CodeGroup>

### Prompt Playground

Coming soon...

### Special Example: Using Cohere Rerank with Post Proxy

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="cohere",
    Authorization="$PROVIDER_API_KEY"
)

response = portkey.post_proxy(
    url="https://api.cohere.ai/v1/rerank",
    json={
        "model": "rerank-english-v2.0",
        "query": "What is the capital of France?",
        "documents": [
            "Paris is the capital of France.",
            "London is the capital of the United Kingdom.",
            "Berlin is the capital of Germany."
        ],
        "top_n": 2
    }
)
```

```Node node
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "cohere",
    Authorization: "$PROVIDER_API_KEY"
});

const response = await portkey.postProxy({
    url: "https://api.cohere.ai/v1/rerank",
    json: {
        model: "rerank-english-v2.0",
        query: "What is the capital of France?",
        documents: [
            "Paris is the capital of France.",
            "London is the capital of the United Kingdom.",
            "Berlin is the capital of Germany."
        ],
        top_n: 2
    }
});
```

```bash cURL
curl https://api.portkey.ai/post-proxy \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: cohere" \
-H "Authorization: Bearer $PROVIDER_API_KEY" \
-d '{
  "url": "https://api.cohere.ai/v1/rerank",
  "json": {
    "model": "rerank-english-v2.0",
    "query": "What is the capital of France?",
    "documents": [
      "Paris is the capital of France.",
      "London is the capital of the United Kingdom.",
      "Berlin is the capital of Germany."
    ],
    "top_n": 2
  }
}'
```

```Python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$PROVIDER_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="cohere",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.post_proxy(
    url="https://api.cohere.ai/v1/rerank",
    json={
        "model": "rerank-english-v2.0",
        "query": "What is the capital of France?",
        "documents": [
            "Paris is the capital of France.",
            "London is the capital of the United Kingdom.",
            "Berlin is the capital of Germany."
        ],
        "top_n": 2
    }
)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const client = new OpenAI({
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "cerebras",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await client.chat.completions.create({
    model: "cerebras/btlm-3b-8k-base",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ],
    tools: [{
        type: "function",
        function: {
            name: "get_capital",
            description: "Get the capital city of a country",
            parameters: {
                type: "object",
                properties: {
                    country: {
                        type: "string",
                        description: "The name of the country"
                    }
                },
                required: ["country"]
            }
        }
    }],
    tool_choice: "auto"
});
```

</CodeGroup>

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