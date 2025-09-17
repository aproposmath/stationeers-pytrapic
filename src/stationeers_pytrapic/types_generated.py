from enum import IntEnum as _IntEnum


class LogicType(_IntEnum):
    None_ = 0
    Power = 1
    Open = 2
    Mode = 3
    Error = 4
    Pressure = 5
    Temperature = 6
    PressureExternal = 7
    PressureInternal = 8
    Activate = 9
    Lock = 10
    Charge = 11
    Setting = 12
    Reagents = 13
    RatioOxygen = 14
    RatioCarbonDioxide = 15
    RatioNitrogen = 16
    RatioPollutant = 17
    RatioVolatiles = 18
    RatioWater = 19
    Horizontal = 20
    Vertical = 21
    SolarAngle = 22
    Maximum = 23
    Ratio = 24
    PowerPotential = 25
    PowerActual = 26
    Quantity = 27
    On = 28
    ImportQuantity = 29
    ImportSlotOccupant = 30
    ExportQuantity = 31
    ExportSlotOccupant = 32
    RequiredPower = 33
    HorizontalRatio = 34
    VerticalRatio = 35
    PowerRequired = 36
    Idle = 37
    Color = 38
    ElevatorSpeed = 39
    ElevatorLevel = 40
    RecipeHash = 41
    ExportSlotHash = 42
    ImportSlotHash = 43
    PlantHealth1 = 44
    PlantHealth2 = 45
    PlantHealth3 = 46
    PlantHealth4 = 47
    PlantGrowth1 = 48
    PlantGrowth2 = 49
    PlantGrowth3 = 50
    PlantGrowth4 = 51
    PlantEfficiency1 = 52
    PlantEfficiency2 = 53
    PlantEfficiency3 = 54
    PlantEfficiency4 = 55
    PlantHash1 = 56
    PlantHash2 = 57
    PlantHash3 = 58
    PlantHash4 = 59
    RequestHash = 60
    CompletionRatio = 61
    ClearMemory = 62
    ExportCount = 63
    ImportCount = 64
    PowerGeneration = 65
    TotalMoles = 66
    Volume = 67
    Plant = 68
    Harvest = 69
    Output = 70
    PressureSetting = 71
    TemperatureSetting = 72
    TemperatureExternal = 73
    Filtration = 74
    AirRelease = 75
    PositionX = 76
    PositionY = 77
    PositionZ = 78
    VelocityMagnitude = 79
    VelocityRelativeX = 80
    VelocityRelativeY = 81
    VelocityRelativeZ = 82
    RatioNitrousOxide = 83
    PrefabHash = 84
    ForceWrite = 85
    SignalStrength = 86
    SignalID = 87
    TargetX = 88
    TargetY = 89
    TargetZ = 90
    SettingInput = 91
    SettingOutput = 92
    CurrentResearchPodType = 93
    ManualResearchRequiredPod = 94
    MineablesInVicinity = 95
    MineablesInQueue = 96
    NextWeatherEventTime = 97
    Combustion = 98
    Fuel = 99
    ReturnFuelCost = 100
    CollectableGoods = 101
    Time = 102
    Bpm = 103
    EnvironmentEfficiency = 104
    WorkingGasEfficiency = 105
    PressureInput = 106
    TemperatureInput = 107
    RatioOxygenInput = 108
    RatioCarbonDioxideInput = 109
    RatioNitrogenInput = 110
    RatioPollutantInput = 111
    RatioVolatilesInput = 112
    RatioWaterInput = 113
    RatioNitrousOxideInput = 114
    TotalMolesInput = 115
    PressureInput2 = 116
    TemperatureInput2 = 117
    RatioOxygenInput2 = 118
    RatioCarbonDioxideInput2 = 119
    RatioNitrogenInput2 = 120
    RatioPollutantInput2 = 121
    RatioVolatilesInput2 = 122
    RatioWaterInput2 = 123
    RatioNitrousOxideInput2 = 124
    TotalMolesInput2 = 125
    PressureOutput = 126
    TemperatureOutput = 127
    RatioOxygenOutput = 128
    RatioCarbonDioxideOutput = 129
    RatioNitrogenOutput = 130
    RatioPollutantOutput = 131
    RatioVolatilesOutput = 132
    RatioWaterOutput = 133
    RatioNitrousOxideOutput = 134
    TotalMolesOutput = 135
    PressureOutput2 = 136
    TemperatureOutput2 = 137
    RatioOxygenOutput2 = 138
    RatioCarbonDioxideOutput2 = 139
    RatioNitrogenOutput2 = 140
    RatioPollutantOutput2 = 141
    RatioVolatilesOutput2 = 142
    RatioWaterOutput2 = 143
    RatioNitrousOxideOutput2 = 144
    TotalMolesOutput2 = 145
    CombustionInput = 146
    CombustionInput2 = 147
    CombustionOutput = 148
    CombustionOutput2 = 149
    OperationalTemperatureEfficiency = 150
    TemperatureDifferentialEfficiency = 151
    PressureEfficiency = 152
    CombustionLimiter = 153
    Throttle = 154
    Rpm = 155
    Stress = 156
    InterrogationProgress = 157
    TargetPadIndex = 158
    SizeX = 160
    SizeY = 161
    SizeZ = 162
    MinimumWattsToContact = 163
    WattsReachingContact = 164
    Channel0 = 165
    Channel1 = 166
    Channel2 = 167
    Channel3 = 168
    Channel4 = 169
    Channel5 = 170
    Channel6 = 171
    Channel7 = 172
    LineNumber = 173
    Flush = 174
    SoundAlert = 175
    SolarIrradiance = 176
    RatioLiquidNitrogen = 177
    RatioLiquidNitrogenInput = 178
    RatioLiquidNitrogenInput2 = 179
    RatioLiquidNitrogenOutput = 180
    RatioLiquidNitrogenOutput2 = 181
    VolumeOfLiquid = 182
    RatioLiquidOxygen = 183
    RatioLiquidOxygenInput = 184
    RatioLiquidOxygenInput2 = 185
    RatioLiquidOxygenOutput = 186
    RatioLiquidOxygenOutput2 = 187
    RatioLiquidVolatiles = 188
    RatioLiquidVolatilesInput = 189
    RatioLiquidVolatilesInput2 = 190
    RatioLiquidVolatilesOutput = 191
    RatioLiquidVolatilesOutput2 = 192
    RatioSteam = 193
    RatioSteamInput = 194
    RatioSteamInput2 = 195
    RatioSteamOutput = 196
    RatioSteamOutput2 = 197
    ContactTypeId = 198
    RatioLiquidCarbonDioxide = 199
    RatioLiquidCarbonDioxideInput = 200
    RatioLiquidCarbonDioxideInput2 = 201
    RatioLiquidCarbonDioxideOutput = 202
    RatioLiquidCarbonDioxideOutput2 = 203
    RatioLiquidPollutant = 204
    RatioLiquidPollutantInput = 205
    RatioLiquidPollutantInput2 = 206
    RatioLiquidPollutantOutput = 207
    RatioLiquidPollutantOutput2 = 208
    RatioLiquidNitrousOxide = 209
    RatioLiquidNitrousOxideInput = 210
    RatioLiquidNitrousOxideInput2 = 211
    RatioLiquidNitrousOxideOutput = 212
    RatioLiquidNitrousOxideOutput2 = 213
    Progress = 214
    DestinationCode = 215
    Acceleration = 216
    ReferenceId = 217
    AutoShutOff = 218
    Mass = 219
    DryMass = 220
    Thrust = 221
    Weight = 222
    ThrustToWeight = 223
    TimeToDestination = 224
    BurnTimeRemaining = 225
    AutoLand = 226
    ForwardX = 227
    ForwardY = 228
    ForwardZ = 229
    Orientation = 230
    VelocityX = 231
    VelocityY = 232
    VelocityZ = 233
    PassedMoles = 234
    ExhaustVelocity = 235
    FlightControlRule = 236
    ReEntryAltitude = 237
    Apex = 238
    EntityState = 239
    DrillCondition = 240
    Index = 241
    CelestialHash = 242
    AlignmentError = 243
    DistanceAu = 244
    OrbitPeriod = 245
    Inclination = 246
    Eccentricity = 247
    SemiMajorAxis = 248
    DistanceKm = 249
    CelestialParentHash = 250
    TrueAnomaly = 251
    RatioHydrogen = 252
    RatioLiquidHydrogen = 253
    RatioPollutedWater = 254
    Discover = 255
    Chart = 256
    Survey = 257
    NavPoints = 258
    ChartedNavPoints = 259
    Sites = 260
    CurrentCode = 261
    Density = 262
    Richness = 263
    Size = 264
    TotalQuantity = 265
    MinedQuantity = 266
    BestContactFilter = 267
    NameHash = 268
    Altitude = 269
    TargetSlotIndex = 270
    TargetPrefabHash = 271
    Extended = 272
    NetworkFault = 273
    ProportionalGain = 274
    IntegralGain = 275
    DerivativeGain = 276
    Minimum = 277
    Setpoint = 278
    Reset = 279
    StackSize = 280


class LogicSlotType(_IntEnum):
    None_ = 0
    Occupied = 1
    OccupantHash = 2
    Quantity = 3
    Damage = 4
    Efficiency = 5
    Health = 6
    Growth = 7
    Pressure = 8
    Temperature = 9
    Charge = 10
    ChargeRatio = 11
    Class = 12
    PressureWaste = 13
    PressureAir = 14
    MaxQuantity = 15
    Mature = 16
    PrefabHash = 17
    Seeding = 18
    LineNumber = 19
    Volume = 20
    Open = 21
    On = 22
    Lock = 23
    SortingClass = 24
    FilterType = 25
    ReferenceId = 26
    HarvestedHash = 27
    Mode = 28
    MaturityRatio = 29
    SeedingRatio = 30


class LogicReagentMode(_IntEnum):
    Contents = 0
    Required = 1
    Recipe = 2
    TotalContents = 3


class LogicBatchMethod(_IntEnum):
    Average = 0
    Sum = 1
    Minimum = 2
    Maximum = 3


class SoundAlert(_IntEnum):
    None_ = 0
    Alarm2 = 1
    Alarm3 = 2
    Alarm4 = 3
    Alarm5 = 4
    Alarm6 = 5
    Alarm7 = 6
    Music1 = 7
    Music2 = 8
    Music3 = 9
    Alarm8 = 10
    Alarm9 = 11
    Alarm10 = 12
    Alarm11 = 13
    Alarm12 = 14
    Danger = 15
    Warning = 16
    Alert = 17
    StormIncoming = 18
    IntruderAlert = 19
    Depressurising = 20
    Pressurising = 21
    AirlockCycling = 22
    PowerLow = 23
    SystemFailure = 24
    Welcome = 25
    MalfunctionDetected = 26
    HaltWhoGoesThere = 27
    FireFireFire = 28
    One = 29
    Two = 30
    Three = 31
    Four = 32
    Five = 33
    Floor = 34
    RocketLaunching = 35
    LiftOff = 36
    TraderIncoming = 37
    TraderLanded = 38
    PressureHigh = 39
    PressureLow = 40
    TemperatureHigh = 41
    TemperatureLow = 42
    PollutantsDetected = 43
    HighCarbonDioxide = 44
    Alarm1 = 45


class LogicTransmitterMode(_IntEnum):
    Passive = 0
    Active = 1


class ElevatorMode(_IntEnum):
    Stationary = 0
    Upward = 1
    Downward = 2


class ColorType(_IntEnum):
    Blue = 0
    Gray = 1
    Green = 2
    Orange = 3
    Red = 4
    Yellow = 5
    White = 6
    Black = 7
    Brown = 8
    Khaki = 9
    Pink = 10
    Purple = 11


class EntityState(_IntEnum):
    Alive = 0
    Dead = 1
    Unconscious = 2
    Decay = 3


class AirControlMode(_IntEnum):
    None_ = 0
    Offline = 1
    Pressure = 2
    Draught = 4


class DaylightSensorMode(_IntEnum):
    Default = 0
    Horizontal = 1
    Vertical = 2


class ConditionOperation(_IntEnum):
    Equals = 0
    Greater = 1
    Less = 2
    NotEquals = 3


class AirConditioningMode(_IntEnum):
    Cold = 0
    Hot = 1


class VentDirection(_IntEnum):
    Outward = 0
    Inward = 1


class PowerMode(_IntEnum):
    Idle = 0
    Discharged = 1
    Discharging = 2
    Charging = 3
    Charged = 4


class RobotMode(_IntEnum):
    None_ = 0
    Follow = 1
    MoveToTarget = 2
    Roam = 3
    Unload = 4
    PathToTarget = 5
    StorageFull = 6


class SortingClass(_IntEnum):
    Default = 0
    Kits = 1
    Tools = 2
    Resources = 3
    Food = 4
    Clothing = 5
    Appliances = 6
    Atmospherics = 7
    Storage = 8
    Ores = 9
    Ices = 10


class Class(_IntEnum):
    None_ = 0
    Helmet = 1
    Suit = 2
    Back = 3
    GasFilter = 4
    GasCanister = 5
    Motherboard = 6
    Circuitboard = 7
    DataDisk = 8
    Organ = 9
    Ore = 10
    Plant = 11
    Uniform = 12
    Entity = 13
    Battery = 14
    Egg = 15
    Belt = 16
    Tool = 17
    Appliance = 18
    Ingot = 19
    Torpedo = 20
    Cartridge = 21
    AccessCard = 22
    Magazine = 23
    Circuit = 24
    Bottle = 25
    ProgrammableChip = 26
    Glasses = 27
    CreditCard = 28
    DirtCanister = 29
    SensorProcessingUnit = 30
    LiquidCanister = 31
    LiquidBottle = 32
    Wreckage = 33
    SoundCartridge = 34
    DrillHead = 35
    ScanningHead = 36
    Flare = 37
    Blocked = 38
    SuitMod = 39
    Crate = 40
    Portables = 41
    RocketPayload = 42


class GasType(_IntEnum):
    Undefined = 0
    Oxygen = 1
    Nitrogen = 2
    Air = 3
    CarbonDioxide = 4
    Volatiles = 8
    Fuel = 9
    Pollutant = 16
    Water = 32
    NitrousOxide = 64
    LiquidNitrogen = 128
    LiquidOxygen = 256
    LiquidVolatiles = 512
    Steam = 1024
    LiquidCarbonDioxide = 2048
    LiquidPollutant = 4096
    LiquidNitrousOxide = 8192
    Hydrogen = 16384
    LiquidHydrogen = 32768
    PollutedWater = 65536


class RocketMode(_IntEnum):
    Invalid = 0
    None_ = 1
    Mine = 2
    Survey = 3
    Discover = 4
    Chart = 5
    Deploy = 6


class ReEntryProfile(_IntEnum):
    None_ = 0
    Low = 1
    Medium = 2
    High = 3
    Max = 4


class SorterInstruction(_IntEnum):
    None_ = 0
    FilterPrefabHashEquals = 1
    FilterPrefabHashNotEquals = 2
    FilterSortingClassCompare = 3
    FilterSlotTypeCompare = 4
    FilterQuantityCompare = 5
    LimitNextExecutionByCount = 6


class PrinterInstruction(_IntEnum):
    None_ = 0
    StackPointer = 1
    ExecuteRecipe = 2
    WaitUntilNextValid = 3
    JumpIfNextInvalid = 4
    JumpToAddress = 5
    DeviceSetLock = 6
    EjectReagent = 7
    EjectAllReagents = 8
    MissingRecipeReagent = 9


class TraderInstruction(_IntEnum):
    None_ = 0
    WriteTraderData = 1
    StrongestContactIdHash = 2
    StrongestContactMetaData = 3
    StrongestContactSignalData = 4
    WriteTraderBuyData = 5
    WriteTraderSellData = 6
    TraderBuyThingData = 7
    TraderBuyThingChildData = 8
    TraderBuyGasData = 9
    TraderSellThingData = 10
    TraderSellGasData = 11
    TraderSellThingChildData = 12
    FilterPrefabHashEquals = 13
    FilterPrefabHashNotEquals = 14
    FilterSortingClassCompare = 15
    FilterQuantityCompare = 16
    FilterGasContains = 17
    FilterGasNotContains = 18


class ShuttleType(_IntEnum):
    None_ = 0
    Small = 1
    SmallGas = 2
    Medium = 3
    MediumGas = 4
    Large = 5
    LargeGas = 6
    MediumPlane = 7
    LargePlane = 8


class HashType(_IntEnum):
    Prefab = 0
    GasLiquid = 1


class DisplayMode(_IntEnum):
    Default = 0
    Percent = 1
    Power = 2
    Kelvin = 3
    Celsius = 4
    Meters = 5
    Credits = 6
    Seconds = 7
    Minutes = 8
    Days = 9
    String = 10
    Fahrenheit = 11
    Litres = 12
    Mol = 13
    Pa = 14


class ContactTier(_IntEnum):
    Close = 0
    Medium = 1
    Far = 2


class SettingDisplayMode(_IntEnum):
    Number = 0
    String = 1


class _GenericStructure:

    @property
    def None_(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("None_")

    @None_.setter
    def None_(self, value):
        return self.__setattr__("None_", value)

    @property
    def Power(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Power")

    @Power.setter
    def Power(self, value):
        return self.__setattr__("Power", value)

    @property
    def Open(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Open")

    @Open.setter
    def Open(self, value):
        return self.__setattr__("Open", value)

    @property
    def Mode(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Mode")

    @Mode.setter
    def Mode(self, value):
        return self.__setattr__("Mode", value)

    @property
    def Error(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Error")

    @Error.setter
    def Error(self, value):
        return self.__setattr__("Error", value)

    @property
    def Pressure(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Pressure")

    @Pressure.setter
    def Pressure(self, value):
        return self.__setattr__("Pressure", value)

    @property
    def Temperature(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Temperature")

    @Temperature.setter
    def Temperature(self, value):
        return self.__setattr__("Temperature", value)

    @property
    def PressureExternal(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureExternal")

    @PressureExternal.setter
    def PressureExternal(self, value):
        return self.__setattr__("PressureExternal", value)

    @property
    def PressureInternal(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureInternal")

    @PressureInternal.setter
    def PressureInternal(self, value):
        return self.__setattr__("PressureInternal", value)

    @property
    def Activate(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Activate")

    @Activate.setter
    def Activate(self, value):
        return self.__setattr__("Activate", value)

    @property
    def Lock(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Lock")

    @Lock.setter
    def Lock(self, value):
        return self.__setattr__("Lock", value)

    @property
    def Charge(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Charge")

    @Charge.setter
    def Charge(self, value):
        return self.__setattr__("Charge", value)

    @property
    def Setting(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Setting")

    @Setting.setter
    def Setting(self, value):
        return self.__setattr__("Setting", value)

    @property
    def Reagents(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Reagents")

    @Reagents.setter
    def Reagents(self, value):
        return self.__setattr__("Reagents", value)

    @property
    def RatioOxygen(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioOxygen")

    @RatioOxygen.setter
    def RatioOxygen(self, value):
        return self.__setattr__("RatioOxygen", value)

    @property
    def RatioCarbonDioxide(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioCarbonDioxide")

    @RatioCarbonDioxide.setter
    def RatioCarbonDioxide(self, value):
        return self.__setattr__("RatioCarbonDioxide", value)

    @property
    def RatioNitrogen(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrogen")

    @RatioNitrogen.setter
    def RatioNitrogen(self, value):
        return self.__setattr__("RatioNitrogen", value)

    @property
    def RatioPollutant(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioPollutant")

    @RatioPollutant.setter
    def RatioPollutant(self, value):
        return self.__setattr__("RatioPollutant", value)

    @property
    def RatioVolatiles(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioVolatiles")

    @RatioVolatiles.setter
    def RatioVolatiles(self, value):
        return self.__setattr__("RatioVolatiles", value)

    @property
    def RatioWater(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioWater")

    @RatioWater.setter
    def RatioWater(self, value):
        return self.__setattr__("RatioWater", value)

    @property
    def Horizontal(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Horizontal")

    @Horizontal.setter
    def Horizontal(self, value):
        return self.__setattr__("Horizontal", value)

    @property
    def Vertical(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Vertical")

    @Vertical.setter
    def Vertical(self, value):
        return self.__setattr__("Vertical", value)

    @property
    def SolarAngle(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SolarAngle")

    @SolarAngle.setter
    def SolarAngle(self, value):
        return self.__setattr__("SolarAngle", value)

    @property
    def Maximum(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Maximum")

    @Maximum.setter
    def Maximum(self, value):
        return self.__setattr__("Maximum", value)

    @property
    def Ratio(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Ratio")

    @Ratio.setter
    def Ratio(self, value):
        return self.__setattr__("Ratio", value)

    @property
    def PowerPotential(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PowerPotential")

    @PowerPotential.setter
    def PowerPotential(self, value):
        return self.__setattr__("PowerPotential", value)

    @property
    def PowerActual(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PowerActual")

    @PowerActual.setter
    def PowerActual(self, value):
        return self.__setattr__("PowerActual", value)

    @property
    def Quantity(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Quantity")

    @Quantity.setter
    def Quantity(self, value):
        return self.__setattr__("Quantity", value)

    @property
    def On(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("On")

    @On.setter
    def On(self, value):
        return self.__setattr__("On", value)

    @property
    def ImportQuantity(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ImportQuantity")

    @ImportQuantity.setter
    def ImportQuantity(self, value):
        return self.__setattr__("ImportQuantity", value)

    @property
    def ImportSlotOccupant(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ImportSlotOccupant")

    @ImportSlotOccupant.setter
    def ImportSlotOccupant(self, value):
        return self.__setattr__("ImportSlotOccupant", value)

    @property
    def ExportQuantity(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ExportQuantity")

    @ExportQuantity.setter
    def ExportQuantity(self, value):
        return self.__setattr__("ExportQuantity", value)

    @property
    def ExportSlotOccupant(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ExportSlotOccupant")

    @ExportSlotOccupant.setter
    def ExportSlotOccupant(self, value):
        return self.__setattr__("ExportSlotOccupant", value)

    @property
    def RequiredPower(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RequiredPower")

    @RequiredPower.setter
    def RequiredPower(self, value):
        return self.__setattr__("RequiredPower", value)

    @property
    def HorizontalRatio(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("HorizontalRatio")

    @HorizontalRatio.setter
    def HorizontalRatio(self, value):
        return self.__setattr__("HorizontalRatio", value)

    @property
    def VerticalRatio(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("VerticalRatio")

    @VerticalRatio.setter
    def VerticalRatio(self, value):
        return self.__setattr__("VerticalRatio", value)

    @property
    def PowerRequired(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PowerRequired")

    @PowerRequired.setter
    def PowerRequired(self, value):
        return self.__setattr__("PowerRequired", value)

    @property
    def Idle(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Idle")

    @Idle.setter
    def Idle(self, value):
        return self.__setattr__("Idle", value)

    @property
    def Color(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Color")

    @Color.setter
    def Color(self, value):
        return self.__setattr__("Color", value)

    @property
    def ElevatorSpeed(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ElevatorSpeed")

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value):
        return self.__setattr__("ElevatorSpeed", value)

    @property
    def ElevatorLevel(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ElevatorLevel")

    @ElevatorLevel.setter
    def ElevatorLevel(self, value):
        return self.__setattr__("ElevatorLevel", value)

    @property
    def RecipeHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RecipeHash")

    @RecipeHash.setter
    def RecipeHash(self, value):
        return self.__setattr__("RecipeHash", value)

    @property
    def ExportSlotHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ExportSlotHash")

    @ExportSlotHash.setter
    def ExportSlotHash(self, value):
        return self.__setattr__("ExportSlotHash", value)

    @property
    def ImportSlotHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ImportSlotHash")

    @ImportSlotHash.setter
    def ImportSlotHash(self, value):
        return self.__setattr__("ImportSlotHash", value)

    @property
    def PlantHealth1(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHealth1")

    @PlantHealth1.setter
    def PlantHealth1(self, value):
        return self.__setattr__("PlantHealth1", value)

    @property
    def PlantHealth2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHealth2")

    @PlantHealth2.setter
    def PlantHealth2(self, value):
        return self.__setattr__("PlantHealth2", value)

    @property
    def PlantHealth3(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHealth3")

    @PlantHealth3.setter
    def PlantHealth3(self, value):
        return self.__setattr__("PlantHealth3", value)

    @property
    def PlantHealth4(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHealth4")

    @PlantHealth4.setter
    def PlantHealth4(self, value):
        return self.__setattr__("PlantHealth4", value)

    @property
    def PlantGrowth1(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantGrowth1")

    @PlantGrowth1.setter
    def PlantGrowth1(self, value):
        return self.__setattr__("PlantGrowth1", value)

    @property
    def PlantGrowth2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantGrowth2")

    @PlantGrowth2.setter
    def PlantGrowth2(self, value):
        return self.__setattr__("PlantGrowth2", value)

    @property
    def PlantGrowth3(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantGrowth3")

    @PlantGrowth3.setter
    def PlantGrowth3(self, value):
        return self.__setattr__("PlantGrowth3", value)

    @property
    def PlantGrowth4(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantGrowth4")

    @PlantGrowth4.setter
    def PlantGrowth4(self, value):
        return self.__setattr__("PlantGrowth4", value)

    @property
    def PlantEfficiency1(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantEfficiency1")

    @PlantEfficiency1.setter
    def PlantEfficiency1(self, value):
        return self.__setattr__("PlantEfficiency1", value)

    @property
    def PlantEfficiency2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantEfficiency2")

    @PlantEfficiency2.setter
    def PlantEfficiency2(self, value):
        return self.__setattr__("PlantEfficiency2", value)

    @property
    def PlantEfficiency3(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantEfficiency3")

    @PlantEfficiency3.setter
    def PlantEfficiency3(self, value):
        return self.__setattr__("PlantEfficiency3", value)

    @property
    def PlantEfficiency4(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantEfficiency4")

    @PlantEfficiency4.setter
    def PlantEfficiency4(self, value):
        return self.__setattr__("PlantEfficiency4", value)

    @property
    def PlantHash1(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHash1")

    @PlantHash1.setter
    def PlantHash1(self, value):
        return self.__setattr__("PlantHash1", value)

    @property
    def PlantHash2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHash2")

    @PlantHash2.setter
    def PlantHash2(self, value):
        return self.__setattr__("PlantHash2", value)

    @property
    def PlantHash3(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHash3")

    @PlantHash3.setter
    def PlantHash3(self, value):
        return self.__setattr__("PlantHash3", value)

    @property
    def PlantHash4(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHash4")

    @PlantHash4.setter
    def PlantHash4(self, value):
        return self.__setattr__("PlantHash4", value)

    @property
    def RequestHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RequestHash")

    @RequestHash.setter
    def RequestHash(self, value):
        return self.__setattr__("RequestHash", value)

    @property
    def CompletionRatio(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CompletionRatio")

    @CompletionRatio.setter
    def CompletionRatio(self, value):
        return self.__setattr__("CompletionRatio", value)

    @property
    def ClearMemory(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ClearMemory")

    @ClearMemory.setter
    def ClearMemory(self, value):
        return self.__setattr__("ClearMemory", value)

    @property
    def ExportCount(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ExportCount")

    @ExportCount.setter
    def ExportCount(self, value):
        return self.__setattr__("ExportCount", value)

    @property
    def ImportCount(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ImportCount")

    @ImportCount.setter
    def ImportCount(self, value):
        return self.__setattr__("ImportCount", value)

    @property
    def PowerGeneration(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PowerGeneration")

    @PowerGeneration.setter
    def PowerGeneration(self, value):
        return self.__setattr__("PowerGeneration", value)

    @property
    def TotalMoles(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TotalMoles")

    @TotalMoles.setter
    def TotalMoles(self, value):
        return self.__setattr__("TotalMoles", value)

    @property
    def Volume(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Volume")

    @Volume.setter
    def Volume(self, value):
        return self.__setattr__("Volume", value)

    @property
    def Plant(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Plant")

    @Plant.setter
    def Plant(self, value):
        return self.__setattr__("Plant", value)

    @property
    def Harvest(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Harvest")

    @Harvest.setter
    def Harvest(self, value):
        return self.__setattr__("Harvest", value)

    @property
    def Output(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Output")

    @Output.setter
    def Output(self, value):
        return self.__setattr__("Output", value)

    @property
    def PressureSetting(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureSetting")

    @PressureSetting.setter
    def PressureSetting(self, value):
        return self.__setattr__("PressureSetting", value)

    @property
    def TemperatureSetting(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TemperatureSetting")

    @TemperatureSetting.setter
    def TemperatureSetting(self, value):
        return self.__setattr__("TemperatureSetting", value)

    @property
    def TemperatureExternal(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TemperatureExternal")

    @TemperatureExternal.setter
    def TemperatureExternal(self, value):
        return self.__setattr__("TemperatureExternal", value)

    @property
    def Filtration(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Filtration")

    @Filtration.setter
    def Filtration(self, value):
        return self.__setattr__("Filtration", value)

    @property
    def AirRelease(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("AirRelease")

    @AirRelease.setter
    def AirRelease(self, value):
        return self.__setattr__("AirRelease", value)

    @property
    def PositionX(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PositionX")

    @PositionX.setter
    def PositionX(self, value):
        return self.__setattr__("PositionX", value)

    @property
    def PositionY(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PositionY")

    @PositionY.setter
    def PositionY(self, value):
        return self.__setattr__("PositionY", value)

    @property
    def PositionZ(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PositionZ")

    @PositionZ.setter
    def PositionZ(self, value):
        return self.__setattr__("PositionZ", value)

    @property
    def VelocityMagnitude(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("VelocityMagnitude")

    @VelocityMagnitude.setter
    def VelocityMagnitude(self, value):
        return self.__setattr__("VelocityMagnitude", value)

    @property
    def VelocityRelativeX(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("VelocityRelativeX")

    @VelocityRelativeX.setter
    def VelocityRelativeX(self, value):
        return self.__setattr__("VelocityRelativeX", value)

    @property
    def VelocityRelativeY(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("VelocityRelativeY")

    @VelocityRelativeY.setter
    def VelocityRelativeY(self, value):
        return self.__setattr__("VelocityRelativeY", value)

    @property
    def VelocityRelativeZ(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("VelocityRelativeZ")

    @VelocityRelativeZ.setter
    def VelocityRelativeZ(self, value):
        return self.__setattr__("VelocityRelativeZ", value)

    @property
    def RatioNitrousOxide(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrousOxide")

    @RatioNitrousOxide.setter
    def RatioNitrousOxide(self, value):
        return self.__setattr__("RatioNitrousOxide", value)

    @property
    def PrefabHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PrefabHash")

    @PrefabHash.setter
    def PrefabHash(self, value):
        return self.__setattr__("PrefabHash", value)

    @property
    def ForceWrite(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ForceWrite")

    @ForceWrite.setter
    def ForceWrite(self, value):
        return self.__setattr__("ForceWrite", value)

    @property
    def SignalStrength(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SignalStrength")

    @SignalStrength.setter
    def SignalStrength(self, value):
        return self.__setattr__("SignalStrength", value)

    @property
    def SignalID(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SignalID")

    @SignalID.setter
    def SignalID(self, value):
        return self.__setattr__("SignalID", value)

    @property
    def TargetX(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TargetX")

    @TargetX.setter
    def TargetX(self, value):
        return self.__setattr__("TargetX", value)

    @property
    def TargetY(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TargetY")

    @TargetY.setter
    def TargetY(self, value):
        return self.__setattr__("TargetY", value)

    @property
    def TargetZ(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TargetZ")

    @TargetZ.setter
    def TargetZ(self, value):
        return self.__setattr__("TargetZ", value)

    @property
    def SettingInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SettingInput")

    @SettingInput.setter
    def SettingInput(self, value):
        return self.__setattr__("SettingInput", value)

    @property
    def SettingOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SettingOutput")

    @SettingOutput.setter
    def SettingOutput(self, value):
        return self.__setattr__("SettingOutput", value)

    @property
    def CurrentResearchPodType(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CurrentResearchPodType")

    @CurrentResearchPodType.setter
    def CurrentResearchPodType(self, value):
        return self.__setattr__("CurrentResearchPodType", value)

    @property
    def ManualResearchRequiredPod(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ManualResearchRequiredPod")

    @ManualResearchRequiredPod.setter
    def ManualResearchRequiredPod(self, value):
        return self.__setattr__("ManualResearchRequiredPod", value)

    @property
    def MineablesInVicinity(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("MineablesInVicinity")

    @MineablesInVicinity.setter
    def MineablesInVicinity(self, value):
        return self.__setattr__("MineablesInVicinity", value)

    @property
    def MineablesInQueue(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("MineablesInQueue")

    @MineablesInQueue.setter
    def MineablesInQueue(self, value):
        return self.__setattr__("MineablesInQueue", value)

    @property
    def NextWeatherEventTime(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("NextWeatherEventTime")

    @NextWeatherEventTime.setter
    def NextWeatherEventTime(self, value):
        return self.__setattr__("NextWeatherEventTime", value)

    @property
    def Combustion(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Combustion")

    @Combustion.setter
    def Combustion(self, value):
        return self.__setattr__("Combustion", value)

    @property
    def Fuel(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Fuel")

    @Fuel.setter
    def Fuel(self, value):
        return self.__setattr__("Fuel", value)

    @property
    def ReturnFuelCost(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ReturnFuelCost")

    @ReturnFuelCost.setter
    def ReturnFuelCost(self, value):
        return self.__setattr__("ReturnFuelCost", value)

    @property
    def CollectableGoods(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CollectableGoods")

    @CollectableGoods.setter
    def CollectableGoods(self, value):
        return self.__setattr__("CollectableGoods", value)

    @property
    def Time(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Time")

    @Time.setter
    def Time(self, value):
        return self.__setattr__("Time", value)

    @property
    def Bpm(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Bpm")

    @Bpm.setter
    def Bpm(self, value):
        return self.__setattr__("Bpm", value)

    @property
    def EnvironmentEfficiency(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("EnvironmentEfficiency")

    @EnvironmentEfficiency.setter
    def EnvironmentEfficiency(self, value):
        return self.__setattr__("EnvironmentEfficiency", value)

    @property
    def WorkingGasEfficiency(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("WorkingGasEfficiency")

    @WorkingGasEfficiency.setter
    def WorkingGasEfficiency(self, value):
        return self.__setattr__("WorkingGasEfficiency", value)

    @property
    def PressureInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureInput")

    @PressureInput.setter
    def PressureInput(self, value):
        return self.__setattr__("PressureInput", value)

    @property
    def TemperatureInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TemperatureInput")

    @TemperatureInput.setter
    def TemperatureInput(self, value):
        return self.__setattr__("TemperatureInput", value)

    @property
    def RatioOxygenInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioOxygenInput")

    @RatioOxygenInput.setter
    def RatioOxygenInput(self, value):
        return self.__setattr__("RatioOxygenInput", value)

    @property
    def RatioCarbonDioxideInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioCarbonDioxideInput")

    @RatioCarbonDioxideInput.setter
    def RatioCarbonDioxideInput(self, value):
        return self.__setattr__("RatioCarbonDioxideInput", value)

    @property
    def RatioNitrogenInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrogenInput")

    @RatioNitrogenInput.setter
    def RatioNitrogenInput(self, value):
        return self.__setattr__("RatioNitrogenInput", value)

    @property
    def RatioPollutantInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioPollutantInput")

    @RatioPollutantInput.setter
    def RatioPollutantInput(self, value):
        return self.__setattr__("RatioPollutantInput", value)

    @property
    def RatioVolatilesInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioVolatilesInput")

    @RatioVolatilesInput.setter
    def RatioVolatilesInput(self, value):
        return self.__setattr__("RatioVolatilesInput", value)

    @property
    def RatioWaterInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioWaterInput")

    @RatioWaterInput.setter
    def RatioWaterInput(self, value):
        return self.__setattr__("RatioWaterInput", value)

    @property
    def RatioNitrousOxideInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrousOxideInput")

    @RatioNitrousOxideInput.setter
    def RatioNitrousOxideInput(self, value):
        return self.__setattr__("RatioNitrousOxideInput", value)

    @property
    def TotalMolesInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TotalMolesInput")

    @TotalMolesInput.setter
    def TotalMolesInput(self, value):
        return self.__setattr__("TotalMolesInput", value)

    @property
    def PressureInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureInput2")

    @PressureInput2.setter
    def PressureInput2(self, value):
        return self.__setattr__("PressureInput2", value)

    @property
    def TemperatureInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TemperatureInput2")

    @TemperatureInput2.setter
    def TemperatureInput2(self, value):
        return self.__setattr__("TemperatureInput2", value)

    @property
    def RatioOxygenInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioOxygenInput2")

    @RatioOxygenInput2.setter
    def RatioOxygenInput2(self, value):
        return self.__setattr__("RatioOxygenInput2", value)

    @property
    def RatioCarbonDioxideInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioCarbonDioxideInput2")

    @RatioCarbonDioxideInput2.setter
    def RatioCarbonDioxideInput2(self, value):
        return self.__setattr__("RatioCarbonDioxideInput2", value)

    @property
    def RatioNitrogenInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrogenInput2")

    @RatioNitrogenInput2.setter
    def RatioNitrogenInput2(self, value):
        return self.__setattr__("RatioNitrogenInput2", value)

    @property
    def RatioPollutantInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioPollutantInput2")

    @RatioPollutantInput2.setter
    def RatioPollutantInput2(self, value):
        return self.__setattr__("RatioPollutantInput2", value)

    @property
    def RatioVolatilesInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioVolatilesInput2")

    @RatioVolatilesInput2.setter
    def RatioVolatilesInput2(self, value):
        return self.__setattr__("RatioVolatilesInput2", value)

    @property
    def RatioWaterInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioWaterInput2")

    @RatioWaterInput2.setter
    def RatioWaterInput2(self, value):
        return self.__setattr__("RatioWaterInput2", value)

    @property
    def RatioNitrousOxideInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrousOxideInput2")

    @RatioNitrousOxideInput2.setter
    def RatioNitrousOxideInput2(self, value):
        return self.__setattr__("RatioNitrousOxideInput2", value)

    @property
    def TotalMolesInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TotalMolesInput2")

    @TotalMolesInput2.setter
    def TotalMolesInput2(self, value):
        return self.__setattr__("TotalMolesInput2", value)

    @property
    def PressureOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureOutput")

    @PressureOutput.setter
    def PressureOutput(self, value):
        return self.__setattr__("PressureOutput", value)

    @property
    def TemperatureOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TemperatureOutput")

    @TemperatureOutput.setter
    def TemperatureOutput(self, value):
        return self.__setattr__("TemperatureOutput", value)

    @property
    def RatioOxygenOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioOxygenOutput")

    @RatioOxygenOutput.setter
    def RatioOxygenOutput(self, value):
        return self.__setattr__("RatioOxygenOutput", value)

    @property
    def RatioCarbonDioxideOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioCarbonDioxideOutput")

    @RatioCarbonDioxideOutput.setter
    def RatioCarbonDioxideOutput(self, value):
        return self.__setattr__("RatioCarbonDioxideOutput", value)

    @property
    def RatioNitrogenOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrogenOutput")

    @RatioNitrogenOutput.setter
    def RatioNitrogenOutput(self, value):
        return self.__setattr__("RatioNitrogenOutput", value)

    @property
    def RatioPollutantOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioPollutantOutput")

    @RatioPollutantOutput.setter
    def RatioPollutantOutput(self, value):
        return self.__setattr__("RatioPollutantOutput", value)

    @property
    def RatioVolatilesOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioVolatilesOutput")

    @RatioVolatilesOutput.setter
    def RatioVolatilesOutput(self, value):
        return self.__setattr__("RatioVolatilesOutput", value)

    @property
    def RatioWaterOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioWaterOutput")

    @RatioWaterOutput.setter
    def RatioWaterOutput(self, value):
        return self.__setattr__("RatioWaterOutput", value)

    @property
    def RatioNitrousOxideOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrousOxideOutput")

    @RatioNitrousOxideOutput.setter
    def RatioNitrousOxideOutput(self, value):
        return self.__setattr__("RatioNitrousOxideOutput", value)

    @property
    def TotalMolesOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TotalMolesOutput")

    @TotalMolesOutput.setter
    def TotalMolesOutput(self, value):
        return self.__setattr__("TotalMolesOutput", value)

    @property
    def PressureOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureOutput2")

    @PressureOutput2.setter
    def PressureOutput2(self, value):
        return self.__setattr__("PressureOutput2", value)

    @property
    def TemperatureOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TemperatureOutput2")

    @TemperatureOutput2.setter
    def TemperatureOutput2(self, value):
        return self.__setattr__("TemperatureOutput2", value)

    @property
    def RatioOxygenOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioOxygenOutput2")

    @RatioOxygenOutput2.setter
    def RatioOxygenOutput2(self, value):
        return self.__setattr__("RatioOxygenOutput2", value)

    @property
    def RatioCarbonDioxideOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioCarbonDioxideOutput2")

    @RatioCarbonDioxideOutput2.setter
    def RatioCarbonDioxideOutput2(self, value):
        return self.__setattr__("RatioCarbonDioxideOutput2", value)

    @property
    def RatioNitrogenOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrogenOutput2")

    @RatioNitrogenOutput2.setter
    def RatioNitrogenOutput2(self, value):
        return self.__setattr__("RatioNitrogenOutput2", value)

    @property
    def RatioPollutantOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioPollutantOutput2")

    @RatioPollutantOutput2.setter
    def RatioPollutantOutput2(self, value):
        return self.__setattr__("RatioPollutantOutput2", value)

    @property
    def RatioVolatilesOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioVolatilesOutput2")

    @RatioVolatilesOutput2.setter
    def RatioVolatilesOutput2(self, value):
        return self.__setattr__("RatioVolatilesOutput2", value)

    @property
    def RatioWaterOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioWaterOutput2")

    @RatioWaterOutput2.setter
    def RatioWaterOutput2(self, value):
        return self.__setattr__("RatioWaterOutput2", value)

    @property
    def RatioNitrousOxideOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrousOxideOutput2")

    @RatioNitrousOxideOutput2.setter
    def RatioNitrousOxideOutput2(self, value):
        return self.__setattr__("RatioNitrousOxideOutput2", value)

    @property
    def TotalMolesOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TotalMolesOutput2")

    @TotalMolesOutput2.setter
    def TotalMolesOutput2(self, value):
        return self.__setattr__("TotalMolesOutput2", value)

    @property
    def CombustionInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CombustionInput")

    @CombustionInput.setter
    def CombustionInput(self, value):
        return self.__setattr__("CombustionInput", value)

    @property
    def CombustionInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CombustionInput2")

    @CombustionInput2.setter
    def CombustionInput2(self, value):
        return self.__setattr__("CombustionInput2", value)

    @property
    def CombustionOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CombustionOutput")

    @CombustionOutput.setter
    def CombustionOutput(self, value):
        return self.__setattr__("CombustionOutput", value)

    @property
    def CombustionOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CombustionOutput2")

    @CombustionOutput2.setter
    def CombustionOutput2(self, value):
        return self.__setattr__("CombustionOutput2", value)

    @property
    def OperationalTemperatureEfficiency(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("OperationalTemperatureEfficiency")

    @OperationalTemperatureEfficiency.setter
    def OperationalTemperatureEfficiency(self, value):
        return self.__setattr__("OperationalTemperatureEfficiency", value)

    @property
    def TemperatureDifferentialEfficiency(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TemperatureDifferentialEfficiency")

    @TemperatureDifferentialEfficiency.setter
    def TemperatureDifferentialEfficiency(self, value):
        return self.__setattr__("TemperatureDifferentialEfficiency", value)

    @property
    def PressureEfficiency(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureEfficiency")

    @PressureEfficiency.setter
    def PressureEfficiency(self, value):
        return self.__setattr__("PressureEfficiency", value)

    @property
    def CombustionLimiter(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CombustionLimiter")

    @CombustionLimiter.setter
    def CombustionLimiter(self, value):
        return self.__setattr__("CombustionLimiter", value)

    @property
    def Throttle(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Throttle")

    @Throttle.setter
    def Throttle(self, value):
        return self.__setattr__("Throttle", value)

    @property
    def Rpm(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Rpm")

    @Rpm.setter
    def Rpm(self, value):
        return self.__setattr__("Rpm", value)

    @property
    def Stress(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Stress")

    @Stress.setter
    def Stress(self, value):
        return self.__setattr__("Stress", value)

    @property
    def InterrogationProgress(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("InterrogationProgress")

    @InterrogationProgress.setter
    def InterrogationProgress(self, value):
        return self.__setattr__("InterrogationProgress", value)

    @property
    def TargetPadIndex(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TargetPadIndex")

    @TargetPadIndex.setter
    def TargetPadIndex(self, value):
        return self.__setattr__("TargetPadIndex", value)

    @property
    def SizeX(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SizeX")

    @SizeX.setter
    def SizeX(self, value):
        return self.__setattr__("SizeX", value)

    @property
    def SizeY(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SizeY")

    @SizeY.setter
    def SizeY(self, value):
        return self.__setattr__("SizeY", value)

    @property
    def SizeZ(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SizeZ")

    @SizeZ.setter
    def SizeZ(self, value):
        return self.__setattr__("SizeZ", value)

    @property
    def MinimumWattsToContact(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("MinimumWattsToContact")

    @MinimumWattsToContact.setter
    def MinimumWattsToContact(self, value):
        return self.__setattr__("MinimumWattsToContact", value)

    @property
    def WattsReachingContact(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("WattsReachingContact")

    @WattsReachingContact.setter
    def WattsReachingContact(self, value):
        return self.__setattr__("WattsReachingContact", value)

    @property
    def Channel0(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Channel0")

    @Channel0.setter
    def Channel0(self, value):
        return self.__setattr__("Channel0", value)

    @property
    def Channel1(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Channel1")

    @Channel1.setter
    def Channel1(self, value):
        return self.__setattr__("Channel1", value)

    @property
    def Channel2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Channel2")

    @Channel2.setter
    def Channel2(self, value):
        return self.__setattr__("Channel2", value)

    @property
    def Channel3(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Channel3")

    @Channel3.setter
    def Channel3(self, value):
        return self.__setattr__("Channel3", value)

    @property
    def Channel4(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Channel4")

    @Channel4.setter
    def Channel4(self, value):
        return self.__setattr__("Channel4", value)

    @property
    def Channel5(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Channel5")

    @Channel5.setter
    def Channel5(self, value):
        return self.__setattr__("Channel5", value)

    @property
    def Channel6(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Channel6")

    @Channel6.setter
    def Channel6(self, value):
        return self.__setattr__("Channel6", value)

    @property
    def Channel7(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Channel7")

    @Channel7.setter
    def Channel7(self, value):
        return self.__setattr__("Channel7", value)

    @property
    def LineNumber(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("LineNumber")

    @LineNumber.setter
    def LineNumber(self, value):
        return self.__setattr__("LineNumber", value)

    @property
    def Flush(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Flush")

    @Flush.setter
    def Flush(self, value):
        return self.__setattr__("Flush", value)

    @property
    def SoundAlert(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SoundAlert")

    @SoundAlert.setter
    def SoundAlert(self, value):
        return self.__setattr__("SoundAlert", value)

    @property
    def SolarIrradiance(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SolarIrradiance")

    @SolarIrradiance.setter
    def SolarIrradiance(self, value):
        return self.__setattr__("SolarIrradiance", value)

    @property
    def RatioLiquidNitrogen(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrogen")

    @RatioLiquidNitrogen.setter
    def RatioLiquidNitrogen(self, value):
        return self.__setattr__("RatioLiquidNitrogen", value)

    @property
    def RatioLiquidNitrogenInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrogenInput")

    @RatioLiquidNitrogenInput.setter
    def RatioLiquidNitrogenInput(self, value):
        return self.__setattr__("RatioLiquidNitrogenInput", value)

    @property
    def RatioLiquidNitrogenInput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrogenInput2")

    @RatioLiquidNitrogenInput2.setter
    def RatioLiquidNitrogenInput2(self, value):
        return self.__setattr__("RatioLiquidNitrogenInput2", value)

    @property
    def RatioLiquidNitrogenOutput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrogenOutput")

    @RatioLiquidNitrogenOutput.setter
    def RatioLiquidNitrogenOutput(self, value):
        return self.__setattr__("RatioLiquidNitrogenOutput", value)

    @property
    def RatioLiquidNitrogenOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrogenOutput2")

    @RatioLiquidNitrogenOutput2.setter
    def RatioLiquidNitrogenOutput2(self, value):
        return self.__setattr__("RatioLiquidNitrogenOutput2", value)

    @property
    def VolumeOfLiquid(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("VolumeOfLiquid")

    @VolumeOfLiquid.setter
    def VolumeOfLiquid(self, value):
        return self.__setattr__("VolumeOfLiquid", value)

    @property
    def RatioLiquidOxygen(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidOxygen")

    @RatioLiquidOxygen.setter
    def RatioLiquidOxygen(self, value):
        return self.__setattr__("RatioLiquidOxygen", value)

    @property
    def RatioLiquidOxygenInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidOxygenInput")

    @RatioLiquidOxygenInput.setter
    def RatioLiquidOxygenInput(self, value):
        return self.__setattr__("RatioLiquidOxygenInput", value)

    @property
    def RatioLiquidOxygenInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidOxygenInput2")

    @RatioLiquidOxygenInput2.setter
    def RatioLiquidOxygenInput2(self, value):
        return self.__setattr__("RatioLiquidOxygenInput2", value)

    @property
    def RatioLiquidOxygenOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidOxygenOutput")

    @RatioLiquidOxygenOutput.setter
    def RatioLiquidOxygenOutput(self, value):
        return self.__setattr__("RatioLiquidOxygenOutput", value)

    @property
    def RatioLiquidOxygenOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidOxygenOutput2")

    @RatioLiquidOxygenOutput2.setter
    def RatioLiquidOxygenOutput2(self, value):
        return self.__setattr__("RatioLiquidOxygenOutput2", value)

    @property
    def RatioLiquidVolatiles(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidVolatiles")

    @RatioLiquidVolatiles.setter
    def RatioLiquidVolatiles(self, value):
        return self.__setattr__("RatioLiquidVolatiles", value)

    @property
    def RatioLiquidVolatilesInput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidVolatilesInput")

    @RatioLiquidVolatilesInput.setter
    def RatioLiquidVolatilesInput(self, value):
        return self.__setattr__("RatioLiquidVolatilesInput", value)

    @property
    def RatioLiquidVolatilesInput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidVolatilesInput2")

    @RatioLiquidVolatilesInput2.setter
    def RatioLiquidVolatilesInput2(self, value):
        return self.__setattr__("RatioLiquidVolatilesInput2", value)

    @property
    def RatioLiquidVolatilesOutput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidVolatilesOutput")

    @RatioLiquidVolatilesOutput.setter
    def RatioLiquidVolatilesOutput(self, value):
        return self.__setattr__("RatioLiquidVolatilesOutput", value)

    @property
    def RatioLiquidVolatilesOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidVolatilesOutput2")

    @RatioLiquidVolatilesOutput2.setter
    def RatioLiquidVolatilesOutput2(self, value):
        return self.__setattr__("RatioLiquidVolatilesOutput2", value)

    @property
    def RatioSteam(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioSteam")

    @RatioSteam.setter
    def RatioSteam(self, value):
        return self.__setattr__("RatioSteam", value)

    @property
    def RatioSteamInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioSteamInput")

    @RatioSteamInput.setter
    def RatioSteamInput(self, value):
        return self.__setattr__("RatioSteamInput", value)

    @property
    def RatioSteamInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioSteamInput2")

    @RatioSteamInput2.setter
    def RatioSteamInput2(self, value):
        return self.__setattr__("RatioSteamInput2", value)

    @property
    def RatioSteamOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioSteamOutput")

    @RatioSteamOutput.setter
    def RatioSteamOutput(self, value):
        return self.__setattr__("RatioSteamOutput", value)

    @property
    def RatioSteamOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioSteamOutput2")

    @RatioSteamOutput2.setter
    def RatioSteamOutput2(self, value):
        return self.__setattr__("RatioSteamOutput2", value)

    @property
    def ContactTypeId(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ContactTypeId")

    @ContactTypeId.setter
    def ContactTypeId(self, value):
        return self.__setattr__("ContactTypeId", value)

    @property
    def RatioLiquidCarbonDioxide(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxide")

    @RatioLiquidCarbonDioxide.setter
    def RatioLiquidCarbonDioxide(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxide", value)

    @property
    def RatioLiquidCarbonDioxideInput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideInput")

    @RatioLiquidCarbonDioxideInput.setter
    def RatioLiquidCarbonDioxideInput(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideInput", value)

    @property
    def RatioLiquidCarbonDioxideInput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideInput2")

    @RatioLiquidCarbonDioxideInput2.setter
    def RatioLiquidCarbonDioxideInput2(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideInput2", value)

    @property
    def RatioLiquidCarbonDioxideOutput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideOutput")

    @RatioLiquidCarbonDioxideOutput.setter
    def RatioLiquidCarbonDioxideOutput(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideOutput", value)

    @property
    def RatioLiquidCarbonDioxideOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideOutput2")

    @RatioLiquidCarbonDioxideOutput2.setter
    def RatioLiquidCarbonDioxideOutput2(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideOutput2", value)

    @property
    def RatioLiquidPollutant(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidPollutant")

    @RatioLiquidPollutant.setter
    def RatioLiquidPollutant(self, value):
        return self.__setattr__("RatioLiquidPollutant", value)

    @property
    def RatioLiquidPollutantInput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidPollutantInput")

    @RatioLiquidPollutantInput.setter
    def RatioLiquidPollutantInput(self, value):
        return self.__setattr__("RatioLiquidPollutantInput", value)

    @property
    def RatioLiquidPollutantInput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidPollutantInput2")

    @RatioLiquidPollutantInput2.setter
    def RatioLiquidPollutantInput2(self, value):
        return self.__setattr__("RatioLiquidPollutantInput2", value)

    @property
    def RatioLiquidPollutantOutput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidPollutantOutput")

    @RatioLiquidPollutantOutput.setter
    def RatioLiquidPollutantOutput(self, value):
        return self.__setattr__("RatioLiquidPollutantOutput", value)

    @property
    def RatioLiquidPollutantOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidPollutantOutput2")

    @RatioLiquidPollutantOutput2.setter
    def RatioLiquidPollutantOutput2(self, value):
        return self.__setattr__("RatioLiquidPollutantOutput2", value)

    @property
    def RatioLiquidNitrousOxide(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrousOxide")

    @RatioLiquidNitrousOxide.setter
    def RatioLiquidNitrousOxide(self, value):
        return self.__setattr__("RatioLiquidNitrousOxide", value)

    @property
    def RatioLiquidNitrousOxideInput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideInput")

    @RatioLiquidNitrousOxideInput.setter
    def RatioLiquidNitrousOxideInput(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideInput", value)

    @property
    def RatioLiquidNitrousOxideInput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideInput2")

    @RatioLiquidNitrousOxideInput2.setter
    def RatioLiquidNitrousOxideInput2(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideInput2", value)

    @property
    def RatioLiquidNitrousOxideOutput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideOutput")

    @RatioLiquidNitrousOxideOutput.setter
    def RatioLiquidNitrousOxideOutput(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideOutput", value)

    @property
    def RatioLiquidNitrousOxideOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideOutput2")

    @RatioLiquidNitrousOxideOutput2.setter
    def RatioLiquidNitrousOxideOutput2(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideOutput2", value)

    @property
    def Progress(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Progress")

    @Progress.setter
    def Progress(self, value):
        return self.__setattr__("Progress", value)

    @property
    def DestinationCode(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("DestinationCode")

    @DestinationCode.setter
    def DestinationCode(self, value):
        return self.__setattr__("DestinationCode", value)

    @property
    def Acceleration(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Acceleration")

    @Acceleration.setter
    def Acceleration(self, value):
        return self.__setattr__("Acceleration", value)

    @property
    def ReferenceId(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ReferenceId")

    @ReferenceId.setter
    def ReferenceId(self, value):
        return self.__setattr__("ReferenceId", value)

    @property
    def AutoShutOff(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("AutoShutOff")

    @AutoShutOff.setter
    def AutoShutOff(self, value):
        return self.__setattr__("AutoShutOff", value)

    @property
    def Mass(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Mass")

    @Mass.setter
    def Mass(self, value):
        return self.__setattr__("Mass", value)

    @property
    def DryMass(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("DryMass")

    @DryMass.setter
    def DryMass(self, value):
        return self.__setattr__("DryMass", value)

    @property
    def Thrust(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Thrust")

    @Thrust.setter
    def Thrust(self, value):
        return self.__setattr__("Thrust", value)

    @property
    def Weight(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Weight")

    @Weight.setter
    def Weight(self, value):
        return self.__setattr__("Weight", value)

    @property
    def ThrustToWeight(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ThrustToWeight")

    @ThrustToWeight.setter
    def ThrustToWeight(self, value):
        return self.__setattr__("ThrustToWeight", value)

    @property
    def TimeToDestination(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TimeToDestination")

    @TimeToDestination.setter
    def TimeToDestination(self, value):
        return self.__setattr__("TimeToDestination", value)

    @property
    def BurnTimeRemaining(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("BurnTimeRemaining")

    @BurnTimeRemaining.setter
    def BurnTimeRemaining(self, value):
        return self.__setattr__("BurnTimeRemaining", value)

    @property
    def AutoLand(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("AutoLand")

    @AutoLand.setter
    def AutoLand(self, value):
        return self.__setattr__("AutoLand", value)

    @property
    def ForwardX(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ForwardX")

    @ForwardX.setter
    def ForwardX(self, value):
        return self.__setattr__("ForwardX", value)

    @property
    def ForwardY(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ForwardY")

    @ForwardY.setter
    def ForwardY(self, value):
        return self.__setattr__("ForwardY", value)

    @property
    def ForwardZ(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ForwardZ")

    @ForwardZ.setter
    def ForwardZ(self, value):
        return self.__setattr__("ForwardZ", value)

    @property
    def Orientation(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Orientation")

    @Orientation.setter
    def Orientation(self, value):
        return self.__setattr__("Orientation", value)

    @property
    def VelocityX(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("VelocityX")

    @VelocityX.setter
    def VelocityX(self, value):
        return self.__setattr__("VelocityX", value)

    @property
    def VelocityY(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("VelocityY")

    @VelocityY.setter
    def VelocityY(self, value):
        return self.__setattr__("VelocityY", value)

    @property
    def VelocityZ(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("VelocityZ")

    @VelocityZ.setter
    def VelocityZ(self, value):
        return self.__setattr__("VelocityZ", value)

    @property
    def PassedMoles(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PassedMoles")

    @PassedMoles.setter
    def PassedMoles(self, value):
        return self.__setattr__("PassedMoles", value)

    @property
    def ExhaustVelocity(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ExhaustVelocity")

    @ExhaustVelocity.setter
    def ExhaustVelocity(self, value):
        return self.__setattr__("ExhaustVelocity", value)

    @property
    def FlightControlRule(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("FlightControlRule")

    @FlightControlRule.setter
    def FlightControlRule(self, value):
        return self.__setattr__("FlightControlRule", value)

    @property
    def ReEntryAltitude(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ReEntryAltitude")

    @ReEntryAltitude.setter
    def ReEntryAltitude(self, value):
        return self.__setattr__("ReEntryAltitude", value)

    @property
    def Apex(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Apex")

    @Apex.setter
    def Apex(self, value):
        return self.__setattr__("Apex", value)

    @property
    def EntityState(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("EntityState")

    @EntityState.setter
    def EntityState(self, value):
        return self.__setattr__("EntityState", value)

    @property
    def DrillCondition(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("DrillCondition")

    @DrillCondition.setter
    def DrillCondition(self, value):
        return self.__setattr__("DrillCondition", value)

    @property
    def Index(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Index")

    @Index.setter
    def Index(self, value):
        return self.__setattr__("Index", value)

    @property
    def CelestialHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CelestialHash")

    @CelestialHash.setter
    def CelestialHash(self, value):
        return self.__setattr__("CelestialHash", value)

    @property
    def AlignmentError(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("AlignmentError")

    @AlignmentError.setter
    def AlignmentError(self, value):
        return self.__setattr__("AlignmentError", value)

    @property
    def DistanceAu(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("DistanceAu")

    @DistanceAu.setter
    def DistanceAu(self, value):
        return self.__setattr__("DistanceAu", value)

    @property
    def OrbitPeriod(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("OrbitPeriod")

    @OrbitPeriod.setter
    def OrbitPeriod(self, value):
        return self.__setattr__("OrbitPeriod", value)

    @property
    def Inclination(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Inclination")

    @Inclination.setter
    def Inclination(self, value):
        return self.__setattr__("Inclination", value)

    @property
    def Eccentricity(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Eccentricity")

    @Eccentricity.setter
    def Eccentricity(self, value):
        return self.__setattr__("Eccentricity", value)

    @property
    def SemiMajorAxis(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SemiMajorAxis")

    @SemiMajorAxis.setter
    def SemiMajorAxis(self, value):
        return self.__setattr__("SemiMajorAxis", value)

    @property
    def DistanceKm(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("DistanceKm")

    @DistanceKm.setter
    def DistanceKm(self, value):
        return self.__setattr__("DistanceKm", value)

    @property
    def CelestialParentHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CelestialParentHash")

    @CelestialParentHash.setter
    def CelestialParentHash(self, value):
        return self.__setattr__("CelestialParentHash", value)

    @property
    def TrueAnomaly(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TrueAnomaly")

    @TrueAnomaly.setter
    def TrueAnomaly(self, value):
        return self.__setattr__("TrueAnomaly", value)

    @property
    def RatioHydrogen(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioHydrogen")

    @RatioHydrogen.setter
    def RatioHydrogen(self, value):
        return self.__setattr__("RatioHydrogen", value)

    @property
    def RatioLiquidHydrogen(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidHydrogen")

    @RatioLiquidHydrogen.setter
    def RatioLiquidHydrogen(self, value):
        return self.__setattr__("RatioLiquidHydrogen", value)

    @property
    def RatioPollutedWater(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioPollutedWater")

    @RatioPollutedWater.setter
    def RatioPollutedWater(self, value):
        return self.__setattr__("RatioPollutedWater", value)

    @property
    def Discover(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Discover")

    @Discover.setter
    def Discover(self, value):
        return self.__setattr__("Discover", value)

    @property
    def Chart(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Chart")

    @Chart.setter
    def Chart(self, value):
        return self.__setattr__("Chart", value)

    @property
    def Survey(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Survey")

    @Survey.setter
    def Survey(self, value):
        return self.__setattr__("Survey", value)

    @property
    def NavPoints(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("NavPoints")

    @NavPoints.setter
    def NavPoints(self, value):
        return self.__setattr__("NavPoints", value)

    @property
    def ChartedNavPoints(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ChartedNavPoints")

    @ChartedNavPoints.setter
    def ChartedNavPoints(self, value):
        return self.__setattr__("ChartedNavPoints", value)

    @property
    def Sites(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Sites")

    @Sites.setter
    def Sites(self, value):
        return self.__setattr__("Sites", value)

    @property
    def CurrentCode(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CurrentCode")

    @CurrentCode.setter
    def CurrentCode(self, value):
        return self.__setattr__("CurrentCode", value)

    @property
    def Density(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Density")

    @Density.setter
    def Density(self, value):
        return self.__setattr__("Density", value)

    @property
    def Richness(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Richness")

    @Richness.setter
    def Richness(self, value):
        return self.__setattr__("Richness", value)

    @property
    def Size(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Size")

    @Size.setter
    def Size(self, value):
        return self.__setattr__("Size", value)

    @property
    def TotalQuantity(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TotalQuantity")

    @TotalQuantity.setter
    def TotalQuantity(self, value):
        return self.__setattr__("TotalQuantity", value)

    @property
    def MinedQuantity(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("MinedQuantity")

    @MinedQuantity.setter
    def MinedQuantity(self, value):
        return self.__setattr__("MinedQuantity", value)

    @property
    def BestContactFilter(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("BestContactFilter")

    @BestContactFilter.setter
    def BestContactFilter(self, value):
        return self.__setattr__("BestContactFilter", value)

    @property
    def NameHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("NameHash")

    @NameHash.setter
    def NameHash(self, value):
        return self.__setattr__("NameHash", value)

    @property
    def Altitude(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Altitude")

    @Altitude.setter
    def Altitude(self, value):
        return self.__setattr__("Altitude", value)

    @property
    def TargetSlotIndex(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TargetSlotIndex")

    @TargetSlotIndex.setter
    def TargetSlotIndex(self, value):
        return self.__setattr__("TargetSlotIndex", value)

    @property
    def TargetPrefabHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TargetPrefabHash")

    @TargetPrefabHash.setter
    def TargetPrefabHash(self, value):
        return self.__setattr__("TargetPrefabHash", value)

    @property
    def Extended(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Extended")

    @Extended.setter
    def Extended(self, value):
        return self.__setattr__("Extended", value)

    @property
    def NetworkFault(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("NetworkFault")

    @NetworkFault.setter
    def NetworkFault(self, value):
        return self.__setattr__("NetworkFault", value)

    @property
    def ProportionalGain(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ProportionalGain")

    @ProportionalGain.setter
    def ProportionalGain(self, value):
        return self.__setattr__("ProportionalGain", value)

    @property
    def IntegralGain(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("IntegralGain")

    @IntegralGain.setter
    def IntegralGain(self, value):
        return self.__setattr__("IntegralGain", value)

    @property
    def DerivativeGain(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("DerivativeGain")

    @DerivativeGain.setter
    def DerivativeGain(self, value):
        return self.__setattr__("DerivativeGain", value)

    @property
    def Minimum(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Minimum")

    @Minimum.setter
    def Minimum(self, value):
        return self.__setattr__("Minimum", value)

    @property
    def Setpoint(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Setpoint")

    @Setpoint.setter
    def Setpoint(self, value):
        return self.__setattr__("Setpoint", value)

    @property
    def Reset(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Reset")

    @Reset.setter
    def Reset(self, value):
        return self.__setattr__("Reset", value)

    @property
    def StackSize(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("StackSize")

    @StackSize.setter
    def StackSize(self, value):
        return self.__setattr__("StackSize", value)


class _GenericStructures:

    @property
    def None_(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("None_")

    @None_.setter
    def None_(self, value):
        return self.__setattr__("None_", value)

    @property
    def Power(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Power")

    @Power.setter
    def Power(self, value):
        return self.__setattr__("Power", value)

    @property
    def Open(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Open")

    @Open.setter
    def Open(self, value):
        return self.__setattr__("Open", value)

    @property
    def Mode(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Mode")

    @Mode.setter
    def Mode(self, value):
        return self.__setattr__("Mode", value)

    @property
    def Error(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Error")

    @Error.setter
    def Error(self, value):
        return self.__setattr__("Error", value)

    @property
    def Pressure(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Pressure")

    @Pressure.setter
    def Pressure(self, value):
        return self.__setattr__("Pressure", value)

    @property
    def Temperature(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Temperature")

    @Temperature.setter
    def Temperature(self, value):
        return self.__setattr__("Temperature", value)

    @property
    def PressureExternal(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureExternal")

    @PressureExternal.setter
    def PressureExternal(self, value):
        return self.__setattr__("PressureExternal", value)

    @property
    def PressureInternal(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureInternal")

    @PressureInternal.setter
    def PressureInternal(self, value):
        return self.__setattr__("PressureInternal", value)

    @property
    def Activate(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Activate")

    @Activate.setter
    def Activate(self, value):
        return self.__setattr__("Activate", value)

    @property
    def Lock(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Lock")

    @Lock.setter
    def Lock(self, value):
        return self.__setattr__("Lock", value)

    @property
    def Charge(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Charge")

    @Charge.setter
    def Charge(self, value):
        return self.__setattr__("Charge", value)

    @property
    def Setting(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Setting")

    @Setting.setter
    def Setting(self, value):
        return self.__setattr__("Setting", value)

    @property
    def Reagents(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Reagents")

    @Reagents.setter
    def Reagents(self, value):
        return self.__setattr__("Reagents", value)

    @property
    def RatioOxygen(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioOxygen")

    @RatioOxygen.setter
    def RatioOxygen(self, value):
        return self.__setattr__("RatioOxygen", value)

    @property
    def RatioCarbonDioxide(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioCarbonDioxide")

    @RatioCarbonDioxide.setter
    def RatioCarbonDioxide(self, value):
        return self.__setattr__("RatioCarbonDioxide", value)

    @property
    def RatioNitrogen(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrogen")

    @RatioNitrogen.setter
    def RatioNitrogen(self, value):
        return self.__setattr__("RatioNitrogen", value)

    @property
    def RatioPollutant(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioPollutant")

    @RatioPollutant.setter
    def RatioPollutant(self, value):
        return self.__setattr__("RatioPollutant", value)

    @property
    def RatioVolatiles(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioVolatiles")

    @RatioVolatiles.setter
    def RatioVolatiles(self, value):
        return self.__setattr__("RatioVolatiles", value)

    @property
    def RatioWater(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioWater")

    @RatioWater.setter
    def RatioWater(self, value):
        return self.__setattr__("RatioWater", value)

    @property
    def Horizontal(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Horizontal")

    @Horizontal.setter
    def Horizontal(self, value):
        return self.__setattr__("Horizontal", value)

    @property
    def Vertical(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Vertical")

    @Vertical.setter
    def Vertical(self, value):
        return self.__setattr__("Vertical", value)

    @property
    def SolarAngle(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SolarAngle")

    @SolarAngle.setter
    def SolarAngle(self, value):
        return self.__setattr__("SolarAngle", value)

    @property
    def Maximum(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Maximum")

    @Maximum.setter
    def Maximum(self, value):
        return self.__setattr__("Maximum", value)

    @property
    def Ratio(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Ratio")

    @Ratio.setter
    def Ratio(self, value):
        return self.__setattr__("Ratio", value)

    @property
    def PowerPotential(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PowerPotential")

    @PowerPotential.setter
    def PowerPotential(self, value):
        return self.__setattr__("PowerPotential", value)

    @property
    def PowerActual(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PowerActual")

    @PowerActual.setter
    def PowerActual(self, value):
        return self.__setattr__("PowerActual", value)

    @property
    def Quantity(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Quantity")

    @Quantity.setter
    def Quantity(self, value):
        return self.__setattr__("Quantity", value)

    @property
    def On(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("On")

    @On.setter
    def On(self, value):
        return self.__setattr__("On", value)

    @property
    def ImportQuantity(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ImportQuantity")

    @ImportQuantity.setter
    def ImportQuantity(self, value):
        return self.__setattr__("ImportQuantity", value)

    @property
    def ImportSlotOccupant(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ImportSlotOccupant")

    @ImportSlotOccupant.setter
    def ImportSlotOccupant(self, value):
        return self.__setattr__("ImportSlotOccupant", value)

    @property
    def ExportQuantity(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ExportQuantity")

    @ExportQuantity.setter
    def ExportQuantity(self, value):
        return self.__setattr__("ExportQuantity", value)

    @property
    def ExportSlotOccupant(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ExportSlotOccupant")

    @ExportSlotOccupant.setter
    def ExportSlotOccupant(self, value):
        return self.__setattr__("ExportSlotOccupant", value)

    @property
    def RequiredPower(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RequiredPower")

    @RequiredPower.setter
    def RequiredPower(self, value):
        return self.__setattr__("RequiredPower", value)

    @property
    def HorizontalRatio(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("HorizontalRatio")

    @HorizontalRatio.setter
    def HorizontalRatio(self, value):
        return self.__setattr__("HorizontalRatio", value)

    @property
    def VerticalRatio(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("VerticalRatio")

    @VerticalRatio.setter
    def VerticalRatio(self, value):
        return self.__setattr__("VerticalRatio", value)

    @property
    def PowerRequired(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PowerRequired")

    @PowerRequired.setter
    def PowerRequired(self, value):
        return self.__setattr__("PowerRequired", value)

    @property
    def Idle(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Idle")

    @Idle.setter
    def Idle(self, value):
        return self.__setattr__("Idle", value)

    @property
    def Color(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Color")

    @Color.setter
    def Color(self, value):
        return self.__setattr__("Color", value)

    @property
    def ElevatorSpeed(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ElevatorSpeed")

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value):
        return self.__setattr__("ElevatorSpeed", value)

    @property
    def ElevatorLevel(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ElevatorLevel")

    @ElevatorLevel.setter
    def ElevatorLevel(self, value):
        return self.__setattr__("ElevatorLevel", value)

    @property
    def RecipeHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RecipeHash")

    @RecipeHash.setter
    def RecipeHash(self, value):
        return self.__setattr__("RecipeHash", value)

    @property
    def ExportSlotHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ExportSlotHash")

    @ExportSlotHash.setter
    def ExportSlotHash(self, value):
        return self.__setattr__("ExportSlotHash", value)

    @property
    def ImportSlotHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ImportSlotHash")

    @ImportSlotHash.setter
    def ImportSlotHash(self, value):
        return self.__setattr__("ImportSlotHash", value)

    @property
    def PlantHealth1(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHealth1")

    @PlantHealth1.setter
    def PlantHealth1(self, value):
        return self.__setattr__("PlantHealth1", value)

    @property
    def PlantHealth2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHealth2")

    @PlantHealth2.setter
    def PlantHealth2(self, value):
        return self.__setattr__("PlantHealth2", value)

    @property
    def PlantHealth3(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHealth3")

    @PlantHealth3.setter
    def PlantHealth3(self, value):
        return self.__setattr__("PlantHealth3", value)

    @property
    def PlantHealth4(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHealth4")

    @PlantHealth4.setter
    def PlantHealth4(self, value):
        return self.__setattr__("PlantHealth4", value)

    @property
    def PlantGrowth1(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantGrowth1")

    @PlantGrowth1.setter
    def PlantGrowth1(self, value):
        return self.__setattr__("PlantGrowth1", value)

    @property
    def PlantGrowth2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantGrowth2")

    @PlantGrowth2.setter
    def PlantGrowth2(self, value):
        return self.__setattr__("PlantGrowth2", value)

    @property
    def PlantGrowth3(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantGrowth3")

    @PlantGrowth3.setter
    def PlantGrowth3(self, value):
        return self.__setattr__("PlantGrowth3", value)

    @property
    def PlantGrowth4(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantGrowth4")

    @PlantGrowth4.setter
    def PlantGrowth4(self, value):
        return self.__setattr__("PlantGrowth4", value)

    @property
    def PlantEfficiency1(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantEfficiency1")

    @PlantEfficiency1.setter
    def PlantEfficiency1(self, value):
        return self.__setattr__("PlantEfficiency1", value)

    @property
    def PlantEfficiency2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantEfficiency2")

    @PlantEfficiency2.setter
    def PlantEfficiency2(self, value):
        return self.__setattr__("PlantEfficiency2", value)

    @property
    def PlantEfficiency3(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantEfficiency3")

    @PlantEfficiency3.setter
    def PlantEfficiency3(self, value):
        return self.__setattr__("PlantEfficiency3", value)

    @property
    def PlantEfficiency4(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantEfficiency4")

    @PlantEfficiency4.setter
    def PlantEfficiency4(self, value):
        return self.__setattr__("PlantEfficiency4", value)

    @property
    def PlantHash1(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHash1")

    @PlantHash1.setter
    def PlantHash1(self, value):
        return self.__setattr__("PlantHash1", value)

    @property
    def PlantHash2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHash2")

    @PlantHash2.setter
    def PlantHash2(self, value):
        return self.__setattr__("PlantHash2", value)

    @property
    def PlantHash3(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHash3")

    @PlantHash3.setter
    def PlantHash3(self, value):
        return self.__setattr__("PlantHash3", value)

    @property
    def PlantHash4(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHash4")

    @PlantHash4.setter
    def PlantHash4(self, value):
        return self.__setattr__("PlantHash4", value)

    @property
    def RequestHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RequestHash")

    @RequestHash.setter
    def RequestHash(self, value):
        return self.__setattr__("RequestHash", value)

    @property
    def CompletionRatio(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CompletionRatio")

    @CompletionRatio.setter
    def CompletionRatio(self, value):
        return self.__setattr__("CompletionRatio", value)

    @property
    def ClearMemory(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ClearMemory")

    @ClearMemory.setter
    def ClearMemory(self, value):
        return self.__setattr__("ClearMemory", value)

    @property
    def ExportCount(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ExportCount")

    @ExportCount.setter
    def ExportCount(self, value):
        return self.__setattr__("ExportCount", value)

    @property
    def ImportCount(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ImportCount")

    @ImportCount.setter
    def ImportCount(self, value):
        return self.__setattr__("ImportCount", value)

    @property
    def PowerGeneration(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PowerGeneration")

    @PowerGeneration.setter
    def PowerGeneration(self, value):
        return self.__setattr__("PowerGeneration", value)

    @property
    def TotalMoles(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TotalMoles")

    @TotalMoles.setter
    def TotalMoles(self, value):
        return self.__setattr__("TotalMoles", value)

    @property
    def Volume(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Volume")

    @Volume.setter
    def Volume(self, value):
        return self.__setattr__("Volume", value)

    @property
    def Plant(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Plant")

    @Plant.setter
    def Plant(self, value):
        return self.__setattr__("Plant", value)

    @property
    def Harvest(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Harvest")

    @Harvest.setter
    def Harvest(self, value):
        return self.__setattr__("Harvest", value)

    @property
    def Output(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Output")

    @Output.setter
    def Output(self, value):
        return self.__setattr__("Output", value)

    @property
    def PressureSetting(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureSetting")

    @PressureSetting.setter
    def PressureSetting(self, value):
        return self.__setattr__("PressureSetting", value)

    @property
    def TemperatureSetting(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TemperatureSetting")

    @TemperatureSetting.setter
    def TemperatureSetting(self, value):
        return self.__setattr__("TemperatureSetting", value)

    @property
    def TemperatureExternal(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TemperatureExternal")

    @TemperatureExternal.setter
    def TemperatureExternal(self, value):
        return self.__setattr__("TemperatureExternal", value)

    @property
    def Filtration(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Filtration")

    @Filtration.setter
    def Filtration(self, value):
        return self.__setattr__("Filtration", value)

    @property
    def AirRelease(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("AirRelease")

    @AirRelease.setter
    def AirRelease(self, value):
        return self.__setattr__("AirRelease", value)

    @property
    def PositionX(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PositionX")

    @PositionX.setter
    def PositionX(self, value):
        return self.__setattr__("PositionX", value)

    @property
    def PositionY(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PositionY")

    @PositionY.setter
    def PositionY(self, value):
        return self.__setattr__("PositionY", value)

    @property
    def PositionZ(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PositionZ")

    @PositionZ.setter
    def PositionZ(self, value):
        return self.__setattr__("PositionZ", value)

    @property
    def VelocityMagnitude(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("VelocityMagnitude")

    @VelocityMagnitude.setter
    def VelocityMagnitude(self, value):
        return self.__setattr__("VelocityMagnitude", value)

    @property
    def VelocityRelativeX(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("VelocityRelativeX")

    @VelocityRelativeX.setter
    def VelocityRelativeX(self, value):
        return self.__setattr__("VelocityRelativeX", value)

    @property
    def VelocityRelativeY(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("VelocityRelativeY")

    @VelocityRelativeY.setter
    def VelocityRelativeY(self, value):
        return self.__setattr__("VelocityRelativeY", value)

    @property
    def VelocityRelativeZ(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("VelocityRelativeZ")

    @VelocityRelativeZ.setter
    def VelocityRelativeZ(self, value):
        return self.__setattr__("VelocityRelativeZ", value)

    @property
    def RatioNitrousOxide(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrousOxide")

    @RatioNitrousOxide.setter
    def RatioNitrousOxide(self, value):
        return self.__setattr__("RatioNitrousOxide", value)

    @property
    def PrefabHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PrefabHash")

    @PrefabHash.setter
    def PrefabHash(self, value):
        return self.__setattr__("PrefabHash", value)

    @property
    def ForceWrite(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ForceWrite")

    @ForceWrite.setter
    def ForceWrite(self, value):
        return self.__setattr__("ForceWrite", value)

    @property
    def SignalStrength(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SignalStrength")

    @SignalStrength.setter
    def SignalStrength(self, value):
        return self.__setattr__("SignalStrength", value)

    @property
    def SignalID(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SignalID")

    @SignalID.setter
    def SignalID(self, value):
        return self.__setattr__("SignalID", value)

    @property
    def TargetX(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TargetX")

    @TargetX.setter
    def TargetX(self, value):
        return self.__setattr__("TargetX", value)

    @property
    def TargetY(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TargetY")

    @TargetY.setter
    def TargetY(self, value):
        return self.__setattr__("TargetY", value)

    @property
    def TargetZ(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TargetZ")

    @TargetZ.setter
    def TargetZ(self, value):
        return self.__setattr__("TargetZ", value)

    @property
    def SettingInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SettingInput")

    @SettingInput.setter
    def SettingInput(self, value):
        return self.__setattr__("SettingInput", value)

    @property
    def SettingOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SettingOutput")

    @SettingOutput.setter
    def SettingOutput(self, value):
        return self.__setattr__("SettingOutput", value)

    @property
    def CurrentResearchPodType(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CurrentResearchPodType")

    @CurrentResearchPodType.setter
    def CurrentResearchPodType(self, value):
        return self.__setattr__("CurrentResearchPodType", value)

    @property
    def ManualResearchRequiredPod(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ManualResearchRequiredPod")

    @ManualResearchRequiredPod.setter
    def ManualResearchRequiredPod(self, value):
        return self.__setattr__("ManualResearchRequiredPod", value)

    @property
    def MineablesInVicinity(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("MineablesInVicinity")

    @MineablesInVicinity.setter
    def MineablesInVicinity(self, value):
        return self.__setattr__("MineablesInVicinity", value)

    @property
    def MineablesInQueue(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("MineablesInQueue")

    @MineablesInQueue.setter
    def MineablesInQueue(self, value):
        return self.__setattr__("MineablesInQueue", value)

    @property
    def NextWeatherEventTime(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("NextWeatherEventTime")

    @NextWeatherEventTime.setter
    def NextWeatherEventTime(self, value):
        return self.__setattr__("NextWeatherEventTime", value)

    @property
    def Combustion(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Combustion")

    @Combustion.setter
    def Combustion(self, value):
        return self.__setattr__("Combustion", value)

    @property
    def Fuel(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Fuel")

    @Fuel.setter
    def Fuel(self, value):
        return self.__setattr__("Fuel", value)

    @property
    def ReturnFuelCost(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ReturnFuelCost")

    @ReturnFuelCost.setter
    def ReturnFuelCost(self, value):
        return self.__setattr__("ReturnFuelCost", value)

    @property
    def CollectableGoods(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CollectableGoods")

    @CollectableGoods.setter
    def CollectableGoods(self, value):
        return self.__setattr__("CollectableGoods", value)

    @property
    def Time(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Time")

    @Time.setter
    def Time(self, value):
        return self.__setattr__("Time", value)

    @property
    def Bpm(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Bpm")

    @Bpm.setter
    def Bpm(self, value):
        return self.__setattr__("Bpm", value)

    @property
    def EnvironmentEfficiency(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("EnvironmentEfficiency")

    @EnvironmentEfficiency.setter
    def EnvironmentEfficiency(self, value):
        return self.__setattr__("EnvironmentEfficiency", value)

    @property
    def WorkingGasEfficiency(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("WorkingGasEfficiency")

    @WorkingGasEfficiency.setter
    def WorkingGasEfficiency(self, value):
        return self.__setattr__("WorkingGasEfficiency", value)

    @property
    def PressureInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureInput")

    @PressureInput.setter
    def PressureInput(self, value):
        return self.__setattr__("PressureInput", value)

    @property
    def TemperatureInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TemperatureInput")

    @TemperatureInput.setter
    def TemperatureInput(self, value):
        return self.__setattr__("TemperatureInput", value)

    @property
    def RatioOxygenInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioOxygenInput")

    @RatioOxygenInput.setter
    def RatioOxygenInput(self, value):
        return self.__setattr__("RatioOxygenInput", value)

    @property
    def RatioCarbonDioxideInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioCarbonDioxideInput")

    @RatioCarbonDioxideInput.setter
    def RatioCarbonDioxideInput(self, value):
        return self.__setattr__("RatioCarbonDioxideInput", value)

    @property
    def RatioNitrogenInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrogenInput")

    @RatioNitrogenInput.setter
    def RatioNitrogenInput(self, value):
        return self.__setattr__("RatioNitrogenInput", value)

    @property
    def RatioPollutantInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioPollutantInput")

    @RatioPollutantInput.setter
    def RatioPollutantInput(self, value):
        return self.__setattr__("RatioPollutantInput", value)

    @property
    def RatioVolatilesInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioVolatilesInput")

    @RatioVolatilesInput.setter
    def RatioVolatilesInput(self, value):
        return self.__setattr__("RatioVolatilesInput", value)

    @property
    def RatioWaterInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioWaterInput")

    @RatioWaterInput.setter
    def RatioWaterInput(self, value):
        return self.__setattr__("RatioWaterInput", value)

    @property
    def RatioNitrousOxideInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrousOxideInput")

    @RatioNitrousOxideInput.setter
    def RatioNitrousOxideInput(self, value):
        return self.__setattr__("RatioNitrousOxideInput", value)

    @property
    def TotalMolesInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TotalMolesInput")

    @TotalMolesInput.setter
    def TotalMolesInput(self, value):
        return self.__setattr__("TotalMolesInput", value)

    @property
    def PressureInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureInput2")

    @PressureInput2.setter
    def PressureInput2(self, value):
        return self.__setattr__("PressureInput2", value)

    @property
    def TemperatureInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TemperatureInput2")

    @TemperatureInput2.setter
    def TemperatureInput2(self, value):
        return self.__setattr__("TemperatureInput2", value)

    @property
    def RatioOxygenInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioOxygenInput2")

    @RatioOxygenInput2.setter
    def RatioOxygenInput2(self, value):
        return self.__setattr__("RatioOxygenInput2", value)

    @property
    def RatioCarbonDioxideInput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioCarbonDioxideInput2")

    @RatioCarbonDioxideInput2.setter
    def RatioCarbonDioxideInput2(self, value):
        return self.__setattr__("RatioCarbonDioxideInput2", value)

    @property
    def RatioNitrogenInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrogenInput2")

    @RatioNitrogenInput2.setter
    def RatioNitrogenInput2(self, value):
        return self.__setattr__("RatioNitrogenInput2", value)

    @property
    def RatioPollutantInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioPollutantInput2")

    @RatioPollutantInput2.setter
    def RatioPollutantInput2(self, value):
        return self.__setattr__("RatioPollutantInput2", value)

    @property
    def RatioVolatilesInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioVolatilesInput2")

    @RatioVolatilesInput2.setter
    def RatioVolatilesInput2(self, value):
        return self.__setattr__("RatioVolatilesInput2", value)

    @property
    def RatioWaterInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioWaterInput2")

    @RatioWaterInput2.setter
    def RatioWaterInput2(self, value):
        return self.__setattr__("RatioWaterInput2", value)

    @property
    def RatioNitrousOxideInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrousOxideInput2")

    @RatioNitrousOxideInput2.setter
    def RatioNitrousOxideInput2(self, value):
        return self.__setattr__("RatioNitrousOxideInput2", value)

    @property
    def TotalMolesInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TotalMolesInput2")

    @TotalMolesInput2.setter
    def TotalMolesInput2(self, value):
        return self.__setattr__("TotalMolesInput2", value)

    @property
    def PressureOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureOutput")

    @PressureOutput.setter
    def PressureOutput(self, value):
        return self.__setattr__("PressureOutput", value)

    @property
    def TemperatureOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TemperatureOutput")

    @TemperatureOutput.setter
    def TemperatureOutput(self, value):
        return self.__setattr__("TemperatureOutput", value)

    @property
    def RatioOxygenOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioOxygenOutput")

    @RatioOxygenOutput.setter
    def RatioOxygenOutput(self, value):
        return self.__setattr__("RatioOxygenOutput", value)

    @property
    def RatioCarbonDioxideOutput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioCarbonDioxideOutput")

    @RatioCarbonDioxideOutput.setter
    def RatioCarbonDioxideOutput(self, value):
        return self.__setattr__("RatioCarbonDioxideOutput", value)

    @property
    def RatioNitrogenOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrogenOutput")

    @RatioNitrogenOutput.setter
    def RatioNitrogenOutput(self, value):
        return self.__setattr__("RatioNitrogenOutput", value)

    @property
    def RatioPollutantOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioPollutantOutput")

    @RatioPollutantOutput.setter
    def RatioPollutantOutput(self, value):
        return self.__setattr__("RatioPollutantOutput", value)

    @property
    def RatioVolatilesOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioVolatilesOutput")

    @RatioVolatilesOutput.setter
    def RatioVolatilesOutput(self, value):
        return self.__setattr__("RatioVolatilesOutput", value)

    @property
    def RatioWaterOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioWaterOutput")

    @RatioWaterOutput.setter
    def RatioWaterOutput(self, value):
        return self.__setattr__("RatioWaterOutput", value)

    @property
    def RatioNitrousOxideOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrousOxideOutput")

    @RatioNitrousOxideOutput.setter
    def RatioNitrousOxideOutput(self, value):
        return self.__setattr__("RatioNitrousOxideOutput", value)

    @property
    def TotalMolesOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TotalMolesOutput")

    @TotalMolesOutput.setter
    def TotalMolesOutput(self, value):
        return self.__setattr__("TotalMolesOutput", value)

    @property
    def PressureOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureOutput2")

    @PressureOutput2.setter
    def PressureOutput2(self, value):
        return self.__setattr__("PressureOutput2", value)

    @property
    def TemperatureOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TemperatureOutput2")

    @TemperatureOutput2.setter
    def TemperatureOutput2(self, value):
        return self.__setattr__("TemperatureOutput2", value)

    @property
    def RatioOxygenOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioOxygenOutput2")

    @RatioOxygenOutput2.setter
    def RatioOxygenOutput2(self, value):
        return self.__setattr__("RatioOxygenOutput2", value)

    @property
    def RatioCarbonDioxideOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioCarbonDioxideOutput2")

    @RatioCarbonDioxideOutput2.setter
    def RatioCarbonDioxideOutput2(self, value):
        return self.__setattr__("RatioCarbonDioxideOutput2", value)

    @property
    def RatioNitrogenOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrogenOutput2")

    @RatioNitrogenOutput2.setter
    def RatioNitrogenOutput2(self, value):
        return self.__setattr__("RatioNitrogenOutput2", value)

    @property
    def RatioPollutantOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioPollutantOutput2")

    @RatioPollutantOutput2.setter
    def RatioPollutantOutput2(self, value):
        return self.__setattr__("RatioPollutantOutput2", value)

    @property
    def RatioVolatilesOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioVolatilesOutput2")

    @RatioVolatilesOutput2.setter
    def RatioVolatilesOutput2(self, value):
        return self.__setattr__("RatioVolatilesOutput2", value)

    @property
    def RatioWaterOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioWaterOutput2")

    @RatioWaterOutput2.setter
    def RatioWaterOutput2(self, value):
        return self.__setattr__("RatioWaterOutput2", value)

    @property
    def RatioNitrousOxideOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrousOxideOutput2")

    @RatioNitrousOxideOutput2.setter
    def RatioNitrousOxideOutput2(self, value):
        return self.__setattr__("RatioNitrousOxideOutput2", value)

    @property
    def TotalMolesOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TotalMolesOutput2")

    @TotalMolesOutput2.setter
    def TotalMolesOutput2(self, value):
        return self.__setattr__("TotalMolesOutput2", value)

    @property
    def CombustionInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CombustionInput")

    @CombustionInput.setter
    def CombustionInput(self, value):
        return self.__setattr__("CombustionInput", value)

    @property
    def CombustionInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CombustionInput2")

    @CombustionInput2.setter
    def CombustionInput2(self, value):
        return self.__setattr__("CombustionInput2", value)

    @property
    def CombustionOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CombustionOutput")

    @CombustionOutput.setter
    def CombustionOutput(self, value):
        return self.__setattr__("CombustionOutput", value)

    @property
    def CombustionOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CombustionOutput2")

    @CombustionOutput2.setter
    def CombustionOutput2(self, value):
        return self.__setattr__("CombustionOutput2", value)

    @property
    def OperationalTemperatureEfficiency(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("OperationalTemperatureEfficiency")

    @OperationalTemperatureEfficiency.setter
    def OperationalTemperatureEfficiency(self, value):
        return self.__setattr__("OperationalTemperatureEfficiency", value)

    @property
    def TemperatureDifferentialEfficiency(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TemperatureDifferentialEfficiency")

    @TemperatureDifferentialEfficiency.setter
    def TemperatureDifferentialEfficiency(self, value):
        return self.__setattr__("TemperatureDifferentialEfficiency", value)

    @property
    def PressureEfficiency(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureEfficiency")

    @PressureEfficiency.setter
    def PressureEfficiency(self, value):
        return self.__setattr__("PressureEfficiency", value)

    @property
    def CombustionLimiter(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CombustionLimiter")

    @CombustionLimiter.setter
    def CombustionLimiter(self, value):
        return self.__setattr__("CombustionLimiter", value)

    @property
    def Throttle(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Throttle")

    @Throttle.setter
    def Throttle(self, value):
        return self.__setattr__("Throttle", value)

    @property
    def Rpm(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Rpm")

    @Rpm.setter
    def Rpm(self, value):
        return self.__setattr__("Rpm", value)

    @property
    def Stress(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Stress")

    @Stress.setter
    def Stress(self, value):
        return self.__setattr__("Stress", value)

    @property
    def InterrogationProgress(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("InterrogationProgress")

    @InterrogationProgress.setter
    def InterrogationProgress(self, value):
        return self.__setattr__("InterrogationProgress", value)

    @property
    def TargetPadIndex(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TargetPadIndex")

    @TargetPadIndex.setter
    def TargetPadIndex(self, value):
        return self.__setattr__("TargetPadIndex", value)

    @property
    def SizeX(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SizeX")

    @SizeX.setter
    def SizeX(self, value):
        return self.__setattr__("SizeX", value)

    @property
    def SizeY(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SizeY")

    @SizeY.setter
    def SizeY(self, value):
        return self.__setattr__("SizeY", value)

    @property
    def SizeZ(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SizeZ")

    @SizeZ.setter
    def SizeZ(self, value):
        return self.__setattr__("SizeZ", value)

    @property
    def MinimumWattsToContact(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("MinimumWattsToContact")

    @MinimumWattsToContact.setter
    def MinimumWattsToContact(self, value):
        return self.__setattr__("MinimumWattsToContact", value)

    @property
    def WattsReachingContact(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("WattsReachingContact")

    @WattsReachingContact.setter
    def WattsReachingContact(self, value):
        return self.__setattr__("WattsReachingContact", value)

    @property
    def Channel0(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Channel0")

    @Channel0.setter
    def Channel0(self, value):
        return self.__setattr__("Channel0", value)

    @property
    def Channel1(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Channel1")

    @Channel1.setter
    def Channel1(self, value):
        return self.__setattr__("Channel1", value)

    @property
    def Channel2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Channel2")

    @Channel2.setter
    def Channel2(self, value):
        return self.__setattr__("Channel2", value)

    @property
    def Channel3(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Channel3")

    @Channel3.setter
    def Channel3(self, value):
        return self.__setattr__("Channel3", value)

    @property
    def Channel4(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Channel4")

    @Channel4.setter
    def Channel4(self, value):
        return self.__setattr__("Channel4", value)

    @property
    def Channel5(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Channel5")

    @Channel5.setter
    def Channel5(self, value):
        return self.__setattr__("Channel5", value)

    @property
    def Channel6(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Channel6")

    @Channel6.setter
    def Channel6(self, value):
        return self.__setattr__("Channel6", value)

    @property
    def Channel7(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Channel7")

    @Channel7.setter
    def Channel7(self, value):
        return self.__setattr__("Channel7", value)

    @property
    def LineNumber(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("LineNumber")

    @LineNumber.setter
    def LineNumber(self, value):
        return self.__setattr__("LineNumber", value)

    @property
    def Flush(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Flush")

    @Flush.setter
    def Flush(self, value):
        return self.__setattr__("Flush", value)

    @property
    def SoundAlert(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SoundAlert")

    @SoundAlert.setter
    def SoundAlert(self, value):
        return self.__setattr__("SoundAlert", value)

    @property
    def SolarIrradiance(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SolarIrradiance")

    @SolarIrradiance.setter
    def SolarIrradiance(self, value):
        return self.__setattr__("SolarIrradiance", value)

    @property
    def RatioLiquidNitrogen(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrogen")

    @RatioLiquidNitrogen.setter
    def RatioLiquidNitrogen(self, value):
        return self.__setattr__("RatioLiquidNitrogen", value)

    @property
    def RatioLiquidNitrogenInput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrogenInput")

    @RatioLiquidNitrogenInput.setter
    def RatioLiquidNitrogenInput(self, value):
        return self.__setattr__("RatioLiquidNitrogenInput", value)

    @property
    def RatioLiquidNitrogenInput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrogenInput2")

    @RatioLiquidNitrogenInput2.setter
    def RatioLiquidNitrogenInput2(self, value):
        return self.__setattr__("RatioLiquidNitrogenInput2", value)

    @property
    def RatioLiquidNitrogenOutput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrogenOutput")

    @RatioLiquidNitrogenOutput.setter
    def RatioLiquidNitrogenOutput(self, value):
        return self.__setattr__("RatioLiquidNitrogenOutput", value)

    @property
    def RatioLiquidNitrogenOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrogenOutput2")

    @RatioLiquidNitrogenOutput2.setter
    def RatioLiquidNitrogenOutput2(self, value):
        return self.__setattr__("RatioLiquidNitrogenOutput2", value)

    @property
    def VolumeOfLiquid(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("VolumeOfLiquid")

    @VolumeOfLiquid.setter
    def VolumeOfLiquid(self, value):
        return self.__setattr__("VolumeOfLiquid", value)

    @property
    def RatioLiquidOxygen(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidOxygen")

    @RatioLiquidOxygen.setter
    def RatioLiquidOxygen(self, value):
        return self.__setattr__("RatioLiquidOxygen", value)

    @property
    def RatioLiquidOxygenInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidOxygenInput")

    @RatioLiquidOxygenInput.setter
    def RatioLiquidOxygenInput(self, value):
        return self.__setattr__("RatioLiquidOxygenInput", value)

    @property
    def RatioLiquidOxygenInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidOxygenInput2")

    @RatioLiquidOxygenInput2.setter
    def RatioLiquidOxygenInput2(self, value):
        return self.__setattr__("RatioLiquidOxygenInput2", value)

    @property
    def RatioLiquidOxygenOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidOxygenOutput")

    @RatioLiquidOxygenOutput.setter
    def RatioLiquidOxygenOutput(self, value):
        return self.__setattr__("RatioLiquidOxygenOutput", value)

    @property
    def RatioLiquidOxygenOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidOxygenOutput2")

    @RatioLiquidOxygenOutput2.setter
    def RatioLiquidOxygenOutput2(self, value):
        return self.__setattr__("RatioLiquidOxygenOutput2", value)

    @property
    def RatioLiquidVolatiles(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidVolatiles")

    @RatioLiquidVolatiles.setter
    def RatioLiquidVolatiles(self, value):
        return self.__setattr__("RatioLiquidVolatiles", value)

    @property
    def RatioLiquidVolatilesInput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidVolatilesInput")

    @RatioLiquidVolatilesInput.setter
    def RatioLiquidVolatilesInput(self, value):
        return self.__setattr__("RatioLiquidVolatilesInput", value)

    @property
    def RatioLiquidVolatilesInput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidVolatilesInput2")

    @RatioLiquidVolatilesInput2.setter
    def RatioLiquidVolatilesInput2(self, value):
        return self.__setattr__("RatioLiquidVolatilesInput2", value)

    @property
    def RatioLiquidVolatilesOutput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidVolatilesOutput")

    @RatioLiquidVolatilesOutput.setter
    def RatioLiquidVolatilesOutput(self, value):
        return self.__setattr__("RatioLiquidVolatilesOutput", value)

    @property
    def RatioLiquidVolatilesOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidVolatilesOutput2")

    @RatioLiquidVolatilesOutput2.setter
    def RatioLiquidVolatilesOutput2(self, value):
        return self.__setattr__("RatioLiquidVolatilesOutput2", value)

    @property
    def RatioSteam(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioSteam")

    @RatioSteam.setter
    def RatioSteam(self, value):
        return self.__setattr__("RatioSteam", value)

    @property
    def RatioSteamInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioSteamInput")

    @RatioSteamInput.setter
    def RatioSteamInput(self, value):
        return self.__setattr__("RatioSteamInput", value)

    @property
    def RatioSteamInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioSteamInput2")

    @RatioSteamInput2.setter
    def RatioSteamInput2(self, value):
        return self.__setattr__("RatioSteamInput2", value)

    @property
    def RatioSteamOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioSteamOutput")

    @RatioSteamOutput.setter
    def RatioSteamOutput(self, value):
        return self.__setattr__("RatioSteamOutput", value)

    @property
    def RatioSteamOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioSteamOutput2")

    @RatioSteamOutput2.setter
    def RatioSteamOutput2(self, value):
        return self.__setattr__("RatioSteamOutput2", value)

    @property
    def ContactTypeId(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ContactTypeId")

    @ContactTypeId.setter
    def ContactTypeId(self, value):
        return self.__setattr__("ContactTypeId", value)

    @property
    def RatioLiquidCarbonDioxide(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxide")

    @RatioLiquidCarbonDioxide.setter
    def RatioLiquidCarbonDioxide(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxide", value)

    @property
    def RatioLiquidCarbonDioxideInput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideInput")

    @RatioLiquidCarbonDioxideInput.setter
    def RatioLiquidCarbonDioxideInput(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideInput", value)

    @property
    def RatioLiquidCarbonDioxideInput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideInput2")

    @RatioLiquidCarbonDioxideInput2.setter
    def RatioLiquidCarbonDioxideInput2(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideInput2", value)

    @property
    def RatioLiquidCarbonDioxideOutput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideOutput")

    @RatioLiquidCarbonDioxideOutput.setter
    def RatioLiquidCarbonDioxideOutput(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideOutput", value)

    @property
    def RatioLiquidCarbonDioxideOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideOutput2")

    @RatioLiquidCarbonDioxideOutput2.setter
    def RatioLiquidCarbonDioxideOutput2(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideOutput2", value)

    @property
    def RatioLiquidPollutant(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidPollutant")

    @RatioLiquidPollutant.setter
    def RatioLiquidPollutant(self, value):
        return self.__setattr__("RatioLiquidPollutant", value)

    @property
    def RatioLiquidPollutantInput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidPollutantInput")

    @RatioLiquidPollutantInput.setter
    def RatioLiquidPollutantInput(self, value):
        return self.__setattr__("RatioLiquidPollutantInput", value)

    @property
    def RatioLiquidPollutantInput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidPollutantInput2")

    @RatioLiquidPollutantInput2.setter
    def RatioLiquidPollutantInput2(self, value):
        return self.__setattr__("RatioLiquidPollutantInput2", value)

    @property
    def RatioLiquidPollutantOutput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidPollutantOutput")

    @RatioLiquidPollutantOutput.setter
    def RatioLiquidPollutantOutput(self, value):
        return self.__setattr__("RatioLiquidPollutantOutput", value)

    @property
    def RatioLiquidPollutantOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidPollutantOutput2")

    @RatioLiquidPollutantOutput2.setter
    def RatioLiquidPollutantOutput2(self, value):
        return self.__setattr__("RatioLiquidPollutantOutput2", value)

    @property
    def RatioLiquidNitrousOxide(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrousOxide")

    @RatioLiquidNitrousOxide.setter
    def RatioLiquidNitrousOxide(self, value):
        return self.__setattr__("RatioLiquidNitrousOxide", value)

    @property
    def RatioLiquidNitrousOxideInput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideInput")

    @RatioLiquidNitrousOxideInput.setter
    def RatioLiquidNitrousOxideInput(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideInput", value)

    @property
    def RatioLiquidNitrousOxideInput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideInput2")

    @RatioLiquidNitrousOxideInput2.setter
    def RatioLiquidNitrousOxideInput2(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideInput2", value)

    @property
    def RatioLiquidNitrousOxideOutput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideOutput")

    @RatioLiquidNitrousOxideOutput.setter
    def RatioLiquidNitrousOxideOutput(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideOutput", value)

    @property
    def RatioLiquidNitrousOxideOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideOutput2")

    @RatioLiquidNitrousOxideOutput2.setter
    def RatioLiquidNitrousOxideOutput2(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideOutput2", value)

    @property
    def Progress(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Progress")

    @Progress.setter
    def Progress(self, value):
        return self.__setattr__("Progress", value)

    @property
    def DestinationCode(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("DestinationCode")

    @DestinationCode.setter
    def DestinationCode(self, value):
        return self.__setattr__("DestinationCode", value)

    @property
    def Acceleration(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Acceleration")

    @Acceleration.setter
    def Acceleration(self, value):
        return self.__setattr__("Acceleration", value)

    @property
    def ReferenceId(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ReferenceId")

    @ReferenceId.setter
    def ReferenceId(self, value):
        return self.__setattr__("ReferenceId", value)

    @property
    def AutoShutOff(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("AutoShutOff")

    @AutoShutOff.setter
    def AutoShutOff(self, value):
        return self.__setattr__("AutoShutOff", value)

    @property
    def Mass(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Mass")

    @Mass.setter
    def Mass(self, value):
        return self.__setattr__("Mass", value)

    @property
    def DryMass(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("DryMass")

    @DryMass.setter
    def DryMass(self, value):
        return self.__setattr__("DryMass", value)

    @property
    def Thrust(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Thrust")

    @Thrust.setter
    def Thrust(self, value):
        return self.__setattr__("Thrust", value)

    @property
    def Weight(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Weight")

    @Weight.setter
    def Weight(self, value):
        return self.__setattr__("Weight", value)

    @property
    def ThrustToWeight(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ThrustToWeight")

    @ThrustToWeight.setter
    def ThrustToWeight(self, value):
        return self.__setattr__("ThrustToWeight", value)

    @property
    def TimeToDestination(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TimeToDestination")

    @TimeToDestination.setter
    def TimeToDestination(self, value):
        return self.__setattr__("TimeToDestination", value)

    @property
    def BurnTimeRemaining(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("BurnTimeRemaining")

    @BurnTimeRemaining.setter
    def BurnTimeRemaining(self, value):
        return self.__setattr__("BurnTimeRemaining", value)

    @property
    def AutoLand(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("AutoLand")

    @AutoLand.setter
    def AutoLand(self, value):
        return self.__setattr__("AutoLand", value)

    @property
    def ForwardX(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ForwardX")

    @ForwardX.setter
    def ForwardX(self, value):
        return self.__setattr__("ForwardX", value)

    @property
    def ForwardY(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ForwardY")

    @ForwardY.setter
    def ForwardY(self, value):
        return self.__setattr__("ForwardY", value)

    @property
    def ForwardZ(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ForwardZ")

    @ForwardZ.setter
    def ForwardZ(self, value):
        return self.__setattr__("ForwardZ", value)

    @property
    def Orientation(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Orientation")

    @Orientation.setter
    def Orientation(self, value):
        return self.__setattr__("Orientation", value)

    @property
    def VelocityX(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("VelocityX")

    @VelocityX.setter
    def VelocityX(self, value):
        return self.__setattr__("VelocityX", value)

    @property
    def VelocityY(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("VelocityY")

    @VelocityY.setter
    def VelocityY(self, value):
        return self.__setattr__("VelocityY", value)

    @property
    def VelocityZ(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("VelocityZ")

    @VelocityZ.setter
    def VelocityZ(self, value):
        return self.__setattr__("VelocityZ", value)

    @property
    def PassedMoles(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PassedMoles")

    @PassedMoles.setter
    def PassedMoles(self, value):
        return self.__setattr__("PassedMoles", value)

    @property
    def ExhaustVelocity(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ExhaustVelocity")

    @ExhaustVelocity.setter
    def ExhaustVelocity(self, value):
        return self.__setattr__("ExhaustVelocity", value)

    @property
    def FlightControlRule(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("FlightControlRule")

    @FlightControlRule.setter
    def FlightControlRule(self, value):
        return self.__setattr__("FlightControlRule", value)

    @property
    def ReEntryAltitude(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ReEntryAltitude")

    @ReEntryAltitude.setter
    def ReEntryAltitude(self, value):
        return self.__setattr__("ReEntryAltitude", value)

    @property
    def Apex(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Apex")

    @Apex.setter
    def Apex(self, value):
        return self.__setattr__("Apex", value)

    @property
    def EntityState(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("EntityState")

    @EntityState.setter
    def EntityState(self, value):
        return self.__setattr__("EntityState", value)

    @property
    def DrillCondition(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("DrillCondition")

    @DrillCondition.setter
    def DrillCondition(self, value):
        return self.__setattr__("DrillCondition", value)

    @property
    def Index(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Index")

    @Index.setter
    def Index(self, value):
        return self.__setattr__("Index", value)

    @property
    def CelestialHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CelestialHash")

    @CelestialHash.setter
    def CelestialHash(self, value):
        return self.__setattr__("CelestialHash", value)

    @property
    def AlignmentError(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("AlignmentError")

    @AlignmentError.setter
    def AlignmentError(self, value):
        return self.__setattr__("AlignmentError", value)

    @property
    def DistanceAu(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("DistanceAu")

    @DistanceAu.setter
    def DistanceAu(self, value):
        return self.__setattr__("DistanceAu", value)

    @property
    def OrbitPeriod(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("OrbitPeriod")

    @OrbitPeriod.setter
    def OrbitPeriod(self, value):
        return self.__setattr__("OrbitPeriod", value)

    @property
    def Inclination(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Inclination")

    @Inclination.setter
    def Inclination(self, value):
        return self.__setattr__("Inclination", value)

    @property
    def Eccentricity(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Eccentricity")

    @Eccentricity.setter
    def Eccentricity(self, value):
        return self.__setattr__("Eccentricity", value)

    @property
    def SemiMajorAxis(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SemiMajorAxis")

    @SemiMajorAxis.setter
    def SemiMajorAxis(self, value):
        return self.__setattr__("SemiMajorAxis", value)

    @property
    def DistanceKm(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("DistanceKm")

    @DistanceKm.setter
    def DistanceKm(self, value):
        return self.__setattr__("DistanceKm", value)

    @property
    def CelestialParentHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CelestialParentHash")

    @CelestialParentHash.setter
    def CelestialParentHash(self, value):
        return self.__setattr__("CelestialParentHash", value)

    @property
    def TrueAnomaly(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TrueAnomaly")

    @TrueAnomaly.setter
    def TrueAnomaly(self, value):
        return self.__setattr__("TrueAnomaly", value)

    @property
    def RatioHydrogen(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioHydrogen")

    @RatioHydrogen.setter
    def RatioHydrogen(self, value):
        return self.__setattr__("RatioHydrogen", value)

    @property
    def RatioLiquidHydrogen(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidHydrogen")

    @RatioLiquidHydrogen.setter
    def RatioLiquidHydrogen(self, value):
        return self.__setattr__("RatioLiquidHydrogen", value)

    @property
    def RatioPollutedWater(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioPollutedWater")

    @RatioPollutedWater.setter
    def RatioPollutedWater(self, value):
        return self.__setattr__("RatioPollutedWater", value)

    @property
    def Discover(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Discover")

    @Discover.setter
    def Discover(self, value):
        return self.__setattr__("Discover", value)

    @property
    def Chart(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Chart")

    @Chart.setter
    def Chart(self, value):
        return self.__setattr__("Chart", value)

    @property
    def Survey(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Survey")

    @Survey.setter
    def Survey(self, value):
        return self.__setattr__("Survey", value)

    @property
    def NavPoints(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("NavPoints")

    @NavPoints.setter
    def NavPoints(self, value):
        return self.__setattr__("NavPoints", value)

    @property
    def ChartedNavPoints(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ChartedNavPoints")

    @ChartedNavPoints.setter
    def ChartedNavPoints(self, value):
        return self.__setattr__("ChartedNavPoints", value)

    @property
    def Sites(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Sites")

    @Sites.setter
    def Sites(self, value):
        return self.__setattr__("Sites", value)

    @property
    def CurrentCode(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CurrentCode")

    @CurrentCode.setter
    def CurrentCode(self, value):
        return self.__setattr__("CurrentCode", value)

    @property
    def Density(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Density")

    @Density.setter
    def Density(self, value):
        return self.__setattr__("Density", value)

    @property
    def Richness(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Richness")

    @Richness.setter
    def Richness(self, value):
        return self.__setattr__("Richness", value)

    @property
    def Size(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Size")

    @Size.setter
    def Size(self, value):
        return self.__setattr__("Size", value)

    @property
    def TotalQuantity(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TotalQuantity")

    @TotalQuantity.setter
    def TotalQuantity(self, value):
        return self.__setattr__("TotalQuantity", value)

    @property
    def MinedQuantity(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("MinedQuantity")

    @MinedQuantity.setter
    def MinedQuantity(self, value):
        return self.__setattr__("MinedQuantity", value)

    @property
    def BestContactFilter(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("BestContactFilter")

    @BestContactFilter.setter
    def BestContactFilter(self, value):
        return self.__setattr__("BestContactFilter", value)

    @property
    def NameHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("NameHash")

    @NameHash.setter
    def NameHash(self, value):
        return self.__setattr__("NameHash", value)

    @property
    def Altitude(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Altitude")

    @Altitude.setter
    def Altitude(self, value):
        return self.__setattr__("Altitude", value)

    @property
    def TargetSlotIndex(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TargetSlotIndex")

    @TargetSlotIndex.setter
    def TargetSlotIndex(self, value):
        return self.__setattr__("TargetSlotIndex", value)

    @property
    def TargetPrefabHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TargetPrefabHash")

    @TargetPrefabHash.setter
    def TargetPrefabHash(self, value):
        return self.__setattr__("TargetPrefabHash", value)

    @property
    def Extended(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Extended")

    @Extended.setter
    def Extended(self, value):
        return self.__setattr__("Extended", value)

    @property
    def NetworkFault(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("NetworkFault")

    @NetworkFault.setter
    def NetworkFault(self, value):
        return self.__setattr__("NetworkFault", value)

    @property
    def ProportionalGain(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ProportionalGain")

    @ProportionalGain.setter
    def ProportionalGain(self, value):
        return self.__setattr__("ProportionalGain", value)

    @property
    def IntegralGain(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("IntegralGain")

    @IntegralGain.setter
    def IntegralGain(self, value):
        return self.__setattr__("IntegralGain", value)

    @property
    def DerivativeGain(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("DerivativeGain")

    @DerivativeGain.setter
    def DerivativeGain(self, value):
        return self.__setattr__("DerivativeGain", value)

    @property
    def Minimum(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Minimum")

    @Minimum.setter
    def Minimum(self, value):
        return self.__setattr__("Minimum", value)

    @property
    def Setpoint(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Setpoint")

    @Setpoint.setter
    def Setpoint(self, value):
        return self.__setattr__("Setpoint", value)

    @property
    def Reset(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Reset")

    @Reset.setter
    def Reset(self, value):
        return self.__setattr__("Reset", value)

    @property
    def StackSize(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("StackSize")

    @StackSize.setter
    def StackSize(self, value):
        return self.__setattr__("StackSize", value)
