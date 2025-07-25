import glob
from pathlib import Path

import pytest

from stationeers_pytrapic.compiler import *

example_files = glob.glob(str(Path(__file__).parent.parent / "examples" / "*.py"))


@pytest.mark.parametrize("example_file", example_files, ids=lambda x: Path(x).stem)
def test_examples(example_file):
    """
    Test that all example files compile without errors.
    """
    example_file = Path(example_file)
    code = example_file.read_text(encoding="utf-8")

    try:
        result = compile_code(code)

        if "error" in result:
            pytest.fail(
                f"Compilation failed for {example_file}: {result['error']}\n"
                f"Stack trace: {result.get('stack_trace', 'No stack trace available')}"
            )

        result = f"# registers: {result['num_registers']}\n# lines: {result['num_lines']}\n{result['code']}\n"
        result_file = Path(__file__).parent / "results" / example_file.with_suffix(".ic10").name
        result_file.write_text(result, encoding="utf-8")

        reference_file = result_file.with_suffix(".ref")
        # reference_file.write_text(result, encoding="utf-8")
        reference = reference_file.read_text(encoding="utf-8")

        if result != reference:
            pytest.fail(
                f"Compilation result for {example_file} does not match reference.\n"
            )
    except Exception as e:
        pytest.fail(f"Compilation failed for {example_file}: {e}")
