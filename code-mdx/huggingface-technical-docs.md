---
title: 'HuggingFace'
description: 'Integrate HuggingFace LLMs into your applications with Portkey'
---

**Portkey Provider Slug:** `huggingface`

## Overview

HuggingFace is a platform for developers to collaborate on building LLM-powered applications. This document outlines the features, supported models, and integration methods available for HuggingFace through the Portkey platform.

## Quick Links

- [HuggingFace Website](https://huggingface.co/)
- [Pricing](https://huggingface.co/pricing#endpoints)
- [Documentation](https://huggingface.co/docs/api-inference/index)
- [Discord Community](https://huggingface.co/join/discord)

## Supported Features

### Supported Models

| Type | Models |
|------|--------|
| Chat Completions | All OpenAI compliant chat completions models on HuggingFace |
| Completions | All OpenAI compliant completions models on HuggingFace |

[View all supported models](https://huggingface.co/models)

### Unsupported Features

- Portkey currently only supports OpenAI compatible models on HuggingFace
- Prompt playground is not supported for HuggingFace models

## Integration Guide

### Chat Completions Calls

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="huggingface",
    Authorization="$PROVIDER_API_KEY"
)

response = portkey.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
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
    provider: "huggingface",
    Authorization: "$PROVIDER_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct",
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
-H "x-portkey-provider: huggingface" \
-H "Authorization: Bearer $PROVIDER_API_KEY" \
-d '{
  "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
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
    api_key="$PROVIDER_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="huggingface",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about programming."}
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
        provider: "huggingface",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await client.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "Tell me a joke about programming."}
    ]
});
```

</CodeGroup>

### Integration via Virtual Key

1. **Generate a Virtual Key**
   Get your API key from HuggingFace and add it to Portkey to create a virtual key.

   You can get your HuggingFace API key from the HuggingFace website [here](https://huggingface.co/).

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
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the capital of France?"}
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
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What's the capital of France?"}
    ]
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-virtual-key: $VIRTUAL_KEY" \
-d '{
  "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", content: "What's the capital of France?"}
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
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the capital of France?"}
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
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What's the capital of France?"}
    ]
});
```

</CodeGroup>

### Prompt Playground

Coming soon

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