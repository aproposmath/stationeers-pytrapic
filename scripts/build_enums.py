import json
import keyword
from pathlib import Path

data = json.load(open("Enums.json", "r"))

generated_types = set()

file_code = f"from enum import IntEnum as _IntEnum\n\n"
for collection in data.values():
    for enum_data in collection.values():
        name = enum_data["enumName"]
        if name in generated_types:
            continue
        generated_types.add(name)
        values = enum_data["values"]
        file_code += f"\nclass {name}(_IntEnum):\n"
        for value_name, value in values.items():
            if keyword.iskeyword(value_name):
                value_name += "_"
            value = value["value"]
            file_code += f"    {value_name} = {value}\n"


logic_types = data["scriptEnums"]["LogicType"]["values"]

for multiple in [False, True]:
    class_name = "_GenericStructure"
    return_type = "stationeers_pytrapic.types._DeviceLogicType"

    if multiple:
        class_name += "s"
        return_type = return_type.replace("_Device", "_Devices")

    code = f"\nclass {class_name}:\n"

    for name in logic_types:
        if keyword.iskeyword(name):
            name += "_"
        code += f"""
    @property
    def {name}(self) -> "{return_type}":
        return self.__getattr__("{name}")

    @{name}.setter
    def {name}(self, value):
        return self.__setattr__("{name}", value)
"""
    file_code += code

for name in logic_types:
    value = logic_types[name]["value"]

(
    Path(__file__).parent.parent / "src" / "stationeers_pytrapic" / "types_generated.py"
).write_text(file_code)
