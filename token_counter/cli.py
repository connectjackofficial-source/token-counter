"""token-counter CLI."""
import argparse
import json

from .counter import count, count_many, estimate_cost, model_prices


def main():
    ap = argparse.ArgumentParser(prog="token-counter")
    ap.add_argument("prompt", nargs="?", help="prompt text")
    ap.add_argument("--model", default="gpt-4o")
    ap.add_argument("--output-tokens", type=int, default=0,
                    help="expected output length for cost estimate")
    ap.add_argument("--file", default=None,
                    help="count every line of a file (batch mode)")
    args = ap.parse_args()

    if args.file:
        lines = [l for l in open(args.file, encoding="utf-8")
                 if l.strip()]
        counts = count_many(lines)
        print(json.dumps({
            "items": len(counts),
            "total_tokens": sum(counts),
            "per_line": counts,
        }, indent=2))
    elif args.prompt:
        print(estimate_cost(args.prompt, model=args.model,
                            output_tokens=args.output_tokens))
    else:
        print(json.dumps(model_prices(), indent=2))


if __name__ == "__main__":
    main()
