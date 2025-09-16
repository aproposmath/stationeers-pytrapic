from stationeers_pytrapic.symbols import *
from library import airlock
from library import solar

airlock.init()
solar.init()

num_calls = 88

while True:
    yield_()
    airlock.update()
    solar.update()
    num_calls -= 1
    db.Setting = num_calls
