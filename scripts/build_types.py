import keyword
import subprocess
import sys
import xml.etree.ElementTree
from pathlib import Path

__types_template = """
import enum

class logicType(enum.StrEnum):
    {logic_types}

class logicSlotType:
    {logic_slot_types}

del enum
"""


__generic_structure_header = """

class GenericStructure:
"""

__generic_structures_property = """
    @property
    def {property_name}(self) -> "stationeers_pytrapic.types.DevicesLogicType":
        return self.__getattr__("{property_name}")

    @{property_name}.setter
    def {property_name}(self, value):
        return self.__setattr__("{property_name}")
"""

__generic_structures_header = """

class GenericStructures:
"""

__generic_structure_property = """
    @property
    def {property_name}(self) -> "stationeers_pytrapic.types.DeviceLogicType":
        return self.__getattr__("{property_name}")

    @{property_name}.setter
    def {property_name}(self, value):
        return self.__setattr__("{property_name}")
"""


def parse_xml_file(xml_file: str) -> dict:
    logic_types = []
    logic_slot_types = []

    with open(xml_file, "r") as file:
        tree = xml.etree.ElementTree.parse(file)
        root = tree.getroot()

        for logic in root.findall("./Interface/Record"):
            name = logic.find("Key").text
            if name.startswith("LogicType"):
                name = name.replace("LogicType", "")
                value = name
                if keyword.iskeyword(name):
                    name = name + "_"
                logic_types.append(f"{name} = '{value}'")

            if name.startswith("LogicSlotType"):
                name = name.replace("LogicSlotType", "")
                value = name
                if keyword.iskeyword(name):
                    name = name + "_"
                logic_slot_types.append(f"{name} = '{value}'")

        structures = "from .types import DevicesByType\n\n"

        for structure in root.findall("./Things/RecordThing"):
            name = structure.find("Key").text
            if name.startswith("Structure") and not "(" in name:
                varname = name[len("Structure") :]
                structures += f"{varname}: DevicesByType = DevicesByType('{name}')\n"

    logic_types_str = "\n    ".join(logic_types)
    logic_slot_types_str = "\n    ".join(logic_slot_types)

    types_file = __types_template.format(
        logic_types=logic_types_str,
        logic_slot_types=logic_slot_types_str,
    )

    c_structures = __generic_structures_header
    c_structure = __generic_structure_header

    for logic_type in logic_types:
        property_name = logic_type.split("=")[0].strip()
        c_structures += __generic_structures_property.format(property_name=property_name)
        c_structure += __generic_structure_property.format(property_name=property_name)

    types_file += "\n\n" + c_structures + "\n\n" + c_structure

    return {"types_generated.py": types_file, "structures_generated.py": structures}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        default_path = (
            Path.home()
            / ".steam"
            / "steam"
            / "steamapps"
            / "common"
            / "Stationeers"
            / "rocketstation_Data"
            / "StreamingAssets"
            / "Language"
            / "english.xml"
        )

        if default_path.exists():
            print(f"Using default path: {default_path}")
            sys.argv.append(str(default_path))
        else:
            print(
                "Usage: python build_types.py <path_to_english.xml in stationeers data folder>"
            )
            sys.exit(1)
    for file_name, content in parse_xml_file(sys.argv[1]).items():
        out_file = (
            Path(__file__).parent.parent / "src" / "stationeers_pytrapic" / file_name
        )

        out_file.write_text(content, encoding="utf-8")

        subprocess.check_output(["black", str(out_file)], stderr=subprocess.STDOUT)

        print("Output written to", out_file)
