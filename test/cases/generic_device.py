from stationeers_pytrapic.symbols import *

dev = _Devices('ModularDeviceSquareButton', 'name')
db.Setting = dev.Maximum.Temperature
dev.Setting = 123
db.Setting = dev.Temperature.Maximum
