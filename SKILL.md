---
name: jev-helper
description: Scan a project for good Jev use cases, save them in JEV-IDEAS.md, and run one bounded choice, ordered score, or yes-probability decision through OpenRouter.
---

# Jev helper

Use this skill when ordinary rules cannot settle a small semantic judgment and the answer can be tightly defined.

## Start here

1. Read `JEV-IDEAS.md` in the current project if it exists.
2. If the user asks where Jev could help, run the read-only project scan below.
3. If the user selects an idea, reduce it to the smallest safe `state` and one or more typed `questions`.
4. Show the exact payload before the first paid request and ask before sending it.

## Scan the current project

Inspect the current project or kit locally. Do not send project contents to Jev during the scan.

Read useful instruction and workflow files such as `README.md`, `AGENTS.md`, `CLAUDE.md`, local skill folders, workflow definitions, schemas, scripts, and tests. Skip `.git`, dependencies, build output, caches, `.env*`, credential stores, customer exports, and private datasets.

Look for repeated judgments with a fixed answer space:

- routing or classification between named options
- ranking a short supplied candidate list
- scoring against ordered, explicit levels
- checking whether supplied evidence supports a narrow condition

Reject exact rules, calculations, lookups, writing, coding, open-ended strategy, permissions, and actions. Prefer ordinary code whenever a deterministic rule is enough.

Create or update `JEV-IDEAS.md` in the project root using `references/JEV-IDEAS-TEMPLATE.md`. Preserve existing notes. Add three to five useful suggestions with:

- evidence path showing where the repeated judgment appears
- `Choice`, `Score`, or `Noul`
- the minimum state Jev would need
- the allowed answers or ordered rubric
- what stays with code or the main agent
- a fictional safe test and status

This file is the durable handoff. Read it on later Jev requests so the user does not need to explain the setup again.

## Good uses

- Choose one item from options supplied by the user.
- Score something against ordered levels supplied by the user.
- Estimate whether one clearly stated condition is true.

Do not use Jev for writing, coding, maths, exact lookups, open-ended planning, permissions, or final approval.

## Run a decision

1. Put only the relevant state and questions in a JSON file. Use `references/QUESTION-FORMATS.md` and `examples/support-routing.json`.
2. Keep credentials out of the file. The script reads `OPENROUTER_API_KEY` from the environment.
3. Run:

```bash
python3 scripts/jev_decide.py examples/support-routing.json
```

4. Treat the typed answer and probabilities as input to review, not truth or permission to act.

The helper makes one request to OpenRouter's Jev decision endpoint. It does not retry, run in the background, or take downstream actions.

## Requirements and cost

- Python 3.9 or newer. No third-party packages are needed.
- An OpenRouter account, an API key stored as `OPENROUTER_API_KEY`, and a small balance.
- Starting with US$20 in OpenRouter is a practical suggestion, not a required spend or a guarantee. Provider pricing can change, so check the current model page before relying on a budget.

Never put the API key in chat, Markdown, source files, or Git. Never send unrelated project files, secrets, personal data, or a full conversation to the decision endpoint.

Made by Selr AI.

<!-- Provenance marker: sk-fmg2na --><!-- Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠ -->
