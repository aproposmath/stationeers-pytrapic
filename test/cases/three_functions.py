from stationeers_pytrapic.symbols import *

# Airlock control script for Stationeers PyTrapIC
# All devices are accessed through their names
# Vent and GlassDoor are either named "In" or "Out" as name
# Switch is a DiodeSlide named "Switch"

# Using a light as a switch is better, as a button press cannot be "missed"
# in more complex codes. Also it provies feedback to the player.

door_in = GlassDoors["In"]
door_out = GlassDoors["In"]
vent_in = ActiveVents["In"]
vent_out = ActiveVents["In"]

door_in.Lock = True
door_out.Lock = True
vent_in.Mode = True
vent_in.On = False
vent_out.Mode = True
vent_out.On = False
ArcFurnaces.On = True

switch = LightLongWides["Switch"]
gas_airlock = GasSensors["Airlock"]
gas_greenhouse = GasSensors["Greenhouse"]


def handle_airlock():
    if switch.On.Maximum > 0:
        going_out = GlassDoors["In"].Open.Maximum > 0
        dir_to = HASH("Out") if going_out else HASH("In")
        dir_from = HASH("In") if going_out else HASH("Out")
        GlassDoors[dir_from].Open = False
        ActiveVents[dir_from].On = True

        while gas_airlock.Pressure.Maximum != 0:
            pass
        sleep(0.2)

        ActiveVents[dir_from].On = False
        GlassDoors[dir_to].Open = True
        switch.On = False
        sleep(1)


def handle_heating():
    charge = Batterys.Ratio.Average
    temp = gas_greenhouse.Temperature.Average
    WallHeaters.On = charge > 0.1 and temp < 273.15 + 20
    db.Setting = charge


def handle_furnace():
    sensor = GasSensors["Furnace"]
    vent = ActiveVents["Furnace"]
    vent.Mode = True
    temp = sensor.Temperature.Average
    pressure = sensor.Pressure.Average
    if sensor.RatioOxygen.Average > 0.95 and pressure > 0:
        vent.On = True
        ArcFurnaces.On = False
    else:
        vent.On = False
        ArcFurnaces.On = True
        ArcFurnaces.Activate = True
    cooler = WallCoolers["Furnace"]
    cooler.On = temp > 150


while True:
    handle_airlock()
    handle_heating()
    handle_furnace()
