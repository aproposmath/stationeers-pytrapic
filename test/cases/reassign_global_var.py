from stationeers_pytrapic.symbols import *

name_hash = HASH("foo")


def f():
    global name_hash
    name_hash = HASH("bar")
    GrowLights[name_hash].Lock = True


GrowLights[name_hash].Lock = True
f()
GrowLights[name_hash].Lock = True
