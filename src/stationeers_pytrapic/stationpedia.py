import base64
import json
from pathlib import Path


def highlight(code: str) -> str:
    from .mod_daemon import highlight as _highlight

    return f"<margin=3em>{_highlight(code)}</margin>"


def get_example_page(name, code_file, description):
    code = (Path(__file__).parent / "examples" / f"{code_file}.py").read_text(
        encoding="utf-8"
    )

    header = f"""
<align=right><size=110%><color=green><link=pytrapic>Back to PyTrapIC main page</link></color></size></align>

{description}

"""
    copy_code = f"""

Click the code below to copy the code.
<margin=3em>
<color=#808080><link=Clipboard>{code}</link></color>
</margin>
"""

    text = header + highlight(code) + copy_code

    return {
        "key": f"pytrapic_example_{name}",
        "title": f"PyTrapIC Example - {name.capitalize()}",
        "text": text,
    }


def get_pages():
    main_text = readme
    examples = [
        ("logic_types", "Logic Types"),
        ("batch_operations", "Batch Operations"),
        ("loops", "Loops"),
        ("misc", "Miscellaneous"),
        ("stack", "Stack"),
        ("constexpr", "Constexpr"),
        ("intrinsics", "Intrinsics"),
        ("compiler_options", "Compiler Options"),
        ("solar", "Solar Panel Alignment"),
        ("airlock", "Simple Airlock"),
    ]

    example_links = ""
    pages = []

    for name, description in examples:
        pages.append(get_example_page(name, name, description))
        example_links += f'• <color=green><link="pytrapic_example_{name}">{description}</link></color>\n'

    main_text = readme.replace("__EXAMPLES_LIST__", example_links.strip())

    pages.append(
        {
            "key": "pytrapic",
            "title": "PyTrapIC",
            "text": main_text,
        },
    )

    return pages


def get_pages_encoded() -> str:
    pages = get_pages()
    json_str = json.dumps(pages)
    encoded_bytes = base64.b64encode(json_str.encode("utf-8"))
    encoded_str = encoded_bytes.decode("utf-8")
    return encoded_str


_lib_code = """from stationeers_pytrapic.symbols import *
from .library import your_lib_name
your_lib_name.init()
while True:
    your_lib_name.update()
"""

readme = (
    f"""
This mod lets you write code for Stationeers' ICs in Python instead of IC10 assembly. Python is converted to IC10 when you <b>Export</b> from the in-game editor.

<h1>Features</h1>
• Write code in Python (only subset of Python features supported)
• Import code from <b>Libraries</b> (local or workshop) for easy code sharing/reuse
• Syntax highlighting  
• Auto-completion (<color="yellow">Tab</color> key)
• IC10 preview
• Compile errors shown as tooltips  
• All IC10 commands available as Python functions (intrinsics)

<h1>Getting Started</h1>

The <color=yellow><b>first line</b></color> in your code must <color=yellow><b>exactly match</b></color>:
<color=#a0a0a0><margin=3em><link=Clipboard>from stationeers_pytrapic.symbols import *</link></margin></color>
Only then will the mod recognize it as Python code. See the <b>Examples</b> below. You can copy each example code to the clipboard by clicking the code block at the very bottom of the example page.

<h1>Examples</h1>

__EXAMPLES_LIST__

<h1>Usage Notes</h1>
• Save-compatible: Remove/add it any time without breaking your savegames
• Multiplayer-compatible: Also works if you are the only one using it (untested)
• ICs still run IC10, not Python (Python code will be transpiled to IC10 on export)
• Start Python code with:<br><i>from stationeers_pytrapic.symbols import *</i>  
• Function args/returns use top stack slots (511, 510, ...), otherwise the stack is not used by the transpiler
• Structures match Stationpedia names (without "Structure", e.g. "ArcFurnace")  
• Access structures by pin:<indent=40%>WallHeater(d0)</indent>
• Or all of them by type (append "s"):<indent=40%>WallHeaters</indent>
• Access by name:<indent=40%>WallHeaters["Greenhouse"]</indent>

<h1>Libraries</h1>
If you have some python code stored in a library named <color=#a0a0a0><i>your_lib_name</i></color> and your library provides two functions <color=#a0a0a0><i>init()</i></color> and <color=#a0a0a0><i>update()</i></color>, you can use it like this on a chip:

{highlight(_lib_code)}

""".replace(
        "<h1>", "<b><size=150%><color=#3060ff>"
    )
    .replace("</h1>", "</color></size></b>")
    .replace("<h2>", "<b><size=100%><color=#3060ff>")
    .replace("</h2>", "</color></size></b>")
)
