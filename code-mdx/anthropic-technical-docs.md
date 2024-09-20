# Anthropic

**Portkey Provider Slug:** `anthropic`

## Overview

Anthropic's latest features and APIs are supported on Portkey. This document outlines the features, supported models, and integration methods available for Anthropic through the Portkey platform.

Most common models:
- claude-3-5-sonnet-20240620
- claude-3-opus-20240229
- claude-3-sonnet-20240229
- claude-3-haiku-20240307

## Quick Links

- [Anthropic Website](https://anthropic.com/)
- [Pricing](https://www.anthropic.com/pricing)
- [Documentation](https://docs.anthropic.com/en/api/getting-started)
- [Discord Community](https://anthropic.com/discord)

## Supported Features

### Supported Models

1. **Claude 3 & 3.1 Models (supports Vision capabilities)**
   Portkey supports all the latest Claude series of models by Anthropic.
   [Model List](https://docs.anthropic.com/en/docs/about-claude/models)

2. **Text Completions**
   Portkey supports all text completions models offered by Anthropic.
   [Legacy Models List](https://docs.anthropic.com/en/docs/about-claude/models#legacy-models)

### Anthropic-Specific Features

1. **Function / Tool Calling**
   Function calling allows you to connect models like Claude-3.5-Sonnet to external tools and systems.
   [Learn more](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)

2. **Parallel Function / Tool Calling**
   With this feature, you can generate multiple function calls in a single response.
   [Learn more](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#multiple-tool-example)

3. **Prompt Caching**
   Prompt caching optimizes your API usage by allowing resuming from specific prefixes in your prompts.
   [Learn more](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)

## Integration Guide

### Chat Completions Call

<CodeGroup>

```python Python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="anthropic",
    Authorization="$ANTHROPIC_API_KEY"
)

response = portkey.chat.completions.create(
    model="claude-3-5-sonnet-20240620",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    max_tokens=100
)
```

```js Node.js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "anthropic",
    Authorization: "$ANTHROPIC_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "claude-3-5-sonnet-20240620",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ],
    max_tokens: 100
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: anthropic" \
-H "Authorization: Bearer $ANTHROPIC_API_KEY" \
-d '{
  "model": "claude-3-5-sonnet-20240620",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
  ],
  "max_tokens": 100
}'
```

```python Anthropic Python SDK (via OpenAI)
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$ANTHROPIC_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="anthropic",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.chat.completions.create(
    model="claude-3-5-sonnet-20240620",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    max_tokens=100
)
```

```js Anthropic Node.js SDK (via OpenAI)
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const client = new OpenAI({
    apiKey: "$ANTHROPIC_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "anthropic",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await client.chat.completions.create({
    model: "claude-3-5-sonnet-20240620",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ],
    max_tokens: 100
});
```

</CodeGroup>

### Integration via Virtual Key

1. **Generate a Virtual Key**
   Get your API key from Anthropic and add it to Portkey to create a virtual key.
   You can get your Anthropic API key from the Anthropic website.

2. **Using the Virtual Key**

<CodeGroup>

```python Python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    virtual_key="$VIRTUAL_KEY"
)

response = portkey.chat.completions.create(
    model="claude-3-5-sonnet-20240620",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    max_tokens=100
)
```

```js Node.js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    virtualKey: "$VIRTUAL_KEY"
});

const response = await portkey.chat.completions.create({
    model: "claude-3-5-sonnet-20240620",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ],
    max_tokens: 100
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-virtual-key: $VIRTUAL_KEY" \
-d '{
  "model": "claude-3-5-sonnet-20240620",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
  ],
  "max_tokens": 100
}'
```

```python Anthropic Python SDK (via OpenAI)
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$VIRTUAL_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.chat.completions.create(
    model="claude-3-5-sonnet-20240620",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    max_tokens=100
)
```

```js Anthropic Node.js SDK (via OpenAI)
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const client = new OpenAI({
    apiKey: "$VIRTUAL_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await client.chat.completions.create({
    model: "claude-3-5-sonnet-20240620",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ],
    max_tokens: 100
});
```

</CodeGroup>

### Prompt Playground

Manage and test prompts for Anthropic models in the Prompt Library.

Note: Prompt Caching is coming soon on Portkey prompts playground.

<CodeGroup>

```python Python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="anthropic",
    Authorization="$ANTHROPIC_API_KEY"
)

response = portkey.chat.completions.create(
    model="claude-3-5-sonnet-20240620",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    max_tokens=100,
    prompt_id="PROMPT_ID_FROM_LIBRARY"
)
```

```js Node.js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "anthropic",
    Authorization: "$ANTHROPIC_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "claude-3-5-sonnet-20240620",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ],
    max_tokens: 100,
    promptId: "PROMPT_ID_FROM_LIBRARY"
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: anthropic" \
-H "Authorization: Bearer $ANTHROPIC_API_KEY" \
-H "x-portkey-prompt-id: PROMPT_ID_FROM_LIBRARY" \
-d '{
  "model": "claude-3-5-sonnet-20240620",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
  ],
  "max_tokens": 100
}'
```

</CodeGroup>

## Special Examples

### Tool Calling

<CodeGroup>

```python Python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="anthropic",
    Authorization="$ANTHROPIC_API_KEY"
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"]
                    }
                },
                "required": ["location"]
            }
        }
    }
]

response = portkey.chat.completions.create(
    model="claude-3-5-sonnet-20240620",
    messages=[
        {"role": "user", "content": "What's the weather like in Boston?"}
    ],
    tools=tools,
    tool_choice="auto"
)

print(response.choices[0].message)
```

```js Node.js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "anthropic",
    Authorization: "$ANTHROPIC_API_KEY"
});

const tools = [
    {
        type: "function",
        function: {
            name: "get_current_weather",
            description: "Get the current weather in a given location",
            parameters: {
                type: "object",
                properties: {
                    location: {
                        type: "string",
                        description: "The city and state, e.g. San Francisco, CA"
                    },
                    unit: {
                        type: "string",
                        enum: ["celsius", "fahrenheit"]
                    }
                },
                required: ["location"]
            }
        }
    }
];

const response = await portkey.chat.completions.create({
    model: "claude-3-5-sonnet-20240620",
    messages: [
        {role: "user", content: "What's the weather like in Boston?"}
    ],
    tools: tools,
    tool_choice: "auto"
});

console.log(response.choices[0].message);
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: anthropic" \
-H "Authorization: Bearer $ANTHROPIC_API_KEY" \
-d '{
  "model": "claude-3-5-sonnet-20240620",
  "messages": [
    {"role": "user", "content": "What'"'"'s the weather like in Boston?"}
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
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            },
            "unit": {
              "type": "string",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location"]
        }
      }
    }
  ],
  "tool_choice": "auto"
}'
```

</CodeGroup>

### Prompt Caching

<CodeGroup>

```python Python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="anthropic",
    Authorization="$ANTHROPIC_API_KEY"
)

response = portkey.chat.completions.create(
    model="claude-3-5-sonnet-20240620",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    max_tokens=100,
    cache_status=True,  # Enable cache status in the response
    cache_force_refresh=False  # Use cached response if available
)
```

```js Node.js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "anthropic",
    Authorization: "$ANTHROPIC_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "claude-3-5-sonnet-20240620",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ],
    max_tokens: 100,
    cacheStatus: true,  // Enable cache status in the response
    cacheForceRefresh: false  // Use cached response if available
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: anthropic" \
-H "Authorization: Bearer $ANTHROPIC_API_KEY" \
-H "x-portkey-cache-status: true" \
-H "x-portkey-cache-force-refresh: false" \
-d '{
  "model": "claude-3-5-sonnet-20240620",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
  ],
  "max_tokens": 100
}'
```

```python Anthropic Python SDK (via OpenAI)
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$ANTHROPIC_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="anthropic",
        api_key="$PORTKEY_API_KEY",
        cache_status="true",
        cache_force_refresh="false"
    )
)

response = client.chat.completions.create(
    model="claude-3-5-sonnet-20240620",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    max_tokens=100
)
```

```js Anthropic Node.js SDK (via OpenAI)
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const client = new OpenAI({
    apiKey: "$ANTHROPIC_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "anthropic",
        apiKey: "$PORTKEY_API_KEY",
        cacheStatus: "true",
        cacheForceRefresh: "false"
    })
});

const response = await client.chat.completions.create({
    model: "claude-3-5-sonnet-20240620",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ],
    max_tokens: 100
});
```

</CodeGroup>

## Portkey Capabilities

Portkey offers several advanced capabilities for managing your Anthropic integrations:

1. **Configure Routing**: Set up custom routing for your Anthropic requests. [Learn more](/docs/product/ai-gateway/routing)

2. **Add Metadata to Requests**: Enhance your Anthropic requests with additional metadata. [Learn more](/docs/product/observability/metadata)

3. **A/B Test Different Models**: Conduct A/B tests with various Anthropic models. [Learn more](/docs/product/ai-gateway/load-balance)

4. **Gain Insights to Requests**: Obtain detailed insights into your Anthropic API requests. [Learn more](/docs/product/observability/traces)

## Conclusion

This documentation provides a comprehensive guide to integrating Anthropic's AI models using Portkey. It covers various methods of integration, including direct API calls, virtual key usage, and special features like tool calling and prompt caching. For more detailed information or specific use cases, refer to the Anthropic and Portkey documentation linked throughout this guide.