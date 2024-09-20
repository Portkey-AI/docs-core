---
title: 'Moonshot'
description: 'Integrate Moonshot LLMs into your applications with Portkey'
---

**Portkey Provider Slug:** `moonshot`

## Overview

Moonshot allows developers and enterprises to build LLM-powered applications. This document outlines the features, supported models, and integration methods available for Moonshot through the Portkey platform.

## Quick Links

- [Moonshot Website](https://www.moonshot.cn/)
- [Documentation](https://platform.moonshot.cn/docs/intro#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90%E6%A8%A1%E5%9E%8B)

## Supported Features

### Supported Models

| Type | Models |
|------|--------|
| Chat Completions | moonshot-v1-8k, moonshot-v1-16k, moonshot-v1-128k |

### Unsupported Features

- **Prompt Playground**: Prompt playground is not supported for Moonshot models.

## Integration Guide

### Chat Completions Calls

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="moonshot",
    Authorization="$PROVIDER_API_KEY"
)

response = portkey.chat.completions.create(
    model="moonshot-v1-16k",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about AI."}
    ]
)
```

```Node node
import { Portkey } from "portkey-ai";

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "moonshot",
    Authorization: "$PROVIDER_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "moonshot-v1-16k",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "Tell me a joke about AI."}
    ]
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: moonshot" \
-H "Authorization: Bearer $PROVIDER_API_KEY" \
-d '{
  "model": "moonshot-v1-16k",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a joke about AI."}
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
        provider="moonshot",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.chat.completions.create(
    model="moonshot-v1-16k",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about AI."}
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
        provider: "moonshot",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await client.chat.completions.create({
    model: "moonshot-v1-16k",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "Tell me a joke about AI."}
    ]
});
```

</CodeGroup>

### Integration via Virtual Key

1. **Generate a Virtual Key**
   Get your API key from Moonshot and add it to Portkey to create a virtual key.

   You can get your Moonshot API key from the Moonshot website.

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
    model="moonshot-v1-16k",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about AI."}
    ]
)
```

```Node node
import { Portkey } from "portkey-ai";

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    virtualKey: "$VIRTUAL_KEY"
});

const response = await portkey.chat.completions.create({
    model: "moonshot-v1-16k",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "Tell me a joke about AI."}
    ]
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-virtual-key: $VIRTUAL_KEY" \
-d '{
  "model": "moonshot-v1-16k",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", content": "Tell me a joke about AI."}
  ]
}'
```

```Python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="",  # Not needed when using virtual key
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        api_key="$PORTKEY_API_KEY",
        virtual_key="$VIRTUAL_KEY"
    )
)

response = client.chat.completions.create(
    model="moonshot-v1-16k",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about AI."}
    ]
)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const client = new OpenAI({
    apiKey: "",  // Not needed when using virtual key
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        apiKey: "$PORTKEY_API_KEY",
        virtualKey: "$VIRTUAL_KEY"
    })
});

const response = await client.chat.completions.create({
    model: "moonshot-v1-16k",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "Tell me a joke about AI."}
    ]
});
```

</CodeGroup>

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