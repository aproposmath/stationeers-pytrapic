from stationeers_pytrapic.symbols import *

light_sensor = d0


# define all utility functions here
def handle_solar_panels():
    panels = SolarPanel  # port facing north
    sensor = d1  # port facing east

    panels.Horizontal = sensor.Horizontal
    panels.Vertical = 90 - sensor.Vertical


def handle_growlight():
    GrowLight.On = light_sensor.Vertical > 90


def handle_airlock():
    h_in = HASH("In")
    h_out = HASH("Out")
    h_switch = HASH("Switch")

    GlassDoor[h_in].Lock = True
    GlassDoor[h_out].Lock = True
    ActiveVent[h_in].Mode = True
    ActiveVent[h_in].On = False
    ActiveVent[h_out].Mode = True
    ActiveVent[h_out].On = False

    while True:
        if DiodeSlide[h_switch].On.Maximum > 0:
            going_out = GlassDoor[h_in].Open.Maximum > 0
            dir_to = h_out if going_out else h_in
            dir_from = h_in if going_out else h_out
            GlassDoor[dir_from].Open = False
            ActiveVent[dir_from].On = True

            while GasSensor.Pressure.Maximum != 0:
                pass
            sleep(0.2)

            ActiveVent[dir_from].On = False
            GlassDoor[dir_to].Open = True
            DiodeSlide[h_switch].On = False
            sleep(1)


# set only one if statement to True, to ignore the other function calls

# first IC: grow light and airlock
if True:
    while True:
        handle_growlight()
        handle_airlock()

# second IC: solar panels
if False:
    while True:
        handle_solar_panels()
