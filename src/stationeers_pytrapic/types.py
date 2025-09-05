import enum
from dataclasses import dataclass
from logging import warn

from .types_generated import *


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


class _Register:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


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
        return eval_str if len(eval_str) < len(hash_str) else hash_str
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

    def _load(self, output: _Register) -> float:
        from .intrinsics import ls

        id = self._device_id

        return ls(output, id._id, self._slot_index, self._slot_type)

    def _set(self, value: float | _Register):
        from .intrinsics import ss

        id = self._device_id

        return ss(id._id, self._slot_index, self._slot_type, value)


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
        from .intrinsics import lbs, lbns

        if self._name is None:
            return lambda r: lbs(
                r, self._device_hash, self._slot_index, self._slot_type, batch_mode
            )
        else:
            return lambda r: lbns(
                r,
                self._device_hash,
                self._name_hash,
                self._slot_index,
                self._slot_type,
                batch_mode,
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
        from .intrinsics import sbs

        return sbs(self._device_hash, self._slot_index, self._slot_type, value)


@dataclass
class _DeviceLogicType:
    _cls: type
    _device_id: DeviceId
    _logic_type: str

    def _load(self, output: _Register) -> float:
        from .intrinsics import l, ld

        id = self._device_id
        if id._is_ref_id:
            return ld(output, id._id, self._logic_type)
        else:
            return l(output, id._id, self._logic_type)

    def _set(self, value: float | _Register):
        from .intrinsics import s, sd

        id = self._device_id
        if id._is_ref_id:
            return sd(id._id, self._logic_type, value)
        else:
            return s(id._id, self._logic_type, value)


@dataclass
class _DevicesLogicType:
    _device_hash: _deviceHash
    _logic_type: str
    _name: str | int | None = None

    @property
    def _name_hash(self) -> int | str | None:
        if self._name is None:
            raise ValueError("Name must be set to compute name hash")
        return compute_hash(self._name)

    def _load(self, batch_mode: _batchMode):
        from .intrinsics import lb, lbn

        if self._name is None:
            # All devices of a specific type
            return lambda r: lb(r, self._device_hash, self._logic_type, batch_mode)
        else:
            # All devices of a specific type, with a specific name
            return lambda r: lbn(
                r, self._device_hash, self._name_hash, self._logic_type, batch_mode
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
        from .intrinsics import sb, sbn

        if self._name is None:
            # All devices of a specific type
            return sb(self._device_hash, self._logic_type, value)
        else:
            # All devices of a specific type, with a specific name
            return sbn(self._device_hash, self._name_hash, self._logic_type, value)


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
        from .intrinsics import poke, put, putd

        if self._id is None:
            return poke(self._addr, value)

        if self._is_ref_id:
            return putd(self._id, self._addr, value)

        return put(self._id, self._addr, value)

    def _load(self, output: _Register) -> float:
        from .intrinsics import get, getd

        if self._is_ref_id:
            return getd(output, self._id, self._addr)

        return get(output, self._id or "db", self._addr)


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

ra = _Register("ra")
r0 = _Register("r0")
r1 = _Register("r1")
r2 = _Register("r2")
r3 = _Register("r3")
r4 = _Register("r4")
r5 = _Register("r5")
r6 = _Register("r6")
r7 = _Register("r7")
r8 = _Register("r8")
r9 = _Register("r9")
r10 = _Register("r10")
r11 = _Register("r11")
r12 = _Register("r12")
r13 = _Register("r13")
r14 = _Register("r14")
r15 = _Register("r15")
r16 = _Register("r16")
sp = _Register("sp")

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
