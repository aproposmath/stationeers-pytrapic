from stationeers_pytrapic.symbols import *

# Calculate Seconds from midnight using the sun angles
# assumes a DaylightSensor at d0
sensor = DaylightSensor(d0)

# min max values can be 0 at start,
# wait for one in-game day to have them updated

max_vertical = 0 #0.9019 for Mars
min_vertical = 0 #-1.3245 for Mars
last_vertical = 0
last_sign = 0


def handle_minmax(vertical):
  # Compare current vertical with the last one,
  # if the sign of 'last_vertical - vertical' changes
  # store last_vertical as new extreme value
  global min_vertical, max_vertical, last_sign, last_vertical
  if last_vertical == 0:
    last_vertical = vertical
    return
  if last_sign == 0:
    last_sign = vertical-last_vertical
  sign = vertical - last_vertical
  sign *= last_sign
  if sign < 0:
    if last_sign > 0:
      max_vertical = last_vertical
    else:
      min_vertical = last_vertical
    last_sign *= -1.0
  last_vertical = vertical
  #ConsoleLED5s['min_vert'].Setting = min_vertical
  #ConsoleLED5s['max_vert'].Setting = max_vertical

def calc_time(vertical):
  # Calculate
  smax = max_vertical
  sin(smax, smax)
  smax *= 0.5
  smin = min_vertical
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
  acos(time,time)
  time = time / (2 * 3.141592)
  if last_sign > 0:
    time = 1-time
  # c is now 0...1 but 0 at noon
  time += 0.5
  time %= 1
  # c is now 0...1 but 0 at midnight
  time *= 20 * 60 # seconds from midnight

  return time

def get_vertical():
  # return altitude of sun, 0 at horizont, in radians
  vertical = sensor.Vertical
  vertical = 90 - vertical
  vertical /= 180
  vertical *= 3.141592
  return vertical

while True:
  yield_()
  vertical = get_vertical()

  handle_minmax(vertical)
  time = calc_time(vertical)
  db.Setting = time

  display = ConsoleLED5s
  display['time'].Setting = time
  display['min_vert'].Setting = min_vertical
  display['max_vert'].Setting = max_vertical

