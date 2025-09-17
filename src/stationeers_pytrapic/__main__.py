import argparse
import logging
import sys
from pathlib import Path

from .compiler import compile_code, CompileOptions


def main():
    parser = argparse.ArgumentParser(description="A simple command-line tool.")
    parser.add_argument("input_file", help="Input python file")
    parser.add_argument("--compact", help="Apply optimizations", action="store_true")
    parser.add_argument(
        "--stats", help="Print statistisc as comment", action="store_true"
    )
    parser.add_argument(
        "--comments",
        help="Append input code as comment on each line",
        action="store_true",
    )
    args = parser.parse_args()

    # logging.basicConfig(
    #     level=logging.INFO,
    #     format="%(name)s - %(levelname)s - %(message)s",
    # )

    code = Path(args.input_file).read_text()
    options = CompileOptions(
        compact=args.compact,
        original_code_as_comment=args.comments,
        remove_labels=args.compact,
    )
    data = compile_code(code, options)
    code = data.get("code", "")
    error = data.get("error", {})
    stack_trace = error.get("stack_trace", "")
    if error:
        print(f"Error: {error['description']}", file=sys.stderr)
        if stack_trace:
            print(f"Stack trace: {stack_trace}", file=sys.stderr)
        sys.exit(1)
    elif code:
        print(code)
        if args.stats:
            print(f"# num registers: {data.get('num_registers', -1)}")
            print(f"# num lines:     {data.get('num_lines', -1)}")
            print(f"# num bytes:     {data.get('num_bytes', -1)}")


if __name__ == "__main__":
    main()
