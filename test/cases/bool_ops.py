from stationeers_pytrapic.symbols import *

while True:

    charge = Batteries.Ratio.Average
    is_storm_incoming = WeatherStations.NextWeatherEventTime.Average < 1

    soon_loading = charge < 0.2 and is_storm_incoming

    need_to_load = not soon_loading

    if soon_loading:
        db.Setting = 2

    if need_to_load:
        db.Setting = -charge
