# pytrapic: use_push_pop_functions
from stationeers_pytrapic.symbols import *


def add_two(a, b):
    return a + b


def compute(x, y, z):
    return add_two(x + y, z)


db.Setting = compute(1, 2, 3)
