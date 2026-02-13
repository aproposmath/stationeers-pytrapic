from stationeers_pytrapic.symbols import *

# Batch operations

# Use the plural name (append "s") to do batch operations
GrowLights.On = True

# Use bracket operator for named batch instructions
GrowLights["Potatos"].On = True

# Access batch properties, either first by batch mode, or by property name
charge0 = Batteries.Average.Charge
charge1 = Batteries.Charge.Average

# having batch mode first is useful if you access the same type multiple times
batteries_bank1 = Batteries["Bank1"].Average

if batteries_bank1.Charge < 0.2:
    SolidFuelGenerators.On = True
    # wait until charge is above 30%
    while batteries_bank1.Charge < 0.3:
        pass
    SolidFuelGenerators.On = False
