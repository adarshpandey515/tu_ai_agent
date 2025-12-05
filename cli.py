import sys
import argparse
from src.groq_client import GroqClient, GroqError


def parse_args(argv):
    p = argparse.ArgumentParser(description="TU AI Agent CLI using Groq")
    p.add_argument("prompt", nargs="?", help="Prompt to send to the model")
    p.add_argument("-t", "--temperature", type=float, default=0.2, help="Sampling temperature")
    p.add_argument("-m", "--max-tokens", type=int, default=1024, help="Max tokens in response")
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv or sys.argv[1:])

    prompt = args.prompt
    if not prompt:
        # read from stdin if not provided
        prompt = sys.stdin.read().strip()

    try:
        client = GroqClient()
        out = client.complete(prompt=prompt, temperature=args.temperature, max_tokens=args.max_tokens)
        print(out)
        return 0
    except GroqError as ge:
        print(f"Error: {ge}", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
