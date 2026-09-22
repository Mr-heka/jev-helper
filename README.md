# Simple Jev helper

A deliberately small Claude Code and Codex skill for sending one bounded decision to Jev through OpenRouter.

![A simple agent-to-Jev decision flow](assets/jev-flow.png)

It scans your current project for suitable bounded judgments, saves the suggestions in `JEV-IDEAS.md`, and supports Jev's three useful question shapes: choice, ordered score, and yes probability.

You need Python 3.9+, an OpenRouter account, an API key, and a small balance. We suggest starting with US$20. Actual usage varies and provider pricing can change.

It does not include automatic routing, background services, internal evaluation systems, or production workflow logic. Your main agent still owns writing, code, rules, permissions, and final decisions.

Start with [SETUP-PROMPT.md](SETUP-PROMPT.md).

Made by Selr AI.
