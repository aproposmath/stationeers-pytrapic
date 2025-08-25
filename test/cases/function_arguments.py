from stationeers_pytrapic.symbols import *


def set_enable_fuel_generator(on):
    SolidFuelGenerators.On = on


while True:
    set_enable_fuel_generator(Batterys.Ratio.Average < 0.2)
