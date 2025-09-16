from stationeers_pytrapic.symbols import *


def inner_function():
    GrowLights.On = True


def outer_function():
    # this function calls another function,
    # so we have to save the return address
    # and restore it after the call
    push(ra)

    # do some stuff
    GrowLights.On = False

    # call the inner function
    inner_function()
    inner_function()

    # pop ra again before the function returns
    ra = pop()


outer_function()

db.Setting = GrowLights.On.Maximum
