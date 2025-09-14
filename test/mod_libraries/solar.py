from stationeer_pytrapic.symbols import *

panels = SolarPanels  # port facing north
sensor = DaylightSensor(d0)  # port facing east


def init():
    pass


def update():
    panels.Horizontal = sensor.Horizontal
    panels.Vertical = 90 - sensor.Vertical
