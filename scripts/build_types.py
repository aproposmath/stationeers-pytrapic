import json
from dataclasses import dataclass, field
from pathlib import Path

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
from stationeers_pytrapic.types import _DevicesLogicType, _DeviceLogicType, _BaseStructure, _BaseStructures, _DeviceSlotType, _DevicesSlotType, _BaseSlotType, _BaseSlotTypes, LogicType as _LT, LogicSlotType as _LST, _Register

from stationeers_pytrapic.types_generated import LogicBatchMethod
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

    def generate_code(self, multiple: bool = False, is_slot: bool = False) -> str:
        if is_slot:
            single_type = "_DeviceSlotType"
            multiple_type = "_DevicesSlotType"
            prefix = "_LST"
        else:
            single_type = "_DeviceLogicType"
            multiple_type = "_DevicesLogicType"
            prefix = "_LT"
        logic_type = multiple_type if multiple else single_type
        return_type = multiple_type if multiple else "float"
        name = self.name
        code = ""
        args = ["self"]
        args.append(f"{prefix}.{name}")
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
    name: str | None = None
    is_name_unique: bool = False
    type_name: str | None = None
    attributes: set[str] = field(default_factory=set)


@dataclass
class Structure:
    name: str
    prefab_name: str | None
    id: int | None
    properties: set[Property]
    bases: set[str]
    slots: set[Slot] = field(default_factory=set)


def get_name(name: str, multiple: bool) -> str:
    if multiple and name[-1] == 'y':
        name = name[:-1] + "ie"
    if multiple:
        name = name + "s"
    return name

def generate_generic_structure(struct: Structure, multiple: bool = False) -> str:
    code = ""
    is_base = struct.id is None
    bases = (
        ", ".join(
            [get_name("_BaseStructure", multiple)] + sorted([get_name(b, multiple) for b in struct.bases])
        )
        if not is_base
        else ""
    )
    name = get_name(struct.name, multiple)

    prefix = ""
    if multiple and not is_base:
        prefix = "_"
    classname = f"{prefix}{name}"
    code += f"class {classname}({bases}):\n"
    if not is_base:
        if struct.id is not None:
            code += f"  _hash: int = {struct.id}\n"
        if struct.prefab_name is not None:
            code += f'  _prefab_name: int = "{struct.prefab_name}"\n'
    if multiple and not is_base:
        code += f"  def __getitem__(self, name: str | int | float) -> '{classname}':\n"
        code += f"      return {classname}(name)\n"

        for mode in ["Average", "Minimum", "Maximum", "Sum"]:
            code += f"  @property\n"
            code += f"  def {mode}(self) -> {struct.name}:\n"
            code += f"      return {struct.name}(name=self._name, batch_mode=LogicBatchMethod.{mode})\n"

    struct_name = name

    for prop in sorted(struct.properties):
        code += prop.generate_code(multiple)

    for slot in sorted(struct.slots, key=lambda s: s.number):
        names = [f"slot{slot.number}"]
        if slot.name and slot.is_name_unique:
            names.append(slot.name.replace(" ", ""))

        slot_type = slot.type_name
        ret_type = f"_SlotType{slot_type}"
        if multiple:
            ret_type = ret_type + "s"

        for name in names:
            code += f"  @property\n"
            code += f"  def {name}(self) -> {ret_type}:\n"
            if name != names[0]:
                code += f"      return self.{names[0]}\n"
                continue
            if multiple:
                code += f"      return {ret_type}(self, {slot.number})\n"
            else:
                code += (
                    f"      return {ret_type}(self, {slot.number})\n"
                )

    if multiple and not is_base:
        code += f"{struct_name} : {classname} = {classname}()\n"
    return code


def parse_json_file(json_file: Path) -> dict:
    structures = []

    structure_types = set()
    P = Property
    S = Structure
    S = lambda name, props: Structure(name, None, None, props, set(), set())

    base_classes = [
        S("_BaseGas", set([P(name) for name in gases])),
        S("_BaseGasInput", set([P(name + "Input") for name in gases])),
        S("_BaseGasOutput", set([P(name + "Output") for name in gases])),
        S("_BaseGasOutput2", set([P(name + "Output2") for name in gases])),
        S("_Power", set([P("On", True), P("RequiredPower"), P("Power")])),
        S("_On", set([P("On", True)])),
        S("_Activate", set([P("Activate", True)])),
        S("_Lock", set([P("Lock", True)])),
        S("_Open", set([P("Open", True)])),
        S("_Error", set([P("Error")])),
        S("_Ratio", set([P("Ratio")])),
        S("_Maximum", set([P("Maximum")])),
        S("_SettingW", set([P("Setting", True)])),
        S("_SettingR", set([P("Setting")])),
        S("_Mode", set([P("Mode", True)])),
        S("_ModeR", set([P("Mode")])),
        S("_Temperature", set([P("Temperature"), P("Pressure")])),
        S("_PollWater", set([P("RatioPollutedWater")])),
        S("_Combustion", set([P("Combustion"), P("TotalMoles")])),
        S("_Idle", set([P("Idle")])),
        S("_ImportCount", set([P("ImportCount", True)])),
        S("_ClearMemory", set([P("ClearMemory", True, False)])),
        S("_Hydrogen", set([P("RatioHydrogen"), P("RatioLiquidHydrogen")])),
        S("_ImportCount", set([P("ImportCount")])),
        S("_ExportCount", set([P("ExportCount")])),
        S("_Volume", set([P("Volume"), P("VolumeOfLiquid")])),
        S("_Vertical", set([P("Vertical"), P("Horizontal")])),
        S("_VerticalW", set([P("Vertical", True), P("Horizontal", True)])),
        S("_RecipeHash", set([P("RecipeHash", True)])),
        S("_Charge", set([P("Charge")])),
        S("_Reagents", set([P("Reagents")])),
        S("_Quantity", set([P("Quantity")])),
    ]

    data = json.loads(json_file.read_text(encoding="utf-8"))
    pages = []
    for page in data["pages"]:
        name = page["Key"]
        if not name.startswith("ThingStructure"):
            continue

        nprops = 0
        props = extract_properties(page)
        for prop in page["LogicInsert"]:
            prop_name = extract_name(prop["LogicName"])
            if prop_name in ["NameHash", "PrefabHash", "ReferenceId"]:
                continue
            nprops += 1
        if props:
            page["_properties"] = props
            pages.append(page)

    code = __header

    code += generate_slot_types(pages)

    for page in pages:
        name = page["Key"]
        var_name = name.replace("ThingStructure", "")
        # print("Generating", var_name)
        prefab_hash = page["PrefabHash"]
        prefab_name = page["PrefabName"]
        # print(f"Processing page: {var_name}")
        properties = page["_properties"]
        slots = page.get("_slots", [])

        bases = set()
        if not properties:
            print(f"Skipping {var_name} with no properties")
            continue
        for base_class in base_classes:
            if base_class.properties.issubset(properties):
                properties = properties - base_class.properties
                bases.add(base_class.name)

        structures.append(
            Structure(var_name, prefab_name, prefab_hash, properties, bases, slots)
        )

    prop_count = {}

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


def generate_slot_types(pages):
    pass


def extract_name(s: str) -> str:
    while "<" in s:
        i0 = s.index("<")
        i1 = s.index(">")
        if i0 == 0 and i1 == len(s) - 1:
            break
        s = s[:i0] + s[i1 + 1 :]
    if s.startswith("<N:EN:"):
        s = s[6:]
    if s.endswith(">"):
        s = s[:-1]
    return s


def extract_properties(page: dict) -> set[Property]:
    properties = set()
    for prop in page["LogicInsert"]:
        prop_name = extract_name(prop["LogicName"])

        if prop_name in ["NameHash", "PrefabHash", "ReferenceId"]:
            continue

        access = prop["LogicAccessTypes"]
        can_read = "Read" in access
        can_write = "Write" in access
        properties.add(Property(prop_name, can_write, can_read))
    return properties


def extract_slots(page: dict, slot_types: dict) -> list[Slot]:
    res = list()
    slots = page["SlotInserts"]
    slot_names_count = dict()
    for slot in slots:
        name = extract_name(slot["SlotName"])
        slot_names_count[name] = slot_names_count.get(name, 0) + 1
        slot_index = slot["SlotIndex"]
        slot_name = name
        res.append(Slot(slot_index, slot_name))
    for insert in page["LogicSlotInsert"]:
        name = extract_name(insert["LogicName"])
        islots = [int(s) for s in insert["LogicAccessTypes"].split(",")]
        for si in islots:
            res[si].attributes.add(name)
    for slot in res:
        slot.is_name_unique = slot_names_count[slot.name] == 1
        attrs = tuple(sorted(slot.attributes))
        if attrs and slot.is_name_unique and attrs not in slot_types:
            name = slot.name
            if name[-1] in "0123456789":
                name = " ".join(name.split(" ")[:-1])
            name = name.replace(" ", "")
            slot_types[attrs] = name
            print("New slot type:", name, attrs)
            slot.type_name = name
    return res


def generate_slot_types(pages):
    slot_types = {}
    for page in pages:
        slots = extract_slots(page, slot_types)
        if not slots:
            continue
        page["_slots"] = slots

    common_slots = set(list(slot_types.keys())[0])
    for t in slot_types.keys():
        common_slots.intersection_update(set(t))

    common_tuple = tuple(sorted(common_slots))
    if common_tuple in slot_types:
        old_name = slot_types[common_tuple]
        new_name = "Common"
        slot_types[common_tuple] = new_name
        for p in pages:
            if "_slots" not in p:
                continue
            for s in p["_slots"]:
                if s.type_name == old_name:
                    s.type_name = new_name

    for attrs, name in slot_types.items():
        print(f"  {name}: {attrs}")

    for p in pages:
        if "_slots" not in p:
            continue
        for s in p["_slots"]:
            if s.type_name is None:
                attrs = tuple(sorted(s.attributes))
                s.attributes = s.attributes - common_slots
                if attrs in slot_types:
                    s.type_name = slot_types[attrs]
                else:
                    print("UNKNOWN SLOT TYPE:", p["Key"], s, attrs)
                    s.type_name = "Common"

    for attrs in list(slot_types.keys()):
        if set(attrs) == common_slots:
            continue
        type_name = slot_types.pop(attrs)
        new_attrs = tuple(sorted(set(attrs) - common_slots))
        slot_types[new_attrs] = type_name
        print(type_name, "\n\t\t", " ".join(new_attrs))

    slot_types = {v: k for k, v in slot_types.items()}
    common_attrs = slot_types.pop("Common")

    def make_slot_class(name, attrs, multiple=False):
        is_common = name == "Common"
        base_name = "_BaseSlotType" if is_common else "_SlotTypeCommon"

        if multiple:
            name += "s"
            base_name += "s"
        code = f"class _SlotType{name}({base_name}):\n"
        for attr in attrs:
            code += Property(attr, True, True).generate_code(multiple, True)

        return code

    code = make_slot_class("Common", common_attrs)
    code += make_slot_class("Common", common_attrs, True)

    for name in sorted(slot_types.keys()):
        code += make_slot_class(name, slot_types[name])
        code += make_slot_class(name, slot_types[name], True)

    return code


if __name__ == "__main__":
    json_file = Path(__file__).parent / "Stationpedia.json"
    for file_name, content in parse_json_file(json_file).items():
        out_file = (
            Path(__file__).parent.parent / "src" / "stationeers_pytrapic" / file_name
        )

        out_file.write_text(content, encoding="utf-8")

        # subprocess.check_output(["black", str(out_file)], stderr=subprocess.STDOUT)

        print("Output written to", out_file)
