# OpenAI

Integrate OpenAI LLMs into your applications with Portkey

**Portkey Provider Slug:** `openai`

## Overview

OpenAI offers a range of powerful language models and APIs that can be easily integrated into various applications through Portkey. This document outlines the features, supported models, and integration methods available for OpenAI through the Portkey platform.

Most common models:
- gpt-4o
- gpt-4o-mini
- o1-preview
- o1-mini
- gpt-4-turbo
- dall-e-3
- tts-1
- text-embedding-3-large
- whisper-1

## Quick Links

- [OpenAI Website](https://openai.com/)
- [Pricing](https://openai.com/pricing)
- [Documentation](https://platform.openai.com/docs/api-reference/introduction)
- [Discord Community](https://discord.com/invite/openai)

## Supported Features

### Supported Models

| Type | Description |
|------|-------------|
| Chat Completions | Portkey supports all chat models offered by OpenAI |
| Embed | Portkey supports all embedding models offered by OpenAI |
| Vision | Portkey supports all vision models offered by OpenAI |
| Audio Transcriptions | Portkey supports all Audio Transcription models offered by OpenAI |
| Audio Translations | Portkey supports all Audio Translation models offered by OpenAI |
| Create Speech | Portkey supports all text to speech models offered by OpenAI |
| Completions | Portkey supports all completions models offered by OpenAI |

[Full list of models and endpoint compatibility](https://platform.openai.com/docs/models/model-endpoint-compatibility)

### OpenAI-Specific Features

- **Function / Tool Calling**: Connect models like gpt-4o to external tools and systems. [Learn more](https://platform.openai.com/docs/guides/function-calling)
- **Parallel Function / Tool Calling**: Generate multiple function calls in a single response. [Learn more](https://platform.openai.com/docs/guides/function-calling/configuring-parallel-function-calling)
- **Structured Outputs**: Ensure the model generates responses that adhere to your supplied JSON Schema. [Learn more](https://docs.OpenAI.ai/structured-responses/structured-response-formatting)
- **Reproducible Outputs**: Control deterministic outputs. [Learn more](https://platform.openai.com/docs/advanced-usage/reproducible-outputs)
- **Reasoning**: Models that think before answering, producing a long internal chain of thought. [Learn more](https://platform.openai.com/docs/guides/reasoning)
- **Batch Processing**: Send asynchronous groups of requests with 50% lower costs and higher rate limits. [Learn more](https://platform.openai.com/docs/guides/batch)
- **Fine-tuning**: Train OpenAI's models on more examples than can fit in the prompt for better results. [Learn more](https://platform.openai.com/docs/guides/fine-tuning)

## Integration Guide

### Chat Completions

<CodeGroup>

```python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="openai",
    authorisation="$PROVIDER_API_KEY"
)

response = portkey.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].message.content)
```

```js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "openai",
    authorisation: "$PROVIDER_API_KEY"
});

async function main() {
    const response = await portkey.chat.completions.create({
        model: "gpt-4o-mini",
        messages: [
            {role: "system", content: "You are a helpful assistant."},
            {role: "user", content: "Hello, how are you?"}
        ]
    });

    console.log(response.choices[0].message.content);
}

main();
```

```bash
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: openai" \
  -H "Authorization: Bearer $PROVIDER_API_KEY" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hello, how are you?"}
    ]
  }'
```

</CodeGroup>

### Audio Transcription

<CodeGroup>

```python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="openai",
    authorisation="$PROVIDER_API_KEY"
)

with open("audio.mp3", "rb") as audio_file:
    response = portkey.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )

print(response.text)
```

```js
import Portkey from 'portkey-ai';
import fs from 'fs';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "openai",
    authorisation: "$PROVIDER_API_KEY"
});

async function main() {
    const audioFile = fs.createReadStream('audio.mp3');
    const response = await portkey.audio.transcriptions.create({
        model: "whisper-1",
        file: audioFile
    });

    console.log(response.text);
}

main();
```

```bash
curl https://api.portkey.ai/v1/audio/transcriptions \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: openai" \
  -H "Authorization: Bearer $PROVIDER_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F file=@"audio.mp3" \
  -F model="whisper-1"
```

</CodeGroup>

### Embeddings

<CodeGroup>

```python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="openai",
    authorisation="$PROVIDER_API_KEY"
)

response = portkey.embeddings.create(
    model="text-embedding-3-large",
    input="The quick brown fox jumps over the lazy dog"
)

print(response.data[0].embedding)
```

```js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "openai",
    authorisation: "$PROVIDER_API_KEY"
});

async function main() {
    const response = await portkey.embeddings.create({
        model: "text-embedding-3-large",
        input: "The quick brown fox jumps over the lazy dog"
    });

    console.log(response.data[0].embedding);
}

main();
```

```bash
curl https://api.portkey.ai/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: openai" \
  -H "Authorization: Bearer $PROVIDER_API_KEY" \
  -d '{
    "model": "text-embedding-3-large",
    "input": "The quick brown fox jumps over the lazy dog"
  }'
```

</CodeGroup>

### Image Generation

<CodeGroup>

```python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="openai",
    authorisation="$PROVIDER_API_KEY"
)

response = portkey.images.generate(
    model="dall-e-3",
    prompt="A cute baby sea otter",
    n=1,
    size="1024x1024"
)

print(response.data[0].url)
```

```js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "openai",
    authorisation: "$PROVIDER_API_KEY"
});

async function main() {
    const response = await portkey.images.generate({
        model: "dall-e-3",
        prompt: "A cute baby sea otter",
        n: 1,
        size: "1024x1024"
    });

    console.log(response.data[0].url);
}

main();
```

```bash
curl https://api.portkey.ai/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: openai" \
  -H "Authorization: Bearer $PROVIDER_API_KEY" \
  -d '{
    "model": "dall-e-3",
    "prompt": "A cute baby sea otter",
    "n": 1,
    "size": "1024x1024"
  }'
```

</CodeGroup>

### Integration via Virtual Key

1. **Generate a Virtual Key**
   Get your API key from OpenAI and add it to Portkey to create a virtual key.

   You can get your OpenAI API key from the OpenAI website [here](https://platform.openai.com/api-keys).

2. **Using the Virtual Key**

<CodeGroup>

```python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    virtual_key="$VIRTUAL_KEY"
)

response = portkey.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].message.content)
```

```js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    virtualKey: "$VIRTUAL_KEY"
});

async function main() {
    const response = await portkey.chat.completions.create({
        model: "gpt-4o-mini",
        messages: [
            {role: "system", content: "You are a helpful assistant."},
            {role: "user", content: "Hello, how are you?"}
        ]
    });

    console.log(response.choices[0].message.content);
}

main();
```

```bash
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-virtual-key: $VIRTUAL_KEY" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hello, how are you?"}
    ]
  }'
```

</CodeGroup>

### Prompt Playground

Manage and test prompts for OpenAI models in the Prompt Library.

<CodeGroup>

```python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="$PORTKEY_API_KEY",
    provider="openai",
    authorisation="$PROVIDER_API_KEY"
)

response = portkey.chat.completions.create(
    model="gpt-4o-mini",
    prompt_id="my-custom-prompt",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].message.content)
```

```js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
    apiKey: "$PORTKEY_API_KEY",
    provider: "openai",
    authorisation: "$PROVIDER_API_KEY"
});

async function main() {
    const response = await portkey.chat.completions.create({
        model: "gpt-4o-mini",
        promptSlug: "my-custom-prompt",
        messages: [
            {role: "user", content: "Hello, how are you?"}
        ]
    });

    console.log(response.choices[0].message.content);
}

main();
```

```bash
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: openai" \
  -H "Authorization: Bearer $PROVIDER_API_KEY" \
  -d '{
    "model": "gpt-4o-mini",
    "prompt_id": "my-custom-prompt",
    "messages": [
      {"role": "user", "content": "Hello, how are you?"}
    ]
  }'
```

</CodeGroup>

## Special Examples

### Using Vision Models

<CodeGroup>

```python
from portkey_ai import Portkey

portkey = Portkey(api_key="$PORTKEY_API_KEY", provider="openai")

response = portkey.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {"role": "user", "content": [
            {"type": "text", "text": "What's in this image?"},
            {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
        ]}
    ],
    max_tokens=300
)
```

```js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
  apiKey: '$PORTKEY_API_KEY',
  provider: 'openai'
});

const response = await portkey.chat.completions.create({
  model: 'gpt-4-vision-preview',
  messages: [
    {
      role: 'user',
      content: [
        { type: 'text', text: 'What\'s in this image?' },
        { type: 'image_url', image_url: { url: 'https://example.com/image.jpg' } }
      ]
    }
  ],
  max_tokens: 300
});
```
```bash
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: openai" \
  -d '{
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "What'\''s in this image?"},
          {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
        ]
      }
    ],
    "max_tokens": 300
  }'
```

</CodeGroup>

### Tool Calling

Use Portkey's APIs to make a run a tool calling pipeline for OpenAI models:

<CodeGroup>

```python
from portkey_ai import Portkey

portkey = Portkey(api_key="$PORTKEY_API_KEY", provider="openai")

response = portkey.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What's the weather like in Boston?"}],
    tools=[{
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
    }],
    tool_choice="auto"
)
```

```js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
  apiKey: '$PORTKEY_API_KEY',
  provider: 'openai'
});

const response = await portkey.chat.completions.create({
  model: 'gpt-4o',
  messages: [{ role: 'user', content: 'What\'s the weather like in Boston?' }],
  tools: [{
    type: 'function',
    function: {
      name: 'get_current_weather',
      description: 'Get the current weather in a given location',
      parameters: {
        type: 'object',
        properties: {
          location: { type: 'string', description: 'The city and state, e.g. San Francisco, CA' },
          unit: { type: 'string', enum: ['celsius', 'fahrenheit'] }
        },
        required: ['location']
      }
    }
  }],
  tool_choice: 'auto'
});
```

```bash
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: openai" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "What'\''s the weather like in Boston?"}],
    "tools": [{
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
    }],
    "tool_choice": "auto"
  }'
```

</CodeGroup>

### Structured Outputs

Use Portkey to observe your structured outputs requests to OpenAI:

Note: OpenAI Structured Outputs is not supported on Portkey prompts playground

<CodeGroup>

```python
from portkey_ai import Portkey

portkey = Portkey(api_key="$PORTKEY_API_KEY", provider="openai")

response = portkey.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Generate a JSON object with name, age, and occupation for a fictional person."}],
    response_format={"type": "json_object"}
)
```

```js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
  apiKey: '$PORTKEY_API_KEY',
  provider: 'openai'
});

const response = await portkey.chat.completions.create({
  model: 'gpt-4o',
  messages: [{ role: 'user', content: 'Generate a JSON object with name, age, and occupation for a fictional person.' }],
  response_format: { type: 'json_object' }
});
```

```bash
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: openai" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Generate a JSON object with name, age, and occupation for a fictional person."}],
    "response_format": {"type": "json_object"}
  }'
```

</CodeGroup>

### OpenAI JSON Mode

Use Portkey's Post Proxy APIs to make a call to OpenAI JSON Mode:

Note: OpenAI JSON Mode is not supported on Portkey prompts playground

<CodeGroup>

```python
from portkey_ai import Portkey

portkey = Portkey(api_key="$PORTKEY_API_KEY", provider="openai")

response = portkey.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Generate a JSON object with three random colors and their hexadecimal codes."}],
    response_format={"type": "json_object"}
)
```

```js
import Portkey from 'portkey-ai';

const portkey = new Portkey({
  apiKey: '$PORTKEY_API_KEY',
  provider: 'openai'
});

const response = await portkey.chat.completions.create({
  model: 'gpt-4o',
  messages: [{ role: 'user', content: 'Generate a JSON object with three random colors and their hexadecimal codes.' }],
  response_format: { type: 'json_object' }
});
```

```bash
curl https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: $PORTKEY_API_KEY" \
  -H "x-portkey-provider: openai" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Generate a JSON object with three random colors and their hexadecimal codes."}],
    "response_format": {"type": "json_object"}
  }'
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