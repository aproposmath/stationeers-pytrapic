from stationeers_pytrapic.symbols import *


def while_condition():
    # blocking wait until pressure is 0
    while GasSensors["Airlock"].Average.Pressure > 0:
        pass


def for_range():
    sum = 0
    for i in range(10):
        sum += stack[i]
    return sum


def for_list():
    for name_hash in [HASH("O2"), HASH("N2"), HASH("VOL"), HASH("CO2")]:
        pressure = PipeAnalysizers[name_hash].Average.Pressure
        ConsoleLED1x2s[name_hash].Setting = pressure


# typical endless loop as main entry point
while True:
    while_condition()
    db.Setting = for_range()
    for_list()
    for_range()
