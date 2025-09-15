from stationeers_pytrapic.symbols import *
import library.airlock as airlock

airlock.init()

while True:
    yield_()
    airlock.update()
