---
title: 'Groq'
description: 'Integrate Groq LLMs into your applications with Portkey'
---

**Portkey Provider Slug:** `groq`

## Overview

Groq provides Large Language Models (LLMs) for integration into applications. This document outlines the features, supported models, and integration methods available for Groq through the Portkey platform.

Most common models:
- mixtral-8x7b-32768
- llama3-70b-8192

## Quick Links

- [Groq Website](https://groq.com)
- [Pricing](https://groq.com/pricing/)
- [Documentation](https://console.groq.com/docs/quickstart)
- [Discord Community](https://discord.gg/n8KtCjfAug)

## Supported Features

### Supported Models

| Type | Models |
|------|--------|
| Chat Completions | gemma2-9b-it, gemma-7b-it, llama-guard-3-8b, llama3-groq-8b-8192-tool-use-preview |
| Vision | llava-v1.5-7b-4096-preview |
| Content Moderation | llama-guard-3-8b |

[More models](https://console.groq.com/docs/models)

### Unsupported Models

- **Speech**: Portkey currently does not support the speech API for Groq models.

### Groq-Specific Features

- **Tool Calling**: Groq API endpoints support tool use for programmatic execution of specified operations through requests with explicitly defined operations. [Learn more](https://console.groq.com/docs/tool-use)

- **JSON Mode**: JSON mode is a feature that guarantees all chat completions are valid JSON. [Learn more](https://console.groq.com/docs/text-chat)

## Integration Guide

### Text Calls

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="groq",
    Authorization="$PROVIDER_API_KEY"
)

response = portkey.chat.completions.create(
    model="gemma-7b-it",
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
    provider: "groq",
    Authorization: "$PROVIDER_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "gemma-7b-it",
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
  -H "x-portkey-provider: groq" \
  -H "Authorization: Bearer $PROVIDER_API_KEY" \
  -d '{
    "model": "gemma-7b-it",
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
        provider="groq",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.chat.completions.create(
    model="gemma-7b-it",
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
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "groq",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await openai.chat.completions.create({
    model: "gemma-7b-it",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});

console.log(response.choices[0].message.content);
```

</CodeGroup>

### Vision Calls

<CodeGroup>

```Python python
from portkey_ai import Portkey
import base64

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="groq",
    Authorization="$PROVIDER_API_KEY"
)

with open("image.jpg", "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

response = portkey.chat.completions.create(
    model="llava-v1.5-7b-4096-preview",
    messages=[
        {"role": "user", "content": [
            {"type": "text", "text": "What's in this image?"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
        ]}
    ]
)

print(response.choices[0].message.content)
```

```Node node
import Portkey from 'portkey-ai';
import fs from 'fs';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "groq",
    Authorization: "$PROVIDER_API_KEY"
});

const image = fs.readFileSync('image.jpg', {encoding: 'base64'});

const response = await portkey.chat.completions.create({
    model: "llava-v1.5-7b-4096-preview",
    messages: [
        {role: "user", content: [
            {type: "text", text: "What's in this image?"},
            {type: "image_url", image_url: {url: `data:image/jpeg;base64,${image}`}}
        ]}
    ]
});

console.log(response.choices[0].message.content);
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: groq" \
  -H "Authorization: Bearer $PROVIDER_API_KEY" \
  -d '{
    "model": "llava-v1.5-7b-4096-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "What'\''s in this image?"},
          {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEASABIAAD/..."}}
        ]
      }
    ]
  }'
```

```Python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders
import base64

client = OpenAI(
    api_key="$PROVIDER_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="groq",
        api_key="$PORTKEY_API_KEY"
    )
)

with open("image.jpg", "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

response = client.chat.completions.create(
    model="llava-v1.5-7b-4096-preview",
    messages=[
        {"role": "user", "content": [
            {"type": "text", "text": "What's in this image?"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
        ]}
    ]
)

print(response.choices[0].message.content)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';
import fs from 'fs';

const openai = new OpenAI({
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "groq",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const image = fs.readFileSync('image.jpg', {encoding: 'base64'});

const response = await openai.chat.completions.create({
    model: "llava-v1.5-7b-4096-preview",
    messages: [
        {role: "user", content: [
            {type: "text", text: "What's in this image?"},
            {type: "image_url", image_url: {url: `data:image/jpeg;base64,${image}`}}
        ]}
    ]
});

console.log(response.choices[0].message.content);
```

</CodeGroup>

### Integration via Virtual Key

1. **Generate a Virtual Key**
   Get your API key from Groq and add it to Portkey to create a virtual key.

   You can get your Groq API key from the Groq console [here](https://console.groq.com/keys).

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
    model="gemma-7b-it",
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
    model: "gemma-7b-it",
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
    "model": "gemma-7b-it",
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
    model="gemma-7b-it",
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
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        apiKey: "$PORTKEY_API_KEY",
        virtualKey: "$VIRTUAL_KEY"
    })
});

const response = await openai.chat.completions.create({
    model: "gemma-7b-it",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});

console.log(response.choices[0].message.content);
```

</CodeGroup>

### Prompt Playground

Manage and test prompts for Groq models in the Prompt Library.

[Insert screenshot of Prompt Playground here]

#### Using Prompts from the Prompt Library

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="groq",
    Authorization="$PROVIDER_API_KEY"
)

response = portkey.chat.completions.create(
    model="gemma-7b-it",
    prompt_id="my-custom-prompt",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)
```

```Node node
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "groq",
    Authorization: "$PROVIDER_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "gemma-7b-it",
    promptSlug: "my-custom-prompt",
    messages: [
        {role: "user", content: "What is the capital of France?"}
    ]
});

console.log(response.choices[0].message.content);
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: groq" \
  -H "Authorization: Bearer $PROVIDER_API_KEY" \
  -d '{
    "model": "gemma-7b-it",
    "prompt_id": "my-custom-prompt",
    "messages": [
      {"role": "user", "content": "What is the capital of France?"}
    ]
  }'
```

```Python OpenAI Python SDK
# Not supported
```

```Node OpenAI Node SDK
// Not supported
```

</CodeGroup>

### Special Example: Chat Completion with Tool Call

<CodeGroup>

```Python python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="groq",
    Authorization="$PROVIDER_API_KEY"
)

response = portkey.chat.completions.create(
    model="llama3-groq-8b-8192-tool-use-preview",
    messages=[
        {"role": "user", "content": "What's the weather like in San Francisco?"},
    ],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"},
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                    },
                    "required": ["location"]
                }
            }
        }
    ],
    tool_choice="auto"
)

print(response.choices[0].message.content)
```

```Node node
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "groq",
    Authorization: "$PROVIDER_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "llama3-groq-8b-8192-tool-use-preview",
    messages: [
        {role: "user", content: "What's the weather like in San Francisco?"},
    ],
    tools: [
        {
            type: "function",
            function: {
                name: "get_current_weather",
                description: "Get the current weather in a given location",
                parameters: {
                    type: "object",
                    properties: {
                        location: {type: "string", description: "The city and state, e.g. San Francisco, CA"},
                        unit: {type: "string", enum: ["celsius", "fahrenheit"]}
                    },
                    required: ["location"]
                }
            }
        }
    ],
    toolChoice: "auto"
});

console.log(response.choices[0].message.content);
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: groq" \
  -H "Authorization: Bearer $PROVIDER_API_KEY" \
  -d '{
    "model": "llama3-groq-8b-8192-tool-use-preview",
    "messages": [
      {"role": "user", "content": "What'\''s the weather like in San Francisco?"}
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_current_weather",
          "description": "Get the current weather in a given location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"},
              "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            },
            "required": ["location"]
          }
        }
      }
    ],
    "tool_choice": "auto"
  }'
```

```Python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$PROVIDER_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="groq",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.chat.completions.create(
    model="llama3-groq-8b-8192-tool-use-preview",
    messages=[
        {"role": "user", "content": "What's the weather like in San Francisco?"},
    ],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"},
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                    },
                    "required": ["location"]
                }
            }
        }
    ],
    tool_choice="auto"
)

print(response.choices[0].message.content)
```

```Node OpenAI Node SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "groq",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await openai.chat.completions.create({
    model: "llama3-groq-8b-8192-tool-use-preview",
    messages: [
        {role: "user", content: "What's the weather like in San Francisco?"},
    ],
    tools: [
        {
            type: "function",
            function: {
                name: "get_current_weather",
                description: "Get the current weather in a given location",
                parameters: {
                    type: "object",
                    properties: {
                        location: {type: "string", description: "The city and state, e.g. San Francisco, CA"},
                        unit: {type: "string", enum: ["celsius", "fahrenheit"]}
                    },
                    required: ["location"]
                }
            }
        }
    ],
    toolChoice: "auto"
});

console.log(response.choices[0].message.content);
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