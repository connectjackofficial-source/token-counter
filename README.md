# token-counter

> Estimate token count for a prompt. Rough heuristic: ~4 chars/token for
> English, ~2 chars/token for CJK.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

## Usage

```python
from token_counter.counter import count, estimate_cost

count("hello world")  # ~3
estimate_cost("hello world")
# {'tokens': 3, 'model': 'gpt-4o', 'cost': 0.000008}
```

## Batch counting

```python
from token_counter.counter import count_many

count_many(["prompt one", "prompt two"])  # [3, 3]

# or via CLI: count every non-empty line of a file
python -m token_counter.cli --file prompts.txt
```

## Cost with expected output

```python
estimate_cost("hello world", model="gpt-4o", output_tokens=500)
# includes both input and output cost
```

## CLI

```bash
python -m token_counter.cli "hello world"
python -m token_counter.cli --model sonnet --output-tokens 200 "write code"
python -m token_counter.cli --file prompts.txt
```

## License

MIT
