"""token-counter CLI."""
import argparse

from .counter import count, estimate_cost, model_prices


def main():
    ap = argparse.ArgumentParser(prog="token-counter")
    ap.add_argument("prompt", nargs="?", help="prompt text")
    ap.add_argument("--model", default="gpt-4o")
    args = ap.parse_args()
    if args.prompt:
        print(estimate_cost(args.prompt, model=args.model))
    else:
        print(model_prices())


if __name__ == "__main__":
    main()
