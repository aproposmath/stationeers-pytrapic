from stationeers_pytrapic.symbols import *

furnace = AdvancedFurnace(d0)

def main():
    HeatCap = furnace.RatioCarbonDioxide * 28.2
    HeatCap += furnace.RatioNitrogen * 28.2
    HeatCap += furnace.RatioNitrousOxide * 28.2
    HeatCap += furnace.RatioPollutant * 28.2
    HeatCap += furnace.RatioOxygen * 28.2
    HeatCap += furnace.RatioVolatiles * 28.2
    HeatCap *= furnace.TotalMoles

    return HeatCap

temp = main()
