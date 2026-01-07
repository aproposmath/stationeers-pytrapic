from stationeers_pytrapic.symbols import *


def main():
    prev_ok = False
    while True:
        yield_()
        ok = LogicSwitchs[HASH("Connect")].Open.Maximum
        if ok and not prev_ok:
            sleep(5)
        prev_ok = ok


main()
