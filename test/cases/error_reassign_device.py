from stationeers_pytrapic.symbols import *

# this should fail because reassigning a device name is not allowed
light = GrowLight(ref_id=0x00)


def f():
    global light
    light = GrowLight(ref_id=0x01)
    light.Lock = True


f()
light.Lock = True
