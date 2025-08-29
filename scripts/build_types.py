from dataclasses import dataclass
from pathlib import Path
import json

gases = [
    "RatioCarbonDioxide",
    "RatioLiquidCarbonDioxide",
    "RatioLiquidNitrogen",
    "RatioLiquidNitrousOxide",
    "RatioLiquidOxygen",
    "RatioLiquidPollutant",
    "RatioLiquidVolatiles",
    "RatioNitrogen",
    "RatioNitrousOxide",
    "RatioOxygen",
    "RatioPollutant",
    "RatioSteam",
    "RatioVolatiles",
    "RatioWater",
]

__header = """
from stationeers_pytrapic.types import _DevicesLogicType, _DeviceLogicType, _BaseStructure, _BaseStructures
"""


@dataclass
class Property:
    name: str
    can_write: bool = False
    can_read: bool = True

    def __lt__(self, other: "Property") -> bool:
        return (self.name, self.can_read, self.can_write) < (
            other.name,
            other.can_read,
            other.can_write,
        )

    def __hash__(self):
        return hash((self.name, self.can_read, self.can_write))

    def generate_code(self, multiple: bool = False) -> str:
        logic_type = "_DevicesLogicType" if multiple else "_DeviceLogicType"
        return_type = "_DevicesLogicType" if multiple else "float"
        name = self.name
        code = ""
        args = []
        if multiple:
            args.append("self._hash")
        else:
            args.append("self")
            args.append("self._id")
        args.append(f"'{name}'")
        if multiple:
            args.append("self._name")
        args = ", ".join(args)
        if self.can_read or self.can_write:
            code += f"  @property\n"
            code += f"  def {name}(self) -> {return_type}:\n"
            code += f"      return {logic_type}({args})\n"

        if self.can_write:
            code += f"  @{name}.setter\n"
            code += f"  def {name}(self, value: int | float):\n"
            code += f"      pass\n"
        return code


@dataclass
class Slot:
    number: int


@dataclass
class Structure:
    name: str
    id: int | None
    properties: set[Property]
    # slots: set[Slot]
    bases: set[str]


def generate_generic_structure(struct: Structure, multiple: bool = False) -> str:
    code = ""
    is_base = struct.id is None
    suffix = "s" if multiple else ""
    bases = (
        ", ".join(
            [f"_BaseStructure" + suffix] + sorted([b + suffix for b in struct.bases])
        )
        if not is_base
        else ""
    )
    name = struct.name + suffix
    prefix = ""
    if multiple and not is_base:
        prefix = "_"
    classname = f"{prefix}{name}"
    code += f"class {classname}({bases}):\n"
    if not is_base:
        code += f"  _hash: int = {struct.id}\n"
    if multiple and not is_base:
        code += f"  def __getitem__(self, name: str | int | float) -> '{classname}':\n"
        code += f"      return {classname}(name)\n"

    for prop in sorted(struct.properties):
        code += prop.generate_code(multiple)
    if multiple and not is_base:
        code += f"{name} : {classname} = {classname}()\n"
    return code


def parse_json_file(json_file: Path) -> dict:
    structures = []

    structure_types = set()
    P = Property
    S = Structure

    base_classes = [
        S("_BaseGas", None, set([P(name) for name in gases]), []),
        S("_BaseGasInput", None, set([P(name + "Input") for name in gases]), []),
        S("_BaseGasOutput", None, set([P(name + "Output") for name in gases]), []),
        S("_BaseGasOutput2", None, set([P(name + "Output2") for name in gases]), []),
        S("_Power", None, set([P("On", True), P("RequiredPower"), P("Power")]), []),
        S("_On", None, set([P("On", True)]), []),
        S("_Activate", None, set([P("Activate", True)]), []),
        S("_Lock", None, set([P("Lock", True)]), []),
        S("_Open", None, set([P("Open", True)]), []),
        S("_Error", None, set([P("Error")]), []),
        S("_Ratio", None, set([P("Ratio")]), []),
        S("_Maximum", None, set([P("Maximum")]), []),
        S("_SettingW", None, set([P("Setting", True)]), []),
        S("_SettingR", None, set([P("Setting")]), []),
        S("_Mode", None, set([P("Mode", True)]), []),
        S("_ModeR", None, set([P("Mode")]), []),
        S("_Temperature", None, set([P("Temperature"), P("Pressure")]), []),
        S("_PollWater", None, set([P("RatioPollutedWater")]), []),
        S("_Combustion", None, set([P("Combustion"), P("TotalMoles")]), []),
        S("_Idle", None, set([P("Idle")]), []),
        S("_ImportCount", None, set([P("ImportCount", True)]), []),
        S("_ClearMemory", None, set([P("ClearMemory", True, False)]), []),
        S("_Hydrogen", None, set([P("RatioHydrogen"), P("RatioLiquidHydrogen")]), []),
        S("_ImportCount", None, set([P("ImportCount")]), []),
        S("_ExportCount", None, set([P("ExportCount")]), []),
        S("_Volume", None, set([P("Volume"), P("VolumeOfLiquid")]), []),
        S("_Vertical", None, set([P("Vertical"), P("Horizontal")]), []),
        S("_VerticalW", None, set([P("Vertical", True), P("Horizontal", True)]), []),
        S("_RecipeHash", None, set([P("RecipeHash", True)]), []),
        S("_Charge", None, set([P("Charge")]), []),
        S("_Reagents", None, set([P("Reagents")]), []),
        S("_Quantity", None, set([P("Quantity")]), []),
    ]

    data = json.loads(json_file.read_text(encoding="utf-8"))
    for page in data["pages"]:
        name = page["Key"]
        if not name.startswith("ThingStructure"):
            print("skipping", name)
            continue

        var_name = name.replace("ThingStructure", "")
        print("Generating", var_name)
        prefab_hash = page["PrefabHash"]
        # print(f"Processing page: {var_name}")
        properties = set()
        for prop in page["LogicInsert"]:
            prop_name = prop["LogicName"]
            while "<" in prop_name:
                i0 = prop_name.index("<")
                i1 = prop_name.index(">")
                prop_name = prop_name[:i0] + prop_name[i1 + 1 :]

            if prop_name in ["NameHash", "PrefabHash", "ReferenceId"]:
                continue
            access = prop["LogicAccessTypes"]
            can_read = "Read" in access
            can_write = "Write" in access
            properties.add(Property(prop_name, can_write, can_read))
            # print(f"  {'r' if can_read else ' '}{'w' if can_write else ' '} {prop_name}")

        bases = set()
        if properties:
            for base_class in base_classes:
                if base_class.properties.issubset(properties):
                    properties = properties - base_class.properties
                    bases.add(base_class.name)

            structures.append(Structure(var_name, prefab_hash, properties, bases))

            # prop_name = prop.find("Key").text
            # can_read = prop.find("CanRead").text == "true"
            # can_write = prop.find("CanWrite").text == "true"
            # properties.append(Property(name=prop_name, can_read=can_read, can_write=can_write))
        # if name.startswith("LogicType"):
        #     name = name.replace("LogicType", "")
        #     value = name
        #     if keyword.iskeyword(name):
        #         name = name + "_"
        #     logic_types.append(f"{name} = '{value}'")
        #
        # if name.startswith("LogicSlotType"):
        #     name = name.replace("LogicSlotType", "")
        #     value = name
        #     if keyword.iskeyword(name):
        #         name = name + "_"
        #     logic_slot_types.append(f"{name} = '{value}'")

    prop_count = {}

    code = __header

    structures = base_classes + structures
    for struct in structures:
        code += generate_generic_structure(struct, False)
        code += generate_generic_structure(struct, True)
        for p in struct.properties:
            prop_count[p.name] = prop_count.get(p.name, 0) + 1

    for struct in structures:
        structure_types.add(
            tuple(
                sorted(
                    [
                        (p.name, p.can_read, p.can_write)
                        for p in struct.properties
                        if prop_count[p.name] < 80
                    ]
                )
            )
        )
    print("Found structures:", len(structures))
    print("Found structure types:", len(structure_types))
    print("Found properties", len(prop_count))
    print("Property counts:")
    for prop, count in prop_count.items():
        if count > 10:
            print(f"  {prop}: {count}")

    # print("Structure types:")
    # for struct_type in structure_types:
    #     print("  ", struct_type)
    return {"structures_generated.py": code}


if __name__ == "__main__":
    json_file = Path(__file__).parent / "Stationpedia.json"
    for file_name, content in parse_json_file(json_file).items():
        out_file = (
            Path(__file__).parent.parent / "src" / "stationeers_pytrapic" / file_name
        )

        out_file.write_text(content, encoding="utf-8")

        # subprocess.check_output(["black", str(out_file)], stderr=subprocess.STDOUT)

        print("Output written to", out_file)
