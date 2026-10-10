"""token-counter: estimate token count for a prompt.

Heuristic: ~4 chars per token for English, ~2 chars per token for CJK.
"""
from __future__ import annotations

import re


def count(prompt: str) -> int:
    """Estimate token count."""
    cjk = len(re.findall(r'[\u4e00-\u9fff]', prompt))
    other = len(prompt) - cjk
    return round(other / 4 + cjk / 2)


def count_many(prompts: list) -> list:
    """Batch estimate: returns one token count per prompt."""
    return [count(p) for p in prompts]


# (input $/1k, output $/1k) by model
PRICES = {
    "gpt-4o": (0.0025, 0.01),
    "haiku": (0.00025, 0.00125),
    "sonnet": (0.003, 0.015),
    "opus": (0.015, 0.075),
    "gemini-pro": (0.00125, 0.005),
}

# Role weighting mirrors real chat APIs: system/context costs less per
# token than assistant output, so a naive char-count overstates the bill.
ROLE_WEIGHT = {"system": 0.5, "user": 1.0, "assistant": 1.5, "tool": 1.0}


def count_messages(messages: list) -> dict:
    """Count a chat-style message list:
    [{"role": "user", "content": "..."}, ...].

    Returns per-role counts plus a weighted total.
    """
    per_role = {}
    for m in messages:
        role = m.get("role", "user")
        per_role[role] = per_role.get(role, 0) + count(str(m.get("content", "")))
    total = 0
    for role, n in per_role.items():
        total += int(n * ROLE_WEIGHT.get(role, 1.0))
    return {"per_role": per_role, "total": total}


def estimate_cost(prompt: str, model: str = "gpt-4o",
                  output_tokens: int = 0) -> dict:
    tokens = count(prompt)
    in_rate, out_rate = PRICES.get(model, PRICES["gpt-4o"])
    cost = (tokens / 1000) * in_rate + (output_tokens / 1000) * out_rate
    return {"tokens": tokens, "model": model,
            "output_tokens": output_tokens,
            "cost": round(cost, 6)}


def model_prices() -> dict:
    return {m: {"input_per_1k": p[0], "output_per_1k": p[1]}
            for m, p in PRICES.items()}
