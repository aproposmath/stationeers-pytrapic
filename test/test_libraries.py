import glob
from pathlib import Path

import astroid
from astroid import nodes
import pytest
from test_cases import run_case

from stationeers_pytrapic.compiler import *

script_files = glob.glob(str(Path(__file__).parent / "mod_scripts" / "*.py"))


def find_imported_libraries(src):
    libraries = {}

    tree = astroid.parse(src)
    for node in tree.body:
        if isinstance(node, nodes.ImportFrom) and node.modname == "library":
            for name, _ in node.names:
                libraries[name] = load_library(name)
    return libraries


def load_library(lib_name):
    if not lib_name.endswith(".py"):
        lib_name += ".py"
    src = (Path(__file__).parent / "mod_libraries" / lib_name).read_text()
    return src


def load_script(script_name):
    if not script_name.endswith(".py"):
        script_name += ".py"
    src = (Path(__file__).parent / "mod_scripts" / script_name).read_text()
    modules = find_imported_libraries(src)
    modules[""] = src
    return modules


@pytest.mark.parametrize("script_file", script_files, ids=lambda x: Path(x).stem)
@pytest.mark.parametrize("compact", [False, True], ids=["full", "compact"])
def test_scripts(script_file, compact):
    modules = load_script(Path(script_file).name)
    run_case(script_file, compact=compact, modules=modules)


if __name__ == "__main__":
    # Compiler._raise_exceptions = True
    import sys

    if len(sys.argv) > 1:
        script_files = sys.argv[1:]
    for compact in [False, True]:
        for file in script_files:
            modules = load_script(Path(file).name)
            run_case(
                file,
                write_reference=True,
                compact=compact,
                modules=modules,
            )
