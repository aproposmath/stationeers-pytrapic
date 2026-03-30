from stationeers_pytrapic.symbols import *

pump = VolumePump(d0, alias=True)
furnace = ArcFurnace(d1, alias=True)

while True:
    yield_()
    if sdse(pump):
        pump.On = True

    if sdns(furnace):
        continue

    furnace.Activate = True
