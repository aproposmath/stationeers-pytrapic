from stationeers_pytrapic.symbols import *

panel0 = SolarPanel(d0)
panel1 = SolarPanel(d1, alias=True)
panel2 = SolarPanel(d2, alias="SOLAR_PANEL_2")

panel0.Horizontal = 1
panel1.Horizontal = 2
panel2.Horizontal = 3
