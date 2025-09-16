import glob
from pathlib import Path

import pytest

from stationeers_pytrapic.compiler import *

case_files = glob.glob(str(Path(__file__).parent / "cases" / "*.py"))
example_files = [
    f
    for f in glob.glob(
        str(
            Path(__file__).parent.parent
            / "src"
            / "stationeers_pytrapic"
            / "examples"
            / "*.py"
        )
    )
    if "__init__" not in f
]


def run_case(
    code_file,
    result_file=None,
    reference_file=None,
    write_reference=False,
    compact=False,
    modules=None,
):
    code_file = Path(code_file)

    suffix = ".compact" if compact else ""

    if result_file is None:
        result_file = Path(code_file).with_suffix(suffix + ".ic10")

    if reference_file is None:
        reference_file = Path(code_file).with_suffix(suffix + ".ref")

    code = code_file.read_text(encoding="utf-8")

    try:
        if modules is not None:
            modules = modules.copy()
            modules[""] = code
            code = modules
        result = compile_code(code, compact=compact)

        if "error" in result:
            result_str = "Error: " + result["error"]["description"] + "\n"
        else:
            result_str = f"{result['code']}\n# registers: {result['num_registers']}\n# lines: {result['num_lines']}\n"

        if write_reference:
            if reference_file.exists():
                old_reference = reference_file.read_text(encoding="utf-8")
                if old_reference != result_str:
                    print(f"Reference file {reference_file} changed")
            else:
                print(f"New reference file {reference_file}")
            reference_file.write_text(result_str, encoding="utf-8")

        reference = reference_file.read_text(encoding="utf-8")

        if "error" in result and not reference.startswith("Error: "):
            # No error in reference, fail the test
            pytest.fail(
                f"Compilation failed for {code_file}: {result['error']}\n"
                f"Stack trace: {result.get('stack_trace', 'No stack trace available')}"
            )

        result_file.write_text(result_str, encoding="utf-8")

        if result_str != reference:
            pytest.fail(f"Different code generated.\n")
    except Exception as e:
        pytest.fail(f"Compilation failed for {code_file}: {e}")


@pytest.mark.parametrize("case_file", case_files, ids=lambda x: Path(x).stem)
@pytest.mark.parametrize("compact", [False, True], ids=["full", "compact"])
def test_cases(case_file, compact):
    run_case(case_file, compact=compact)


@pytest.mark.parametrize("example_file", example_files, ids=lambda x: Path(x).stem)
def test_examples(example_file):
    example_file = Path(example_file)
    result_file = (
        Path(__file__).parent / "results" / example_file.with_suffix(".ic10").name
    )
    reference_file = result_file.with_suffix(".ref")
    run_case(example_file, result_file, reference_file)


if __name__ == "__main__":
    for compact in [False, True]:
        suffix = ".compact" if compact else ""
        for c in case_files:
            run_case(
                c,
                write_reference=True,
                compact=compact,
            )

        for e in example_files:
            run_case(
                e,
                Path(__file__).parent
                / "results"
                / Path(e).with_suffix(suffix + ".ic10").name,
                Path(__file__).parent
                / "results"
                / Path(e).with_suffix(suffix + ".ref").name,
                write_reference=True,
                compact=compact,
            )
