from stationeers_pytrapic.symbols import *

# a gets assigned r0
a = DaylightSensors.Horizontal.Minimum
while True:
    a += 1
    if a > 10:
        break

    # also b gets assigned r0, because a is not read below
    b = 3
    b *= DaylightSensors.Horizontal.Maximum
