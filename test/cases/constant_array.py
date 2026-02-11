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


def len1():
    db.Setting = [90][db.On]

def len2():
    db.Setting = [90, 91][db.On]

def len3():
    db.Setting = [90, 91, 92][db.On]
                      
def len4():           
    db.Setting = [90, 91, 92, 93][db.On]
                      
def len5():           
    db.Setting = [90, 91, 92, 93, 94][db.On]
                      
def len6():           
    db.Setting = [90, 91, 92, 93, 94, 95][db.On]
                      
def len7():           
    db.Setting = [90, 91, 92, 93, 94, 95, 96][db.On]
                      
def len8():           
    db.Setting = [90, 91, 92, 93, 94, 95, 96, 97][db.On]


while True:
    for i in range(3):
        show_amount(i)
    len1()
    len2()
    len3()
    len4()
    len5()
    len6()
    len7()
    len8()
