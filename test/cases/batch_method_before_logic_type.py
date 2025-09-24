from stationeers_pytrapic.symbols import *

tank = TankSmallInsulateds["NightAir"].Average
sensor = GasSensors["Outside"].Minimum
vents = ActiveVents

while True:
    vents.On = tank.Pressure < 5000 and sensor.Temperature < 273.15 + 140
