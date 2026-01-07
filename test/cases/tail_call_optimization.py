from stationeers_pytrapic.symbols import *


def inner():
    db.Setting = 0


def outer1():
    db.Setting = 1
    inner()


def outer2():
    db.Setting = 2
    inner()
    db.Setting = 3


while True:
    outer1()
    outer1()
    outer2()
    outer2()


