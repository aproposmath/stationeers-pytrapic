from stationeers_pytrapic.symbols import *

# Airlock control script for Stationeers PyTrapIC
# All devices are accessed through their names
# Vent and GlassDoor are either named "In" or "Out" as name
# Switch is a DiodeSlide named "Switch"

# Using a light as a switch is better, as a button press cannot be "missed"
# in more complex codes. Also it provies feedback to the player.

h_in = HASH("In")
h_out = HASH("Out")
h_switch = HASH("Switch")

GlassDoors[h_in].Lock = True
GlassDoors[h_out].Lock = True
ActiveVents[h_in].Mode = True
ActiveVents[h_in].On = False
ActiveVents[h_out].Mode = True
ActiveVents[h_out].On = False

while True:
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
