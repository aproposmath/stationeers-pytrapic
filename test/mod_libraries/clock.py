from stationeers_pytrapic.symbols import *

# Calculate Seconds from midnight using the sun angles
# assumes a DaylightSensor at d0
# the time is stored in db.Setting
# stack[510] is 1 if sun is above horizon (day), otherwise 0 (night)
# stack[511] is the time in seconds until sunset/sunrise
sensor = DaylightSensor(d0)

SECONDS_CALIBRATE = (
    5  # seconds between measurements, increase for more accuracy on first day
)
MINUTES_PER_DAY = 20  # thats a hard-coded value in Stationeers
SECONDS_PER_DAY = MINUTES_PER_DAY * 60
DT = tau / SECONDS_PER_DAY * SECONDS_CALIBRATE

angle_min = 0
angle_max = 0
last_angle = 0
last_sign = 0


def handle_minmax(vertical):
    global last_angle, angle_min, angle_max, last_sign
    # Compare current vertical with the last one,
    # if the sign of 'last_vertical - vertical' changes
    # store last_vertical as new extreme value
    last_vertical = last_angle
    if last_vertical != 0:
        if last_sign == 0:
            sign = vertical - last_vertical

        sign = vertical - last_vertical
        product = sign * last_sign
        if product < 0:
            # sign changed, store last_vertical as new extreme
            if last_sign > 0:
                angle_max = last_vertical
            else:
                angle_min = last_vertical
            last_sign = sign
    last_vertical = vertical


def calc_time(vertical):
    smax = 0.5 * angle_max
    smin = 0.5 * angle_min
    a = smax + smin
    b = smax - smin

    time = (vertical - a) / b
    time = max(time, -1)
    time = min(time, 1)
    time = acos(time) / tau
    if last_sign > 0:
        time = 1 - time

    # add half a day, then convert to seconds
    time = ((time + 0.5) % 1) * SECONDS_PER_DAY
    return time


def get_vertical():
    # return altitude of sun, 0 at horizont, in radians
    vertical = (90 - sensor.Vertical) * (pi / 180)
    return sin(vertical)


def init():
    global angle_min, angle_max, last_sign, last_angle
    clr(db)
    deriv1 = 0
    deriv2 = 0

    v = get_vertical()
    deriv1 -= v
    deriv2 += v
    sleep(SECONDS_CALIBRATE)

    v = get_vertical()
    last_angle = v
    deriv0 = v
    deriv2 -= 2 * v
    sleep(SECONDS_CALIBRATE)

    v = get_vertical()
    deriv1 += v
    deriv2 += v

    deriv1 *= 0.5 / DT
    deriv2 *= 1.0 / (DT * DT)

    last_sign = deriv1
    b = deriv0 + deriv2
    deriv0 -= b
    a = sqrt(deriv0 * deriv0 + deriv1 * deriv1)

    angle_min = b - a
    angle_max = b + a


def calc_time_to_sunset(time):
    time_sunset = calc_time(0)
    if time_sunset < 0:
        time_sunset = SECONDS_PER_DAY - time_sunset
    time_sunset = (time_sunset - time + SECONDS_PER_DAY) % SECONDS_PER_DAY
    return time_sunset


def update():
    push(ra)
    vertical = get_vertical()
    handle_minmax(vertical)
    time = calc_time(vertical)
    db.Setting = time
    stack[510] = vertical > 0
    stack[511] = calc_time_to_sunset(time)
    ra = pop()
    return time


def is_day():
    return stack[510]


def get_time():
    return db.Setting


def get_time_to_sunset():
    return stack[511]


if __name__ == "__main__":
    init()
    while True:
        update()
        yield_()
