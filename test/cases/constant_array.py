from stationeers_pytrapic.symbols import *
i = db.Setting

db.On = [3,6,7,3,6][i]
db.Setting = 999
db.On = [123, 456][i]
db.Setting = 999
db.On = [777][i]

def show_amount(gas_type_index):
    arr = [HASH("O2"), HASH("N2"), HASH("CO2")]
    h = arr[gas_type_index]

    sensor = GasSensors[h].Average
    ConsoleLED5s[h].Setting = sensor.Pressure


while True:
    for i in range(3):
        show_amount(i)
