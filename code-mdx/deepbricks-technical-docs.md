# Deepbricks

**Portkey Provider Slug:** `deepbricks`

## Overview

Deepbricks is an inference API that allows you to call models like GPT-4o, Claude, and Llama over a unified API. This document outlines the features, supported models, and integration methods available for Deepbricks through the Portkey platform.

## Quick Links

- [Deepbricks Website](https://deepbricks.ai)
- [Documentation](https://deepbricks.ai/docs)
- [Portkey Community](https://portkey.ai/community)

## Supported Features

### Supported Models

| Type | Models |
|------|--------|
| Chat Completions and Image Generations | GPT-4o-2024-08-06, GPT-4o, GPT-4-turbo, Claude-3.5-Sonnet, GPT-4o-mini, GPT-3.5-turbo, LLama-3.1-405b, LLama-3.1-70b, LLama-3-70b |
| Image Generation | dall-e-3 |

[More models](https://deepbricks.ai/pricing)

### Unsupported Features

- **Prompt Playground**: Prompt playground is not supported for Deepbricks models

## Integration Guide

### Chat Completions Call

<CodeGroup>

```python
# Use Portkey Python SDK to make chat calls to Deepbricks chat completions models
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="deepbricks",
    Authorization="$PROVIDER_API_KEY"
)

response = portkey.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
```

```js
// Use Portkey Node.js SDK to make chat calls to Deepbricks chat completions models
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "deepbricks",
    Authorization: "$PROVIDER_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "gpt-4o",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});
```

```bash
# Use Portkey's REST API to make chat calls to Deepbricks chat completions models
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: deepbricks" \
-H "Authorization: Bearer $PROVIDER_API_KEY" \
-d '{
  "model": "gpt-4o",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
  ]
}'
```

```python
# Use OpenAI Python SDK to make chat calls to Deepbricks chat completions models
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$PROVIDER_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="deepbricks",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
```

```js
// Use OpenAI Node.js SDK to make chat calls to Deepbricks chat completions models
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "deepbricks",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});
```

</CodeGroup>

### Integration via Virtual Key

1. **Generate a Virtual Key**
   Get your API key from Deepbricks and add it to Portkey to create a virtual key.

   You can get your Deepbricks API key from the Deepbricks website [here](https://deepbricks.ai/api-key).

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
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
```

```js
// Initialize Portkey with the virtual key in Node.js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    virtualKey: "$VIRTUAL_KEY"
});

const response = await portkey.chat.completions.create({
    model: "gpt-4o",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});
```

```bash
# Use Portkey's REST API to make chat calls to Deepbricks chat completions models like gpt-4o
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-virtual-key: $VIRTUAL_KEY" \
-d '{
  "model": "gpt-4o",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
  ]
}'
```

```python
# Use OpenAI Python SDK to make chat calls to Deepbricks chat completions models like gpt-4o
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
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
```

```js
// Use OpenAI Node.js SDK to make chat calls to Deepbricks chat completions models like gpt-4o
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        apiKey: "$PORTKEY_API_KEY",
        virtualKey: "$VIRTUAL_KEY"
    })
});

const response = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});
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