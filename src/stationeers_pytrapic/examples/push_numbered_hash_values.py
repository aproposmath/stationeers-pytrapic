from stationeers_pytrapic.symbols import *

prefix = define("PREFIX", 'HASH("Some name prefix ")')
first_number = define("FIRST_NUMBER", 0)
last_number = define("LAST_NUMBER", 42)
I = 512-16

def init_lut():
    # 4-bit lookup table for CRC32 calculation
    stack[I+0] = 0x00000000
    stack[I+1] = 0x1DB71064
    stack[I+2] = 0x3B6E20C8
    stack[I+3] = 0x26D930AC
    stack[I+4] = 0x76DC4190
    stack[I+5] = 0x6B6B51F4
    stack[I+6] = 0x4DB26158
    stack[I+7] = 0x5005713C
    stack[I+8] = 0xEDB88320
    stack[I+9] = 0xF00F9344
    stack[I+10]= 0xD6D6A3E8
    stack[I+11]= 0xCB61B38C
    stack[I+12]= 0x9B64C2B0
    stack[I+13]= 0x86D3D2D4
    stack[I+14]= 0xA00AE278
    stack[I+15]= 0xBDBDF21C


def hash_number_fast_nibble(crc, n):
    """ use 4-bit nibble lookup table """
    # signed -> unsigned hash

    if crc < 0:
        crc += 2**32

    crc = crc ^ 0xFFFFFFFF

    n_digits = 1
    factor = 1
    while 10*factor <= n:
        n_digits += 1
        factor *= 10

    while n_digits > 0:
        n_digits -= 1
        digit = floor(n/factor)
        n -= digit*factor
        factor /=10

        # convert digit to ASCII
        digit += 48

        #digit = digit & 0xFF
        crc = crc ^ digit

        # use 4-bit nibble lookup table
        # process low nibble
        pos = I + (crc & 0x0F)
        crc = stack[pos] ^ (crc >> 4)
        # process high nibble
        pos = I + (crc & 0x0F)
        crc = stack[pos] ^ (crc >> 4)

    crc = crc ^ 0xFFFFFFFF

    # unsigned -> signed hash
    if crc >= 2**31:
        crc -= 2**32

    return crc

db.Mode = 6
db.Setting = STR("CALC..")
init_lut()

i = first_number
while i <= last_number:
  push(hash_number_fast_nibble(prefix, i))
  i+=1

db.Setting = STR("DONE")

while False:
  # Code for checking results: create a small LED display with name 
  # "Some name prefix n", then the number n should appear on the display
  i = 0
  while i <= last_number:
    h = stack[i]
    ConsoleLED5s[h].Setting = i
    i+=1
