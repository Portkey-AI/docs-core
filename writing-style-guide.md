# Portkey Documentation Writing Style Guide

Inspired by Bun's documentation style: **direct, concise, and action-oriented**.

**Remember: People hate boring docs.** Say less, show more. Use code samples, graphs, images, and GIFs to demonstrate concepts. Make every doc scannable. If you can make it shorter without losing meaning, do it—the reader will thank you.

## Core Principles (Based on Bun.js Documentation Analysis)

After analyzing Bun's documentation, their style is characterized by:

1. **Minimal use of "you"** - Often omit "you" entirely: "Install Bun" not "You can install Bun"
2. **Direct imperatives** - Start with action verbs: "Run the file", "Configure settings"
3. **Concise statements** - Every word serves a purpose, no fluff
4. **Objective tone** - Focus on tasks and tools, not the reader
5. **Factual descriptions** - State what things are/do, not what users can do with them

## Our Adapted Principles

1. **Be direct** - Remove unnecessary words and conditional language
2. **Use imperatives** - Tell users what to do, not what they "can" do
3. **Focus on actions** - Start with verbs when possible
4. **Remove hedging** - Cut "if you want to", "you can", "you should" when the intent is clear
5. **Omit "you" when possible** - "Add providers" is better than "You can add providers"
6. **Say less, show more** - Use visuals (code, images, GIFs, graphs) instead of long explanations
7. **Prioritize scannability** - Structure content so readers can quickly find what they need
8. **Shorter is better** - Cut every word that doesn't add value. If it's shorter and just as clear, use it.

## Common Patterns to Simplify

### Pattern 1: Conditional Statements → Direct Actions

❌ **Avoid:**
- "If you just want to use AI models in your workspace,"
- "If you want to share credentials across workspaces,"
- "If you're using a provider like Fireworks AI,"

✅ **Use:**
- "To use AI models in your workspace,"
- "To share credentials across workspaces,"
- "For providers like Fireworks AI,"

### Pattern 2: "You can" → Direct Imperative (Omit "You" When Possible)

Bun's style: They often omit "you" entirely, making statements more direct.

❌ **Avoid:**
- "You can add providers via UI"
- "You can configure budget limits"
- "You can choose from three options"

✅ **Use (Bun-style):**
- "Add providers via UI"
- "Configure budget limits"
- "Choose from three options"

**Exception:** Keep "you can" when describing capabilities that are optional or when presenting alternatives:
- ✅ "You can use existing credentials or create new ones" (shows choice - "you" helps clarify it's a user choice)
- ✅ "You can also specify the provider in the header" (alternative method - the "also" signals it's an option, not the primary method)
- ✅ "You can optionally configure periodic resets" (clearly optional)

**Note:** When the action is clearly directed at the user, omitting "you" is fine. When showing options/alternatives, keeping "you" can help clarify it's a choice.

### Pattern 3: "You should" → Direct Instruction

❌ **Avoid:**
- "You should configure this setting"
- "You should use an explicit allow-list"

✅ **Use:**
- "Configure this setting"
- "Use an explicit allow-list"

### Pattern 4: "You need to" → "To" or Direct Action

❌ **Avoid:**
- "You need to create an integration first"
- "You need to set up credentials"

✅ **Use:**
- "Create an integration first"
- "Set up credentials"
- Or: "To use this feature, create an integration first"

### Pattern 5: Remove Unnecessary Introductions

❌ **Avoid:**
- "Here's how you can do this:"
- "This is where you can configure:"
- "You will see a list of:"

✅ **Use:**
- "Do this:"
- "Configure:"
- "You'll see a list of:" (only if the list is actually visible)

## Code Examples: Use CodeGroup Instead of Tabs

**Use `<CodeGroup>` for multiple code examples** - Mintlify's CodeGroup component provides a cleaner, more modern interface for displaying multiple code examples.

### Format

````mdx
<CodeGroup>
```python Python
# Python code here
```

```js JavaScript
// JavaScript code here
```

```sh cURL
# cURL example here
```
</CodeGroup>
````

**Key points:**
- Each code block needs a title (becomes the tab label): ` ```language Title`
- CodeGroup automatically creates a tabbed interface
- Cleaner syntax than `<Tabs>` and `<Tab>` components
- Works great for showing the same example in multiple languages

**Example:**
```mdx
<CodeGroup>
```python Python
from portkey_ai import Portkey

portkey = Portkey(api_key="PORTKEY_API_KEY")
```

```js JavaScript
import Portkey from 'portkey-ai'

const portkey = new Portkey({
    apiKey: "PORTKEY_API_KEY"
})
```
</CodeGroup>
```

**Reference:** [Mintlify CodeGroup Documentation](https://www.mintlify.com/docs/components/code-groups)

## Code Formatting: K&R Style & Best Practices

Follow these formatting rules for all code examples to ensure consistency and readability:

### K&R Style (Kernighan & Ritchie)

**Opening braces on the same line:**

✅ **Good:**
```python
# Python - compact dicts and arrays
messages=[{"role": "user", "content": "Hello"}]
```

```javascript
// JavaScript - opening brace on same line
const portkey = new Portkey({
    apiKey: "PORTKEY_API_KEY"
})

const response = await portkey.chat.completions.create({
    model: "@anthropic/claude-sonnet-4",
    messages: [{ role: "user", content: "Hello" }]
})
```

❌ **Avoid:**
```javascript
// Opening brace on new line
const portkey = new Portkey(
{
    apiKey: "PORTKEY_API_KEY"
}
)
```

### Indentation Rules

**Use 4-space indentation consistently:**

✅ **Good:**
```python
response = portkey.chat.completions.create(
    model="@anthropic/claude-sonnet-4",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Hello"},
            {"type": "image_url", "image_url": {"url": "..."}}
        ]
    }]
)
```

❌ **Avoid:**
```python
# Unnecessary multi-line nesting for simple objects
messages=[
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Hello"
            }
        ]
    }
]
```

### Keep Simple Objects Compact

**Single-line for simple objects:**

✅ **Good:**
```python
{"role": "user", "content": "Hello"}
{"type": "text", "text": "What's in this image?"}
{"type": "file", "file": {"mime_type": "application/pdf", "file_data": data}}
```

```javascript
{ role: "user", content: "Hello" }
{ type: "text", text: "What's in this image?" }
{ type: "file", file: { mime_type: "application/pdf", file_data: data } }
```

❌ **Avoid:**
```python
# Unnecessarily breaking up simple objects
{
    "type": "text",
    "text": "Hello"
}
```

### Remove Trailing Commas in Python

✅ **Good:**
```python
messages=[{"role": "user", "content": "Hello"}]
```

❌ **Avoid:**
```python
messages=[
    {"role": "user", "content": "Hello"}
],  # Trailing comma after closing bracket
```

### Comment Style

**Use language-appropriate comment syntax:**

✅ **Good:**
```python
# Python comments use hash
portkey = Portkey(api_key="PORTKEY_API_KEY")
```

```javascript
// JavaScript comments use double slash
const portkey = new Portkey({
    apiKey: "PORTKEY_API_KEY"
})
```

❌ **Avoid:**
```python
// Wrong comment syntax for Python
portkey = Portkey(api_key="PORTKEY_API_KEY")
```

### Summary Checklist

- [ ] Opening braces on the same line (K&R style)
- [ ] 4-space indentation throughout
- [ ] Simple objects on one line
- [ ] No trailing commas in Python after closing brackets
- [ ] Correct comment syntax for the language
- [ ] Consistent formatting across all examples

## Say Less, Show More (Visual Content & Scannability)

**Core principle:** People scan docs, they don't read them. Show, don't tell.

### Use Visual Content Strategically

❌ **Avoid:**
- Long paragraphs explaining how a UI works
- Step-by-step text descriptions of visual processes
- Explaining what a feature looks like in words

✅ **Use:**
- Screenshots showing the UI
- GIFs demonstrating workflows
- Code samples instead of explaining syntax
- Diagrams/graphs for complex relationships
- Visual examples before text explanations

**Examples:**

❌ **Bad:**
> "To add a provider, navigate to the Model Catalog section in the left sidebar. You'll see a button labeled 'Add Provider' in the top right corner. Click this button to open a modal dialog. In this dialog, you'll see a dropdown menu where you can select the provider type, and below that, input fields for your API key and other credentials."

✅ **Good:**
> "Add a provider:
> 
> ![Add Provider UI](path/to/image.png)
> 
> 1. Go to Model Catalog → Add Provider
> 2. Select provider type
> 3. Enter credentials"

### Prioritize Scannability

Make content easy to scan:

✅ **Do:**
- Use clear headings and subheadings
- Break long paragraphs into bullet points
- Use numbered lists for sequences
- Put the most important info first
- Use tables for comparisons
- Use code blocks for examples
- Add visual breaks (images, code blocks) between sections

❌ **Don't:**
- Write walls of text
- Bury important info in paragraphs
- Use long sentences when short ones work
- Explain what a screenshot shows

### Make It Shorter

**Rule:** If you can make it shorter without losing meaning, do it.

❌ **Before (47 words):**
> "When you are working with the Model Catalog feature, you have the ability to configure various settings that will allow you to control how models are displayed and managed within your workspace environment."

✅ **After (12 words):**
> "Configure Model Catalog settings to control how models are displayed and managed."

**Before publishing, ask:**
- Can I replace this paragraph with a screenshot?
- Can I replace this explanation with a code example?
- Can I cut this sentence in half?
- Would a bullet list be clearer than this paragraph?
- Is every word necessary?

## Examples from Our Docs

### Before → After

**Before:**
> "If you just want to use AI models in your workspace, see the Model Catalog documentation."

**After:**
> "To use AI models in your workspace, see the Model Catalog documentation."

---

**Before:**
> "You can add providers via UI or API."

**After:**
> "Add providers via UI or API."

---

**Before:**
> "When provisioning an integration to a workspace, you can enforce powerful governance rules by setting budget and rate limits."

**After:**
> "When provisioning an integration to a workspace, enforce governance rules by setting budget and rate limits."

---

**Before:**
> "If you're using a provider like Fireworks AI with many community models, you can toggle on 'Automatically enable new models'."

**After:**
> "For providers like Fireworks AI with many community models, toggle on 'Automatically enable new models'."

## When to Keep Conditional Language

Keep conditional language when:
1. **Showing alternatives/options:** "You can use existing credentials or create new ones"
2. **Presenting alternative methods:** "You can also specify the provider in the header" (when "also" indicates an alternative to the primary method)
3. **Explaining optional features:** "You can optionally configure periodic resets"
4. **Describing capabilities (not instructions):** "You can track spending across all workspaces"
5. **Clarifying context:** "If you're an org admin, you'll see the Integrations tab"

**Key distinction:** 
- ❌ "You can add providers" → This is an instruction, make it direct: "Add providers"
- ✅ "You can also add providers" → This is an alternative/option, keep "you can also"

## Tone Guidelines (Inspired by Bun)

Bun's documentation tone:
- **Objective and factual** - "Bun is an all-in-one toolkit" (not "Bun can be used as...")
- **Direct commands** - "Install Bun", "Run the file" (not "You can install Bun")
- **Minimal personal pronouns** - Focus on the tool/task, not the reader
- **Concise** - No unnecessary words or explanations

Our adapted tone:
- **Confident but not bossy** - Use imperatives, but explain why when helpful
- **Helpful, not prescriptive** - Show options when they exist
- **Clear, not verbose** - Every word should add value
- **Action-oriented** - Start with what the user does, not what the system does
- **Omit "you" when natural** - "Add providers" reads better than "You can add providers"

## Making Docs Approachable (Without Using "You")

Bun's docs feel friendly and approachable even without personal pronouns. Here's how:

### 1. **Simple, Conversational Language**
❌ "The system enables you to configure multiple deployment environments"
✅ "Portkey supports multiple deployment environments"

❌ "It is possible to utilize the API for programmatic access"
✅ "Use the API for programmatic access"

### 2. **Examples First, Explanations Second (Show, Don't Tell)**
❌ "To add a provider, you need to navigate to the Model Catalog section, then click the Add Provider button, and finally enter your credentials."
✅ "Add a provider:
1. Go to Model Catalog → Add Provider
2. Enter your credentials"

**Even better:** Show a screenshot or GIF of the process, then list the steps.

### 3. **Positive, Empowering Framing**
❌ "You must configure credentials before making requests"
✅ "Configure credentials to start making requests"

❌ "You cannot use this feature without setting up an integration"
✅ "Set up an integration to use this feature"

### 4. **Short, Digestible Sentences**
❌ "When you are provisioning an integration to a workspace, you have the ability to enforce powerful governance rules through the configuration of budget and rate limits, which provides you with granular control over costs and usage patterns."
✅ "When provisioning an integration to a workspace, enforce governance rules by setting budget and rate limits. This gives you granular control over costs and usage patterns."

### 5. **Assumes Competence, Explains Clearly**
❌ "If you don't know how to do this, you should read the following guide..."
✅ "For detailed setup, see the [integration guide](/product/integrations)"

### 6. **Natural, Not Robotic**
❌ "The following steps must be executed in order to complete the process"
✅ "Complete these steps:"

❌ "It is recommended that users configure this setting"
✅ "Configure this setting for better performance"

### 7. **Helpful Structure (Easy to Scan)**
- Use bullet points for lists
- Number steps for sequences
- Use headings that describe what you'll learn/do
- Put the most important info first

### 8. **Encouraging, Not Intimidating**
❌ "This feature requires advanced configuration and may be difficult for beginners"
✅ "This feature offers advanced configuration options"

❌ "You need to understand X, Y, and Z before proceeding"
✅ "This builds on concepts from [X](/link), [Y](/link), and [Z](/link)"

### 9. **Practical Focus (Visual & Actionable)**
- Show real examples, not abstract concepts
- Include code snippets that work
- Use screenshots/GIFs for UI workflows
- Use diagrams for complex relationships
- Explain the "why" when it's helpful, not just the "what"
- Prefer visuals over long explanations

### 10. **Confident but Not Condescending**
❌ "As you may already know, Portkey is a gateway..."
✅ "Portkey is an AI gateway that..."

❌ "Obviously, you'll want to configure this..."
✅ "Configure this setting to..."

## Checklist (Bun-Inspired)

Before publishing, ask:
- [ ] Can I remove "you" and make it a direct instruction? ("Add providers" vs "You can add providers")
- [ ] Can I remove "you can" and make it a direct instruction?
- [ ] Can I change "if you want to" to "to"?
- [ ] Can I start this sentence with a verb?
- [ ] Is every word necessary?
- [ ] Would this read naturally without "you"? (Bun often omits it)
- [ ] Am I stating facts directly? ("Portkey stores credentials" vs "You can store credentials in Portkey")
- [ ] Does this sound friendly and approachable? (Simple language, positive framing)
- [ ] Am I showing examples before explaining? (Show, don't just tell)
- [ ] Are my sentences short and digestible? (Break up long sentences)
- [ ] Am I assuming competence? (Don't talk down to readers)
- [ ] Does this read like natural conversation? (Not robotic or overly formal)
- [ ] **Can I replace this text with a screenshot, GIF, or diagram?** (Say less, show more)
- [ ] **Can I replace this explanation with a code example?** (Code > words)
- [ ] **Am I using CodeGroup for multiple code examples?** (Use `<CodeGroup>` instead of `<Tabs>`)
- [ ] **Do code examples follow K&R style?** (Opening braces on same line, 4-space indentation, simple objects compact)
- [ ] **Are comments using correct syntax?** (# for Python, // for JavaScript)
- [ ] **Is this easy to scan?** (Headings, bullets, lists, visual breaks)
- [ ] **Can I make this shorter without losing meaning?** (Shorter is better)
- [ ] **Am I explaining what a visual shows?** (If yes, remove the explanation—the visual speaks for itself)

## Quick Reference

| Instead of | Use (Bun-style) |
|------------|-----------------|
| "If you want to X" | "To X" |
| "You can X" | "X" (when it's an instruction - omit "you") |
| "You should X" | "X" |
| "You need to X" | "X" or "To X" |
| "If you're using X" | "For X" or "When using X" |
| "Here's how you can" | "Do this:" or just start with the action |
| "You will see" | "You'll see" (only if actually visible) |
| "Portkey allows you to X" | "Portkey supports X" or "X with Portkey" |
| "You can use X to Y" | "Use X to Y" or "X enables Y" |
| Long paragraph explaining UI | Screenshot/GIF + short steps |
| Explaining what code does | Show code example |
| Describing a visual process | Show the visual (image/GIF) |
| Multiple code examples | Use `<CodeGroup>` instead of `<Tabs>` |
| Wall of text | Bullets, lists, headings, visual breaks |
| Inconsistent code formatting | Follow K&R style (see Code Formatting section) |

## Bun Documentation Examples

From Bun's actual docs:
- ✅ "Bun ships as a single, dependency-free executable." (Simple, factual, friendly)
- ✅ "Install Bun via script, package manager, or Docker." (Direct, clear, approachable)
- ✅ "Use `bun run` to execute a source file." (Action-oriented, no fluff)
- ✅ "Bun is an all-in-one toolkit for developing modern JavaScript/TypeScript applications." (Positive framing, empowering)

**What makes these friendly:**
- No "you" but still feels personal and direct
- Simple words, no jargon
- Positive framing ("is" not "can be used as")
- Short sentences, easy to read
- Assumes you know what you're doing
- Feels like a helpful colleague, not a manual
