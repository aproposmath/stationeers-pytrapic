from stationeers_pytrapic.symbols import *


def set_enable_fuel_generator(on):
    SolidFuelGenerators.On = on


def set_stack_entry(entry0, entry1, entry2, entry3):
    device_stack = Stack(device_id=0xBEEF)
    device_stack[0] = entry0
    device_stack[1] = entry1
    device_stack[2] = entry2
    device_stack[3] = entry3


while True:
    set_enable_fuel_generator(Batteries.Ratio.Average < 0.2)
    set_stack_entry(6, 5, 4, 3)
