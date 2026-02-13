import re
from pathlib import Path

from stationeers_pytrapic import compiler

_try_url = "https://aproposmath.github.io/stationeers-pytrapic?fileUrl=https://raw.githubusercontent.com/aproposmath/stationeers-pytrapic/refs/heads/main/src/stationeers_pytrapic/examples/"

_table_template = """
<details{open_attr}>
<summary><strong>{name}</strong> — <a href="{url}" target="_blank" rel="noopener noreferrer">Try it</a></summary>

<table>
<th>Python</th>
<th>IC10</th>
<tr>
<td>
```py
{py_src}
```
</td>
<td>
```asm
{ic10_src}
```
</td>
</table>
</details>
"""


def compile_examples(examples, open_attr=""):
    examples_dir = Path(compiler.__file__).parent / "examples"
    result = ""
    for example in examples:
        py_src = (examples_dir / example).read_text(encoding="utf-8").strip()
        ic10_src = compiler.compile_code(py_src)["code"].strip()
        name = example.removesuffix(".py").replace("_", " ").title()
        result += _table_template.format(
            py_src=py_src,
            ic10_src=ic10_src,
            name=name,
            url=_try_url + example,
            open_attr=open_attr,
        )
    return result


def get_examples():
    # Implement your logic here to generate examples
    return compile_examples(["constexpr.py"])


def get_simple_examples():
    # Implement your logic here to generate simple examples
    return compile_examples(["solar.py"], " open")


def replace_section(text: str, header: str, new_body: str) -> str:
    pattern = re.compile(rf"(?ms)^({re.escape(header)}\s*\n).*?(?=\n##|\Z)")
    replacement = rf"\1{new_body.rstrip()}\n"
    if pattern.search(text):
        return pattern.sub(replacement, text, count=1)
    return text


def main() -> None:
    readme_path = Path("README.md")
    readme = readme_path.read_text(encoding="utf-8")

    simple_examples_body = get_simple_examples()
    readme = replace_section(readme, "## Simple Examples", simple_examples_body)

    examples_body = get_examples()
    readme = replace_section(readme, "## Examples", examples_body)

    readme_path.write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    main()
