---
title: 'Local AI'
description: 'Integrate Local AI models into your applications with Portkey'
---

**Portkey Provider Slug:** `local_ai`

## Overview

Local AI lets you run over 379 open source chat, image, audio models locally with a drop-in replacement for the OpenAI API. This document outlines the features, supported models, and integration methods available for Local AI through the Portkey platform.

## Quick Links

- [Local AI Website](https://localai.io/)
- [Documentation](https://localai.io/)
- [Community](https://portkey.ai/community)

## Supported Features

### Supported Models

Local AI supports a wide range of models for various tasks:

- Chat Completions
- Reranker
- Text-to-Speech
- Image Generation
- Embeddings
- Speech-to-Text

Portkey supports Local AI API through a Post Proxy call. Read more [here](/../link/to/post-proxy-dcoumentation).

[Explore more models](https://localai.io/gallery.html)

### Unsupported Features

- **Prompt Playground**: Prompt playground is not supported for Inference models.

## Integration Guide

### Chat Completions Call

<CodeGroup>

```python Python
from portkey_ai import Portkey

# Initialize the client with the API key and custom host for Local AI
portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    custom_host="http://localhost:8080"  # Replace with your Local AI endpoint
)

# Make a chat completion call
response = portkey.chat.completions.create(
    model="llama-3.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me about Local AI."}
    ]
)

print(response.choices[0].message.content)
```

```js Node.js
import Portkey from 'portkey-ai';

// Initialize the client with the API key and custom host for Local AI
const portkey = new Portkey({
  apiKey: "$PORTKEY_API_KEY",
  customHost: "http://localhost:8080"  // Replace with your Local AI endpoint
});

// Make a chat completion call
const response = await portkey.chat.completions.create({
  model: "llama-3.1",
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "Tell me about Local AI." }
  ]
});

console.log(response.choices[0].message.content);
```

```bash cURL
curl -X POST "http://localhost:8080/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -d '{
    "model": "llama-3.1",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Tell me about Local AI."}
    ]
  }'
```

```python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$PROVIDER_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="local_ai",
        api_key="$PORTKEY_API_KEY",
        custom_host="http://localhost:8080"  # Replace with your Local AI endpoint
    )
)

response = client.chat.completions.create(
    model="llama-3.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me about Local AI."}
    ]
)

print(response.choices[0].message.content)
```

```js OpenAI Node.js SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "local_ai",
        apiKey: "$PORTKEY_API_KEY",
        customHost: "http://localhost:8080"  // Replace with your Local AI endpoint
    })
});

const response = await openai.chat.completions.create({
  model: "llama-3.1",
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "Tell me about Local AI." }
  ]
});

console.log(response.choices[0].message.content);
```

</CodeGroup>

### Integration via Virtual Key

Information about integration via virtual key is not provided in the given JSON data.

### Prompt Playground

Prompt playground functionality for Local AI is coming soon.

## Explore Advanced Portkey Features

<CardGroup cols={2}>
  <Card title="Configure Routing" href="/docs/product/ai-gateway/routing">
    Configure routing for your Local AI requests
  </Card>
  <Card title="Add Metadata to Requests" href="/docs/product/observability/metadata">
    Add metadata to your Local AI requests
  </Card>
  <Card title="A/B Test Different Models" href="/docs/product/ai-gateway/load-balance">
    A/B test different models
  </Card>
  <Card title="Gain Insights to Requests" href="/docs/product/observability/traces">
    Gain insights to your Local AI requests
  </Card>
</CardGroup>