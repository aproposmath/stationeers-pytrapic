from stationeers_pytrapic.symbols import *

db.Setting = 0.5
db.Setting = 1.0 * 3.0
db.Setting = 1.0 * 3.0 + 2.0
db.Setting = ((1.0 * 3.0 + 2.0) / 5.0) % 8324.92
db.Setting = 0.5**3

A = 50
B = 20

db.Setting = A * B
db.Setting = A * B / 1000


MINUTES_PER_DAY = 20  # thats a hard-coded value in Stationeers
C = A * B
D = tau / C * pi

db.Setting = D
