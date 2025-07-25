from stationeers_pytrapic.symbols import *

light_sensor = DaylightSensor(d0)
grow_light = GrowLight(d1)


# define all utility functions here
def handle_solar_panels():
    panels = SolarPanels  # port facing north

    panels.Horizontal = light_sensor.Horizontal
    panels.Vertical = 90 - light_sensor.Vertical


def handle_growlight():
    grow_light.On = light_sensor.Vertical > 90

def setup_airlock():
    h_in = HASH("In")
    h_out = HASH("Out")

    GlassDoors[h_in].Lock = True
    GlassDoors[h_out].Lock = True
    ActiveVents[h_in].Mode = True
    ActiveVents[h_in].On = False
    ActiveVents[h_out].Mode = True
    ActiveVents[h_out].On = False

def handle_airlock():
    h_in = HASH("In")
    h_out = HASH("Out")
    h_switch = HASH("Switch")

    if DiodeSlides[h_switch].On.Maximum > 0:
        going_out = GlassDoors[h_in].Open.Maximum > 0
        dir_to = h_out if going_out else h_in
        dir_from = h_in if going_out else h_out
        GlassDoors[dir_from].Open = False
        ActiveVents[dir_from].On = True

        while GasSensors.Pressure.Maximum != 0:
            pass
        sleep(0.2)

        ActiveVents[dir_from].On = False
        GlassDoors[dir_to].Open = True
        DiodeSlides[h_switch].On = False
        sleep(1)


# set only one if statement to True, to ignore the other function calls

# first IC: grow light and airlock
if True:
    setup_airlock()
    while True:
        handle_airlock()
        handle_growlight()

# second IC: solar panels
if False:
    while True:
        handle_solar_panels()
