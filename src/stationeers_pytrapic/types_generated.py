import enum


class _logicType(enum.StrEnum):
    None_ = "None"
    Power = "Power"
    Open = "Open"
    Mode = "Mode"
    Error = "Error"
    Flush = "Flush"
    SoundAlert = "SoundAlert"
    VolumeOfLiquid = "VolumeOfLiquid"
    Lock = "Lock"
    Pressure = "Pressure"
    Temperature = "Temperature"
    PressureInput = "PressureInput"
    TemperatureInput = "TemperatureInput"
    PressureInput2 = "PressureInput2"
    TemperatureInput2 = "TemperatureInput2"
    PressureOutput = "PressureOutput"
    TargetPadIndex = "TargetPadIndex"
    InterrogationProgress = "InterrogationProgress"
    SizeX = "SizeX"
    SizeY = "SizeY"
    SizeZ = "SizeZ"
    MinWattsToContact = "MinWattsToContact"
    WattsReachingContact = "WattsReachingContact"
    LineNumber = "LineNumber"
    TemperatureOutput = "TemperatureOutput"
    PressureOutput2 = "PressureOutput2"
    TemperatureOutput2 = "TemperatureOutput2"
    PressureExternal = "PressureExternal"
    PressureInternal = "PressureInternal"
    Activate = "Activate"
    Charge = "Charge"
    Setting = "Setting"
    Reagents = "Reagents"
    RatioOxygen = "RatioOxygen"
    RatioCarbonDioxide = "RatioCarbonDioxide"
    RatioNitrogen = "RatioNitrogen"
    RatioPollutant = "RatioPollutant"
    RatioVolatiles = "RatioVolatiles"
    RatioWater = "RatioWater"
    RatioPollutedWater = "RatioPollutedWater"
    RatioNitrousOxide = "RatioNitrousOxide"
    RatioLiquidNitrogen = "RatioLiquidNitrogen"
    Combustion = "Combustion"
    RatioOxygenInput = "RatioOxygenInput"
    RatioCarbonDioxideInput = "RatioCarbonDioxideInput"
    RatioNitrogenInput = "RatioNitrogenInput"
    RatioPollutantInput = "RatioPollutantInput"
    RatioVolatilesInput = "RatioVolatilesInput"
    RatioWaterInput = "RatioWaterInput"
    RatioNitrousOxideInput = "RatioNitrousOxideInput"
    RatioLiquidNitrogenInput = "RatioLiquidNitrogenInput"
    CombustionInput = "CombustionInput"
    RatioOxygenInput2 = "RatioOxygenInput2"
    RatioCarbonDioxideInput2 = "RatioCarbonDioxideInput2"
    RatioNitrogenInput2 = "RatioNitrogenInput2"
    RatioPollutantInput2 = "RatioPollutantInput2"
    RatioVolatilesInput2 = "RatioVolatilesInput2"
    RatioWaterInput2 = "RatioWaterInput2"
    RatioNitrousOxideInput2 = "RatioNitrousOxideInput2"
    RatioLiquidNitrogenInput2 = "RatioLiquidNitrogenInput2"
    CombustionInput2 = "CombustionInput2"
    RatioOxygenOutput = "RatioOxygenOutput"
    RatioCarbonDioxideOutput = "RatioCarbonDioxideOutput"
    RatioNitrogenOutput = "RatioNitrogenOutput"
    RatioPollutantOutput = "RatioPollutantOutput"
    RatioVolatilesOutput = "RatioVolatilesOutput"
    RatioWaterOutput = "RatioWaterOutput"
    RatioNitrousOxideOutput = "RatioNitrousOxideOutput"
    RatioLiquidNitrogenOutput = "RatioLiquidNitrogenOutput"
    CombustionOutput = "CombustionOutput"
    RatioOxygenOutput2 = "RatioOxygenOutput2"
    RatioCarbonDioxideOutput2 = "RatioCarbonDioxideOutput2"
    RatioNitrogenOutput2 = "RatioNitrogenOutput2"
    RatioPollutantOutput2 = "RatioPollutantOutput2"
    RatioVolatilesOutput2 = "RatioVolatilesOutput2"
    RatioWaterOutput2 = "RatioWaterOutput2"
    RatioNitrousOxideOutput2 = "RatioNitrousOxideOutput2"
    RatioLiquidNitrogenOutput2 = "RatioLiquidNitrogenOutput2"
    CombustionOutput2 = "CombustionOutput2"
    Horizontal = "Horizontal"
    Vertical = "Vertical"
    SolarAngle = "SolarAngle"
    SolarConstant = "SolarConstant"
    Maximum = "Maximum"
    Ratio = "Ratio"
    PowerPotential = "PowerPotential"
    PowerActual = "PowerActual"
    Quantity = "Quantity"
    On = "On"
    ImportQuantity = "ImportQuantity"
    ImportSlotOccupant = "ImportSlotOccupant"
    ExportQuantity = "ExportQuantity"
    ExportSlotOccupant = "ExportSlotOccupant"
    RequiredPower = "RequiredPower"
    HorizontalRatio = "HorizontalRatio"
    VerticalRatio = "VerticalRatio"
    PowerRequired = "PowerRequired"
    Idle = "Idle"
    Color = "Color"
    ElevatorSpeed = "ElevatorSpeed"
    ElevatorLevel = "ElevatorLevel"
    RecipeHash = "RecipeHash"
    ExportSlotHash = "ExportSlotHash"
    ImportSlotHash = "ImportSlotHash"
    PlantHealth1 = "PlantHealth1"
    PlantHealth2 = "PlantHealth2"
    PlantHealth3 = "PlantHealth3"
    PlantHealth4 = "PlantHealth4"
    PlantGrowth1 = "PlantGrowth1"
    PlantGrowth2 = "PlantGrowth2"
    PlantGrowth3 = "PlantGrowth3"
    PlantGrowth4 = "PlantGrowth4"
    PlantEfficiency1 = "PlantEfficiency1"
    PlantEfficiency2 = "PlantEfficiency2"
    PlantEfficiency3 = "PlantEfficiency3"
    PlantEfficiency4 = "PlantEfficiency4"
    PlantHash1 = "PlantHash1"
    PlantHash2 = "PlantHash2"
    PlantHash3 = "PlantHash3"
    PlantHash4 = "PlantHash4"
    RequestHash = "RequestHash"
    CompletionRatio = "CompletionRatio"
    ClearMemory = "ClearMemory"
    ExportCount = "ExportCount"
    ImportCount = "ImportCount"
    PowerGeneration = "PowerGeneration"
    TotalMoles = "TotalMoles"
    TotalMolesInput = "TotalMolesInput"
    TotalMolesInput2 = "TotalMolesInput2"
    TotalMolesOutput = "TotalMolesOutput"
    TotalMolesOutput2 = "TotalMolesOutput2"
    Volume = "Volume"
    Plant = "Plant"
    Harvest = "Harvest"
    Output = "Output"
    PressureSetting = "PressureSetting"
    TemperatureSetting = "TemperatureSetting"
    TemperatureExternal = "TemperatureExternal"
    Filtration = "Filtration"
    AirRelease = "AirRelease"
    PositionX = "PositionX"
    PositionY = "PositionY"
    PositionZ = "PositionZ"
    VelocityMagnitude = "VelocityMagnitude"
    VelocityRelativeX = "VelocityRelativeX"
    VelocityRelativeY = "VelocityRelativeY"
    VelocityRelativeZ = "VelocityRelativeZ"
    PrefabHash = "PrefabHash"
    ForceWrite = "ForceWrite"
    SignalStrength = "SignalStrength"
    SignalID = "SignalID"
    OperationalTemperatureEfficiency = "OperationalTemperatureEfficiency"
    TemperatureDifferentialEfficiency = "TemperatureDifferentialEfficiency"
    CombustionLimiter = "CombustionLimiter"
    Throttle = "Throttle"
    Rpm = "Rpm"
    Stress = "Stress"
    PressureEfficiency = "PressureEfficiency"
    RatioLiquidOxygen = "RatioLiquidOxygen"
    RatioLiquidOxygenInput = "RatioLiquidOxygenInput"
    RatioLiquidOxygenInput2 = "RatioLiquidOxygenInput2"
    RatioLiquidOxygenOutput = "RatioLiquidOxygenOutput"
    RatioLiquidOxygenOutput2 = "RatioLiquidOxygenOutput2"
    RatioLiquidVolatiles = "RatioLiquidVolatiles"
    RatioLiquidVolatilesInput = "RatioLiquidVolatilesInput"
    RatioLiquidVolatilesInput2 = "RatioLiquidVolatilesInput2"
    RatioLiquidVolatilesOutput = "RatioLiquidVolatilesOutput"
    RatioLiquidVolatilesOutput2 = "RatioLiquidVolatilesOutput2"
    RatioSteam = "RatioSteam"
    RatioSteamInput = "RatioSteamInput"
    RatioSteamInput2 = "RatioSteamInput2"
    RatioSteamOutput = "RatioSteamOutput"
    RatioSteamOutput2 = "RatioSteamOutput2"
    RatioLiquidCarbonDioxide = "RatioLiquidCarbonDioxide"
    RatioLiquidCarbonDioxideInput = "RatioLiquidCarbonDioxideInput"
    RatioLiquidCarbonDioxideInput2 = "RatioLiquidCarbonDioxideInput2"
    RatioLiquidCarbonDioxideOutput = "RatioLiquidCarbonDioxideOutput"
    RatioLiquidCarbonDioxideOutput2 = "RatioLiquidCarbonDioxideOutput2"
    RatioLiquidPollutant = "RatioLiquidPollutant"
    RatioLiquidPollutantInput = "RatioLiquidPollutantInput"
    RatioLiquidPollutantInput2 = "RatioLiquidPollutantInput2"
    RatioLiquidPollutantOutput = "RatioLiquidPollutantOutput"
    RatioLiquidPollutantOutput2 = "RatioLiquidPollutantOutput2"
    RatioLiquidNitrousOxide = "RatioLiquidNitrousOxide"
    RatioLiquidNitrousOxideInput = "RatioLiquidNitrousOxideInput"
    RatioLiquidNitrousOxideInput2 = "RatioLiquidNitrousOxideInput2"
    RatioLiquidNitrousOxideOutput = "RatioLiquidNitrousOxideOutput"
    RatioLiquidNitrousOxideOutput2 = "RatioLiquidNitrousOxideOutput2"
    RatioHydrogen = "RatioHydrogen"
    RatioLiquidHydrogen = "RatioLiquidHydrogen"
    ContactTypeId = "ContactTypeId"
    Bypass = "Bypass"
    Progress = "Progress"
    DestinationCode = "DestinationCode"
    Acceleration = "Acceleration"
    AutoShutOff = "AutoShutOff"
    Thrust = "Thrust"
    ThrustToWeight = "ThrustToWeight"
    Weight = "Weight"
    OverShootTarget = "OverShootTarget"
    TimeToDestination = "TimeToDestination"
    BurnTimeRemaining = "BurnTimeRemaining"
    AutoLand = "AutoLand"
    DryMass = "DryMass"
    Mass = "Mass"
    TargetX = "TargetX"
    TargetY = "TargetY"
    TargetZ = "TargetZ"
    SettingInputHash = "SettingInputHash"
    SettingOutputHash = "SettingOutputHash"
    Channel = "Channel"
    Unknown = "Unknown"
    Time = "Time"
    Bpm = "Bpm"
    EnvironmentEfficiency = "EnvironmentEfficiency"
    WorkingGasEfficiency = "WorkingGasEfficiency"


class _logicSlotType:
    None_ = "None"
    Occupied = "Occupied"
    OccupantHash = "OccupantHash"
    Quantity = "Quantity"
    Damage = "Damage"
    Efficiency = "Efficiency"
    Mature = "Mature"
    Seeding = "Seeding"
    HarvestedHash = "HarvestedHash"
    Health = "Health"
    Growth = "Growth"
    Pressure = "Pressure"
    Temperature = "Temperature"
    Charge = "Charge"
    ChargeRatio = "ChargeRatio"
    Class = "Class"
    PressureWaste = "PressureWaste"
    PressureAir = "PressureAir"
    MaxQuantity = "MaxQuantity"
    PrefabHash = "PrefabHash"


del enum


class _GenericStructures:

    @property
    def None_(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("None_")

    @None_.setter
    def None_(self, value):
        return self.__setattr__("None_")

    @property
    def Power(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Power")

    @Power.setter
    def Power(self, value):
        return self.__setattr__("Power")

    @property
    def Open(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Open")

    @Open.setter
    def Open(self, value):
        return self.__setattr__("Open")

    @property
    def Mode(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Mode")

    @Mode.setter
    def Mode(self, value):
        return self.__setattr__("Mode")

    @property
    def Error(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Error")

    @Error.setter
    def Error(self, value):
        return self.__setattr__("Error")

    @property
    def Flush(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Flush")

    @Flush.setter
    def Flush(self, value):
        return self.__setattr__("Flush")

    @property
    def SoundAlert(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SoundAlert")

    @SoundAlert.setter
    def SoundAlert(self, value):
        return self.__setattr__("SoundAlert")

    @property
    def VolumeOfLiquid(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("VolumeOfLiquid")

    @VolumeOfLiquid.setter
    def VolumeOfLiquid(self, value):
        return self.__setattr__("VolumeOfLiquid")

    @property
    def Lock(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Lock")

    @Lock.setter
    def Lock(self, value):
        return self.__setattr__("Lock")

    @property
    def Pressure(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Pressure")

    @Pressure.setter
    def Pressure(self, value):
        return self.__setattr__("Pressure")

    @property
    def Temperature(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Temperature")

    @Temperature.setter
    def Temperature(self, value):
        return self.__setattr__("Temperature")

    @property
    def PressureInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureInput")

    @PressureInput.setter
    def PressureInput(self, value):
        return self.__setattr__("PressureInput")

    @property
    def TemperatureInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TemperatureInput")

    @TemperatureInput.setter
    def TemperatureInput(self, value):
        return self.__setattr__("TemperatureInput")

    @property
    def PressureInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureInput2")

    @PressureInput2.setter
    def PressureInput2(self, value):
        return self.__setattr__("PressureInput2")

    @property
    def TemperatureInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TemperatureInput2")

    @TemperatureInput2.setter
    def TemperatureInput2(self, value):
        return self.__setattr__("TemperatureInput2")

    @property
    def PressureOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureOutput")

    @PressureOutput.setter
    def PressureOutput(self, value):
        return self.__setattr__("PressureOutput")

    @property
    def TargetPadIndex(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TargetPadIndex")

    @TargetPadIndex.setter
    def TargetPadIndex(self, value):
        return self.__setattr__("TargetPadIndex")

    @property
    def InterrogationProgress(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("InterrogationProgress")

    @InterrogationProgress.setter
    def InterrogationProgress(self, value):
        return self.__setattr__("InterrogationProgress")

    @property
    def SizeX(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SizeX")

    @SizeX.setter
    def SizeX(self, value):
        return self.__setattr__("SizeX")

    @property
    def SizeY(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SizeY")

    @SizeY.setter
    def SizeY(self, value):
        return self.__setattr__("SizeY")

    @property
    def SizeZ(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SizeZ")

    @SizeZ.setter
    def SizeZ(self, value):
        return self.__setattr__("SizeZ")

    @property
    def MinWattsToContact(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("MinWattsToContact")

    @MinWattsToContact.setter
    def MinWattsToContact(self, value):
        return self.__setattr__("MinWattsToContact")

    @property
    def WattsReachingContact(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("WattsReachingContact")

    @WattsReachingContact.setter
    def WattsReachingContact(self, value):
        return self.__setattr__("WattsReachingContact")

    @property
    def LineNumber(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("LineNumber")

    @LineNumber.setter
    def LineNumber(self, value):
        return self.__setattr__("LineNumber")

    @property
    def TemperatureOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TemperatureOutput")

    @TemperatureOutput.setter
    def TemperatureOutput(self, value):
        return self.__setattr__("TemperatureOutput")

    @property
    def PressureOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureOutput2")

    @PressureOutput2.setter
    def PressureOutput2(self, value):
        return self.__setattr__("PressureOutput2")

    @property
    def TemperatureOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TemperatureOutput2")

    @TemperatureOutput2.setter
    def TemperatureOutput2(self, value):
        return self.__setattr__("TemperatureOutput2")

    @property
    def PressureExternal(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureExternal")

    @PressureExternal.setter
    def PressureExternal(self, value):
        return self.__setattr__("PressureExternal")

    @property
    def PressureInternal(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureInternal")

    @PressureInternal.setter
    def PressureInternal(self, value):
        return self.__setattr__("PressureInternal")

    @property
    def Activate(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Activate")

    @Activate.setter
    def Activate(self, value):
        return self.__setattr__("Activate")

    @property
    def Charge(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Charge")

    @Charge.setter
    def Charge(self, value):
        return self.__setattr__("Charge")

    @property
    def Setting(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Setting")

    @Setting.setter
    def Setting(self, value):
        return self.__setattr__("Setting")

    @property
    def Reagents(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Reagents")

    @Reagents.setter
    def Reagents(self, value):
        return self.__setattr__("Reagents")

    @property
    def RatioOxygen(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioOxygen")

    @RatioOxygen.setter
    def RatioOxygen(self, value):
        return self.__setattr__("RatioOxygen")

    @property
    def RatioCarbonDioxide(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioCarbonDioxide")

    @RatioCarbonDioxide.setter
    def RatioCarbonDioxide(self, value):
        return self.__setattr__("RatioCarbonDioxide")

    @property
    def RatioNitrogen(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrogen")

    @RatioNitrogen.setter
    def RatioNitrogen(self, value):
        return self.__setattr__("RatioNitrogen")

    @property
    def RatioPollutant(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioPollutant")

    @RatioPollutant.setter
    def RatioPollutant(self, value):
        return self.__setattr__("RatioPollutant")

    @property
    def RatioVolatiles(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioVolatiles")

    @RatioVolatiles.setter
    def RatioVolatiles(self, value):
        return self.__setattr__("RatioVolatiles")

    @property
    def RatioWater(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioWater")

    @RatioWater.setter
    def RatioWater(self, value):
        return self.__setattr__("RatioWater")

    @property
    def RatioPollutedWater(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioPollutedWater")

    @RatioPollutedWater.setter
    def RatioPollutedWater(self, value):
        return self.__setattr__("RatioPollutedWater")

    @property
    def RatioNitrousOxide(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrousOxide")

    @RatioNitrousOxide.setter
    def RatioNitrousOxide(self, value):
        return self.__setattr__("RatioNitrousOxide")

    @property
    def RatioLiquidNitrogen(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrogen")

    @RatioLiquidNitrogen.setter
    def RatioLiquidNitrogen(self, value):
        return self.__setattr__("RatioLiquidNitrogen")

    @property
    def Combustion(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Combustion")

    @Combustion.setter
    def Combustion(self, value):
        return self.__setattr__("Combustion")

    @property
    def RatioOxygenInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioOxygenInput")

    @RatioOxygenInput.setter
    def RatioOxygenInput(self, value):
        return self.__setattr__("RatioOxygenInput")

    @property
    def RatioCarbonDioxideInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioCarbonDioxideInput")

    @RatioCarbonDioxideInput.setter
    def RatioCarbonDioxideInput(self, value):
        return self.__setattr__("RatioCarbonDioxideInput")

    @property
    def RatioNitrogenInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrogenInput")

    @RatioNitrogenInput.setter
    def RatioNitrogenInput(self, value):
        return self.__setattr__("RatioNitrogenInput")

    @property
    def RatioPollutantInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioPollutantInput")

    @RatioPollutantInput.setter
    def RatioPollutantInput(self, value):
        return self.__setattr__("RatioPollutantInput")

    @property
    def RatioVolatilesInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioVolatilesInput")

    @RatioVolatilesInput.setter
    def RatioVolatilesInput(self, value):
        return self.__setattr__("RatioVolatilesInput")

    @property
    def RatioWaterInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioWaterInput")

    @RatioWaterInput.setter
    def RatioWaterInput(self, value):
        return self.__setattr__("RatioWaterInput")

    @property
    def RatioNitrousOxideInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrousOxideInput")

    @RatioNitrousOxideInput.setter
    def RatioNitrousOxideInput(self, value):
        return self.__setattr__("RatioNitrousOxideInput")

    @property
    def RatioLiquidNitrogenInput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrogenInput")

    @RatioLiquidNitrogenInput.setter
    def RatioLiquidNitrogenInput(self, value):
        return self.__setattr__("RatioLiquidNitrogenInput")

    @property
    def CombustionInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CombustionInput")

    @CombustionInput.setter
    def CombustionInput(self, value):
        return self.__setattr__("CombustionInput")

    @property
    def RatioOxygenInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioOxygenInput2")

    @RatioOxygenInput2.setter
    def RatioOxygenInput2(self, value):
        return self.__setattr__("RatioOxygenInput2")

    @property
    def RatioCarbonDioxideInput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioCarbonDioxideInput2")

    @RatioCarbonDioxideInput2.setter
    def RatioCarbonDioxideInput2(self, value):
        return self.__setattr__("RatioCarbonDioxideInput2")

    @property
    def RatioNitrogenInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrogenInput2")

    @RatioNitrogenInput2.setter
    def RatioNitrogenInput2(self, value):
        return self.__setattr__("RatioNitrogenInput2")

    @property
    def RatioPollutantInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioPollutantInput2")

    @RatioPollutantInput2.setter
    def RatioPollutantInput2(self, value):
        return self.__setattr__("RatioPollutantInput2")

    @property
    def RatioVolatilesInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioVolatilesInput2")

    @RatioVolatilesInput2.setter
    def RatioVolatilesInput2(self, value):
        return self.__setattr__("RatioVolatilesInput2")

    @property
    def RatioWaterInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioWaterInput2")

    @RatioWaterInput2.setter
    def RatioWaterInput2(self, value):
        return self.__setattr__("RatioWaterInput2")

    @property
    def RatioNitrousOxideInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrousOxideInput2")

    @RatioNitrousOxideInput2.setter
    def RatioNitrousOxideInput2(self, value):
        return self.__setattr__("RatioNitrousOxideInput2")

    @property
    def RatioLiquidNitrogenInput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrogenInput2")

    @RatioLiquidNitrogenInput2.setter
    def RatioLiquidNitrogenInput2(self, value):
        return self.__setattr__("RatioLiquidNitrogenInput2")

    @property
    def CombustionInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CombustionInput2")

    @CombustionInput2.setter
    def CombustionInput2(self, value):
        return self.__setattr__("CombustionInput2")

    @property
    def RatioOxygenOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioOxygenOutput")

    @RatioOxygenOutput.setter
    def RatioOxygenOutput(self, value):
        return self.__setattr__("RatioOxygenOutput")

    @property
    def RatioCarbonDioxideOutput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioCarbonDioxideOutput")

    @RatioCarbonDioxideOutput.setter
    def RatioCarbonDioxideOutput(self, value):
        return self.__setattr__("RatioCarbonDioxideOutput")

    @property
    def RatioNitrogenOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrogenOutput")

    @RatioNitrogenOutput.setter
    def RatioNitrogenOutput(self, value):
        return self.__setattr__("RatioNitrogenOutput")

    @property
    def RatioPollutantOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioPollutantOutput")

    @RatioPollutantOutput.setter
    def RatioPollutantOutput(self, value):
        return self.__setattr__("RatioPollutantOutput")

    @property
    def RatioVolatilesOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioVolatilesOutput")

    @RatioVolatilesOutput.setter
    def RatioVolatilesOutput(self, value):
        return self.__setattr__("RatioVolatilesOutput")

    @property
    def RatioWaterOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioWaterOutput")

    @RatioWaterOutput.setter
    def RatioWaterOutput(self, value):
        return self.__setattr__("RatioWaterOutput")

    @property
    def RatioNitrousOxideOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrousOxideOutput")

    @RatioNitrousOxideOutput.setter
    def RatioNitrousOxideOutput(self, value):
        return self.__setattr__("RatioNitrousOxideOutput")

    @property
    def RatioLiquidNitrogenOutput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrogenOutput")

    @RatioLiquidNitrogenOutput.setter
    def RatioLiquidNitrogenOutput(self, value):
        return self.__setattr__("RatioLiquidNitrogenOutput")

    @property
    def CombustionOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CombustionOutput")

    @CombustionOutput.setter
    def CombustionOutput(self, value):
        return self.__setattr__("CombustionOutput")

    @property
    def RatioOxygenOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioOxygenOutput2")

    @RatioOxygenOutput2.setter
    def RatioOxygenOutput2(self, value):
        return self.__setattr__("RatioOxygenOutput2")

    @property
    def RatioCarbonDioxideOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioCarbonDioxideOutput2")

    @RatioCarbonDioxideOutput2.setter
    def RatioCarbonDioxideOutput2(self, value):
        return self.__setattr__("RatioCarbonDioxideOutput2")

    @property
    def RatioNitrogenOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrogenOutput2")

    @RatioNitrogenOutput2.setter
    def RatioNitrogenOutput2(self, value):
        return self.__setattr__("RatioNitrogenOutput2")

    @property
    def RatioPollutantOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioPollutantOutput2")

    @RatioPollutantOutput2.setter
    def RatioPollutantOutput2(self, value):
        return self.__setattr__("RatioPollutantOutput2")

    @property
    def RatioVolatilesOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioVolatilesOutput2")

    @RatioVolatilesOutput2.setter
    def RatioVolatilesOutput2(self, value):
        return self.__setattr__("RatioVolatilesOutput2")

    @property
    def RatioWaterOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioWaterOutput2")

    @RatioWaterOutput2.setter
    def RatioWaterOutput2(self, value):
        return self.__setattr__("RatioWaterOutput2")

    @property
    def RatioNitrousOxideOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioNitrousOxideOutput2")

    @RatioNitrousOxideOutput2.setter
    def RatioNitrousOxideOutput2(self, value):
        return self.__setattr__("RatioNitrousOxideOutput2")

    @property
    def RatioLiquidNitrogenOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrogenOutput2")

    @RatioLiquidNitrogenOutput2.setter
    def RatioLiquidNitrogenOutput2(self, value):
        return self.__setattr__("RatioLiquidNitrogenOutput2")

    @property
    def CombustionOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CombustionOutput2")

    @CombustionOutput2.setter
    def CombustionOutput2(self, value):
        return self.__setattr__("CombustionOutput2")

    @property
    def Horizontal(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Horizontal")

    @Horizontal.setter
    def Horizontal(self, value):
        return self.__setattr__("Horizontal")

    @property
    def Vertical(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Vertical")

    @Vertical.setter
    def Vertical(self, value):
        return self.__setattr__("Vertical")

    @property
    def SolarAngle(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SolarAngle")

    @SolarAngle.setter
    def SolarAngle(self, value):
        return self.__setattr__("SolarAngle")

    @property
    def SolarConstant(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SolarConstant")

    @SolarConstant.setter
    def SolarConstant(self, value):
        return self.__setattr__("SolarConstant")

    @property
    def Maximum(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Maximum")

    @Maximum.setter
    def Maximum(self, value):
        return self.__setattr__("Maximum")

    @property
    def Ratio(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Ratio")

    @Ratio.setter
    def Ratio(self, value):
        return self.__setattr__("Ratio")

    @property
    def PowerPotential(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PowerPotential")

    @PowerPotential.setter
    def PowerPotential(self, value):
        return self.__setattr__("PowerPotential")

    @property
    def PowerActual(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PowerActual")

    @PowerActual.setter
    def PowerActual(self, value):
        return self.__setattr__("PowerActual")

    @property
    def Quantity(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Quantity")

    @Quantity.setter
    def Quantity(self, value):
        return self.__setattr__("Quantity")

    @property
    def On(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("On")

    @On.setter
    def On(self, value):
        return self.__setattr__("On")

    @property
    def ImportQuantity(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ImportQuantity")

    @ImportQuantity.setter
    def ImportQuantity(self, value):
        return self.__setattr__("ImportQuantity")

    @property
    def ImportSlotOccupant(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ImportSlotOccupant")

    @ImportSlotOccupant.setter
    def ImportSlotOccupant(self, value):
        return self.__setattr__("ImportSlotOccupant")

    @property
    def ExportQuantity(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ExportQuantity")

    @ExportQuantity.setter
    def ExportQuantity(self, value):
        return self.__setattr__("ExportQuantity")

    @property
    def ExportSlotOccupant(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ExportSlotOccupant")

    @ExportSlotOccupant.setter
    def ExportSlotOccupant(self, value):
        return self.__setattr__("ExportSlotOccupant")

    @property
    def RequiredPower(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RequiredPower")

    @RequiredPower.setter
    def RequiredPower(self, value):
        return self.__setattr__("RequiredPower")

    @property
    def HorizontalRatio(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("HorizontalRatio")

    @HorizontalRatio.setter
    def HorizontalRatio(self, value):
        return self.__setattr__("HorizontalRatio")

    @property
    def VerticalRatio(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("VerticalRatio")

    @VerticalRatio.setter
    def VerticalRatio(self, value):
        return self.__setattr__("VerticalRatio")

    @property
    def PowerRequired(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PowerRequired")

    @PowerRequired.setter
    def PowerRequired(self, value):
        return self.__setattr__("PowerRequired")

    @property
    def Idle(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Idle")

    @Idle.setter
    def Idle(self, value):
        return self.__setattr__("Idle")

    @property
    def Color(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Color")

    @Color.setter
    def Color(self, value):
        return self.__setattr__("Color")

    @property
    def ElevatorSpeed(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ElevatorSpeed")

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value):
        return self.__setattr__("ElevatorSpeed")

    @property
    def ElevatorLevel(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ElevatorLevel")

    @ElevatorLevel.setter
    def ElevatorLevel(self, value):
        return self.__setattr__("ElevatorLevel")

    @property
    def RecipeHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RecipeHash")

    @RecipeHash.setter
    def RecipeHash(self, value):
        return self.__setattr__("RecipeHash")

    @property
    def ExportSlotHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ExportSlotHash")

    @ExportSlotHash.setter
    def ExportSlotHash(self, value):
        return self.__setattr__("ExportSlotHash")

    @property
    def ImportSlotHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ImportSlotHash")

    @ImportSlotHash.setter
    def ImportSlotHash(self, value):
        return self.__setattr__("ImportSlotHash")

    @property
    def PlantHealth1(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHealth1")

    @PlantHealth1.setter
    def PlantHealth1(self, value):
        return self.__setattr__("PlantHealth1")

    @property
    def PlantHealth2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHealth2")

    @PlantHealth2.setter
    def PlantHealth2(self, value):
        return self.__setattr__("PlantHealth2")

    @property
    def PlantHealth3(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHealth3")

    @PlantHealth3.setter
    def PlantHealth3(self, value):
        return self.__setattr__("PlantHealth3")

    @property
    def PlantHealth4(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHealth4")

    @PlantHealth4.setter
    def PlantHealth4(self, value):
        return self.__setattr__("PlantHealth4")

    @property
    def PlantGrowth1(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantGrowth1")

    @PlantGrowth1.setter
    def PlantGrowth1(self, value):
        return self.__setattr__("PlantGrowth1")

    @property
    def PlantGrowth2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantGrowth2")

    @PlantGrowth2.setter
    def PlantGrowth2(self, value):
        return self.__setattr__("PlantGrowth2")

    @property
    def PlantGrowth3(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantGrowth3")

    @PlantGrowth3.setter
    def PlantGrowth3(self, value):
        return self.__setattr__("PlantGrowth3")

    @property
    def PlantGrowth4(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantGrowth4")

    @PlantGrowth4.setter
    def PlantGrowth4(self, value):
        return self.__setattr__("PlantGrowth4")

    @property
    def PlantEfficiency1(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantEfficiency1")

    @PlantEfficiency1.setter
    def PlantEfficiency1(self, value):
        return self.__setattr__("PlantEfficiency1")

    @property
    def PlantEfficiency2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantEfficiency2")

    @PlantEfficiency2.setter
    def PlantEfficiency2(self, value):
        return self.__setattr__("PlantEfficiency2")

    @property
    def PlantEfficiency3(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantEfficiency3")

    @PlantEfficiency3.setter
    def PlantEfficiency3(self, value):
        return self.__setattr__("PlantEfficiency3")

    @property
    def PlantEfficiency4(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantEfficiency4")

    @PlantEfficiency4.setter
    def PlantEfficiency4(self, value):
        return self.__setattr__("PlantEfficiency4")

    @property
    def PlantHash1(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHash1")

    @PlantHash1.setter
    def PlantHash1(self, value):
        return self.__setattr__("PlantHash1")

    @property
    def PlantHash2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHash2")

    @PlantHash2.setter
    def PlantHash2(self, value):
        return self.__setattr__("PlantHash2")

    @property
    def PlantHash3(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHash3")

    @PlantHash3.setter
    def PlantHash3(self, value):
        return self.__setattr__("PlantHash3")

    @property
    def PlantHash4(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PlantHash4")

    @PlantHash4.setter
    def PlantHash4(self, value):
        return self.__setattr__("PlantHash4")

    @property
    def RequestHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RequestHash")

    @RequestHash.setter
    def RequestHash(self, value):
        return self.__setattr__("RequestHash")

    @property
    def CompletionRatio(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CompletionRatio")

    @CompletionRatio.setter
    def CompletionRatio(self, value):
        return self.__setattr__("CompletionRatio")

    @property
    def ClearMemory(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ClearMemory")

    @ClearMemory.setter
    def ClearMemory(self, value):
        return self.__setattr__("ClearMemory")

    @property
    def ExportCount(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ExportCount")

    @ExportCount.setter
    def ExportCount(self, value):
        return self.__setattr__("ExportCount")

    @property
    def ImportCount(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ImportCount")

    @ImportCount.setter
    def ImportCount(self, value):
        return self.__setattr__("ImportCount")

    @property
    def PowerGeneration(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PowerGeneration")

    @PowerGeneration.setter
    def PowerGeneration(self, value):
        return self.__setattr__("PowerGeneration")

    @property
    def TotalMoles(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TotalMoles")

    @TotalMoles.setter
    def TotalMoles(self, value):
        return self.__setattr__("TotalMoles")

    @property
    def TotalMolesInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TotalMolesInput")

    @TotalMolesInput.setter
    def TotalMolesInput(self, value):
        return self.__setattr__("TotalMolesInput")

    @property
    def TotalMolesInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TotalMolesInput2")

    @TotalMolesInput2.setter
    def TotalMolesInput2(self, value):
        return self.__setattr__("TotalMolesInput2")

    @property
    def TotalMolesOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TotalMolesOutput")

    @TotalMolesOutput.setter
    def TotalMolesOutput(self, value):
        return self.__setattr__("TotalMolesOutput")

    @property
    def TotalMolesOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TotalMolesOutput2")

    @TotalMolesOutput2.setter
    def TotalMolesOutput2(self, value):
        return self.__setattr__("TotalMolesOutput2")

    @property
    def Volume(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Volume")

    @Volume.setter
    def Volume(self, value):
        return self.__setattr__("Volume")

    @property
    def Plant(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Plant")

    @Plant.setter
    def Plant(self, value):
        return self.__setattr__("Plant")

    @property
    def Harvest(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Harvest")

    @Harvest.setter
    def Harvest(self, value):
        return self.__setattr__("Harvest")

    @property
    def Output(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Output")

    @Output.setter
    def Output(self, value):
        return self.__setattr__("Output")

    @property
    def PressureSetting(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureSetting")

    @PressureSetting.setter
    def PressureSetting(self, value):
        return self.__setattr__("PressureSetting")

    @property
    def TemperatureSetting(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TemperatureSetting")

    @TemperatureSetting.setter
    def TemperatureSetting(self, value):
        return self.__setattr__("TemperatureSetting")

    @property
    def TemperatureExternal(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TemperatureExternal")

    @TemperatureExternal.setter
    def TemperatureExternal(self, value):
        return self.__setattr__("TemperatureExternal")

    @property
    def Filtration(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Filtration")

    @Filtration.setter
    def Filtration(self, value):
        return self.__setattr__("Filtration")

    @property
    def AirRelease(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("AirRelease")

    @AirRelease.setter
    def AirRelease(self, value):
        return self.__setattr__("AirRelease")

    @property
    def PositionX(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PositionX")

    @PositionX.setter
    def PositionX(self, value):
        return self.__setattr__("PositionX")

    @property
    def PositionY(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PositionY")

    @PositionY.setter
    def PositionY(self, value):
        return self.__setattr__("PositionY")

    @property
    def PositionZ(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PositionZ")

    @PositionZ.setter
    def PositionZ(self, value):
        return self.__setattr__("PositionZ")

    @property
    def VelocityMagnitude(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("VelocityMagnitude")

    @VelocityMagnitude.setter
    def VelocityMagnitude(self, value):
        return self.__setattr__("VelocityMagnitude")

    @property
    def VelocityRelativeX(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("VelocityRelativeX")

    @VelocityRelativeX.setter
    def VelocityRelativeX(self, value):
        return self.__setattr__("VelocityRelativeX")

    @property
    def VelocityRelativeY(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("VelocityRelativeY")

    @VelocityRelativeY.setter
    def VelocityRelativeY(self, value):
        return self.__setattr__("VelocityRelativeY")

    @property
    def VelocityRelativeZ(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("VelocityRelativeZ")

    @VelocityRelativeZ.setter
    def VelocityRelativeZ(self, value):
        return self.__setattr__("VelocityRelativeZ")

    @property
    def PrefabHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PrefabHash")

    @PrefabHash.setter
    def PrefabHash(self, value):
        return self.__setattr__("PrefabHash")

    @property
    def ForceWrite(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ForceWrite")

    @ForceWrite.setter
    def ForceWrite(self, value):
        return self.__setattr__("ForceWrite")

    @property
    def SignalStrength(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SignalStrength")

    @SignalStrength.setter
    def SignalStrength(self, value):
        return self.__setattr__("SignalStrength")

    @property
    def SignalID(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SignalID")

    @SignalID.setter
    def SignalID(self, value):
        return self.__setattr__("SignalID")

    @property
    def OperationalTemperatureEfficiency(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("OperationalTemperatureEfficiency")

    @OperationalTemperatureEfficiency.setter
    def OperationalTemperatureEfficiency(self, value):
        return self.__setattr__("OperationalTemperatureEfficiency")

    @property
    def TemperatureDifferentialEfficiency(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TemperatureDifferentialEfficiency")

    @TemperatureDifferentialEfficiency.setter
    def TemperatureDifferentialEfficiency(self, value):
        return self.__setattr__("TemperatureDifferentialEfficiency")

    @property
    def CombustionLimiter(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("CombustionLimiter")

    @CombustionLimiter.setter
    def CombustionLimiter(self, value):
        return self.__setattr__("CombustionLimiter")

    @property
    def Throttle(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Throttle")

    @Throttle.setter
    def Throttle(self, value):
        return self.__setattr__("Throttle")

    @property
    def Rpm(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Rpm")

    @Rpm.setter
    def Rpm(self, value):
        return self.__setattr__("Rpm")

    @property
    def Stress(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Stress")

    @Stress.setter
    def Stress(self, value):
        return self.__setattr__("Stress")

    @property
    def PressureEfficiency(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("PressureEfficiency")

    @PressureEfficiency.setter
    def PressureEfficiency(self, value):
        return self.__setattr__("PressureEfficiency")

    @property
    def RatioLiquidOxygen(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidOxygen")

    @RatioLiquidOxygen.setter
    def RatioLiquidOxygen(self, value):
        return self.__setattr__("RatioLiquidOxygen")

    @property
    def RatioLiquidOxygenInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidOxygenInput")

    @RatioLiquidOxygenInput.setter
    def RatioLiquidOxygenInput(self, value):
        return self.__setattr__("RatioLiquidOxygenInput")

    @property
    def RatioLiquidOxygenInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidOxygenInput2")

    @RatioLiquidOxygenInput2.setter
    def RatioLiquidOxygenInput2(self, value):
        return self.__setattr__("RatioLiquidOxygenInput2")

    @property
    def RatioLiquidOxygenOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidOxygenOutput")

    @RatioLiquidOxygenOutput.setter
    def RatioLiquidOxygenOutput(self, value):
        return self.__setattr__("RatioLiquidOxygenOutput")

    @property
    def RatioLiquidOxygenOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidOxygenOutput2")

    @RatioLiquidOxygenOutput2.setter
    def RatioLiquidOxygenOutput2(self, value):
        return self.__setattr__("RatioLiquidOxygenOutput2")

    @property
    def RatioLiquidVolatiles(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidVolatiles")

    @RatioLiquidVolatiles.setter
    def RatioLiquidVolatiles(self, value):
        return self.__setattr__("RatioLiquidVolatiles")

    @property
    def RatioLiquidVolatilesInput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidVolatilesInput")

    @RatioLiquidVolatilesInput.setter
    def RatioLiquidVolatilesInput(self, value):
        return self.__setattr__("RatioLiquidVolatilesInput")

    @property
    def RatioLiquidVolatilesInput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidVolatilesInput2")

    @RatioLiquidVolatilesInput2.setter
    def RatioLiquidVolatilesInput2(self, value):
        return self.__setattr__("RatioLiquidVolatilesInput2")

    @property
    def RatioLiquidVolatilesOutput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidVolatilesOutput")

    @RatioLiquidVolatilesOutput.setter
    def RatioLiquidVolatilesOutput(self, value):
        return self.__setattr__("RatioLiquidVolatilesOutput")

    @property
    def RatioLiquidVolatilesOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidVolatilesOutput2")

    @RatioLiquidVolatilesOutput2.setter
    def RatioLiquidVolatilesOutput2(self, value):
        return self.__setattr__("RatioLiquidVolatilesOutput2")

    @property
    def RatioSteam(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioSteam")

    @RatioSteam.setter
    def RatioSteam(self, value):
        return self.__setattr__("RatioSteam")

    @property
    def RatioSteamInput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioSteamInput")

    @RatioSteamInput.setter
    def RatioSteamInput(self, value):
        return self.__setattr__("RatioSteamInput")

    @property
    def RatioSteamInput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioSteamInput2")

    @RatioSteamInput2.setter
    def RatioSteamInput2(self, value):
        return self.__setattr__("RatioSteamInput2")

    @property
    def RatioSteamOutput(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioSteamOutput")

    @RatioSteamOutput.setter
    def RatioSteamOutput(self, value):
        return self.__setattr__("RatioSteamOutput")

    @property
    def RatioSteamOutput2(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioSteamOutput2")

    @RatioSteamOutput2.setter
    def RatioSteamOutput2(self, value):
        return self.__setattr__("RatioSteamOutput2")

    @property
    def RatioLiquidCarbonDioxide(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxide")

    @RatioLiquidCarbonDioxide.setter
    def RatioLiquidCarbonDioxide(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxide")

    @property
    def RatioLiquidCarbonDioxideInput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideInput")

    @RatioLiquidCarbonDioxideInput.setter
    def RatioLiquidCarbonDioxideInput(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideInput")

    @property
    def RatioLiquidCarbonDioxideInput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideInput2")

    @RatioLiquidCarbonDioxideInput2.setter
    def RatioLiquidCarbonDioxideInput2(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideInput2")

    @property
    def RatioLiquidCarbonDioxideOutput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideOutput")

    @RatioLiquidCarbonDioxideOutput.setter
    def RatioLiquidCarbonDioxideOutput(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideOutput")

    @property
    def RatioLiquidCarbonDioxideOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideOutput2")

    @RatioLiquidCarbonDioxideOutput2.setter
    def RatioLiquidCarbonDioxideOutput2(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideOutput2")

    @property
    def RatioLiquidPollutant(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidPollutant")

    @RatioLiquidPollutant.setter
    def RatioLiquidPollutant(self, value):
        return self.__setattr__("RatioLiquidPollutant")

    @property
    def RatioLiquidPollutantInput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidPollutantInput")

    @RatioLiquidPollutantInput.setter
    def RatioLiquidPollutantInput(self, value):
        return self.__setattr__("RatioLiquidPollutantInput")

    @property
    def RatioLiquidPollutantInput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidPollutantInput2")

    @RatioLiquidPollutantInput2.setter
    def RatioLiquidPollutantInput2(self, value):
        return self.__setattr__("RatioLiquidPollutantInput2")

    @property
    def RatioLiquidPollutantOutput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidPollutantOutput")

    @RatioLiquidPollutantOutput.setter
    def RatioLiquidPollutantOutput(self, value):
        return self.__setattr__("RatioLiquidPollutantOutput")

    @property
    def RatioLiquidPollutantOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidPollutantOutput2")

    @RatioLiquidPollutantOutput2.setter
    def RatioLiquidPollutantOutput2(self, value):
        return self.__setattr__("RatioLiquidPollutantOutput2")

    @property
    def RatioLiquidNitrousOxide(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrousOxide")

    @RatioLiquidNitrousOxide.setter
    def RatioLiquidNitrousOxide(self, value):
        return self.__setattr__("RatioLiquidNitrousOxide")

    @property
    def RatioLiquidNitrousOxideInput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideInput")

    @RatioLiquidNitrousOxideInput.setter
    def RatioLiquidNitrousOxideInput(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideInput")

    @property
    def RatioLiquidNitrousOxideInput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideInput2")

    @RatioLiquidNitrousOxideInput2.setter
    def RatioLiquidNitrousOxideInput2(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideInput2")

    @property
    def RatioLiquidNitrousOxideOutput(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideOutput")

    @RatioLiquidNitrousOxideOutput.setter
    def RatioLiquidNitrousOxideOutput(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideOutput")

    @property
    def RatioLiquidNitrousOxideOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideOutput2")

    @RatioLiquidNitrousOxideOutput2.setter
    def RatioLiquidNitrousOxideOutput2(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideOutput2")

    @property
    def RatioHydrogen(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioHydrogen")

    @RatioHydrogen.setter
    def RatioHydrogen(self, value):
        return self.__setattr__("RatioHydrogen")

    @property
    def RatioLiquidHydrogen(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("RatioLiquidHydrogen")

    @RatioLiquidHydrogen.setter
    def RatioLiquidHydrogen(self, value):
        return self.__setattr__("RatioLiquidHydrogen")

    @property
    def ContactTypeId(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ContactTypeId")

    @ContactTypeId.setter
    def ContactTypeId(self, value):
        return self.__setattr__("ContactTypeId")

    @property
    def Bypass(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Bypass")

    @Bypass.setter
    def Bypass(self, value):
        return self.__setattr__("Bypass")

    @property
    def Progress(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Progress")

    @Progress.setter
    def Progress(self, value):
        return self.__setattr__("Progress")

    @property
    def DestinationCode(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("DestinationCode")

    @DestinationCode.setter
    def DestinationCode(self, value):
        return self.__setattr__("DestinationCode")

    @property
    def Acceleration(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Acceleration")

    @Acceleration.setter
    def Acceleration(self, value):
        return self.__setattr__("Acceleration")

    @property
    def AutoShutOff(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("AutoShutOff")

    @AutoShutOff.setter
    def AutoShutOff(self, value):
        return self.__setattr__("AutoShutOff")

    @property
    def Thrust(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Thrust")

    @Thrust.setter
    def Thrust(self, value):
        return self.__setattr__("Thrust")

    @property
    def ThrustToWeight(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("ThrustToWeight")

    @ThrustToWeight.setter
    def ThrustToWeight(self, value):
        return self.__setattr__("ThrustToWeight")

    @property
    def Weight(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Weight")

    @Weight.setter
    def Weight(self, value):
        return self.__setattr__("Weight")

    @property
    def OverShootTarget(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("OverShootTarget")

    @OverShootTarget.setter
    def OverShootTarget(self, value):
        return self.__setattr__("OverShootTarget")

    @property
    def TimeToDestination(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TimeToDestination")

    @TimeToDestination.setter
    def TimeToDestination(self, value):
        return self.__setattr__("TimeToDestination")

    @property
    def BurnTimeRemaining(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("BurnTimeRemaining")

    @BurnTimeRemaining.setter
    def BurnTimeRemaining(self, value):
        return self.__setattr__("BurnTimeRemaining")

    @property
    def AutoLand(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("AutoLand")

    @AutoLand.setter
    def AutoLand(self, value):
        return self.__setattr__("AutoLand")

    @property
    def DryMass(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("DryMass")

    @DryMass.setter
    def DryMass(self, value):
        return self.__setattr__("DryMass")

    @property
    def Mass(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Mass")

    @Mass.setter
    def Mass(self, value):
        return self.__setattr__("Mass")

    @property
    def TargetX(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TargetX")

    @TargetX.setter
    def TargetX(self, value):
        return self.__setattr__("TargetX")

    @property
    def TargetY(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TargetY")

    @TargetY.setter
    def TargetY(self, value):
        return self.__setattr__("TargetY")

    @property
    def TargetZ(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("TargetZ")

    @TargetZ.setter
    def TargetZ(self, value):
        return self.__setattr__("TargetZ")

    @property
    def SettingInputHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SettingInputHash")

    @SettingInputHash.setter
    def SettingInputHash(self, value):
        return self.__setattr__("SettingInputHash")

    @property
    def SettingOutputHash(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("SettingOutputHash")

    @SettingOutputHash.setter
    def SettingOutputHash(self, value):
        return self.__setattr__("SettingOutputHash")

    @property
    def Channel(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Channel")

    @Channel.setter
    def Channel(self, value):
        return self.__setattr__("Channel")

    @property
    def Unknown(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Unknown")

    @Unknown.setter
    def Unknown(self, value):
        return self.__setattr__("Unknown")

    @property
    def Time(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Time")

    @Time.setter
    def Time(self, value):
        return self.__setattr__("Time")

    @property
    def Bpm(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("Bpm")

    @Bpm.setter
    def Bpm(self, value):
        return self.__setattr__("Bpm")

    @property
    def EnvironmentEfficiency(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("EnvironmentEfficiency")

    @EnvironmentEfficiency.setter
    def EnvironmentEfficiency(self, value):
        return self.__setattr__("EnvironmentEfficiency")

    @property
    def WorkingGasEfficiency(self) -> "stationeers_pytrapic.types._DevicesLogicType":
        return self.__getattr__("WorkingGasEfficiency")

    @WorkingGasEfficiency.setter
    def WorkingGasEfficiency(self, value):
        return self.__setattr__("WorkingGasEfficiency")


class _GenericStructure:

    @property
    def None_(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("None_")

    @None_.setter
    def None_(self, value):
        return self.__setattr__("None_")

    @property
    def Power(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Power")

    @Power.setter
    def Power(self, value):
        return self.__setattr__("Power")

    @property
    def Open(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Open")

    @Open.setter
    def Open(self, value):
        return self.__setattr__("Open")

    @property
    def Mode(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Mode")

    @Mode.setter
    def Mode(self, value):
        return self.__setattr__("Mode")

    @property
    def Error(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Error")

    @Error.setter
    def Error(self, value):
        return self.__setattr__("Error")

    @property
    def Flush(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Flush")

    @Flush.setter
    def Flush(self, value):
        return self.__setattr__("Flush")

    @property
    def SoundAlert(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SoundAlert")

    @SoundAlert.setter
    def SoundAlert(self, value):
        return self.__setattr__("SoundAlert")

    @property
    def VolumeOfLiquid(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("VolumeOfLiquid")

    @VolumeOfLiquid.setter
    def VolumeOfLiquid(self, value):
        return self.__setattr__("VolumeOfLiquid")

    @property
    def Lock(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Lock")

    @Lock.setter
    def Lock(self, value):
        return self.__setattr__("Lock")

    @property
    def Pressure(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Pressure")

    @Pressure.setter
    def Pressure(self, value):
        return self.__setattr__("Pressure")

    @property
    def Temperature(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Temperature")

    @Temperature.setter
    def Temperature(self, value):
        return self.__setattr__("Temperature")

    @property
    def PressureInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureInput")

    @PressureInput.setter
    def PressureInput(self, value):
        return self.__setattr__("PressureInput")

    @property
    def TemperatureInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TemperatureInput")

    @TemperatureInput.setter
    def TemperatureInput(self, value):
        return self.__setattr__("TemperatureInput")

    @property
    def PressureInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureInput2")

    @PressureInput2.setter
    def PressureInput2(self, value):
        return self.__setattr__("PressureInput2")

    @property
    def TemperatureInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TemperatureInput2")

    @TemperatureInput2.setter
    def TemperatureInput2(self, value):
        return self.__setattr__("TemperatureInput2")

    @property
    def PressureOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureOutput")

    @PressureOutput.setter
    def PressureOutput(self, value):
        return self.__setattr__("PressureOutput")

    @property
    def TargetPadIndex(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TargetPadIndex")

    @TargetPadIndex.setter
    def TargetPadIndex(self, value):
        return self.__setattr__("TargetPadIndex")

    @property
    def InterrogationProgress(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("InterrogationProgress")

    @InterrogationProgress.setter
    def InterrogationProgress(self, value):
        return self.__setattr__("InterrogationProgress")

    @property
    def SizeX(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SizeX")

    @SizeX.setter
    def SizeX(self, value):
        return self.__setattr__("SizeX")

    @property
    def SizeY(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SizeY")

    @SizeY.setter
    def SizeY(self, value):
        return self.__setattr__("SizeY")

    @property
    def SizeZ(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SizeZ")

    @SizeZ.setter
    def SizeZ(self, value):
        return self.__setattr__("SizeZ")

    @property
    def MinWattsToContact(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("MinWattsToContact")

    @MinWattsToContact.setter
    def MinWattsToContact(self, value):
        return self.__setattr__("MinWattsToContact")

    @property
    def WattsReachingContact(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("WattsReachingContact")

    @WattsReachingContact.setter
    def WattsReachingContact(self, value):
        return self.__setattr__("WattsReachingContact")

    @property
    def LineNumber(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("LineNumber")

    @LineNumber.setter
    def LineNumber(self, value):
        return self.__setattr__("LineNumber")

    @property
    def TemperatureOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TemperatureOutput")

    @TemperatureOutput.setter
    def TemperatureOutput(self, value):
        return self.__setattr__("TemperatureOutput")

    @property
    def PressureOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureOutput2")

    @PressureOutput2.setter
    def PressureOutput2(self, value):
        return self.__setattr__("PressureOutput2")

    @property
    def TemperatureOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TemperatureOutput2")

    @TemperatureOutput2.setter
    def TemperatureOutput2(self, value):
        return self.__setattr__("TemperatureOutput2")

    @property
    def PressureExternal(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureExternal")

    @PressureExternal.setter
    def PressureExternal(self, value):
        return self.__setattr__("PressureExternal")

    @property
    def PressureInternal(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureInternal")

    @PressureInternal.setter
    def PressureInternal(self, value):
        return self.__setattr__("PressureInternal")

    @property
    def Activate(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Activate")

    @Activate.setter
    def Activate(self, value):
        return self.__setattr__("Activate")

    @property
    def Charge(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Charge")

    @Charge.setter
    def Charge(self, value):
        return self.__setattr__("Charge")

    @property
    def Setting(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Setting")

    @Setting.setter
    def Setting(self, value):
        return self.__setattr__("Setting")

    @property
    def Reagents(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Reagents")

    @Reagents.setter
    def Reagents(self, value):
        return self.__setattr__("Reagents")

    @property
    def RatioOxygen(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioOxygen")

    @RatioOxygen.setter
    def RatioOxygen(self, value):
        return self.__setattr__("RatioOxygen")

    @property
    def RatioCarbonDioxide(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioCarbonDioxide")

    @RatioCarbonDioxide.setter
    def RatioCarbonDioxide(self, value):
        return self.__setattr__("RatioCarbonDioxide")

    @property
    def RatioNitrogen(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrogen")

    @RatioNitrogen.setter
    def RatioNitrogen(self, value):
        return self.__setattr__("RatioNitrogen")

    @property
    def RatioPollutant(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioPollutant")

    @RatioPollutant.setter
    def RatioPollutant(self, value):
        return self.__setattr__("RatioPollutant")

    @property
    def RatioVolatiles(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioVolatiles")

    @RatioVolatiles.setter
    def RatioVolatiles(self, value):
        return self.__setattr__("RatioVolatiles")

    @property
    def RatioWater(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioWater")

    @RatioWater.setter
    def RatioWater(self, value):
        return self.__setattr__("RatioWater")

    @property
    def RatioPollutedWater(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioPollutedWater")

    @RatioPollutedWater.setter
    def RatioPollutedWater(self, value):
        return self.__setattr__("RatioPollutedWater")

    @property
    def RatioNitrousOxide(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrousOxide")

    @RatioNitrousOxide.setter
    def RatioNitrousOxide(self, value):
        return self.__setattr__("RatioNitrousOxide")

    @property
    def RatioLiquidNitrogen(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrogen")

    @RatioLiquidNitrogen.setter
    def RatioLiquidNitrogen(self, value):
        return self.__setattr__("RatioLiquidNitrogen")

    @property
    def Combustion(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Combustion")

    @Combustion.setter
    def Combustion(self, value):
        return self.__setattr__("Combustion")

    @property
    def RatioOxygenInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioOxygenInput")

    @RatioOxygenInput.setter
    def RatioOxygenInput(self, value):
        return self.__setattr__("RatioOxygenInput")

    @property
    def RatioCarbonDioxideInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioCarbonDioxideInput")

    @RatioCarbonDioxideInput.setter
    def RatioCarbonDioxideInput(self, value):
        return self.__setattr__("RatioCarbonDioxideInput")

    @property
    def RatioNitrogenInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrogenInput")

    @RatioNitrogenInput.setter
    def RatioNitrogenInput(self, value):
        return self.__setattr__("RatioNitrogenInput")

    @property
    def RatioPollutantInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioPollutantInput")

    @RatioPollutantInput.setter
    def RatioPollutantInput(self, value):
        return self.__setattr__("RatioPollutantInput")

    @property
    def RatioVolatilesInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioVolatilesInput")

    @RatioVolatilesInput.setter
    def RatioVolatilesInput(self, value):
        return self.__setattr__("RatioVolatilesInput")

    @property
    def RatioWaterInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioWaterInput")

    @RatioWaterInput.setter
    def RatioWaterInput(self, value):
        return self.__setattr__("RatioWaterInput")

    @property
    def RatioNitrousOxideInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrousOxideInput")

    @RatioNitrousOxideInput.setter
    def RatioNitrousOxideInput(self, value):
        return self.__setattr__("RatioNitrousOxideInput")

    @property
    def RatioLiquidNitrogenInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrogenInput")

    @RatioLiquidNitrogenInput.setter
    def RatioLiquidNitrogenInput(self, value):
        return self.__setattr__("RatioLiquidNitrogenInput")

    @property
    def CombustionInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CombustionInput")

    @CombustionInput.setter
    def CombustionInput(self, value):
        return self.__setattr__("CombustionInput")

    @property
    def RatioOxygenInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioOxygenInput2")

    @RatioOxygenInput2.setter
    def RatioOxygenInput2(self, value):
        return self.__setattr__("RatioOxygenInput2")

    @property
    def RatioCarbonDioxideInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioCarbonDioxideInput2")

    @RatioCarbonDioxideInput2.setter
    def RatioCarbonDioxideInput2(self, value):
        return self.__setattr__("RatioCarbonDioxideInput2")

    @property
    def RatioNitrogenInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrogenInput2")

    @RatioNitrogenInput2.setter
    def RatioNitrogenInput2(self, value):
        return self.__setattr__("RatioNitrogenInput2")

    @property
    def RatioPollutantInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioPollutantInput2")

    @RatioPollutantInput2.setter
    def RatioPollutantInput2(self, value):
        return self.__setattr__("RatioPollutantInput2")

    @property
    def RatioVolatilesInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioVolatilesInput2")

    @RatioVolatilesInput2.setter
    def RatioVolatilesInput2(self, value):
        return self.__setattr__("RatioVolatilesInput2")

    @property
    def RatioWaterInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioWaterInput2")

    @RatioWaterInput2.setter
    def RatioWaterInput2(self, value):
        return self.__setattr__("RatioWaterInput2")

    @property
    def RatioNitrousOxideInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrousOxideInput2")

    @RatioNitrousOxideInput2.setter
    def RatioNitrousOxideInput2(self, value):
        return self.__setattr__("RatioNitrousOxideInput2")

    @property
    def RatioLiquidNitrogenInput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrogenInput2")

    @RatioLiquidNitrogenInput2.setter
    def RatioLiquidNitrogenInput2(self, value):
        return self.__setattr__("RatioLiquidNitrogenInput2")

    @property
    def CombustionInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CombustionInput2")

    @CombustionInput2.setter
    def CombustionInput2(self, value):
        return self.__setattr__("CombustionInput2")

    @property
    def RatioOxygenOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioOxygenOutput")

    @RatioOxygenOutput.setter
    def RatioOxygenOutput(self, value):
        return self.__setattr__("RatioOxygenOutput")

    @property
    def RatioCarbonDioxideOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioCarbonDioxideOutput")

    @RatioCarbonDioxideOutput.setter
    def RatioCarbonDioxideOutput(self, value):
        return self.__setattr__("RatioCarbonDioxideOutput")

    @property
    def RatioNitrogenOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrogenOutput")

    @RatioNitrogenOutput.setter
    def RatioNitrogenOutput(self, value):
        return self.__setattr__("RatioNitrogenOutput")

    @property
    def RatioPollutantOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioPollutantOutput")

    @RatioPollutantOutput.setter
    def RatioPollutantOutput(self, value):
        return self.__setattr__("RatioPollutantOutput")

    @property
    def RatioVolatilesOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioVolatilesOutput")

    @RatioVolatilesOutput.setter
    def RatioVolatilesOutput(self, value):
        return self.__setattr__("RatioVolatilesOutput")

    @property
    def RatioWaterOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioWaterOutput")

    @RatioWaterOutput.setter
    def RatioWaterOutput(self, value):
        return self.__setattr__("RatioWaterOutput")

    @property
    def RatioNitrousOxideOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrousOxideOutput")

    @RatioNitrousOxideOutput.setter
    def RatioNitrousOxideOutput(self, value):
        return self.__setattr__("RatioNitrousOxideOutput")

    @property
    def RatioLiquidNitrogenOutput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrogenOutput")

    @RatioLiquidNitrogenOutput.setter
    def RatioLiquidNitrogenOutput(self, value):
        return self.__setattr__("RatioLiquidNitrogenOutput")

    @property
    def CombustionOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CombustionOutput")

    @CombustionOutput.setter
    def CombustionOutput(self, value):
        return self.__setattr__("CombustionOutput")

    @property
    def RatioOxygenOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioOxygenOutput2")

    @RatioOxygenOutput2.setter
    def RatioOxygenOutput2(self, value):
        return self.__setattr__("RatioOxygenOutput2")

    @property
    def RatioCarbonDioxideOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioCarbonDioxideOutput2")

    @RatioCarbonDioxideOutput2.setter
    def RatioCarbonDioxideOutput2(self, value):
        return self.__setattr__("RatioCarbonDioxideOutput2")

    @property
    def RatioNitrogenOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrogenOutput2")

    @RatioNitrogenOutput2.setter
    def RatioNitrogenOutput2(self, value):
        return self.__setattr__("RatioNitrogenOutput2")

    @property
    def RatioPollutantOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioPollutantOutput2")

    @RatioPollutantOutput2.setter
    def RatioPollutantOutput2(self, value):
        return self.__setattr__("RatioPollutantOutput2")

    @property
    def RatioVolatilesOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioVolatilesOutput2")

    @RatioVolatilesOutput2.setter
    def RatioVolatilesOutput2(self, value):
        return self.__setattr__("RatioVolatilesOutput2")

    @property
    def RatioWaterOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioWaterOutput2")

    @RatioWaterOutput2.setter
    def RatioWaterOutput2(self, value):
        return self.__setattr__("RatioWaterOutput2")

    @property
    def RatioNitrousOxideOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioNitrousOxideOutput2")

    @RatioNitrousOxideOutput2.setter
    def RatioNitrousOxideOutput2(self, value):
        return self.__setattr__("RatioNitrousOxideOutput2")

    @property
    def RatioLiquidNitrogenOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrogenOutput2")

    @RatioLiquidNitrogenOutput2.setter
    def RatioLiquidNitrogenOutput2(self, value):
        return self.__setattr__("RatioLiquidNitrogenOutput2")

    @property
    def CombustionOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CombustionOutput2")

    @CombustionOutput2.setter
    def CombustionOutput2(self, value):
        return self.__setattr__("CombustionOutput2")

    @property
    def Horizontal(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Horizontal")

    @Horizontal.setter
    def Horizontal(self, value):
        return self.__setattr__("Horizontal")

    @property
    def Vertical(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Vertical")

    @Vertical.setter
    def Vertical(self, value):
        return self.__setattr__("Vertical")

    @property
    def SolarAngle(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SolarAngle")

    @SolarAngle.setter
    def SolarAngle(self, value):
        return self.__setattr__("SolarAngle")

    @property
    def SolarConstant(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SolarConstant")

    @SolarConstant.setter
    def SolarConstant(self, value):
        return self.__setattr__("SolarConstant")

    @property
    def Maximum(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Maximum")

    @Maximum.setter
    def Maximum(self, value):
        return self.__setattr__("Maximum")

    @property
    def Ratio(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Ratio")

    @Ratio.setter
    def Ratio(self, value):
        return self.__setattr__("Ratio")

    @property
    def PowerPotential(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PowerPotential")

    @PowerPotential.setter
    def PowerPotential(self, value):
        return self.__setattr__("PowerPotential")

    @property
    def PowerActual(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PowerActual")

    @PowerActual.setter
    def PowerActual(self, value):
        return self.__setattr__("PowerActual")

    @property
    def Quantity(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Quantity")

    @Quantity.setter
    def Quantity(self, value):
        return self.__setattr__("Quantity")

    @property
    def On(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("On")

    @On.setter
    def On(self, value):
        return self.__setattr__("On")

    @property
    def ImportQuantity(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ImportQuantity")

    @ImportQuantity.setter
    def ImportQuantity(self, value):
        return self.__setattr__("ImportQuantity")

    @property
    def ImportSlotOccupant(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ImportSlotOccupant")

    @ImportSlotOccupant.setter
    def ImportSlotOccupant(self, value):
        return self.__setattr__("ImportSlotOccupant")

    @property
    def ExportQuantity(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ExportQuantity")

    @ExportQuantity.setter
    def ExportQuantity(self, value):
        return self.__setattr__("ExportQuantity")

    @property
    def ExportSlotOccupant(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ExportSlotOccupant")

    @ExportSlotOccupant.setter
    def ExportSlotOccupant(self, value):
        return self.__setattr__("ExportSlotOccupant")

    @property
    def RequiredPower(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RequiredPower")

    @RequiredPower.setter
    def RequiredPower(self, value):
        return self.__setattr__("RequiredPower")

    @property
    def HorizontalRatio(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("HorizontalRatio")

    @HorizontalRatio.setter
    def HorizontalRatio(self, value):
        return self.__setattr__("HorizontalRatio")

    @property
    def VerticalRatio(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("VerticalRatio")

    @VerticalRatio.setter
    def VerticalRatio(self, value):
        return self.__setattr__("VerticalRatio")

    @property
    def PowerRequired(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PowerRequired")

    @PowerRequired.setter
    def PowerRequired(self, value):
        return self.__setattr__("PowerRequired")

    @property
    def Idle(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Idle")

    @Idle.setter
    def Idle(self, value):
        return self.__setattr__("Idle")

    @property
    def Color(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Color")

    @Color.setter
    def Color(self, value):
        return self.__setattr__("Color")

    @property
    def ElevatorSpeed(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ElevatorSpeed")

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value):
        return self.__setattr__("ElevatorSpeed")

    @property
    def ElevatorLevel(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ElevatorLevel")

    @ElevatorLevel.setter
    def ElevatorLevel(self, value):
        return self.__setattr__("ElevatorLevel")

    @property
    def RecipeHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RecipeHash")

    @RecipeHash.setter
    def RecipeHash(self, value):
        return self.__setattr__("RecipeHash")

    @property
    def ExportSlotHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ExportSlotHash")

    @ExportSlotHash.setter
    def ExportSlotHash(self, value):
        return self.__setattr__("ExportSlotHash")

    @property
    def ImportSlotHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ImportSlotHash")

    @ImportSlotHash.setter
    def ImportSlotHash(self, value):
        return self.__setattr__("ImportSlotHash")

    @property
    def PlantHealth1(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHealth1")

    @PlantHealth1.setter
    def PlantHealth1(self, value):
        return self.__setattr__("PlantHealth1")

    @property
    def PlantHealth2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHealth2")

    @PlantHealth2.setter
    def PlantHealth2(self, value):
        return self.__setattr__("PlantHealth2")

    @property
    def PlantHealth3(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHealth3")

    @PlantHealth3.setter
    def PlantHealth3(self, value):
        return self.__setattr__("PlantHealth3")

    @property
    def PlantHealth4(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHealth4")

    @PlantHealth4.setter
    def PlantHealth4(self, value):
        return self.__setattr__("PlantHealth4")

    @property
    def PlantGrowth1(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantGrowth1")

    @PlantGrowth1.setter
    def PlantGrowth1(self, value):
        return self.__setattr__("PlantGrowth1")

    @property
    def PlantGrowth2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantGrowth2")

    @PlantGrowth2.setter
    def PlantGrowth2(self, value):
        return self.__setattr__("PlantGrowth2")

    @property
    def PlantGrowth3(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantGrowth3")

    @PlantGrowth3.setter
    def PlantGrowth3(self, value):
        return self.__setattr__("PlantGrowth3")

    @property
    def PlantGrowth4(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantGrowth4")

    @PlantGrowth4.setter
    def PlantGrowth4(self, value):
        return self.__setattr__("PlantGrowth4")

    @property
    def PlantEfficiency1(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantEfficiency1")

    @PlantEfficiency1.setter
    def PlantEfficiency1(self, value):
        return self.__setattr__("PlantEfficiency1")

    @property
    def PlantEfficiency2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantEfficiency2")

    @PlantEfficiency2.setter
    def PlantEfficiency2(self, value):
        return self.__setattr__("PlantEfficiency2")

    @property
    def PlantEfficiency3(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantEfficiency3")

    @PlantEfficiency3.setter
    def PlantEfficiency3(self, value):
        return self.__setattr__("PlantEfficiency3")

    @property
    def PlantEfficiency4(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantEfficiency4")

    @PlantEfficiency4.setter
    def PlantEfficiency4(self, value):
        return self.__setattr__("PlantEfficiency4")

    @property
    def PlantHash1(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHash1")

    @PlantHash1.setter
    def PlantHash1(self, value):
        return self.__setattr__("PlantHash1")

    @property
    def PlantHash2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHash2")

    @PlantHash2.setter
    def PlantHash2(self, value):
        return self.__setattr__("PlantHash2")

    @property
    def PlantHash3(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHash3")

    @PlantHash3.setter
    def PlantHash3(self, value):
        return self.__setattr__("PlantHash3")

    @property
    def PlantHash4(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PlantHash4")

    @PlantHash4.setter
    def PlantHash4(self, value):
        return self.__setattr__("PlantHash4")

    @property
    def RequestHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RequestHash")

    @RequestHash.setter
    def RequestHash(self, value):
        return self.__setattr__("RequestHash")

    @property
    def CompletionRatio(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CompletionRatio")

    @CompletionRatio.setter
    def CompletionRatio(self, value):
        return self.__setattr__("CompletionRatio")

    @property
    def ClearMemory(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ClearMemory")

    @ClearMemory.setter
    def ClearMemory(self, value):
        return self.__setattr__("ClearMemory")

    @property
    def ExportCount(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ExportCount")

    @ExportCount.setter
    def ExportCount(self, value):
        return self.__setattr__("ExportCount")

    @property
    def ImportCount(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ImportCount")

    @ImportCount.setter
    def ImportCount(self, value):
        return self.__setattr__("ImportCount")

    @property
    def PowerGeneration(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PowerGeneration")

    @PowerGeneration.setter
    def PowerGeneration(self, value):
        return self.__setattr__("PowerGeneration")

    @property
    def TotalMoles(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TotalMoles")

    @TotalMoles.setter
    def TotalMoles(self, value):
        return self.__setattr__("TotalMoles")

    @property
    def TotalMolesInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TotalMolesInput")

    @TotalMolesInput.setter
    def TotalMolesInput(self, value):
        return self.__setattr__("TotalMolesInput")

    @property
    def TotalMolesInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TotalMolesInput2")

    @TotalMolesInput2.setter
    def TotalMolesInput2(self, value):
        return self.__setattr__("TotalMolesInput2")

    @property
    def TotalMolesOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TotalMolesOutput")

    @TotalMolesOutput.setter
    def TotalMolesOutput(self, value):
        return self.__setattr__("TotalMolesOutput")

    @property
    def TotalMolesOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TotalMolesOutput2")

    @TotalMolesOutput2.setter
    def TotalMolesOutput2(self, value):
        return self.__setattr__("TotalMolesOutput2")

    @property
    def Volume(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Volume")

    @Volume.setter
    def Volume(self, value):
        return self.__setattr__("Volume")

    @property
    def Plant(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Plant")

    @Plant.setter
    def Plant(self, value):
        return self.__setattr__("Plant")

    @property
    def Harvest(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Harvest")

    @Harvest.setter
    def Harvest(self, value):
        return self.__setattr__("Harvest")

    @property
    def Output(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Output")

    @Output.setter
    def Output(self, value):
        return self.__setattr__("Output")

    @property
    def PressureSetting(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureSetting")

    @PressureSetting.setter
    def PressureSetting(self, value):
        return self.__setattr__("PressureSetting")

    @property
    def TemperatureSetting(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TemperatureSetting")

    @TemperatureSetting.setter
    def TemperatureSetting(self, value):
        return self.__setattr__("TemperatureSetting")

    @property
    def TemperatureExternal(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TemperatureExternal")

    @TemperatureExternal.setter
    def TemperatureExternal(self, value):
        return self.__setattr__("TemperatureExternal")

    @property
    def Filtration(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Filtration")

    @Filtration.setter
    def Filtration(self, value):
        return self.__setattr__("Filtration")

    @property
    def AirRelease(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("AirRelease")

    @AirRelease.setter
    def AirRelease(self, value):
        return self.__setattr__("AirRelease")

    @property
    def PositionX(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PositionX")

    @PositionX.setter
    def PositionX(self, value):
        return self.__setattr__("PositionX")

    @property
    def PositionY(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PositionY")

    @PositionY.setter
    def PositionY(self, value):
        return self.__setattr__("PositionY")

    @property
    def PositionZ(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PositionZ")

    @PositionZ.setter
    def PositionZ(self, value):
        return self.__setattr__("PositionZ")

    @property
    def VelocityMagnitude(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("VelocityMagnitude")

    @VelocityMagnitude.setter
    def VelocityMagnitude(self, value):
        return self.__setattr__("VelocityMagnitude")

    @property
    def VelocityRelativeX(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("VelocityRelativeX")

    @VelocityRelativeX.setter
    def VelocityRelativeX(self, value):
        return self.__setattr__("VelocityRelativeX")

    @property
    def VelocityRelativeY(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("VelocityRelativeY")

    @VelocityRelativeY.setter
    def VelocityRelativeY(self, value):
        return self.__setattr__("VelocityRelativeY")

    @property
    def VelocityRelativeZ(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("VelocityRelativeZ")

    @VelocityRelativeZ.setter
    def VelocityRelativeZ(self, value):
        return self.__setattr__("VelocityRelativeZ")

    @property
    def PrefabHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PrefabHash")

    @PrefabHash.setter
    def PrefabHash(self, value):
        return self.__setattr__("PrefabHash")

    @property
    def ForceWrite(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ForceWrite")

    @ForceWrite.setter
    def ForceWrite(self, value):
        return self.__setattr__("ForceWrite")

    @property
    def SignalStrength(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SignalStrength")

    @SignalStrength.setter
    def SignalStrength(self, value):
        return self.__setattr__("SignalStrength")

    @property
    def SignalID(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SignalID")

    @SignalID.setter
    def SignalID(self, value):
        return self.__setattr__("SignalID")

    @property
    def OperationalTemperatureEfficiency(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("OperationalTemperatureEfficiency")

    @OperationalTemperatureEfficiency.setter
    def OperationalTemperatureEfficiency(self, value):
        return self.__setattr__("OperationalTemperatureEfficiency")

    @property
    def TemperatureDifferentialEfficiency(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TemperatureDifferentialEfficiency")

    @TemperatureDifferentialEfficiency.setter
    def TemperatureDifferentialEfficiency(self, value):
        return self.__setattr__("TemperatureDifferentialEfficiency")

    @property
    def CombustionLimiter(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("CombustionLimiter")

    @CombustionLimiter.setter
    def CombustionLimiter(self, value):
        return self.__setattr__("CombustionLimiter")

    @property
    def Throttle(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Throttle")

    @Throttle.setter
    def Throttle(self, value):
        return self.__setattr__("Throttle")

    @property
    def Rpm(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Rpm")

    @Rpm.setter
    def Rpm(self, value):
        return self.__setattr__("Rpm")

    @property
    def Stress(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Stress")

    @Stress.setter
    def Stress(self, value):
        return self.__setattr__("Stress")

    @property
    def PressureEfficiency(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("PressureEfficiency")

    @PressureEfficiency.setter
    def PressureEfficiency(self, value):
        return self.__setattr__("PressureEfficiency")

    @property
    def RatioLiquidOxygen(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidOxygen")

    @RatioLiquidOxygen.setter
    def RatioLiquidOxygen(self, value):
        return self.__setattr__("RatioLiquidOxygen")

    @property
    def RatioLiquidOxygenInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidOxygenInput")

    @RatioLiquidOxygenInput.setter
    def RatioLiquidOxygenInput(self, value):
        return self.__setattr__("RatioLiquidOxygenInput")

    @property
    def RatioLiquidOxygenInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidOxygenInput2")

    @RatioLiquidOxygenInput2.setter
    def RatioLiquidOxygenInput2(self, value):
        return self.__setattr__("RatioLiquidOxygenInput2")

    @property
    def RatioLiquidOxygenOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidOxygenOutput")

    @RatioLiquidOxygenOutput.setter
    def RatioLiquidOxygenOutput(self, value):
        return self.__setattr__("RatioLiquidOxygenOutput")

    @property
    def RatioLiquidOxygenOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidOxygenOutput2")

    @RatioLiquidOxygenOutput2.setter
    def RatioLiquidOxygenOutput2(self, value):
        return self.__setattr__("RatioLiquidOxygenOutput2")

    @property
    def RatioLiquidVolatiles(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidVolatiles")

    @RatioLiquidVolatiles.setter
    def RatioLiquidVolatiles(self, value):
        return self.__setattr__("RatioLiquidVolatiles")

    @property
    def RatioLiquidVolatilesInput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidVolatilesInput")

    @RatioLiquidVolatilesInput.setter
    def RatioLiquidVolatilesInput(self, value):
        return self.__setattr__("RatioLiquidVolatilesInput")

    @property
    def RatioLiquidVolatilesInput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidVolatilesInput2")

    @RatioLiquidVolatilesInput2.setter
    def RatioLiquidVolatilesInput2(self, value):
        return self.__setattr__("RatioLiquidVolatilesInput2")

    @property
    def RatioLiquidVolatilesOutput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidVolatilesOutput")

    @RatioLiquidVolatilesOutput.setter
    def RatioLiquidVolatilesOutput(self, value):
        return self.__setattr__("RatioLiquidVolatilesOutput")

    @property
    def RatioLiquidVolatilesOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidVolatilesOutput2")

    @RatioLiquidVolatilesOutput2.setter
    def RatioLiquidVolatilesOutput2(self, value):
        return self.__setattr__("RatioLiquidVolatilesOutput2")

    @property
    def RatioSteam(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioSteam")

    @RatioSteam.setter
    def RatioSteam(self, value):
        return self.__setattr__("RatioSteam")

    @property
    def RatioSteamInput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioSteamInput")

    @RatioSteamInput.setter
    def RatioSteamInput(self, value):
        return self.__setattr__("RatioSteamInput")

    @property
    def RatioSteamInput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioSteamInput2")

    @RatioSteamInput2.setter
    def RatioSteamInput2(self, value):
        return self.__setattr__("RatioSteamInput2")

    @property
    def RatioSteamOutput(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioSteamOutput")

    @RatioSteamOutput.setter
    def RatioSteamOutput(self, value):
        return self.__setattr__("RatioSteamOutput")

    @property
    def RatioSteamOutput2(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioSteamOutput2")

    @RatioSteamOutput2.setter
    def RatioSteamOutput2(self, value):
        return self.__setattr__("RatioSteamOutput2")

    @property
    def RatioLiquidCarbonDioxide(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxide")

    @RatioLiquidCarbonDioxide.setter
    def RatioLiquidCarbonDioxide(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxide")

    @property
    def RatioLiquidCarbonDioxideInput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideInput")

    @RatioLiquidCarbonDioxideInput.setter
    def RatioLiquidCarbonDioxideInput(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideInput")

    @property
    def RatioLiquidCarbonDioxideInput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideInput2")

    @RatioLiquidCarbonDioxideInput2.setter
    def RatioLiquidCarbonDioxideInput2(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideInput2")

    @property
    def RatioLiquidCarbonDioxideOutput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideOutput")

    @RatioLiquidCarbonDioxideOutput.setter
    def RatioLiquidCarbonDioxideOutput(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideOutput")

    @property
    def RatioLiquidCarbonDioxideOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidCarbonDioxideOutput2")

    @RatioLiquidCarbonDioxideOutput2.setter
    def RatioLiquidCarbonDioxideOutput2(self, value):
        return self.__setattr__("RatioLiquidCarbonDioxideOutput2")

    @property
    def RatioLiquidPollutant(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidPollutant")

    @RatioLiquidPollutant.setter
    def RatioLiquidPollutant(self, value):
        return self.__setattr__("RatioLiquidPollutant")

    @property
    def RatioLiquidPollutantInput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidPollutantInput")

    @RatioLiquidPollutantInput.setter
    def RatioLiquidPollutantInput(self, value):
        return self.__setattr__("RatioLiquidPollutantInput")

    @property
    def RatioLiquidPollutantInput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidPollutantInput2")

    @RatioLiquidPollutantInput2.setter
    def RatioLiquidPollutantInput2(self, value):
        return self.__setattr__("RatioLiquidPollutantInput2")

    @property
    def RatioLiquidPollutantOutput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidPollutantOutput")

    @RatioLiquidPollutantOutput.setter
    def RatioLiquidPollutantOutput(self, value):
        return self.__setattr__("RatioLiquidPollutantOutput")

    @property
    def RatioLiquidPollutantOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidPollutantOutput2")

    @RatioLiquidPollutantOutput2.setter
    def RatioLiquidPollutantOutput2(self, value):
        return self.__setattr__("RatioLiquidPollutantOutput2")

    @property
    def RatioLiquidNitrousOxide(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrousOxide")

    @RatioLiquidNitrousOxide.setter
    def RatioLiquidNitrousOxide(self, value):
        return self.__setattr__("RatioLiquidNitrousOxide")

    @property
    def RatioLiquidNitrousOxideInput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideInput")

    @RatioLiquidNitrousOxideInput.setter
    def RatioLiquidNitrousOxideInput(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideInput")

    @property
    def RatioLiquidNitrousOxideInput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideInput2")

    @RatioLiquidNitrousOxideInput2.setter
    def RatioLiquidNitrousOxideInput2(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideInput2")

    @property
    def RatioLiquidNitrousOxideOutput(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideOutput")

    @RatioLiquidNitrousOxideOutput.setter
    def RatioLiquidNitrousOxideOutput(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideOutput")

    @property
    def RatioLiquidNitrousOxideOutput2(
        self,
    ) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidNitrousOxideOutput2")

    @RatioLiquidNitrousOxideOutput2.setter
    def RatioLiquidNitrousOxideOutput2(self, value):
        return self.__setattr__("RatioLiquidNitrousOxideOutput2")

    @property
    def RatioHydrogen(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioHydrogen")

    @RatioHydrogen.setter
    def RatioHydrogen(self, value):
        return self.__setattr__("RatioHydrogen")

    @property
    def RatioLiquidHydrogen(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("RatioLiquidHydrogen")

    @RatioLiquidHydrogen.setter
    def RatioLiquidHydrogen(self, value):
        return self.__setattr__("RatioLiquidHydrogen")

    @property
    def ContactTypeId(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ContactTypeId")

    @ContactTypeId.setter
    def ContactTypeId(self, value):
        return self.__setattr__("ContactTypeId")

    @property
    def Bypass(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Bypass")

    @Bypass.setter
    def Bypass(self, value):
        return self.__setattr__("Bypass")

    @property
    def Progress(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Progress")

    @Progress.setter
    def Progress(self, value):
        return self.__setattr__("Progress")

    @property
    def DestinationCode(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("DestinationCode")

    @DestinationCode.setter
    def DestinationCode(self, value):
        return self.__setattr__("DestinationCode")

    @property
    def Acceleration(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Acceleration")

    @Acceleration.setter
    def Acceleration(self, value):
        return self.__setattr__("Acceleration")

    @property
    def AutoShutOff(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("AutoShutOff")

    @AutoShutOff.setter
    def AutoShutOff(self, value):
        return self.__setattr__("AutoShutOff")

    @property
    def Thrust(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Thrust")

    @Thrust.setter
    def Thrust(self, value):
        return self.__setattr__("Thrust")

    @property
    def ThrustToWeight(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("ThrustToWeight")

    @ThrustToWeight.setter
    def ThrustToWeight(self, value):
        return self.__setattr__("ThrustToWeight")

    @property
    def Weight(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Weight")

    @Weight.setter
    def Weight(self, value):
        return self.__setattr__("Weight")

    @property
    def OverShootTarget(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("OverShootTarget")

    @OverShootTarget.setter
    def OverShootTarget(self, value):
        return self.__setattr__("OverShootTarget")

    @property
    def TimeToDestination(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TimeToDestination")

    @TimeToDestination.setter
    def TimeToDestination(self, value):
        return self.__setattr__("TimeToDestination")

    @property
    def BurnTimeRemaining(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("BurnTimeRemaining")

    @BurnTimeRemaining.setter
    def BurnTimeRemaining(self, value):
        return self.__setattr__("BurnTimeRemaining")

    @property
    def AutoLand(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("AutoLand")

    @AutoLand.setter
    def AutoLand(self, value):
        return self.__setattr__("AutoLand")

    @property
    def DryMass(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("DryMass")

    @DryMass.setter
    def DryMass(self, value):
        return self.__setattr__("DryMass")

    @property
    def Mass(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Mass")

    @Mass.setter
    def Mass(self, value):
        return self.__setattr__("Mass")

    @property
    def TargetX(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TargetX")

    @TargetX.setter
    def TargetX(self, value):
        return self.__setattr__("TargetX")

    @property
    def TargetY(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TargetY")

    @TargetY.setter
    def TargetY(self, value):
        return self.__setattr__("TargetY")

    @property
    def TargetZ(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("TargetZ")

    @TargetZ.setter
    def TargetZ(self, value):
        return self.__setattr__("TargetZ")

    @property
    def SettingInputHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SettingInputHash")

    @SettingInputHash.setter
    def SettingInputHash(self, value):
        return self.__setattr__("SettingInputHash")

    @property
    def SettingOutputHash(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("SettingOutputHash")

    @SettingOutputHash.setter
    def SettingOutputHash(self, value):
        return self.__setattr__("SettingOutputHash")

    @property
    def Channel(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Channel")

    @Channel.setter
    def Channel(self, value):
        return self.__setattr__("Channel")

    @property
    def Unknown(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Unknown")

    @Unknown.setter
    def Unknown(self, value):
        return self.__setattr__("Unknown")

    @property
    def Time(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Time")

    @Time.setter
    def Time(self, value):
        return self.__setattr__("Time")

    @property
    def Bpm(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("Bpm")

    @Bpm.setter
    def Bpm(self, value):
        return self.__setattr__("Bpm")

    @property
    def EnvironmentEfficiency(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("EnvironmentEfficiency")

    @EnvironmentEfficiency.setter
    def EnvironmentEfficiency(self, value):
        return self.__setattr__("EnvironmentEfficiency")

    @property
    def WorkingGasEfficiency(self) -> "stationeers_pytrapic.types._DeviceLogicType":
        return self.__getattr__("WorkingGasEfficiency")

    @WorkingGasEfficiency.setter
    def WorkingGasEfficiency(self, value):
        return self.__setattr__("WorkingGasEfficiency")


__all__ = ["_logicType", "_GenericStructures", "_GenericStructure", "_logicSlotType"]
