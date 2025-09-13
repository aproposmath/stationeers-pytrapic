from stationeers_pytrapic.symbols import *

# Calculate Seconds from midnight using the sun angles
# assumes a DaylightSensor at d0
# the time is stored in db.Setting
sensor = DaylightSensor(d0)

# min max values can be 0 at start,
# wait for one in-game day to have them updated

# stack offsets
ITIME = 500
ISUNSET = 501
IMIN = 502
IMAX = 503
IVERT = 504
ISIGN = 505

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
    smax *= 0.5
    smin = stack[IMIN]
    smin *= 0.5
    a = smax + smin
    b = smax - smin

    time = vertical
    time -= a
    time /= b
    time = max(time, -1)
    time = min(time, 1)
    time = acos(time)
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
    vertical = sin(vertical)
    return vertical


def init():
    clr(db)
    push(ra)
    deriv0 = 0
    deriv1 = 0
    deriv2 = 0

    v = get_vertical()
    deriv1 -= v
    deriv2 += v
    sleep(TSLEEP)

    v = get_vertical()
    stack[IVERT] = v
    deriv0 = v
    v *= 2
    deriv2 -= v
    sleep(TSLEEP)

    v = get_vertical()
    deriv1 += v
    deriv2 += v

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
    a = sqrt(a)

    v = b - a
    stack[IMIN] = v

    v = b + a
    stack[IMAX] = v
    ra = pop()


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
