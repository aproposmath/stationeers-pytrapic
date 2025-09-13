import enum
import sys
from dataclasses import dataclass, field

import astroid

from .types_generated import *
from .utils import get_loop_ancestor


@dataclass
class IC10Register:
    name: str
    scope: str = ""
    code_expr: "str | _BaseStructure | _BaseStructures" = ""
    _lifetime: range | None = None
    _color: int = -1
    _is_intermediate: bool = False

    nodes_reading: list[astroid.NodeNG] = field(default_factory=list)
    nodes_writing: list[astroid.NodeNG] = field(default_factory=list)

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
            max_line = max(node.lineno for node in all_nodes) if all_nodes else -1
            self._lifetime = range(min_line, max_line + 1)
        return self._lifetime


@dataclass
class IC10Operand:
    """
    An operand for an IC10 instruction, can be a register or an immediate value
    """

    value: str | float | int | IC10Register

    @property
    def is_register(self) -> bool:
        return isinstance(self.value, IC10Register)

    def to_string(self) -> str:
        if isinstance(self.value, IC10Register):
            return self.value.code_expr
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
    node: astroid.NodeNG = None

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
        code = " " * self.indent * shift + self.op
        if self.output:
            if not isinstance(self.output, IC10Register):
                from .compile_pass import CompilerError

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
            if not isinstance(inputs[i], IC10Operand):
                inputs[i] = IC10Operand(inputs[i])
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

    res = (
        base64.b64encode(zlib.compress(json.dumps(data).encode()))
        .decode()
        .replace("+", "-")
        .replace("/", "_")
        .replace("=", "")
    )
    return res


def decode_data(encoded: str) -> dict:
    """Decodes a base64-encoded, zlib-compressed string back into a dictionary. Replaces - and _ with + and / respectively, and adds padding (=) if necessary."""
    import base64
    import json
    import zlib

    if len(encoded) % 4:
        encoded += "=" * (4 - len(encoded) % 4)

    encoded = encoded.replace("-", "+").replace("_", "/")
    return json.loads(zlib.decompress(base64.b64decode(encoded)).decode())


class HashMode(enum.Enum):
    """Hashing mode for names."""

    VERBOSE = 0  # keep HASH("name") in the code
    COMPACT = 1  # keep HASH("name") in the code only if it's shorter
    EVAL = 0  # always evaluate the hash


hash_mode = HashMode.VERBOSE


def compute_hash(name: int | str | _Register) -> int | str:
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

    # return f'HASH("{name}")'

    import zlib

    val = zlib.crc32(name.encode())
    val = (val ^ 0x80000000) - 0x80000000
    eval_str = str(val)
    hash_str = f'HASH("{name}")'

    if hash_mode == HashMode.VERBOSE:
        return hash_str
    elif hash_mode == HashMode.COMPACT:
        return val if len(eval_str) < len(hash_str) else hash_str
    elif hash_mode == HashMode.EVAL:
        return eval_str

    raise ValueError(f"Invalid hash mode: {hash_mode}")


class _deviceHash(int):
    pass


class _nameHash(int):
    pass


class _batchMode(enum.IntEnum):
    Average = 0
    Sum = 1
    Minimum = 2
    Maximum = 3


class _reagentMode(enum.IntEnum):
    Contents = 0
    Required = 1
    Recipe = 2


class _slotIndex(int):
    pass


@dataclass
class DeviceId:
    _id: str | None = None
    _is_ref_id: bool = False


@dataclass
class _DeviceSlotType:
    _cls: type
    _device_id: DeviceId
    _slot_index: _slotIndex
    _slot_type: _logicSlotType

    def _load(self, output: _Register) -> IC10Instruction:
        id = self._device_id
        return IC10Instruction(
            "ls", [id._id, self._slot_index, self._slot_type], output
        )

    def _set(self, value: float | _Register) -> IC10Instruction:
        id = self._device_id
        return IC10Instruction("ss", [id._id, self._slot_index, self._slot_type, value])


@dataclass
class _DevicesSlotType:
    _cls: type
    _device_hash: _deviceHash
    _slot_index: _slotIndex
    _slot_type: _logicSlotType
    _name: str | int | None = None

    @property
    def _name_hash(self) -> int | str | None:
        if self._name is None:
            raise ValueError("Name must be set to compute name hash")
        return compute_hash(self._name)

    def _load(self, batch_mode: _batchMode):
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
        return self._load(_batchMode.Minimum)

    @property
    def Maximum(self) -> float:
        return self._load(_batchMode.Maximum)

    @property
    def Average(self) -> float:
        return self._load(_batchMode.Average)

    @property
    def Sum(self) -> float:
        return self._load(_batchMode.Sum)

    def _set(self, value: float | _Register):
        return IC10Instruction(
            "sbs", [self._device_hash, self._slot_index, self._slot_type, value]
        )


@dataclass
class _DeviceLogicType:
    _cls: type
    _device_id: DeviceId
    _logic_type: str

    def _load(self, output: _Register) -> float:
        id = self._device_id
        instr = "ld" if id._is_ref_id else "l"
        return IC10Instruction(instr, [id._id, self._logic_type], output)

    def _set(self, value: float | _Register):
        id = self._device_id
        instr = "sd" if id._is_ref_id else "s"
        return IC10Instruction(instr, [id._id, self._logic_type, value])


@dataclass
class _DevicesLogicType:
    _device_hash: _deviceHash
    _logic_type: str
    _name: str | int | None = None

    @property
    def _name_hash(self) -> int | str | None:
        if not self._name:
            raise ValueError("Name must be set to compute name hash")

        return compute_hash(self._name)

    def _load(self, batch_mode: _batchMode):
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
        return self._load(_batchMode.Minimum)

    @property
    def Maximum(self) -> float:
        return self._load(_batchMode.Maximum)

    @property
    def Average(self) -> float:
        return self._load(_batchMode.Average)

    @property
    def Sum(self) -> float:
        return self._load(_batchMode.Sum)

    def _set(self, value: float | _Register):
        if self._name is None:
            return IC10Instruction("sb", [self._device_hash, self._logic_type, value])
        else:
            return IC10Instruction(
                "sbn", [self._device_hash, self._name_hash, self._logic_type, value]
            )


del enum


@dataclass
class _BaseSlotType:
    _cls: type
    _id: DeviceId
    _slot_index: _slotIndex


@dataclass
class _BaseSlotTypes:
    _cls: type
    _hash: _deviceHash
    _slot_index: _slotIndex
    _name: str | int | None = None


class _BaseStructure:
    _id: DeviceId

    def __init__(self, device_id: str | None = None, ref_id: str | None = None):
        self._id = DeviceId(device_id or ref_id, ref_id is not None)

    @property
    def PrefabHash(self) -> float:
        return _DeviceLogicType(type(self), self._id, "PrefabHash")

    @property
    def ReferenceId(self) -> float:
        return _DeviceLogicType(type(self), self._id, "ReferenceId")

    @property
    def NameHash(self) -> float:
        return _DeviceLogicType(type(self), self._id, "NameHash")

    def __str__(self):
        return type(self).__name__ + f"({self._id._id})"


class _BaseStructures:
    _hash: int = None
    _name: str | int | None = None

    def __init__(self, name: str | int | None = None):
        self._name = name

    @property
    def PrefabHash(self) -> _DevicesLogicType:
        return _DevicesLogicType(self._hash, "PrefabHash", self._name)

    @property
    def ReferenceId(self) -> _DevicesLogicType:
        return _DevicesLogicType(self._hash, "ReferenceId", self._name)

    @property
    def NameHash(self) -> _DevicesLogicType:
        return _DevicesLogicType(self._hash, "NameHash", self._name)

    def __str__(self):
        return type(self).__name__[1:] + f"(name={self._name})"


class _Device(_BaseStructure, _GenericStructure):
    def __getattr__(self, attr_name: str) -> _DeviceLogicType:
        if attr_name in ["_id", "_hash"] or attr_name.startswith("__"):
            return super().__getattr__(attr_name)
        return _DeviceLogicType(type(self), self._id, attr_name)

    def __str__(self):
        return f"{self._id._id}"


class _StackValue:
    _id: str | None = None
    _is_ref_id: bool = False
    _addr: str | None = None

    def __init__(self, _id, is_ref_id, _addr):
        self._id = _id
        self._is_ref_id = is_ref_id
        self._addr = _addr

    def _set(self, value: float | _Register):
        if self._id is None:
            return IC10Instruction("poke", [self._addr, value])

        if self._is_ref_id:
            return IC10Instruction("putd", [self._id, self._addr, value])

        return IC10Instruction("put", [self._id, self._addr, value])

    def _load(self, output: _Register) -> float:
        if self._is_ref_id:
            return IC10Instruction("getd", [self._id, self._addr], output)

        return IC10Instruction("get", [self._id or "db", self._addr], output)


class Stack:
    _id: str | None = None
    _is_ref_id: bool = False

    def __init__(self, device_id: str | None = None, ref_id: str | None = None):
        self._id = device_id or ref_id
        self._is_ref_id = ref_id is not None

    def __getitem__(self, index: int | _Register) -> _Register:
        return _StackValue(self._id, self._is_ref_id, index)

    def __setitem__(self, index: int | _Register, value: float | _Register) -> None:
        return _StackValue(self._id, self._is_ref_id, index)


stack = Stack()

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

d0 = _Device("d0")
d1 = _Device("d1")
d2 = _Device("d2")
d3 = _Device("d3")
d4 = _Device("d4")
d5 = _Device("d5")
db = _Device("db")

__all__ = [
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
    "_logicType",
    "_reagentMode",
    "_slotIndex",
    "_deviceHash",
    "_batchMode",
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
