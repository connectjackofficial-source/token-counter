"""Tests for file-level counting."""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from token_counter.counter import count, count_file


def test_count_file():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "prompt.txt"
        text = "hello world, this is a prompt with some tokens in it"
        p.write_text(text, encoding="utf-8")
        res = count_file(str(p))
        assert res["path"] == str(p)
        assert res["chars"] == len(text)
        assert res["tokens"] == count(text)
    print("test_count_file: ok")


def test_count_file_cjk():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "cn.txt"
        text = "请解释缓存机制以及如何在生产环境中使用"
        p.write_text(text, encoding="utf-8")
        res = count_file(str(p))
        assert res["tokens"] == count(text)
    print("test_count_file_cjk: ok")


def test_count_file_empty():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "empty.txt"
        p.write_text("", encoding="utf-8")
        res = count_file(str(p))
        assert res["tokens"] == 0
    print("test_count_file_empty: ok")


if __name__ == "__main__":
    test_count_file()
    test_count_file_cjk()
    test_count_file_empty()
    print("token-counter file tests passed")
