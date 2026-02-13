import json
import keyword
import re
import subprocess
from pathlib import Path

import requests
from bs4 import BeautifulSoup

type_mapping = {
    "r?": "_Register",
    "d?": "Device",
    "num": "float",
    "r": "Register",
    "d": "_Device",
    "Device": "_Device",
    "Register": "_Register",
    "logicType": "LogicType|int|float",
    "reagentMode": "LogicReagentMode|int|float",
    "slotIndex": "int|float",
    "logicSlotType": "LogicSlotType|int|float",
    "deviceHash": "_deviceHash|int|float",
    "batchMode": "LogicBatchMethod|int|float",
    "nameHash": "int|float",
}


def parse_dl_entry(entry):
    # Extract the instruction + param string
    dt = entry.find("dt")
    if not dt:
        raise ValueError("No <dt> found in entry")

    pre = dt.find("pre")
    if not pre:
        raise ValueError("No <pre> found in <dt>")

    raw_text = pre.get_text(strip=True)
    parts = raw_text.split()
    if not parts:
        raise ValueError("No parts found in raw_text")

    name = parts[0]
    param_specs = parts[1:]

    parameters = []
    for _, spec in enumerate(param_specs):
        # Match param format like: a(r|num) or b(r?) or label(hash)
        match = re.match(r"(\w+)\(([^)]+)\)", spec)
        if match:
            param_name = match.group(1)
            param_type = match.group(2)
        else:
            param_name = ""
            param_type = spec

        param_type = param_type.replace("r?", "Register")
        param_type = param_type.replace("d?", "Device")
        param_type = param_type.replace("num", "float")
        param_type = param_type.replace("id", "float")

        for t in [
            "Device",
            "Register",
            "logicType",
            "reagentMode",
            "slotIndex",
            "logicSlotType",
            "deviceHash",
            "batchMode",
            "nameHash",
        ]:
            param_type = param_type.replace(t, type_mapping[t])

        parameters.append({"name": param_name, "type": param_type})

    if (
        len(parameters) > 1
        and parameters[0]["name"] == ""
        and parameters[1]["name"] == "a"
    ):
        parameters[0]["name"] = "output"

    # Extract description from <dd><p>
    dd = entry.find("dd")
    description = ""
    if dd:
        p = dd.find("p")
        if p:
            description = p.get_text(strip=True)

    if (
        (
            name.startswith("l")
            or name.startswith("get")
            or description.startswith("Register = ")
        )
        and parameters[0]["type"] == "_Register"
        and parameters[0]["name"] == ""
    ):
        # The first parameter is an output parameter in load/get instructions,
        # or if the descriptions starts with "Register = "
        parameters[0]["name"] = "output"

    description = description.replace("Register", "output")

    description = description.replace("output =", "Returns").strip()

    for i, p in enumerate(parameters):
        if p["name"] == "":
            param_index = i if parameters[0]["name"] == "output" else i + 1
            p["name"] = f"param{param_index}"
        if ["name"] != "output" and p["type"] == "_Register":
            p["type"] = "float"

    return {
        "name": name,
        "parameters": parameters,
        "description": description,
        "returns": "None",
    }


def fetch_ic10_instructions():

    html_path = Path("ic10.html")

    if not html_path.exists():
        url = "https://stationeers-wiki.com/IC10/instructions"
        response = requests.get(url)
        response.raise_for_status()
        html_path.write_text(response.text)

    html = html_path.read_text()

    soup = BeautifulSoup(html, "html.parser")
    instructions_data = []

    entries = soup.find_all("dl")

    for entry in entries:
        res = parse_dl_entry(entry)
        if res:
            instructions_data.append(res)

    return instructions_data


def generate_intrinsics_py(instructions):
    builtins_code = []
    for instr in instructions:
        name = instr["name"]

        return_type = None
        if len(instr["parameters"]) > 0 and instr["parameters"][0]["name"] == "output":
            return_type = instr["parameters"][0]["type"]
            instr["parameters"] = instr["parameters"][1:]

        params = ", ".join(f"{p['name']}: {p['type']}" for p in instr["parameters"])
        description = instr.get("description", "").replace('"', '\\"')

        if keyword.iskeyword(name):
            name += "_"

        expr = '""'
        args = ", ".join(p["name"] for p in instr["parameters"])
        opcode = instr["name"]
        if len(instr["parameters"]):
            expr = "} {".join(p["name"] for p in instr["parameters"])
            expr = 'f"{' + expr + '}"'
        output = "_Register('invalid')" if return_type else "None"
        body = f"return _IC10('{opcode}', [{args}], {output})"
        code = f"""
def {name}({params}) -> {return_type}:
    \"\"\"{description}\"\"\"
    {body}
"""
        builtins_code.append(code.strip())

    code = f"""# This file is auto-generated from IC10 instructions_data
from .types import *
from .types_generated import *
from .types import IC10 as _IC10, IC10Register as _Register

"""
    code += "\n\n".join(builtins_code)
    code += """
def HASH(name: str) -> float:
    from .types import compute_hash
    return compute_hash(name)
def STR(s: str) -> float:
    from .types import compute_string
    return compute_string(s)
"""
    out_path = Path("../src/stationeers_pytrapic/intrinsics.py")
    out_path.write_text(code, encoding="utf-8")
    subprocess.check_output(["black", str(out_path)], stderr=subprocess.STDOUT)
    print("Output written to", out_path)


def generate_highlight_json(instructions):
    keywords = [f"r{i}" for i in range(16)]
    keywords += [f"d{i}" for i in range(16)]

    data = {
        "keywords": keywords,
        "instructions": [instr["name"] for instr in instructions],
    }

    with open("../webapp/src/ic10.json", "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False,
        )


if __name__ == "__main__":
    instructions = fetch_ic10_instructions()
    generate_intrinsics_py(instructions)
    generate_highlight_json(instructions)
