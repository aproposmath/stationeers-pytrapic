from stationeers_pytrapic.symbols import *
import library.solar as solar

solar.init()

while True:
    yield_()
    solar.update()
