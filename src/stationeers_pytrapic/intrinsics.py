# This file is auto-generated from IC10 instructions_data
from .types import *
from .types_generated import *
from .types import IC10 as _IC10, IC10Register as _Register


def alias(param1: str, param2: _Register | _Device) -> None:
    """Labels register or device reference with name, device references also affect what shows on the screws on the IC base."""
    return _IC10("alias", [param1, param2], None)


def define(param1: str, param2: float) -> None:
    """Creates a label that will be replaced throughout the program with the provided value."""
    return _IC10("define", [param1, param2], None)


def hcf() -> None:
    """Halt and catch fire"""
    return _IC10("hcf", [], None)


def sleep(a: _Register | float) -> None:
    """Pauses execution on the IC for a seconds"""
    return _IC10("sleep", [a], None)


def yield_() -> None:
    """Pauses execution for 1 tick"""
    return _IC10("yield", [], None)


def abs(a: _Register | float) -> _Register:
    """Returns the absolute value of a"""
    return _IC10("abs", [a], _Register("invalid"))


def add(a: _Register | float, b: _Register | float) -> _Register:
    """Returns a + b."""
    return _IC10("add", [a, b], _Register("invalid"))


def ceil(a: _Register | float) -> _Register:
    """Returns smallest integer greater than a"""
    return _IC10("ceil", [a], _Register("invalid"))


def div(a: _Register | float, b: _Register | float) -> _Register:
    """Returns a / b"""
    return _IC10("div", [a, b], _Register("invalid"))


def exp(a: _Register | float) -> _Register:
    """exp(a) or e^a"""
    return _IC10("exp", [a], _Register("invalid"))


def floor(a: _Register | float) -> _Register:
    """Returns largest integer less than a"""
    return _IC10("floor", [a], _Register("invalid"))


def log(a: _Register | float) -> _Register:
    """base e log(a) or ln(a)"""
    return _IC10("log", [a], _Register("invalid"))


def max(a: _Register | float, b: _Register | float) -> _Register:
    """Returns max of a or b"""
    return _IC10("max", [a, b], _Register("invalid"))


def min(a: _Register | float, b: _Register | float) -> _Register:
    """Returns min of a or b"""
    return _IC10("min", [a, b], _Register("invalid"))


def mod(a: _Register | float, b: _Register | float) -> _Register:
    """Returns a mod b (note: NOT a % b)"""
    return _IC10("mod", [a, b], _Register("invalid"))


def move(a: _Register | float) -> _Register:
    """Returns provided num or register value."""
    return _IC10("move", [a], _Register("invalid"))


def mul(a: _Register | float, b: _Register | float) -> _Register:
    """Returns a * b"""
    return _IC10("mul", [a, b], _Register("invalid"))


def rand() -> _Register:
    """Returns a random value x with 0 <= x < 1"""
    return _IC10("rand", [], _Register("invalid"))


def round(a: _Register | float) -> _Register:
    """Returns a rounded to nearest integer"""
    return _IC10("round", [a], _Register("invalid"))


def sqrt(a: _Register | float) -> _Register:
    """Returns square root of a"""
    return _IC10("sqrt", [a], _Register("invalid"))


def sub(a: _Register | float, b: _Register | float) -> _Register:
    """Returns a - b."""
    return _IC10("sub", [a, b], _Register("invalid"))


def trunc(a: _Register | float) -> _Register:
    """Returns a with fractional part removed"""
    return _IC10("trunc", [a], _Register("invalid"))


def acos(a: _Register | float) -> _Register:
    """Returns the angle (radians) whos cos is the specified value"""
    return _IC10("acos", [a], _Register("invalid"))


def asin(a: _Register | float) -> _Register:
    """Returns the angle (radians) whos sine is the specified value"""
    return _IC10("asin", [a], _Register("invalid"))


def atan(a: _Register | float) -> _Register:
    """Returns the angle (radians) whos tan is the specified value"""
    return _IC10("atan", [a], _Register("invalid"))


def atan2(a: _Register | float, b: _Register | float) -> _Register:
    """Returns the angle (radians) whose tangent is the quotient of two specified values: a (y) and b (x)"""
    return _IC10("atan2", [a, b], _Register("invalid"))


def cos(a: _Register | float) -> _Register:
    """Returns the cosine of the specified angle (radians)"""
    return _IC10("cos", [a], _Register("invalid"))


def sin(a: _Register | float) -> _Register:
    """Returns the sine of the specified angle (radians)"""
    return _IC10("sin", [a], _Register("invalid"))


def tan(a: _Register | float) -> _Register:
    """Returns the tan of the specified angle (radians)"""
    return _IC10("tan", [a], _Register("invalid"))


def clr(param1: _Device) -> None:
    """Clears the stack memory for the provided device."""
    return _IC10("clr", [param1], None)


def clrd(id: _Register | float) -> None:
    """Seeks directly for the provided device id and clears the stack memory of that device"""
    return _IC10("clrd", [id], None)


def get(param1: _Device, address: _Register | float) -> _Register:
    """Using the provided device, attempts to read the stack value at the provided address, and places it in the register."""
    return _IC10("get", [param1, address], _Register("invalid"))


def getd(id: _Register | float, address: _Register | float) -> _Register:
    """Seeks directly for the provided device id, attempts to read the stack value at the provided address, and places it in the register."""
    return _IC10("getd", [id, address], _Register("invalid"))


def peek() -> _Register:
    """Returns the value at the top of the stack"""
    return _IC10("peek", [], _Register("invalid"))


def poke(address: _Register | float, value: _Register | float) -> None:
    """Stores the provided value at the provided address in the stack."""
    return _IC10("poke", [address, value], None)


def pop() -> _Register:
    """Returns the value at the top of the stack and decrements sp"""
    return _IC10("pop", [], _Register("invalid"))


def push(a: _Register | float) -> None:
    """Pushes the value of a to the stack at sp and increments sp"""
    return _IC10("push", [a], None)


def put(param1: _Device, address: _Register | float, value: _Register | float) -> None:
    """Using the provided device, attempts to write the provided value to the stack at the provided address."""
    return _IC10("put", [param1, address, value], None)


def putd(
    id: _Register | float, address: _Register | float, value: _Register | float
) -> None:
    """Seeks directly for the provided device id, attempts to write the provided value to the stack at the provided address."""
    return _IC10("putd", [id, address, value], None)


def l(param1: _Device, param2: LogicType) -> _Register:
    """Loads device LogicType to register by housing index value."""
    return _IC10("l", [param1, param2], _Register("invalid"))


def ld(id: _Register | float, param2: LogicType) -> _Register:
    """Loads device LogicType to register by direct ID reference."""
    return _IC10("ld", [id, param2], _Register("invalid"))


def lr(param1: _Device, param2: LogicReagentMode, param3: int) -> _Register:
    """Loads reagent of device's ReagentMode where a hash of the reagent type to check for. ReagentMode can be either Contents (0), Required (1), Recipe (2). Can use either the word, or the number."""
    return _IC10("lr", [param1, param2, param3], _Register("invalid"))


def ls(param1: _Device, param2: _slotIndex, param3: LogicSlotType) -> _Register:
    """Loads slot LogicSlotType on device to register."""
    return _IC10("ls", [param1, param2, param3], _Register("invalid"))


def s(param1: _Device, param2: LogicType, param3: _Register) -> None:
    """Stores register value to LogicType on device by housing index value."""
    return _IC10("s", [param1, param2, param3], None)


def sd(id: _Register | float, param2: LogicType, param3: _Register) -> None:
    """Stores register value to LogicType on device by direct ID reference."""
    return _IC10("sd", [id, param2, param3], None)


def ss(
    param1: _Device, param2: _slotIndex, param3: LogicSlotType, param4: _Register
) -> None:
    """Stores register value to device stored in a slot LogicSlotType on device."""
    return _IC10("ss", [param1, param2, param3, param4], None)


def rmap(param1: _Register, param2: _Device, reagentHash: _Register | float) -> None:
    """Given a reagent hash, store the corresponding prefab hash that the device expects to fulfill the reagent requirement. For example, on an autolathe, the hash for Iron will store the hash for ItemIronIngot."""
    return _IC10("rmap", [param1, param2, reagentHash], None)


def lb(param1: _deviceHash, param2: LogicType, param3: LogicBatchMethod) -> _Register:
    """Loads LogicType from all output network devices with provided type hash using the provide batch mode. Average (0), Sum (1), Minimum (2), Maximum (3). Can use either the word, or the number."""
    return _IC10("lb", [param1, param2, param3], _Register("invalid"))


def lbn(
    param1: _deviceHash, param2: _nameHash, param3: LogicType, param4: LogicBatchMethod
) -> _Register:
    """Loads LogicType from all output network devices with provided type and name hashes using the provide batch mode. Average (0), Sum (1), Minimum (2), Maximum (3). Can use either the word, or the number."""
    return _IC10("lbn", [param1, param2, param3, param4], _Register("invalid"))


def lbns(
    param1: _deviceHash,
    param2: _nameHash,
    param3: _slotIndex,
    param4: LogicSlotType,
    param5: LogicBatchMethod,
) -> _Register:
    """Loads LogicSlotType from slotIndex from all output network devices with provided type and name hashes using the provide batch mode. Average (0), Sum (1), Minimum (2), Maximum (3). Can use either the word, or the number."""
    return _IC10("lbns", [param1, param2, param3, param4, param5], _Register("invalid"))


def lbs(
    param1: _deviceHash,
    param2: _slotIndex,
    param3: LogicSlotType,
    param4: LogicBatchMethod,
) -> _Register:
    """Loads LogicSlotType from slotIndex from all output network devices with provided type hash using the provide batch mode. Average (0), Sum (1), Minimum (2), Maximum (3). Can use either the word, or the number."""
    return _IC10("lbs", [param1, param2, param3, param4], _Register("invalid"))


def sb(param1: _deviceHash, param2: LogicType, param3: _Register) -> None:
    """Stores register value to LogicType on all output network devices with provided type hash."""
    return _IC10("sb", [param1, param2, param3], None)


def sbn(
    param1: _deviceHash, param2: _nameHash, param3: LogicType, param4: _Register
) -> None:
    """Stores register value to LogicType on all output network devices with provided type hash and name."""
    return _IC10("sbn", [param1, param2, param3, param4], None)


def sbs(
    param1: _deviceHash, param2: _slotIndex, param3: LogicSlotType, param4: _Register
) -> None:
    """Stores register value to LogicSlotType on all output network devices with provided type hash in the provided slot."""
    return _IC10("sbs", [param1, param2, param3, param4], None)


def and_(a: _Register | float, b: _Register | float) -> _Register:
    """Performs a bitwise logical AND operation on the binary representation of two values. Each bit of the result is determined by evaluating the corresponding bits of the input values. If both bits are 1, the resulting bit is set to 1. Otherwise the resulting bit is set to 0."""
    return _IC10("and", [a, b], _Register("invalid"))


def nor(a: _Register | float, b: _Register | float) -> _Register:
    """Performs a bitwise logical NOR (NOT OR) operation on the binary representation of two values. Each bit of the result is determined by evaluating the corresponding bits of the input values. If both bits are 0, the resulting bit is set to 1. Otherwise, if at least one bit is 1, the resulting bit is set to 0."""
    return _IC10("nor", [a, b], _Register("invalid"))


def not_(a: _Register | float) -> _Register:
    """Performs a bitwise logical NOT operation flipping each bit of the input value, resulting in a binary complement. If a bit is 1, it becomes 0, and if a bit is 0, it becomes 1."""
    return _IC10("not", [a], _Register("invalid"))


def or_(a: _Register | float, b: _Register | float) -> _Register:
    """Performs a bitwise logical OR operation on the binary representation of two values. Each bit of the result is determined by evaluating the corresponding bits of the input values. If either bit is 1, the resulting bit is set to 1. If both bits are 0, the resulting bit is set to 0."""
    return _IC10("or", [a, b], _Register("invalid"))


def sla(a: _Register | float, b: _Register | float) -> _Register:
    """Performs a bitwise arithmetic left shift operation on the binary representation of a value. It shifts the bits to the left and fills the vacated rightmost bits with zeros (note that this is indistinguishable from 'sll')."""
    return _IC10("sla", [a, b], _Register("invalid"))


def sll(a: _Register | float, b: _Register | float) -> _Register:
    """Performs a bitwise logical left shift operation on the binary representation of a value. It shifts the bits to the left and fills the vacated rightmost bits with zeros."""
    return _IC10("sll", [a, b], _Register("invalid"))


def sra(a: _Register | float, b: _Register | float) -> _Register:
    """Performs a bitwise arithmetic right shift operation on the binary representation of a value. It shifts the bits to the right and fills the vacated leftmost bits with a copy of the sign bit (the most significant bit)."""
    return _IC10("sra", [a, b], _Register("invalid"))


def srl(a: _Register | float, b: _Register | float) -> _Register:
    """Performs a bitwise logical right shift operation on the binary representation of a value. It shifts the bits to the right and fills the vacated leftmost bits with zeros"""
    return _IC10("srl", [a, b], _Register("invalid"))


def xor(a: _Register | float, b: _Register | float) -> _Register:
    """Performs a bitwise logical XOR (exclusive OR) operation on the binary representation of two values. Each bit of the result is determined by evaluating the corresponding bits of the input values. If the bits are different (one bit is 0 and the other is 1), the resulting bit is set to 1. If the bits are the same (both 0 or both 1), the resulting bit is set to 0."""
    return _IC10("xor", [a, b], _Register("invalid"))


def select(
    a: _Register | float, b: _Register | float, c: _Register | float
) -> _Register:
    """Returns b if a is non-zero, otherwise c"""
    return _IC10("select", [a, b, c], _Register("invalid"))


def sdns(param1: _Device) -> _Register:
    """Returns 1 if device is not set, otherwise 0"""
    return _IC10("sdns", [param1], _Register("invalid"))


def sdse(param1: _Device) -> _Register:
    """Returns 1 if device is set, otherwise 0."""
    return _IC10("sdse", [param1], _Register("invalid"))


def sap(a: _Register | float, b: _Register | float, c: _Register | float) -> _Register:
    """Returns 1 if abs(a - b) <= max(c * max(abs(a), abs(b)), float.epsilon * 8), otherwise 0"""
    return _IC10("sap", [a, b, c], _Register("invalid"))


def sapz(a: _Register | float, b: _Register | float) -> _Register:
    """Returns 1 if abs(a) <= max(b * abs(a), float.epsilon * 8), otherwise 0"""
    return _IC10("sapz", [a, b], _Register("invalid"))


def seq(a: _Register | float, b: _Register | float) -> _Register:
    """Returns 1 if a == b, otherwise 0"""
    return _IC10("seq", [a, b], _Register("invalid"))


def seqz(a: _Register | float) -> _Register:
    """Returns 1 if a == 0, otherwise 0"""
    return _IC10("seqz", [a], _Register("invalid"))


def sge(a: _Register | float, b: _Register | float) -> _Register:
    """Returns 1 if a >= b, otherwise 0"""
    return _IC10("sge", [a, b], _Register("invalid"))


def sgez(a: _Register | float) -> _Register:
    """Returns 1 if a >= 0, otherwise 0"""
    return _IC10("sgez", [a], _Register("invalid"))


def sgt(a: _Register | float, b: _Register | float) -> _Register:
    """Returns 1 if a > b, otherwise 0"""
    return _IC10("sgt", [a, b], _Register("invalid"))


def sgtz(a: _Register | float) -> _Register:
    """Returns 1 if a > 0, otherwise 0"""
    return _IC10("sgtz", [a], _Register("invalid"))


def sle(a: _Register | float, b: _Register | float) -> _Register:
    """Returns 1 if a <= b, otherwise 0"""
    return _IC10("sle", [a, b], _Register("invalid"))


def slez(a: _Register | float) -> _Register:
    """Returns 1 if a <= 0, otherwise 0"""
    return _IC10("slez", [a], _Register("invalid"))


def slt(a: _Register | float, b: _Register | float) -> _Register:
    """Returns 1 if a < b, otherwise 0"""
    return _IC10("slt", [a, b], _Register("invalid"))


def sltz(a: _Register | float) -> _Register:
    """Returns 1 if a < 0, otherwise 0"""
    return _IC10("sltz", [a], _Register("invalid"))


def sna(a: _Register | float, b: _Register | float, c: _Register | float) -> _Register:
    """Returns 1 if abs(a - b) > max(c * max(abs(a), abs(b)), float.epsilon * 8), otherwise 0"""
    return _IC10("sna", [a, b, c], _Register("invalid"))


def snan(a: _Register | float) -> _Register:
    """Returns 1 if a is NaN, otherwise 0"""
    return _IC10("snan", [a], _Register("invalid"))


def snanz(a: _Register | float) -> _Register:
    """Returns 0 if a is NaN, otherwise 1"""
    return _IC10("snanz", [a], _Register("invalid"))


def snaz(a: _Register | float, b: _Register | float) -> _Register:
    """Returns 1 if abs(a) > max(b * abs(a), float.epsilon), otherwise 0"""
    return _IC10("snaz", [a, b], _Register("invalid"))


def sne(a: _Register | float, b: _Register | float) -> _Register:
    """Returns 1 if a != b, otherwise 0"""
    return _IC10("sne", [a, b], _Register("invalid"))


def snez(a: _Register | float) -> _Register:
    """Returns 1 if a != 0, otherwise 0"""
    return _IC10("snez", [a], _Register("invalid"))


def j(param1: int) -> None:
    """Jump execution to line a"""
    return _IC10("j", [param1], None)


def jal(param1: int) -> None:
    """Jump execution to line a and store next line number in ra"""
    return _IC10("jal", [param1], None)


def jr(param1: int) -> None:
    """Relative jump to line a"""
    return _IC10("jr", [param1], None)


def bdns(a: _Register | float) -> _Device:
    """Branch to line a if device d isn't set"""
    return _IC10("bdns", [a], _Register("invalid"))


def bdnsal(a: _Register | float) -> _Device:
    """Jump execution to line a and store next line number if device is not set"""
    return _IC10("bdnsal", [a], _Register("invalid"))


def bdse(a: _Register | float) -> _Device:
    """Branch to line a if device d is set"""
    return _IC10("bdse", [a], _Register("invalid"))


def bdseal(a: _Register | float) -> _Device:
    """Jump execution to line a and store next line number if device is set"""
    return _IC10("bdseal", [a], _Register("invalid"))


def brdns(a: _Register | float) -> _Device:
    """Relative branch to line a if device is not set"""
    return _IC10("brdns", [a], _Register("invalid"))


def brdse(a: _Register | float) -> _Device:
    """Relative branch to line a if device is set"""
    return _IC10("brdse", [a], _Register("invalid"))


def bap(
    a: _Register | float,
    b: _Register | float,
    c: _Register | float,
    d: _Register | float,
) -> None:
    """Branch to line d if abs(a - b) <= max(c * max(abs(a), abs(b)), float.epsilon * 8)"""
    return _IC10("bap", [a, b, c, d], None)


def brap(
    a: _Register | float,
    b: _Register | float,
    c: _Register | float,
    d: _Register | float,
) -> None:
    """Relative branch to line d if abs(a - b) <= max(c * max(abs(a), abs(b)), float.epsilon * 8)"""
    return _IC10("brap", [a, b, c, d], None)


def bapal(
    a: _Register | float,
    b: _Register | float,
    c: _Register | float,
    d: _Register | float,
) -> None:
    """Branch to line c if a != b and store next line number in ra"""
    return _IC10("bapal", [a, b, c, d], None)


def bapz(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if abs(a) <= max(b * abs(a), float.epsilon * 8)"""
    return _IC10("bapz", [a, b, c], None)


def brapz(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Relative branch to line c if abs(a) <= max(b * abs(a), float.epsilon * 8)"""
    return _IC10("brapz", [a, b, c], None)


def bapzal(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if abs(a) <= max(b * abs(a), float.epsilon * 8) and store next line number in ra"""
    return _IC10("bapzal", [a, b, c], None)


def beq(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if a == b"""
    return _IC10("beq", [a, b, c], None)


def breq(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Relative branch to line c if a == b"""
    return _IC10("breq", [a, b, c], None)


def beqal(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if a == b and store next line number in ra"""
    return _IC10("beqal", [a, b, c], None)


def beqz(a: _Register | float, b: _Register | float) -> None:
    """Branch to line b if a == 0"""
    return _IC10("beqz", [a, b], None)


def breqz(a: _Register | float, b: _Register | float) -> None:
    """Relative branch to line b if a == 0"""
    return _IC10("breqz", [a, b], None)


def beqzal(a: _Register | float, b: _Register | float) -> None:
    """Branch to line b if a == 0 and store next line number in ra"""
    return _IC10("beqzal", [a, b], None)


def bge(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if a >= b"""
    return _IC10("bge", [a, b, c], None)


def brge(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Relative branch to line c if a >= b"""
    return _IC10("brge", [a, b, c], None)


def bgeal(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if a >= b and store next line number in ra"""
    return _IC10("bgeal", [a, b, c], None)


def bgez(a: _Register | float, b: _Register | float) -> None:
    """Branch to line b if a >= 0"""
    return _IC10("bgez", [a, b], None)


def brgez(a: _Register | float, b: _Register | float) -> None:
    """Relative branch to line b if a >= 0"""
    return _IC10("brgez", [a, b], None)


def bgezal(a: _Register | float, b: _Register | float) -> None:
    """Branch to line b if a >= 0 and store next line number in ra"""
    return _IC10("bgezal", [a, b], None)


def bgt(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if a > b"""
    return _IC10("bgt", [a, b, c], None)


def brgt(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """relative branch to line c if a > b"""
    return _IC10("brgt", [a, b, c], None)


def bgtal(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if a > b and store next line number in ra"""
    return _IC10("bgtal", [a, b, c], None)


def bgtz(a: _Register | float, b: _Register | float) -> None:
    """Branch to line b if a > 0"""
    return _IC10("bgtz", [a, b], None)


def brgtz(a: _Register | float, b: _Register | float) -> None:
    """Relative branch to line b if a > 0"""
    return _IC10("brgtz", [a, b], None)


def bgtzal(a: _Register | float, b: _Register | float) -> None:
    """Branch to line b if a > 0 and store next line number in ra"""
    return _IC10("bgtzal", [a, b], None)


def ble(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if a <= b"""
    return _IC10("ble", [a, b, c], None)


def brle(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Relative branch to line c if a <= b"""
    return _IC10("brle", [a, b, c], None)


def bleal(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if a <= b and store next line number in ra"""
    return _IC10("bleal", [a, b, c], None)


def blez(a: _Register | float, b: _Register | float) -> None:
    """Branch to line b if a <= 0"""
    return _IC10("blez", [a, b], None)


def brlez(a: _Register | float, b: _Register | float) -> None:
    """Relative branch to line b if a <= 0"""
    return _IC10("brlez", [a, b], None)


def blezal(a: _Register | float, b: _Register | float) -> None:
    """Branch to line b if a <= 0 and store next line number in ra"""
    return _IC10("blezal", [a, b], None)


def blt(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if a < b"""
    return _IC10("blt", [a, b, c], None)


def brlt(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Relative branch to line c if a < b"""
    return _IC10("brlt", [a, b, c], None)


def bltal(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if a < b and store next line number in ra"""
    return _IC10("bltal", [a, b, c], None)


def bltz(a: _Register | float, b: _Register | float) -> None:
    """Branch to line b if a < 0"""
    return _IC10("bltz", [a, b], None)


def brltz(a: _Register | float, b: _Register | float) -> None:
    """Relative branch to line b if a < 0"""
    return _IC10("brltz", [a, b], None)


def bltzal(a: _Register | float, b: _Register | float) -> None:
    """Branch to line b if a < 0 and store next line number in ra"""
    return _IC10("bltzal", [a, b], None)


def bna(
    a: _Register | float,
    b: _Register | float,
    c: _Register | float,
    d: _Register | float,
) -> None:
    """Branch to line d if abs(a - b) > max(c * max(abs(a), abs(b)), float.epsilon * 8)"""
    return _IC10("bna", [a, b, c, d], None)


def brna(
    a: _Register | float,
    b: _Register | float,
    c: _Register | float,
    d: _Register | float,
) -> None:
    """Relative branch to line d if abs(a - b) > max(c * max(abs(a), abs(b)), float.epsilon * 8)"""
    return _IC10("brna", [a, b, c, d], None)


def bnaal(
    a: _Register | float,
    b: _Register | float,
    c: _Register | float,
    d: _Register | float,
) -> None:
    """Branch to line d if abs(a - b) <= max(c * max(abs(a), abs(b)), float.epsilon * 8) and store next line number in ra"""
    return _IC10("bnaal", [a, b, c, d], None)


def bnan(a: _Register | float, b: _Register | float) -> None:
    """Branch to line b if a is not a number (NaN)"""
    return _IC10("bnan", [a, b], None)


def brnan(a: _Register | float, b: _Register | float) -> None:
    """Relative branch to line b if a is not a number (NaN)"""
    return _IC10("brnan", [a, b], None)


def bnaz(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if abs(a) > max (b * abs(a), float.epsilon * 8)"""
    return _IC10("bnaz", [a, b, c], None)


def brnaz(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Relative branch to line c if abs(a) > max(b * abs(a), float.epsilon * 8)"""
    return _IC10("brnaz", [a, b, c], None)


def bnazal(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if abs(a) > max (b * abs(a), float.epsilon * 8) and store next line number in ra"""
    return _IC10("bnazal", [a, b, c], None)


def bne(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if a != b"""
    return _IC10("bne", [a, b, c], None)


def brne(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Relative branch to line c if a != b"""
    return _IC10("brne", [a, b, c], None)


def bneal(a: _Register | float, b: _Register | float, c: _Register | float) -> None:
    """Branch to line c if a != b and store next line number in ra"""
    return _IC10("bneal", [a, b, c], None)


def bnez(a: _Register | float, b: _Register | float) -> None:
    """branch to line b if a != 0"""
    return _IC10("bnez", [a, b], None)


def brnez(a: _Register | float, b: _Register | float) -> None:
    """Relative branch to line b if a != 0"""
    return _IC10("brnez", [a, b], None)


def bnezal(a: _Register | float, b: _Register | float) -> None:
    """Branch to line b if a != 0 and store next line number in ra"""
    return _IC10("bnezal", [a, b], None)


def HASH(name: str) -> float:
    from .types import compute_hash

    return compute_hash(name)


def STR(s: str) -> float:
    return f'STR("{s}")'
