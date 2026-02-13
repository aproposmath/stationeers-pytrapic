import re
from pathlib import Path

from stationeers_pytrapic import compiler

_try_url = "https://aproposmath.github.io/stationeers-pytrapic?fileUrl=https://raw.githubusercontent.com/aproposmath/stationeers-pytrapic/refs/heads/main/src/stationeers_pytrapic/examples/"

_collapse_header = """
<details>
<summary id="{tag}"><strong>{name}</strong></summary>
"""

_collapse_footer = """
</details>
"""

_table_template = """
<table>
<tr><th style="padding:2px 6px;">Python&nbsp;&nbsp;<a href="{url}" target="_blank" rel="noopener noreferrer">Open in online editor</a>
</th></tr>
<tr><td style="padding:2px 6px;">

```py
{py_src}
```

</td></tr>
<tr><th style="padding:2px 6px;">IC10</th></tr>
<tr><td style="padding:2px 6px;">

```asm
{ic10_src}
```

</td></tr>
</table>
"""


def compile_examples(examples, collapse=True):
    examples_dir = Path(compiler.__file__).parent / "examples"
    result = ""
    options = compiler.CompileOptions(
        compact=False,
        remove_labels=True,
        inline_functions=True,
    )
    for example in examples:
        py_src = (examples_dir / example).read_text(encoding="utf-8").strip().replace("\n\n\n", "\n\n")
        data = compiler.compile_code(py_src, options)
        # print(data)
        ic10_src = data['code'].strip()
        name = example.removesuffix(".py").replace("_", " ").title()
        markdown = _table_template.format(
            py_src=py_src,
            ic10_src=ic10_src,
            name=name,
            url=_try_url + example,
        )

        header_template = _collapse_header if collapse else ""
        footer = _collapse_footer if collapse else ""
        result += header_template.format(name=name, tag="example-"+example.replace("_","-").replace(".", "-")) + markdown + footer
    return result


def get_examples():
    # Implement your logic here to generate examples
    return compile_examples(
        [
            "logic_types.py",
            "batch_operations.py",
            "loops.py",
            "misc.py",
            "stack.py",
            "constexpr.py",
            "intrinsics.py",
            "compiler_options.py",
        ],
        True,
    ).strip()


def get_simple_examples():
    # Implement your logic here to generate simple examples
    return compile_examples(["solar.py"], False).strip()


def replace_section(text: str, header: str, new_body: str) -> str:
    pattern = re.compile(rf"(?ms)^({re.escape(header)}\s*\n).*?(?=\n##|\Z)")
    replacement = rf"\1{new_body.rstrip()}\n"
    if pattern.search(text):
        return pattern.sub(replacement, text, count=1)
    return text


def main() -> None:
    readme_path = Path("README.md")
    readme = readme_path.read_text(encoding="utf-8")

    simple_examples_body = (
        "More examples are [below](#examples)\n\n" + get_simple_examples()
    )
    readme = replace_section(readme, "## Simple Example", simple_examples_body)

    examples_body = get_examples()
    readme = replace_section(readme, "## Examples", examples_body)

    readme_path.write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    main()
