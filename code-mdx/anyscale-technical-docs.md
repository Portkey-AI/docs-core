---
title: 'Anyscale'
description: 'Integrate Anyscale LLMs into your applications with Portkey'
---

**Portkey Provider Slug:** `anyscale`

## Overview

Anyscale Private Endpoints allows you to seamlessly serve the most popular open source large language models (LLMs) in your cloud environment without compromising on performance. As a result, you can concentrate on customizing your LLM-powered applications while adhering to the highest security standards.

**Note:** Effective August 1, 2024 Anyscale Endpoints API will be available exclusively through the fully Hosted Anyscale Platform. Multi-tenant access to LLM models will be removed.

## Quick Links

- [Anyscale Website](https://docs.anyscale.com/endpoints/intro/)
- [Documentation](https://docs.anyscale.com/1.0.0/endpoints/overview/)

## Supported Features

### Supported Models

| Type | Models |
|------|--------|
| Chat Completions | mistralai/Mistral-7B-Instruct-v0.1, HuggingFaceH4/zephyr-7b-beta, meta-llama/Llama-2-7b-chat-hf, meta-llama/Llama-2-13b-chat-hf, meta-llama/Llama-2-70b-chat-hf, codellama/CodeLlama-34b-Instruct-hf |

[More models](https://docs.anyscale.com/1.0.0/endpoints/overview/)

## Integration Guide

### Chat Completions

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="anyscale",
    authorisation="$ANYSCALE_API_KEY"
)

response = portkey.chat.completions.create(
    model="meta-llama/Llama-2-7b-chat-hf",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)
```

```Node node
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "anyscale",
    authorisation: "$ANYSCALE_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "meta-llama/Llama-2-7b-chat-hf",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});

console.log(response.choices[0].message.content);
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: anyscale" \
  -H "Authorization: Bearer $ANYSCALE_API_KEY" \
  -d '{
    "model": "meta-llama/Llama-2-7b-chat-hf",
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
    api_key="$ANYSCALE_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="anyscale",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.chat.completions.create(
    model="meta-llama/Llama-2-7b-chat-hf",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
    apiKey: "$ANYSCALE_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "anyscale",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await openai.chat.completions.create({
    model: "meta-llama/Llama-2-7b-chat-hf",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});

console.log(response.choices[0].message.content);
```

</CodeGroup>

### Integration via Virtual Key

1. **Generate a Virtual Key**
   Get your API key from Anyscale and add it to Portkey to create a virtual key.

   You can get your Anyscale API key from the Anyscale console.

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
    model="meta-llama/Llama-2-7b-chat-hf",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)
```

```Node node
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    virtualKey: "$VIRTUAL_KEY"
});

const response = await portkey.chat.completions.create({
    model: "meta-llama/Llama-2-7b-chat-hf",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});

console.log(response.choices[0].message.content);
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-virtual-key: $VIRTUAL_KEY" \
  -d '{
    "model": "meta-llama/Llama-2-7b-chat-hf",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", content": "What is the capital of France?"}
    ]
  }'
```

```Python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$ANYSCALE_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        api_key="$PORTKEY_API_KEY",
        virtual_key="$VIRTUAL_KEY"
    )
)

response = client.chat.completions.create(
    model="meta-llama/Llama-2-7b-chat-hf",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
    apiKey: "$ANYSCALE_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        apiKey: "$PORTKEY_API_KEY",
        virtualKey: "$VIRTUAL_KEY"
    })
});

const response = await openai.chat.completions.create({
    model: "meta-llama/Llama-2-7b-chat-hf",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});

console.log(response.choices[0].message.content);
```

</CodeGroup>

### Prompt Playground

Manage and test prompts for Anyscale models in the Prompt Library.

[Insert screenshot of Prompt Playground here]

#### Using Prompts from the Prompt Library

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="anyscale",
    authorisation="$ANYSCALE_API_KEY"
)

response = portkey.chat.completions.create(
    model="meta-llama/Llama-2-7b-chat-hf",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    prompt_id="your-prompt-id"
)

print(response.choices[0].message.content)
```

```Node node
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "anyscale",
    authorisation: "$ANYSCALE_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "meta-llama/Llama-2-7b-chat-hf",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ],
    promptId: "your-prompt-id"
});

console.log(response.choices[0].message.content);
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: anyscale" \
  -H "Authorization: Bearer $ANYSCALE_API_KEY" \
  -d '{
    "model": "meta-llama/Llama-2-7b-chat-hf",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is the capital of France?"}
    ],
    "prompt_id": "your-prompt-id"
  }'
```

```Python OpenAI Python SDK
Not supported
```

```Node OpenAI Node SDK
Not supported
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
