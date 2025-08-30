from stationeers_pytrapic.symbols import *


def align_solar_panels(panels, sensor):
    panels.Horizontal = sensor.Horizontal
    panels.Vertical = 90 - sensor.Vertical


while True:
    align_solar_panels(SolarPanels, DaylightSensor(d0))
