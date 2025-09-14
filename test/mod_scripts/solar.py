from stationeers_pytrapic.symbols import *
from library import solar

solar.init()

while True:
    yield_()
    solar.update()
