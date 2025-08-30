from stationeers_pytrapic.symbols import *


def f_inner():
    return db.Setting + db.Setting


def f_mid():
    return f_inner() * f_inner()


def f_outer():
    return f_mid() + f_mid() + f_inner()


while True:
    db.Setting = f_outer() + f_outer() + f_mid()
