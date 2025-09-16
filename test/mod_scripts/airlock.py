from stationeers_pytrapic.symbols import *
from library import airlock

airlock.init()

while True:
    yield_()
    airlock.update()
