# Question formats

Use only the smallest relevant state. Question names are stable keys in the returned `answers` object.

## Choice

Use when exactly one supplied option must be selected.

```json
"queue": {"type": "Choice", "options": ["billing", "technical"]}
```

## Score

Use ordered levels with clear criteria. Do not use a vague numeric scale.

```json
"priority": {"type": "Score", "scores": ["low", "normal", "urgent"]}
```

## Noul

Use for the probability that one narrow statement is true.

```json
"supported": {"type": "Noul", "statement": "The supplied evidence supports the claim"}
```

Check the current TypeSafe/OpenRouter format if the API rejects a shape. Do not silently invent a new schema.
