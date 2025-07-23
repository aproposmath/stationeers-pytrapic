from stationeers_pytrapic.symbols import *

panels = SolarPanel  # port facing north
sensor = d1  # port facing east

while True:
    panels.Horizontal = sensor.Horizontal
    panels.Vertical = 90 - sensor.Vertical
