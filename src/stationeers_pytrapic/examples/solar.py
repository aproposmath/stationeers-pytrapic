from stationeers_pytrapic.symbols import *

panels = SolarPanels  # port facing north
sensor = DaylightSensor(d0)  # port facing east

while True:
    panels.Horizontal = sensor.Horizontal
    panels.Vertical = 90 - sensor.Vertical
