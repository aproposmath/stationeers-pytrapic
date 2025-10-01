from stationeers_pytrapic.symbols import *

while True:
    charge = Batteries.Ratio.Average

    if charge < 0.2:
        continue

    if charge < 0.1:
        break

    ArcFurnaces.Activate = True
