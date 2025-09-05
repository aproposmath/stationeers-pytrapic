from stationeers_pytrapic.symbols import *


def handle_furnace():
    furnace = ArcFurnace(d0)
    if furnace.Import.Occupied:
        furnace.Activate = True
    tmp = furnace.slot0.PrefabHash
    furnace.Export.Occupied = tmp


def handle_furnaces():
    furnaces = ArcFurnaces
    if furnaces.Import.Occupied.Maximum:
        furnaces.Activate = True
    tmp = furnaces.slot0.PrefabHash.Maximum
    furnaces.Export.Occupied = tmp


while True:
    handle_furnace()
    handle_furnaces()
