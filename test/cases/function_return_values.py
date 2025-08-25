from stationeers_pytrapic.symbols import *


def get_battery_charge():
    return Batterys.Ratio.Average


while True:
    SolidFuelGenerators.On = get_battery_charge() < 0.2
