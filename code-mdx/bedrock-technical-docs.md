---
title: 'AWS Bedrock'
description: 'Integrate AWS Bedrock LLMs into your applications with Portkey'
---

**Portkey Provider Slug:** `bedrock`

## Overview

AWS Bedrock lets you access models from AI21, Anthropic, Meta, Cohere, and more over a single API. This document outlines the features, supported models, and integration methods available for AWS Bedrock through the Portkey platform.

Most common models:
- Claude 3.5 Sonnet
- Jurassic
- Titan
- Command R+
- Llama 3.1
- Mistral Large
- Stable Diffusion 3

## Quick Links

- [AWS Bedrock Website](https://aws.amazon.com/bedrock)
- [Pricing](https://aws.amazon.com/bedrock/pricing)
- [Documentation](https://docs.aws.amazon.com/bedrock/)
- [Community](https://community.aws/generative-ai)

## Supported Features

### Supported Models

| Type | Models |
|------|--------|
| Chat Completions | AI21 Labs: Jurassic-2 Mid, Jurassic-2 Ultra, Jamba-Instruct<br>Anthropic: Claude 3 Sonnet, Claude 3.5 Sonnet, Claude 3 Haiku, Claude 3 Opus<br>Cohere: Command R, Command R+<br>Mistral AI: Mistral Large |
| Text Models | Amazon: Titan Text G1 - Express, Titan Text G1 - Lite, Titan Text Premier, Titan Embeddings G1 - Text, Titan Text Embeddings V2<br>Anthropic: Claude, Claude Instant<br>Meta: Llama 2 Chat 13B, Llama 2 Chat 70B, Llama 3 8B Instruct, Llama 3 70B Instruct, Llama 3.1 8B Instruct, Llama 3.1 70B Instruct, Llama 3.1 405B Instruct<br>Mistral AI: Mistral 7B Instruct, Mixtral 8X7B Instruct, Mistral Large 2 (24.07), Mistral Small |
| Embed Models | Amazon: Titan Embeddings G1 - Text, Titan Text Embeddings V2, Titan Multimodal Embeddings G1<br>Cohere: Embed English, Embed Multilingual |
| Image Generations | Amazon: Titan Image Generator G1 V1, Titan Image Generator G1 V2<br>Stability AI: Stable Diffusion XL, Stable Image Ultra, Stable Image Core |

[More models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html)

### AWS Bedrock-Specific Features

- **Function / Tool Calling**: AWS Bedrock supports function and tool calling capabilities.
- **Parallel Function / Tool Calling**: Parallel function and tool calling is supported.
- **Stream Chat Completions**: AWS Bedrock allows streaming of chat completions.
- **Stream Completions**: Streaming of completions is supported.

## Integration Guide

### Chat Completions Call

<CodeGroup>

```python Python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="bedrock",
    aws_access_key_id="$AWS_ACCESS_KEY_ID",
    aws_secret_access_key="$AWS_SECRET_ACCESS_KEY",
    aws_region="us-east-1"
)

response = portkey.chat.completions.create(
    model="anthropic.claude-3-sonnet-20240229-v1:0",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me about AWS Bedrock."}
    ]
)

print(response.choices[0].message.content)
```

```js Node.js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: '$PORTKEY_API_KEY',
    provider: 'bedrock',
    awsAccessKeyId: '$AWS_ACCESS_KEY_ID',
    awsSecretAccessKey: '$AWS_SECRET_ACCESS_KEY',
    awsRegion: 'us-east-1'
});

const response = await portkey.chat.completions.create({
    model: 'anthropic.claude-3-sonnet-20240229-v1:0',
    messages: [
        { role: 'system', content: 'You are a helpful assistant.' },
        { role: 'user', content: 'Tell me about AWS Bedrock.' }
    ]
});

console.log(response.choices[0].message.content);
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: bedrock" \
-H "x-portkey-aws-access-key-id: $AWS_ACCESS_KEY_ID" \
-H "x-portkey-aws-secret-access-key: $AWS_SECRET_ACCESS_KEY" \
-H "x-portkey-aws-region: us-east-1" \
-d '{
  "model": "anthropic.claude-3-sonnet-20240229-v1:0",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me about AWS Bedrock."}
  ]
}'
```

```python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    base_url=PORTKEY_GATEWAY_URL,
    api_key="$AWS_SECRET_ACCESS_KEY",
    default_headers=createHeaders(
        provider="bedrock",
        api_key="$PORTKEY_API_KEY",
        aws_access_key_id="$AWS_ACCESS_KEY_ID",
        aws_secret_access_key="$AWS_SECRET_ACCESS_KEY",
        aws_region="us-east-1"
    )
)

response = client.chat.completions.create(
    model="anthropic.claude-3-sonnet-20240229-v1:0",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me about AWS Bedrock."}
    ]
)

print(response.choices[0].message.content)
```

```js OpenAI Node.js SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const client = new OpenAI({
    baseURL: PORTKEY_GATEWAY_URL,
    apiKey: '$AWS_SECRET_ACCESS_KEY',
    defaultHeaders: createHeaders({
        provider: 'bedrock',
        apiKey: '$PORTKEY_API_KEY',
        awsAccessKeyId: '$AWS_ACCESS_KEY_ID',
        awsSecretAccessKey: '$AWS_SECRET_ACCESS_KEY',
        awsRegion: 'us-east-1'
    })
});

const response = await client.chat.completions.create({
    model: 'anthropic.claude-3-sonnet-20240229-v1:0',
    messages: [
        { role: 'system', content: 'You are a helpful assistant.' },
        { role: 'user', content: 'Tell me about AWS Bedrock.' }
    ]
});

console.log(response.choices[0].message.content);
```

</CodeGroup>

### Embedding Call

<CodeGroup>

```python Python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="bedrock",
    aws_access_key_id="$AWS_ACCESS_KEY_ID",
    aws_secret_access_key="$AWS_SECRET_ACCESS_KEY",
    aws_region="us-east-1"
)

response = portkey.embeddings.create(
    model="cohere.embed-english-v3",
    input="AWS Bedrock is a fully managed service for foundation models."
)

print(response.data[0].embedding)
```

```js Node.js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: '$PORTKEY_API_KEY',
    provider: 'bedrock',
    awsAccessKeyId: '$AWS_ACCESS_KEY_ID',
    awsSecretAccessKey: '$AWS_SECRET_ACCESS_KEY',
    awsRegion: 'us-east-1'
});

const response = await portkey.embeddings.create({
    model: 'cohere.embed-english-v3',
    input: 'AWS Bedrock is a fully managed service for foundation models.'
});

console.log(response.data[0].embedding);
```

```bash cURL
curl https://api.portkey.ai/v1/embeddings \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: bedrock" \
-H "x-portkey-aws-access-key-id: $AWS_ACCESS_KEY_ID" \
-H "x-portkey-aws-secret-access-key: $AWS_SECRET_ACCESS_KEY" \
-H "x-portkey-aws-region: us-east-1" \
-d '{
  "model": "cohere.embed-english-v3",
  "input": "AWS Bedrock is a fully managed service for foundation models."
}'
```

```python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    base_url=PORTKEY_GATEWAY_URL,
    api_key="$AWS_SECRET_ACCESS_KEY",
    default_headers=createHeaders(
        provider="bedrock",
        api_key="$PORTKEY_API_KEY",
        aws_access_key_id="$AWS_ACCESS_KEY_ID",
        aws_secret_access_key="$AWS_SECRET_ACCESS_KEY",
        aws_region="us-east-1"
    )
)

response = client.embeddings.create(
    model="cohere.embed-english-v3",
    input="AWS Bedrock is a fully managed service for foundation models."
)

print(response.data[0].embedding)
```

```js OpenAI Node.js SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const client = new OpenAI({
    baseURL: PORTKEY_GATEWAY_URL,
    apiKey: '$AWS_SECRET_ACCESS_KEY',
    defaultHeaders: createHeaders({
        provider: 'bedrock',
        apiKey: '$PORTKEY_API_KEY',
        awsAccessKeyId: '$AWS_ACCESS_KEY_ID',
        awsSecretAccessKey: '$AWS_SECRET_ACCESS_KEY',
        awsRegion: 'us-east-1'
    })
});

const response = await client.embeddings.create({
    model: 'cohere.embed-english-v3',
    input: 'AWS Bedrock is a fully managed service for foundation models.'
});

console.log(response.data[0].embedding);
```

</CodeGroup>

### Image Generation Call

<CodeGroup>

```python Python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="bedrock",
    aws_access_key_id="$AWS_ACCESS_KEY_ID",
    aws_secret_access_key="$AWS_SECRET_ACCESS_KEY",
    aws_region="us-east-1"
)

response = portkey.images.generate(
    model="stability.stable-diffusion-xl-v1",
    prompt="A serene landscape with mountains and a lake",
    n=1,
    size="1024x1024"
)

print(response.data[0].url)
```

```js Node.js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: '$PORTKEY_API_KEY',
    provider: 'bedrock',
    awsAccessKeyId: '$AWS_ACCESS_KEY_ID',
    awsSecretAccessKey: '$AWS_SECRET_ACCESS_KEY',
    awsRegion: 'us-east-1'
});

const response = await portkey.images.generate({
    model: 'stability.stable-diffusion-xl-v1',
    prompt: 'A serene landscape with mountains and a lake',
    n: 1,
    size: '1024x1024'
});

console.log(response.data[0].url);
```

```bash cURL
curl https://api.portkey.ai/v1/images/generations \
-H "Content-Type: application/json" \
-H "x-portkey-api-key: $PORTKEY_API_KEY" \
-H "x-portkey-provider: bedrock" \
-H "x-portkey-aws-access-key-id: $AWS_ACCESS_KEY_ID" \
-H "x-portkey-aws-secret-access-key: $AWS_SECRET_ACCESS_KEY" \
-H "x-portkey-aws-region: us-east-1" \
-d '{
  "model": "stability.stable-diffusion-xl-v1",
  "prompt": "A serene landscape with mountains and a lake",
  "n": 1,
  "size": "1024x1024"
}'
```

```python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    base_url=PORTKEY_GATEWAY_URL,
    api_key="$AWS_SECRET_ACCESS_KEY",
    default_headers=createHeaders(
        provider="bedrock",
        api_key="$PORTKEY_API_KEY",
        aws_access_key_id="$AWS_ACCESS_KEY_ID",
        aws_secret_access_key="$AWS_SECRET_ACCESS_KEY",
        aws_region="us-east-1"
    )
)

response = client.images.generate(
    model="stability.stable-diffusion-xl-v1",
    prompt="A serene landscape with mountains and a lake",
    n=1,
    size="1024x1024"
)

print(response.data[0].url)
```

```js OpenAI Node.js SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const client = new OpenAI({
    baseURL: PORTKEY_GATEWAY_URL,
    apiKey: '$AWS_SECRET_ACCESS_KEY',
    defaultHeaders: createHeaders({
        provider: 'bedrock',
        apiKey: '$PORTKEY_API_KEY',
        awsAccessKeyId: '$AWS_ACCESS_KEY_ID',
        awsSecretAccessKey: '$AWS_SECRET_ACCESS_KEY',
        awsRegion: 'us-east-1'
    })
});

const response = await client.images.generate({
    model: 'stability.stable-diffusion-xl-v1',
    prompt: 'A serene landscape with mountains and a lake',
    n: 1,
    import Portkey from 'portkey-ai';

const portkey = new Portkey({
  apiKey: '$PORTKEY_API_KEY',
  provider: 'bedrock',
  awsAccessKeyId: '$AWS_ACCESS_KEY_ID',
  awsSecretAccessKey: '$AWS_SECRET_ACCESS_KEY',
  awsRegion: '$AWS_REGION'
});

function getCurrentWeather(location, unit = 'fahrenheit') {
  // Simulated weather function
  return `The current weather in ${location} is 72°${unit[0].toUpperCase()}`;
}

async function main() {
  const response = await portkey.chat.completions.create({
    model: 'anthropic.claude-3-sonnet-20240229-v1:0',
    messages: [{ role: 'user', content: "What's the weather like in San Francisco?" }],
    tools: [{
      type: 'function',
      function: {
        name: 'getCurrentWeather',
        description: 'Get the current weather in a given location',
        parameters: {
          type: 'object',
          properties: {
            location: { type: 'string' },
            unit: { type: 'string', enum: ['celsius', 'fahrenheit'] }
          },
          required: ['location']
        }
      }
    }]
  });

  if (response.choices[0].message.tool_calls) {
    const toolCall = response.choices[0].message.tool_calls[0];
    const functionName = toolCall.function.name;
    const functionArgs = JSON.parse(toolCall.function.arguments);

    if (functionName === 'getCurrentWeather') {
      const weatherInfo = getCurrentWeather(functionArgs.location, functionArgs.unit);
      console.log(`Weather info: ${weatherInfo}`);
    }
  } else {
    console.log(response.choices[0].message.content);
  }
}

main();
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: bedrock" \
  -H "x-portkey-aws-access-key-id: $AWS_ACCESS_KEY_ID" \
  -H "x-portkey-aws-secret-access-key: $AWS_SECRET_ACCESS_KEY" \
  -H "x-portkey-aws-region: $AWS_REGION" \
  -d '{
    "model": "anthropic.claude-3-sonnet-20240229-v1:0",
    "messages": [
      {"role": "user", "content": "What'"'"'s the weather like in San Francisco?"}
    ],
    "tools": [{
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {"type": "string"},
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
          },
          "required": ["location"]
        }
      }
    }]
  }'
```

```python OpenAI Python SDK
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$AWS_SECRET_ACCESS_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="bedrock",
        api_key="$PORTKEY_API_KEY",
        aws_access_key_id="$AWS_ACCESS_KEY_ID",
        aws_secret_access_key="$AWS_SECRET_ACCESS_KEY",
        aws_region="$AWS_REGION"
    )
)

def get_current_weather(location, unit="fahrenheit"):
    # Simulated weather function
    return f"The current weather in {location} is 72°{unit[0].upper()}"

response = client.chat.completions.create(
    model="anthropic.claude-3-sonnet-20240229-v1:0",
    messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}],
    tools=[{
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["location"]
            }
        }
    }]
)

if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    function_name = tool_call.function.name
    function_args = eval(tool_call.function.arguments)
    
    if function_name == "get_current_weather":
        weather_info = get_current_weather(**function_args)
        print(f"Weather info: {weather_info}")
else:
    print(response.choices[0].message.content)
```

```js OpenAI Node.js SDK
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const client = new OpenAI({
  apiKey: '$AWS_SECRET_ACCESS_KEY',
  baseURL: PORTKEY_GATEWAY_URL,
  defaultHeaders: createHeaders({
    provider: 'bedrock',
    apiKey: '$PORTKEY_API_KEY',
    awsAccessKeyId: '$AWS_ACCESS_KEY_ID',
    awsSecretAccessKey: '$AWS_SECRET_ACCESS_KEY',
    awsRegion: '$AWS_REGION'
  })
});

function getCurrentWeather(location, unit = 'fahrenheit') {
  // Simulated weather function
  return `The current weather in ${location} is 72°${unit[0].toUpperCase()}`;
}

async function main() {
  const response = await client.chat.completions.create({
    model: 'anthropic.claude-3-sonnet-20240229-v1:0',
    messages: [{ role: 'user', content: "What's the weather like in San Francisco?" }],
    tools: [{
      type: 'function',
      function: {
        name: 'getCurrentWeather',
        description: 'Get the current weather in a given location',
        parameters: {
          type: 'object',
          properties: {
            location: { type: 'string' },
            unit: { type: 'string', enum: ['celsius', 'fahrenheit'] }
          },
          required: ['location']
        }
      }
    }]
  });

  if (response.choices[0].message.tool_calls) {
    const toolCall = response.choices[0].message.tool_calls[0];
    const functionName = toolCall.function.name;
    const functionArgs = JSON.parse(toolCall.function.arguments);

    if (functionName === 'getCurrentWeather') {
      const weatherInfo = getCurrentWeather(functionArgs.location, functionArgs.unit);
      console.log(`Weather info: ${weatherInfo}`);
    }
  } else {
    console.log(response.choices[0].message.content);
  }
}

main();
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