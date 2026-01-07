from stationeers_pytrapic.symbols import *

prefix = define("PREFIX", 'HASH("Some name prefix ")')


# Computes CRC32 hash of "SOME NAME PREFIX " + some number
def hash_number(crc, n):
    # signed -> unsigned hash
    if crc < 0:
        crc += 2**32

    crc = crc ^ 0xFFFFFFFF

    n_digits = 1
    factor = 1
    while 10 * factor <= n:
        n_digits += 1
        factor *= 10

    while n_digits > 0:
        n_digits -= 1
        digit = floor(n / factor)
        n -= digit * factor
        factor /= 10

        # convert digit to ASCII
        digit += 48

        digit = digit & 0xFF
        crc = crc ^ digit
        i = 0
        while i < 8:
            i += 1
            uneven = crc % 2
            crc >>= 1
            if uneven == 1:
                crc = crc ^ 0xEDB88320

    crc = crc ^ 0xFFFFFFFF

    # unsigned -> signed hash
    if crc >= 2**31:
        crc -= 2**32

    return crc


while True:
    i = 0
    while i < 150:
        hash_value = hash_number(prefix, i)
        # access ConsoleLED5s with name hash
        ConsoleLED5s[hash_value].On = 1
        i += 1
