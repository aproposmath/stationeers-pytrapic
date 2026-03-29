from stationeers_pytrapic.symbols import *

analyzer = PipeAnalysizers["NightAir"].Average
sensor = GasSensors["Outside"].Minimum
vents = ActiveVents

while True:
    vents.On = analyzer.Pressure < 5000 and sensor.Temperature < 273.15 + 140
