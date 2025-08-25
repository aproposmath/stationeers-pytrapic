from stationeers_pytrapic.symbols import *

display = ConsoleLED1x3s
display.Mode = 10


def append_number(num_string, n):
    if n == 0:
        return 256 * num_string + 48
    d = 1
    while d <= n / 10:
        d *= 10
    db.Setting = d
    while d >= 1:
        round(d, d)
        digit = n / d
        trunc(digit, digit)
        num_string *= 256
        num_string += digit
        num_string += 48
        n -= digit * d
        d = d / 10
    return num_string


num0 = 55
num1 = 999

while True:
    yield_()
    num_string = 0
    num_string = append_number(num_string, num0)
    num_string *= 256
    num_string += 47  # ASCII for '/'
    num_string = append_number(num_string, num1)
    display.Setting = num_string

    num0 += 1
    num1 -= 1
