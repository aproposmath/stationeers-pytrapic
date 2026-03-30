from stationeers_pytrapic.symbols import *


def hi():
    display = ConsoleLED1x2(d0)
    display.Mode = DisplayMode.String
    display.Setting = STR("Hi")


while True:
    hi()
