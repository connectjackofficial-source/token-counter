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


def estimate_cost(prompt: str, model: str = "gpt-4o") -> dict:
    tokens = count(prompt)
    prices = {"gpt-4o": 0.0025, "haiku": 0.00025, "sonnet": 0.003}
    price = prices.get(model, 0.0025)
    cost = (tokens / 1000) * price
    return {"tokens": tokens, "model": model, "cost": round(cost, 6)}
