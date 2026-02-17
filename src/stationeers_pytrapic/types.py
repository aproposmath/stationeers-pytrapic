import enum
import math
import sys
from dataclasses import dataclass, field
import copy

from astroid import nodes

from .types_generated import *
from .types_generated import _GenericStructure, _GenericStructures
from .utils import OutputMode, format_enum, get_loop_ancestor, calc_hash

from . import utils


@dataclass
class IC10Register:
    name: str
    scope: str = ""
    code_expr: "str | _BaseStructure | _BaseStructures" = ""
    _lifetime: range | None = None
    _color: int = -1
    _is_intermediate: bool = False

    nodes_reading: list[nodes.NodeNG] = field(default_factory=list)
    nodes_writing: list[nodes.NodeNG] = field(default_factory=list)

    def __hash__(self):
        return hash((self.code_expr, self.scope))

    @property
    def is_overwritten(self) -> int:
        return len(self.nodes_writing) > 1

    @property
    def is_written(self) -> int:
        return len(self.nodes_writing)

    @property
    def is_read(self) -> int:
        return len(self.nodes_reading)

    @property
    def is_builtin_object(self) -> bool:
        return isinstance(self.code_expr, _BaseStructure) or isinstance(
            self.code_expr, _BaseStructures
        )

    @property
    def is_register(self) -> bool:
        return isinstance(self.code_expr, str) and self.code_expr.startswith(
            "__register."
        )

    @property
    def lifetime(self):
        if self._lifetime is None:
            if self._is_intermediate:
                n = self.nodes_writing[0].lineno
                self._lifetime = range(n, n + 1)
                return self._lifetime

            for node in self.nodes_writing:
                if node.scope().name == "":
                    self._lifetime = range(0, sys.maxsize)
                    break

        if self._lifetime is None:
            all_nodes = [
                get_loop_ancestor(n) for n in self.nodes_reading + self.nodes_writing
            ]
            min_line = (
                min(node.lineno for node in all_nodes) if all_nodes else sys.maxsize
            )
            max_line = max(node.end_lineno for node in all_nodes) if all_nodes else -1
            self._lifetime = range(min_line, max_line + 1)
        return self._lifetime


@dataclass
class IC10Operand:
    """
    An operand for an IC10 instruction, can be a register or an immediate value
    """

    value: str | float | int | IC10Register

    def __init__(self, value: str | float | int | IC10Register):
        if isinstance(value, _Device):
            value = value._dev_id._id or "db"
        elif isinstance(value, DeviceId):
            value = value._id or "db"
        elif isinstance(value, float) and int(value) == value:
            value = int(value)
        self.value = value

    @property
    def is_register(self) -> bool:
        return isinstance(self.value, IC10Register)

    def to_string(self) -> str:
        if isinstance(self.value, IC10Register):
            return self.value.code_expr
        elif isinstance(self.value, float):
            absval = abs(self.value)
            if absval >= 0.1:
                return f"{self.value:.16g}"
            if absval == 0:
                return "0"
            ndigits = 16 + -int(math.log10(abs(self.value)))
            format_str = f"{{value:.{ndigits}f}}"
            return format_str.format(value=self.value).rstrip("0").rstrip(".")
        elif isinstance(self.value, int):
            return utils.format_int(self.value)
        return str(self.value)


@dataclass
class IC10Instruction:
    op: str  # The ic10 instruction name
    inputs: list[IC10Operand] = field(default_factory=list)
    output: IC10Register | None = None  # output register (or None if no output)
    comment: str = ""
    indent: int = 0
    lineno: int | None = (
        None  # ic10 line number, this is set later and might change during compile passes
    )
    node: nodes.NodeNG = None

    @property
    def registers(self) -> list[IC10Register]:
        regs = []
        if self.output:
            regs.append(self.output)
        for inp in self.inputs:
            if inp.is_register:
                regs.append(inp.value)
        return regs

    def to_string(self, shift=2) -> str:
        from .compile_pass import CompilerError

        for inp in self.inputs:
            if not isinstance(inp, IC10Operand):
                raise CompilerError(
                    f"Input must be an IC10Operand, have {inp}", self.node
                )
            if isinstance(inp.value, _DevicesLogicType):
                raise CompilerError(
                    f"Missing LogicBatchMethod in expression",
                    self.node,
                )

        code = " " * self.indent * shift + self.op
        if self.output:
            if not isinstance(self.output, IC10Register):

                raise CompilerError(
                    f"Output must be a register, have '{self.output}' of type {type(self.output)}",
                    self.node,
                )
            code += f" {self.output.code_expr}"
        for inp in self.inputs:
            code += f" {inp.to_string()}"
        if self.comment:
            code += f"  # {self.comment}"
        return code

    def __init__(self, op: str, inputs=None, output=None, comment="", indent=0):
        inputs = inputs or []
        for i in range(len(inputs)):
            value = inputs[i]
            if isinstance(value, enum.IntEnum):
                value = format_enum(value)
            if not isinstance(value, IC10Operand):
                inputs[i] = IC10Operand(value)
        self.op = op
        self.inputs = inputs if inputs is not None else []
        self.output = output
        self.comment = comment
        self.indent = indent

        if isinstance(output, str) and output.startswith("__register."):
            raise ValueError("Output cannot be a string register name")


IC10 = IC10Instruction
_Register = IC10Register


def encode_data(data: dict) -> str:
    """Encodes a dictionary into a base64-encoded, zlib-compressed string. Replaces + and / with _ and - respectively, and removes padding (=) to make it URL-safe."""
    import base64
    import json
    import zlib

    return (
        base64.b64encode(zlib.compress(json.dumps(data).encode()))
        .decode()
        .replace("+", "-")
        .replace("/", "_")
        .replace("=", "")
    )


def decode_data(encoded: str) -> dict:
    """Decodes a base64-encoded, zlib-compressed string back into a dictionary. Replaces - and _ with + and / respectively, and adds padding (=) if necessary."""
    import base64
    import json
    import zlib

    if len(encoded) % 4:
        encoded += "=" * (4 - len(encoded) % 4)

    encoded = encoded.replace("-", "+").replace("_", "/")
    return json.loads(zlib.decompress(base64.b64decode(encoded)).decode())


def _apply_output_mode(
    num_value: float, string_value: str, output_mode: OutputMode
) -> float:
    if output_mode is None:
        output_mode = utils._output_mode

    if output_mode == OutputMode.VERBOSE:
        return string_value

    if output_mode == OutputMode.NUMERIC:
        return num_value

    return num_value if len(str(num_value)) < len(string_value) else string_value


def compute_hash(name: int | str | _Register, output_mode=None) -> int | str:
    if not isinstance(name, str):
        return name

    if name.startswith("__register."):
        return name

    if name == "":
        raise ValueError("Name cannot be an empty string")

    if name[0] == '"' and name[-1] == '"':
        name = name[1:-1]

    if name.startswith('HASH("') and name.endswith('")'):
        name = name[6:-2]

    hash_str = f'HASH("{name}")'
    val = calc_hash(name)

    return _apply_output_mode(val, hash_str, output_mode)


def compute_string(s: str, output_mode=None) -> float:
    val = 0
    for char in s[::-1]:
        val = val << 8 | ord(char)
    return _apply_output_mode(val, f'STR("{s}")', output_mode)


class _deviceHash(float):
    pass


def device_hash(cls: type) -> _deviceHash:
    return compute_hash(cls._prefab_name)


class _nameHash(float):
    pass


class _slotIndex(int):
    pass


@dataclass
class DeviceId:
    _id: str | None = None
    _is_ref_id: bool = False


@dataclass
class _BaseAccess:
    _obj: "_BaseStructure"

    @property
    def _dev_id(self) -> DeviceId:
        return self._obj._dev_id

    @property
    def _id(self) -> str:
        return self._dev_id._id

    @property
    def _is_ref_id(self) -> str:
        return self._dev_id._is_ref_id

    @property
    def _prefab_name(self) -> str | int | None:
        return self._obj._prefab_name

    @property
    def _prefab_hash(self) -> str | int | None:
        return self._obj._prefab_name


@dataclass
class _BaseBatchAccess:
    _obj: "_BaseStructures"

    @property
    def _name(self) -> str | int | None:
        return self._obj._name

    @property
    def _prefab_name(self) -> str | int | None:
        return self._obj._prefab_name

    @property
    def _name_hash(self) -> int | str | None:
        if self._name is None:
            raise ValueError(f"Name must be set in class {type(self._obj).__name__}")

        return compute_hash(self._name)

    @property
    def _device_hash(self) -> int | str | None:
        if not self._prefab_name:
            raise ValueError("Name must be set to compute name hash")

        return compute_hash(self._prefab_name)


@dataclass
class _DeviceSlotType(_BaseAccess):
    _slot_type: LogicSlotType

    @property
    def _slot_index(self) -> _slotIndex:
        return self._obj._slot_index

    def _load(self, output: _Register) -> IC10Instruction:
        return IC10Instruction(
            "ls", [self._id, self._slot_index, self._slot_type], output
        )

    def _set(self, value: float | _Register) -> IC10Instruction:
        return IC10Instruction(
            "ss", [self._id, self._slot_index, self._slot_type, value]
        )


@dataclass
class _DevicesSlotType(_BaseBatchAccess):
    _slot_type: LogicSlotType

    @property
    def _slot_index(self) -> _slotIndex:
        return self._obj._slot_index

    def _load(self, batch_mode: LogicBatchMethod):
        if self._name is None:
            return lambda r: IC10(
                "lbs",
                [self._device_hash, self._slot_index, self._slot_type, batch_mode],
                r,
            )
        else:
            return lambda r: IC10(
                "lbns",
                [
                    self._device_hash,
                    self._name_hash,
                    self._slot_index,
                    self._slot_type,
                    batch_mode,
                ],
                r,
            )

    @property
    def Minimum(self) -> float:
        return self._load(LogicBatchMethod.Minimum)

    @property
    def Maximum(self) -> float:
        return self._load(LogicBatchMethod.Maximum)

    @property
    def Average(self) -> float:
        return self._load(LogicBatchMethod.Average)

    @property
    def Sum(self) -> float:
        return self._load(LogicBatchMethod.Sum)

    def _set(self, value: float | _Register):
        return IC10Instruction(
            "sbs", [self._device_hash, self._slot_index, self._slot_type, value]
        )


@dataclass
class _DeviceLogicType(_BaseAccess):
    _logic_type: str

    def _load(self, output: _Register) -> float:
        if self._obj._batch_mode is not None:
            return _DevicesLogicType(self._obj, self._logic_type)._load(
                self._obj._batch_mode
            )(output)
        else:
            return IC10Instruction("l", [self._id, self._logic_type], output)

    def _set(self, value: float | _Register):
        if self._obj._batch_mode is not None:
            return _DevicesLogicType(self._obj, self._logic_type)._set(value)
        return IC10Instruction("s", [self._id, self._logic_type, value])


@dataclass
class _DevicesLogicType(_BaseBatchAccess):
    _logic_type: str = ""

    def _load(self, batch_mode: LogicBatchMethod):
        if not self._logic_type:
            raise ValueError("Logic type must be set")

        if self._name is None:
            # All devices of a specific type
            return lambda r: IC10Instruction(
                "lb", [self._device_hash, self._logic_type, batch_mode], r
            )
        else:
            # All devices of a specific type, with a specific name
            return lambda r: IC10Instruction(
                "lbn",
                [self._device_hash, self._name_hash, self._logic_type, batch_mode],
                r,
            )

    @property
    def Minimum(self) -> float:
        obj = copy.deepcopy(self._obj)
        obj._batch_mode = LogicBatchMethod.Minimum
        return _DeviceLogicType(obj, self._logic_type)

    @property
    def Maximum(self) -> float:
        obj = copy.deepcopy(self._obj)
        obj._batch_mode = LogicBatchMethod.Maximum
        return _DeviceLogicType(obj, self._logic_type)

    @property
    def Average(self) -> float:
        obj = copy.deepcopy(self._obj)
        obj._batch_mode = LogicBatchMethod.Average
        return _DeviceLogicType(obj, self._logic_type)

    @property
    def Sum(self) -> float:
        obj = copy.deepcopy(self._obj)
        obj._batch_mode = LogicBatchMethod.Sum
        return _DeviceLogicType(obj, self._logic_type)

    def _set(self, value: float | _Register):
        if self._name is None:
            return IC10Instruction("sb", [self._device_hash, self._logic_type, value])
        else:
            return IC10Instruction(
                "sbn", [self._device_hash, self._name_hash, self._logic_type, value]
            )


@dataclass
class _BaseSlotType(_BaseAccess):
    _slot_index: _slotIndex


@dataclass
class _BaseSlotTypes(_BaseBatchAccess):
    _slot_index: _slotIndex


class _BaseStructure:
    _dev_id: DeviceId
    _prefab_name: str | None = None
    _hash: int = -1
    _name: str | int | None = None
    _batch_mode: LogicBatchMethod = None

    def __init__(
        self,
        device_id: "_BaseStructure | str | None" = None,
        ref_id: str | None = None,
        name: str | int | None = None,
        batch_mode: LogicBatchMethod = None,
    ):
        if isinstance(device_id, _BaseStructure):
            self._dev_id = device_id._dev_id
        elif isinstance(device_id, DeviceId):
            self._dev_id = device_id
        else:
            self._dev_id = DeviceId(device_id or ref_id, ref_id is not None)

        self._name = name
        self._batch_mode = batch_mode

    @property
    def PrefabHash(self) -> float:
        return _DeviceLogicType(self, LogicType.PrefabHash)

    @property
    def ReferenceId(self) -> float:
        return _DeviceLogicType(self, LogicType.ReferenceId)

    @property
    def NameHash(self) -> float:
        return _DeviceLogicType(self, LogicType.NameHash)

    def __str__(self):
        return type(self).__name__ + f"({self._dev_id})"


class _BaseStructures:
    _hash: int = None
    _name: str | int | None = None
    _prefab_name: str | None = None

    def __init__(self, name: str | int | None = None):
        self._name = name

    @property
    def PrefabHash(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, LogicType.PrefabHash)

    @property
    def ReferenceId(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, LogicType.ReferenceId)

    @property
    def NameHash(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, LogicType.NameHash)

    def __str__(self):
        return type(self).__name__[1:] + f"(name={self._name})"


class Device(_BaseStructure, _GenericStructure):
    def __getattr__(self, attr_name: str) -> _DeviceLogicType:
        if attr_name in [
            "_dev_id",
            "_id",
            "_hash",
            "_is_ref_id",
        ] or attr_name.startswith("__"):
            return super().__getattr__(attr_name)
        return _DeviceLogicType(self, attr_name)

    def __str__(self):
        return f"Device({self._dev_id})"


class Devices(_BaseStructures, _GenericStructures):
    def __init__(
        self,
        prefabHash: int,
        name: str | int | None = None,
        batch_mode: LogicBatchMethod = None,
    ):
        self._hash = prefabHash
        self._prefab_name = prefabHash
        self._name = name
        self._batch_mode = batch_mode

    def __getattr__(self, attr_name: str) -> _DeviceLogicType:
        if attr_name in [
            "_hash",
            "_name",
            "_prefab_name",
            "_batch_mode",
        ] or attr_name.startswith("__"):
            return super().__getattr__(attr_name)
        return _DevicesLogicType(self, attr_name)

    def _get_batch_device(self, batch_mode: LogicBatchMethod) -> "_Device":
        d = _Device()
        d._prefab_name = self._prefab_name
        d._batch_mode = batch_mode
        return d

    @property
    def Minimum(self) -> _DeviceLogicType:
        return self._get_batch_device(LogicBatchMethod.Minimum)

    @property
    def Maximum(self) -> _DeviceLogicType:
        return self._get_batch_device(LogicBatchMethod.Maximum)

    @property
    def Average(self) -> _DeviceLogicType:
        return self._get_batch_device(LogicBatchMethod.Average)

    @property
    def Sum(self) -> _DeviceLogicType:
        return self._get_batch_device(LogicBatchMethod.Sum)

    def __str__(self):
        return f"Device({self._dev_id})"


_Device = Device
_Devices = Devices


@dataclass
class _StackValue(_BaseAccess):
    _addr: str | int

    def _set(self, value: float | _Register):
        if self._is_ref_id:
            return IC10Instruction("putd", [self._id, self._addr, value])

        if self._id is None or self._id == "db":
            return IC10Instruction("poke", [self._addr, value])

        return IC10Instruction("put", [self._id, self._addr, value])

    def _load(self, output: _Register) -> float:
        if self._is_ref_id:
            return IC10Instruction("getd", [self._id, self._addr], output)

        return IC10Instruction("get", [self._id or "db", self._addr], output)


@dataclass
class Stack(_BaseAccess):
    def __init__(self, device_id=None, ref_id: str | int | _Register | None = None):
        if device_id is None and ref_id is None:
            device_id = "db"
        self._obj = _BaseStructure(device_id, ref_id)

    def __getitem__(self, index: int | _Register) -> float:
        return _StackValue(self._obj, index)

    def __setitem__(self, index: int | _Register, value: float | _Register) -> None:
        return _StackValue(self._obj, index)


_Reg = lambda name: _Register(name, code_expr=name)

ra = _Reg("ra")
r0 = _Reg("r0")
r1 = _Reg("r1")
r2 = _Reg("r2")
r3 = _Reg("r3")
r4 = _Reg("r4")
r5 = _Reg("r5")
r6 = _Reg("r6")
r7 = _Reg("r7")
r8 = _Reg("r8")
r9 = _Reg("r9")
r10 = _Reg("r10")
r11 = _Reg("r11")
r12 = _Reg("r12")
r13 = _Reg("r13")
r14 = _Reg("r14")
r15 = _Reg("r15")
r16 = _Reg("r16")
sp = _Reg("sp")

d0: _Device = _Device("d0")
d1: _Device = _Device("d1")
d2: _Device = _Device("d2")
d3: _Device = _Device("d3")
d4: _Device = _Device("d4")
d5: _Device = _Device("d5")
db: _Device = _Device("db")

stack: Stack = Stack()


pi: float = math.pi
tau: float = 2 * math.pi
rgas: float = 8.31446261815324

constants = {
    "pi": pi,
    "tau": tau,
    "rgas": rgas,
}

range = __builtins__["range"]


def constexpr(func):
    return func

def emit_code(func):
    return func


__all__ = [
    "pi",
    "rgas",
    "tau",
    "ra",
    "r0",
    "r1",
    "r2",
    "r3",
    "r4",
    "r5",
    "r6",
    "r7",
    "r8",
    "r9",
    "r10",
    "r11",
    "r12",
    "r13",
    "r14",
    "r15",
    "r16",
    "sp",
    "d0",
    "d1",
    "d2",
    "d3",
    "d4",
    "d5",
    "db",
    "_Register",
    "_Device",
    "_Devices",
    "range",
    "constexpr",
    "Device",
    "Devices",
    "_slotIndex",
    "_deviceHash",
    "_nameHash",
    "_GenericStructure",
    "_GenericStructures",
    "_DeviceLogicType",
    "_DevicesLogicType",
    "Stack",
    "stack",
    "_StackValue",
    "_DeviceSlotType",
    "_DevicesSlotType",
]
