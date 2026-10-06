"""Tests for token-counter."""
from token_counter.counter import count, estimate_cost, model_prices


def test_count_cjk():
    assert count("你好世界") == 4
    print("test_count_cjk: ok")


def test_count_english():
    n = count("hello world")
    assert 2 <= n <= 4
    print("test_count_english: ok")


def test_estimate():
    cost = estimate_cost("hello", model="haiku")
    assert cost["model"] == "haiku"
    assert cost["tokens"] > 0
    print("test_estimate: ok")


def test_prices():
    assert "opus" in model_prices()
    print("test_prices: ok")


if __name__ == "__main__":
    test_count_cjk()
    test_count_english()
    test_estimate()
    test_prices()
    print("token-counter tests passed")
