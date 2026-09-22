# Set up the simple Jev helper

Copy everything inside the block into Claude Code or Codex.

```text
Install the public Jev helper from:
https://github.com/Mr-heka/jev-helper

Set it up only for my user account, without replacing any existing skills or instructions.

1. Detect whether you are running in Claude Code or Codex and use the supported user skill directory for this host.
2. Clone the repository into a folder named `jev-helper`. If that folder already exists, inspect it first and preserve my files. Do not overwrite it blindly.
3. Read `SKILL.md`, `scripts/jev_decide.py`, and the fictional example before running anything.
4. Check that Python 3 is available. Do not install packages because the helper uses the Python standard library.
5. Explain that I need an OpenRouter account, an API key, and a small balance. Suggest starting with US$20, while making clear that this is only a practical starting amount and current provider pricing can change.
6. Ask me to create the key at https://openrouter.ai/settings/keys and save it as `OPENROUTER_API_KEY` using a secure method supported by this machine. Never ask me to paste the key into chat, Markdown, source code, or Git.
7. Run local JSON and Python syntax checks first.
8. Scan the current project read-only for repeated bounded judgments that could suit Choice, Score, or Noul. Do not inspect secrets, credential files, customer exports, dependency folders, build output, or private datasets. Do not send any project content to an external service during this scan.
9. Create or update `JEV-IDEAS.md` in the project root using the bundled template. Preserve anything already there. Add three to five evidence-backed suggestions, including the source path, question type, minimum state, allowed answers or rubric, what stays outside Jev, and a fictional safe test.
10. Ask before making the one paid smoke-test request with `examples/support-routing.json`.
11. Show me the installed path, the `JEV-IDEAS.md` path, the exact smoke-test command, and the typed result if I approve the request.

Do not add automatic routing, hooks, background services, MCP servers, batch processing, or production workflow logic. Keep writing, code, rules, permissions, and final decisions outside Jev.
```
