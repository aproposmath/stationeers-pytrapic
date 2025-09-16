from stationeers_pytrapic.symbols import *
from library import clock

clock.init()
display_time = ConsoleLED5s["Time"]
display_time.On = True
display_time.Setting = 0
display_time.Mode = 7
display_sunset = ConsoleLED5s["Sunset"]
display_sunset.On = True
display_sunset.Setting = 0
display_sunset.Mode = 7
lights = LightLongs

while True:
    yield_()
    time = clock.update()
    display_time.Setting = time
    display_sunset.Setting = clock.get_time_to_sunset()
    lights.On = not clock.is_day()
