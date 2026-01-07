from stationeers_pytrapic.symbols import *

CondensationChambers[123].On = (
    GasSensors.Temperature.Average > 100
    and GasSensors.Temperature.Average < 200
    and GasSensors.Pressure.Average > 150
    and GasSensors.Pressure.Average < 250
    or GasSensors.Pressure.Average < 270
)
