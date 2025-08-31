from stationeers_pytrapic.symbols import *

# Calculate Seconds from midnight using the sun angles
# assumes a DaylightSensor at d0
# the time is stored in db.Setting
sensor = DaylightSensor(d0)

# min max values can be 0 at start,
# wait for one in-game day to have them updated

# stack offsets
ITIME = 0
ISUNSET = 1
IMIN = 2
IMAX = 3
IVERT = 4
ISIGN = 5

SECONDS_PER_DAY = 20 * 60
TSLEEP = 5
DT = 2 * 3.14159261 / (20 * 60) * 5

display_time = ConsoleLED5s["Time"]
display_time.On = True
display_time.Setting = 0
display_time.Mode = 7
display_sunset = ConsoleLED5s["Sunset"]
display_sunset.On = True
display_sunset.Setting = 0
display_sunset.Mode = 7


def handle_minmax(vertical):
    # Compare current vertical with the last one,
    # if the sign of 'last_vertical - vertical' changes
    # store last_vertical as new extreme value
    last_vertical = stack[IVERT]
    if last_vertical != 0:
        last_sign = stack[ISIGN]
        if last_sign == 0:
            stack[ISIGN] = vertical - last_vertical

        sign = vertical - last_vertical
        product = sign * last_sign
        if product < 0:
            # sign changed, store last_vertical as new extreme
            addr = IMAX if last_sign > 0 else IMIN
            stack[addr] = last_vertical
            stack[ISIGN] = sign
    stack[IVERT] = vertical


def calc_time(vertical):
    smax = stack[IMAX]
    sin(smax, smax)
    smax *= 0.5
    smin = stack[IMIN]
    sin(smin, smin)
    smin *= 0.5
    a = smax + smin
    b = smax - smin

    time = vertical
    sin(time, time)
    time -= a
    time /= b
    max(time, time, -1)
    min(time, time, 1)
    acos(time, time)
    time = time / (2 * 3.141592)
    if stack[ISIGN] > 0:
        time = 1 - time
    # time is now 0...1 but 0 at noon
    time += 0.5
    time %= 1  # time is now 0...1 but 0 at midnight
    time *= SECONDS_PER_DAY  # seconds from midnight
    return time


def get_vertical():
    # return altitude of sun, 0 at horizont, in radians
    vertical = sensor.Vertical
    vertical = 90 - vertical
    vertical /= 180
    vertical *= 3.141592
    return vertical


def init():
    clr(db)
    i = 0
    deriv0 = 0
    deriv1 = 0
    deriv2 = 0
    while i < 3:
        v = get_vertical()
        stack[IVERT] = v
        sin(v, v)
        if i == 0:
            deriv1 -= v
            deriv2 += v
            sleep(TSLEEP)
        if i == 1:
            deriv0 = v
            v *= 2
            deriv2 -= v
            sleep(TSLEEP)
        if i == 2:
            deriv1 += v
            deriv2 += v
        i += 1

    deriv1 *= 0.5
    deriv1 /= DT
    deriv2 /= DT
    deriv2 /= DT

    stack[ISIGN] = deriv1

    b = deriv0 + deriv2

    deriv0 -= b
    deriv0 *= deriv0
    deriv1 *= deriv1
    a = deriv0 + deriv1
    sqrt(a, a)

    v = b - a
    asin(v, v)
    stack[IMIN] = v

    v = b + a
    asin(v, v)
    stack[IMAX] = v


init()

while True:
    yield_()
    vertical = get_vertical()
    handle_minmax(vertical)
    time = calc_time(vertical)
    display_time.Setting = time
    db.Setting = time
    stack[ITIME] = time

    time_sunset = calc_time(0)
    if time_sunset < time:
        time_sunset = SECONDS_PER_DAY - time_sunset
    time_to_sunset = time_sunset - time
    time_to_sunset += SECONDS_PER_DAY
    time_to_sunset %= SECONDS_PER_DAY
    display_sunset.Setting = time_to_sunset
    stack[ISUNSET] = time_to_sunset
