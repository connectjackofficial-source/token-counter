"""Tests for message-level counting."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from token_counter.counter import count, count_messages


def test_count_messages_basic():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain caching in one paragraph."},
        {"role": "assistant", "content": "Caching stores repeated results."},
    ]
    r = count_messages(messages)
    assert set(r["per_role"]) == {"system", "user", "assistant"}
    # system weighted 0.5 < user 1.0 < assistant 1.5
    assert r["total"] > sum(r["per_role"].values()) * 0.9
    assert r["total"] >= 0
    print("test_count_messages_basic: ok")


def test_count_messages_matches_count():
    messages = [{"role": "user", "content": "hello world"}]
    r = count_messages(messages)
    assert r["per_role"]["user"] == count("hello world")
    print("test_count_messages_matches_count: ok")


def test_count_messages_cjk():
    messages = [{"role": "user", "content": "请解释缓存机制并给出示例"}]
    r = count_messages(messages)
    assert r["per_role"]["user"] == count("请解释缓存机制并给出示例")
    print("test_count_messages_cjk: ok")


if __name__ == "__main__":
    test_count_messages_basic()
    test_count_messages_matches_count()
    test_count_messages_cjk()
    print("token-counter message tests passed")
