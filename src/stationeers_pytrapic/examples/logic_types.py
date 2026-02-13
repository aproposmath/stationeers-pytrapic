from stationeers_pytrapic.symbols import *

# Simple access to logic types

# access devices by their symbolic names (d0-d5, db)
db.Setting = d0.RatioCarbonDioxide

# simple calculations will get optimized away
d1.Setting = 273.15 + 22

# use structure names to get proper autocompletion
sensor = DaylightSensor(d5)
db.Setting = sensor.Horizontal
