from stationeers_pytrapic.symbols import *

# assign boolean value directly from comparison
GrowLights.On = DaylightSensor(d0).Vertical > 90

# if-else expression will use "select" IC10 instruction
db.Setting = STR("Day") if DaylightSensor(d0).Vertical < 90 else STR("Night")
