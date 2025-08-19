import argparse
import logging
import sys
from pathlib import Path

from .compiler import compile_code


def main():
    parser = argparse.ArgumentParser(description="A simple command-line tool.")
    parser.add_argument("input_file", help="Input python file")
    parser.add_argument("--compact", help="Apply optimizations", action="store_true")
    args = parser.parse_args()

    # logging.basicConfig(
    #     level=logging.INFO,
    #     format="%(name)s - %(levelname)s - %(message)s",
    # )

    code = Path(args.input_file).read_text()
    data = compile_code(code, compact=args.compact)
    code = data.get("code", "")
    error = data.get("error", "")
    stack_trace = data.get("stack_trace", "")
    if error:
        print(f"Error: {error}", file=sys.stderr)
        if stack_trace:
            print(f"Stack trace: {stack_trace}", file=sys.stderr)
        sys.exit(1)
    elif code:
        print(code)


if __name__ == "__main__":
    main()
