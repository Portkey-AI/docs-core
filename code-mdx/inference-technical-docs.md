---
title: 'Inference.net'
description: 'Integrate Inference.net LLMs into your applications with Portkey'
---

**Portkey Provider Slug:** `Inference`

## Overview

Inference.net is a wholesaler of LLM inference tokens for models like Llama 3.1. This document outlines the features, supported models, and integration methods available for Inference.net through the Portkey platform.

## Quick Links

- [Inference.net Website](https://www.inference.net/)
- [Documentation](https://www.inference.net/)
- [Community](https://portkey.ai/community)

## Supported Features

### Supported Models

| Type | Models |
|------|--------|
| Chat Completions | LLama-3.1, Llama-3 |

[More models](https://www.inference.net/)

### Unsupported Features

- **Prompt Playground**: Prompt playground is not supported for Inference models

## Integration Guide

### Chat Completions Calls

<CodeGroup>

```python
# Use Portkey Python SDK to make chat calls to Inference chat completions models
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="inference",
    authorisation="$PROVIDER_API_KEY"
)

response = portkey.chat.completions.create(
    model="llama-3.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about AI."}
    ]
)

print(response.choices[0].message.content)
```

```js
// Use Portkey Node.js SDK to make chat calls to Inference chat completions models
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "inference",
    authorisation: "$PROVIDER_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "llama-3.1",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "Tell me a joke about AI."}
    ]
});

console.log(response.choices[0].message.content);
```

```bash
# Use Portkey's REST API to make chat calls to Inference chat completions models
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: inference" \
  -H "Authorization: Bearer $PROVIDER_API_KEY" \
  -d '{
    "model": "llama-3.1",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Tell me a joke about AI."}
    ]
  }'
```

```python
# Use OpenAI Python SDK to make chat calls to Inference chat completions models
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$PROVIDER_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="inference",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.chat.completions.create(
    model="llama-3.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about AI."}
    ]
)

print(response.choices[0].message.content)
```

```js
// Use OpenAI Node.js SDK to make chat calls to Inference chat completions models
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "inference",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await openai.chat.completions.create({
    model: "llama-3.1",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "Tell me a joke about AI."}
    ]
});

console.log(response.choices[0].message.content);
```

</CodeGroup>

### Integration via Virtual Key

1. **Generate a Virtual Key**
   Get your API key from Inference and add it to Portkey to create a virtual key.

   You can get your Inference API key from the Inference website [here](https://www.inference.net/).

   [Insert screenshot of virtual key generation process here]

2. **Using the Virtual Key**

<CodeGroup>

```python
# Initialize Portkey with the virtual key in Python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    virtual_key="$VIRTUAL_KEY"
)

response = portkey.chat.completions.create(
    model="llama-3.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about AI."}
    ]
)

print(response.choices[0].message.content)
```

```js
// Initialize Portkey with the virtual key in Node.js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    virtualKey: "$VIRTUAL_KEY"
});

const response = await portkey.chat.completions.create({
    model: "llama-3.1",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "Tell me a joke about AI."}
    ]
});

console.log(response.choices[0].message.content);
```

```bash
# Use Portkey's REST API to make chat calls to Inference chat completions models like llama-3.1
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-virtual-key: $VIRTUAL_KEY" \
  -d '{
    "model": "llama-3.1",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Tell me a joke about AI."}
    ]
  }'
```

```python
# Use OpenAI Python SDK to make chat calls to Inference chat completions models like llama-3.1
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$PORTKEY_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        virtual_key="$VIRTUAL_KEY"
    )
)

response = client.chat.completions.create(
    model="llama-3.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about AI."}
    ]
)

print(response.choices[0].message.content)
```

```js
// Use OpenAI Node.js SDK to make chat calls to Inference chat completions models like llama-3.1
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
    apiKey: "$PORTKEY_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        virtualKey: "$VIRTUAL_KEY"
    })
});

const response = await openai.chat.completions.create({
    model: "llama-3.1",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "Tell me a joke about AI."}
    ]
});

console.log(response.choices[0].message.content);
```

</CodeGroup>

### Prompt Playground

Coming soon..

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