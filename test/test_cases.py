import glob
from pathlib import Path

import pytest

from stationeers_pytrapic.compiler import *

case_files = glob.glob(str(Path(__file__).parent / "cases" / "*.py"))


@pytest.mark.parametrize("case_file", case_files, ids=lambda x: Path(x).stem)
def test_cases(case_file):
    """
    Test that all example files compile without errors.
    """
    case_file = Path(case_file)
    code = case_file.read_text(encoding="utf-8")

    try:
        result = compile_code(code)

        if "error" in result:
            pytest.fail(
                f"Compilation failed for {case_file}: {result['error']}\n"
                f"Stack trace: {result.get('stack_trace', 'No stack trace available')}"
            )

        result = f"# registers: {result['num_registers']}\n# lines: {result['num_lines']}\n{result['code']}\n"
        result_file = case_file.with_suffix(".ic10")
        result_file.write_text(result, encoding="utf-8")

        reference_file = case_file.with_suffix(".ref")
        # reference_file.write_text(result, encoding="utf-8")
        reference = reference_file.read_text(encoding="utf-8")

        if result != reference:
            pytest.fail(f"Different code generated.\n")
    except Exception as e:
        pytest.fail(f"Compilation failed for {case_file}: {e}")
