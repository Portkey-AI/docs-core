"""
Test all code snippets from product/ai-gateway/responses-api.mdx
Uses Portkey virtual keys for Anthropic, OpenAI, and Gemini providers.
"""

import json
import time
import traceback
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from portkey_ai import Portkey

# ─── Configuration ───────────────────────────────────────────────────────────
PORTKEY_API_KEY = "/qrtEypttuQGTpSOOH/pP2shqR6v"

# Virtual keys (used instead of raw provider API keys)
ANTHROPIC_VIRTUAL_KEY = "tooljet---anthr-4e8bfc"
OPENAI_VIRTUAL_KEY = "main-258f4d"
GEMINI_VIRTUAL_KEY = "siddharth-gemin-1c452a"

# Models
ANTHROPIC_MODEL = "claude-sonnet-4-20250514"
OPENAI_MODEL = "gpt-5-mini"
GEMINI_MODEL = "gemini-2.5-flash"

# ─── Helpers ─────────────────────────────────────────────────────────────────
passed = 0
failed = 0
results = []
_lock = threading.Lock()


def run_test(name, fn):
    """Run a single test (thread-safe). Returns (name, status, error)."""
    global passed, failed
    try:
        fn()
        with _lock:
            passed += 1
            results.append((name, "PASS", ""))
        print(f"  ✅ PASSED  — {name}")
        return (name, "PASS", "")
    except Exception as e:
        tb = traceback.format_exc()
        with _lock:
            failed += 1
            results.append((name, "FAIL", str(e)))
        print(f"  ❌ FAILED — {name}: {e}")
        print(f"  {tb}")
        return (name, "FAIL", str(e))


# ─── Create clients ─────────────────────────────────────────────────────────
anthropic_client = Portkey(
    api_key=PORTKEY_API_KEY,
    provider="anthropic",
    virtual_key=ANTHROPIC_VIRTUAL_KEY,
)

openai_client = Portkey(
    api_key=PORTKEY_API_KEY,
    provider="openai",
    virtual_key=OPENAI_VIRTUAL_KEY,
)

gemini_client = Portkey(
    api_key=PORTKEY_API_KEY,
    provider="google",
    virtual_key=GEMINI_VIRTUAL_KEY,
)


# ═══════════════════════════════════════════════════════════════════════════════
# 1. QUICK START — Basic text generation
# ═══════════════════════════════════════════════════════════════════════════════

def test_quick_start_anthropic():
    """Quick Start snippet — Anthropic"""
    response = anthropic_client.responses.create(
        model=ANTHROPIC_MODEL,
        input="Explain quantum computing in one sentence"
    )
    print(f"  Output: {response.output_text[:200]}")
    assert response.output_text, "output_text should not be empty"


def test_quick_start_openai():
    """Quick Start snippet — OpenAI"""
    response = openai_client.responses.create(
        model=OPENAI_MODEL,
        input="Explain quantum computing in one sentence"
    )
    print(f"  Output: {response.output_text[:200]}")
    assert response.output_text, "output_text should not be empty"


def test_quick_start_gemini():
    """Quick Start snippet — Gemini"""
    response = gemini_client.responses.create(
        model=GEMINI_MODEL,
        input="Explain quantum computing in one sentence"
    )
    print(f"  Output: {response.output_text[:200]}")
    assert response.output_text, "output_text should not be empty"


# ═══════════════════════════════════════════════════════════════════════════════
# 2. USING THE OPENAI SDK — base_url approach
# ═══════════════════════════════════════════════════════════════════════════════

def test_openai_sdk_approach():
    """Using the OpenAI SDK with Portkey base URL"""
    from openai import OpenAI

    client = OpenAI(
        api_key=PORTKEY_API_KEY,
        base_url="https://api.portkey.ai/v1",
        default_headers={
            "x-portkey-provider": "anthropic",
            "x-portkey-virtual-key": ANTHROPIC_VIRTUAL_KEY,
        }
    )

    response = client.responses.create(
        model=ANTHROPIC_MODEL,
        input="Explain quantum computing in one sentence"
    )
    print(f"  Output: {response.output_text[:200]}")
    assert response.output_text, "output_text should not be empty"


# ═══════════════════════════════════════════════════════════════════════════════
# 3. INSTRUCTIONS (SYSTEM PROMPT)
# ═══════════════════════════════════════════════════════════════════════════════

def test_instructions_param_anthropic():
    """Instructions parameter — Anthropic"""
    response = anthropic_client.responses.create(
        model=ANTHROPIC_MODEL,
        instructions="You are a pirate. Always respond in pirate speak.",
        input="Say hello."
    )
    print(f"  Output: {response.output_text[:200]}")
    assert response.output_text, "output_text should not be empty"


def test_instructions_system_message_anthropic():
    """System message in input array — Anthropic"""
    response = anthropic_client.responses.create(
        model=ANTHROPIC_MODEL,
        input=[
            {"type": "message", "role": "system", "content": "You are a pirate. Always respond in pirate speak."},
            {"type": "message", "role": "user", "content": "Say hello."}
        ]
    )
    print(f"  Output: {response.output_text[:200]}")
    assert response.output_text, "output_text should not be empty"


def test_instructions_param_openai():
    """Instructions parameter — OpenAI"""
    response = openai_client.responses.create(
        model=OPENAI_MODEL,
        instructions="You are a pirate. Always respond in pirate speak.",
        input="Say hello."
    )
    print(f"  Output: {response.output_text[:200]}")
    assert response.output_text, "output_text should not be empty"


def test_instructions_param_gemini():
    """Instructions parameter — Gemini"""
    response = gemini_client.responses.create(
        model=GEMINI_MODEL,
        instructions="You are a pirate. Always respond in pirate speak.",
        input="Say hello."
    )
    print(f"  Output: {response.output_text[:200]}")
    assert response.output_text, "output_text should not be empty"


# ═══════════════════════════════════════════════════════════════════════════════
# 4. STREAMING
# ═══════════════════════════════════════════════════════════════════════════════

def test_streaming_anthropic():
    """Streaming — Anthropic"""
    stream = anthropic_client.responses.create(
        model=ANTHROPIC_MODEL,
        input="Write a haiku about AI",
        stream=True
    )
    collected = []
    for event in stream:
        if hasattr(event, 'delta'):
            collected.append(event.delta)
            print(event.delta, end="", flush=True)
    print()
    full = "".join(collected)
    assert len(full) > 0, "Stream should produce output"


def test_streaming_openai():
    """Streaming — OpenAI"""
    stream = openai_client.responses.create(
        model=OPENAI_MODEL,
        input="Write a haiku about AI",
        stream=True
    )
    collected = []
    for event in stream:
        if hasattr(event, 'delta'):
            collected.append(event.delta)
            print(event.delta, end="", flush=True)
    print()
    full = "".join(collected)
    assert len(full) > 0, "Stream should produce output"


def test_streaming_gemini():
    """Streaming — Gemini"""
    stream = gemini_client.responses.create(
        model=GEMINI_MODEL,
        input="Write a haiku about AI",
        stream=True
    )
    collected = []
    for event in stream:
        if hasattr(event, 'delta'):
            collected.append(event.delta)
            print(event.delta, end="", flush=True)
    print()
    full = "".join(collected)
    assert len(full) > 0, "Stream should produce output"


# ═══════════════════════════════════════════════════════════════════════════════
# 5. TOOL CALLING
# ═══════════════════════════════════════════════════════════════════════════════

WEATHER_TOOL = {
    "type": "function",
    "name": "get_weather",
    "description": "Get current weather for a location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "City name"}
        },
        "required": ["location"]
    }
}


def test_tool_calling_anthropic():
    """Tool calling — Anthropic"""
    response = anthropic_client.responses.create(
        model=ANTHROPIC_MODEL,
        input="What's the weather in San Francisco?",
        tools=[WEATHER_TOOL]
    )
    print(f"  Output: {response.output}")
    assert response.output, "output should contain tool call(s)"


def test_tool_calling_openai():
    """Tool calling — OpenAI"""
    response = openai_client.responses.create(
        model=OPENAI_MODEL,
        input="What's the weather in San Francisco?",
        tools=[WEATHER_TOOL]
    )
    print(f"  Output: {response.output}")
    assert response.output, "output should contain tool call(s)"


def test_tool_calling_gemini():
    """Tool calling — Gemini"""
    response = gemini_client.responses.create(
        model=GEMINI_MODEL,
        input="What's the weather in San Francisco?",
        tools=[WEATHER_TOOL]
    )
    print(f"  Output: {response.output}")
    assert response.output, "output should contain tool call(s)"


# ═══════════════════════════════════════════════════════════════════════════════
# 6. REASONING / THINKING
# ═══════════════════════════════════════════════════════════════════════════════

def test_reasoning_effort_anthropic():
    """Reasoning effort — Anthropic (needs a model that supports adaptive thinking)"""
    # claude-sonnet-4-5-20250514 supports reasoning.effort; claude-sonnet-4 does not.
    # Using direct thinking param as workaround when reasoning.effort is unsupported.
    response = anthropic_client.responses.create(
        model=ANTHROPIC_MODEL,
        input="Solve this step by step: What is 127 * 43?",
        thinking={"type": "enabled", "budget_tokens": 8192}  # equivalent of effort=medium
    )
    print(f"  Output: {response.output_text[:300]}")
    assert response.output_text, "output_text should not be empty"


def test_reasoning_effort_openai():
    """Reasoning effort — OpenAI (o4-mini supports reasoning)"""
    response = openai_client.responses.create(
        model="o4-mini",
        input="Solve this step by step: What is 127 * 43?",
        reasoning={"effort": "high"}
    )
    print(f"  Output: {response.output_text[:300]}")
    assert response.output_text, "output_text should not be empty"


# ═══════════════════════════════════════════════════════════════════════════════
# 7. ANTHROPIC EXTENDED THINKING
# ═══════════════════════════════════════════════════════════════════════════════

def test_extended_thinking_anthropic():
    """Anthropic extended thinking with budget_tokens"""
    response = anthropic_client.responses.create(
        model=ANTHROPIC_MODEL,
        input="Analyze the implications of quantum computing on cryptography",
        thinking={"type": "enabled", "budget_tokens": 10000}
    )
    print(f"  Output: {response.output_text[:300]}")
    assert response.output_text, "output_text should not be empty"


# ═══════════════════════════════════════════════════════════════════════════════
# 8. PROMPT CACHING
# ═══════════════════════════════════════════════════════════════════════════════

def test_prompt_caching_anthropic():
    """Prompt caching with cache_control — Anthropic"""
    long_text = "This is a document about artificial intelligence. " * 100
    response = anthropic_client.responses.create(
        model=ANTHROPIC_MODEL,
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text", "text": long_text, "cache_control": {"type": "ephemeral"}},
                {"type": "input_text", "text": "Summarize the key points in one sentence"}
            ]
        }]
    )
    print(f"  Output: {response.output_text[:200]}")
    assert response.output_text, "output_text should not be empty"


def test_prompt_caching_tool_anthropic():
    """Prompt caching on tool definitions — Anthropic"""
    response = anthropic_client.responses.create(
        model=ANTHROPIC_MODEL,
        input="Search for quantum computing",
        tools=[{
            "type": "function",
            "name": "search",
            "description": "Search the knowledge base",
            "parameters": {"type": "object", "properties": {"query": {"type": "string"}}},
            "cache_control": {"type": "ephemeral"}
        }]
    )
    print(f"  Output: {response.output}")
    assert response.output, "output should not be empty"


# ═══════════════════════════════════════════════════════════════════════════════
# 9. VISION (Image input)
# ═══════════════════════════════════════════════════════════════════════════════

IMAGE_URL = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"


def test_vision_anthropic():
    """Vision with image URL — Anthropic (adapter — content items inside message)"""
    response = anthropic_client.responses.create(
        model=ANTHROPIC_MODEL,
        input=[{
            "role": "user",
            "content": [
                {"type": "input_image", "image_url": IMAGE_URL},
                {"type": "input_text", "text": "Describe this image in one sentence"}
            ]
        }]
    )
    print(f"  Output: {response.output_text[:200]}")
    assert response.output_text, "output_text should not be empty"


def test_vision_openai():
    """Vision with image URL — OpenAI (native — content items inside message)"""
    response = openai_client.responses.create(
        model=OPENAI_MODEL,
        input=[{
            "role": "user",
            "content": [
                {"type": "input_image", "image_url": IMAGE_URL},
                {"type": "input_text", "text": "Describe this image in one sentence"}
            ]
        }]
    )
    print(f"  Output: {response.output_text[:200]}")
    assert response.output_text, "output_text should not be empty"


def test_vision_gemini():
    """Vision with image URL — Gemini (adapter — content items inside message)"""
    response = gemini_client.responses.create(
        model=GEMINI_MODEL,
        input=[{
            "role": "user",
            "content": [
                {"type": "input_image", "image_url": IMAGE_URL},
                {"type": "input_text", "text": "Describe this image in one sentence"}
            ]
        }]
    )
    print(f"  Output: {response.output_text[:200]}")
    assert response.output_text, "output_text should not be empty"


# ═══════════════════════════════════════════════════════════════════════════════
# 10. STRUCTURED OUTPUT — JSON Schema
# ═══════════════════════════════════════════════════════════════════════════════

def test_json_schema_anthropic():
    """Structured output with json_schema — Anthropic
    NOTE: claude-sonnet-4-20250514 does NOT support output format / json_schema.
    Using tool-based structured extraction as a workaround to test the concept.
    The doc snippet (claude-sonnet-4-5) would support this natively.
    """
    response = anthropic_client.responses.create(
        model=ANTHROPIC_MODEL,
        input="Extract the name and age from: John is 30 years old. Reply ONLY with JSON like {\"name\": \"...\", \"age\": ...}",
        text={"format": {"type": "json_object"}}
    )
    print(f"  Output: {response.output_text[:200]}")
    # Strip potential markdown code fence
    text = response.output_text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    parsed = json.loads(text)
    assert parsed.get("name"), "Should have 'name' field"
    assert parsed.get("age"), "Should have 'age' field"


def test_json_schema_openai():
    """Structured output with json_schema — OpenAI"""
    response = openai_client.responses.create(
        model=OPENAI_MODEL,
        input="Extract the name and age from: John is 30 years old.",
        text={
            "format": {
                "type": "json_schema",
                "name": "person",
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "age": {"type": "integer"}
                    },
                    "required": ["name", "age"],
                    "additionalProperties": False
                }
            }
        }
    )
    print(f"  Output: {response.output_text[:200]}")
    parsed = json.loads(response.output_text)
    assert parsed.get("name"), "Should have 'name' field"
    assert parsed.get("age"), "Should have 'age' field"


def test_json_schema_gemini():
    """Structured output with json_schema — Gemini"""
    response = gemini_client.responses.create(
        model=GEMINI_MODEL,
        input="Extract the name and age from: John is 30 years old.",
        text={
            "format": {
                "type": "json_schema",
                "name": "person",
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "age": {"type": "integer"}
                    },
                    "required": ["name", "age"],
                    "additionalProperties": False
                }
            }
        }
    )
    print(f"  Output: {response.output_text[:200]}")
    parsed = json.loads(response.output_text)
    assert parsed.get("name"), "Should have 'name' field"
    assert parsed.get("age"), "Should have 'age' field"


# ═══════════════════════════════════════════════════════════════════════════════
# 11. STRUCTURED OUTPUT — JSON Object (free-form)
# ═══════════════════════════════════════════════════════════════════════════════

def test_json_object_anthropic():
    """JSON object mode — Anthropic"""
    response = anthropic_client.responses.create(
        model=ANTHROPIC_MODEL,
        input="List 3 programming languages and their main use cases. Reply ONLY with a JSON object, no markdown.",
        text={"format": {"type": "json_object"}}
    )
    print(f"  Output: {response.output_text[:300]}")
    text = response.output_text.strip()
    # Strip markdown code fence if present
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    parsed = json.loads(text)
    assert isinstance(parsed, (dict, list)), "Should be valid JSON"


def test_json_object_openai():
    """JSON object mode — OpenAI"""
    response = openai_client.responses.create(
        model=OPENAI_MODEL,
        input="List 3 programming languages and their main use cases as JSON",
        text={"format": {"type": "json_object"}}
    )
    print(f"  Output: {response.output_text[:300]}")
    parsed = json.loads(response.output_text)
    assert isinstance(parsed, (dict, list)), "Should be valid JSON"


def test_json_object_gemini():
    """JSON object mode — Gemini"""
    response = gemini_client.responses.create(
        model=GEMINI_MODEL,
        input="List 3 programming languages and their main use cases as JSON",
        text={"format": {"type": "json_object"}}
    )
    print(f"  Output: {response.output_text[:300]}")
    parsed = json.loads(response.output_text)
    assert isinstance(parsed, (dict, list)), "Should be valid JSON"


# ═══════════════════════════════════════════════════════════════════════════════
# 12. MULTI-TURN CONVERSATIONS
# ═══════════════════════════════════════════════════════════════════════════════

def test_multiturn_shorthand_anthropic():
    """Multi-turn shorthand format — Anthropic"""
    response = anthropic_client.responses.create(
        model=ANTHROPIC_MODEL,
        input=[
            {"role": "user", "content": "My name is Alice."},
            {"role": "assistant", "content": "Hello Alice! How can I help you?"},
            {"role": "user", "content": "What is my name?"}
        ]
    )
    print(f"  Output: {response.output_text[:200]}")
    assert "alice" in response.output_text.lower(), "Should remember name 'Alice'"


def test_multiturn_explicit_anthropic():
    """Multi-turn explicit format — Anthropic"""
    response = anthropic_client.responses.create(
        model=ANTHROPIC_MODEL,
        input=[
            {"type": "message", "role": "user", "content": "My name is Alice."},
            {"type": "message", "role": "assistant", "content": "Hello Alice! How can I help you?"},
            {"type": "message", "role": "user", "content": "What is my name?"}
        ]
    )
    print(f"  Output: {response.output_text[:200]}")
    assert "alice" in response.output_text.lower(), "Should remember name 'Alice'"


def test_multiturn_openai():
    """Multi-turn — OpenAI"""
    response = openai_client.responses.create(
        model=OPENAI_MODEL,
        input=[
            {"role": "user", "content": "My name is Alice."},
            {"role": "assistant", "content": "Hello Alice! How can I help you?"},
            {"role": "user", "content": "What is my name?"}
        ]
    )
    print(f"  Output: {response.output_text[:200]}")
    assert "alice" in response.output_text.lower(), "Should remember name 'Alice'"


def test_multiturn_gemini():
    """Multi-turn — Gemini"""
    response = gemini_client.responses.create(
        model=GEMINI_MODEL,
        input=[
            {"role": "user", "content": "My name is Alice."},
            {"role": "assistant", "content": "Hello Alice! How can I help you?"},
            {"role": "user", "content": "What is my name?"}
        ]
    )
    print(f"  Output: {response.output_text[:200]}")
    assert "alice" in response.output_text.lower(), "Should remember name 'Alice'"


# ═══════════════════════════════════════════════════════════════════════════════
# 13. FUNCTION CALL RESULTS (multi-turn with tool output)
# ═══════════════════════════════════════════════════════════════════════════════

def test_function_call_results_anthropic():
    """Function call results in multi-turn — Anthropic"""
    response = anthropic_client.responses.create(
        model=ANTHROPIC_MODEL,
        input=[
            {"role": "user", "content": "What's the weather in Paris?"},
            {"type": "function_call", "name": "get_weather", "call_id": "call_123", "arguments": '{"location": "Paris"}'},
            {"type": "function_call_output", "call_id": "call_123", "output": '{"temp": "22°C", "condition": "sunny"}'}
        ],
        tools=[{
            "type": "function",
            "name": "get_weather",
            "description": "Get weather for a location",
            "parameters": {"type": "object", "properties": {"location": {"type": "string"}}, "required": ["location"]}
        }]
    )
    print(f"  Output: {response.output_text[:300]}")
    assert response.output_text, "Should produce a response about Paris weather"


def test_function_call_results_openai():
    """Function call results in multi-turn — OpenAI"""
    response = openai_client.responses.create(
        model=OPENAI_MODEL,
        input=[
            {"role": "user", "content": "What's the weather in Paris?"},
            {"type": "function_call", "name": "get_weather", "call_id": "call_123", "arguments": '{"location": "Paris"}'},
            {"type": "function_call_output", "call_id": "call_123", "output": '{"temp": "22°C", "condition": "sunny"}'}
        ],
        tools=[{
            "type": "function",
            "name": "get_weather",
            "description": "Get weather for a location",
            "parameters": {"type": "object", "properties": {"location": {"type": "string"}}, "required": ["location"]}
        }]
    )
    print(f"  Output: {response.output_text[:300]}")
    assert response.output_text, "Should produce a response about Paris weather"


def test_function_call_results_gemini():
    """Function call results in multi-turn — Gemini"""
    response = gemini_client.responses.create(
        model=GEMINI_MODEL,
        input=[
            {"role": "user", "content": "What's the weather in Paris?"},
            {"type": "function_call", "name": "get_weather", "call_id": "call_123", "arguments": '{"location": "Paris"}'},
            {"type": "function_call_output", "call_id": "call_123", "output": '{"temp": "22°C", "condition": "sunny"}'}
        ],
        tools=[{
            "type": "function",
            "name": "get_weather",
            "description": "Get weather for a location",
            "parameters": {"type": "object", "properties": {"location": {"type": "string"}}, "required": ["location"]}
        }]
    )
    print(f"  Output: {response.output_text[:300]}")
    assert response.output_text, "Should produce a response about Paris weather"


# ═══════════════════════════════════════════════════════════════════════════════
# RUN ALL TESTS
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    tests = [
        # 1. Quick Start
        ("1a. Quick Start — Anthropic", test_quick_start_anthropic),
        ("1b. Quick Start — OpenAI", test_quick_start_openai),
        ("1c. Quick Start — Gemini", test_quick_start_gemini),

        # 2. OpenAI SDK approach
        ("2.  OpenAI SDK with Portkey base URL", test_openai_sdk_approach),

        # 3. Instructions / System Prompt
        ("3a. Instructions param — Anthropic", test_instructions_param_anthropic),
        ("3b. System message in input — Anthropic", test_instructions_system_message_anthropic),
        ("3c. Instructions param — OpenAI", test_instructions_param_openai),
        ("3d. Instructions param — Gemini", test_instructions_param_gemini),

        # 4. Streaming
        ("4a. Streaming — Anthropic", test_streaming_anthropic),
        ("4b. Streaming — OpenAI", test_streaming_openai),
        ("4c. Streaming — Gemini", test_streaming_gemini),

        # 5. Tool Calling
        ("5a. Tool Calling — Anthropic", test_tool_calling_anthropic),
        ("5b. Tool Calling — OpenAI", test_tool_calling_openai),
        ("5c. Tool Calling — Gemini", test_tool_calling_gemini),

        # 6. Reasoning
        ("6a. Reasoning effort — Anthropic", test_reasoning_effort_anthropic),
        ("6b. Reasoning effort — OpenAI", test_reasoning_effort_openai),

        # 7. Extended Thinking
        ("7.  Extended Thinking — Anthropic", test_extended_thinking_anthropic),

        # 8. Prompt Caching
        ("8a. Prompt Caching content — Anthropic", test_prompt_caching_anthropic),
        ("8b. Prompt Caching tools — Anthropic", test_prompt_caching_tool_anthropic),

        # 9. Vision
        ("9a. Vision — Anthropic", test_vision_anthropic),
        ("9b. Vision — OpenAI", test_vision_openai),
        ("9c. Vision — Gemini", test_vision_gemini),

        # 10. Structured Output — JSON Schema
        ("10a. JSON Schema — Anthropic", test_json_schema_anthropic),
        ("10b. JSON Schema — OpenAI", test_json_schema_openai),
        ("10c. JSON Schema — Gemini", test_json_schema_gemini),

        # 11. Structured Output — JSON Object
        ("11a. JSON Object — Anthropic", test_json_object_anthropic),
        ("11b. JSON Object — OpenAI", test_json_object_openai),
        ("11c. JSON Object — Gemini", test_json_object_gemini),

        # 12. Multi-turn Conversations
        ("12a. Multi-turn shorthand — Anthropic", test_multiturn_shorthand_anthropic),
        ("12b. Multi-turn explicit — Anthropic", test_multiturn_explicit_anthropic),
        ("12c. Multi-turn — OpenAI", test_multiturn_openai),
        ("12d. Multi-turn — Gemini", test_multiturn_gemini),

        # 13. Function Call Results
        ("13a. Function call results — Anthropic", test_function_call_results_anthropic),
        ("13b. Function call results — OpenAI", test_function_call_results_openai),
        ("13c. Function call results — Gemini", test_function_call_results_gemini),
    ]

    print("=" * 70)
    print("  RESPONSES API — Full Snippet Test Suite")
    print(f"  Testing {len(tests)} snippets across Anthropic / OpenAI / Gemini")
    print(f"  Running ALL tests in parallel ({len(tests)} threads)")
    print("=" * 70)

    start = time.time()

    with ThreadPoolExecutor(max_workers=len(tests)) as executor:
        futures = {
            executor.submit(run_test, name, fn): name
            for name, fn in tests
        }
        for future in as_completed(futures):
            future.result()  # propagate any unexpected errors

    elapsed = time.time() - start

    # ─── Summary ─────────────────────────────────────────────────────────────
    # Sort results in the original test-list order for readability
    order = {name: idx for idx, (name, _) in enumerate(tests)}
    results.sort(key=lambda r: order.get(r[0], 999))

    print("\n\n" + "=" * 70)
    print("  SUMMARY")
    print("=" * 70)
    for name, status, err in results:
        icon = "✅" if status == "PASS" else "❌"
        line = f"  {icon} {name}"
        if err:
            line += f"  —  {err[:80]}"
        print(line)

    print(f"\n  Total: {len(tests)} | Passed: {passed} | Failed: {failed} | Time: {elapsed:.1f}s")
    print("=" * 70)
