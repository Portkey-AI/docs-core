# Cohere

**Portkey Provider Slug:** `cohere`

## Overview

Cohere allows developers and enterprises to build LLM-powered applications. This document outlines the features, supported models, and integration methods available for Cohere through the Portkey platform.

## Quick Links

- [Cohere Website](https://cohere.com/)
- [Documentation](https://docs.cohere.com/docs/the-cohere-platform)
- [Discord Community](https://discord.com/invite/co-mmunity)

## Supported Features

### Supported Models

| Type | Models |
|------|--------|
| Chat Completions and Generate | command-r-plus-* family, command-r-* family, command, command-light, command-nightly, command-light-nightly, c4ai-aya-23-35b, c4ai-aya-23-8b |
| Embed | embed-* family |
| Rerank | rerank-* family |
| Rate | Supported |
| Summarise | Supported |
| Classify | Supported |

[More models](https://docs.cohere.com/docs/models)

### Unsupported Features

- Prompt playground is not supported for Cohere models
- Unsupported parameters: response_format, seed, prompt_truncation, preambles, documents, conversation_id, connectors, search_queries_only, citation_quality, max_input_tokens, safety_mode

### Cohere-Specific Features

Rerank, Rate, Summarise, and Classify are supported through the Post Proxy call. Read more [here](/../link/to/post-proxy-dcoumentation).

## Integration Guide

### Chat Completions Call

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="cohere",
    authorisation="$COHERE_API_KEY"
)

response = portkey.chat.completions.create(
    model="command-r-plus",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about programming."}
    ]
)
```

```Node node
import Portkey from 'portkey-ai';

const portkey = new Portkey({
  apiKey: "$PORTKEY_API_KEY",
  provider: "cohere",
  authorisation: "$COHERE_API_KEY"
});

const response = await portkey.chat.completions.create({
  model: "command-r-plus",
  messages: [
    {role: "system", content: "You are a helpful assistant."},
    {role: "user", content: "Tell me a joke about programming."}
  ]
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: cohere" \
  -H "Authorization: Bearer $COHERE_API_KEY" \
  -d '{
    "model": "command-r-plus",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Tell me a joke about programming."}
    ]
  }'
```

```Python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$COHERE_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="cohere",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.chat.completions.create(
    model="command-r-plus",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about programming."}
    ]
)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
  apiKey: "$COHERE_API_KEY",
  baseURL: PORTKEY_GATEWAY_URL,
  defaultHeaders: createHeaders({
    provider: "cohere",
    apiKey: "$PORTKEY_API_KEY"
  })
});

const response = await openai.chat.completions.create({
  model: "command-r-plus",
  messages: [
    {role: "system", content: "You are a helpful assistant."},
    {role: "user", content: "Tell me a joke about programming."}
  ]
});
```

</CodeGroup>

### Integration via Virtual Key

1. **Generate a Virtual Key**
   Get your API key from Cohere and add it to Portkey to create a virtual key.

   You can get your Cohere API key from the Cohere website [here](https://dashboard.cohere.com/api-keys).

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
    model="command-r-plus",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about programming."}
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
  model: "command-r-plus",
  messages: [
    {role: "system", content: "You are a helpful assistant."},
    {role: "user", content: "Tell me a joke about programming."}
  ]
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-virtual-key: $VIRTUAL_KEY" \
  -d '{
    "model": "command-r-plus",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Tell me a joke about programming."}
    ]
  }'
```

```Python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        api_key="$PORTKEY_API_KEY",
        virtual_key="$VIRTUAL_KEY"
    )
)

response = client.chat.completions.create(
    model="command-r-plus",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", content": "Tell me a joke about programming."}
    ]
)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
  apiKey: "",
  baseURL: PORTKEY_GATEWAY_URL,
  defaultHeaders: createHeaders({
    apiKey: "$PORTKEY_API_KEY",
    virtualKey: "$VIRTUAL_KEY"
  })
});

const response = await openai.chat.completions.create({
  model: "command-r-plus",
  messages: [
    {role: "system", content: "You are a helpful assistant."},
    {role: "user", content: "Tell me a joke about programming."}
  ]
});
```

</CodeGroup>

### Special Example: Using Cohere Rerank with Post Proxy

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="cohere",
    authorisation="$COHERE_API_KEY"
)

response = portkey.post_proxy(
    endpoint="https://api.cohere.ai/v1/rerank",
    json={
        "model": "rerank-english-v2.0",
        "query": "What is the capital of France?",
        "documents": [
            "The capital of France is Paris.",
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
  authorisation: "$COHERE_API_KEY"
});

const response = await portkey.postProxy({
  endpoint: "https://api.cohere.ai/v1/rerank",
  json: {
    model: "rerank-english-v2.0",
    query: "What is the capital of France?",
    documents: [
      "The capital of France is Paris.",
      "London is the capital of the United Kingdom.",
      "Berlin is the capital of Germany."
    ],
    top_n: 2
  }
});
```

```bash cURL
curl https://api.portkey.ai/proxy \
  -X POST \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: cohere" \
  -H "Authorization: Bearer $COHERE_API_KEY" \
  -d '{
    "endpoint": "https://api.cohere.ai/v1/rerank",
    "json": {
      "model": "rerank-english-v2.0",
      "query": "What is the capital of France?",
      "documents": [
        "The capital of France is Paris.",
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
    api_key="$COHERE_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="cohere",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.post(
    "proxy",
    json={
        "endpoint": "https://api.cohere.ai/v1/rerank",
        "json": {
            "model": "rerank-english-v2.0",
            "query": "What is the capital of France?",
            "documents": [
                "The capital of France is Paris.",
                "London is the capital of the United Kingdom.",
                "Berlin is the capital of Germany."
            ],
            "top_n": 2
        }
    }
)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
  apiKey: "$COHERE_API_KEY",
  baseURL: PORTKEY_GATEWAY_URL,
  defaultHeaders: createHeaders({
    provider: "cohere",
    apiKey: "$PORTKEY_API_KEY"
  })
});

const response = await openai.post('proxy', {
  json: {
    endpoint: "https://api.cohere.ai/v1/rerank",
    json: {
      model: "rerank-english-v2.0",
      query: "What is the capital of France?",
      documents: [
        "The capital of France is Paris.",
        "London is the capital of the United Kingdom.",
        "Berlin is the capital of Germany."
      ],
      top_n: 2
    }
  }
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