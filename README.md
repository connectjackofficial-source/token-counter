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

## License

MIT
