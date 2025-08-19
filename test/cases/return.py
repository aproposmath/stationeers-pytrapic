from stationeers_pytrapic.symbols import *


def f0():
    return


def f1():
    return


def f2():
    charge = Batterys.Ratio.Average

    if charge > 0.2:
        return

    ArcFurnaces.Activate = True


def f3():
    charge = Batterys.Ratio.Average

    if charge < 0.2:
        return

    ArcFurnaces.Activate = True


while True:
    f0()
    f1()
    f1()
    f2()
    f3()
    f3()
