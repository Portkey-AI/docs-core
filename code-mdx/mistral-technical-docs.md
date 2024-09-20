---
title: 'Mistral'
description: 'Integrate Mistral LLMs into your applications with Portkey'
---

**Portkey Provider Slug:** `mistral-ai`

## Overview

Mistral offers open and portable generative AI for developers and businesses. This document outlines the features, supported models, and integration methods available for Mistral through the Portkey platform.

## Quick Links

- [Mistral Website](https://mistral.ai/)
- [Documentation](https://docs.mistral.ai/)
- [Discord Community](https://discord.gg/mistralai)

## Supported Features

### Supported Models

| Type | Models |
|------|--------|
| Chat Completions | open-mistral-* family, open-mixtral-* family, pixtral-12b-2409, open-codestral-mamba, codestral-latest, mistral-large-latest, mistral-small-latest |
| Embed | mistral-embed |
| FIM Completion | codestral-2405, codestral-latest |

[More models](https://docs.mistral.ai/getting-started/models/)

### Unsupported Features

- FIM completions is currently not supported in Prompt Playground

### Mistral-Specific Features

- **Agents**: Rerank is supported through the Post Proxy call. Read more [here](/../link/to/post-proxy-dcoumentation)

## Integration Guide

### Chat Completions Calls

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="mistral-ai",
    authorisation="$PROVIDER_API_KEY"
)

response = portkey.chat.completions.create(
    model="open-mistral-7b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
)
```

```Node node
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "mistral-ai",
    authorisation: "$PROVIDER_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "open-mistral-7b",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "Hello, how are you?"}
    ]
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: mistral-ai" \
-H "Authorization: Bearer $PROVIDER_API_KEY" \
-d '{
  "model": "open-mistral-7b",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, how are you?"}
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
        provider="mistral-ai",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.chat.completions.create(
    model="open-mistral-7b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", content": "Hello, how are you?"}
    ]
)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "mistral-ai",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await openai.chat.completions.create({
    model: "open-mistral-7b",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "Hello, how are you?"}
    ]
});
```

</CodeGroup>

### Embeddings Calls

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="mistral-ai",
    authorisation="$PROVIDER_API_KEY"
)

response = portkey.embeddings.create(
    model="mistral-embed",
    input="The quick brown fox jumps over the lazy dog"
)
```

```Node node
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "mistral-ai",
    authorisation: "$PROVIDER_API_KEY"
});

const response = await portkey.embeddings.create({
    model: "mistral-embed",
    input: "The quick brown fox jumps over the lazy dog"
});
```

```bash cURL
curl https://api.portkey.ai/v1/embeddings \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: mistral-ai" \
-H "Authorization: Bearer $PROVIDER_API_KEY" \
-d '{
  "model": "mistral-embed",
  "input": "The quick brown fox jumps over the lazy dog"
}'
```

```Python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$PROVIDER_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="mistral-ai",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.embeddings.create(
    model="mistral-embed",
    input="The quick brown fox jumps over the lazy dog"
)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "mistral-ai",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await openai.embeddings.create({
    model: "mistral-embed",
    input: "The quick brown fox jumps over the lazy dog"
});
```

</CodeGroup>

### FIM Completion Calls

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="mistral-ai",
    authorisation="$PROVIDER_API_KEY"
)

response = portkey.completions.create(
    model="codestral-2405",
    prompt="def fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return <fim_prefix>fibonacci(n-1) + fibonacci(n-2)<fim_suffix>\n\nprint(fibonacci(10))",
    max_tokens=50
)
```

```Node node
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "mistral-ai",
    authorisation: "$PROVIDER_API_KEY"
});

const response = await portkey.completions.create({
    model: "codestral-2405",
    prompt: "def fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return <fim_prefix>fibonacci(n-1) + fibonacci(n-2)<fim_suffix>\n\nprint(fibonacci(10))",
    maxTokens: 50
});
```

```bash cURL
curl https://api.portkey.ai/v1/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: mistral-ai" \
-H "Authorization: Bearer $PROVIDER_API_KEY" \
-d '{
  "model": "codestral-2405",
  "prompt": "def fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return <fim_prefix>fibonacci(n-1) + fibonacci(n-2)<fim_suffix>\n\nprint(fibonacci(10))",
  "max_tokens": 50
}'
```

```Python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$PROVIDER_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="mistral-ai",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.completions.create(
    model="codestral-2405",
    prompt="def fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return <fim_prefix>fibonacci(n-1) + fibonacci(n-2)<fim_suffix>\n\nprint(fibonacci(10))",
    max_tokens=50
)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "mistral-ai",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await openai.completions.create({
    model: "codestral-2405",
    prompt: "def fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return <fim_prefix>fibonacci(n-1) + fibonacci(n-2)<fim_suffix>\n\nprint(fibonacci(10))",
    maxTokens: 50
});
```

</CodeGroup>

### Integration via Virtual Key

1. **Generate a Virtual Key**
   Get your API key from Mistral and add it to Portkey to create a virtual key.

   You can get your Mistral API key from the Mistral website.

   [Insert screenshot of virtual key generation process here]

2. **Using the Virtual Key**

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    virtual_key="$VIRTUAL_KEY"
)

response = portkey.completions.create(
    model="codestral-2405",
    prompt="def fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return <fim_prefix>fibonacci(n-1) + fibonacci(n-2)<fim_suffix>\n\nprint(fibonacci(10))",
    max_tokens=50
)
```

```Node node
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    virtualKey: "$VIRTUAL_KEY"
});

const response = await portkey.completions.create({
    model: "codestral-2405",
    prompt: "def fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return <fim_prefix>fibonacci(n-1) + fibonacci(n-2)<fim_suffix>\n\nprint(fibonacci(10))",
    maxTokens: 50
});
```

```bash cURL
curl https://api.portkey.ai/v1/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-virtual-key: $VIRTUAL_KEY" \
-d '{
  "model": "codestral-2405",
  "prompt": "def fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return <fim_prefix>fibonacci(n-1) + fibonacci(n-2)<fim_suffix>\n\nprint(fibonacci(10))",
  "max_tokens": 50
}'
```

```Python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$VIRTUAL_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.completions.create(
    model="codestral-2405",
    prompt="def fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return <fim_prefix>fibonacci(n-1) + fibonacci(n-2)<fim_suffix>\n\nprint(fibonacci(10))",
    max_tokens=50
)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
    apiKey: "$VIRTUAL_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await openai.completions.create({
    model: "codestral-2405",
    prompt: "def fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return <fim_prefix>fibonacci(n-1) + fibonacci(n-2)<fim_suffix>\n\nprint(fibonacci(10))",
    maxTokens: 50
});
```

</CodeGroup>

### Prompt Playground

Manage and test prompts for Mistral models in the Prompt Library.

[Insert screenshot of Prompt Playground here]

#### Using Prompts from the Prompt Library

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="mistral-ai",
    authorisation="$PROVIDER_API_KEY"
)

response = portkey.chat.completions.create(
    model="open-mistral-7b",
    prompt_id="my-saved-prompt",
    prompt_variables={
        "user_input": "What is the capital of France?"
    }
)
```

```Node node
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "mistral-ai",
    authorisation: "$PROVIDER_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "open-mistral-7b",
    promptSlug: "my-saved-prompt",
    promptVariables: {
        userInput: "What is the capital of France?"
    }
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: mistral-ai" \
-H "Authorization: Bearer $PROVIDER_API_KEY" \
-d '{
  "model": "open-mistral-7b",
  "prompt_id": "my-saved-prompt",
  "prompt_variables": {
    "user_input": "What is the capital of France?"
  }
}'
```

```Python OpenAI Python SDK
# Not supported
```

```Node OpenAI Node SDK
// Not supported
```

</CodeGroup>

## Special Examples

### Using Codestral endpoints using custom_host property

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="mistral-ai",
    authorisation="$PROVIDER_API_KEY",
    custom_host="https://api.codestral.ai"
)

response = portkey.completions.create(
    model="codestral-2405",
    prompt="def fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return <fim_prefix>fibonacci(n-1) + fibonacci(n-2)<fim_suffix>\n\nprint(fibonacci(10))",
    max_tokens=50
)
```

```Node node
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "mistral-ai",
    authorisation: "$PROVIDER_API_KEY",
    customHost: "https://api.codestral.ai"
});

const response = await portkey.completions.create({
    model: "codestral-2405",
    prompt: "def fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return <fim_prefix>fibonacci(n-1) + fibonacci(n-2)<fim_suffix>\n\nprint(fibonacci(10))",
    maxTokens: 50
});
```

```bash cURL
curl https://api.portkey.ai/v1/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: mistral-ai" \
-H "Authorization: Bearer $PROVIDER_API_KEY" \
-H "x-portkey-custom-host: https://api.codestral.ai" \
-d '{
  "model": "codestral-2405",
  "prompt": "def fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return <fim_prefix>fibonacci(n-1) + fibonacci(n-2)<fim_suffix>\n\nprint(fibonacci(10))",
  "max_tokens": 50
}'
```

```Python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$PROVIDER_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="mistral-ai",
        api_key="$PORTKEY_API_KEY",
        custom_host="https://api.codestral.ai"
    )
)

response = client.completions.create(
    model="codestral-2405",
    prompt="def fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return <fim_prefix>fibonacci(n-1) + fibonacci(n-2)<fim_suffix>\n\nprint(fibonacci(10))",
    max_tokens=50
)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "mistral-ai",
        apiKey: "$PORTKEY_API_KEY",
        customHost: "https://api.codestral.ai"
    })
});

const response = await openai.completions.create({
    model: "codestral-2405",
    prompt: "def fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return <fim_prefix>fibonacci(n-1) + fibonacci(n-2)<fim_suffix>\n\nprint(fibonacci(10))",
    maxTokens: 50
});
```

</CodeGroup>

## Explore Advanced Portkey Features

<CardGroup cols={2}>
  <Card title="Configure Routing" href="/docs/product/ai-gateway/routing">
    Configure routing for your Mistral requests
  </Card>
  <Card title="Add Metadata to Requests" href="/docs/product/observability/metadata">
    Add metadata to your Mistral requests
  </Card>
  <Card title="A/B Test Different Models" href="/docs/product/ai-gateway/load-balance">
    A/B test different models
  </Card>
  <Card title="Gain Insights to Requests" href="/docs/product/observability/traces">
    Gain insights to your Mistral requests
  </Card>
</CardGroup>