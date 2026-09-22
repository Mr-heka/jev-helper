#!/usr/bin/env python3
"""Send one small typed decision request to Jev through OpenRouter."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request


URL = "https://openrouter.ai/api/alpha/decisions"
MODEL = "typesafe/jev-1.13"


def fail(message: str) -> None:
    print(f"jev-helper: {message}", file=sys.stderr)
    raise SystemExit(1)


if len(sys.argv) != 2:
    fail("usage: python3 scripts/jev_decide.py INPUT.json")

key = os.environ.get("OPENROUTER_API_KEY", "").strip()
if not key:
    fail("OPENROUTER_API_KEY is not set")

try:
    with open(sys.argv[1], encoding="utf-8") as handle:
        body = json.load(handle)
except (OSError, json.JSONDecodeError):
    fail("could not read valid JSON input")

if not isinstance(body, dict) or set(body) != {"state", "questions"}:
    fail("input must contain only state and questions")
if not isinstance(body["questions"], dict) or not body["questions"]:
    fail("questions must be a non-empty object")

payload = json.dumps({"model": MODEL, **body}).encode("utf-8")
request = urllib.request.Request(
    URL,
    data=payload,
    method="POST",
    headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    },
)

try:
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)
except urllib.error.HTTPError as error:
    fail(f"OpenRouter returned HTTP {error.code}")
except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError):
    fail("the OpenRouter request failed")

answers = result.get("answers") if isinstance(result, dict) else None
if not isinstance(answers, dict):
    fail("OpenRouter returned an unexpected response")

print(json.dumps({
    "model": result.get("model"),
    "answers": answers,
    "usage": result.get("usage"),
}, indent=2))
