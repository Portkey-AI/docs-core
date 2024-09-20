# Fireworks AI

**Portkey Provider Slug:** `fireworks-ai`

## Overview

Fireworks AI is a generative AI inference platform that allows you to run and customize models. This document outlines the features, supported models, and integration methods available for Fireworks AI through the Portkey platform.

## Quick Links

- [Fireworks Website](https://fireworks.ai/)
- [Pricing](https://fireworks.ai/pricing)
- [Documentation](https://docs.fireworks.ai/getting-started/introduction)
- [Discord Community](https://discord.com/invite/fireworks-ai)

## Supported Features

### Supported Models

| Type | Description |
|------|-------------|
| Chat Completions | Portkey supports the majority of chat models offered by Fireworks |
| Embed | Portkey supports the majority of embed models offered by Fireworks |
| Vision | Portkey supports the majority of vision models offered by Fireworks |

[View all supported models](https://fireworks.ai/models)

**Note:** Fireworks model names generally have an `accounts/fireworks/models/` prefix. For example, to use llama-v3p1-405b-instruct, you need to pass `accounts/fireworks/models/llama-v3p1-405b-instruct` as the model name.

### Unsupported Features

- Portkey currently doesn't support any speech endpoints provided by Fireworks.

### Fireworks-Specific Features

1. **Function Calling**: The function calling API allows users to describe the set of tools/functions available to the model and have the model intelligently choose the right set of function calls to invoke given the context. [Learn more](https://docs.fireworks.ai/guides/function-calling)

2. **Grammar Mode**: Grammar mode allows you to specify a forced output schema for any Fireworks model via an extended BNF formal grammar (GBNF format). [Learn more](https://docs.fireworks.ai/structured-responses/structured-output-grammar-based)

3. **JSON Mode**: JSON mode enables you to provide a JSON schema to force any Fireworks language model to respond in a specific format. [Learn more](https://docs.fireworks.ai/structured-responses/structured-response-formatting)

## Integration Guide

### Chat Completions Call

<CodeGroup>

```python Python (Portkey SDK)
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="fireworks-ai",
    Authorization="$PROVIDER_API_KEY"
)

response = portkey.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
```

```javascript JavaScript (Portkey SDK)
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "fireworks-ai",
    Authorization: "$PROVIDER_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: fireworks-ai" \
  -H "Authorization: Bearer $PROVIDER_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/llama-v3p1-405b-instruct",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is the capital of France?"}
    ]
  }'
```

```python Python (OpenAI SDK)
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

client = OpenAI(
    api_key="$PROVIDER_API_KEY",
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="fireworks-ai",
        api_key="$PORTKEY_API_KEY"
    )
)

response = client.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", content: "What is the capital of France?"}
    ]
)
```

```javascript JavaScript (OpenAI SDK)
import OpenAI from 'openai';
import { PORTKEY_GATEWAY_URL, createHeaders } from 'portkey-ai';

const openai = new OpenAI({
    apiKey: "$PROVIDER_API_KEY",
    baseURL: PORTKEY_GATEWAY_URL,
    defaultHeaders: createHeaders({
        provider: "fireworks-ai",
        apiKey: "$PORTKEY_API_KEY"
    })
});

const response = await openai.chat.completions.create({
    model: "accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});
```

</CodeGroup>

### Integration via Virtual Key

1. **Generate a Virtual Key**
   Get your API key from Fireworks and add it to Portkey to create a virtual key.

   You can get your Fireworks API key from the [Fireworks website](https://fireworks.ai/).

2. **Using the Virtual Key**

<CodeGroup>

```python Python (Portkey SDK)
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    virtual_key="$VIRTUAL_KEY"
)

response = portkey.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
```

```javascript JavaScript (Portkey SDK)
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    virtualKey: "$VIRTUAL_KEY"
});

const response = await portkey.chat.completions.create({
    model: "accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-virtual-key: $VIRTUAL_KEY" \
  -d '{
    "model": "accounts/fireworks/models/llama-v3p1-405b-instruct",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is the capital of France?"}
    ]
  }'
```

```python Python (OpenAI SDK)
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
    model="accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
```

```javascript JavaScript (OpenAI SDK)
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
    model: "accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages: [
        {role: "system", content: "You are a helpful assistant."},
        {role: "user", content: "What is the capital of France?"}
    ]
});
```

</CodeGroup>

### Prompt Playground

Manage and test prompts for Fireworks models in the Prompt Library.

<CodeGroup>

```python Python (Portkey SDK)
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="fireworks-ai",
    Authorization="$PROVIDER_API_KEY"
)

response = portkey.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p1-405b-instruct",
    prompt_key="my-fireworks-prompt",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
```

```javascript JavaScript (Portkey SDK)
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "fireworks-ai",
    Authorization: "$PROVIDER_API_KEY"
});

const response = await portkey.chat.completions.create({
    model: "accounts/fireworks/models/llama-v3p1-405b-instruct",
    promptKey: "my-fireworks-prompt",
    messages: [
        {role: "user", content: "What is the capital of France?"}
    ]
});
```

```bash cURL
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: fireworks-ai" \
  -H "Authorization: Bearer $PROVIDER_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/llama-v3p1-405b-instruct",
    "prompt_key": "my-fireworks-prompt",
    "messages": [
      {"role": "user", "content": "What is the capital of France?"}
    ]
  }'
```

</CodeGroup>

## Special Examples

### Using Vision Models

<CodeGroup>

```python Python (Portkey SDK)
from portkey_ai import Portkey
import base64

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="fireworks-ai",
    Authorization="$PROVIDER_API_KEY"
)

with open("image.jpg", "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

response = portkey.chat.completions.create(
    model="accounts/fireworks/models/llava-v1.5-7b-4096-preview",
    messages=[
        {"role": "user", "content": "What's in this image?"},
        {"role": "system", "content": [{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}]}
    ]
)
```

```javascript JavaScript (Portkey SDK)
import Portkey from 'portkey-ai';
import fs from 'fs';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "fireworks-ai",
    Authorization: "$PROVIDER_API_KEY"
});

const imageBase64 = fs.readFileSync('image.jpg', {encoding: 'base64'});

const response = await portkey.chat.completions.create({
    model: "accounts/fireworks/models/llava-v1.5-7b-4096-preview",
    messages: [
        {role: "user", content: "What's in this image?"},
        {role: "system", content: [{type: "image_url", image_url: {url: `data:image/jpeg;base64,${imageBase64}`}}]}
    ]
});
```

</CodeGroup>

### Using Image Generation Models

<CodeGroup>

```python Python (Portkey SDK)
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="fireworks-ai",
    Authorization="$PROVIDER_API_KEY"
)

response = portkey.images.generate(
    model="accounts/fireworks/models/stable-diffusion-xl-1024-v1-0",
    prompt="A futuristic cityscape with flying cars",
    n=1,
    size="1024x1024"
)

image_url = response.data[0].url
```

```javascript JavaScript (Portkey SDK)
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "fireworks-ai",
    Authorization: "$PROVIDER_API_KEY"
});

const response = await portkey.images.generate({
    model: "accounts/fireworks/models/stable-diffusion-xl-1024-v1-0",
    prompt: "A futuristic cityscape with flying cars",
    n: 1,
    size: "1024x1024"
});

const imageUrl = response.data[0].url;
```

</CodeGroup>

### Fireworks Grammar Mode

**Note:** Fireworks Grammar Mode is not supported on Portkey prompts playground.

<CodeGroup>

```python Python (Portkey SDK)
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="fireworks-ai",
    Authorization="$PROVIDER_API_KEY"
)

grammar = """root ::= number "+" number "=" number
number ::= [0-9]+"""

response = portkey.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages=[
        {"role": "user", "content": "Give me a simple addition equation."}
    ],
    grammar=grammar
)
```

```javascript JavaScript (Portkey SDK)
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "fireworks-ai",
    Authorization: "$PROVIDER_API_KEY"
});

const grammar = `root ::= number "+" number "=" number
number ::= [0-9]+`;

const response = await portkey.chat.completions.create({
    model: "accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages: [
        {role: "user", content: "Give me a simple addition equation."}
    ],
    grammar: grammar
});
```

</CodeGroup>

### Fireworks JSON Mode

**Note:** Fireworks JSON Mode is not supported on Portkey prompts playground.

<CodeGroup>

```python Python (Portkey SDK)
from portkey_ai import Portkey
import json

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="fireworks-ai",
    Authorization="$PROVIDER_API_KEY"
)

json_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "city": {"type": "string"}
    },
    "required": ["name", "age", "city"]
}

response = portkey.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages=[
        {"role": "user", "content": "Generate a person's details."}
    ],
    response_format={"type": "json_object"},
    json_schema=json_schema
)

generated_json = json.loads(response.choices[0].message.content)
```

```javascript JavaScript (Portkey SDK)
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "fireworks-ai",
    Authorization: "$PROVIDER_API_KEY"
});

const jsonSchema = {
    type: "object",
    properties: {
        name: {type: "string"},
        age: {type: "integer"},
        city: {type: "string"}
    },
    required: ["name", "age", "city"]
};

const response = await portkey.chat.completions.create({
    model: "accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages: [
        {role: "user", content: "Generate a person's details."}
    ],
    response_format: {type: "json_object"},
    json_schema: jsonSchema
});

const generatedJson = JSON.parse(response.choices[0].message.content);
```

</CodeGroup>

## Explore Advanced Portkey Features

Portkey offers several advanced features to enhance your experience with Fireworks AI:

1. **Configure Routing**: Set up custom routing for your Fireworks requests. [Learn more](/docs/product/ai-gateway/routing)

2. **Add Metadata to Requests**: Enhance your Fireworks requests with additional metadata. [Learn more](/docs/product/observability/metadata)

3. **A/B Test Different Models**: Experiment with different Fireworks models to optimize performance. [Learn more](/docs/product/ai-gateway/load-balance)

4. **Gain Insights to Requests**: Analyze and understand your Fireworks requests in depth. [Learn more](/docs/product/observability/traces)

These features allow you to fine-tune your use of Fireworks AI models and gain valuable insights into your application's performance.

## Conclusion

This documentation provides a comprehensive guide to integrating Fireworks AI with Portkey. From basic chat completions to advanced features like Grammar Mode and JSON Mode, you now have the tools to leverage Fireworks AI's powerful models in your applications. Remember to refer to the Fireworks AI documentation for model-specific details and best practices.