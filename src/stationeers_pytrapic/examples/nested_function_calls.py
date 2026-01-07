from stationeers_pytrapic.symbols import *


def inner_function():
    GrowLights.On = True


def outer_function():
    # do some stuff
    GrowLights.On = False

    # call the inner function
    inner_function()
    inner_function()


outer_function()

db.Setting = GrowLights.On.Maximum
