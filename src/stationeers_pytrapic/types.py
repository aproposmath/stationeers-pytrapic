import enum
from dataclasses import dataclass
from logging import warn

from .types_generated import *


class Register:
    def __init__(self, num: int):
        self.num = num

    def __str__(self):
        if isinstance(self.num, str):
            return self.num
        return f"r{self.num}"


def compute_hash(name: str | Register) -> int:
    if isinstance(name, Register):
        return name

    import zlib

    val = zlib.crc32(name.encode())
    if val >= 2**31:
        val -= 2**32
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
class DeviceLogicType:
    _cls: any
    _device_id: str
    _logic_type: str

    def _load(self, output: Register) -> float:
        from .intrinsics import l

        return l(output, self._device_id, self._logic_type)

    def _set(self, value: float | Register):
        from .intrinsics import s

        return s(self._device_id, self._logic_type, value)


class Device(GenericStructure):
    def __init__(self, num: int | str):
        self.__num = num

    def __str__(self):
        return f"d{self.__num}"

    def __getattr__(self, attr_name: str) -> DeviceLogicType:
        if attr_name.startswith("__"):
            return super().__getattr__(attr_name)

        return DeviceLogicType(self, str(self), attr_name)


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
    _id: str | None = None

    def __init__(self, device_id: str):
        self._id = device_id

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
        self._name_hash = compute_hash(name) if isinstance(name, str) else name

    @property
    def PrefabHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PrefabHash", self._name_hash)

    @property
    def ReferenceId(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ReferenceId", self._name_hash)

    @property
    def NameHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "NameHash", self._name_hash)


ra = Register("ra")
r0 = Register(0)
r1 = Register(1)
r2 = Register(2)
r3 = Register(3)
r4 = Register(4)
r5 = Register(5)
r6 = Register(6)
r7 = Register(7)
r8 = Register(8)
r9 = Register(9)
r10 = Register(10)
r11 = Register(11)
r12 = Register(12)
r13 = Register(13)
r14 = Register(14)
r15 = Register(15)
r16 = Register(16)

d0 = Device(0)
d1 = Device(1)
d2 = Device(2)
d3 = Device(3)
d4 = Device(4)
d5 = Device(5)
db = Device("b")

sp = Register("sp")  # Stack Pointer
