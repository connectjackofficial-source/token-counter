"""Tests for batch counting and output-cost estimation."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from token_counter.counter import count_many, estimate_cost, model_prices


def test_count_many():
    counts = count_many(["hello world", "你好世界", "a b c"])
    assert len(counts) == 3
    assert counts[0] >= 1
    print("test_count_many: ok")


def test_estimate_with_output():
    est = estimate_cost("hello world", model="gpt-4o", output_tokens=500)
    assert est["output_tokens"] == 500
    assert est["cost"] > 0
    # output cost raises the total
    est_no_out = estimate_cost("hello world", model="gpt-4o")
    assert est["cost"] > est_no_out["cost"]
    print("test_estimate_with_output: ok")


def test_model_prices_shape():
    prices = model_prices()
    assert "gpt-4o" in prices
    assert "input_per_1k" in prices["gpt-4o"]
    assert "output_per_1k" in prices["gpt-4o"]
    print("test_model_prices_shape: ok")


if __name__ == "__main__":
    test_count_many()
    test_estimate_with_output()
    test_model_prices_shape()
    print("token-counter batch tests passed")
