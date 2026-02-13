from stationeers_pytrapic.symbols import *

# Builtin functions STR and HASH
# Depending on compiler settings, they will be evaluated at compile time
db.Setting = STR("Hello")
db.Setting = HASH("StructureAutholathe")

# all ic10 instructions are available as python functions
push(HASH("Some name"))

# instructions with an output argument will return a value and have one operand less
db.Setting = pop()

# any string argument of an intrinsic will be emited as-is
# but variables (bat_name) are also supported
but_name = HASH("Main Battery")
charge = lbn("HASH('StructureBattery')", bat_name, "Average", LogicType.Ratio)
Diodes["Low Power"].On = charge < 0.1
