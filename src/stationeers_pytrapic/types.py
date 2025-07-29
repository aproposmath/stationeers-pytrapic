import enum
from dataclasses import dataclass
from logging import warn

from .types_generated import *


class Register:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


def compute_hash(name: str | Register) -> int:
    if isinstance(name, Register):
        return name

    if name.startswith("__register."):
        return name

    if name[0] == '"' and name[-1] == '"':
        name = name[1:-1]

    import zlib
    val = zlib.crc32(name.encode())
    val = (val ^ 0x80000000) - 0x80000000
    return val

class deviceHash(int):
    pass


class nameHash(int):
    pass


class batchMode(enum.IntEnum):
    Average = 0
    Sum = 1
    Minimum = 2
    Maximum = 3


class reagentMode(enum.IntEnum):
    Contents = 0
    Required = 1
    Recipe = 2


class slotIndex(int):
    pass

@dataclass
class DeviceId:
    _id: str | None = None
    _is_ref_id: bool = False


@dataclass
class DeviceLogicType:
    _cls: any
    _device_id: DeviceId
    _logic_type: str

    def _load(self, output: Register) -> float:
        from .intrinsics import l, ld

        id = self._device_id
        if id._is_ref_id:
            return ld(output, id._id ,self._logic_type)
        else:
            return l(output, id._id ,self._logic_type)

    def _set(self, value: float | Register):
        from .intrinsics import s, sd

        id = self._device_id
        if id._is_ref_id:
            return sd(id._id, self._logic_type, value)
        else:
            return s(id._id, self._logic_type, value)


@dataclass
class DevicesLogicType:
    _device_hash: deviceHash
    _logic_type: str
    _name_hash: nameHash | None = None

    def _load(self, batch_mode: batchMode):
        from .intrinsics import lb, lbn

        if self._name_hash is None:
            # All devices of a specific type
            return lambda r: lb(r, self._device_hash, self._logic_type, batch_mode)
        else:
            # All devices of a specific type, with a specific name
            return lambda r: lbn(
                r, self._device_hash, self._name_hash, self._logic_type, batch_mode
            )

    @property
    def Minimum(self) -> float:
        return self._load(batchMode.Minimum)

    @property
    def Maximum(self) -> float:
        return self._load(batchMode.Maximum)

    @property
    def Average(self) -> float:
        return self._load(batchMode.Average)

    @property
    def Sum(self) -> float:
        return self._load(batchMode.Sum)

    def _set(self, value: float | Register):
        from .intrinsics import sb, sbn

        if self._name_hash is None:
            # All devices of a specific type
            return sb(self._device_hash, self._logic_type, value)
        else:
            # All devices of a specific type, with a specific name
            return sbn(self._device_hash, self._name_hash, self._logic_type, value)


# @dataclass
# class DevicesByName(GenericStructures):
#     device_hash: deviceHash
#     name_hash: nameHash
#
#     def __getattr__(self, attr_name: str) -> DevicesLogicType:
#         if attr_name == "device_hash" or attr_name.startswith("__"):
#             return super().__getattr__(attr_name)
#
#         return DevicesLogicType(self.device_hash, attr_name, self.name_hash)
#
#
# class DevicesByType(GenericStructures):
#     def __init__(self, structure_name: str):
#         self.device_hash = compute_hash(structure_name)
#
#     def __getattr__(self, attr_name: str) -> DevicesLogicType:
#         if attr_name == "device_hash" or attr_name.startswith("__"):
#             return super().__getattr__(attr_name)
#
#         return DevicesLogicType(self.device_hash, attr_name)
#
#     def __getitem__(self, name: str | Register) -> DevicesByName:
#         if isinstance(name, str):
#             name = compute_hash(name)
#         return DevicesByName(self.device_hash, name)


del enum

class _BaseStructure:
    _hash: int = None
    _id: DeviceId

    def __init__(self, device_id: str | None = None, ref_id: str | None = None):
        self._id = DeviceId(device_id or ref_id, ref_id is not None)

    @property
    def PrefabHash(self) -> float:
        return DeviceLogicType(type(self), self._id, "PrefabHash")

    @property
    def ReferenceId(self) -> float:
        return DeviceLogicType(type(self), self._id, "ReferenceId")

    @property
    def NameHash(self) -> float:
        return DeviceLogicType(type(self), self._id, "NameHash")


class _BaseStructures:
    _hash: int = None
    _name_hash: nameHash | None = None

    def __init__(self, name: str | int | None = None):
        # print("make base structures", name, type(name))
        if isinstance(name, str) and not name.startswith("__register."):
            name = compute_hash(name)
        self._name_hash = name

    @property
    def PrefabHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PrefabHash", self._name_hash)

    @property
    def ReferenceId(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ReferenceId", self._name_hash)

    @property
    def NameHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "NameHash", self._name_hash)


class Device(_BaseStructure, GenericStructure):
    def __getattr__(self, attr_name: str) -> DeviceLogicType:
        if attr_name in ["_id" , "_hash"] or attr_name.startswith("__"):
            return super().__getattr__(attr_name)
        return DeviceLogicType(type(self), self._id, attr_name)

    def __str__(self):
        return f"{self._id._id}"

ra = Register("ra")
r0 = Register("r0")
r1 = Register("r1")
r2 = Register("r2")
r3 = Register("r3")
r4 = Register("r4")
r5 = Register("r5")
r6 = Register("r6")
r7 = Register("r7")
r8 = Register("r8")
r9 = Register("r9")
r10 = Register("r10")
r11 = Register("r11")
r12 = Register("r12")
r13 = Register("r13")
r14 = Register("r14")
r15 = Register("r15")
r16 = Register("r16")
sp = Register("sp")

d0 = Device("d0")
d1 = Device("d1")
d2 = Device("d2")
d3 = Device("d3")
d4 = Device("d4")
d5 = Device("d5")
db = Device("db")
