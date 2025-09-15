from stationeers_pytrapic.symbols import *
import library.airlock as airlock
import library.solar as solar

airlock.init()
solar.init()

num_calls = 88

while True:
    yield_()
    airlock.update()
    solar.update()
    num_calls -= 1
    db.Setting = num_calls
