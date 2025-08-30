# This file is auto-generated from IC10 instructions_data
from .types import *
from .types_generated import *


def alias(param1: str, param2: _Register | _Device):
    """Labels register or device reference with name, device references also affect what shows on the screws on the IC base."""
    return "alias " + f"{param1} {param2}"


def define(param1: str, param2: float):
    """Creates a label that will be replaced throughout the program with the provided value."""
    return "define " + f"{param1} {param2}"


def hcf():
    """Halt and catch fire"""
    return "hcf " + ""


def sleep(a: _Register | float):
    """Pauses execution on the IC for a seconds"""
    return "sleep " + f"{a}"


def yield_():
    """Pauses execution for 1 tick"""
    return "yield " + ""


def abs(output: _Register, a: _Register | float):
    """output = the absolute value of a"""
    return "abs " + f"{output} {a}"


def add(output: _Register, a: _Register | float, b: _Register | float):
    """output = a + b."""
    return "add " + f"{output} {a} {b}"


def ceil(output: _Register, a: _Register | float):
    """output = smallest integer greater than a"""
    return "ceil " + f"{output} {a}"


def div(output: _Register, a: _Register | float, b: _Register | float):
    """output = a / b"""
    return "div " + f"{output} {a} {b}"


def exp(output: _Register, a: _Register | float):
    """exp(a) or e^a"""
    return "exp " + f"{output} {a}"


def floor(output: _Register, a: _Register | float):
    """output = largest integer less than a"""
    return "floor " + f"{output} {a}"


def log(output: _Register, a: _Register | float):
    """base e log(a) or ln(a)"""
    return "log " + f"{output} {a}"


def max(output: _Register, a: _Register | float, b: _Register | float):
    """output = max of a or b"""
    return "max " + f"{output} {a} {b}"


def min(output: _Register, a: _Register | float, b: _Register | float):
    """output = min of a or b"""
    return "min " + f"{output} {a} {b}"


def mod(output: _Register, a: _Register | float, b: _Register | float):
    """output = a mod b (note: NOT a % b)"""
    return "mod " + f"{output} {a} {b}"


def move(output: _Register, a: _Register | float):
    """output = provided num or register value."""
    return "move " + f"{output} {a}"


def mul(output: _Register, a: _Register | float, b: _Register | float):
    """output = a * b"""
    return "mul " + f"{output} {a} {b}"


def rand(output: _Register):
    """output = a random value x with 0 <= x < 1"""
    return "rand " + f"{output}"


def round(output: _Register, a: _Register | float):
    """output = a rounded to nearest integer"""
    return "round " + f"{output} {a}"


def sqrt(output: _Register, a: _Register | float):
    """output = square root of a"""
    return "sqrt " + f"{output} {a}"


def sub(output: _Register, a: _Register | float, b: _Register | float):
    """output = a - b."""
    return "sub " + f"{output} {a} {b}"


def trunc(output: _Register, a: _Register | float):
    """output = a with fractional part removed"""
    return "trunc " + f"{output} {a}"


def acos(output: _Register, a: _Register | float):
    """Returns the angle (radians) whos cos is the specified value"""
    return "acos " + f"{output} {a}"


def asin(output: _Register, a: _Register | float):
    """Returns the angle (radians) whos sine is the specified value"""
    return "asin " + f"{output} {a}"


def atan(output: _Register, a: _Register | float):
    """Returns the angle (radians) whos tan is the specified value"""
    return "atan " + f"{output} {a}"


def atan2(output: _Register, a: _Register | float, b: _Register | float):
    """Returns the angle (radians) whose tangent is the quotient of two specified values: a (y) and b (x)"""
    return "atan2 " + f"{output} {a} {b}"


def cos(output: _Register, a: _Register | float):
    """Returns the cosine of the specified angle (radians)"""
    return "cos " + f"{output} {a}"


def sin(output: _Register, a: _Register | float):
    """Returns the sine of the specified angle (radians)"""
    return "sin " + f"{output} {a}"


def tan(output: _Register, a: _Register | float):
    """Returns the tan of the specified angle (radians)"""
    return "tan " + f"{output} {a}"


def clr(param1: _Device):
    """Clears the stack memory for the provided device."""
    return "clr " + f"{param1}"


def clrd(id: _Register | float):
    """Seeks directly for the provided device id and clears the stack memory of that device"""
    return "clrd " + f"{id}"


def get(output: _Register, param2: _Device, address: _Register | float):
    """Using the provided device, attempts to read the stack value at the provided address, and places it in the register."""
    return "get " + f"{output} {param2} {address}"


def getd(output: _Register, id: _Register | float, address: _Register | float):
    """Seeks directly for the provided device id, attempts to read the stack value at the provided address, and places it in the register."""
    return "getd " + f"{output} {id} {address}"


def peek(output: _Register):
    """output = the value at the top of the stack"""
    return "peek " + f"{output}"


def poke(address: _Register | float, value: _Register | float):
    """Stores the provided value at the provided address in the stack."""
    return "poke " + f"{address} {value}"


def pop(output: _Register):
    """output = the value at the top of the stack and decrements sp"""
    return "pop " + f"{output}"


def push(a: _Register | float):
    """Pushes the value of a to the stack at sp and increments sp"""
    return "push " + f"{a}"


def put(param1: _Device, address: _Register | float, value: _Register | float):
    """Using the provided device, attempts to write the provided value to the stack at the provided address."""
    return "put " + f"{param1} {address} {value}"


def putd(id: _Register | float, address: _Register | float, value: _Register | float):
    """Seeks directly for the provided device id, attempts to write the provided value to the stack at the provided address."""
    return "putd " + f"{id} {address} {value}"


def l(output: _Register, param2: _Device, param3: _logicType):
    """Loads device LogicType to register by housing index value."""
    return "l " + f"{output} {param2} {param3}"


def ld(output: _Register, id: _Register | float, param3: _logicType):
    """Loads device LogicType to register by direct ID reference."""
    return "ld " + f"{output} {id} {param3}"


def lr(output: _Register, param2: _Device, param3: _reagentMode, param4: int):
    """Loads reagent of device's ReagentMode where a hash of the reagent type to check for. ReagentMode can be either Contents (0), Required (1), Recipe (2). Can use either the word, or the number."""
    return "lr " + f"{output} {param2} {param3} {param4}"


def ls(output: _Register, param2: _Device, param3: _slotIndex, param4: _logicSlotType):
    """Loads slot LogicSlotType on device to register."""
    return "ls " + f"{output} {param2} {param3} {param4}"


def s(param1: _Device, param2: _logicType, param3: _Register):
    """Stores register value to LogicType on device by housing index value."""
    return "s " + f"{param1} {param2} {param3}"


def sd(id: _Register | float, param2: _logicType, param3: _Register):
    """Stores register value to LogicType on device by direct ID reference."""
    return "sd " + f"{id} {param2} {param3}"


def ss(param1: _Device, param2: _slotIndex, param3: _logicSlotType, param4: _Register):
    """Stores register value to device stored in a slot LogicSlotType on device."""
    return "ss " + f"{param1} {param2} {param3} {param4}"


def rmap(param1: _Register, param2: _Device, reagentHash: _Register | float):
    """Given a reagent hash, store the corresponding prefab hash that the device expects to fulfill the reagent requirement. For example, on an autolathe, the hash for Iron will store the hash for ItemIronIngot."""
    return "rmap " + f"{param1} {param2} {reagentHash}"


def lb(output: _Register, param2: _deviceHash, param3: _logicType, param4: _batchMode):
    """Loads LogicType from all output network devices with provided type hash using the provide batch mode. Average (0), Sum (1), Minimum (2), Maximum (3). Can use either the word, or the number."""
    return "lb " + f"{output} {param2} {param3} {param4}"


def lbn(
    output: _Register,
    param2: _deviceHash,
    param3: _nameHash,
    param4: _logicType,
    param5: _batchMode,
):
    """Loads LogicType from all output network devices with provided type and name hashes using the provide batch mode. Average (0), Sum (1), Minimum (2), Maximum (3). Can use either the word, or the number."""
    return "lbn " + f"{output} {param2} {param3} {param4} {param5}"


def lbns(
    output: _Register,
    param2: _deviceHash,
    param3: _nameHash,
    param4: _slotIndex,
    param5: _logicSlotType,
    param6: _batchMode,
):
    """Loads LogicSlotType from slotIndex from all output network devices with provided type and name hashes using the provide batch mode. Average (0), Sum (1), Minimum (2), Maximum (3). Can use either the word, or the number."""
    return "lbns " + f"{output} {param2} {param3} {param4} {param5} {param6}"


def lbs(
    output: _Register,
    param2: _deviceHash,
    param3: _slotIndex,
    param4: _logicSlotType,
    param5: _batchMode,
):
    """Loads LogicSlotType from slotIndex from all output network devices with provided type hash using the provide batch mode. Average (0), Sum (1), Minimum (2), Maximum (3). Can use either the word, or the number."""
    return "lbs " + f"{output} {param2} {param3} {param4} {param5}"


def sb(param1: _deviceHash, param2: _logicType, param3: _Register):
    """Stores register value to LogicType on all output network devices with provided type hash."""
    return "sb " + f"{param1} {param2} {param3}"


def sbn(param1: _deviceHash, param2: _nameHash, param3: _logicType, param4: _Register):
    """Stores register value to LogicType on all output network devices with provided type hash and name."""
    return "sbn " + f"{param1} {param2} {param3} {param4}"


def sbs(
    param1: _deviceHash, param2: _slotIndex, param3: _logicSlotType, param4: _Register
):
    """Stores register value to LogicSlotType on all output network devices with provided type hash in the provided slot."""
    return "sbs " + f"{param1} {param2} {param3} {param4}"


def and_(output: _Register, a: _Register | float, b: _Register | float):
    """Performs a bitwise logical AND operation on the binary representation of two values. Each bit of the result is determined by evaluating the corresponding bits of the input values. If both bits are 1, the resulting bit is set to 1. Otherwise the resulting bit is set to 0."""
    return "and " + f"{output} {a} {b}"


def nor(output: _Register, a: _Register | float, b: _Register | float):
    """Performs a bitwise logical NOR (NOT OR) operation on the binary representation of two values. Each bit of the result is determined by evaluating the corresponding bits of the input values. If both bits are 0, the resulting bit is set to 1. Otherwise, if at least one bit is 1, the resulting bit is set to 0."""
    return "nor " + f"{output} {a} {b}"


def not_(output: _Register, a: _Register | float):
    """Performs a bitwise logical NOT operation flipping each bit of the input value, resulting in a binary complement. If a bit is 1, it becomes 0, and if a bit is 0, it becomes 1."""
    return "not " + f"{output} {a}"


def or_(output: _Register, a: _Register | float, b: _Register | float):
    """Performs a bitwise logical OR operation on the binary representation of two values. Each bit of the result is determined by evaluating the corresponding bits of the input values. If either bit is 1, the resulting bit is set to 1. If both bits are 0, the resulting bit is set to 0."""
    return "or " + f"{output} {a} {b}"


def sla(output: _Register, a: _Register | float, b: _Register | float):
    """Performs a bitwise arithmetic left shift operation on the binary representation of a value. It shifts the bits to the left and fills the vacated rightmost bits with zeros (note that this is indistinguishable from 'sll')."""
    return "sla " + f"{output} {a} {b}"


def sll(output: _Register, a: _Register | float, b: _Register | float):
    """Performs a bitwise logical left shift operation on the binary representation of a value. It shifts the bits to the left and fills the vacated rightmost bits with zeros."""
    return "sll " + f"{output} {a} {b}"


def sra(output: _Register, a: _Register | float, b: _Register | float):
    """Performs a bitwise arithmetic right shift operation on the binary representation of a value. It shifts the bits to the right and fills the vacated leftmost bits with a copy of the sign bit (the most significant bit)."""
    return "sra " + f"{output} {a} {b}"


def srl(output: _Register, a: _Register | float, b: _Register | float):
    """Performs a bitwise logical right shift operation on the binary representation of a value. It shifts the bits to the right and fills the vacated leftmost bits with zeros"""
    return "srl " + f"{output} {a} {b}"


def xor(output: _Register, a: _Register | float, b: _Register | float):
    """Performs a bitwise logical XOR (exclusive OR) operation on the binary representation of two values. Each bit of the result is determined by evaluating the corresponding bits of the input values. If the bits are different (one bit is 0 and the other is 1), the resulting bit is set to 1. If the bits are the same (both 0 or both 1), the resulting bit is set to 0."""
    return "xor " + f"{output} {a} {b}"


def select(
    output: _Register, a: _Register | float, b: _Register | float, c: _Register | float
):
    """output = b if a is non-zero, otherwise c"""
    return "select " + f"{output} {a} {b} {c}"


def sdns(output: _Register, param2: _Device):
    """output = 1 if device is not set, otherwise 0"""
    return "sdns " + f"{output} {param2}"


def sdse(output: _Register, param2: _Device):
    """output = 1 if device is set, otherwise 0."""
    return "sdse " + f"{output} {param2}"


def sap(
    output: _Register, a: _Register | float, b: _Register | float, c: _Register | float
):
    """output = 1 if abs(a - b) <= max(c * max(abs(a), abs(b)), float.epsilon * 8), otherwise 0"""
    return "sap " + f"{output} {a} {b} {c}"


def sapz(output: _Register, a: _Register | float, b: _Register | float):
    """output = 1 if abs(a) <= max(b * abs(a), float.epsilon * 8), otherwise 0"""
    return "sapz " + f"{output} {a} {b}"


def seq(output: _Register, a: _Register | float, b: _Register | float):
    """output = 1 if a == b, otherwise 0"""
    return "seq " + f"{output} {a} {b}"


def seqz(output: _Register, a: _Register | float):
    """output = 1 if a == 0, otherwise 0"""
    return "seqz " + f"{output} {a}"


def sge(output: _Register, a: _Register | float, b: _Register | float):
    """output = 1 if a >= b, otherwise 0"""
    return "sge " + f"{output} {a} {b}"


def sgez(output: _Register, a: _Register | float):
    """output = 1 if a >= 0, otherwise 0"""
    return "sgez " + f"{output} {a}"


def sgt(output: _Register, a: _Register | float, b: _Register | float):
    """output = 1 if a > b, otherwise 0"""
    return "sgt " + f"{output} {a} {b}"


def sgtz(output: _Register, a: _Register | float):
    """output = 1 if a > 0, otherwise 0"""
    return "sgtz " + f"{output} {a}"


def sle(output: _Register, a: _Register | float, b: _Register | float):
    """output = 1 if a <= b, otherwise 0"""
    return "sle " + f"{output} {a} {b}"


def slez(output: _Register, a: _Register | float):
    """output = 1 if a <= 0, otherwise 0"""
    return "slez " + f"{output} {a}"


def slt(output: _Register, a: _Register | float, b: _Register | float):
    """output = 1 if a < b, otherwise 0"""
    return "slt " + f"{output} {a} {b}"


def sltz(output: _Register, a: _Register | float):
    """output = 1 if a < 0, otherwise 0"""
    return "sltz " + f"{output} {a}"


def sna(
    output: _Register, a: _Register | float, b: _Register | float, c: _Register | float
):
    """output = 1 if abs(a - b) > max(c * max(abs(a), abs(b)), float.epsilon * 8), otherwise 0"""
    return "sna " + f"{output} {a} {b} {c}"


def snan(output: _Register, a: _Register | float):
    """output = 1 if a is NaN, otherwise 0"""
    return "snan " + f"{output} {a}"


def snanz(output: _Register, a: _Register | float):
    """output = 0 if a is NaN, otherwise 1"""
    return "snanz " + f"{output} {a}"


def snaz(output: _Register, a: _Register | float, b: _Register | float):
    """output = 1 if abs(a) > max(b * abs(a), float.epsilon), otherwise 0"""
    return "snaz " + f"{output} {a} {b}"


def sne(output: _Register, a: _Register | float, b: _Register | float):
    """output = 1 if a != b, otherwise 0"""
    return "sne " + f"{output} {a} {b}"


def snez(output: _Register, a: _Register | float):
    """output = 1 if a != 0, otherwise 0"""
    return "snez " + f"{output} {a}"


def j(param1: int):
    """Jump execution to line a"""
    return "j " + f"{param1}"


def jal(param1: int):
    """Jump execution to line a and store next line number in ra"""
    return "jal " + f"{param1}"


def jr(param1: int):
    """Relative jump to line a"""
    return "jr " + f"{param1}"


def bdns(output: _Device, a: _Register | float):
    """Branch to line a if device d isn't set"""
    return "bdns " + f"{output} {a}"


def bdnsal(output: _Device, a: _Register | float):
    """Jump execution to line a and store next line number if device is not set"""
    return "bdnsal " + f"{output} {a}"


def bdse(output: _Device, a: _Register | float):
    """Branch to line a if device d is set"""
    return "bdse " + f"{output} {a}"


def bdseal(output: _Device, a: _Register | float):
    """Jump execution to line a and store next line number if device is set"""
    return "bdseal " + f"{output} {a}"


def brdns(output: _Device, a: _Register | float):
    """Relative branch to line a if device is not set"""
    return "brdns " + f"{output} {a}"


def brdse(output: _Device, a: _Register | float):
    """Relative branch to line a if device is set"""
    return "brdse " + f"{output} {a}"


def bap(
    a: _Register | float,
    b: _Register | float,
    c: _Register | float,
    d: _Register | float,
):
    """Branch to line d if abs(a - b) <= max(c * max(abs(a), abs(b)), float.epsilon * 8)"""
    return "bap " + f"{a} {b} {c} {d}"


def brap(
    a: _Register | float,
    b: _Register | float,
    c: _Register | float,
    d: _Register | float,
):
    """Relative branch to line d if abs(a - b) <= max(c * max(abs(a), abs(b)), float.epsilon * 8)"""
    return "brap " + f"{a} {b} {c} {d}"


def bapal(
    a: _Register | float,
    b: _Register | float,
    c: _Register | float,
    d: _Register | float,
):
    """Branch to line c if a != b and store next line number in ra"""
    return "bapal " + f"{a} {b} {c} {d}"


def bapz(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if abs(a) <= max(b * abs(a), float.epsilon * 8)"""
    return "bapz " + f"{a} {b} {c}"


def brapz(a: _Register | float, b: _Register | float, c: _Register | float):
    """Relative branch to line c if abs(a) <= max(b * abs(a), float.epsilon * 8)"""
    return "brapz " + f"{a} {b} {c}"


def bapzal(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if abs(a) <= max(b * abs(a), float.epsilon * 8) and store next line number in ra"""
    return "bapzal " + f"{a} {b} {c}"


def beq(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if a == b"""
    return "beq " + f"{a} {b} {c}"


def breq(a: _Register | float, b: _Register | float, c: _Register | float):
    """Relative branch to line c if a == b"""
    return "breq " + f"{a} {b} {c}"


def beqal(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if a == b and store next line number in ra"""
    return "beqal " + f"{a} {b} {c}"


def beqz(a: _Register | float, b: _Register | float):
    """Branch to line b if a == 0"""
    return "beqz " + f"{a} {b}"


def breqz(a: _Register | float, b: _Register | float):
    """Relative branch to line b if a == 0"""
    return "breqz " + f"{a} {b}"


def beqzal(a: _Register | float, b: _Register | float):
    """Branch to line b if a == 0 and store next line number in ra"""
    return "beqzal " + f"{a} {b}"


def bge(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if a >= b"""
    return "bge " + f"{a} {b} {c}"


def brge(a: _Register | float, b: _Register | float, c: _Register | float):
    """Relative branch to line c if a >= b"""
    return "brge " + f"{a} {b} {c}"


def bgeal(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if a >= b and store next line number in ra"""
    return "bgeal " + f"{a} {b} {c}"


def bgez(a: _Register | float, b: _Register | float):
    """Branch to line b if a >= 0"""
    return "bgez " + f"{a} {b}"


def brgez(a: _Register | float, b: _Register | float):
    """Relative branch to line b if a >= 0"""
    return "brgez " + f"{a} {b}"


def bgezal(a: _Register | float, b: _Register | float):
    """Branch to line b if a >= 0 and store next line number in ra"""
    return "bgezal " + f"{a} {b}"


def bgt(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if a > b"""
    return "bgt " + f"{a} {b} {c}"


def brgt(a: _Register | float, b: _Register | float, c: _Register | float):
    """relative branch to line c if a > b"""
    return "brgt " + f"{a} {b} {c}"


def bgtal(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if a > b and store next line number in ra"""
    return "bgtal " + f"{a} {b} {c}"


def bgtz(a: _Register | float, b: _Register | float):
    """Branch to line b if a > 0"""
    return "bgtz " + f"{a} {b}"


def brgtz(a: _Register | float, b: _Register | float):
    """Relative branch to line b if a > 0"""
    return "brgtz " + f"{a} {b}"


def bgtzal(a: _Register | float, b: _Register | float):
    """Branch to line b if a > 0 and store next line number in ra"""
    return "bgtzal " + f"{a} {b}"


def ble(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if a <= b"""
    return "ble " + f"{a} {b} {c}"


def brle(a: _Register | float, b: _Register | float, c: _Register | float):
    """Relative branch to line c if a <= b"""
    return "brle " + f"{a} {b} {c}"


def bleal(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if a <= b and store next line number in ra"""
    return "bleal " + f"{a} {b} {c}"


def blez(a: _Register | float, b: _Register | float):
    """Branch to line b if a <= 0"""
    return "blez " + f"{a} {b}"


def brlez(a: _Register | float, b: _Register | float):
    """Relative branch to line b if a <= 0"""
    return "brlez " + f"{a} {b}"


def blezal(a: _Register | float, b: _Register | float):
    """Branch to line b if a <= 0 and store next line number in ra"""
    return "blezal " + f"{a} {b}"


def blt(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if a < b"""
    return "blt " + f"{a} {b} {c}"


def brlt(a: _Register | float, b: _Register | float, c: _Register | float):
    """Relative branch to line c if a < b"""
    return "brlt " + f"{a} {b} {c}"


def bltal(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if a < b and store next line number in ra"""
    return "bltal " + f"{a} {b} {c}"


def bltz(a: _Register | float, b: _Register | float):
    """Branch to line b if a < 0"""
    return "bltz " + f"{a} {b}"


def brltz(a: _Register | float, b: _Register | float):
    """Relative branch to line b if a < 0"""
    return "brltz " + f"{a} {b}"


def bltzal(a: _Register | float, b: _Register | float):
    """Branch to line b if a < 0 and store next line number in ra"""
    return "bltzal " + f"{a} {b}"


def bna(
    a: _Register | float,
    b: _Register | float,
    c: _Register | float,
    d: _Register | float,
):
    """Branch to line d if abs(a - b) > max(c * max(abs(a), abs(b)), float.epsilon * 8)"""
    return "bna " + f"{a} {b} {c} {d}"


def brna(
    a: _Register | float,
    b: _Register | float,
    c: _Register | float,
    d: _Register | float,
):
    """Relative branch to line d if abs(a - b) > max(c * max(abs(a), abs(b)), float.epsilon * 8)"""
    return "brna " + f"{a} {b} {c} {d}"


def bnaal(
    a: _Register | float,
    b: _Register | float,
    c: _Register | float,
    d: _Register | float,
):
    """Branch to line d if abs(a - b) <= max(c * max(abs(a), abs(b)), float.epsilon * 8) and store next line number in ra"""
    return "bnaal " + f"{a} {b} {c} {d}"


def bnan(a: _Register | float, b: _Register | float):
    """Branch to line b if a is not a number (NaN)"""
    return "bnan " + f"{a} {b}"


def brnan(a: _Register | float, b: _Register | float):
    """Relative branch to line b if a is not a number (NaN)"""
    return "brnan " + f"{a} {b}"


def bnaz(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if abs(a) > max (b * abs(a), float.epsilon * 8)"""
    return "bnaz " + f"{a} {b} {c}"


def brnaz(a: _Register | float, b: _Register | float, c: _Register | float):
    """Relative branch to line c if abs(a) > max(b * abs(a), float.epsilon * 8)"""
    return "brnaz " + f"{a} {b} {c}"


def bnazal(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if abs(a) > max (b * abs(a), float.epsilon * 8) and store next line number in ra"""
    return "bnazal " + f"{a} {b} {c}"


def bne(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if a != b"""
    return "bne " + f"{a} {b} {c}"


def brne(a: _Register | float, b: _Register | float, c: _Register | float):
    """Relative branch to line c if a != b"""
    return "brne " + f"{a} {b} {c}"


def bneal(a: _Register | float, b: _Register | float, c: _Register | float):
    """Branch to line c if a != b and store next line number in ra"""
    return "bneal " + f"{a} {b} {c}"


def bnez(a: _Register | float, b: _Register | float):
    """branch to line b if a != 0"""
    return "bnez " + f"{a} {b}"


def brnez(a: _Register | float, b: _Register | float):
    """Relative branch to line b if a != 0"""
    return "brnez " + f"{a} {b}"


def bnezal(a: _Register | float, b: _Register | float):
    """Branch to line b if a != 0 and store next line number in ra"""
    return "bnezal " + f"{a} {b}"


def HASH(name: str) -> float:
    return f"HASH({name})"


def STR(s: str) -> float:
    return f"STR({s})"
