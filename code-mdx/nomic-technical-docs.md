---
title: 'Nomic'
description: 'Integrate Nomic embedding models into your applications with Portkey'
---

**Portkey Provider Slug:** `nomic`

## Overview

Nomic provides embedding models that can be easily integrated into various applications through Portkey. This document outlines the features, supported models, and integration methods available for Nomic through the Portkey platform.

## Quick Links

- [Nomic Website](https://www.nomic.ai/)
- [Pricing](https://atlas.nomic.ai/#pricing)
- [Documentation](https://docs.nomic.ai/index.html)
- [Discord Community](https://discord.com/invite/myY5YDR8z8)

## Supported Features

### Supported Models

| Type | Models |
|------|--------|
| Text Embedding | nomic-embed-text-v1, nomic-embed-text-v1.5 |

[More models](https://docs.nomic.ai/atlas/models/text-embedding)

### Unsupported Models

- **Image Embedding**: Portkey currently does not support the image embedding API for Nomic models (nomic-embed-vision-v1, nomic-embed-vision-v1.5).

## Integration Guide

### Text Embedding Calls

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="nomic",
    Authorization="$PROVIDER_API_KEY"
)

response = portkey.embeddings.create(
    model="nomic-embed-text-v1",
    input=["Your text to embed"]
)

print(response.data[0].embedding)
```

```Node node
import { Portkey } from "portkey-ai";

const portkey = new Portkey({
  apiKey: "$PORTKEY_API_KEY",
  provider: "nomic",
  Authorization: "$PROVIDER_API_KEY"
});

const response = await portkey.embeddings.create({
  model: "nomic-embed-text-v1",
  input: ["Your text to embed"]
});

console.log(response.data[0].embedding);
```

```bash cURL
curl https://api.portkey.ai/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: nomic" \
  -H "Authorization: Bearer $PROVIDER_API_KEY" \
  -d '{
    "model": "nomic-embed-text-v1",
    "input": ["Your text to embed"]
  }'
```

```Python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$PROVIDER_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="nomic",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.embeddings.create(
    model="nomic-embed-text-v1",
    input=["Your text to embed"]
)

print(response.data[0].embedding)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
  apiKey: "$PROVIDER_API_KEY",
  baseURL: PORTKEY_GATEWAY_URL,
  defaultHeaders: createHeaders({
    provider: "nomic",
    apiKey: "$PORTKEY_API_KEY"
  })
});

const response = await openai.embeddings.create({
  model: "nomic-embed-text-v1",
  input: ["Your text to embed"]
});

console.log(response.data[0].embedding);
```

</CodeGroup>

### Integration via Virtual Key

1. **Generate a Virtual Key**
   Get your API key from Nomic and add it to Portkey to create a virtual key.

   You can get your Nomic API key from the Nomic website.

   [Insert screenshot of virtual key generation process here]

2. **Using the Virtual Key**

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    virtual_key="$VIRTUAL_KEY"
)

response = portkey.embeddings.create(
    model="nomic-embed-text-v1",
    input=["Your text to embed"]
)

print(response.data[0].embedding)
```

```Node node
import { Portkey } from "portkey-ai";

const portkey = new Portkey({
  apiKey: "$PORTKEY_API_KEY",
  virtualKey: "$VIRTUAL_KEY"
});

const response = await portkey.embeddings.create({
  model: "nomic-embed-text-v1",
  input: ["Your text to embed"]
});

console.log(response.data[0].embedding);
```

```bash cURL
curl https://api.portkey.ai/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-virtual-key: $VIRTUAL_KEY" \
  -d '{
    "model": "nomic-embed-text-v1",
    "input": ["Your text to embed"]
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

response = client.embeddings.create(
    model="nomic-embed-text-v1",
    input=["Your text to embed"]
)

print(response.data[0].embedding)
```

```Node OpenAI Node SDK
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

const response = await openai.embeddings.create({
  model: "nomic-embed-text-v1",
  input: ["Your text to embed"]
});

console.log(response.data[0].embedding);
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