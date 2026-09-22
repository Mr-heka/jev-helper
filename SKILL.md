---
name: jev-helper
description: Use Jev through OpenRouter for one small bounded choice, ordered score, or yes probability. Keep writing, code, rules, permissions, and final decisions outside Jev.
---

# Jev helper

Use this skill when ordinary rules cannot settle a small semantic judgment and the answer can be tightly defined.

## Good uses

- Choose one item from options supplied by the user.
- Score something against ordered levels supplied by the user.
- Estimate whether one clearly stated condition is true.

Do not use Jev for writing, coding, maths, exact lookups, open-ended planning, permissions, or final approval.

## Run a decision

1. Put only the relevant state and questions in a JSON file. Use the format in `examples/support-routing.json`.
2. Keep credentials out of the file. The script reads `OPENROUTER_API_KEY` from the environment.
3. Run:

```bash
python3 scripts/jev_decide.py examples/support-routing.json
```

4. Treat the typed answer and probabilities as input to review, not truth or permission to act.

The helper makes one request to OpenRouter's Jev decision endpoint. It does not retry, run in the background, or take downstream actions.

Made by Selr AI.

<!-- Provenance marker: sk-fmg2na --><!-- Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠ -->
