# LangChain No-LLM Agent

A zero-LLM-cost project for practicing LangChain tool calling, routing, guardrails, authorization, human approval, and tool-call limits.

## Architecture

User -> Input Guard -> Deterministic Router -> Tool Guard -> LangChain Tool -> Output Guard -> User

No OpenAI, Azure OpenAI, Gemini, or other paid LLM is required.

## Free tools

1. Weather - Open-Meteo
2. Calculator - local Python
3. Dictionary - dictionaryapi.dev

## Setup

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
python -m app.main
```

## Examples

```text
What is the weather in Pune?
calculate 25 * 4
define artificial
```

Type `exit` to stop.

## What to practice

- `@tool`
- tool schemas
- `tool.invoke()`
- tool registry
- deterministic routing
- input guardrails
- tool authorization
- output guardrails
- human approval
- maximum tool calls
- external free APIs

## Upgrade path

After understanding this project, replace `app/agent/router.py` with an LLM-based router or build a LangGraph version using the same tools and guardrails.
