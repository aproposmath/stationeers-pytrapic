from stationeer_pytrapic.symbols import *

panels = SolarPanels  # port facing north
sensor = DaylightSensor(d0)  # port facing east


def init():
    pass


def update():
    panels.Horizontal = sensor.Horizontal
    panels.Vertical = 90 - sensor.Vertical


if __name__ == "__main__":
    init()
    while True:
        update()
        yield_()
