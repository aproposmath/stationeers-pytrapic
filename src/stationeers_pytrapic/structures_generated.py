from stationeers_pytrapic.types import (
    _DevicesLogicType,
    _DeviceLogicType,
    _BaseStructure,
    _BaseStructures,
    _DeviceSlotType,
    _DevicesSlotType,
    _BaseSlotType,
    _BaseSlotTypes,
    LogicType as _LT,
    LogicSlotType as _LST,
)


class _SlotTypeCommon(_BaseSlotType):
    @property
    def Class(self) -> float:
        return _DeviceSlotType(self, _LST.Class)

    @Class.setter
    def Class(self, value: int | float):
        pass

    @property
    def Damage(self) -> float:
        return _DeviceSlotType(self, _LST.Damage)

    @Damage.setter
    def Damage(self, value: int | float):
        pass

    @property
    def MaxQuantity(self) -> float:
        return _DeviceSlotType(self, _LST.MaxQuantity)

    @MaxQuantity.setter
    def MaxQuantity(self, value: int | float):
        pass

    @property
    def OccupantHash(self) -> float:
        return _DeviceSlotType(self, _LST.OccupantHash)

    @OccupantHash.setter
    def OccupantHash(self, value: int | float):
        pass

    @property
    def Occupied(self) -> float:
        return _DeviceSlotType(self, _LST.Occupied)

    @Occupied.setter
    def Occupied(self, value: int | float):
        pass

    @property
    def PrefabHash(self) -> float:
        return _DeviceSlotType(self, _LST.PrefabHash)

    @PrefabHash.setter
    def PrefabHash(self, value: int | float):
        pass

    @property
    def Quantity(self) -> float:
        return _DeviceSlotType(self, _LST.Quantity)

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass

    @property
    def ReferenceId(self) -> float:
        return _DeviceSlotType(self, _LST.ReferenceId)

    @ReferenceId.setter
    def ReferenceId(self, value: int | float):
        pass

    @property
    def SortingClass(self) -> float:
        return _DeviceSlotType(self, _LST.SortingClass)

    @SortingClass.setter
    def SortingClass(self, value: int | float):
        pass


class _SlotTypeCommons(_BaseSlotTypes):
    @property
    def Class(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Class)

    @Class.setter
    def Class(self, value: int | float):
        pass

    @property
    def Damage(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Damage)

    @Damage.setter
    def Damage(self, value: int | float):
        pass

    @property
    def MaxQuantity(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.MaxQuantity)

    @MaxQuantity.setter
    def MaxQuantity(self, value: int | float):
        pass

    @property
    def OccupantHash(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.OccupantHash)

    @OccupantHash.setter
    def OccupantHash(self, value: int | float):
        pass

    @property
    def Occupied(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Occupied)

    @Occupied.setter
    def Occupied(self, value: int | float):
        pass

    @property
    def PrefabHash(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.PrefabHash)

    @PrefabHash.setter
    def PrefabHash(self, value: int | float):
        pass

    @property
    def Quantity(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Quantity)

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass

    @property
    def ReferenceId(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.ReferenceId)

    @ReferenceId.setter
    def ReferenceId(self, value: int | float):
        pass

    @property
    def SortingClass(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.SortingClass)

    @SortingClass.setter
    def SortingClass(self, value: int | float):
        pass


class _SlotTypeAppliance(_SlotTypeCommon):
    @property
    def On(self) -> float:
        return _DeviceSlotType(self, _LST.On)

    @On.setter
    def On(self, value: int | float):
        pass


class _SlotTypeAppliances(_SlotTypeCommons):
    @property
    def On(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.On)

    @On.setter
    def On(self, value: int | float):
        pass


class _SlotTypeBack(_SlotTypeCommon):
    @property
    def Charge(self) -> float:
        return _DeviceSlotType(self, _LST.Charge)

    @Charge.setter
    def Charge(self, value: int | float):
        pass

    @property
    def ChargeRatio(self) -> float:
        return _DeviceSlotType(self, _LST.ChargeRatio)

    @ChargeRatio.setter
    def ChargeRatio(self, value: int | float):
        pass

    @property
    def Pressure(self) -> float:
        return _DeviceSlotType(self, _LST.Pressure)

    @Pressure.setter
    def Pressure(self, value: int | float):
        pass


class _SlotTypeBacks(_SlotTypeCommons):
    @property
    def Charge(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Charge)

    @Charge.setter
    def Charge(self, value: int | float):
        pass

    @property
    def ChargeRatio(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.ChargeRatio)

    @ChargeRatio.setter
    def ChargeRatio(self, value: int | float):
        pass

    @property
    def Pressure(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Pressure)

    @Pressure.setter
    def Pressure(self, value: int | float):
        pass


class _SlotTypeBattery(_SlotTypeCommon):
    @property
    def Charge(self) -> float:
        return _DeviceSlotType(self, _LST.Charge)

    @Charge.setter
    def Charge(self, value: int | float):
        pass

    @property
    def ChargeRatio(self) -> float:
        return _DeviceSlotType(self, _LST.ChargeRatio)

    @ChargeRatio.setter
    def ChargeRatio(self, value: int | float):
        pass


class _SlotTypeBatterys(_SlotTypeCommons):
    @property
    def Charge(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Charge)

    @Charge.setter
    def Charge(self, value: int | float):
        pass

    @property
    def ChargeRatio(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.ChargeRatio)

    @ChargeRatio.setter
    def ChargeRatio(self, value: int | float):
        pass


class _SlotTypeCircuitboard(_SlotTypeCommon):
    @property
    def Mode(self) -> float:
        return _DeviceSlotType(self, _LST.Mode)

    @Mode.setter
    def Mode(self, value: int | float):
        pass


class _SlotTypeCircuitboards(_SlotTypeCommons):
    @property
    def Mode(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Mode)

    @Mode.setter
    def Mode(self, value: int | float):
        pass


class _SlotTypeFilter(_SlotTypeCommon):
    @property
    def FilterType(self) -> float:
        return _DeviceSlotType(self, _LST.FilterType)

    @FilterType.setter
    def FilterType(self, value: int | float):
        pass


class _SlotTypeFilters(_SlotTypeCommons):
    @property
    def FilterType(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.FilterType)

    @FilterType.setter
    def FilterType(self, value: int | float):
        pass


class _SlotTypeGasCanister(_SlotTypeCommon):
    @property
    def Open(self) -> float:
        return _DeviceSlotType(self, _LST.Open)

    @Open.setter
    def Open(self, value: int | float):
        pass

    @property
    def Pressure(self) -> float:
        return _DeviceSlotType(self, _LST.Pressure)

    @Pressure.setter
    def Pressure(self, value: int | float):
        pass

    @property
    def Temperature(self) -> float:
        return _DeviceSlotType(self, _LST.Temperature)

    @Temperature.setter
    def Temperature(self, value: int | float):
        pass

    @property
    def Volume(self) -> float:
        return _DeviceSlotType(self, _LST.Volume)

    @Volume.setter
    def Volume(self, value: int | float):
        pass


class _SlotTypeGasCanisters(_SlotTypeCommons):
    @property
    def Open(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Open)

    @Open.setter
    def Open(self, value: int | float):
        pass

    @property
    def Pressure(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Pressure)

    @Pressure.setter
    def Pressure(self, value: int | float):
        pass

    @property
    def Temperature(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Temperature)

    @Temperature.setter
    def Temperature(self, value: int | float):
        pass

    @property
    def Volume(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Volume)

    @Volume.setter
    def Volume(self, value: int | float):
        pass


class _SlotTypeHelmet(_SlotTypeCommon):
    @property
    def Charge(self) -> float:
        return _DeviceSlotType(self, _LST.Charge)

    @Charge.setter
    def Charge(self, value: int | float):
        pass

    @property
    def ChargeRatio(self) -> float:
        return _DeviceSlotType(self, _LST.ChargeRatio)

    @ChargeRatio.setter
    def ChargeRatio(self, value: int | float):
        pass

    @property
    def Lock(self) -> float:
        return _DeviceSlotType(self, _LST.Lock)

    @Lock.setter
    def Lock(self, value: int | float):
        pass

    @property
    def On(self) -> float:
        return _DeviceSlotType(self, _LST.On)

    @On.setter
    def On(self, value: int | float):
        pass

    @property
    def Open(self) -> float:
        return _DeviceSlotType(self, _LST.Open)

    @Open.setter
    def Open(self, value: int | float):
        pass

    @property
    def Pressure(self) -> float:
        return _DeviceSlotType(self, _LST.Pressure)

    @Pressure.setter
    def Pressure(self, value: int | float):
        pass


class _SlotTypeHelmets(_SlotTypeCommons):
    @property
    def Charge(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Charge)

    @Charge.setter
    def Charge(self, value: int | float):
        pass

    @property
    def ChargeRatio(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.ChargeRatio)

    @ChargeRatio.setter
    def ChargeRatio(self, value: int | float):
        pass

    @property
    def Lock(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Lock)

    @Lock.setter
    def Lock(self, value: int | float):
        pass

    @property
    def On(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.On)

    @On.setter
    def On(self, value: int | float):
        pass

    @property
    def Open(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Open)

    @Open.setter
    def Open(self, value: int | float):
        pass

    @property
    def Pressure(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Pressure)

    @Pressure.setter
    def Pressure(self, value: int | float):
        pass


class _SlotTypeMask(_SlotTypeCommon):
    @property
    def Lock(self) -> float:
        return _DeviceSlotType(self, _LST.Lock)

    @Lock.setter
    def Lock(self, value: int | float):
        pass

    @property
    def On(self) -> float:
        return _DeviceSlotType(self, _LST.On)

    @On.setter
    def On(self, value: int | float):
        pass

    @property
    def Open(self) -> float:
        return _DeviceSlotType(self, _LST.Open)

    @Open.setter
    def Open(self, value: int | float):
        pass


class _SlotTypeMasks(_SlotTypeCommons):
    @property
    def Lock(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Lock)

    @Lock.setter
    def Lock(self, value: int | float):
        pass

    @property
    def On(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.On)

    @On.setter
    def On(self, value: int | float):
        pass

    @property
    def Open(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Open)

    @Open.setter
    def Open(self, value: int | float):
        pass


class _SlotTypePlant(_SlotTypeCommon):
    @property
    def Efficiency(self) -> float:
        return _DeviceSlotType(self, _LST.Efficiency)

    @Efficiency.setter
    def Efficiency(self, value: int | float):
        pass

    @property
    def Growth(self) -> float:
        return _DeviceSlotType(self, _LST.Growth)

    @Growth.setter
    def Growth(self, value: int | float):
        pass

    @property
    def Health(self) -> float:
        return _DeviceSlotType(self, _LST.Health)

    @Health.setter
    def Health(self, value: int | float):
        pass

    @property
    def Mature(self) -> float:
        return _DeviceSlotType(self, _LST.Mature)

    @Mature.setter
    def Mature(self, value: int | float):
        pass

    @property
    def MaturityRatio(self) -> float:
        return _DeviceSlotType(self, _LST.MaturityRatio)

    @MaturityRatio.setter
    def MaturityRatio(self, value: int | float):
        pass

    @property
    def Seeding(self) -> float:
        return _DeviceSlotType(self, _LST.Seeding)

    @Seeding.setter
    def Seeding(self, value: int | float):
        pass

    @property
    def SeedingRatio(self) -> float:
        return _DeviceSlotType(self, _LST.SeedingRatio)

    @SeedingRatio.setter
    def SeedingRatio(self, value: int | float):
        pass


class _SlotTypePlants(_SlotTypeCommons):
    @property
    def Efficiency(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Efficiency)

    @Efficiency.setter
    def Efficiency(self, value: int | float):
        pass

    @property
    def Growth(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Growth)

    @Growth.setter
    def Growth(self, value: int | float):
        pass

    @property
    def Health(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Health)

    @Health.setter
    def Health(self, value: int | float):
        pass

    @property
    def Mature(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Mature)

    @Mature.setter
    def Mature(self, value: int | float):
        pass

    @property
    def MaturityRatio(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.MaturityRatio)

    @MaturityRatio.setter
    def MaturityRatio(self, value: int | float):
        pass

    @property
    def Seeding(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Seeding)

    @Seeding.setter
    def Seeding(self, value: int | float):
        pass

    @property
    def SeedingRatio(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.SeedingRatio)

    @SeedingRatio.setter
    def SeedingRatio(self, value: int | float):
        pass


class _SlotTypeProgrammableChip(_SlotTypeCommon):
    @property
    def LineNumber(self) -> float:
        return _DeviceSlotType(self, _LST.LineNumber)

    @LineNumber.setter
    def LineNumber(self, value: int | float):
        pass


class _SlotTypeProgrammableChips(_SlotTypeCommons):
    @property
    def LineNumber(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.LineNumber)

    @LineNumber.setter
    def LineNumber(self, value: int | float):
        pass


class _SlotTypeSuit(_SlotTypeCommon):
    @property
    def Charge(self) -> float:
        return _DeviceSlotType(self, _LST.Charge)

    @Charge.setter
    def Charge(self, value: int | float):
        pass

    @property
    def ChargeRatio(self) -> float:
        return _DeviceSlotType(self, _LST.ChargeRatio)

    @ChargeRatio.setter
    def ChargeRatio(self, value: int | float):
        pass

    @property
    def Pressure(self) -> float:
        return _DeviceSlotType(self, _LST.Pressure)

    @Pressure.setter
    def Pressure(self, value: int | float):
        pass

    @property
    def PressureAir(self) -> float:
        return _DeviceSlotType(self, _LST.PressureAir)

    @PressureAir.setter
    def PressureAir(self, value: int | float):
        pass

    @property
    def PressureWaste(self) -> float:
        return _DeviceSlotType(self, _LST.PressureWaste)

    @PressureWaste.setter
    def PressureWaste(self, value: int | float):
        pass


class _SlotTypeSuits(_SlotTypeCommons):
    @property
    def Charge(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Charge)

    @Charge.setter
    def Charge(self, value: int | float):
        pass

    @property
    def ChargeRatio(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.ChargeRatio)

    @ChargeRatio.setter
    def ChargeRatio(self, value: int | float):
        pass

    @property
    def Pressure(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.Pressure)

    @Pressure.setter
    def Pressure(self, value: int | float):
        pass

    @property
    def PressureAir(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.PressureAir)

    @PressureAir.setter
    def PressureAir(self, value: int | float):
        pass

    @property
    def PressureWaste(self) -> _DevicesSlotType:
        return _DevicesSlotType(self, _LST.PressureWaste)

    @PressureWaste.setter
    def PressureWaste(self, value: int | float):
        pass


class _BaseGas:
    @property
    def RatioCarbonDioxide(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxide)

    @property
    def RatioLiquidCarbonDioxide(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidCarbonDioxide)

    @property
    def RatioLiquidNitrogen(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidNitrogen)

    @property
    def RatioLiquidNitrousOxide(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidNitrousOxide)

    @property
    def RatioLiquidOxygen(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidOxygen)

    @property
    def RatioLiquidPollutant(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidPollutant)

    @property
    def RatioLiquidVolatiles(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidVolatiles)

    @property
    def RatioNitrogen(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogen)

    @property
    def RatioNitrousOxide(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxide)

    @property
    def RatioOxygen(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygen)

    @property
    def RatioPollutant(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutant)

    @property
    def RatioSteam(self) -> float:
        return _DeviceLogicType(self, _LT.RatioSteam)

    @property
    def RatioVolatiles(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatiles)

    @property
    def RatioWater(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWater)


class _BaseGass:
    @property
    def RatioCarbonDioxide(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxide)

    @property
    def RatioLiquidCarbonDioxide(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidCarbonDioxide)

    @property
    def RatioLiquidNitrogen(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidNitrogen)

    @property
    def RatioLiquidNitrousOxide(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidNitrousOxide)

    @property
    def RatioLiquidOxygen(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidOxygen)

    @property
    def RatioLiquidPollutant(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidPollutant)

    @property
    def RatioLiquidVolatiles(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidVolatiles)

    @property
    def RatioNitrogen(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogen)

    @property
    def RatioNitrousOxide(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxide)

    @property
    def RatioOxygen(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygen)

    @property
    def RatioPollutant(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutant)

    @property
    def RatioSteam(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioSteam)

    @property
    def RatioVolatiles(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatiles)

    @property
    def RatioWater(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWater)


class _BaseGasInput:
    @property
    def RatioCarbonDioxideInput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideInput)

    @property
    def RatioLiquidCarbonDioxideInput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidCarbonDioxideInput)

    @property
    def RatioLiquidNitrogenInput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidNitrogenInput)

    @property
    def RatioLiquidNitrousOxideInput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidNitrousOxideInput)

    @property
    def RatioLiquidOxygenInput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidOxygenInput)

    @property
    def RatioLiquidPollutantInput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidPollutantInput)

    @property
    def RatioLiquidVolatilesInput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidVolatilesInput)

    @property
    def RatioNitrogenInput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenInput)

    @property
    def RatioNitrousOxideInput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideInput)

    @property
    def RatioOxygenInput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenInput)

    @property
    def RatioPollutantInput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantInput)

    @property
    def RatioSteamInput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioSteamInput)

    @property
    def RatioVolatilesInput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesInput)

    @property
    def RatioWaterInput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterInput)


class _BaseGasInputs:
    @property
    def RatioCarbonDioxideInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideInput)

    @property
    def RatioLiquidCarbonDioxideInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidCarbonDioxideInput)

    @property
    def RatioLiquidNitrogenInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidNitrogenInput)

    @property
    def RatioLiquidNitrousOxideInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidNitrousOxideInput)

    @property
    def RatioLiquidOxygenInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidOxygenInput)

    @property
    def RatioLiquidPollutantInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidPollutantInput)

    @property
    def RatioLiquidVolatilesInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidVolatilesInput)

    @property
    def RatioNitrogenInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenInput)

    @property
    def RatioNitrousOxideInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideInput)

    @property
    def RatioOxygenInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenInput)

    @property
    def RatioPollutantInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantInput)

    @property
    def RatioSteamInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioSteamInput)

    @property
    def RatioVolatilesInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesInput)

    @property
    def RatioWaterInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterInput)


class _BaseGasOutput:
    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioLiquidCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidCarbonDioxideOutput)

    @property
    def RatioLiquidNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidNitrogenOutput)

    @property
    def RatioLiquidNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidNitrousOxideOutput)

    @property
    def RatioLiquidOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidOxygenOutput)

    @property
    def RatioLiquidPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidPollutantOutput)

    @property
    def RatioLiquidVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidVolatilesOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioSteamOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioSteamOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)


class _BaseGasOutputs:
    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioLiquidCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidCarbonDioxideOutput)

    @property
    def RatioLiquidNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidNitrogenOutput)

    @property
    def RatioLiquidNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidNitrousOxideOutput)

    @property
    def RatioLiquidOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidOxygenOutput)

    @property
    def RatioLiquidPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidPollutantOutput)

    @property
    def RatioLiquidVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidVolatilesOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioSteamOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioSteamOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)


class _BaseGasOutput2:
    @property
    def RatioCarbonDioxideOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput2)

    @property
    def RatioLiquidCarbonDioxideOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidCarbonDioxideOutput2)

    @property
    def RatioLiquidNitrogenOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidNitrogenOutput2)

    @property
    def RatioLiquidNitrousOxideOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidNitrousOxideOutput2)

    @property
    def RatioLiquidOxygenOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidOxygenOutput2)

    @property
    def RatioLiquidPollutantOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidPollutantOutput2)

    @property
    def RatioLiquidVolatilesOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidVolatilesOutput2)

    @property
    def RatioNitrogenOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput2)

    @property
    def RatioNitrousOxideOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput2)

    @property
    def RatioOxygenOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput2)

    @property
    def RatioPollutantOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput2)

    @property
    def RatioSteamOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioSteamOutput2)

    @property
    def RatioVolatilesOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput2)

    @property
    def RatioWaterOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput2)


class _BaseGasOutput2s:
    @property
    def RatioCarbonDioxideOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput2)

    @property
    def RatioLiquidCarbonDioxideOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidCarbonDioxideOutput2)

    @property
    def RatioLiquidNitrogenOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidNitrogenOutput2)

    @property
    def RatioLiquidNitrousOxideOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidNitrousOxideOutput2)

    @property
    def RatioLiquidOxygenOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidOxygenOutput2)

    @property
    def RatioLiquidPollutantOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidPollutantOutput2)

    @property
    def RatioLiquidVolatilesOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidVolatilesOutput2)

    @property
    def RatioNitrogenOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput2)

    @property
    def RatioNitrousOxideOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput2)

    @property
    def RatioOxygenOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput2)

    @property
    def RatioPollutantOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput2)

    @property
    def RatioSteamOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioSteamOutput2)

    @property
    def RatioVolatilesOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput2)

    @property
    def RatioWaterOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput2)


class _Power:
    @property
    def On(self) -> float:
        return _DeviceLogicType(self, _LT.On)

    @On.setter
    def On(self, value: int | float):
        pass

    @property
    def Power(self) -> float:
        return _DeviceLogicType(self, _LT.Power)

    @property
    def RequiredPower(self) -> float:
        return _DeviceLogicType(self, _LT.RequiredPower)


class _Powers:
    @property
    def On(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.On)

    @On.setter
    def On(self, value: int | float):
        pass

    @property
    def Power(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Power)

    @property
    def RequiredPower(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RequiredPower)


class _On:
    @property
    def On(self) -> float:
        return _DeviceLogicType(self, _LT.On)

    @On.setter
    def On(self, value: int | float):
        pass


class _Ons:
    @property
    def On(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.On)

    @On.setter
    def On(self, value: int | float):
        pass


class _Activate:
    @property
    def Activate(self) -> float:
        return _DeviceLogicType(self, _LT.Activate)

    @Activate.setter
    def Activate(self, value: int | float):
        pass


class _Activates:
    @property
    def Activate(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Activate)

    @Activate.setter
    def Activate(self, value: int | float):
        pass


class _Lock:
    @property
    def Lock(self) -> float:
        return _DeviceLogicType(self, _LT.Lock)

    @Lock.setter
    def Lock(self, value: int | float):
        pass


class _Locks:
    @property
    def Lock(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Lock)

    @Lock.setter
    def Lock(self, value: int | float):
        pass


class _Open:
    @property
    def Open(self) -> float:
        return _DeviceLogicType(self, _LT.Open)

    @Open.setter
    def Open(self, value: int | float):
        pass


class _Opens:
    @property
    def Open(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Open)

    @Open.setter
    def Open(self, value: int | float):
        pass


class _Error:
    @property
    def Error(self) -> float:
        return _DeviceLogicType(self, _LT.Error)


class _Errors:
    @property
    def Error(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Error)


class _Ratio:
    @property
    def Ratio(self) -> float:
        return _DeviceLogicType(self, _LT.Ratio)


class _Ratios:
    @property
    def Ratio(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Ratio)


class _Maximum:
    @property
    def Maximum(self) -> float:
        return _DeviceLogicType(self, _LT.Maximum)


class _Maximums:
    @property
    def Maximum(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Maximum)


class _SettingW:
    @property
    def Setting(self) -> float:
        return _DeviceLogicType(self, _LT.Setting)

    @Setting.setter
    def Setting(self, value: int | float):
        pass


class _SettingWs:
    @property
    def Setting(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Setting)

    @Setting.setter
    def Setting(self, value: int | float):
        pass


class _SettingR:
    @property
    def Setting(self) -> float:
        return _DeviceLogicType(self, _LT.Setting)


class _SettingRs:
    @property
    def Setting(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Setting)


class _Mode:
    @property
    def Mode(self) -> float:
        return _DeviceLogicType(self, _LT.Mode)

    @Mode.setter
    def Mode(self, value: int | float):
        pass


class _Modes:
    @property
    def Mode(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Mode)

    @Mode.setter
    def Mode(self, value: int | float):
        pass


class _ModeR:
    @property
    def Mode(self) -> float:
        return _DeviceLogicType(self, _LT.Mode)


class _ModeRs:
    @property
    def Mode(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Mode)


class _Temperature:
    @property
    def Pressure(self) -> float:
        return _DeviceLogicType(self, _LT.Pressure)

    @property
    def Temperature(self) -> float:
        return _DeviceLogicType(self, _LT.Temperature)


class _Temperatures:
    @property
    def Pressure(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Pressure)

    @property
    def Temperature(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Temperature)


class _PollWater:
    @property
    def RatioPollutedWater(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutedWater)


class _PollWaters:
    @property
    def RatioPollutedWater(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutedWater)


class _Combustion:
    @property
    def Combustion(self) -> float:
        return _DeviceLogicType(self, _LT.Combustion)

    @property
    def TotalMoles(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMoles)


class _Combustions:
    @property
    def Combustion(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Combustion)

    @property
    def TotalMoles(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMoles)


class _Idle:
    @property
    def Idle(self) -> float:
        return _DeviceLogicType(self, _LT.Idle)


class _Idles:
    @property
    def Idle(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Idle)


class _ImportCount:
    @property
    def ImportCount(self) -> float:
        return _DeviceLogicType(self, _LT.ImportCount)

    @ImportCount.setter
    def ImportCount(self, value: int | float):
        pass


class _ImportCounts:
    @property
    def ImportCount(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ImportCount)

    @ImportCount.setter
    def ImportCount(self, value: int | float):
        pass


class _ClearMemory:
    @property
    def ClearMemory(self) -> float:
        return _DeviceLogicType(self, _LT.ClearMemory)

    @ClearMemory.setter
    def ClearMemory(self, value: int | float):
        pass


class _ClearMemorys:
    @property
    def ClearMemory(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ClearMemory)

    @ClearMemory.setter
    def ClearMemory(self, value: int | float):
        pass


class _Hydrogen:
    @property
    def RatioHydrogen(self) -> float:
        return _DeviceLogicType(self, _LT.RatioHydrogen)

    @property
    def RatioLiquidHydrogen(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidHydrogen)


class _Hydrogens:
    @property
    def RatioHydrogen(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioHydrogen)

    @property
    def RatioLiquidHydrogen(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidHydrogen)


class _ImportCount:
    @property
    def ImportCount(self) -> float:
        return _DeviceLogicType(self, _LT.ImportCount)


class _ImportCounts:
    @property
    def ImportCount(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ImportCount)


class _ExportCount:
    @property
    def ExportCount(self) -> float:
        return _DeviceLogicType(self, _LT.ExportCount)


class _ExportCounts:
    @property
    def ExportCount(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ExportCount)


class _Volume:
    @property
    def Volume(self) -> float:
        return _DeviceLogicType(self, _LT.Volume)

    @property
    def VolumeOfLiquid(self) -> float:
        return _DeviceLogicType(self, _LT.VolumeOfLiquid)


class _Volumes:
    @property
    def Volume(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Volume)

    @property
    def VolumeOfLiquid(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.VolumeOfLiquid)


class _Vertical:
    @property
    def Horizontal(self) -> float:
        return _DeviceLogicType(self, _LT.Horizontal)

    @property
    def Vertical(self) -> float:
        return _DeviceLogicType(self, _LT.Vertical)


class _Verticals:
    @property
    def Horizontal(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Horizontal)

    @property
    def Vertical(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Vertical)


class _VerticalW:
    @property
    def Horizontal(self) -> float:
        return _DeviceLogicType(self, _LT.Horizontal)

    @Horizontal.setter
    def Horizontal(self, value: int | float):
        pass

    @property
    def Vertical(self) -> float:
        return _DeviceLogicType(self, _LT.Vertical)

    @Vertical.setter
    def Vertical(self, value: int | float):
        pass


class _VerticalWs:
    @property
    def Horizontal(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Horizontal)

    @Horizontal.setter
    def Horizontal(self, value: int | float):
        pass

    @property
    def Vertical(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Vertical)

    @Vertical.setter
    def Vertical(self, value: int | float):
        pass


class _RecipeHash:
    @property
    def RecipeHash(self) -> float:
        return _DeviceLogicType(self, _LT.RecipeHash)

    @RecipeHash.setter
    def RecipeHash(self, value: int | float):
        pass


class _RecipeHashs:
    @property
    def RecipeHash(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RecipeHash)

    @RecipeHash.setter
    def RecipeHash(self, value: int | float):
        pass


class _Charge:
    @property
    def Charge(self) -> float:
        return _DeviceLogicType(self, _LT.Charge)


class _Charges:
    @property
    def Charge(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Charge)


class _Reagents:
    @property
    def Reagents(self) -> float:
        return _DeviceLogicType(self, _LT.Reagents)


class _Reagentss:
    @property
    def Reagents(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Reagents)


class _Quantity:
    @property
    def Quantity(self) -> float:
        return _DeviceLogicType(self, _LT.Quantity)


class _Quantitys:
    @property
    def Quantity(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Quantity)


class AccessBridge(_BaseStructure, _Activate, _Lock, _Open, _Power):
    _hash: int = 1298920475
    _prefab_name: int = "StructureAccessBridge"


class _AccessBridges(_BaseStructures, _Activates, _Locks, _Opens, _Powers):
    _hash: int = 1298920475
    _prefab_name: int = "StructureAccessBridge"

    def __getitem__(self, name: str | int | float) -> "_AccessBridges":
        return _AccessBridges(name)


AccessBridges: _AccessBridges = _AccessBridges()


class LiquidDrain(_BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = 1687692899
    _prefab_name: int = "StructureLiquidDrain"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _LiquidDrains(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 1687692899
    _prefab_name: int = "StructureLiquidDrain"

    def __getitem__(self, name: str | int | float) -> "_LiquidDrains":
        return _LiquidDrains(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


LiquidDrains: _LiquidDrains = _LiquidDrains()


class ActiveVent(
    _BaseStructure, _Error, _Lock, _Maximum, _Mode, _Open, _Power, _Ratio, _SettingW
):
    _hash: int = -1129453144
    _prefab_name: int = "StructureActiveVent"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureExternal(self) -> float:
        return _DeviceLogicType(self, _LT.PressureExternal)

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass

    @property
    def PressureInternal(self) -> float:
        return _DeviceLogicType(self, _LT.PressureInternal)

    @PressureInternal.setter
    def PressureInternal(self, value: int | float):
        pass

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def DataDisk(self) -> _SlotTypeCommon:
        return self.slot0


class _ActiveVents(
    _BaseStructures,
    _Errors,
    _Locks,
    _Maximums,
    _Modes,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
):
    _hash: int = -1129453144
    _prefab_name: int = "StructureActiveVent"

    def __getitem__(self, name: str | int | float) -> "_ActiveVents":
        return _ActiveVents(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureExternal(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureExternal)

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass

    @property
    def PressureInternal(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureInternal)

    @PressureInternal.setter
    def PressureInternal(self, value: int | float):
        pass

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def DataDisk(self) -> _SlotTypeCommons:
        return self.slot0


ActiveVents: _ActiveVents = _ActiveVents()


class AdvancedComposter(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Maximum,
    _Mode,
    _Open,
    _Power,
    _Quantity,
    _Ratio,
    _SettingW,
):
    _hash: int = 446212963
    _prefab_name: int = "StructureAdvancedComposter"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _AdvancedComposters(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Maximums,
    _Modes,
    _Opens,
    _Powers,
    _Quantitys,
    _Ratios,
    _SettingWs,
):
    _hash: int = 446212963
    _prefab_name: int = "StructureAdvancedComposter"

    def __getitem__(self, name: str | int | float) -> "_AdvancedComposters":
        return _AdvancedComposters(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


AdvancedComposters: _AdvancedComposters = _AdvancedComposters()


class AdvancedFurnace(
    _BaseStructure,
    _Activate,
    _BaseGas,
    _ClearMemory,
    _Combustion,
    _Error,
    _ExportCount,
    _Hydrogen,
    _ImportCount,
    _Lock,
    _Maximum,
    _Mode,
    _Open,
    _PollWater,
    _Power,
    _Ratio,
    _Reagents,
    _SettingW,
    _Temperature,
):
    _hash: int = 545937711
    _prefab_name: int = "StructureAdvancedFurnace"

    @property
    def RecipeHash(self) -> float:
        return _DeviceLogicType(self, _LT.RecipeHash)

    @property
    def SettingInput(self) -> float:
        return _DeviceLogicType(self, _LT.SettingInput)

    @SettingInput.setter
    def SettingInput(self, value: int | float):
        pass

    @property
    def SettingOutput(self) -> float:
        return _DeviceLogicType(self, _LT.SettingOutput)

    @SettingOutput.setter
    def SettingOutput(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _AdvancedFurnaces(
    _BaseStructures,
    _Activates,
    _BaseGass,
    _ClearMemorys,
    _Combustions,
    _Errors,
    _ExportCounts,
    _Hydrogens,
    _ImportCounts,
    _Locks,
    _Maximums,
    _Modes,
    _Opens,
    _PollWaters,
    _Powers,
    _Ratios,
    _Reagentss,
    _SettingWs,
    _Temperatures,
):
    _hash: int = 545937711
    _prefab_name: int = "StructureAdvancedFurnace"

    def __getitem__(self, name: str | int | float) -> "_AdvancedFurnaces":
        return _AdvancedFurnaces(name)

    @property
    def RecipeHash(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RecipeHash)

    @property
    def SettingInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SettingInput)

    @SettingInput.setter
    def SettingInput(self, value: int | float):
        pass

    @property
    def SettingOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SettingOutput)

    @SettingOutput.setter
    def SettingOutput(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


AdvancedFurnaces: _AdvancedFurnaces = _AdvancedFurnaces()


class AdvancedPackagingMachine(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Open,
    _Power,
    _Reagents,
    _RecipeHash,
):
    _hash: int = -463037670
    _prefab_name: int = "StructureAdvancedPackagingMachine"

    @property
    def CompletionRatio(self) -> float:
        return _DeviceLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> float:
        return _DeviceLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _AdvancedPackagingMachines(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Opens,
    _Powers,
    _Reagentss,
    _RecipeHashs,
):
    _hash: int = -463037670
    _prefab_name: int = "StructureAdvancedPackagingMachine"

    def __getitem__(self, name: str | int | float) -> "_AdvancedPackagingMachines":
        return _AdvancedPackagingMachines(name)

    @property
    def CompletionRatio(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


AdvancedPackagingMachines: _AdvancedPackagingMachines = _AdvancedPackagingMachines()


class AirConditioner(
    _BaseStructure,
    _BaseGasInput,
    _BaseGasOutput,
    _BaseGasOutput2,
    _Error,
    _Lock,
    _Maximum,
    _Mode,
    _Open,
    _Power,
    _Ratio,
    _SettingW,
):
    _hash: int = -2087593337
    _prefab_name: int = "StructureAirConditioner"

    @property
    def CombustionInput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionInput)

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def CombustionOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput2)

    @property
    def OperationalTemperatureEfficiency(self) -> float:
        return _DeviceLogicType(self, _LT.OperationalTemperatureEfficiency)

    @property
    def PressureEfficiency(self) -> float:
        return _DeviceLogicType(self, _LT.PressureEfficiency)

    @property
    def PressureInput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureInput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def PressureOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput2)

    @property
    def TemperatureDifferentialEfficiency(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureDifferentialEfficiency)

    @property
    def TemperatureInput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureInput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TemperatureOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput2)

    @property
    def TotalMolesInput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesInput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)

    @property
    def TotalMolesOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput2)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def ProgrammableChip(self) -> _SlotTypeCommon:
        return self.slot0


class _AirConditioners(
    _BaseStructures,
    _BaseGasInputs,
    _BaseGasOutput2s,
    _BaseGasOutputs,
    _Errors,
    _Locks,
    _Maximums,
    _Modes,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
):
    _hash: int = -2087593337
    _prefab_name: int = "StructureAirConditioner"

    def __getitem__(self, name: str | int | float) -> "_AirConditioners":
        return _AirConditioners(name)

    @property
    def CombustionInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionInput)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def CombustionOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput2)

    @property
    def OperationalTemperatureEfficiency(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.OperationalTemperatureEfficiency)

    @property
    def PressureEfficiency(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureEfficiency)

    @property
    def PressureInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureInput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def PressureOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput2)

    @property
    def TemperatureDifferentialEfficiency(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureDifferentialEfficiency)

    @property
    def TemperatureInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureInput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TemperatureOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput2)

    @property
    def TotalMolesInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesInput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)

    @property
    def TotalMolesOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput2)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def ProgrammableChip(self) -> _SlotTypeCommons:
        return self.slot0


AirConditioners: _AirConditioners = _AirConditioners()


class Airlock(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = -2105052344
    _prefab_name: int = "StructureAirlock"


class _Airlocks(_BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs):
    _hash: int = -2105052344
    _prefab_name: int = "StructureAirlock"

    def __getitem__(self, name: str | int | float) -> "_Airlocks":
        return _Airlocks(name)


Airlocks: _Airlocks = _Airlocks()


class AirlockWide(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = 1941072263
    _prefab_name: int = "StructureAirlockWide"


class _AirlockWides(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = 1941072263
    _prefab_name: int = "StructureAirlockWide"

    def __getitem__(self, name: str | int | float) -> "_AirlockWides":
        return _AirlockWides(name)


AirlockWides: _AirlockWides = _AirlockWides()


class ArcFurnace(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _Idle,
    _ImportCount,
    _Lock,
    _Power,
    _Reagents,
):
    _hash: int = -247344692
    _prefab_name: int = "StructureArcFurnace"

    @property
    def RecipeHash(self) -> float:
        return _DeviceLogicType(self, _LT.RecipeHash)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _ArcFurnaces(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _Idles,
    _ImportCounts,
    _Locks,
    _Powers,
    _Reagentss,
):
    _hash: int = -247344692
    _prefab_name: int = "StructureArcFurnace"

    def __getitem__(self, name: str | int | float) -> "_ArcFurnaces":
        return _ArcFurnaces(name)

    @property
    def RecipeHash(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RecipeHash)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


ArcFurnaces: _ArcFurnaces = _ArcFurnaces()


class AreaPowerControl(
    _BaseStructure, _Charge, _Error, _Lock, _Maximum, _Mode, _Open, _Power, _Ratio
):
    _hash: int = 1999523701
    _prefab_name: int = "StructureAreaPowerControl"

    @property
    def PowerActual(self) -> float:
        return _DeviceLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> float:
        return _DeviceLogicType(self, _LT.PowerPotential)

    @property
    def slot0(self) -> _SlotTypeBattery:
        return _SlotTypeBattery(self, 0)

    @property
    def Battery(self) -> _SlotTypeBattery:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def DataDisk(self) -> _SlotTypeCommon:
        return self.slot1


class _AreaPowerControls(
    _BaseStructures,
    _Charges,
    _Errors,
    _Locks,
    _Maximums,
    _Modes,
    _Opens,
    _Powers,
    _Ratios,
):
    _hash: int = 1999523701
    _prefab_name: int = "StructureAreaPowerControl"

    def __getitem__(self, name: str | int | float) -> "_AreaPowerControls":
        return _AreaPowerControls(name)

    @property
    def PowerActual(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerPotential)

    @property
    def slot0(self) -> _SlotTypeBatterys:
        return _SlotTypeBatterys(self, 0)

    @property
    def Battery(self) -> _SlotTypeBatterys:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def DataDisk(self) -> _SlotTypeCommons:
        return self.slot1


AreaPowerControls: _AreaPowerControls = _AreaPowerControls()


class AreaPowerControlReversed(
    _BaseStructure, _Charge, _Error, _Lock, _Maximum, _Mode, _Open, _Power, _Ratio
):
    _hash: int = -1032513487
    _prefab_name: int = "StructureAreaPowerControlReversed"

    @property
    def PowerActual(self) -> float:
        return _DeviceLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> float:
        return _DeviceLogicType(self, _LT.PowerPotential)

    @property
    def slot0(self) -> _SlotTypeBattery:
        return _SlotTypeBattery(self, 0)

    @property
    def Battery(self) -> _SlotTypeBattery:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def DataDisk(self) -> _SlotTypeCommon:
        return self.slot1


class _AreaPowerControlReverseds(
    _BaseStructures,
    _Charges,
    _Errors,
    _Locks,
    _Maximums,
    _Modes,
    _Opens,
    _Powers,
    _Ratios,
):
    _hash: int = -1032513487
    _prefab_name: int = "StructureAreaPowerControlReversed"

    def __getitem__(self, name: str | int | float) -> "_AreaPowerControlReverseds":
        return _AreaPowerControlReverseds(name)

    @property
    def PowerActual(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerPotential)

    @property
    def slot0(self) -> _SlotTypeBatterys:
        return _SlotTypeBatterys(self, 0)

    @property
    def Battery(self) -> _SlotTypeBatterys:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def DataDisk(self) -> _SlotTypeCommons:
        return self.slot1


AreaPowerControlReverseds: _AreaPowerControlReverseds = _AreaPowerControlReverseds()


class Autolathe(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Open,
    _Power,
    _Reagents,
    _RecipeHash,
):
    _hash: int = 336213101
    _prefab_name: int = "StructureAutolathe"

    @property
    def CompletionRatio(self) -> float:
        return _DeviceLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> float:
        return _DeviceLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _Autolathes(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Opens,
    _Powers,
    _Reagentss,
    _RecipeHashs,
):
    _hash: int = 336213101
    _prefab_name: int = "StructureAutolathe"

    def __getitem__(self, name: str | int | float) -> "_Autolathes":
        return _Autolathes(name)

    @property
    def CompletionRatio(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


Autolathes: _Autolathes = _Autolathes()


class AutomatedOven(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Open,
    _Power,
    _Reagents,
    _RecipeHash,
):
    _hash: int = -1672404896
    _prefab_name: int = "StructureAutomatedOven"

    @property
    def CompletionRatio(self) -> float:
        return _DeviceLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> float:
        return _DeviceLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _AutomatedOvens(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Opens,
    _Powers,
    _Reagentss,
    _RecipeHashs,
):
    _hash: int = -1672404896
    _prefab_name: int = "StructureAutomatedOven"

    def __getitem__(self, name: str | int | float) -> "_AutomatedOvens":
        return _AutomatedOvens(name)

    @property
    def CompletionRatio(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


AutomatedOvens: _AutomatedOvens = _AutomatedOvens()


class AutoMinerSmall(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Open,
    _Power,
):
    _hash: int = 7274344
    _prefab_name: int = "StructureAutoMinerSmall"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _AutoMinerSmalls(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Opens,
    _Powers,
):
    _hash: int = 7274344
    _prefab_name: int = "StructureAutoMinerSmall"

    def __getitem__(self, name: str | int | float) -> "_AutoMinerSmalls":
        return _AutoMinerSmalls(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


AutoMinerSmalls: _AutoMinerSmalls = _AutoMinerSmalls()


class BatterySmall(_BaseStructure, _Charge, _Maximum, _ModeR, _On, _Ratio):
    _hash: int = -2123455080
    _prefab_name: int = "StructureBatterySmall"

    @property
    def Power(self) -> float:
        return _DeviceLogicType(self, _LT.Power)

    @property
    def PowerActual(self) -> float:
        return _DeviceLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> float:
        return _DeviceLogicType(self, _LT.PowerPotential)


class _BatterySmalls(_BaseStructures, _Charges, _Maximums, _ModeRs, _Ons, _Ratios):
    _hash: int = -2123455080
    _prefab_name: int = "StructureBatterySmall"

    def __getitem__(self, name: str | int | float) -> "_BatterySmalls":
        return _BatterySmalls(name)

    @property
    def Power(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Power)

    @property
    def PowerActual(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerPotential)


BatterySmalls: _BatterySmalls = _BatterySmalls()


class BackPressureRegulator(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = -1149857558
    _prefab_name: int = "StructureBackPressureRegulator"


class _BackPressureRegulators(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -1149857558
    _prefab_name: int = "StructureBackPressureRegulator"

    def __getitem__(self, name: str | int | float) -> "_BackPressureRegulators":
        return _BackPressureRegulators(name)


BackPressureRegulators: _BackPressureRegulators = _BackPressureRegulators()


class BasketHoop(_BaseStructure, _Lock, _Power, _SettingW):
    _hash: int = -1613497288
    _prefab_name: int = "StructureBasketHoop"


class _BasketHoops(_BaseStructures, _Locks, _Powers, _SettingWs):
    _hash: int = -1613497288
    _prefab_name: int = "StructureBasketHoop"

    def __getitem__(self, name: str | int | float) -> "_BasketHoops":
        return _BasketHoops(name)


BasketHoops: _BasketHoops = _BasketHoops()


class LogicBatchReader(_BaseStructure, _Error, _Power, _SettingR):
    _hash: int = 264413729
    _prefab_name: int = "StructureLogicBatchReader"


class _LogicBatchReaders(_BaseStructures, _Errors, _Powers, _SettingRs):
    _hash: int = 264413729
    _prefab_name: int = "StructureLogicBatchReader"

    def __getitem__(self, name: str | int | float) -> "_LogicBatchReaders":
        return _LogicBatchReaders(name)


LogicBatchReaders: _LogicBatchReaders = _LogicBatchReaders()


class LogicBatchSlotReader(_BaseStructure, _Error, _Power, _SettingR):
    _hash: int = 436888930
    _prefab_name: int = "StructureLogicBatchSlotReader"


class _LogicBatchSlotReaders(_BaseStructures, _Errors, _Powers, _SettingRs):
    _hash: int = 436888930
    _prefab_name: int = "StructureLogicBatchSlotReader"

    def __getitem__(self, name: str | int | float) -> "_LogicBatchSlotReaders":
        return _LogicBatchSlotReaders(name)


LogicBatchSlotReaders: _LogicBatchSlotReaders = _LogicBatchSlotReaders()


class LogicBatchWriter(_BaseStructure, _Error, _Power):
    _hash: int = 1415443359
    _prefab_name: int = "StructureLogicBatchWriter"

    @property
    def ForceWrite(self) -> float:
        return _DeviceLogicType(self, _LT.ForceWrite)

    @ForceWrite.setter
    def ForceWrite(self, value: int | float):
        pass


class _LogicBatchWriters(_BaseStructures, _Errors, _Powers):
    _hash: int = 1415443359
    _prefab_name: int = "StructureLogicBatchWriter"

    def __getitem__(self, name: str | int | float) -> "_LogicBatchWriters":
        return _LogicBatchWriters(name)

    @property
    def ForceWrite(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ForceWrite)

    @ForceWrite.setter
    def ForceWrite(self, value: int | float):
        pass


LogicBatchWriters: _LogicBatchWriters = _LogicBatchWriters()


class BatteryMedium(_BaseStructure, _Charge, _Maximum, _ModeR, _On, _Ratio):
    _hash: int = -1125305264
    _prefab_name: int = "StructureBatteryMedium"

    @property
    def Power(self) -> float:
        return _DeviceLogicType(self, _LT.Power)

    @property
    def PowerActual(self) -> float:
        return _DeviceLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> float:
        return _DeviceLogicType(self, _LT.PowerPotential)


class _BatteryMediums(_BaseStructures, _Charges, _Maximums, _ModeRs, _Ons, _Ratios):
    _hash: int = -1125305264
    _prefab_name: int = "StructureBatteryMedium"

    def __getitem__(self, name: str | int | float) -> "_BatteryMediums":
        return _BatteryMediums(name)

    @property
    def Power(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Power)

    @property
    def PowerActual(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerPotential)


BatteryMediums: _BatteryMediums = _BatteryMediums()


class BatteryCharger(_BaseStructure, _Activate, _Error, _Power):
    _hash: int = 1945930022
    _prefab_name: int = "StructureBatteryCharger"

    @property
    def slot0(self) -> _SlotTypeBattery:
        return _SlotTypeBattery(self, 0)

    @property
    def slot1(self) -> _SlotTypeBattery:
        return _SlotTypeBattery(self, 1)

    @property
    def slot2(self) -> _SlotTypeBattery:
        return _SlotTypeBattery(self, 2)

    @property
    def slot3(self) -> _SlotTypeBattery:
        return _SlotTypeBattery(self, 3)

    @property
    def slot4(self) -> _SlotTypeBattery:
        return _SlotTypeBattery(self, 4)


class _BatteryChargers(_BaseStructures, _Activates, _Errors, _Powers):
    _hash: int = 1945930022
    _prefab_name: int = "StructureBatteryCharger"

    def __getitem__(self, name: str | int | float) -> "_BatteryChargers":
        return _BatteryChargers(name)

    @property
    def slot0(self) -> _SlotTypeBatterys:
        return _SlotTypeBatterys(self, 0)

    @property
    def slot1(self) -> _SlotTypeBatterys:
        return _SlotTypeBatterys(self, 1)

    @property
    def slot2(self) -> _SlotTypeBatterys:
        return _SlotTypeBatterys(self, 2)

    @property
    def slot3(self) -> _SlotTypeBatterys:
        return _SlotTypeBatterys(self, 3)

    @property
    def slot4(self) -> _SlotTypeBatterys:
        return _SlotTypeBatterys(self, 4)


BatteryChargers: _BatteryChargers = _BatteryChargers()


class BatteryChargerSmall(_BaseStructure, _Activate, _Error, _Power):
    _hash: int = -761772413
    _prefab_name: int = "StructureBatteryChargerSmall"

    @property
    def slot0(self) -> _SlotTypeBattery:
        return _SlotTypeBattery(self, 0)

    @property
    def slot1(self) -> _SlotTypeBattery:
        return _SlotTypeBattery(self, 1)


class _BatteryChargerSmalls(_BaseStructures, _Activates, _Errors, _Powers):
    _hash: int = -761772413
    _prefab_name: int = "StructureBatteryChargerSmall"

    def __getitem__(self, name: str | int | float) -> "_BatteryChargerSmalls":
        return _BatteryChargerSmalls(name)

    @property
    def slot0(self) -> _SlotTypeBatterys:
        return _SlotTypeBatterys(self, 0)

    @property
    def slot1(self) -> _SlotTypeBatterys:
        return _SlotTypeBatterys(self, 1)


BatteryChargerSmalls: _BatteryChargerSmalls = _BatteryChargerSmalls()


class Beacon(_BaseStructure, _Error, _Lock, _Power):
    _hash: int = -188177083
    _prefab_name: int = "StructureBeacon"

    @property
    def Color(self) -> float:
        return _DeviceLogicType(self, _LT.Color)

    @Color.setter
    def Color(self, value: int | float):
        pass


class _Beacons(_BaseStructures, _Errors, _Locks, _Powers):
    _hash: int = -188177083
    _prefab_name: int = "StructureBeacon"

    def __getitem__(self, name: str | int | float) -> "_Beacons":
        return _Beacons(name)

    @property
    def Color(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Color)

    @Color.setter
    def Color(self, value: int | float):
        pass


Beacons: _Beacons = _Beacons()


class Bench1(_BaseStructure, _Error, _Power):
    _hash: int = 406745009
    _prefab_name: int = "StructureBench1"

    @property
    def slot0(self) -> _SlotTypeAppliance:
        return _SlotTypeAppliance(self, 0)

    @property
    def Appliance1(self) -> _SlotTypeAppliance:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeAppliance:
        return _SlotTypeAppliance(self, 1)

    @property
    def Appliance2(self) -> _SlotTypeAppliance:
        return self.slot1


class _Bench1s(_BaseStructures, _Errors, _Powers):
    _hash: int = 406745009
    _prefab_name: int = "StructureBench1"

    def __getitem__(self, name: str | int | float) -> "_Bench1s":
        return _Bench1s(name)

    @property
    def slot0(self) -> _SlotTypeAppliances:
        return _SlotTypeAppliances(self, 0)

    @property
    def Appliance1(self) -> _SlotTypeAppliances:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeAppliances:
        return _SlotTypeAppliances(self, 1)

    @property
    def Appliance2(self) -> _SlotTypeAppliances:
        return self.slot1


Bench1s: _Bench1s = _Bench1s()


class Bench3(_BaseStructure, _Error, _Power):
    _hash: int = -164622691
    _prefab_name: int = "StructureBench3"

    @property
    def slot0(self) -> _SlotTypeAppliance:
        return _SlotTypeAppliance(self, 0)

    @property
    def Appliance1(self) -> _SlotTypeAppliance:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeAppliance:
        return _SlotTypeAppliance(self, 1)

    @property
    def Appliance2(self) -> _SlotTypeAppliance:
        return self.slot1


class _Bench3s(_BaseStructures, _Errors, _Powers):
    _hash: int = -164622691
    _prefab_name: int = "StructureBench3"

    def __getitem__(self, name: str | int | float) -> "_Bench3s":
        return _Bench3s(name)

    @property
    def slot0(self) -> _SlotTypeAppliances:
        return _SlotTypeAppliances(self, 0)

    @property
    def Appliance1(self) -> _SlotTypeAppliances:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeAppliances:
        return _SlotTypeAppliances(self, 1)

    @property
    def Appliance2(self) -> _SlotTypeAppliances:
        return self.slot1


Bench3s: _Bench3s = _Bench3s()


class Bench2(_BaseStructure, _Error, _Power):
    _hash: int = -2127086069
    _prefab_name: int = "StructureBench2"

    @property
    def slot0(self) -> _SlotTypeAppliance:
        return _SlotTypeAppliance(self, 0)

    @property
    def Appliance1(self) -> _SlotTypeAppliance:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeAppliance:
        return _SlotTypeAppliance(self, 1)

    @property
    def Appliance2(self) -> _SlotTypeAppliance:
        return self.slot1


class _Bench2s(_BaseStructures, _Errors, _Powers):
    _hash: int = -2127086069
    _prefab_name: int = "StructureBench2"

    def __getitem__(self, name: str | int | float) -> "_Bench2s":
        return _Bench2s(name)

    @property
    def slot0(self) -> _SlotTypeAppliances:
        return _SlotTypeAppliances(self, 0)

    @property
    def Appliance1(self) -> _SlotTypeAppliances:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeAppliances:
        return _SlotTypeAppliances(self, 1)

    @property
    def Appliance2(self) -> _SlotTypeAppliances:
        return self.slot1


Bench2s: _Bench2s = _Bench2s()


class Bench4(_BaseStructure, _Error, _Power):
    _hash: int = 1750375230
    _prefab_name: int = "StructureBench4"

    @property
    def slot0(self) -> _SlotTypeAppliance:
        return _SlotTypeAppliance(self, 0)

    @property
    def Appliance1(self) -> _SlotTypeAppliance:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeAppliance:
        return _SlotTypeAppliance(self, 1)

    @property
    def Appliance2(self) -> _SlotTypeAppliance:
        return self.slot1


class _Bench4s(_BaseStructures, _Errors, _Powers):
    _hash: int = 1750375230
    _prefab_name: int = "StructureBench4"

    def __getitem__(self, name: str | int | float) -> "_Bench4s":
        return _Bench4s(name)

    @property
    def slot0(self) -> _SlotTypeAppliances:
        return _SlotTypeAppliances(self, 0)

    @property
    def Appliance1(self) -> _SlotTypeAppliances:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeAppliances:
        return _SlotTypeAppliances(self, 1)

    @property
    def Appliance2(self) -> _SlotTypeAppliances:
        return self.slot1


Bench4s: _Bench4s = _Bench4s()


class BlastDoor(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = 337416191
    _prefab_name: int = "StructureBlastDoor"


class _BlastDoors(_BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs):
    _hash: int = 337416191
    _prefab_name: int = "StructureBlastDoor"

    def __getitem__(self, name: str | int | float) -> "_BlastDoors":
        return _BlastDoors(name)


BlastDoors: _BlastDoors = _BlastDoors()


class BlockBed(_BaseStructure, _Activate, _Error, _Power):
    _hash: int = 697908419
    _prefab_name: int = "StructureBlockBed"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Bed(self) -> _SlotTypeCommon:
        return self.slot0


class _BlockBeds(_BaseStructures, _Activates, _Errors, _Powers):
    _hash: int = 697908419
    _prefab_name: int = "StructureBlockBed"

    def __getitem__(self, name: str | int | float) -> "_BlockBeds":
        return _BlockBeds(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Bed(self) -> _SlotTypeCommons:
        return self.slot0


BlockBeds: _BlockBeds = _BlockBeds()


class LogicButton(_BaseStructure, _Activate, _Lock, _SettingR):
    _hash: int = 491845673
    _prefab_name: int = "StructureLogicButton"


class _LogicButtons(_BaseStructures, _Activates, _Locks, _SettingRs):
    _hash: int = 491845673
    _prefab_name: int = "StructureLogicButton"

    def __getitem__(self, name: str | int | float) -> "_LogicButtons":
        return _LogicButtons(name)


LogicButtons: _LogicButtons = _LogicButtons()


class CableAnalysizer(_BaseStructure):
    _hash: int = 1036015121
    _prefab_name: int = "StructureCableAnalysizer"

    @property
    def PowerActual(self) -> float:
        return _DeviceLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> float:
        return _DeviceLogicType(self, _LT.PowerPotential)

    @property
    def PowerRequired(self) -> float:
        return _DeviceLogicType(self, _LT.PowerRequired)


class _CableAnalysizers(_BaseStructures):
    _hash: int = 1036015121
    _prefab_name: int = "StructureCableAnalysizer"

    def __getitem__(self, name: str | int | float) -> "_CableAnalysizers":
        return _CableAnalysizers(name)

    @property
    def PowerActual(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerPotential)

    @property
    def PowerRequired(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerRequired)


CableAnalysizers: _CableAnalysizers = _CableAnalysizers()


class Camera(_BaseStructure, _Mode, _On):
    _hash: int = -342072665
    _prefab_name: int = "StructureCamera"


class _Cameras(_BaseStructures, _Modes, _Ons):
    _hash: int = -342072665
    _prefab_name: int = "StructureCamera"

    def __getitem__(self, name: str | int | float) -> "_Cameras":
        return _Cameras(name)


Cameras: _Cameras = _Cameras()


class CargoStorageMedium(
    _BaseStructure,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Open,
    _Power,
    _Quantity,
    _Ratio,
):
    _hash: int = 1151864003
    _prefab_name: int = "StructureCargoStorageMedium"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1

    @property
    def slot10(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 10)

    @property
    def slot100(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 100)

    @property
    def slot101(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 101)

    @property
    def slot11(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 14)

    @property
    def slot15(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 15)

    @property
    def slot16(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 16)

    @property
    def slot17(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 17)

    @property
    def slot18(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 18)

    @property
    def slot19(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 19)

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def slot20(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 20)

    @property
    def slot21(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 21)

    @property
    def slot22(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 22)

    @property
    def slot23(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 23)

    @property
    def slot24(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 24)

    @property
    def slot25(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 25)

    @property
    def slot26(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 26)

    @property
    def slot27(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 27)

    @property
    def slot28(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 28)

    @property
    def slot29(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 29)

    @property
    def slot3(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 3)

    @property
    def slot30(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 30)

    @property
    def slot31(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 31)

    @property
    def slot32(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 32)

    @property
    def slot33(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 33)

    @property
    def slot34(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 34)

    @property
    def slot35(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 35)

    @property
    def slot36(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 36)

    @property
    def slot37(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 37)

    @property
    def slot38(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 38)

    @property
    def slot39(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 39)

    @property
    def slot4(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 4)

    @property
    def slot40(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 40)

    @property
    def slot41(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 41)

    @property
    def slot42(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 42)

    @property
    def slot43(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 43)

    @property
    def slot44(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 44)

    @property
    def slot45(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 45)

    @property
    def slot46(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 46)

    @property
    def slot47(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 47)

    @property
    def slot48(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 48)

    @property
    def slot49(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 49)

    @property
    def slot5(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 5)

    @property
    def slot50(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 50)

    @property
    def slot51(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 51)

    @property
    def slot52(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 52)

    @property
    def slot53(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 53)

    @property
    def slot54(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 54)

    @property
    def slot55(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 55)

    @property
    def slot56(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 56)

    @property
    def slot57(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 57)

    @property
    def slot58(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 58)

    @property
    def slot59(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 59)

    @property
    def slot6(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 6)

    @property
    def slot60(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 60)

    @property
    def slot61(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 61)

    @property
    def slot62(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 62)

    @property
    def slot63(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 63)

    @property
    def slot64(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 64)

    @property
    def slot65(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 65)

    @property
    def slot66(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 66)

    @property
    def slot67(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 67)

    @property
    def slot68(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 68)

    @property
    def slot69(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 69)

    @property
    def slot7(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 7)

    @property
    def slot70(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 70)

    @property
    def slot71(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 71)

    @property
    def slot72(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 72)

    @property
    def slot73(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 73)

    @property
    def slot74(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 74)

    @property
    def slot75(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 75)

    @property
    def slot76(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 76)

    @property
    def slot77(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 77)

    @property
    def slot78(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 78)

    @property
    def slot79(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 79)

    @property
    def slot8(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 8)

    @property
    def slot80(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 80)

    @property
    def slot81(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 81)

    @property
    def slot82(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 82)

    @property
    def slot83(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 83)

    @property
    def slot84(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 84)

    @property
    def slot85(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 85)

    @property
    def slot86(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 86)

    @property
    def slot87(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 87)

    @property
    def slot88(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 88)

    @property
    def slot89(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 89)

    @property
    def slot9(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 9)

    @property
    def slot90(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 90)

    @property
    def slot91(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 91)

    @property
    def slot92(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 92)

    @property
    def slot93(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 93)

    @property
    def slot94(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 94)

    @property
    def slot95(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 95)

    @property
    def slot96(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 96)

    @property
    def slot97(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 97)

    @property
    def slot98(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 98)

    @property
    def slot99(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 99)


class _CargoStorageMediums(
    _BaseStructures,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Opens,
    _Powers,
    _Quantitys,
    _Ratios,
):
    _hash: int = 1151864003
    _prefab_name: int = "StructureCargoStorageMedium"

    def __getitem__(self, name: str | int | float) -> "_CargoStorageMediums":
        return _CargoStorageMediums(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1

    @property
    def slot10(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 10)

    @property
    def slot100(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 100)

    @property
    def slot101(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 101)

    @property
    def slot11(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 14)

    @property
    def slot15(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 15)

    @property
    def slot16(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 16)

    @property
    def slot17(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 17)

    @property
    def slot18(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 18)

    @property
    def slot19(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 19)

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def slot20(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 20)

    @property
    def slot21(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 21)

    @property
    def slot22(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 22)

    @property
    def slot23(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 23)

    @property
    def slot24(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 24)

    @property
    def slot25(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 25)

    @property
    def slot26(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 26)

    @property
    def slot27(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 27)

    @property
    def slot28(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 28)

    @property
    def slot29(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 29)

    @property
    def slot3(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 3)

    @property
    def slot30(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 30)

    @property
    def slot31(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 31)

    @property
    def slot32(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 32)

    @property
    def slot33(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 33)

    @property
    def slot34(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 34)

    @property
    def slot35(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 35)

    @property
    def slot36(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 36)

    @property
    def slot37(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 37)

    @property
    def slot38(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 38)

    @property
    def slot39(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 39)

    @property
    def slot4(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 4)

    @property
    def slot40(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 40)

    @property
    def slot41(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 41)

    @property
    def slot42(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 42)

    @property
    def slot43(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 43)

    @property
    def slot44(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 44)

    @property
    def slot45(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 45)

    @property
    def slot46(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 46)

    @property
    def slot47(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 47)

    @property
    def slot48(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 48)

    @property
    def slot49(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 49)

    @property
    def slot5(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 5)

    @property
    def slot50(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 50)

    @property
    def slot51(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 51)

    @property
    def slot52(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 52)

    @property
    def slot53(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 53)

    @property
    def slot54(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 54)

    @property
    def slot55(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 55)

    @property
    def slot56(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 56)

    @property
    def slot57(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 57)

    @property
    def slot58(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 58)

    @property
    def slot59(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 59)

    @property
    def slot6(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 6)

    @property
    def slot60(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 60)

    @property
    def slot61(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 61)

    @property
    def slot62(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 62)

    @property
    def slot63(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 63)

    @property
    def slot64(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 64)

    @property
    def slot65(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 65)

    @property
    def slot66(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 66)

    @property
    def slot67(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 67)

    @property
    def slot68(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 68)

    @property
    def slot69(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 69)

    @property
    def slot7(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 7)

    @property
    def slot70(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 70)

    @property
    def slot71(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 71)

    @property
    def slot72(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 72)

    @property
    def slot73(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 73)

    @property
    def slot74(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 74)

    @property
    def slot75(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 75)

    @property
    def slot76(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 76)

    @property
    def slot77(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 77)

    @property
    def slot78(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 78)

    @property
    def slot79(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 79)

    @property
    def slot8(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 8)

    @property
    def slot80(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 80)

    @property
    def slot81(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 81)

    @property
    def slot82(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 82)

    @property
    def slot83(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 83)

    @property
    def slot84(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 84)

    @property
    def slot85(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 85)

    @property
    def slot86(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 86)

    @property
    def slot87(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 87)

    @property
    def slot88(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 88)

    @property
    def slot89(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 89)

    @property
    def slot9(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 9)

    @property
    def slot90(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 90)

    @property
    def slot91(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 91)

    @property
    def slot92(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 92)

    @property
    def slot93(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 93)

    @property
    def slot94(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 94)

    @property
    def slot95(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 95)

    @property
    def slot96(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 96)

    @property
    def slot97(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 97)

    @property
    def slot98(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 98)

    @property
    def slot99(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 99)


CargoStorageMediums: _CargoStorageMediums = _CargoStorageMediums()


class CargoStorageSmall(
    _BaseStructure,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Open,
    _Power,
    _Quantity,
    _Ratio,
):
    _hash: int = -1493672123
    _prefab_name: int = "StructureCargoStorageSmall"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1

    @property
    def slot10(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 10)

    @property
    def slot11(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 14)

    @property
    def slot15(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 15)

    @property
    def slot16(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 16)

    @property
    def slot17(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 17)

    @property
    def slot18(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 18)

    @property
    def slot19(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 19)

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def slot20(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 20)

    @property
    def slot21(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 21)

    @property
    def slot22(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 22)

    @property
    def slot23(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 23)

    @property
    def slot24(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 24)

    @property
    def slot25(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 25)

    @property
    def slot26(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 26)

    @property
    def slot27(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 27)

    @property
    def slot28(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 28)

    @property
    def slot29(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 29)

    @property
    def slot3(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 3)

    @property
    def slot30(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 30)

    @property
    def slot31(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 31)

    @property
    def slot32(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 32)

    @property
    def slot33(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 33)

    @property
    def slot34(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 34)

    @property
    def slot35(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 35)

    @property
    def slot36(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 36)

    @property
    def slot37(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 37)

    @property
    def slot38(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 38)

    @property
    def slot39(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 39)

    @property
    def slot4(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 4)

    @property
    def slot40(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 40)

    @property
    def slot41(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 41)

    @property
    def slot42(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 42)

    @property
    def slot43(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 43)

    @property
    def slot44(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 44)

    @property
    def slot45(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 45)

    @property
    def slot46(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 46)

    @property
    def slot47(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 47)

    @property
    def slot48(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 48)

    @property
    def slot49(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 49)

    @property
    def slot5(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 5)

    @property
    def slot50(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 50)

    @property
    def slot51(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 51)

    @property
    def slot6(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 6)

    @property
    def slot7(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 7)

    @property
    def slot8(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 8)

    @property
    def slot9(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 9)


class _CargoStorageSmalls(
    _BaseStructures,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Opens,
    _Powers,
    _Quantitys,
    _Ratios,
):
    _hash: int = -1493672123
    _prefab_name: int = "StructureCargoStorageSmall"

    def __getitem__(self, name: str | int | float) -> "_CargoStorageSmalls":
        return _CargoStorageSmalls(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1

    @property
    def slot10(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 10)

    @property
    def slot11(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 14)

    @property
    def slot15(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 15)

    @property
    def slot16(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 16)

    @property
    def slot17(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 17)

    @property
    def slot18(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 18)

    @property
    def slot19(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 19)

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def slot20(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 20)

    @property
    def slot21(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 21)

    @property
    def slot22(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 22)

    @property
    def slot23(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 23)

    @property
    def slot24(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 24)

    @property
    def slot25(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 25)

    @property
    def slot26(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 26)

    @property
    def slot27(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 27)

    @property
    def slot28(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 28)

    @property
    def slot29(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 29)

    @property
    def slot3(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 3)

    @property
    def slot30(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 30)

    @property
    def slot31(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 31)

    @property
    def slot32(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 32)

    @property
    def slot33(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 33)

    @property
    def slot34(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 34)

    @property
    def slot35(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 35)

    @property
    def slot36(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 36)

    @property
    def slot37(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 37)

    @property
    def slot38(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 38)

    @property
    def slot39(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 39)

    @property
    def slot4(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 4)

    @property
    def slot40(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 40)

    @property
    def slot41(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 41)

    @property
    def slot42(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 42)

    @property
    def slot43(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 43)

    @property
    def slot44(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 44)

    @property
    def slot45(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 45)

    @property
    def slot46(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 46)

    @property
    def slot47(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 47)

    @property
    def slot48(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 48)

    @property
    def slot49(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 49)

    @property
    def slot5(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 5)

    @property
    def slot50(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 50)

    @property
    def slot51(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 51)

    @property
    def slot6(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 6)

    @property
    def slot7(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 7)

    @property
    def slot8(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 8)

    @property
    def slot9(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 9)


CargoStorageSmalls: _CargoStorageSmalls = _CargoStorageSmalls()


class Centrifuge(
    _BaseStructure,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Open,
    _Power,
    _Reagents,
):
    _hash: int = 690945935
    _prefab_name: int = "StructureCentrifuge"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _Centrifuges(
    _BaseStructures,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Opens,
    _Powers,
    _Reagentss,
):
    _hash: int = 690945935
    _prefab_name: int = "StructureCentrifuge"

    def __getitem__(self, name: str | int | float) -> "_Centrifuges":
        return _Centrifuges(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


Centrifuges: _Centrifuges = _Centrifuges()


class ChuteDigitalFlipFlopSplitterLeft(_BaseStructure, _Mode, _Power, _SettingW):
    _hash: int = -810874728
    _prefab_name: int = "StructureChuteDigitalFlipFlopSplitterLeft"

    @property
    def Quantity(self) -> float:
        return _DeviceLogicType(self, _LT.Quantity)

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass

    @property
    def SettingOutput(self) -> float:
        return _DeviceLogicType(self, _LT.SettingOutput)

    @SettingOutput.setter
    def SettingOutput(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def TransportSlot(self) -> _SlotTypeCommon:
        return self.slot0


class _ChuteDigitalFlipFlopSplitterLefts(_BaseStructures, _Modes, _Powers, _SettingWs):
    _hash: int = -810874728
    _prefab_name: int = "StructureChuteDigitalFlipFlopSplitterLeft"

    def __getitem__(
        self, name: str | int | float
    ) -> "_ChuteDigitalFlipFlopSplitterLefts":
        return _ChuteDigitalFlipFlopSplitterLefts(name)

    @property
    def Quantity(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Quantity)

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass

    @property
    def SettingOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SettingOutput)

    @SettingOutput.setter
    def SettingOutput(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def TransportSlot(self) -> _SlotTypeCommons:
        return self.slot0


ChuteDigitalFlipFlopSplitterLefts: _ChuteDigitalFlipFlopSplitterLefts = (
    _ChuteDigitalFlipFlopSplitterLefts()
)


class ChuteDigitalFlipFlopSplitterRight(_BaseStructure, _Mode, _Power, _SettingW):
    _hash: int = 163728359
    _prefab_name: int = "StructureChuteDigitalFlipFlopSplitterRight"

    @property
    def Quantity(self) -> float:
        return _DeviceLogicType(self, _LT.Quantity)

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass

    @property
    def SettingOutput(self) -> float:
        return _DeviceLogicType(self, _LT.SettingOutput)

    @SettingOutput.setter
    def SettingOutput(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def TransportSlot(self) -> _SlotTypeCommon:
        return self.slot0


class _ChuteDigitalFlipFlopSplitterRights(_BaseStructures, _Modes, _Powers, _SettingWs):
    _hash: int = 163728359
    _prefab_name: int = "StructureChuteDigitalFlipFlopSplitterRight"

    def __getitem__(
        self, name: str | int | float
    ) -> "_ChuteDigitalFlipFlopSplitterRights":
        return _ChuteDigitalFlipFlopSplitterRights(name)

    @property
    def Quantity(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Quantity)

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass

    @property
    def SettingOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SettingOutput)

    @SettingOutput.setter
    def SettingOutput(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def TransportSlot(self) -> _SlotTypeCommons:
        return self.slot0


ChuteDigitalFlipFlopSplitterRights: _ChuteDigitalFlipFlopSplitterRights = (
    _ChuteDigitalFlipFlopSplitterRights()
)


class ChuteDigitalValveLeft(_BaseStructure, _Lock, _Open, _Power, _SettingW):
    _hash: int = 648608238
    _prefab_name: int = "StructureChuteDigitalValveLeft"

    @property
    def Quantity(self) -> float:
        return _DeviceLogicType(self, _LT.Quantity)

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def TransportSlot(self) -> _SlotTypeCommon:
        return self.slot0


class _ChuteDigitalValveLefts(_BaseStructures, _Locks, _Opens, _Powers, _SettingWs):
    _hash: int = 648608238
    _prefab_name: int = "StructureChuteDigitalValveLeft"

    def __getitem__(self, name: str | int | float) -> "_ChuteDigitalValveLefts":
        return _ChuteDigitalValveLefts(name)

    @property
    def Quantity(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Quantity)

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def TransportSlot(self) -> _SlotTypeCommons:
        return self.slot0


ChuteDigitalValveLefts: _ChuteDigitalValveLefts = _ChuteDigitalValveLefts()


class ChuteDigitalValveRight(_BaseStructure, _Lock, _Open, _Power, _SettingW):
    _hash: int = -1337091041
    _prefab_name: int = "StructureChuteDigitalValveRight"

    @property
    def Quantity(self) -> float:
        return _DeviceLogicType(self, _LT.Quantity)

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def TransportSlot(self) -> _SlotTypeCommon:
        return self.slot0


class _ChuteDigitalValveRights(_BaseStructures, _Locks, _Opens, _Powers, _SettingWs):
    _hash: int = -1337091041
    _prefab_name: int = "StructureChuteDigitalValveRight"

    def __getitem__(self, name: str | int | float) -> "_ChuteDigitalValveRights":
        return _ChuteDigitalValveRights(name)

    @property
    def Quantity(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Quantity)

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def TransportSlot(self) -> _SlotTypeCommons:
        return self.slot0


ChuteDigitalValveRights: _ChuteDigitalValveRights = _ChuteDigitalValveRights()


class ChuteExportBin(_BaseStructure, _Error, _Lock, _Open, _Power):
    _hash: int = 1957571043
    _prefab_name: int = "StructureChuteExportBin"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Input(self) -> _SlotTypeCommon:
        return self.slot0


class _ChuteExportBins(_BaseStructures, _Errors, _Locks, _Opens, _Powers):
    _hash: int = 1957571043
    _prefab_name: int = "StructureChuteExportBin"

    def __getitem__(self, name: str | int | float) -> "_ChuteExportBins":
        return _ChuteExportBins(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Input(self) -> _SlotTypeCommons:
        return self.slot0


ChuteExportBins: _ChuteExportBins = _ChuteExportBins()


class ChuteBin(_BaseStructure, _Error, _Lock, _Open, _Power):
    _hash: int = -850484480
    _prefab_name: int = "StructureChuteBin"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Input(self) -> _SlotTypeCommon:
        return self.slot0


class _ChuteBins(_BaseStructures, _Errors, _Locks, _Opens, _Powers):
    _hash: int = -850484480
    _prefab_name: int = "StructureChuteBin"

    def __getitem__(self, name: str | int | float) -> "_ChuteBins":
        return _ChuteBins(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Input(self) -> _SlotTypeCommons:
        return self.slot0


ChuteBins: _ChuteBins = _ChuteBins()


class ChuteInlet(_BaseStructure, _ClearMemory, _ImportCount, _Lock):
    _hash: int = -1469588766
    _prefab_name: int = "StructureChuteInlet"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0


class _ChuteInlets(_BaseStructures, _ClearMemorys, _ImportCounts, _Locks):
    _hash: int = -1469588766
    _prefab_name: int = "StructureChuteInlet"

    def __getitem__(self, name: str | int | float) -> "_ChuteInlets":
        return _ChuteInlets(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0


ChuteInlets: _ChuteInlets = _ChuteInlets()


class ChuteOutlet(_BaseStructure, _ClearMemory, _ExportCount, _ImportCount, _Lock):
    _hash: int = -1022714809
    _prefab_name: int = "StructureChuteOutlet"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot0


class _ChuteOutlets(
    _BaseStructures, _ClearMemorys, _ExportCounts, _ImportCounts, _Locks
):
    _hash: int = -1022714809
    _prefab_name: int = "StructureChuteOutlet"

    def __getitem__(self, name: str | int | float) -> "_ChuteOutlets":
        return _ChuteOutlets(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot0


ChuteOutlets: _ChuteOutlets = _ChuteOutlets()


class CombustionCentrifuge(
    _BaseStructure,
    _BaseGas,
    _BaseGasInput,
    _BaseGasOutput,
    _ClearMemory,
    _Combustion,
    _Error,
    _ExportCount,
    _Hydrogen,
    _ImportCount,
    _Lock,
    _Open,
    _PollWater,
    _Power,
    _Reagents,
    _Temperature,
):
    _hash: int = 1238905683
    _prefab_name: int = "StructureCombustionCentrifuge"

    @property
    def CombustionInput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionInput)

    @property
    def CombustionLimiter(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionLimiter)

    @CombustionLimiter.setter
    def CombustionLimiter(self, value: int | float):
        pass

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureInput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureInput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def Rpm(self) -> float:
        return _DeviceLogicType(self, _LT.Rpm)

    @property
    def Stress(self) -> float:
        return _DeviceLogicType(self, _LT.Stress)

    @property
    def TemperatureInput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureInput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def Throttle(self) -> float:
        return _DeviceLogicType(self, _LT.Throttle)

    @Throttle.setter
    def Throttle(self, value: int | float):
        pass

    @property
    def TotalMolesInput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesInput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def ProgrammableChip(self) -> _SlotTypeCommon:
        return self.slot2


class _CombustionCentrifuges(
    _BaseStructures,
    _BaseGasInputs,
    _BaseGasOutputs,
    _BaseGass,
    _ClearMemorys,
    _Combustions,
    _Errors,
    _ExportCounts,
    _Hydrogens,
    _ImportCounts,
    _Locks,
    _Opens,
    _PollWaters,
    _Powers,
    _Reagentss,
    _Temperatures,
):
    _hash: int = 1238905683
    _prefab_name: int = "StructureCombustionCentrifuge"

    def __getitem__(self, name: str | int | float) -> "_CombustionCentrifuges":
        return _CombustionCentrifuges(name)

    @property
    def CombustionInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionInput)

    @property
    def CombustionLimiter(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionLimiter)

    @CombustionLimiter.setter
    def CombustionLimiter(self, value: int | float):
        pass

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureInput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def Rpm(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Rpm)

    @property
    def Stress(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Stress)

    @property
    def TemperatureInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureInput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def Throttle(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Throttle)

    @Throttle.setter
    def Throttle(self, value: int | float):
        pass

    @property
    def TotalMolesInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesInput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def ProgrammableChip(self) -> _SlotTypeCommons:
        return self.slot2


CombustionCentrifuges: _CombustionCentrifuges = _CombustionCentrifuges()


class CompositeDoor(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = -793837322
    _prefab_name: int = "StructureCompositeDoor"


class _CompositeDoors(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = -793837322
    _prefab_name: int = "StructureCompositeDoor"

    def __getitem__(self, name: str | int | float) -> "_CompositeDoors":
        return _CompositeDoors(name)


CompositeDoors: _CompositeDoors = _CompositeDoors()


class CompositeWindowShutterController(_BaseStructure, _Error, _Lock, _Open, _Power):
    _hash: int = -2078371660
    _prefab_name: int = "StructureCompositeWindowShutterController"


class _CompositeWindowShutterControllers(
    _BaseStructures, _Errors, _Locks, _Opens, _Powers
):
    _hash: int = -2078371660
    _prefab_name: int = "StructureCompositeWindowShutterController"

    def __getitem__(
        self, name: str | int | float
    ) -> "_CompositeWindowShutterControllers":
        return _CompositeWindowShutterControllers(name)


CompositeWindowShutterControllers: _CompositeWindowShutterControllers = (
    _CompositeWindowShutterControllers()
)


class ComputerBigScreenWallMounted(_BaseStructure, _Error, _Lock, _Open, _Power):
    _hash: int = -868055390
    _prefab_name: int = "StructureComputerBigScreenWallMounted"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Motherboard(self) -> _SlotTypeCommon:
        return self.slot0


class _ComputerBigScreenWallMounteds(_BaseStructures, _Errors, _Locks, _Opens, _Powers):
    _hash: int = -868055390
    _prefab_name: int = "StructureComputerBigScreenWallMounted"

    def __getitem__(self, name: str | int | float) -> "_ComputerBigScreenWallMounteds":
        return _ComputerBigScreenWallMounteds(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Motherboard(self) -> _SlotTypeCommons:
        return self.slot0


ComputerBigScreenWallMounteds: _ComputerBigScreenWallMounteds = (
    _ComputerBigScreenWallMounteds()
)


class ComputerBigScreen(_BaseStructure, _Error, _Lock, _Open, _Power):
    _hash: int = 1952395881
    _prefab_name: int = "StructureComputerBigScreen"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Motherboard(self) -> _SlotTypeCommon:
        return self.slot0


class _ComputerBigScreens(_BaseStructures, _Errors, _Locks, _Opens, _Powers):
    _hash: int = 1952395881
    _prefab_name: int = "StructureComputerBigScreen"

    def __getitem__(self, name: str | int | float) -> "_ComputerBigScreens":
        return _ComputerBigScreens(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Motherboard(self) -> _SlotTypeCommons:
        return self.slot0


ComputerBigScreens: _ComputerBigScreens = _ComputerBigScreens()


class Computer(_BaseStructure, _Error, _Lock, _Open, _Power):
    _hash: int = -626563514
    _prefab_name: int = "StructureComputer"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def Motherboard(self) -> _SlotTypeCommon:
        return self.slot2


class _Computers(_BaseStructures, _Errors, _Locks, _Opens, _Powers):
    _hash: int = -626563514
    _prefab_name: int = "StructureComputer"

    def __getitem__(self, name: str | int | float) -> "_Computers":
        return _Computers(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def Motherboard(self) -> _SlotTypeCommons:
        return self.slot2


Computers: _Computers = _Computers()


class ComputerUpright(_BaseStructure, _Error, _Lock, _Open, _Power):
    _hash: int = -405593895
    _prefab_name: int = "StructureComputerUpright"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def Motherboard(self) -> _SlotTypeCommon:
        return self.slot2


class _ComputerUprights(_BaseStructures, _Errors, _Locks, _Opens, _Powers):
    _hash: int = -405593895
    _prefab_name: int = "StructureComputerUpright"

    def __getitem__(self, name: str | int | float) -> "_ComputerUprights":
        return _ComputerUprights(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def Motherboard(self) -> _SlotTypeCommons:
        return self.slot2


ComputerUprights: _ComputerUprights = _ComputerUprights()


class CondensationChamber(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Error,
    _Hydrogen,
    _Lock,
    _Maximum,
    _Open,
    _PollWater,
    _Power,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = 1420719315
    _prefab_name: int = "StructureCondensationChamber"


class _CondensationChambers(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _Locks,
    _Maximums,
    _Opens,
    _PollWaters,
    _Powers,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = 1420719315
    _prefab_name: int = "StructureCondensationChamber"

    def __getitem__(self, name: str | int | float) -> "_CondensationChambers":
        return _CondensationChambers(name)


CondensationChambers: _CondensationChambers = _CondensationChambers()


class CondensationValve(_BaseStructure, _Maximum, _On, _Ratio, _SettingW):
    _hash: int = -965741795
    _prefab_name: int = "StructureCondensationValve"


class _CondensationValves(_BaseStructures, _Maximums, _Ons, _Ratios, _SettingWs):
    _hash: int = -965741795
    _prefab_name: int = "StructureCondensationValve"

    def __getitem__(self, name: str | int | float) -> "_CondensationValves":
        return _CondensationValves(name)


CondensationValves: _CondensationValves = _CondensationValves()


class Console(_BaseStructure, _Error, _Open, _Power, _SettingR):
    _hash: int = 235638270
    _prefab_name: int = "StructureConsole"

    @property
    def slot0(self) -> _SlotTypeCircuitboard:
        return _SlotTypeCircuitboard(self, 0)

    @property
    def Circuitboard(self) -> _SlotTypeCircuitboard:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCircuitboard:
        return _SlotTypeCircuitboard(self, 1)

    @property
    def DataDisk(self) -> _SlotTypeCircuitboard:
        return self.slot1


class _Consoles(_BaseStructures, _Errors, _Opens, _Powers, _SettingRs):
    _hash: int = 235638270
    _prefab_name: int = "StructureConsole"

    def __getitem__(self, name: str | int | float) -> "_Consoles":
        return _Consoles(name)

    @property
    def slot0(self) -> _SlotTypeCircuitboards:
        return _SlotTypeCircuitboards(self, 0)

    @property
    def Circuitboard(self) -> _SlotTypeCircuitboards:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCircuitboards:
        return _SlotTypeCircuitboards(self, 1)

    @property
    def DataDisk(self) -> _SlotTypeCircuitboards:
        return self.slot1


Consoles: _Consoles = _Consoles()


class ConsoleDual(_BaseStructure, _Error, _Open, _Power, _SettingR):
    _hash: int = -722284333
    _prefab_name: int = "StructureConsoleDual"

    @property
    def slot0(self) -> _SlotTypeCircuitboard:
        return _SlotTypeCircuitboard(self, 0)

    @property
    def Circuitboard(self) -> _SlotTypeCircuitboard:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCircuitboard:
        return _SlotTypeCircuitboard(self, 1)

    @property
    def DataDisk(self) -> _SlotTypeCircuitboard:
        return self.slot1


class _ConsoleDuals(_BaseStructures, _Errors, _Opens, _Powers, _SettingRs):
    _hash: int = -722284333
    _prefab_name: int = "StructureConsoleDual"

    def __getitem__(self, name: str | int | float) -> "_ConsoleDuals":
        return _ConsoleDuals(name)

    @property
    def slot0(self) -> _SlotTypeCircuitboards:
        return _SlotTypeCircuitboards(self, 0)

    @property
    def Circuitboard(self) -> _SlotTypeCircuitboards:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCircuitboards:
        return _SlotTypeCircuitboards(self, 1)

    @property
    def DataDisk(self) -> _SlotTypeCircuitboards:
        return self.slot1


ConsoleDuals: _ConsoleDuals = _ConsoleDuals()


class ConsoleMonitor(_BaseStructure, _Error, _Open, _Power, _SettingR):
    _hash: int = 801677497
    _prefab_name: int = "StructureConsoleMonitor"

    @property
    def slot0(self) -> _SlotTypeCircuitboard:
        return _SlotTypeCircuitboard(self, 0)

    @property
    def Circuitboard(self) -> _SlotTypeCircuitboard:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCircuitboard:
        return _SlotTypeCircuitboard(self, 1)

    @property
    def DataDisk(self) -> _SlotTypeCircuitboard:
        return self.slot1


class _ConsoleMonitors(_BaseStructures, _Errors, _Opens, _Powers, _SettingRs):
    _hash: int = 801677497
    _prefab_name: int = "StructureConsoleMonitor"

    def __getitem__(self, name: str | int | float) -> "_ConsoleMonitors":
        return _ConsoleMonitors(name)

    @property
    def slot0(self) -> _SlotTypeCircuitboards:
        return _SlotTypeCircuitboards(self, 0)

    @property
    def Circuitboard(self) -> _SlotTypeCircuitboards:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCircuitboards:
        return _SlotTypeCircuitboards(self, 1)

    @property
    def DataDisk(self) -> _SlotTypeCircuitboards:
        return self.slot1


ConsoleMonitors: _ConsoleMonitors = _ConsoleMonitors()


class CornerLocker(_BaseStructure, _Lock, _Open):
    _hash: int = -1968255729
    _prefab_name: int = "StructureCornerLocker"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def slot3(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 3)

    @property
    def slot4(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 4)

    @property
    def slot5(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 5)


class _CornerLockers(_BaseStructures, _Locks, _Opens):
    _hash: int = -1968255729
    _prefab_name: int = "StructureCornerLocker"

    def __getitem__(self, name: str | int | float) -> "_CornerLockers":
        return _CornerLockers(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def slot3(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 3)

    @property
    def slot4(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 4)

    @property
    def slot5(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 5)


CornerLockers: _CornerLockers = _CornerLockers()


class PassthroughHeatExchangerGasToGas(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -1674187440
    _prefab_name: int = "StructurePassthroughHeatExchangerGasToGas"


class _PassthroughHeatExchangerGasToGass(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = -1674187440
    _prefab_name: int = "StructurePassthroughHeatExchangerGasToGas"

    def __getitem__(
        self, name: str | int | float
    ) -> "_PassthroughHeatExchangerGasToGass":
        return _PassthroughHeatExchangerGasToGass(name)


PassthroughHeatExchangerGasToGass: _PassthroughHeatExchangerGasToGass = (
    _PassthroughHeatExchangerGasToGass()
)


class PassthroughHeatExchangerGasToLiquid(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 1928991265
    _prefab_name: int = "StructurePassthroughHeatExchangerGasToLiquid"


class _PassthroughHeatExchangerGasToLiquids(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = 1928991265
    _prefab_name: int = "StructurePassthroughHeatExchangerGasToLiquid"

    def __getitem__(
        self, name: str | int | float
    ) -> "_PassthroughHeatExchangerGasToLiquids":
        return _PassthroughHeatExchangerGasToLiquids(name)


PassthroughHeatExchangerGasToLiquids: _PassthroughHeatExchangerGasToLiquids = (
    _PassthroughHeatExchangerGasToLiquids()
)


class PassthroughHeatExchangerLiquidToLiquid(
    _BaseStructure, _Maximum, _Ratio, _SettingW
):
    _hash: int = -1472829583
    _prefab_name: int = "StructurePassthroughHeatExchangerLiquidToLiquid"


class _PassthroughHeatExchangerLiquidToLiquids(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = -1472829583
    _prefab_name: int = "StructurePassthroughHeatExchangerLiquidToLiquid"

    def __getitem__(
        self, name: str | int | float
    ) -> "_PassthroughHeatExchangerLiquidToLiquids":
        return _PassthroughHeatExchangerLiquidToLiquids(name)


PassthroughHeatExchangerLiquidToLiquids: _PassthroughHeatExchangerLiquidToLiquids = (
    _PassthroughHeatExchangerLiquidToLiquids()
)


class CryoTubeHorizontal(
    _BaseStructure,
    _Activate,
    _Error,
    _Lock,
    _Maximum,
    _Mode,
    _Open,
    _Power,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = 1443059329
    _prefab_name: int = "StructureCryoTubeHorizontal"

    @property
    def EntityState(self) -> float:
        return _DeviceLogicType(self, _LT.EntityState)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Player(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeMask:
        return _SlotTypeMask(self, 1)

    @property
    def Mask(self) -> _SlotTypeMask:
        return self.slot1


class _CryoTubeHorizontals(
    _BaseStructures,
    _Activates,
    _Errors,
    _Locks,
    _Maximums,
    _Modes,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = 1443059329
    _prefab_name: int = "StructureCryoTubeHorizontal"

    def __getitem__(self, name: str | int | float) -> "_CryoTubeHorizontals":
        return _CryoTubeHorizontals(name)

    @property
    def EntityState(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.EntityState)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Player(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeMasks:
        return _SlotTypeMasks(self, 1)

    @property
    def Mask(self) -> _SlotTypeMasks:
        return self.slot1


CryoTubeHorizontals: _CryoTubeHorizontals = _CryoTubeHorizontals()


class CryoTubeVertical(
    _BaseStructure,
    _Activate,
    _Error,
    _Lock,
    _Maximum,
    _Mode,
    _Open,
    _Power,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = -1381321828
    _prefab_name: int = "StructureCryoTubeVertical"

    @property
    def EntityState(self) -> float:
        return _DeviceLogicType(self, _LT.EntityState)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Player(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeMask:
        return _SlotTypeMask(self, 1)

    @property
    def Mask(self) -> _SlotTypeMask:
        return self.slot1


class _CryoTubeVerticals(
    _BaseStructures,
    _Activates,
    _Errors,
    _Locks,
    _Maximums,
    _Modes,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = -1381321828
    _prefab_name: int = "StructureCryoTubeVertical"

    def __getitem__(self, name: str | int | float) -> "_CryoTubeVerticals":
        return _CryoTubeVerticals(name)

    @property
    def EntityState(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.EntityState)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Player(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeMasks:
        return _SlotTypeMasks(self, 1)

    @property
    def Mask(self) -> _SlotTypeMasks:
        return self.slot1


CryoTubeVerticals: _CryoTubeVerticals = _CryoTubeVerticals()


class DaylightSensor(_BaseStructure, _Activate, _Mode, _On, _Vertical):
    _hash: int = 1076425094
    _prefab_name: int = "StructureDaylightSensor"

    @property
    def SolarAngle(self) -> float:
        return _DeviceLogicType(self, _LT.SolarAngle)

    @property
    def SolarIrradiance(self) -> float:
        return _DeviceLogicType(self, _LT.SolarIrradiance)


class _DaylightSensors(_BaseStructures, _Activates, _Modes, _Ons, _Verticals):
    _hash: int = 1076425094
    _prefab_name: int = "StructureDaylightSensor"

    def __getitem__(self, name: str | int | float) -> "_DaylightSensors":
        return _DaylightSensors(name)

    @property
    def SolarAngle(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SolarAngle)

    @property
    def SolarIrradiance(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SolarIrradiance)


DaylightSensors: _DaylightSensors = _DaylightSensors()


class DeepMiner(
    _BaseStructure,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Maximum,
    _Power,
    _Ratio,
    _SettingW,
):
    _hash: int = 265720906
    _prefab_name: int = "StructureDeepMiner"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot0


class _DeepMiners(
    _BaseStructures,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Maximums,
    _Powers,
    _Ratios,
    _SettingWs,
):
    _hash: int = 265720906
    _prefab_name: int = "StructureDeepMiner"

    def __getitem__(self, name: str | int | float) -> "_DeepMiners":
        return _DeepMiners(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot0


DeepMiners: _DeepMiners = _DeepMiners()


class LogicDial(_BaseStructure, _Mode, _Ratio, _SettingW):
    _hash: int = 554524804
    _prefab_name: int = "StructureLogicDial"


class _LogicDials(_BaseStructures, _Modes, _Ratios, _SettingWs):
    _hash: int = 554524804
    _prefab_name: int = "StructureLogicDial"

    def __getitem__(self, name: str | int | float) -> "_LogicDials":
        return _LogicDials(name)


LogicDials: _LogicDials = _LogicDials()


class DigitalValve(_BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = -1280984102
    _prefab_name: int = "StructureDigitalValve"


class _DigitalValves(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -1280984102
    _prefab_name: int = "StructureDigitalValve"

    def __getitem__(self, name: str | int | float) -> "_DigitalValves":
        return _DigitalValves(name)


DigitalValves: _DigitalValves = _DigitalValves()


class DiodeSlide(_BaseStructure, _Lock, _Power, _SettingW):
    _hash: int = 576516101
    _prefab_name: int = "StructureDiodeSlide"


class _DiodeSlides(_BaseStructures, _Locks, _Powers, _SettingWs):
    _hash: int = 576516101
    _prefab_name: int = "StructureDiodeSlide"

    def __getitem__(self, name: str | int | float) -> "_DiodeSlides":
        return _DiodeSlides(name)


DiodeSlides: _DiodeSlides = _DiodeSlides()


class DrinkingFountain(_BaseStructure, _Error, _Power):
    _hash: int = 1968371847
    _prefab_name: int = "StructureDrinkingFountain"


class _DrinkingFountains(_BaseStructures, _Errors, _Powers):
    _hash: int = 1968371847
    _prefab_name: int = "StructureDrinkingFountain"

    def __getitem__(self, name: str | int | float) -> "_DrinkingFountains":
        return _DrinkingFountains(name)


DrinkingFountains: _DrinkingFountains = _DrinkingFountains()


class SleeperVerticalDroid(_BaseStructure, _Activate, _Error, _Lock, _Open, _Power):
    _hash: int = 1382098999
    _prefab_name: int = "StructureSleeperVerticalDroid"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Player(self) -> _SlotTypeCommon:
        return self.slot0


class _SleeperVerticalDroids(
    _BaseStructures, _Activates, _Errors, _Locks, _Opens, _Powers
):
    _hash: int = 1382098999
    _prefab_name: int = "StructureSleeperVerticalDroid"

    def __getitem__(self, name: str | int | float) -> "_SleeperVerticalDroids":
        return _SleeperVerticalDroids(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Player(self) -> _SlotTypeCommons:
        return self.slot0


SleeperVerticalDroids: _SleeperVerticalDroids = _SleeperVerticalDroids()


class Electrolyzer(
    _BaseStructure,
    _Activate,
    _BaseGas,
    _BaseGasInput,
    _BaseGasOutput,
    _Combustion,
    _Error,
    _Hydrogen,
    _Lock,
    _Maximum,
    _Mode,
    _Open,
    _PollWater,
    _Power,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = -1668992663
    _prefab_name: int = "StructureElectrolyzer"

    @property
    def CombustionInput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionInput)

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureInput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureInput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def TemperatureInput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureInput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesInput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesInput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def ProgrammableChip(self) -> _SlotTypeCommon:
        return self.slot0


class _Electrolyzers(
    _BaseStructures,
    _Activates,
    _BaseGasInputs,
    _BaseGasOutputs,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _Locks,
    _Maximums,
    _Modes,
    _Opens,
    _PollWaters,
    _Powers,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = -1668992663
    _prefab_name: int = "StructureElectrolyzer"

    def __getitem__(self, name: str | int | float) -> "_Electrolyzers":
        return _Electrolyzers(name)

    @property
    def CombustionInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionInput)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureInput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def TemperatureInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureInput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesInput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def ProgrammableChip(self) -> _SlotTypeCommons:
        return self.slot0


Electrolyzers: _Electrolyzers = _Electrolyzers()


class ElectronicsPrinter(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Open,
    _Power,
    _Reagents,
    _RecipeHash,
):
    _hash: int = 1307165496
    _prefab_name: int = "StructureElectronicsPrinter"

    @property
    def CompletionRatio(self) -> float:
        return _DeviceLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> float:
        return _DeviceLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _ElectronicsPrinters(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Opens,
    _Powers,
    _Reagentss,
    _RecipeHashs,
):
    _hash: int = 1307165496
    _prefab_name: int = "StructureElectronicsPrinter"

    def __getitem__(self, name: str | int | float) -> "_ElectronicsPrinters":
        return _ElectronicsPrinters(name)

    @property
    def CompletionRatio(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


ElectronicsPrinters: _ElectronicsPrinters = _ElectronicsPrinters()


class ElevatorLevelIndustrial(_BaseStructure, _Activate, _Error, _Lock, _Open, _Power):
    _hash: int = 2060648791
    _prefab_name: int = "StructureElevatorLevelIndustrial"

    @property
    def ElevatorLevel(self) -> float:
        return _DeviceLogicType(self, _LT.ElevatorLevel)

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> float:
        return _DeviceLogicType(self, _LT.ElevatorSpeed)

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value: int | float):
        pass


class _ElevatorLevelIndustrials(
    _BaseStructures, _Activates, _Errors, _Locks, _Opens, _Powers
):
    _hash: int = 2060648791
    _prefab_name: int = "StructureElevatorLevelIndustrial"

    def __getitem__(self, name: str | int | float) -> "_ElevatorLevelIndustrials":
        return _ElevatorLevelIndustrials(name)

    @property
    def ElevatorLevel(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ElevatorLevel)

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ElevatorSpeed)

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value: int | float):
        pass


ElevatorLevelIndustrials: _ElevatorLevelIndustrials = _ElevatorLevelIndustrials()


class ElevatorLevelFront(_BaseStructure, _Activate, _Error, _Lock, _Open, _Power):
    _hash: int = -827912235
    _prefab_name: int = "StructureElevatorLevelFront"

    @property
    def ElevatorLevel(self) -> float:
        return _DeviceLogicType(self, _LT.ElevatorLevel)

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> float:
        return _DeviceLogicType(self, _LT.ElevatorSpeed)

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value: int | float):
        pass


class _ElevatorLevelFronts(
    _BaseStructures, _Activates, _Errors, _Locks, _Opens, _Powers
):
    _hash: int = -827912235
    _prefab_name: int = "StructureElevatorLevelFront"

    def __getitem__(self, name: str | int | float) -> "_ElevatorLevelFronts":
        return _ElevatorLevelFronts(name)

    @property
    def ElevatorLevel(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ElevatorLevel)

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ElevatorSpeed)

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value: int | float):
        pass


ElevatorLevelFronts: _ElevatorLevelFronts = _ElevatorLevelFronts()


class ElevatorShaftIndustrial(_BaseStructure):
    _hash: int = 1998354978
    _prefab_name: int = "StructureElevatorShaftIndustrial"

    @property
    def ElevatorLevel(self) -> float:
        return _DeviceLogicType(self, _LT.ElevatorLevel)

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> float:
        return _DeviceLogicType(self, _LT.ElevatorSpeed)

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value: int | float):
        pass


class _ElevatorShaftIndustrials(_BaseStructures):
    _hash: int = 1998354978
    _prefab_name: int = "StructureElevatorShaftIndustrial"

    def __getitem__(self, name: str | int | float) -> "_ElevatorShaftIndustrials":
        return _ElevatorShaftIndustrials(name)

    @property
    def ElevatorLevel(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ElevatorLevel)

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ElevatorSpeed)

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value: int | float):
        pass


ElevatorShaftIndustrials: _ElevatorShaftIndustrials = _ElevatorShaftIndustrials()


class ElevatorShaft(_BaseStructure, _Power):
    _hash: int = 826144419
    _prefab_name: int = "StructureElevatorShaft"

    @property
    def ElevatorLevel(self) -> float:
        return _DeviceLogicType(self, _LT.ElevatorLevel)

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> float:
        return _DeviceLogicType(self, _LT.ElevatorSpeed)

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value: int | float):
        pass


class _ElevatorShafts(_BaseStructures, _Powers):
    _hash: int = 826144419
    _prefab_name: int = "StructureElevatorShaft"

    def __getitem__(self, name: str | int | float) -> "_ElevatorShafts":
        return _ElevatorShafts(name)

    @property
    def ElevatorLevel(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ElevatorLevel)

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ElevatorSpeed)

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value: int | float):
        pass


ElevatorShafts: _ElevatorShafts = _ElevatorShafts()


class EvaporationChamber(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Error,
    _Hydrogen,
    _Lock,
    _Maximum,
    _Open,
    _PollWater,
    _Power,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = -1429782576
    _prefab_name: int = "StructureEvaporationChamber"


class _EvaporationChambers(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _Locks,
    _Maximums,
    _Opens,
    _PollWaters,
    _Powers,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = -1429782576
    _prefab_name: int = "StructureEvaporationChamber"

    def __getitem__(self, name: str | int | float) -> "_EvaporationChambers":
        return _EvaporationChambers(name)


EvaporationChambers: _EvaporationChambers = _EvaporationChambers()


class ExpansionValve(_BaseStructure, _Maximum, _On, _Ratio, _SettingW):
    _hash: int = 195298587
    _prefab_name: int = "StructureExpansionValve"


class _ExpansionValves(_BaseStructures, _Maximums, _Ons, _Ratios, _SettingWs):
    _hash: int = 195298587
    _prefab_name: int = "StructureExpansionValve"

    def __getitem__(self, name: str | int | float) -> "_ExpansionValves":
        return _ExpansionValves(name)


ExpansionValves: _ExpansionValves = _ExpansionValves()


class Filtration(
    _BaseStructure,
    _BaseGasInput,
    _BaseGasOutput,
    _BaseGasOutput2,
    _Error,
    _Lock,
    _Maximum,
    _Mode,
    _Open,
    _Power,
    _Ratio,
    _SettingW,
):
    _hash: int = -348054045
    _prefab_name: int = "StructureFiltration"

    @property
    def CombustionInput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionInput)

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def CombustionOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput2)

    @property
    def PressureInput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureInput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def PressureOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput2)

    @property
    def TemperatureInput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureInput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TemperatureOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput2)

    @property
    def TotalMolesInput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesInput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)

    @property
    def TotalMolesOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput2)

    @property
    def slot0(self) -> _SlotTypeFilter:
        return _SlotTypeFilter(self, 0)

    @property
    def slot1(self) -> _SlotTypeFilter:
        return _SlotTypeFilter(self, 1)

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def ProgrammableChip(self) -> _SlotTypeCommon:
        return self.slot2


class _Filtrations(
    _BaseStructures,
    _BaseGasInputs,
    _BaseGasOutput2s,
    _BaseGasOutputs,
    _Errors,
    _Locks,
    _Maximums,
    _Modes,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
):
    _hash: int = -348054045
    _prefab_name: int = "StructureFiltration"

    def __getitem__(self, name: str | int | float) -> "_Filtrations":
        return _Filtrations(name)

    @property
    def CombustionInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionInput)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def CombustionOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput2)

    @property
    def PressureInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureInput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def PressureOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput2)

    @property
    def TemperatureInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureInput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TemperatureOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput2)

    @property
    def TotalMolesInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesInput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)

    @property
    def TotalMolesOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput2)

    @property
    def slot0(self) -> _SlotTypeFilters:
        return _SlotTypeFilters(self, 0)

    @property
    def slot1(self) -> _SlotTypeFilters:
        return _SlotTypeFilters(self, 1)

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def ProgrammableChip(self) -> _SlotTypeCommons:
        return self.slot2


Filtrations: _Filtrations = _Filtrations()


class FlashingLight(_BaseStructure, _Lock, _Power):
    _hash: int = -1535893860
    _prefab_name: int = "StructureFlashingLight"


class _FlashingLights(_BaseStructures, _Locks, _Powers):
    _hash: int = -1535893860
    _prefab_name: int = "StructureFlashingLight"

    def __getitem__(self, name: str | int | float) -> "_FlashingLights":
        return _FlashingLights(name)


FlashingLights: _FlashingLights = _FlashingLights()


class FridgeBig(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Error,
    _Hydrogen,
    _Maximum,
    _Open,
    _PollWater,
    _Power,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = 958476921
    _prefab_name: int = "StructureFridgeBig"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def slot10(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 10)

    @property
    def slot11(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 14)

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def slot3(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 3)

    @property
    def slot4(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 4)

    @property
    def slot5(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 5)

    @property
    def slot6(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 6)

    @property
    def slot7(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 7)

    @property
    def slot8(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 8)

    @property
    def slot9(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 9)


class _FridgeBigs(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _Maximums,
    _Opens,
    _PollWaters,
    _Powers,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = 958476921
    _prefab_name: int = "StructureFridgeBig"

    def __getitem__(self, name: str | int | float) -> "_FridgeBigs":
        return _FridgeBigs(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def slot10(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 10)

    @property
    def slot11(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 14)

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def slot3(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 3)

    @property
    def slot4(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 4)

    @property
    def slot5(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 5)

    @property
    def slot6(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 6)

    @property
    def slot7(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 7)

    @property
    def slot8(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 8)

    @property
    def slot9(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 9)


FridgeBigs: _FridgeBigs = _FridgeBigs()


class FridgeSmall(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _Open,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = 751887598
    _prefab_name: int = "StructureFridgeSmall"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)


class _FridgeSmalls(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _Opens,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = 751887598
    _prefab_name: int = "StructureFridgeSmall"

    def __getitem__(self, name: str | int | float) -> "_FridgeSmalls":
        return _FridgeSmalls(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)


FridgeSmalls: _FridgeSmalls = _FridgeSmalls()


class Furnace(
    _BaseStructure,
    _Activate,
    _BaseGas,
    _ClearMemory,
    _Combustion,
    _ExportCount,
    _Hydrogen,
    _ImportCount,
    _Lock,
    _Maximum,
    _Mode,
    _Open,
    _PollWater,
    _Ratio,
    _Reagents,
    _SettingW,
    _Temperature,
):
    _hash: int = 1947944864
    _prefab_name: int = "StructureFurnace"

    @property
    def RecipeHash(self) -> float:
        return _DeviceLogicType(self, _LT.RecipeHash)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _Furnaces(
    _BaseStructures,
    _Activates,
    _BaseGass,
    _ClearMemorys,
    _Combustions,
    _ExportCounts,
    _Hydrogens,
    _ImportCounts,
    _Locks,
    _Maximums,
    _Modes,
    _Opens,
    _PollWaters,
    _Ratios,
    _Reagentss,
    _SettingWs,
    _Temperatures,
):
    _hash: int = 1947944864
    _prefab_name: int = "StructureFurnace"

    def __getitem__(self, name: str | int | float) -> "_Furnaces":
        return _Furnaces(name)

    @property
    def RecipeHash(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RecipeHash)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


Furnaces: _Furnaces = _Furnaces()


class LargeRocketGasFuelTank(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = -988382953
    _prefab_name: int = "StructureLargeRocketGasFuelTank"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _LargeRocketGasFuelTanks(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = -988382953
    _prefab_name: int = "StructureLargeRocketGasFuelTank"

    def __getitem__(self, name: str | int | float) -> "_LargeRocketGasFuelTanks":
        return _LargeRocketGasFuelTanks(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


LargeRocketGasFuelTanks: _LargeRocketGasFuelTanks = _LargeRocketGasFuelTanks()


class MediumRocketGasFuelTank(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = -1093860567
    _prefab_name: int = "StructureMediumRocketGasFuelTank"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _MediumRocketGasFuelTanks(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = -1093860567
    _prefab_name: int = "StructureMediumRocketGasFuelTank"

    def __getitem__(self, name: str | int | float) -> "_MediumRocketGasFuelTanks":
        return _MediumRocketGasFuelTanks(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


MediumRocketGasFuelTanks: _MediumRocketGasFuelTanks = _MediumRocketGasFuelTanks()


class CapsuleTankGas(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = -1385712131
    _prefab_name: int = "StructureCapsuleTankGas"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _CapsuleTankGass(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = -1385712131
    _prefab_name: int = "StructureCapsuleTankGas"

    def __getitem__(self, name: str | int | float) -> "_CapsuleTankGass":
        return _CapsuleTankGass(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


CapsuleTankGass: _CapsuleTankGass = _CapsuleTankGass()


class GasGenerator(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Error,
    _Hydrogen,
    _Maximum,
    _PollWater,
    _Power,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = 1165997963
    _prefab_name: int = "StructureGasGenerator"

    @property
    def PowerGeneration(self) -> float:
        return _DeviceLogicType(self, _LT.PowerGeneration)


class _GasGenerators(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _Maximums,
    _PollWaters,
    _Powers,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = 1165997963
    _prefab_name: int = "StructureGasGenerator"

    def __getitem__(self, name: str | int | float) -> "_GasGenerators":
        return _GasGenerators(name)

    @property
    def PowerGeneration(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerGeneration)


GasGenerators: _GasGenerators = _GasGenerators()


class GasMixer(_BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = 2104106366
    _prefab_name: int = "StructureGasMixer"


class _GasMixers(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 2104106366
    _prefab_name: int = "StructureGasMixer"

    def __getitem__(self, name: str | int | float) -> "_GasMixers":
        return _GasMixers(name)


GasMixers: _GasMixers = _GasMixers()


class GasSensor(_BaseStructure, _BaseGas, _Hydrogen, _PollWater, _Temperature):
    _hash: int = -1252983604
    _prefab_name: int = "StructureGasSensor"

    @property
    def Combustion(self) -> float:
        return _DeviceLogicType(self, _LT.Combustion)


class _GasSensors(_BaseStructures, _BaseGass, _Hydrogens, _PollWaters, _Temperatures):
    _hash: int = -1252983604
    _prefab_name: int = "StructureGasSensor"

    def __getitem__(self, name: str | int | float) -> "_GasSensors":
        return _GasSensors(name)

    @property
    def Combustion(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Combustion)


GasSensors: _GasSensors = _GasSensors()


class GasTankStorage(_BaseStructure, _Quantity, _Temperature):
    _hash: int = 1632165346
    _prefab_name: int = "StructureGasTankStorage"

    @property
    def RatioCarbonDioxide(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxide)

    @property
    def RatioNitrogen(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogen)

    @property
    def RatioNitrousOxide(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxide)

    @property
    def RatioOxygen(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygen)

    @property
    def RatioPollutant(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutant)

    @property
    def RatioVolatiles(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatiles)

    @property
    def RatioWater(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWater)

    @property
    def slot0(self) -> _SlotTypeGasCanister:
        return _SlotTypeGasCanister(self, 0)

    @property
    def GasCanister(self) -> _SlotTypeGasCanister:
        return self.slot0


class _GasTankStorages(_BaseStructures, _Quantitys, _Temperatures):
    _hash: int = 1632165346
    _prefab_name: int = "StructureGasTankStorage"

    def __getitem__(self, name: str | int | float) -> "_GasTankStorages":
        return _GasTankStorages(name)

    @property
    def RatioCarbonDioxide(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxide)

    @property
    def RatioNitrogen(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogen)

    @property
    def RatioNitrousOxide(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxide)

    @property
    def RatioOxygen(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygen)

    @property
    def RatioPollutant(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutant)

    @property
    def RatioVolatiles(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatiles)

    @property
    def RatioWater(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWater)

    @property
    def slot0(self) -> _SlotTypeGasCanisters:
        return _SlotTypeGasCanisters(self, 0)

    @property
    def GasCanister(self) -> _SlotTypeGasCanisters:
        return self.slot0


GasTankStorages: _GasTankStorages = _GasTankStorages()


class SolidFuelGenerator(_BaseStructure, _ClearMemory, _ImportCount, _Lock, _On):
    _hash: int = 813146305
    _prefab_name: int = "StructureSolidFuelGenerator"

    @property
    def PowerGeneration(self) -> float:
        return _DeviceLogicType(self, _LT.PowerGeneration)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Input(self) -> _SlotTypeCommon:
        return self.slot0


class _SolidFuelGenerators(_BaseStructures, _ClearMemorys, _ImportCounts, _Locks, _Ons):
    _hash: int = 813146305
    _prefab_name: int = "StructureSolidFuelGenerator"

    def __getitem__(self, name: str | int | float) -> "_SolidFuelGenerators":
        return _SolidFuelGenerators(name)

    @property
    def PowerGeneration(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerGeneration)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Input(self) -> _SlotTypeCommons:
        return self.slot0


SolidFuelGenerators: _SolidFuelGenerators = _SolidFuelGenerators()


class GlassDoor(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = -324331872
    _prefab_name: int = "StructureGlassDoor"


class _GlassDoors(_BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs):
    _hash: int = -324331872
    _prefab_name: int = "StructureGlassDoor"

    def __getitem__(self, name: str | int | float) -> "_GlassDoors":
        return _GlassDoors(name)


GlassDoors: _GlassDoors = _GlassDoors()


class GrowLight(_BaseStructure, _Lock, _Power):
    _hash: int = -1758710260
    _prefab_name: int = "StructureGrowLight"


class _GrowLights(_BaseStructures, _Locks, _Powers):
    _hash: int = -1758710260
    _prefab_name: int = "StructureGrowLight"

    def __getitem__(self, name: str | int | float) -> "_GrowLights":
        return _GrowLights(name)


GrowLights: _GrowLights = _GrowLights()


class Harvie(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Mode,
    _Power,
):
    _hash: int = 958056199
    _prefab_name: int = "StructureHarvie"

    @property
    def Harvest(self) -> float:
        return _DeviceLogicType(self, _LT.Harvest)

    @Harvest.setter
    def Harvest(self, value: int | float):
        pass

    @property
    def Plant(self) -> float:
        return _DeviceLogicType(self, _LT.Plant)

    @Plant.setter
    def Plant(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def Hand(self) -> _SlotTypeCommon:
        return self.slot2


class _Harvies(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Modes,
    _Powers,
):
    _hash: int = 958056199
    _prefab_name: int = "StructureHarvie"

    def __getitem__(self, name: str | int | float) -> "_Harvies":
        return _Harvies(name)

    @property
    def Harvest(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Harvest)

    @Harvest.setter
    def Harvest(self, value: int | float):
        pass

    @property
    def Plant(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Plant)

    @Plant.setter
    def Plant(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def Hand(self) -> _SlotTypeCommons:
        return self.slot2


Harvies: _Harvies = _Harvies()


class HydraulicPipeBender(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Open,
    _Power,
    _Reagents,
    _RecipeHash,
):
    _hash: int = -1888248335
    _prefab_name: int = "StructureHydraulicPipeBender"

    @property
    def CompletionRatio(self) -> float:
        return _DeviceLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> float:
        return _DeviceLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _HydraulicPipeBenders(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Opens,
    _Powers,
    _Reagentss,
    _RecipeHashs,
):
    _hash: int = -1888248335
    _prefab_name: int = "StructureHydraulicPipeBender"

    def __getitem__(self, name: str | int | float) -> "_HydraulicPipeBenders":
        return _HydraulicPipeBenders(name)

    @property
    def CompletionRatio(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


HydraulicPipeBenders: _HydraulicPipeBenders = _HydraulicPipeBenders()


class HydroponicsTrayData(
    _BaseStructure, _BaseGas, _Combustion, _Hydrogen, _PollWater, _Temperature
):
    _hash: int = -1841632400
    _prefab_name: int = "StructureHydroponicsTrayData"

    @property
    def slot0(self) -> _SlotTypePlant:
        return _SlotTypePlant(self, 0)

    @property
    def Plant(self) -> _SlotTypePlant:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Fertiliser(self) -> _SlotTypeCommon:
        return self.slot1


class _HydroponicsTrayDatas(
    _BaseStructures, _BaseGass, _Combustions, _Hydrogens, _PollWaters, _Temperatures
):
    _hash: int = -1841632400
    _prefab_name: int = "StructureHydroponicsTrayData"

    def __getitem__(self, name: str | int | float) -> "_HydroponicsTrayDatas":
        return _HydroponicsTrayDatas(name)

    @property
    def slot0(self) -> _SlotTypePlants:
        return _SlotTypePlants(self, 0)

    @property
    def Plant(self) -> _SlotTypePlants:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Fertiliser(self) -> _SlotTypeCommons:
        return self.slot1


HydroponicsTrayDatas: _HydroponicsTrayDatas = _HydroponicsTrayDatas()


class HydroponicsStation(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Error,
    _Hydrogen,
    _Maximum,
    _PollWater,
    _Power,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = 1441767298
    _prefab_name: int = "StructureHydroponicsStation"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypePlant:
        return _SlotTypePlant(self, 0)

    @property
    def slot1(self) -> _SlotTypePlant:
        return _SlotTypePlant(self, 1)

    @property
    def slot2(self) -> _SlotTypePlant:
        return _SlotTypePlant(self, 2)

    @property
    def slot3(self) -> _SlotTypePlant:
        return _SlotTypePlant(self, 3)

    @property
    def slot4(self) -> _SlotTypePlant:
        return _SlotTypePlant(self, 4)

    @property
    def slot5(self) -> _SlotTypePlant:
        return _SlotTypePlant(self, 5)

    @property
    def slot6(self) -> _SlotTypePlant:
        return _SlotTypePlant(self, 6)

    @property
    def slot7(self) -> _SlotTypePlant:
        return _SlotTypePlant(self, 7)


class _HydroponicsStations(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _Maximums,
    _PollWaters,
    _Powers,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = 1441767298
    _prefab_name: int = "StructureHydroponicsStation"

    def __getitem__(self, name: str | int | float) -> "_HydroponicsStations":
        return _HydroponicsStations(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypePlants:
        return _SlotTypePlants(self, 0)

    @property
    def slot1(self) -> _SlotTypePlants:
        return _SlotTypePlants(self, 1)

    @property
    def slot2(self) -> _SlotTypePlants:
        return _SlotTypePlants(self, 2)

    @property
    def slot3(self) -> _SlotTypePlants:
        return _SlotTypePlants(self, 3)

    @property
    def slot4(self) -> _SlotTypePlants:
        return _SlotTypePlants(self, 4)

    @property
    def slot5(self) -> _SlotTypePlants:
        return _SlotTypePlants(self, 5)

    @property
    def slot6(self) -> _SlotTypePlants:
        return _SlotTypePlants(self, 6)

    @property
    def slot7(self) -> _SlotTypePlants:
        return _SlotTypePlants(self, 7)


HydroponicsStations: _HydroponicsStations = _HydroponicsStations()


class CircuitHousing(_BaseStructure, _Error, _Mode, _Power, _SettingW):
    _hash: int = -128473777
    _prefab_name: int = "StructureCircuitHousing"

    @property
    def LineNumber(self) -> float:
        return _DeviceLogicType(self, _LT.LineNumber)

    @LineNumber.setter
    def LineNumber(self, value: int | float):
        pass

    @property
    def StackSize(self) -> float:
        return _DeviceLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeProgrammableChip:
        return _SlotTypeProgrammableChip(self, 0)

    @property
    def ProgrammableChip(self) -> _SlotTypeProgrammableChip:
        return self.slot0


class _CircuitHousings(_BaseStructures, _Errors, _Modes, _Powers, _SettingWs):
    _hash: int = -128473777
    _prefab_name: int = "StructureCircuitHousing"

    def __getitem__(self, name: str | int | float) -> "_CircuitHousings":
        return _CircuitHousings(name)

    @property
    def LineNumber(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.LineNumber)

    @LineNumber.setter
    def LineNumber(self, value: int | float):
        pass

    @property
    def StackSize(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeProgrammableChips:
        return _SlotTypeProgrammableChips(self, 0)

    @property
    def ProgrammableChip(self) -> _SlotTypeProgrammableChips:
        return self.slot0


CircuitHousings: _CircuitHousings = _CircuitHousings()


class CircuitHousingCompact(_BaseStructure, _Error, _Mode, _Power, _SettingW):
    _hash: int = 2037291645
    _prefab_name: int = "StructureCircuitHousingCompact"

    @property
    def LineNumber(self) -> float:
        return _DeviceLogicType(self, _LT.LineNumber)

    @LineNumber.setter
    def LineNumber(self, value: int | float):
        pass

    @property
    def StackSize(self) -> float:
        return _DeviceLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeProgrammableChip:
        return _SlotTypeProgrammableChip(self, 0)

    @property
    def ProgrammableChip(self) -> _SlotTypeProgrammableChip:
        return self.slot0


class _CircuitHousingCompacts(_BaseStructures, _Errors, _Modes, _Powers, _SettingWs):
    _hash: int = 2037291645
    _prefab_name: int = "StructureCircuitHousingCompact"

    def __getitem__(self, name: str | int | float) -> "_CircuitHousingCompacts":
        return _CircuitHousingCompacts(name)

    @property
    def LineNumber(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.LineNumber)

    @LineNumber.setter
    def LineNumber(self, value: int | float):
        pass

    @property
    def StackSize(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeProgrammableChips:
        return _SlotTypeProgrammableChips(self, 0)

    @property
    def ProgrammableChip(self) -> _SlotTypeProgrammableChips:
        return self.slot0


CircuitHousingCompacts: _CircuitHousingCompacts = _CircuitHousingCompacts()


class IceCrusher(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ImportCount,
    _Lock,
    _Maximum,
    _Power,
    _Ratio,
    _SettingW,
):
    _hash: int = 443849486
    _prefab_name: int = "StructureIceCrusher"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0


class _IceCrushers(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ImportCounts,
    _Locks,
    _Maximums,
    _Powers,
    _Ratios,
    _SettingWs,
):
    _hash: int = 443849486
    _prefab_name: int = "StructureIceCrusher"

    def __getitem__(self, name: str | int | float) -> "_IceCrushers":
        return _IceCrushers(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0


IceCrushers: _IceCrushers = _IceCrushers()


class Igniter(_BaseStructure, _On):
    _hash: int = 1005491513
    _prefab_name: int = "StructureIgniter"


class _Igniters(_BaseStructures, _Ons):
    _hash: int = 1005491513
    _prefab_name: int = "StructureIgniter"

    def __getitem__(self, name: str | int | float) -> "_Igniters":
        return _Igniters(name)


Igniters: _Igniters = _Igniters()


class EmergencyButton(
    _BaseStructure, _Activate, _Error, _Lock, _Open, _Power, _SettingR
):
    _hash: int = 1668452680
    _prefab_name: int = "StructureEmergencyButton"


class _EmergencyButtons(
    _BaseStructures, _Activates, _Errors, _Locks, _Opens, _Powers, _SettingRs
):
    _hash: int = 1668452680
    _prefab_name: int = "StructureEmergencyButton"

    def __getitem__(self, name: str | int | float) -> "_EmergencyButtons":
        return _EmergencyButtons(name)


EmergencyButtons: _EmergencyButtons = _EmergencyButtons()


class InteriorDoorGlass(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = -2096421875
    _prefab_name: int = "StructureInteriorDoorGlass"


class _InteriorDoorGlasss(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = -2096421875
    _prefab_name: int = "StructureInteriorDoorGlass"

    def __getitem__(self, name: str | int | float) -> "_InteriorDoorGlasss":
        return _InteriorDoorGlasss(name)


InteriorDoorGlasss: _InteriorDoorGlasss = _InteriorDoorGlasss()


class InteriorDoorPadded(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = 847461335
    _prefab_name: int = "StructureInteriorDoorPadded"


class _InteriorDoorPaddeds(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = 847461335
    _prefab_name: int = "StructureInteriorDoorPadded"

    def __getitem__(self, name: str | int | float) -> "_InteriorDoorPaddeds":
        return _InteriorDoorPaddeds(name)


InteriorDoorPaddeds: _InteriorDoorPaddeds = _InteriorDoorPaddeds()


class InteriorDoorPaddedThin(
    _BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW
):
    _hash: int = 1981698201
    _prefab_name: int = "StructureInteriorDoorPaddedThin"


class _InteriorDoorPaddedThins(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = 1981698201
    _prefab_name: int = "StructureInteriorDoorPaddedThin"

    def __getitem__(self, name: str | int | float) -> "_InteriorDoorPaddedThins":
        return _InteriorDoorPaddedThins(name)


InteriorDoorPaddedThins: _InteriorDoorPaddedThins = _InteriorDoorPaddedThins()


class InteriorDoorTriangle(
    _BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW
):
    _hash: int = -1182923101
    _prefab_name: int = "StructureInteriorDoorTriangle"


class _InteriorDoorTriangles(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = -1182923101
    _prefab_name: int = "StructureInteriorDoorTriangle"

    def __getitem__(self, name: str | int | float) -> "_InteriorDoorTriangles":
        return _InteriorDoorTriangles(name)


InteriorDoorTriangles: _InteriorDoorTriangles = _InteriorDoorTriangles()


class Klaxon(_BaseStructure, _Mode, _Power):
    _hash: int = -828056979
    _prefab_name: int = "StructureKlaxon"

    @property
    def SoundAlert(self) -> float:
        return _DeviceLogicType(self, _LT.SoundAlert)

    @SoundAlert.setter
    def SoundAlert(self, value: int | float):
        pass

    @property
    def Volume(self) -> float:
        return _DeviceLogicType(self, _LT.Volume)

    @Volume.setter
    def Volume(self, value: int | float):
        pass


class _Klaxons(_BaseStructures, _Modes, _Powers):
    _hash: int = -828056979
    _prefab_name: int = "StructureKlaxon"

    def __getitem__(self, name: str | int | float) -> "_Klaxons":
        return _Klaxons(name)

    @property
    def SoundAlert(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SoundAlert)

    @SoundAlert.setter
    def SoundAlert(self, value: int | float):
        pass

    @property
    def Volume(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Volume)

    @Volume.setter
    def Volume(self, value: int | float):
        pass


Klaxons: _Klaxons = _Klaxons()


class RoboticArmDock(_BaseStructure, _Activate, _Error, _Idle, _Power, _SettingW):
    _hash: int = -1818718810
    _prefab_name: int = "StructureRoboticArmDock"

    @property
    def Extended(self) -> float:
        return _DeviceLogicType(self, _LT.Extended)

    @property
    def PositionX(self) -> float:
        return _DeviceLogicType(self, _LT.PositionX)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def ArmSlot(self) -> _SlotTypeCommon:
        return self.slot0


class _RoboticArmDocks(
    _BaseStructures, _Activates, _Errors, _Idles, _Powers, _SettingWs
):
    _hash: int = -1818718810
    _prefab_name: int = "StructureRoboticArmDock"

    def __getitem__(self, name: str | int | float) -> "_RoboticArmDocks":
        return _RoboticArmDocks(name)

    @property
    def Extended(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Extended)

    @property
    def PositionX(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PositionX)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def ArmSlot(self) -> _SlotTypeCommons:
        return self.slot0


RoboticArmDocks: _RoboticArmDocks = _RoboticArmDocks()


class LarreDockAtmos(
    _BaseStructure,
    _Activate,
    _BaseGas,
    _BaseGasInput,
    _Combustion,
    _Error,
    _Hydrogen,
    _Idle,
    _Mode,
    _Open,
    _PollWater,
    _Power,
    _SettingW,
    _Temperature,
):
    _hash: int = 1978422481
    _prefab_name: int = "StructureLarreDockAtmos"

    @property
    def CombustionInput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionInput)

    @property
    def Extended(self) -> float:
        return _DeviceLogicType(self, _LT.Extended)

    @property
    def PositionX(self) -> float:
        return _DeviceLogicType(self, _LT.PositionX)

    @property
    def PressureExternal(self) -> float:
        return _DeviceLogicType(self, _LT.PressureExternal)

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass

    @property
    def PressureInput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureInput)

    @property
    def PressureInternal(self) -> float:
        return _DeviceLogicType(self, _LT.PressureInternal)

    @PressureInternal.setter
    def PressureInternal(self, value: int | float):
        pass

    @property
    def TemperatureInput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureInput)

    @property
    def TotalMolesInput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesInput)

    @property
    def slot0(self) -> _SlotTypeFilter:
        return _SlotTypeFilter(self, 0)

    @property
    def Filter(self) -> _SlotTypeFilter:
        return self.slot0


class _LarreDockAtmoss(
    _BaseStructures,
    _Activates,
    _BaseGasInputs,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _Idles,
    _Modes,
    _Opens,
    _PollWaters,
    _Powers,
    _SettingWs,
    _Temperatures,
):
    _hash: int = 1978422481
    _prefab_name: int = "StructureLarreDockAtmos"

    def __getitem__(self, name: str | int | float) -> "_LarreDockAtmoss":
        return _LarreDockAtmoss(name)

    @property
    def CombustionInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionInput)

    @property
    def Extended(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Extended)

    @property
    def PositionX(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PositionX)

    @property
    def PressureExternal(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureExternal)

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass

    @property
    def PressureInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureInput)

    @property
    def PressureInternal(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureInternal)

    @PressureInternal.setter
    def PressureInternal(self, value: int | float):
        pass

    @property
    def TemperatureInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureInput)

    @property
    def TotalMolesInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesInput)

    @property
    def slot0(self) -> _SlotTypeFilters:
        return _SlotTypeFilters(self, 0)

    @property
    def Filter(self) -> _SlotTypeFilters:
        return self.slot0


LarreDockAtmoss: _LarreDockAtmoss = _LarreDockAtmoss()


class LarreDockBypass(_BaseStructure, _Open, _Power):
    _hash: int = 1011275082
    _prefab_name: int = "StructureLarreDockBypass"


class _LarreDockBypasss(_BaseStructures, _Opens, _Powers):
    _hash: int = 1011275082
    _prefab_name: int = "StructureLarreDockBypass"

    def __getitem__(self, name: str | int | float) -> "_LarreDockBypasss":
        return _LarreDockBypasss(name)


LarreDockBypasss: _LarreDockBypasss = _LarreDockBypasss()


class LarreDockCargo(
    _BaseStructure, _Activate, _Error, _Idle, _Open, _Power, _SettingW
):
    _hash: int = -1555459562
    _prefab_name: int = "StructureLarreDockCargo"

    @property
    def Extended(self) -> float:
        return _DeviceLogicType(self, _LT.Extended)

    @property
    def PositionX(self) -> float:
        return _DeviceLogicType(self, _LT.PositionX)

    @property
    def TargetPrefabHash(self) -> float:
        return _DeviceLogicType(self, _LT.TargetPrefabHash)

    @property
    def TargetSlotIndex(self) -> float:
        return _DeviceLogicType(self, _LT.TargetSlotIndex)

    @TargetSlotIndex.setter
    def TargetSlotIndex(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def ArmSlot(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot255(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 255)

    @property
    def TargetSlot(self) -> _SlotTypeCommon:
        return self.slot255


class _LarreDockCargos(
    _BaseStructures, _Activates, _Errors, _Idles, _Opens, _Powers, _SettingWs
):
    _hash: int = -1555459562
    _prefab_name: int = "StructureLarreDockCargo"

    def __getitem__(self, name: str | int | float) -> "_LarreDockCargos":
        return _LarreDockCargos(name)

    @property
    def Extended(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Extended)

    @property
    def PositionX(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PositionX)

    @property
    def TargetPrefabHash(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TargetPrefabHash)

    @property
    def TargetSlotIndex(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TargetSlotIndex)

    @TargetSlotIndex.setter
    def TargetSlotIndex(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def ArmSlot(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot255(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 255)

    @property
    def TargetSlot(self) -> _SlotTypeCommons:
        return self.slot255


LarreDockCargos: _LarreDockCargos = _LarreDockCargos()


class LarreDockCollector(
    _BaseStructure,
    _Activate,
    _Error,
    _Idle,
    _Mode,
    _Open,
    _Power,
    _Quantity,
    _Ratio,
    _SettingW,
):
    _hash: int = -522428667
    _prefab_name: int = "StructureLarreDockCollector"

    @property
    def Extended(self) -> float:
        return _DeviceLogicType(self, _LT.Extended)

    @property
    def PositionX(self) -> float:
        return _DeviceLogicType(self, _LT.PositionX)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def slot10(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 10)

    @property
    def slot11(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 14)

    @property
    def slot15(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 15)

    @property
    def slot16(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 16)

    @property
    def slot17(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 17)

    @property
    def slot18(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 18)

    @property
    def slot19(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 19)

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def slot3(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 3)

    @property
    def slot4(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 4)

    @property
    def slot5(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 5)

    @property
    def slot6(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 6)

    @property
    def slot7(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 7)

    @property
    def slot8(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 8)

    @property
    def slot9(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 9)


class _LarreDockCollectors(
    _BaseStructures,
    _Activates,
    _Errors,
    _Idles,
    _Modes,
    _Opens,
    _Powers,
    _Quantitys,
    _Ratios,
    _SettingWs,
):
    _hash: int = -522428667
    _prefab_name: int = "StructureLarreDockCollector"

    def __getitem__(self, name: str | int | float) -> "_LarreDockCollectors":
        return _LarreDockCollectors(name)

    @property
    def Extended(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Extended)

    @property
    def PositionX(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PositionX)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def slot10(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 10)

    @property
    def slot11(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 14)

    @property
    def slot15(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 15)

    @property
    def slot16(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 16)

    @property
    def slot17(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 17)

    @property
    def slot18(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 18)

    @property
    def slot19(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 19)

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def slot3(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 3)

    @property
    def slot4(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 4)

    @property
    def slot5(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 5)

    @property
    def slot6(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 6)

    @property
    def slot7(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 7)

    @property
    def slot8(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 8)

    @property
    def slot9(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 9)


LarreDockCollectors: _LarreDockCollectors = _LarreDockCollectors()


class LarreDockHydroponics(
    _BaseStructure, _Activate, _Error, _Idle, _Open, _Power, _SettingW
):
    _hash: int = 85133079
    _prefab_name: int = "StructureLarreDockHydroponics"

    @property
    def Extended(self) -> float:
        return _DeviceLogicType(self, _LT.Extended)

    @property
    def PositionX(self) -> float:
        return _DeviceLogicType(self, _LT.PositionX)

    @property
    def TargetPrefabHash(self) -> float:
        return _DeviceLogicType(self, _LT.TargetPrefabHash)

    @property
    def TargetSlotIndex(self) -> float:
        return _DeviceLogicType(self, _LT.TargetSlotIndex)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def ArmSlot(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def HopperSlot(self) -> _SlotTypeCommon:
        return self.slot1

    @property
    def slot255(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 255)

    @property
    def TargetSlot(self) -> _SlotTypeCommon:
        return self.slot255


class _LarreDockHydroponicss(
    _BaseStructures, _Activates, _Errors, _Idles, _Opens, _Powers, _SettingWs
):
    _hash: int = 85133079
    _prefab_name: int = "StructureLarreDockHydroponics"

    def __getitem__(self, name: str | int | float) -> "_LarreDockHydroponicss":
        return _LarreDockHydroponicss(name)

    @property
    def Extended(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Extended)

    @property
    def PositionX(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PositionX)

    @property
    def TargetPrefabHash(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TargetPrefabHash)

    @property
    def TargetSlotIndex(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TargetSlotIndex)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def ArmSlot(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def HopperSlot(self) -> _SlotTypeCommons:
        return self.slot1

    @property
    def slot255(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 255)

    @property
    def TargetSlot(self) -> _SlotTypeCommons:
        return self.slot255


LarreDockHydroponicss: _LarreDockHydroponicss = _LarreDockHydroponicss()


class Diode(_BaseStructure, _Lock, _Power):
    _hash: int = 1944485013
    _prefab_name: int = "StructureDiode"

    @property
    def Color(self) -> float:
        return _DeviceLogicType(self, _LT.Color)

    @Color.setter
    def Color(self, value: int | float):
        pass


class _Diodes(_BaseStructures, _Locks, _Powers):
    _hash: int = 1944485013
    _prefab_name: int = "StructureDiode"

    def __getitem__(self, name: str | int | float) -> "_Diodes":
        return _Diodes(name)

    @property
    def Color(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Color)

    @Color.setter
    def Color(self, value: int | float):
        pass


Diodes: _Diodes = _Diodes()


class ConsoleLED1x3(_BaseStructure, _Error, _Mode, _Power, _SettingW):
    _hash: int = -1949054743
    _prefab_name: int = "StructureConsoleLED1x3"

    @property
    def Color(self) -> float:
        return _DeviceLogicType(self, _LT.Color)

    @Color.setter
    def Color(self, value: int | float):
        pass


class _ConsoleLED1x3s(_BaseStructures, _Errors, _Modes, _Powers, _SettingWs):
    _hash: int = -1949054743
    _prefab_name: int = "StructureConsoleLED1x3"

    def __getitem__(self, name: str | int | float) -> "_ConsoleLED1x3s":
        return _ConsoleLED1x3s(name)

    @property
    def Color(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Color)

    @Color.setter
    def Color(self, value: int | float):
        pass


ConsoleLED1x3s: _ConsoleLED1x3s = _ConsoleLED1x3s()


class ConsoleLED1x2(_BaseStructure, _Error, _Mode, _Power, _SettingW):
    _hash: int = -53151617
    _prefab_name: int = "StructureConsoleLED1x2"

    @property
    def Color(self) -> float:
        return _DeviceLogicType(self, _LT.Color)

    @Color.setter
    def Color(self, value: int | float):
        pass


class _ConsoleLED1x2s(_BaseStructures, _Errors, _Modes, _Powers, _SettingWs):
    _hash: int = -53151617
    _prefab_name: int = "StructureConsoleLED1x2"

    def __getitem__(self, name: str | int | float) -> "_ConsoleLED1x2s":
        return _ConsoleLED1x2s(name)

    @property
    def Color(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Color)

    @Color.setter
    def Color(self, value: int | float):
        pass


ConsoleLED1x2s: _ConsoleLED1x2s = _ConsoleLED1x2s()


class ConsoleLED5(_BaseStructure, _Error, _Mode, _Power, _SettingW):
    _hash: int = -815193061
    _prefab_name: int = "StructureConsoleLED5"

    @property
    def Color(self) -> float:
        return _DeviceLogicType(self, _LT.Color)

    @Color.setter
    def Color(self, value: int | float):
        pass


class _ConsoleLED5s(_BaseStructures, _Errors, _Modes, _Powers, _SettingWs):
    _hash: int = -815193061
    _prefab_name: int = "StructureConsoleLED5"

    def __getitem__(self, name: str | int | float) -> "_ConsoleLED5s":
        return _ConsoleLED5s(name)

    @property
    def Color(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Color)

    @Color.setter
    def Color(self, value: int | float):
        pass


ConsoleLED5s: _ConsoleLED5s = _ConsoleLED5s()


class LargeDirectHeatExchangeLiquidtoLiquid(
    _BaseStructure, _Maximum, _Ratio, _SettingW
):
    _hash: int = 792686502
    _prefab_name: int = "StructureLargeDirectHeatExchangeLiquidtoLiquid"


class _LargeDirectHeatExchangeLiquidtoLiquids(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = 792686502
    _prefab_name: int = "StructureLargeDirectHeatExchangeLiquidtoLiquid"

    def __getitem__(
        self, name: str | int | float
    ) -> "_LargeDirectHeatExchangeLiquidtoLiquids":
        return _LargeDirectHeatExchangeLiquidtoLiquids(name)


LargeDirectHeatExchangeLiquidtoLiquids: _LargeDirectHeatExchangeLiquidtoLiquids = (
    _LargeDirectHeatExchangeLiquidtoLiquids()
)


class LargeDirectHeatExchangeGastoGas(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -1230658883
    _prefab_name: int = "StructureLargeDirectHeatExchangeGastoGas"


class _LargeDirectHeatExchangeGastoGass(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = -1230658883
    _prefab_name: int = "StructureLargeDirectHeatExchangeGastoGas"

    def __getitem__(
        self, name: str | int | float
    ) -> "_LargeDirectHeatExchangeGastoGass":
        return _LargeDirectHeatExchangeGastoGass(name)


LargeDirectHeatExchangeGastoGass: _LargeDirectHeatExchangeGastoGass = (
    _LargeDirectHeatExchangeGastoGass()
)


class LargeDirectHeatExchangeGastoLiquid(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 1412338038
    _prefab_name: int = "StructureLargeDirectHeatExchangeGastoLiquid"


class _LargeDirectHeatExchangeGastoLiquids(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = 1412338038
    _prefab_name: int = "StructureLargeDirectHeatExchangeGastoLiquid"

    def __getitem__(
        self, name: str | int | float
    ) -> "_LargeDirectHeatExchangeGastoLiquids":
        return _LargeDirectHeatExchangeGastoLiquids(name)


LargeDirectHeatExchangeGastoLiquids: _LargeDirectHeatExchangeGastoLiquids = (
    _LargeDirectHeatExchangeGastoLiquids()
)


class LargeExtendableRadiator(
    _BaseStructure, _Lock, _Maximum, _Open, _Ratio, _SettingW
):
    _hash: int = -566775170
    _prefab_name: int = "StructureLargeExtendableRadiator"

    @property
    def Horizontal(self) -> float:
        return _DeviceLogicType(self, _LT.Horizontal)

    @Horizontal.setter
    def Horizontal(self, value: int | float):
        pass


class _LargeExtendableRadiators(
    _BaseStructures, _Locks, _Maximums, _Opens, _Ratios, _SettingWs
):
    _hash: int = -566775170
    _prefab_name: int = "StructureLargeExtendableRadiator"

    def __getitem__(self, name: str | int | float) -> "_LargeExtendableRadiators":
        return _LargeExtendableRadiators(name)

    @property
    def Horizontal(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Horizontal)

    @Horizontal.setter
    def Horizontal(self, value: int | float):
        pass


LargeExtendableRadiators: _LargeExtendableRadiators = _LargeExtendableRadiators()


class LargeHangerDoor(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = -1351081801
    _prefab_name: int = "StructureLargeHangerDoor"


class _LargeHangerDoors(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = -1351081801
    _prefab_name: int = "StructureLargeHangerDoor"

    def __getitem__(self, name: str | int | float) -> "_LargeHangerDoors":
        return _LargeHangerDoors(name)


LargeHangerDoors: _LargeHangerDoors = _LargeHangerDoors()


class LargeSatelliteDish(
    _BaseStructure, _Activate, _Error, _Idle, _Power, _SettingW, _VerticalW
):
    _hash: int = 1913391845
    _prefab_name: int = "StructureLargeSatelliteDish"

    @property
    def BestContactFilter(self) -> float:
        return _DeviceLogicType(self, _LT.BestContactFilter)

    @BestContactFilter.setter
    def BestContactFilter(self, value: int | float):
        pass

    @property
    def ContactTypeId(self) -> float:
        return _DeviceLogicType(self, _LT.ContactTypeId)

    @property
    def InterrogationProgress(self) -> float:
        return _DeviceLogicType(self, _LT.InterrogationProgress)

    @property
    def MinimumWattsToContact(self) -> float:
        return _DeviceLogicType(self, _LT.MinimumWattsToContact)

    @property
    def SignalID(self) -> float:
        return _DeviceLogicType(self, _LT.SignalID)

    @property
    def SignalStrength(self) -> float:
        return _DeviceLogicType(self, _LT.SignalStrength)

    @property
    def SizeX(self) -> float:
        return _DeviceLogicType(self, _LT.SizeX)

    @property
    def SizeZ(self) -> float:
        return _DeviceLogicType(self, _LT.SizeZ)

    @property
    def TargetPadIndex(self) -> float:
        return _DeviceLogicType(self, _LT.TargetPadIndex)

    @TargetPadIndex.setter
    def TargetPadIndex(self, value: int | float):
        pass

    @property
    def WattsReachingContact(self) -> float:
        return _DeviceLogicType(self, _LT.WattsReachingContact)


class _LargeSatelliteDishs(
    _BaseStructures, _Activates, _Errors, _Idles, _Powers, _SettingWs, _VerticalWs
):
    _hash: int = 1913391845
    _prefab_name: int = "StructureLargeSatelliteDish"

    def __getitem__(self, name: str | int | float) -> "_LargeSatelliteDishs":
        return _LargeSatelliteDishs(name)

    @property
    def BestContactFilter(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.BestContactFilter)

    @BestContactFilter.setter
    def BestContactFilter(self, value: int | float):
        pass

    @property
    def ContactTypeId(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ContactTypeId)

    @property
    def InterrogationProgress(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.InterrogationProgress)

    @property
    def MinimumWattsToContact(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.MinimumWattsToContact)

    @property
    def SignalID(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SignalID)

    @property
    def SignalStrength(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SignalStrength)

    @property
    def SizeX(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SizeX)

    @property
    def SizeZ(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SizeZ)

    @property
    def TargetPadIndex(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TargetPadIndex)

    @TargetPadIndex.setter
    def TargetPadIndex(self, value: int | float):
        pass

    @property
    def WattsReachingContact(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.WattsReachingContact)


LargeSatelliteDishs: _LargeSatelliteDishs = _LargeSatelliteDishs()


class TankBig(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _Open,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = -1606848156
    _prefab_name: int = "StructureTankBig"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _TankBigs(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _Opens,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = -1606848156
    _prefab_name: int = "StructureTankBig"

    def __getitem__(self, name: str | int | float) -> "_TankBigs":
        return _TankBigs(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


TankBigs: _TankBigs = _TankBigs()


class LogicSwitch(_BaseStructure, _Lock, _Open, _SettingR):
    _hash: int = 1220484876
    _prefab_name: int = "StructureLogicSwitch"


class _LogicSwitchs(_BaseStructures, _Locks, _Opens, _SettingRs):
    _hash: int = 1220484876
    _prefab_name: int = "StructureLogicSwitch"

    def __getitem__(self, name: str | int | float) -> "_LogicSwitchs":
        return _LogicSwitchs(name)


LogicSwitchs: _LogicSwitchs = _LogicSwitchs()


class LightRound(_BaseStructure, _Lock, _Power):
    _hash: int = 1514476632
    _prefab_name: int = "StructureLightRound"


class _LightRounds(_BaseStructures, _Locks, _Powers):
    _hash: int = 1514476632
    _prefab_name: int = "StructureLightRound"

    def __getitem__(self, name: str | int | float) -> "_LightRounds":
        return _LightRounds(name)


LightRounds: _LightRounds = _LightRounds()


class LightRoundAngled(_BaseStructure, _Lock, _Power):
    _hash: int = 1592905386
    _prefab_name: int = "StructureLightRoundAngled"


class _LightRoundAngleds(_BaseStructures, _Locks, _Powers):
    _hash: int = 1592905386
    _prefab_name: int = "StructureLightRoundAngled"

    def __getitem__(self, name: str | int | float) -> "_LightRoundAngleds":
        return _LightRoundAngleds(name)


LightRoundAngleds: _LightRoundAngleds = _LightRoundAngleds()


class LightRoundSmall(_BaseStructure, _Lock, _Power):
    _hash: int = 1436121888
    _prefab_name: int = "StructureLightRoundSmall"


class _LightRoundSmalls(_BaseStructures, _Locks, _Powers):
    _hash: int = 1436121888
    _prefab_name: int = "StructureLightRoundSmall"

    def __getitem__(self, name: str | int | float) -> "_LightRoundSmalls":
        return _LightRoundSmalls(name)


LightRoundSmalls: _LightRoundSmalls = _LightRoundSmalls()


class RobotArmDoor(_BaseStructure, _Open):
    _hash: int = -2131782367
    _prefab_name: int = "StructureRobotArmDoor"

    @property
    def Power(self) -> float:
        return _DeviceLogicType(self, _LT.Power)

    @property
    def RequiredPower(self) -> float:
        return _DeviceLogicType(self, _LT.RequiredPower)


class _RobotArmDoors(_BaseStructures, _Opens):
    _hash: int = -2131782367
    _prefab_name: int = "StructureRobotArmDoor"

    def __getitem__(self, name: str | int | float) -> "_RobotArmDoors":
        return _RobotArmDoors(name)

    @property
    def Power(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Power)

    @property
    def RequiredPower(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RequiredPower)


RobotArmDoors: _RobotArmDoors = _RobotArmDoors()


class BackLiquidPressureRegulator(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = 2099900163
    _prefab_name: int = "StructureBackLiquidPressureRegulator"


class _BackLiquidPressureRegulators(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 2099900163
    _prefab_name: int = "StructureBackLiquidPressureRegulator"

    def __getitem__(self, name: str | int | float) -> "_BackLiquidPressureRegulators":
        return _BackLiquidPressureRegulators(name)


BackLiquidPressureRegulators: _BackLiquidPressureRegulators = (
    _BackLiquidPressureRegulators()
)


class LargeRocketLiquidFuelTank(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = -1374757070
    _prefab_name: int = "StructureLargeRocketLiquidFuelTank"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _LargeRocketLiquidFuelTanks(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = -1374757070
    _prefab_name: int = "StructureLargeRocketLiquidFuelTank"

    def __getitem__(self, name: str | int | float) -> "_LargeRocketLiquidFuelTanks":
        return _LargeRocketLiquidFuelTanks(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


LargeRocketLiquidFuelTanks: _LargeRocketLiquidFuelTanks = _LargeRocketLiquidFuelTanks()


class MediumRocketLiquidFuelTank(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = 1143639539
    _prefab_name: int = "StructureMediumRocketLiquidFuelTank"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _MediumRocketLiquidFuelTanks(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = 1143639539
    _prefab_name: int = "StructureMediumRocketLiquidFuelTank"

    def __getitem__(self, name: str | int | float) -> "_MediumRocketLiquidFuelTanks":
        return _MediumRocketLiquidFuelTanks(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


MediumRocketLiquidFuelTanks: _MediumRocketLiquidFuelTanks = (
    _MediumRocketLiquidFuelTanks()
)


class CapsuleTankLiquid(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = 1415396263
    _prefab_name: int = "StructureCapsuleTankLiquid"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _CapsuleTankLiquids(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = 1415396263
    _prefab_name: int = "StructureCapsuleTankLiquid"

    def __getitem__(self, name: str | int | float) -> "_CapsuleTankLiquids":
        return _CapsuleTankLiquids(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


CapsuleTankLiquids: _CapsuleTankLiquids = _CapsuleTankLiquids()


class WaterDigitalValve(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = -517628750
    _prefab_name: int = "StructureWaterDigitalValve"


class _WaterDigitalValves(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -517628750
    _prefab_name: int = "StructureWaterDigitalValve"

    def __getitem__(self, name: str | int | float) -> "_WaterDigitalValves":
        return _WaterDigitalValves(name)


WaterDigitalValves: _WaterDigitalValves = _WaterDigitalValves()


class LiquidPipeAnalyzer(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Error,
    _Hydrogen,
    _Lock,
    _PollWater,
    _Power,
    _Temperature,
    _Volume,
):
    _hash: int = -2113838091
    _prefab_name: int = "StructureLiquidPipeAnalyzer"

    @property
    def NetworkFault(self) -> float:
        return _DeviceLogicType(self, _LT.NetworkFault)


class _LiquidPipeAnalyzers(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _Locks,
    _PollWaters,
    _Powers,
    _Temperatures,
    _Volumes,
):
    _hash: int = -2113838091
    _prefab_name: int = "StructureLiquidPipeAnalyzer"

    def __getitem__(self, name: str | int | float) -> "_LiquidPipeAnalyzers":
        return _LiquidPipeAnalyzers(name)

    @property
    def NetworkFault(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.NetworkFault)


LiquidPipeAnalyzers: _LiquidPipeAnalyzers = _LiquidPipeAnalyzers()


class LiquidTankBig(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = 1098900430
    _prefab_name: int = "StructureLiquidTankBig"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _LiquidTankBigs(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = 1098900430
    _prefab_name: int = "StructureLiquidTankBig"

    def __getitem__(self, name: str | int | float) -> "_LiquidTankBigs":
        return _LiquidTankBigs(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


LiquidTankBigs: _LiquidTankBigs = _LiquidTankBigs()


class LiquidTankBigInsulated(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = -1430440215
    _prefab_name: int = "StructureLiquidTankBigInsulated"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _LiquidTankBigInsulateds(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = -1430440215
    _prefab_name: int = "StructureLiquidTankBigInsulated"

    def __getitem__(self, name: str | int | float) -> "_LiquidTankBigInsulateds":
        return _LiquidTankBigInsulateds(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


LiquidTankBigInsulateds: _LiquidTankBigInsulateds = _LiquidTankBigInsulateds()


class LiquidTankSmall(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = 1988118157
    _prefab_name: int = "StructureLiquidTankSmall"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _LiquidTankSmalls(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = 1988118157
    _prefab_name: int = "StructureLiquidTankSmall"

    def __getitem__(self, name: str | int | float) -> "_LiquidTankSmalls":
        return _LiquidTankSmalls(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


LiquidTankSmalls: _LiquidTankSmalls = _LiquidTankSmalls()


class LiquidTankSmallInsulated(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = 608607718
    _prefab_name: int = "StructureLiquidTankSmallInsulated"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _LiquidTankSmallInsulateds(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = 608607718
    _prefab_name: int = "StructureLiquidTankSmallInsulated"

    def __getitem__(self, name: str | int | float) -> "_LiquidTankSmallInsulateds":
        return _LiquidTankSmallInsulateds(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


LiquidTankSmallInsulateds: _LiquidTankSmallInsulateds = _LiquidTankSmallInsulateds()


class LiquidTankStorage(_BaseStructure, _Quantity, _Temperature):
    _hash: int = 1691898022
    _prefab_name: int = "StructureLiquidTankStorage"

    @property
    def RatioCarbonDioxide(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxide)

    @property
    def RatioNitrogen(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogen)

    @property
    def RatioNitrousOxide(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxide)

    @property
    def RatioOxygen(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygen)

    @property
    def RatioPollutant(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutant)

    @property
    def RatioVolatiles(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatiles)

    @property
    def RatioWater(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWater)

    @property
    def slot0(self) -> _SlotTypeGasCanister:
        return _SlotTypeGasCanister(self, 0)

    @property
    def LiquidCanister(self) -> _SlotTypeGasCanister:
        return self.slot0


class _LiquidTankStorages(_BaseStructures, _Quantitys, _Temperatures):
    _hash: int = 1691898022
    _prefab_name: int = "StructureLiquidTankStorage"

    def __getitem__(self, name: str | int | float) -> "_LiquidTankStorages":
        return _LiquidTankStorages(name)

    @property
    def RatioCarbonDioxide(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxide)

    @property
    def RatioNitrogen(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogen)

    @property
    def RatioNitrousOxide(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxide)

    @property
    def RatioOxygen(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygen)

    @property
    def RatioPollutant(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutant)

    @property
    def RatioVolatiles(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatiles)

    @property
    def RatioWater(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWater)

    @property
    def slot0(self) -> _SlotTypeGasCanisters:
        return _SlotTypeGasCanisters(self, 0)

    @property
    def LiquidCanister(self) -> _SlotTypeGasCanisters:
        return self.slot0


LiquidTankStorages: _LiquidTankStorages = _LiquidTankStorages()


class LiquidVolumePump(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = -454028979
    _prefab_name: int = "StructureLiquidVolumePump"


class _LiquidVolumePumps(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -454028979
    _prefab_name: int = "StructureLiquidVolumePump"

    def __getitem__(self, name: str | int | float) -> "_LiquidVolumePumps":
        return _LiquidVolumePumps(name)


LiquidVolumePumps: _LiquidVolumePumps = _LiquidVolumePumps()


class LiquidPressureRegulator(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = 482248766
    _prefab_name: int = "StructureLiquidPressureRegulator"


class _LiquidPressureRegulators(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 482248766
    _prefab_name: int = "StructureLiquidPressureRegulator"

    def __getitem__(self, name: str | int | float) -> "_LiquidPressureRegulators":
        return _LiquidPressureRegulators(name)


LiquidPressureRegulators: _LiquidPressureRegulators = _LiquidPressureRegulators()


class WaterWallCooler(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = -1369060582
    _prefab_name: int = "StructureWaterWallCooler"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def DataDisk(self) -> _SlotTypeCommon:
        return self.slot0


class _WaterWallCoolers(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -1369060582
    _prefab_name: int = "StructureWaterWallCooler"

    def __getitem__(self, name: str | int | float) -> "_WaterWallCoolers":
        return _WaterWallCoolers(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def DataDisk(self) -> _SlotTypeCommons:
        return self.slot0


WaterWallCoolers: _WaterWallCoolers = _WaterWallCoolers()


class StorageLocker(_BaseStructure, _Lock, _Open):
    _hash: int = -793623899
    _prefab_name: int = "StructureStorageLocker"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def slot10(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 10)

    @property
    def slot11(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 14)

    @property
    def slot15(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 15)

    @property
    def slot16(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 16)

    @property
    def slot17(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 17)

    @property
    def slot18(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 18)

    @property
    def slot19(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 19)

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def slot20(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 20)

    @property
    def slot21(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 21)

    @property
    def slot22(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 22)

    @property
    def slot23(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 23)

    @property
    def slot24(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 24)

    @property
    def slot25(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 25)

    @property
    def slot26(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 26)

    @property
    def slot27(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 27)

    @property
    def slot28(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 28)

    @property
    def slot29(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 29)

    @property
    def slot3(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 3)

    @property
    def slot4(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 4)

    @property
    def slot5(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 5)

    @property
    def slot6(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 6)

    @property
    def slot7(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 7)

    @property
    def slot8(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 8)

    @property
    def slot9(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 9)


class _StorageLockers(_BaseStructures, _Locks, _Opens):
    _hash: int = -793623899
    _prefab_name: int = "StructureStorageLocker"

    def __getitem__(self, name: str | int | float) -> "_StorageLockers":
        return _StorageLockers(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def slot10(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 10)

    @property
    def slot11(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 14)

    @property
    def slot15(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 15)

    @property
    def slot16(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 16)

    @property
    def slot17(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 17)

    @property
    def slot18(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 18)

    @property
    def slot19(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 19)

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def slot20(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 20)

    @property
    def slot21(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 21)

    @property
    def slot22(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 22)

    @property
    def slot23(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 23)

    @property
    def slot24(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 24)

    @property
    def slot25(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 25)

    @property
    def slot26(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 26)

    @property
    def slot27(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 27)

    @property
    def slot28(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 28)

    @property
    def slot29(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 29)

    @property
    def slot3(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 3)

    @property
    def slot4(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 4)

    @property
    def slot5(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 5)

    @property
    def slot6(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 6)

    @property
    def slot7(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 7)

    @property
    def slot8(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 8)

    @property
    def slot9(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 9)


StorageLockers: _StorageLockers = _StorageLockers()


class LockerSmall(_BaseStructure, _Lock, _Open):
    _hash: int = -647164662
    _prefab_name: int = "StructureLockerSmall"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def slot3(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 3)


class _LockerSmalls(_BaseStructures, _Locks, _Opens):
    _hash: int = -647164662
    _prefab_name: int = "StructureLockerSmall"

    def __getitem__(self, name: str | int | float) -> "_LockerSmalls":
        return _LockerSmalls(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def slot3(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 3)


LockerSmalls: _LockerSmalls = _LockerSmalls()


class LogicCompare(_BaseStructure, _Error, _Mode, _Power, _SettingR):
    _hash: int = -1489728908
    _prefab_name: int = "StructureLogicCompare"


class _LogicCompares(_BaseStructures, _Errors, _Modes, _Powers, _SettingRs):
    _hash: int = -1489728908
    _prefab_name: int = "StructureLogicCompare"

    def __getitem__(self, name: str | int | float) -> "_LogicCompares":
        return _LogicCompares(name)


LogicCompares: _LogicCompares = _LogicCompares()


class LogicGate(_BaseStructure, _Error, _Mode, _Power, _SettingR):
    _hash: int = 1942143074
    _prefab_name: int = "StructureLogicGate"


class _LogicGates(_BaseStructures, _Errors, _Modes, _Powers, _SettingRs):
    _hash: int = 1942143074
    _prefab_name: int = "StructureLogicGate"

    def __getitem__(self, name: str | int | float) -> "_LogicGates":
        return _LogicGates(name)


LogicGates: _LogicGates = _LogicGates()


class LogicHashGen(_BaseStructure, _SettingR):
    _hash: int = 2077593121
    _prefab_name: int = "StructureLogicHashGen"


class _LogicHashGens(_BaseStructures, _SettingRs):
    _hash: int = 2077593121
    _prefab_name: int = "StructureLogicHashGen"

    def __getitem__(self, name: str | int | float) -> "_LogicHashGens":
        return _LogicHashGens(name)


LogicHashGens: _LogicHashGens = _LogicHashGens()


class LogicMath(_BaseStructure, _Error, _Mode, _Power, _SettingR):
    _hash: int = 1657691323
    _prefab_name: int = "StructureLogicMath"


class _LogicMaths(_BaseStructures, _Errors, _Modes, _Powers, _SettingRs):
    _hash: int = 1657691323
    _prefab_name: int = "StructureLogicMath"

    def __getitem__(self, name: str | int | float) -> "_LogicMaths":
        return _LogicMaths(name)


LogicMaths: _LogicMaths = _LogicMaths()


class LogicMemory(_BaseStructure, _SettingW):
    _hash: int = -851746783
    _prefab_name: int = "StructureLogicMemory"


class _LogicMemorys(_BaseStructures, _SettingWs):
    _hash: int = -851746783
    _prefab_name: int = "StructureLogicMemory"

    def __getitem__(self, name: str | int | float) -> "_LogicMemorys":
        return _LogicMemorys(name)


LogicMemorys: _LogicMemorys = _LogicMemorys()


class LogicMinMax(_BaseStructure, _Error, _Mode, _Power, _SettingR):
    _hash: int = 929022276
    _prefab_name: int = "StructureLogicMinMax"


class _LogicMinMaxs(_BaseStructures, _Errors, _Modes, _Powers, _SettingRs):
    _hash: int = 929022276
    _prefab_name: int = "StructureLogicMinMax"

    def __getitem__(self, name: str | int | float) -> "_LogicMinMaxs":
        return _LogicMinMaxs(name)


LogicMinMaxs: _LogicMinMaxs = _LogicMinMaxs()


class LogicReader(_BaseStructure, _Error, _Power, _SettingR):
    _hash: int = -345383640
    _prefab_name: int = "StructureLogicReader"


class _LogicReaders(_BaseStructures, _Errors, _Powers, _SettingRs):
    _hash: int = -345383640
    _prefab_name: int = "StructureLogicReader"

    def __getitem__(self, name: str | int | float) -> "_LogicReaders":
        return _LogicReaders(name)


LogicReaders: _LogicReaders = _LogicReaders()


class LogicRocketDownlink(_BaseStructure):
    _hash: int = 876108549
    _prefab_name: int = "StructureLogicRocketDownlink"

    @property
    def Power(self) -> float:
        return _DeviceLogicType(self, _LT.Power)

    @property
    def RequiredPower(self) -> float:
        return _DeviceLogicType(self, _LT.RequiredPower)


class _LogicRocketDownlinks(_BaseStructures):
    _hash: int = 876108549
    _prefab_name: int = "StructureLogicRocketDownlink"

    def __getitem__(self, name: str | int | float) -> "_LogicRocketDownlinks":
        return _LogicRocketDownlinks(name)

    @property
    def Power(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Power)

    @property
    def RequiredPower(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RequiredPower)


LogicRocketDownlinks: _LogicRocketDownlinks = _LogicRocketDownlinks()


class LogicSelect(_BaseStructure, _Error, _Mode, _Power, _SettingR):
    _hash: int = 1822736084
    _prefab_name: int = "StructureLogicSelect"


class _LogicSelects(_BaseStructures, _Errors, _Modes, _Powers, _SettingRs):
    _hash: int = 1822736084
    _prefab_name: int = "StructureLogicSelect"

    def __getitem__(self, name: str | int | float) -> "_LogicSelects":
        return _LogicSelects(name)


LogicSelects: _LogicSelects = _LogicSelects()


class LogicSorter(
    _BaseStructure,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Mode,
    _Power,
):
    _hash: int = 873418029
    _prefab_name: int = "StructureLogicSorter"

    @property
    def StackSize(self) -> float:
        return _DeviceLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def Export2(self) -> _SlotTypeCommon:
        return self.slot2

    @property
    def slot3(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 3)

    @property
    def DataDisk(self) -> _SlotTypeCommon:
        return self.slot3


class _LogicSorters(
    _BaseStructures,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Modes,
    _Powers,
):
    _hash: int = 873418029
    _prefab_name: int = "StructureLogicSorter"

    def __getitem__(self, name: str | int | float) -> "_LogicSorters":
        return _LogicSorters(name)

    @property
    def StackSize(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def Export2(self) -> _SlotTypeCommons:
        return self.slot2

    @property
    def slot3(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 3)

    @property
    def DataDisk(self) -> _SlotTypeCommons:
        return self.slot3


LogicSorters: _LogicSorters = _LogicSorters()


class LogicRocketUplink(_BaseStructure, _Error, _Power):
    _hash: int = 546002924
    _prefab_name: int = "StructureLogicRocketUplink"


class _LogicRocketUplinks(_BaseStructures, _Errors, _Powers):
    _hash: int = 546002924
    _prefab_name: int = "StructureLogicRocketUplink"

    def __getitem__(self, name: str | int | float) -> "_LogicRocketUplinks":
        return _LogicRocketUplinks(name)


LogicRocketUplinks: _LogicRocketUplinks = _LogicRocketUplinks()


class LogicWriter(_BaseStructure, _Error, _Power):
    _hash: int = -1326019434
    _prefab_name: int = "StructureLogicWriter"

    @property
    def ForceWrite(self) -> float:
        return _DeviceLogicType(self, _LT.ForceWrite)

    @ForceWrite.setter
    def ForceWrite(self, value: int | float):
        pass


class _LogicWriters(_BaseStructures, _Errors, _Powers):
    _hash: int = -1326019434
    _prefab_name: int = "StructureLogicWriter"

    def __getitem__(self, name: str | int | float) -> "_LogicWriters":
        return _LogicWriters(name)

    @property
    def ForceWrite(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ForceWrite)

    @ForceWrite.setter
    def ForceWrite(self, value: int | float):
        pass


LogicWriters: _LogicWriters = _LogicWriters()


class LogicWriterSwitch(_BaseStructure, _Activate, _Error, _Power):
    _hash: int = -1321250424
    _prefab_name: int = "StructureLogicWriterSwitch"

    @property
    def ForceWrite(self) -> float:
        return _DeviceLogicType(self, _LT.ForceWrite)

    @ForceWrite.setter
    def ForceWrite(self, value: int | float):
        pass


class _LogicWriterSwitchs(_BaseStructures, _Activates, _Errors, _Powers):
    _hash: int = -1321250424
    _prefab_name: int = "StructureLogicWriterSwitch"

    def __getitem__(self, name: str | int | float) -> "_LogicWriterSwitchs":
        return _LogicWriterSwitchs(name)

    @property
    def ForceWrite(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ForceWrite)

    @ForceWrite.setter
    def ForceWrite(self, value: int | float):
        pass


LogicWriterSwitchs: _LogicWriterSwitchs = _LogicWriterSwitchs()


class ManualFloorHatch(_BaseStructure, _Idle, _Lock, _Open, _SettingW):
    _hash: int = 1435578852
    _prefab_name: int = "StructureManualFloorHatch"


class _ManualFloorHatchs(_BaseStructures, _Idles, _Locks, _Opens, _SettingWs):
    _hash: int = 1435578852
    _prefab_name: int = "StructureManualFloorHatch"

    def __getitem__(self, name: str | int | float) -> "_ManualFloorHatchs":
        return _ManualFloorHatchs(name)


ManualFloorHatchs: _ManualFloorHatchs = _ManualFloorHatchs()


class ManualHatch(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = -1808154199
    _prefab_name: int = "StructureManualHatch"


class _ManualHatchs(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = -1808154199
    _prefab_name: int = "StructureManualHatch"

    def __getitem__(self, name: str | int | float) -> "_ManualHatchs":
        return _ManualHatchs(name)


ManualHatchs: _ManualHatchs = _ManualHatchs()


class LogicMathUnary(_BaseStructure, _Error, _Mode, _Power, _SettingR):
    _hash: int = -1160020195
    _prefab_name: int = "StructureLogicMathUnary"


class _LogicMathUnarys(_BaseStructures, _Errors, _Modes, _Powers, _SettingRs):
    _hash: int = -1160020195
    _prefab_name: int = "StructureLogicMathUnary"

    def __getitem__(self, name: str | int | float) -> "_LogicMathUnarys":
        return _LogicMathUnarys(name)


LogicMathUnarys: _LogicMathUnarys = _LogicMathUnarys()


class PassiveLargeRadiatorGas(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 2066977095
    _prefab_name: int = "StructurePassiveLargeRadiatorGas"


class _PassiveLargeRadiatorGass(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = 2066977095
    _prefab_name: int = "StructurePassiveLargeRadiatorGas"

    def __getitem__(self, name: str | int | float) -> "_PassiveLargeRadiatorGass":
        return _PassiveLargeRadiatorGass(name)


PassiveLargeRadiatorGass: _PassiveLargeRadiatorGass = _PassiveLargeRadiatorGass()


class MediumConvectionRadiator(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -1918215845
    _prefab_name: int = "StructureMediumConvectionRadiator"


class _MediumConvectionRadiators(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = -1918215845
    _prefab_name: int = "StructureMediumConvectionRadiator"

    def __getitem__(self, name: str | int | float) -> "_MediumConvectionRadiators":
        return _MediumConvectionRadiators(name)


MediumConvectionRadiators: _MediumConvectionRadiators = _MediumConvectionRadiators()


class MediumConvectionRadiatorLiquid(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -1169014183
    _prefab_name: int = "StructureMediumConvectionRadiatorLiquid"


class _MediumConvectionRadiatorLiquids(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = -1169014183
    _prefab_name: int = "StructureMediumConvectionRadiatorLiquid"

    def __getitem__(
        self, name: str | int | float
    ) -> "_MediumConvectionRadiatorLiquids":
        return _MediumConvectionRadiatorLiquids(name)


MediumConvectionRadiatorLiquids: _MediumConvectionRadiatorLiquids = (
    _MediumConvectionRadiatorLiquids()
)


class PassiveLargeRadiatorLiquid(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 24786172
    _prefab_name: int = "StructurePassiveLargeRadiatorLiquid"


class _PassiveLargeRadiatorLiquids(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = 24786172
    _prefab_name: int = "StructurePassiveLargeRadiatorLiquid"

    def __getitem__(self, name: str | int | float) -> "_PassiveLargeRadiatorLiquids":
        return _PassiveLargeRadiatorLiquids(name)


PassiveLargeRadiatorLiquids: _PassiveLargeRadiatorLiquids = (
    _PassiveLargeRadiatorLiquids()
)


class MediumHangerDoor(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = -566348148
    _prefab_name: int = "StructureMediumHangerDoor"


class _MediumHangerDoors(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = -566348148
    _prefab_name: int = "StructureMediumHangerDoor"

    def __getitem__(self, name: str | int | float) -> "_MediumHangerDoors":
        return _MediumHangerDoors(name)


MediumHangerDoors: _MediumHangerDoors = _MediumHangerDoors()


class MediumRadiator(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -975966237
    _prefab_name: int = "StructureMediumRadiator"


class _MediumRadiators(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = -975966237
    _prefab_name: int = "StructureMediumRadiator"

    def __getitem__(self, name: str | int | float) -> "_MediumRadiators":
        return _MediumRadiators(name)


MediumRadiators: _MediumRadiators = _MediumRadiators()


class MediumRadiatorLiquid(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -1141760613
    _prefab_name: int = "StructureMediumRadiatorLiquid"


class _MediumRadiatorLiquids(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = -1141760613
    _prefab_name: int = "StructureMediumRadiatorLiquid"

    def __getitem__(self, name: str | int | float) -> "_MediumRadiatorLiquids":
        return _MediumRadiatorLiquids(name)


MediumRadiatorLiquids: _MediumRadiatorLiquids = _MediumRadiatorLiquids()


class SatelliteDish(
    _BaseStructure, _Activate, _Error, _Idle, _Power, _SettingW, _VerticalW
):
    _hash: int = 439026183
    _prefab_name: int = "StructureSatelliteDish"

    @property
    def BestContactFilter(self) -> float:
        return _DeviceLogicType(self, _LT.BestContactFilter)

    @BestContactFilter.setter
    def BestContactFilter(self, value: int | float):
        pass

    @property
    def ContactTypeId(self) -> float:
        return _DeviceLogicType(self, _LT.ContactTypeId)

    @property
    def InterrogationProgress(self) -> float:
        return _DeviceLogicType(self, _LT.InterrogationProgress)

    @property
    def MinimumWattsToContact(self) -> float:
        return _DeviceLogicType(self, _LT.MinimumWattsToContact)

    @property
    def SignalID(self) -> float:
        return _DeviceLogicType(self, _LT.SignalID)

    @property
    def SignalStrength(self) -> float:
        return _DeviceLogicType(self, _LT.SignalStrength)

    @property
    def SizeX(self) -> float:
        return _DeviceLogicType(self, _LT.SizeX)

    @property
    def SizeZ(self) -> float:
        return _DeviceLogicType(self, _LT.SizeZ)

    @property
    def StackSize(self) -> float:
        return _DeviceLogicType(self, _LT.StackSize)

    @property
    def TargetPadIndex(self) -> float:
        return _DeviceLogicType(self, _LT.TargetPadIndex)

    @TargetPadIndex.setter
    def TargetPadIndex(self, value: int | float):
        pass

    @property
    def WattsReachingContact(self) -> float:
        return _DeviceLogicType(self, _LT.WattsReachingContact)


class _SatelliteDishs(
    _BaseStructures, _Activates, _Errors, _Idles, _Powers, _SettingWs, _VerticalWs
):
    _hash: int = 439026183
    _prefab_name: int = "StructureSatelliteDish"

    def __getitem__(self, name: str | int | float) -> "_SatelliteDishs":
        return _SatelliteDishs(name)

    @property
    def BestContactFilter(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.BestContactFilter)

    @BestContactFilter.setter
    def BestContactFilter(self, value: int | float):
        pass

    @property
    def ContactTypeId(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ContactTypeId)

    @property
    def InterrogationProgress(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.InterrogationProgress)

    @property
    def MinimumWattsToContact(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.MinimumWattsToContact)

    @property
    def SignalID(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SignalID)

    @property
    def SignalStrength(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SignalStrength)

    @property
    def SizeX(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SizeX)

    @property
    def SizeZ(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SizeZ)

    @property
    def StackSize(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.StackSize)

    @property
    def TargetPadIndex(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TargetPadIndex)

    @TargetPadIndex.setter
    def TargetPadIndex(self, value: int | float):
        pass

    @property
    def WattsReachingContact(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.WattsReachingContact)


SatelliteDishs: _SatelliteDishs = _SatelliteDishs()


class PowerTransmitterReceiver(
    _BaseStructure, _Charge, _Error, _ModeR, _Power, _VerticalW
):
    _hash: int = 1195820278
    _prefab_name: int = "StructurePowerTransmitterReceiver"

    @property
    def PositionX(self) -> float:
        return _DeviceLogicType(self, _LT.PositionX)

    @property
    def PositionY(self) -> float:
        return _DeviceLogicType(self, _LT.PositionY)

    @property
    def PositionZ(self) -> float:
        return _DeviceLogicType(self, _LT.PositionZ)

    @property
    def PowerActual(self) -> float:
        return _DeviceLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> float:
        return _DeviceLogicType(self, _LT.PowerPotential)


class _PowerTransmitterReceivers(
    _BaseStructures, _Charges, _Errors, _ModeRs, _Powers, _VerticalWs
):
    _hash: int = 1195820278
    _prefab_name: int = "StructurePowerTransmitterReceiver"

    def __getitem__(self, name: str | int | float) -> "_PowerTransmitterReceivers":
        return _PowerTransmitterReceivers(name)

    @property
    def PositionX(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PositionX)

    @property
    def PositionY(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PositionY)

    @property
    def PositionZ(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PositionZ)

    @property
    def PowerActual(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerPotential)


PowerTransmitterReceivers: _PowerTransmitterReceivers = _PowerTransmitterReceivers()


class PowerTransmitter(_BaseStructure, _Charge, _Error, _ModeR, _Power, _VerticalW):
    _hash: int = -65087121
    _prefab_name: int = "StructurePowerTransmitter"

    @property
    def PositionX(self) -> float:
        return _DeviceLogicType(self, _LT.PositionX)

    @property
    def PositionY(self) -> float:
        return _DeviceLogicType(self, _LT.PositionY)

    @property
    def PositionZ(self) -> float:
        return _DeviceLogicType(self, _LT.PositionZ)

    @property
    def PowerActual(self) -> float:
        return _DeviceLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> float:
        return _DeviceLogicType(self, _LT.PowerPotential)


class _PowerTransmitters(
    _BaseStructures, _Charges, _Errors, _ModeRs, _Powers, _VerticalWs
):
    _hash: int = -65087121
    _prefab_name: int = "StructurePowerTransmitter"

    def __getitem__(self, name: str | int | float) -> "_PowerTransmitters":
        return _PowerTransmitters(name)

    @property
    def PositionX(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PositionX)

    @property
    def PositionY(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PositionY)

    @property
    def PositionZ(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PositionZ)

    @property
    def PowerActual(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerPotential)


PowerTransmitters: _PowerTransmitters = _PowerTransmitters()


class MotionSensor(_BaseStructure, _Activate, _On, _Quantity):
    _hash: int = -1713470563
    _prefab_name: int = "StructureMotionSensor"


class _MotionSensors(_BaseStructures, _Activates, _Ons, _Quantitys):
    _hash: int = -1713470563
    _prefab_name: int = "StructureMotionSensor"

    def __getitem__(self, name: str | int | float) -> "_MotionSensors":
        return _MotionSensors(name)


MotionSensors: _MotionSensors = _MotionSensors()


class Nitrolyzer(
    _BaseStructure,
    _Activate,
    _BaseGas,
    _BaseGasInput,
    _BaseGasOutput,
    _Combustion,
    _Error,
    _Hydrogen,
    _Maximum,
    _Mode,
    _Open,
    _PollWater,
    _Power,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = 1898243702
    _prefab_name: int = "StructureNitrolyzer"

    @property
    def CombustionInput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionInput)

    @property
    def CombustionInput2(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionInput2)

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureInput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureInput)

    @property
    def PressureInput2(self) -> float:
        return _DeviceLogicType(self, _LT.PressureInput2)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideInput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideInput2)

    @property
    def RatioLiquidCarbonDioxideInput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidCarbonDioxideInput2)

    @property
    def RatioLiquidNitrogenInput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidNitrogenInput2)

    @property
    def RatioLiquidNitrousOxideInput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidNitrousOxideInput2)

    @property
    def RatioLiquidOxygenInput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidOxygenInput2)

    @property
    def RatioLiquidPollutantInput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidPollutantInput2)

    @property
    def RatioLiquidVolatilesInput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioLiquidVolatilesInput2)

    @property
    def RatioNitrogenInput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenInput2)

    @property
    def RatioNitrousOxideInput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideInput2)

    @property
    def RatioOxygenInput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenInput2)

    @property
    def RatioPollutantInput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantInput2)

    @property
    def RatioSteamInput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioSteamInput2)

    @property
    def RatioVolatilesInput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesInput2)

    @property
    def RatioWaterInput2(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterInput2)

    @property
    def TemperatureInput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureInput)

    @property
    def TemperatureInput2(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureInput2)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesInput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesInput)

    @property
    def TotalMolesInput2(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesInput2)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def ProgrammableChip(self) -> _SlotTypeCommon:
        return self.slot0


class _Nitrolyzers(
    _BaseStructures,
    _Activates,
    _BaseGasInputs,
    _BaseGasOutputs,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _Maximums,
    _Modes,
    _Opens,
    _PollWaters,
    _Powers,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = 1898243702
    _prefab_name: int = "StructureNitrolyzer"

    def __getitem__(self, name: str | int | float) -> "_Nitrolyzers":
        return _Nitrolyzers(name)

    @property
    def CombustionInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionInput)

    @property
    def CombustionInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionInput2)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureInput)

    @property
    def PressureInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureInput2)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideInput2)

    @property
    def RatioLiquidCarbonDioxideInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidCarbonDioxideInput2)

    @property
    def RatioLiquidNitrogenInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidNitrogenInput2)

    @property
    def RatioLiquidNitrousOxideInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidNitrousOxideInput2)

    @property
    def RatioLiquidOxygenInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidOxygenInput2)

    @property
    def RatioLiquidPollutantInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidPollutantInput2)

    @property
    def RatioLiquidVolatilesInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioLiquidVolatilesInput2)

    @property
    def RatioNitrogenInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenInput2)

    @property
    def RatioNitrousOxideInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideInput2)

    @property
    def RatioOxygenInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenInput2)

    @property
    def RatioPollutantInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantInput2)

    @property
    def RatioSteamInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioSteamInput2)

    @property
    def RatioVolatilesInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesInput2)

    @property
    def RatioWaterInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterInput2)

    @property
    def TemperatureInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureInput)

    @property
    def TemperatureInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureInput2)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesInput)

    @property
    def TotalMolesInput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesInput2)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def ProgrammableChip(self) -> _SlotTypeCommons:
        return self.slot0


Nitrolyzers: _Nitrolyzers = _Nitrolyzers()


class HorizontalAutoMiner(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Mode,
    _Open,
    _Power,
):
    _hash: int = 1070427573
    _prefab_name: int = "StructureHorizontalAutoMiner"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _HorizontalAutoMiners(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Modes,
    _Opens,
    _Powers,
):
    _hash: int = 1070427573
    _prefab_name: int = "StructureHorizontalAutoMiner"

    def __getitem__(self, name: str | int | float) -> "_HorizontalAutoMiners":
        return _HorizontalAutoMiners(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


HorizontalAutoMiners: _HorizontalAutoMiners = _HorizontalAutoMiners()


class OccupancySensor(_BaseStructure, _Quantity):
    _hash: int = 322782515
    _prefab_name: int = "StructureOccupancySensor"

    @property
    def Activate(self) -> float:
        return _DeviceLogicType(self, _LT.Activate)


class _OccupancySensors(_BaseStructures, _Quantitys):
    _hash: int = 322782515
    _prefab_name: int = "StructureOccupancySensor"

    def __getitem__(self, name: str | int | float) -> "_OccupancySensors":
        return _OccupancySensors(name)

    @property
    def Activate(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Activate)


OccupancySensors: _OccupancySensors = _OccupancySensors()


class PipeOneWayValveLever(_BaseStructure, _Maximum, _On, _Ratio, _SettingW):
    _hash: int = 1289581593
    _prefab_name: int = "StructurePipeOneWayValveLever"


class _PipeOneWayValveLevers(_BaseStructures, _Maximums, _Ons, _Ratios, _SettingWs):
    _hash: int = 1289581593
    _prefab_name: int = "StructurePipeOneWayValveLever"

    def __getitem__(self, name: str | int | float) -> "_PipeOneWayValveLevers":
        return _PipeOneWayValveLevers(name)


PipeOneWayValveLevers: _PipeOneWayValveLevers = _PipeOneWayValveLevers()


class PipeLiquidOneWayValveLever(_BaseStructure, _Maximum, _On, _Ratio, _SettingW):
    _hash: int = -523832822
    _prefab_name: int = "StructurePipeLiquidOneWayValveLever"


class _PipeLiquidOneWayValveLevers(
    _BaseStructures, _Maximums, _Ons, _Ratios, _SettingWs
):
    _hash: int = -523832822
    _prefab_name: int = "StructurePipeLiquidOneWayValveLever"

    def __getitem__(self, name: str | int | float) -> "_PipeLiquidOneWayValveLevers":
        return _PipeLiquidOneWayValveLevers(name)


PipeLiquidOneWayValveLevers: _PipeLiquidOneWayValveLevers = (
    _PipeLiquidOneWayValveLevers()
)


class OverheadShortCornerLocker(_BaseStructure, _Lock, _Open):
    _hash: int = -1794932560
    _prefab_name: int = "StructureOverheadShortCornerLocker"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)


class _OverheadShortCornerLockers(_BaseStructures, _Locks, _Opens):
    _hash: int = -1794932560
    _prefab_name: int = "StructureOverheadShortCornerLocker"

    def __getitem__(self, name: str | int | float) -> "_OverheadShortCornerLockers":
        return _OverheadShortCornerLockers(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)


OverheadShortCornerLockers: _OverheadShortCornerLockers = _OverheadShortCornerLockers()


class OverheadShortLocker(_BaseStructure, _Lock, _Open):
    _hash: int = 1468249454
    _prefab_name: int = "StructureOverheadShortLocker"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def slot3(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 3)

    @property
    def slot4(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 4)

    @property
    def slot5(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 5)

    @property
    def slot6(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 6)

    @property
    def slot7(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 7)

    @property
    def slot8(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 8)

    @property
    def slot9(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 9)


class _OverheadShortLockers(_BaseStructures, _Locks, _Opens):
    _hash: int = 1468249454
    _prefab_name: int = "StructureOverheadShortLocker"

    def __getitem__(self, name: str | int | float) -> "_OverheadShortLockers":
        return _OverheadShortLockers(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def slot3(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 3)

    @property
    def slot4(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 4)

    @property
    def slot5(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 5)

    @property
    def slot6(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 6)

    @property
    def slot7(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 7)

    @property
    def slot8(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 8)

    @property
    def slot9(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 9)


OverheadShortLockers: _OverheadShortLockers = _OverheadShortLockers()


class LogicPidController(_BaseStructure, _Error, _Power, _SettingR):
    _hash: int = -1905534007
    _prefab_name: int = "StructureLogicPidController"

    @property
    def DerivativeGain(self) -> float:
        return _DeviceLogicType(self, _LT.DerivativeGain)

    @DerivativeGain.setter
    def DerivativeGain(self, value: int | float):
        pass

    @property
    def IntegralGain(self) -> float:
        return _DeviceLogicType(self, _LT.IntegralGain)

    @IntegralGain.setter
    def IntegralGain(self, value: int | float):
        pass

    @property
    def Maximum(self) -> float:
        return _DeviceLogicType(self, _LT.Maximum)

    @Maximum.setter
    def Maximum(self, value: int | float):
        pass

    @property
    def Minimum(self) -> float:
        return _DeviceLogicType(self, _LT.Minimum)

    @Minimum.setter
    def Minimum(self, value: int | float):
        pass

    @property
    def ProportionalGain(self) -> float:
        return _DeviceLogicType(self, _LT.ProportionalGain)

    @ProportionalGain.setter
    def ProportionalGain(self, value: int | float):
        pass

    @property
    def Reset(self) -> float:
        return _DeviceLogicType(self, _LT.Reset)

    @Reset.setter
    def Reset(self, value: int | float):
        pass

    @property
    def Setpoint(self) -> float:
        return _DeviceLogicType(self, _LT.Setpoint)

    @Setpoint.setter
    def Setpoint(self, value: int | float):
        pass


class _LogicPidControllers(_BaseStructures, _Errors, _Powers, _SettingRs):
    _hash: int = -1905534007
    _prefab_name: int = "StructureLogicPidController"

    def __getitem__(self, name: str | int | float) -> "_LogicPidControllers":
        return _LogicPidControllers(name)

    @property
    def DerivativeGain(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.DerivativeGain)

    @DerivativeGain.setter
    def DerivativeGain(self, value: int | float):
        pass

    @property
    def IntegralGain(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.IntegralGain)

    @IntegralGain.setter
    def IntegralGain(self, value: int | float):
        pass

    @property
    def Maximum(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Maximum)

    @Maximum.setter
    def Maximum(self, value: int | float):
        pass

    @property
    def Minimum(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Minimum)

    @Minimum.setter
    def Minimum(self, value: int | float):
        pass

    @property
    def ProportionalGain(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ProportionalGain)

    @ProportionalGain.setter
    def ProportionalGain(self, value: int | float):
        pass

    @property
    def Reset(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Reset)

    @Reset.setter
    def Reset(self, value: int | float):
        pass

    @property
    def Setpoint(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Setpoint)

    @Setpoint.setter
    def Setpoint(self, value: int | float):
        pass


LogicPidControllers: _LogicPidControllers = _LogicPidControllers()


class PipeAnalysizer(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Error,
    _Hydrogen,
    _Lock,
    _PollWater,
    _Power,
    _Temperature,
    _Volume,
):
    _hash: int = 435685051
    _prefab_name: int = "StructurePipeAnalysizer"

    @property
    def NetworkFault(self) -> float:
        return _DeviceLogicType(self, _LT.NetworkFault)


class _PipeAnalysizers(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _Locks,
    _PollWaters,
    _Powers,
    _Temperatures,
    _Volumes,
):
    _hash: int = 435685051
    _prefab_name: int = "StructurePipeAnalysizer"

    def __getitem__(self, name: str | int | float) -> "_PipeAnalysizers":
        return _PipeAnalysizers(name)

    @property
    def NetworkFault(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.NetworkFault)


PipeAnalysizers: _PipeAnalysizers = _PipeAnalysizers()


class PipeHeater(_BaseStructure, _Error, _Lock, _Power):
    _hash: int = -419758574
    _prefab_name: int = "StructurePipeHeater"


class _PipeHeaters(_BaseStructures, _Errors, _Locks, _Powers):
    _hash: int = -419758574
    _prefab_name: int = "StructurePipeHeater"

    def __getitem__(self, name: str | int | float) -> "_PipeHeaters":
        return _PipeHeaters(name)


PipeHeaters: _PipeHeaters = _PipeHeaters()


class LiquidPipeHeater(_BaseStructure, _Error, _Lock, _Power):
    _hash: int = -287495560
    _prefab_name: int = "StructureLiquidPipeHeater"


class _LiquidPipeHeaters(_BaseStructures, _Errors, _Locks, _Powers):
    _hash: int = -287495560
    _prefab_name: int = "StructureLiquidPipeHeater"

    def __getitem__(self, name: str | int | float) -> "_LiquidPipeHeaters":
        return _LiquidPipeHeaters(name)


LiquidPipeHeaters: _LiquidPipeHeaters = _LiquidPipeHeaters()


class PipeIgniter(_BaseStructure, _Activate, _Error):
    _hash: int = 1286441942
    _prefab_name: int = "StructurePipeIgniter"

    @property
    def Power(self) -> float:
        return _DeviceLogicType(self, _LT.Power)

    @property
    def RequiredPower(self) -> float:
        return _DeviceLogicType(self, _LT.RequiredPower)


class _PipeIgniters(_BaseStructures, _Activates, _Errors):
    _hash: int = 1286441942
    _prefab_name: int = "StructurePipeIgniter"

    def __getitem__(self, name: str | int | float) -> "_PipeIgniters":
        return _PipeIgniters(name)

    @property
    def Power(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Power)

    @property
    def RequiredPower(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RequiredPower)


PipeIgniters: _PipeIgniters = _PipeIgniters()


class PortablesConnector(_BaseStructure, _Maximum, _Open, _Ratio, _SettingW):
    _hash: int = -899013427
    _prefab_name: int = "StructurePortablesConnector"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def PortableSlot(self) -> _SlotTypeCommon:
        return self.slot0


class _PortablesConnectors(_BaseStructures, _Maximums, _Opens, _Ratios, _SettingWs):
    _hash: int = -899013427
    _prefab_name: int = "StructurePortablesConnector"

    def __getitem__(self, name: str | int | float) -> "_PortablesConnectors":
        return _PortablesConnectors(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def PortableSlot(self) -> _SlotTypeCommons:
        return self.slot0


PortablesConnectors: _PortablesConnectors = _PortablesConnectors()


class PowerConnector(_BaseStructure, _Open):
    _hash: int = -782951720
    _prefab_name: int = "StructurePowerConnector"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Portableslot(self) -> _SlotTypeCommon:
        return self.slot0


class _PowerConnectors(_BaseStructures, _Opens):
    _hash: int = -782951720
    _prefab_name: int = "StructurePowerConnector"

    def __getitem__(self, name: str | int | float) -> "_PowerConnectors":
        return _PowerConnectors(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Portableslot(self) -> _SlotTypeCommons:
        return self.slot0


PowerConnectors: _PowerConnectors = _PowerConnectors()


class PowerTransmitterOmni(_BaseStructure, _Error, _Power):
    _hash: int = -327468845
    _prefab_name: int = "StructurePowerTransmitterOmni"


class _PowerTransmitterOmnis(_BaseStructures, _Errors, _Powers):
    _hash: int = -327468845
    _prefab_name: int = "StructurePowerTransmitterOmni"

    def __getitem__(self, name: str | int | float) -> "_PowerTransmitterOmnis":
        return _PowerTransmitterOmnis(name)


PowerTransmitterOmnis: _PowerTransmitterOmnis = _PowerTransmitterOmnis()


class Bench(_BaseStructure, _Error, _Power):
    _hash: int = -2042448192
    _prefab_name: int = "StructureBench"

    @property
    def slot0(self) -> _SlotTypeAppliance:
        return _SlotTypeAppliance(self, 0)

    @property
    def Appliance1(self) -> _SlotTypeAppliance:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeAppliance:
        return _SlotTypeAppliance(self, 1)

    @property
    def Appliance2(self) -> _SlotTypeAppliance:
        return self.slot1


class _Benchs(_BaseStructures, _Errors, _Powers):
    _hash: int = -2042448192
    _prefab_name: int = "StructureBench"

    def __getitem__(self, name: str | int | float) -> "_Benchs":
        return _Benchs(name)

    @property
    def slot0(self) -> _SlotTypeAppliances:
        return _SlotTypeAppliances(self, 0)

    @property
    def Appliance1(self) -> _SlotTypeAppliances:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeAppliances:
        return _SlotTypeAppliances(self, 1)

    @property
    def Appliance2(self) -> _SlotTypeAppliances:
        return self.slot1


Benchs: _Benchs = _Benchs()


class PoweredVent(_BaseStructure, _Error, _Lock, _Mode, _Power):
    _hash: int = 938836756
    _prefab_name: int = "StructurePoweredVent"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureExternal(self) -> float:
        return _DeviceLogicType(self, _LT.PressureExternal)

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _PoweredVents(_BaseStructures, _Errors, _Locks, _Modes, _Powers):
    _hash: int = 938836756
    _prefab_name: int = "StructurePoweredVent"

    def __getitem__(self, name: str | int | float) -> "_PoweredVents":
        return _PoweredVents(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureExternal(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureExternal)

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


PoweredVents: _PoweredVents = _PoweredVents()


class PoweredVentLarge(_BaseStructure, _Error, _Lock, _Mode, _Power):
    _hash: int = -785498334
    _prefab_name: int = "StructurePoweredVentLarge"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureExternal(self) -> float:
        return _DeviceLogicType(self, _LT.PressureExternal)

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _PoweredVentLarges(_BaseStructures, _Errors, _Locks, _Modes, _Powers):
    _hash: int = -785498334
    _prefab_name: int = "StructurePoweredVentLarge"

    def __getitem__(self, name: str | int | float) -> "_PoweredVentLarges":
        return _PoweredVentLarges(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureExternal(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureExternal)

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


PoweredVentLarges: _PoweredVentLarges = _PoweredVentLarges()


class PressurantValve(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = 23052817
    _prefab_name: int = "StructurePressurantValve"


class _PressurantValves(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 23052817
    _prefab_name: int = "StructurePressurantValve"

    def __getitem__(self, name: str | int | float) -> "_PressurantValves":
        return _PressurantValves(name)


PressurantValves: _PressurantValves = _PressurantValves()


class PressureFedGasEngine(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Error,
    _Hydrogen,
    _PollWater,
    _Power,
    _Temperature,
):
    _hash: int = -624011170
    _prefab_name: int = "StructurePressureFedGasEngine"

    @property
    def PassedMoles(self) -> float:
        return _DeviceLogicType(self, _LT.PassedMoles)

    @property
    def Throttle(self) -> float:
        return _DeviceLogicType(self, _LT.Throttle)

    @Throttle.setter
    def Throttle(self, value: int | float):
        pass


class _PressureFedGasEngines(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _PollWaters,
    _Powers,
    _Temperatures,
):
    _hash: int = -624011170
    _prefab_name: int = "StructurePressureFedGasEngine"

    def __getitem__(self, name: str | int | float) -> "_PressureFedGasEngines":
        return _PressureFedGasEngines(name)

    @property
    def PassedMoles(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PassedMoles)

    @property
    def Throttle(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Throttle)

    @Throttle.setter
    def Throttle(self, value: int | float):
        pass


PressureFedGasEngines: _PressureFedGasEngines = _PressureFedGasEngines()


class PressureFedLiquidEngine(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Error,
    _Hydrogen,
    _Maximum,
    _PollWater,
    _Power,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = 379750958
    _prefab_name: int = "StructurePressureFedLiquidEngine"

    @property
    def PassedMoles(self) -> float:
        return _DeviceLogicType(self, _LT.PassedMoles)

    @property
    def Throttle(self) -> float:
        return _DeviceLogicType(self, _LT.Throttle)

    @Throttle.setter
    def Throttle(self, value: int | float):
        pass


class _PressureFedLiquidEngines(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _Maximums,
    _PollWaters,
    _Powers,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = 379750958
    _prefab_name: int = "StructurePressureFedLiquidEngine"

    def __getitem__(self, name: str | int | float) -> "_PressureFedLiquidEngines":
        return _PressureFedLiquidEngines(name)

    @property
    def PassedMoles(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PassedMoles)

    @property
    def Throttle(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Throttle)

    @Throttle.setter
    def Throttle(self, value: int | float):
        pass


PressureFedLiquidEngines: _PressureFedLiquidEngines = _PressureFedLiquidEngines()


class PressureRegulator(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = 209854039
    _prefab_name: int = "StructurePressureRegulator"


class _PressureRegulators(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 209854039
    _prefab_name: int = "StructurePressureRegulator"

    def __getitem__(self, name: str | int | float) -> "_PressureRegulators":
        return _PressureRegulators(name)


PressureRegulators: _PressureRegulators = _PressureRegulators()


class ProximitySensor(_BaseStructure, _Quantity, _SettingW):
    _hash: int = 568800213
    _prefab_name: int = "StructureProximitySensor"

    @property
    def Activate(self) -> float:
        return _DeviceLogicType(self, _LT.Activate)


class _ProximitySensors(_BaseStructures, _Quantitys, _SettingWs):
    _hash: int = 568800213
    _prefab_name: int = "StructureProximitySensor"

    def __getitem__(self, name: str | int | float) -> "_ProximitySensors":
        return _ProximitySensors(name)

    @property
    def Activate(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Activate)


ProximitySensors: _ProximitySensors = _ProximitySensors()


class GovernedGasEngine(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Error,
    _Hydrogen,
    _PollWater,
    _Power,
    _Temperature,
):
    _hash: int = -214232602
    _prefab_name: int = "StructureGovernedGasEngine"

    @property
    def PassedMoles(self) -> float:
        return _DeviceLogicType(self, _LT.PassedMoles)

    @property
    def Throttle(self) -> float:
        return _DeviceLogicType(self, _LT.Throttle)

    @Throttle.setter
    def Throttle(self, value: int | float):
        pass


class _GovernedGasEngines(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _PollWaters,
    _Powers,
    _Temperatures,
):
    _hash: int = -214232602
    _prefab_name: int = "StructureGovernedGasEngine"

    def __getitem__(self, name: str | int | float) -> "_GovernedGasEngines":
        return _GovernedGasEngines(name)

    @property
    def PassedMoles(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PassedMoles)

    @property
    def Throttle(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Throttle)

    @Throttle.setter
    def Throttle(self, value: int | float):
        pass


GovernedGasEngines: _GovernedGasEngines = _GovernedGasEngines()


class PumpedLiquidEngine(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Error,
    _Hydrogen,
    _Maximum,
    _PollWater,
    _Power,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = -2031440019
    _prefab_name: int = "StructurePumpedLiquidEngine"

    @property
    def PassedMoles(self) -> float:
        return _DeviceLogicType(self, _LT.PassedMoles)

    @property
    def Throttle(self) -> float:
        return _DeviceLogicType(self, _LT.Throttle)

    @Throttle.setter
    def Throttle(self, value: int | float):
        pass


class _PumpedLiquidEngines(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _Maximums,
    _PollWaters,
    _Powers,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = -2031440019
    _prefab_name: int = "StructurePumpedLiquidEngine"

    def __getitem__(self, name: str | int | float) -> "_PumpedLiquidEngines":
        return _PumpedLiquidEngines(name)

    @property
    def PassedMoles(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PassedMoles)

    @property
    def Throttle(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Throttle)

    @Throttle.setter
    def Throttle(self, value: int | float):
        pass


PumpedLiquidEngines: _PumpedLiquidEngines = _PumpedLiquidEngines()


class PurgeValve(_BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = -737232128
    _prefab_name: int = "StructurePurgeValve"


class _PurgeValves(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -737232128
    _prefab_name: int = "StructurePurgeValve"

    def __getitem__(self, name: str | int | float) -> "_PurgeValves":
        return _PurgeValves(name)


PurgeValves: _PurgeValves = _PurgeValves()


class LogicReagentReader(_BaseStructure, _Error, _Power, _SettingR):
    _hash: int = -124308857
    _prefab_name: int = "StructureLogicReagentReader"


class _LogicReagentReaders(_BaseStructures, _Errors, _Powers, _SettingRs):
    _hash: int = -124308857
    _prefab_name: int = "StructureLogicReagentReader"

    def __getitem__(self, name: str | int | float) -> "_LogicReagentReaders":
        return _LogicReagentReaders(name)


LogicReagentReaders: _LogicReagentReaders = _LogicReagentReaders()


class Recycler(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Power,
    _Reagents,
):
    _hash: int = -1633947337
    _prefab_name: int = "StructureRecycler"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _Recyclers(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Powers,
    _Reagentss,
):
    _hash: int = -1633947337
    _prefab_name: int = "StructureRecycler"

    def __getitem__(self, name: str | int | float) -> "_Recyclers":
        return _Recyclers(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


Recyclers: _Recyclers = _Recyclers()


class RefrigeratedVendingMachine(
    _BaseStructure,
    _Activate,
    _BaseGas,
    _ClearMemory,
    _Combustion,
    _Error,
    _ExportCount,
    _Hydrogen,
    _ImportCount,
    _Lock,
    _PollWater,
    _Power,
    _Quantity,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = -1577831321
    _prefab_name: int = "StructureRefrigeratedVendingMachine"

    @property
    def RequestHash(self) -> float:
        return _DeviceLogicType(self, _LT.RequestHash)

    @RequestHash.setter
    def RequestHash(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1

    @property
    def slot10(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 10)

    @property
    def slot100(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 100)

    @property
    def slot101(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 101)

    @property
    def slot11(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 14)

    @property
    def slot15(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 15)

    @property
    def slot16(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 16)

    @property
    def slot17(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 17)

    @property
    def slot18(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 18)

    @property
    def slot19(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 19)

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def slot20(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 20)

    @property
    def slot21(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 21)

    @property
    def slot22(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 22)

    @property
    def slot23(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 23)

    @property
    def slot24(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 24)

    @property
    def slot25(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 25)

    @property
    def slot26(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 26)

    @property
    def slot27(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 27)

    @property
    def slot28(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 28)

    @property
    def slot29(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 29)

    @property
    def slot3(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 3)

    @property
    def slot30(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 30)

    @property
    def slot31(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 31)

    @property
    def slot32(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 32)

    @property
    def slot33(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 33)

    @property
    def slot34(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 34)

    @property
    def slot35(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 35)

    @property
    def slot36(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 36)

    @property
    def slot37(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 37)

    @property
    def slot38(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 38)

    @property
    def slot39(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 39)

    @property
    def slot4(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 4)

    @property
    def slot40(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 40)

    @property
    def slot41(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 41)

    @property
    def slot42(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 42)

    @property
    def slot43(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 43)

    @property
    def slot44(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 44)

    @property
    def slot45(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 45)

    @property
    def slot46(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 46)

    @property
    def slot47(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 47)

    @property
    def slot48(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 48)

    @property
    def slot49(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 49)

    @property
    def slot5(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 5)

    @property
    def slot50(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 50)

    @property
    def slot51(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 51)

    @property
    def slot52(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 52)

    @property
    def slot53(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 53)

    @property
    def slot54(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 54)

    @property
    def slot55(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 55)

    @property
    def slot56(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 56)

    @property
    def slot57(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 57)

    @property
    def slot58(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 58)

    @property
    def slot59(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 59)

    @property
    def slot6(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 6)

    @property
    def slot60(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 60)

    @property
    def slot61(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 61)

    @property
    def slot62(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 62)

    @property
    def slot63(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 63)

    @property
    def slot64(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 64)

    @property
    def slot65(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 65)

    @property
    def slot66(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 66)

    @property
    def slot67(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 67)

    @property
    def slot68(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 68)

    @property
    def slot69(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 69)

    @property
    def slot7(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 7)

    @property
    def slot70(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 70)

    @property
    def slot71(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 71)

    @property
    def slot72(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 72)

    @property
    def slot73(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 73)

    @property
    def slot74(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 74)

    @property
    def slot75(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 75)

    @property
    def slot76(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 76)

    @property
    def slot77(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 77)

    @property
    def slot78(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 78)

    @property
    def slot79(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 79)

    @property
    def slot8(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 8)

    @property
    def slot80(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 80)

    @property
    def slot81(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 81)

    @property
    def slot82(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 82)

    @property
    def slot83(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 83)

    @property
    def slot84(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 84)

    @property
    def slot85(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 85)

    @property
    def slot86(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 86)

    @property
    def slot87(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 87)

    @property
    def slot88(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 88)

    @property
    def slot89(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 89)

    @property
    def slot9(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 9)

    @property
    def slot90(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 90)

    @property
    def slot91(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 91)

    @property
    def slot92(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 92)

    @property
    def slot93(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 93)

    @property
    def slot94(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 94)

    @property
    def slot95(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 95)

    @property
    def slot96(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 96)

    @property
    def slot97(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 97)

    @property
    def slot98(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 98)

    @property
    def slot99(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 99)


class _RefrigeratedVendingMachines(
    _BaseStructures,
    _Activates,
    _BaseGass,
    _ClearMemorys,
    _Combustions,
    _Errors,
    _ExportCounts,
    _Hydrogens,
    _ImportCounts,
    _Locks,
    _PollWaters,
    _Powers,
    _Quantitys,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = -1577831321
    _prefab_name: int = "StructureRefrigeratedVendingMachine"

    def __getitem__(self, name: str | int | float) -> "_RefrigeratedVendingMachines":
        return _RefrigeratedVendingMachines(name)

    @property
    def RequestHash(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RequestHash)

    @RequestHash.setter
    def RequestHash(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1

    @property
    def slot10(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 10)

    @property
    def slot100(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 100)

    @property
    def slot101(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 101)

    @property
    def slot11(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 14)

    @property
    def slot15(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 15)

    @property
    def slot16(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 16)

    @property
    def slot17(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 17)

    @property
    def slot18(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 18)

    @property
    def slot19(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 19)

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def slot20(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 20)

    @property
    def slot21(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 21)

    @property
    def slot22(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 22)

    @property
    def slot23(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 23)

    @property
    def slot24(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 24)

    @property
    def slot25(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 25)

    @property
    def slot26(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 26)

    @property
    def slot27(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 27)

    @property
    def slot28(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 28)

    @property
    def slot29(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 29)

    @property
    def slot3(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 3)

    @property
    def slot30(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 30)

    @property
    def slot31(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 31)

    @property
    def slot32(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 32)

    @property
    def slot33(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 33)

    @property
    def slot34(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 34)

    @property
    def slot35(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 35)

    @property
    def slot36(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 36)

    @property
    def slot37(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 37)

    @property
    def slot38(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 38)

    @property
    def slot39(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 39)

    @property
    def slot4(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 4)

    @property
    def slot40(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 40)

    @property
    def slot41(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 41)

    @property
    def slot42(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 42)

    @property
    def slot43(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 43)

    @property
    def slot44(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 44)

    @property
    def slot45(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 45)

    @property
    def slot46(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 46)

    @property
    def slot47(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 47)

    @property
    def slot48(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 48)

    @property
    def slot49(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 49)

    @property
    def slot5(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 5)

    @property
    def slot50(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 50)

    @property
    def slot51(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 51)

    @property
    def slot52(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 52)

    @property
    def slot53(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 53)

    @property
    def slot54(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 54)

    @property
    def slot55(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 55)

    @property
    def slot56(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 56)

    @property
    def slot57(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 57)

    @property
    def slot58(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 58)

    @property
    def slot59(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 59)

    @property
    def slot6(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 6)

    @property
    def slot60(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 60)

    @property
    def slot61(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 61)

    @property
    def slot62(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 62)

    @property
    def slot63(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 63)

    @property
    def slot64(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 64)

    @property
    def slot65(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 65)

    @property
    def slot66(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 66)

    @property
    def slot67(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 67)

    @property
    def slot68(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 68)

    @property
    def slot69(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 69)

    @property
    def slot7(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 7)

    @property
    def slot70(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 70)

    @property
    def slot71(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 71)

    @property
    def slot72(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 72)

    @property
    def slot73(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 73)

    @property
    def slot74(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 74)

    @property
    def slot75(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 75)

    @property
    def slot76(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 76)

    @property
    def slot77(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 77)

    @property
    def slot78(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 78)

    @property
    def slot79(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 79)

    @property
    def slot8(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 8)

    @property
    def slot80(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 80)

    @property
    def slot81(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 81)

    @property
    def slot82(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 82)

    @property
    def slot83(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 83)

    @property
    def slot84(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 84)

    @property
    def slot85(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 85)

    @property
    def slot86(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 86)

    @property
    def slot87(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 87)

    @property
    def slot88(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 88)

    @property
    def slot89(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 89)

    @property
    def slot9(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 9)

    @property
    def slot90(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 90)

    @property
    def slot91(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 91)

    @property
    def slot92(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 92)

    @property
    def slot93(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 93)

    @property
    def slot94(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 94)

    @property
    def slot95(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 95)

    @property
    def slot96(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 96)

    @property
    def slot97(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 97)

    @property
    def slot98(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 98)

    @property
    def slot99(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 99)


RefrigeratedVendingMachines: _RefrigeratedVendingMachines = (
    _RefrigeratedVendingMachines()
)


class RocketAvionics(
    _BaseStructure,
    _BaseGas,
    _Error,
    _Hydrogen,
    _Mode,
    _PollWater,
    _Power,
    _Quantity,
    _Reagents,
):
    _hash: int = 808389066
    _prefab_name: int = "StructureRocketAvionics"

    @property
    def Acceleration(self) -> float:
        return _DeviceLogicType(self, _LT.Acceleration)

    @property
    def Altitude(self) -> float:
        return _DeviceLogicType(self, _LT.Altitude)

    @property
    def Apex(self) -> float:
        return _DeviceLogicType(self, _LT.Apex)

    @property
    def AutoLand(self) -> float:
        return _DeviceLogicType(self, _LT.AutoLand)

    @AutoLand.setter
    def AutoLand(self, value: int | float):
        pass

    @property
    def AutoShutOff(self) -> float:
        return _DeviceLogicType(self, _LT.AutoShutOff)

    @AutoShutOff.setter
    def AutoShutOff(self, value: int | float):
        pass

    @property
    def BurnTimeRemaining(self) -> float:
        return _DeviceLogicType(self, _LT.BurnTimeRemaining)

    @property
    def Chart(self) -> float:
        return _DeviceLogicType(self, _LT.Chart)

    @property
    def ChartedNavPoints(self) -> float:
        return _DeviceLogicType(self, _LT.ChartedNavPoints)

    @property
    def CurrentCode(self) -> float:
        return _DeviceLogicType(self, _LT.CurrentCode)

    @property
    def Density(self) -> float:
        return _DeviceLogicType(self, _LT.Density)

    @property
    def DestinationCode(self) -> float:
        return _DeviceLogicType(self, _LT.DestinationCode)

    @DestinationCode.setter
    def DestinationCode(self, value: int | float):
        pass

    @property
    def Discover(self) -> float:
        return _DeviceLogicType(self, _LT.Discover)

    @property
    def DryMass(self) -> float:
        return _DeviceLogicType(self, _LT.DryMass)

    @property
    def FlightControlRule(self) -> float:
        return _DeviceLogicType(self, _LT.FlightControlRule)

    @property
    def Mass(self) -> float:
        return _DeviceLogicType(self, _LT.Mass)

    @property
    def MinedQuantity(self) -> float:
        return _DeviceLogicType(self, _LT.MinedQuantity)

    @property
    def NavPoints(self) -> float:
        return _DeviceLogicType(self, _LT.NavPoints)

    @property
    def Progress(self) -> float:
        return _DeviceLogicType(self, _LT.Progress)

    @property
    def ReEntryAltitude(self) -> float:
        return _DeviceLogicType(self, _LT.ReEntryAltitude)

    @property
    def Richness(self) -> float:
        return _DeviceLogicType(self, _LT.Richness)

    @property
    def Sites(self) -> float:
        return _DeviceLogicType(self, _LT.Sites)

    @property
    def Size(self) -> float:
        return _DeviceLogicType(self, _LT.Size)

    @property
    def StackSize(self) -> float:
        return _DeviceLogicType(self, _LT.StackSize)

    @property
    def Survey(self) -> float:
        return _DeviceLogicType(self, _LT.Survey)

    @property
    def Temperature(self) -> float:
        return _DeviceLogicType(self, _LT.Temperature)

    @property
    def Thrust(self) -> float:
        return _DeviceLogicType(self, _LT.Thrust)

    @property
    def ThrustToWeight(self) -> float:
        return _DeviceLogicType(self, _LT.ThrustToWeight)

    @property
    def TimeToDestination(self) -> float:
        return _DeviceLogicType(self, _LT.TimeToDestination)

    @property
    def TotalMoles(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMoles)

    @property
    def TotalQuantity(self) -> float:
        return _DeviceLogicType(self, _LT.TotalQuantity)

    @property
    def VelocityRelativeY(self) -> float:
        return _DeviceLogicType(self, _LT.VelocityRelativeY)

    @property
    def Weight(self) -> float:
        return _DeviceLogicType(self, _LT.Weight)


class _RocketAvionicss(
    _BaseStructures,
    _BaseGass,
    _Errors,
    _Hydrogens,
    _Modes,
    _PollWaters,
    _Powers,
    _Quantitys,
    _Reagentss,
):
    _hash: int = 808389066
    _prefab_name: int = "StructureRocketAvionics"

    def __getitem__(self, name: str | int | float) -> "_RocketAvionicss":
        return _RocketAvionicss(name)

    @property
    def Acceleration(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Acceleration)

    @property
    def Altitude(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Altitude)

    @property
    def Apex(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Apex)

    @property
    def AutoLand(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.AutoLand)

    @AutoLand.setter
    def AutoLand(self, value: int | float):
        pass

    @property
    def AutoShutOff(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.AutoShutOff)

    @AutoShutOff.setter
    def AutoShutOff(self, value: int | float):
        pass

    @property
    def BurnTimeRemaining(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.BurnTimeRemaining)

    @property
    def Chart(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Chart)

    @property
    def ChartedNavPoints(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ChartedNavPoints)

    @property
    def CurrentCode(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CurrentCode)

    @property
    def Density(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Density)

    @property
    def DestinationCode(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.DestinationCode)

    @DestinationCode.setter
    def DestinationCode(self, value: int | float):
        pass

    @property
    def Discover(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Discover)

    @property
    def DryMass(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.DryMass)

    @property
    def FlightControlRule(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.FlightControlRule)

    @property
    def Mass(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Mass)

    @property
    def MinedQuantity(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.MinedQuantity)

    @property
    def NavPoints(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.NavPoints)

    @property
    def Progress(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Progress)

    @property
    def ReEntryAltitude(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ReEntryAltitude)

    @property
    def Richness(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Richness)

    @property
    def Sites(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Sites)

    @property
    def Size(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Size)

    @property
    def StackSize(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.StackSize)

    @property
    def Survey(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Survey)

    @property
    def Temperature(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Temperature)

    @property
    def Thrust(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Thrust)

    @property
    def ThrustToWeight(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ThrustToWeight)

    @property
    def TimeToDestination(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TimeToDestination)

    @property
    def TotalMoles(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMoles)

    @property
    def TotalQuantity(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalQuantity)

    @property
    def VelocityRelativeY(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.VelocityRelativeY)

    @property
    def Weight(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Weight)


RocketAvionicss: _RocketAvionicss = _RocketAvionicss()


class RocketCelestialTracker(_BaseStructure, _Error, _Power, _Vertical):
    _hash: int = 997453927
    _prefab_name: int = "StructureRocketCelestialTracker"

    @property
    def CelestialHash(self) -> float:
        return _DeviceLogicType(self, _LT.CelestialHash)

    @property
    def Index(self) -> float:
        return _DeviceLogicType(self, _LT.Index)

    @Index.setter
    def Index(self, value: int | float):
        pass

    @property
    def StackSize(self) -> float:
        return _DeviceLogicType(self, _LT.StackSize)


class _RocketCelestialTrackers(_BaseStructures, _Errors, _Powers, _Verticals):
    _hash: int = 997453927
    _prefab_name: int = "StructureRocketCelestialTracker"

    def __getitem__(self, name: str | int | float) -> "_RocketCelestialTrackers":
        return _RocketCelestialTrackers(name)

    @property
    def CelestialHash(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CelestialHash)

    @property
    def Index(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Index)

    @Index.setter
    def Index(self, value: int | float):
        pass

    @property
    def StackSize(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.StackSize)


RocketCelestialTrackers: _RocketCelestialTrackers = _RocketCelestialTrackers()


class RocketCircuitHousing(_BaseStructure, _Error, _Mode, _Power, _SettingW):
    _hash: int = 150135861
    _prefab_name: int = "StructureRocketCircuitHousing"

    @property
    def LineNumber(self) -> float:
        return _DeviceLogicType(self, _LT.LineNumber)

    @LineNumber.setter
    def LineNumber(self, value: int | float):
        pass

    @property
    def StackSize(self) -> float:
        return _DeviceLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeProgrammableChip:
        return _SlotTypeProgrammableChip(self, 0)

    @property
    def ProgrammableChip(self) -> _SlotTypeProgrammableChip:
        return self.slot0


class _RocketCircuitHousings(_BaseStructures, _Errors, _Modes, _Powers, _SettingWs):
    _hash: int = 150135861
    _prefab_name: int = "StructureRocketCircuitHousing"

    def __getitem__(self, name: str | int | float) -> "_RocketCircuitHousings":
        return _RocketCircuitHousings(name)

    @property
    def LineNumber(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.LineNumber)

    @LineNumber.setter
    def LineNumber(self, value: int | float):
        pass

    @property
    def StackSize(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeProgrammableChips:
        return _SlotTypeProgrammableChips(self, 0)

    @property
    def ProgrammableChip(self) -> _SlotTypeProgrammableChips:
        return self.slot0


RocketCircuitHousings: _RocketCircuitHousings = _RocketCircuitHousings()


class RocketEngineTiny(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = 178472613
    _prefab_name: int = "StructureRocketEngineTiny"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _RocketEngineTinys(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 178472613
    _prefab_name: int = "StructureRocketEngineTiny"

    def __getitem__(self, name: str | int | float) -> "_RocketEngineTinys":
        return _RocketEngineTinys(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


RocketEngineTinys: _RocketEngineTinys = _RocketEngineTinys()


class RocketGasCollector(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Lock,
    _PollWater,
    _Power,
    _Temperature,
):
    _hash: int = -1720125735
    _prefab_name: int = "StructureRocketGasCollector"


class _RocketGasCollectors(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Locks,
    _PollWaters,
    _Powers,
    _Temperatures,
):
    _hash: int = -1720125735
    _prefab_name: int = "StructureRocketGasCollector"

    def __getitem__(self, name: str | int | float) -> "_RocketGasCollectors":
        return _RocketGasCollectors(name)


RocketGasCollectors: _RocketGasCollectors = _RocketGasCollectors()


class RocketFiltrationGas(
    _BaseStructure,
    _BaseGasInput,
    _BaseGasOutput,
    _BaseGasOutput2,
    _Error,
    _Lock,
    _Maximum,
    _Mode,
    _Power,
    _Ratio,
    _SettingW,
):
    _hash: int = -1061194321
    _prefab_name: int = "StructureRocketFiltrationGas"

    @property
    def CombustionInput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionInput)

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def CombustionOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput2)

    @property
    def PressureInput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureInput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def PressureOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput2)

    @property
    def TemperatureInput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureInput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TemperatureOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput2)

    @property
    def TotalMolesInput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesInput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)

    @property
    def TotalMolesOutput2(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput2)

    @property
    def slot0(self) -> _SlotTypeFilter:
        return _SlotTypeFilter(self, 0)

    @property
    def GasFilter(self) -> _SlotTypeFilter:
        return self.slot0


class _RocketFiltrationGass(
    _BaseStructures,
    _BaseGasInputs,
    _BaseGasOutput2s,
    _BaseGasOutputs,
    _Errors,
    _Locks,
    _Maximums,
    _Modes,
    _Powers,
    _Ratios,
    _SettingWs,
):
    _hash: int = -1061194321
    _prefab_name: int = "StructureRocketFiltrationGas"

    def __getitem__(self, name: str | int | float) -> "_RocketFiltrationGass":
        return _RocketFiltrationGass(name)

    @property
    def CombustionInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionInput)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def CombustionOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput2)

    @property
    def PressureInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureInput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def PressureOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput2)

    @property
    def TemperatureInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureInput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TemperatureOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput2)

    @property
    def TotalMolesInput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesInput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)

    @property
    def TotalMolesOutput2(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput2)

    @property
    def slot0(self) -> _SlotTypeFilters:
        return _SlotTypeFilters(self, 0)

    @property
    def GasFilter(self) -> _SlotTypeFilters:
        return self.slot0


RocketFiltrationGass: _RocketFiltrationGass = _RocketFiltrationGass()


class RocketManufactory(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Open,
    _Power,
    _Reagents,
    _RecipeHash,
):
    _hash: int = 1781051034
    _prefab_name: int = "StructureRocketManufactory"

    @property
    def CompletionRatio(self) -> float:
        return _DeviceLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> float:
        return _DeviceLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _RocketManufactorys(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Opens,
    _Powers,
    _Reagentss,
    _RecipeHashs,
):
    _hash: int = 1781051034
    _prefab_name: int = "StructureRocketManufactory"

    def __getitem__(self, name: str | int | float) -> "_RocketManufactorys":
        return _RocketManufactorys(name)

    @property
    def CompletionRatio(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


RocketManufactorys: _RocketManufactorys = _RocketManufactorys()


class RocketMiner(
    _BaseStructure,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Power,
    _Quantity,
):
    _hash: int = -2087223687
    _prefab_name: int = "StructureRocketMiner"

    @property
    def DrillCondition(self) -> float:
        return _DeviceLogicType(self, _LT.DrillCondition)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def DrillHeadSlot(self) -> _SlotTypeCommon:
        return self.slot1


class _RocketMiners(
    _BaseStructures,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Powers,
    _Quantitys,
):
    _hash: int = -2087223687
    _prefab_name: int = "StructureRocketMiner"

    def __getitem__(self, name: str | int | float) -> "_RocketMiners":
        return _RocketMiners(name)

    @property
    def DrillCondition(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.DrillCondition)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def DrillHeadSlot(self) -> _SlotTypeCommons:
        return self.slot1


RocketMiners: _RocketMiners = _RocketMiners()


class RocketScanner(_BaseStructure, _Error, _Lock, _Power):
    _hash: int = 2014252591
    _prefab_name: int = "StructureRocketScanner"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def ScannerHeadSlot(self) -> _SlotTypeCommon:
        return self.slot0


class _RocketScanners(_BaseStructures, _Errors, _Locks, _Powers):
    _hash: int = 2014252591
    _prefab_name: int = "StructureRocketScanner"

    def __getitem__(self, name: str | int | float) -> "_RocketScanners":
        return _RocketScanners(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def ScannerHeadSlot(self) -> _SlotTypeCommons:
        return self.slot0


RocketScanners: _RocketScanners = _RocketScanners()


class SDBHopper(_BaseStructure, _ClearMemory, _ImportCount, _Open):
    _hash: int = -1875856925
    _prefab_name: int = "StructureSDBHopper"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0


class _SDBHoppers(_BaseStructures, _ClearMemorys, _ImportCounts, _Opens):
    _hash: int = -1875856925
    _prefab_name: int = "StructureSDBHopper"

    def __getitem__(self, name: str | int | float) -> "_SDBHoppers":
        return _SDBHoppers(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0


SDBHoppers: _SDBHoppers = _SDBHoppers()


class SDBHopperAdvanced(_BaseStructure, _ClearMemory, _ImportCount, _Lock, _Open):
    _hash: int = 467225612
    _prefab_name: int = "StructureSDBHopperAdvanced"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0


class _SDBHopperAdvanceds(
    _BaseStructures, _ClearMemorys, _ImportCounts, _Locks, _Opens
):
    _hash: int = 467225612
    _prefab_name: int = "StructureSDBHopperAdvanced"

    def __getitem__(self, name: str | int | float) -> "_SDBHopperAdvanceds":
        return _SDBHopperAdvanceds(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0


SDBHopperAdvanceds: _SDBHopperAdvanceds = _SDBHopperAdvanceds()


class SDBSilo(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Mode,
    _Open,
    _Power,
    _Quantity,
):
    _hash: int = 1155865682
    _prefab_name: int = "StructureSDBSilo"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _SDBSilos(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Modes,
    _Opens,
    _Powers,
    _Quantitys,
):
    _hash: int = 1155865682
    _prefab_name: int = "StructureSDBSilo"

    def __getitem__(self, name: str | int | float) -> "_SDBSilos":
        return _SDBSilos(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


SDBSilos: _SDBSilos = _SDBSilos()


class SecurityPrinter(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Open,
    _Power,
    _Reagents,
    _RecipeHash,
):
    _hash: int = -641491515
    _prefab_name: int = "StructureSecurityPrinter"

    @property
    def CompletionRatio(self) -> float:
        return _DeviceLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> float:
        return _DeviceLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _SecurityPrinters(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Opens,
    _Powers,
    _Reagentss,
    _RecipeHashs,
):
    _hash: int = -641491515
    _prefab_name: int = "StructureSecurityPrinter"

    def __getitem__(self, name: str | int | float) -> "_SecurityPrinters":
        return _SecurityPrinters(name)

    @property
    def CompletionRatio(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


SecurityPrinters: _SecurityPrinters = _SecurityPrinters()


class ShelfMedium(_BaseStructure, _Open):
    _hash: int = 182006674
    _prefab_name: int = "StructureShelfMedium"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def slot10(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 10)

    @property
    def slot11(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 14)

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def slot3(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 3)

    @property
    def slot4(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 4)

    @property
    def slot5(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 5)

    @property
    def slot6(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 6)

    @property
    def slot7(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 7)

    @property
    def slot8(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 8)

    @property
    def slot9(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 9)


class _ShelfMediums(_BaseStructures, _Opens):
    _hash: int = 182006674
    _prefab_name: int = "StructureShelfMedium"

    def __getitem__(self, name: str | int | float) -> "_ShelfMediums":
        return _ShelfMediums(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def slot10(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 10)

    @property
    def slot11(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 14)

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def slot3(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 3)

    @property
    def slot4(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 4)

    @property
    def slot5(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 5)

    @property
    def slot6(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 6)

    @property
    def slot7(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 7)

    @property
    def slot8(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 8)

    @property
    def slot9(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 9)


ShelfMediums: _ShelfMediums = _ShelfMediums()


class ShortCornerLocker(_BaseStructure, _Lock, _Open):
    _hash: int = 1330754486
    _prefab_name: int = "StructureShortCornerLocker"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)


class _ShortCornerLockers(_BaseStructures, _Locks, _Opens):
    _hash: int = 1330754486
    _prefab_name: int = "StructureShortCornerLocker"

    def __getitem__(self, name: str | int | float) -> "_ShortCornerLockers":
        return _ShortCornerLockers(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)


ShortCornerLockers: _ShortCornerLockers = _ShortCornerLockers()


class ShortLocker(_BaseStructure, _Lock, _Open):
    _hash: int = -554553467
    _prefab_name: int = "StructureShortLocker"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def slot3(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 3)

    @property
    def slot4(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 4)

    @property
    def slot5(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 5)

    @property
    def slot6(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 6)

    @property
    def slot7(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 7)

    @property
    def slot8(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 8)

    @property
    def slot9(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 9)


class _ShortLockers(_BaseStructures, _Locks, _Opens):
    _hash: int = -554553467
    _prefab_name: int = "StructureShortLocker"

    def __getitem__(self, name: str | int | float) -> "_ShortLockers":
        return _ShortLockers(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def slot3(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 3)

    @property
    def slot4(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 4)

    @property
    def slot5(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 5)

    @property
    def slot6(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 6)

    @property
    def slot7(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 7)

    @property
    def slot8(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 8)

    @property
    def slot9(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 9)


ShortLockers: _ShortLockers = _ShortLockers()


class Shower(_BaseStructure, _Activate, _Maximum, _Open, _Ratio, _SettingW):
    _hash: int = -775128944
    _prefab_name: int = "StructureShower"


class _Showers(_BaseStructures, _Activates, _Maximums, _Opens, _Ratios, _SettingWs):
    _hash: int = -775128944
    _prefab_name: int = "StructureShower"

    def __getitem__(self, name: str | int | float) -> "_Showers":
        return _Showers(name)


Showers: _Showers = _Showers()


class ShowerPowered(_BaseStructure, _Error, _Open, _Power):
    _hash: int = -1081797501
    _prefab_name: int = "StructureShowerPowered"


class _ShowerPowereds(_BaseStructures, _Errors, _Opens, _Powers):
    _hash: int = -1081797501
    _prefab_name: int = "StructureShowerPowered"

    def __getitem__(self, name: str | int | float) -> "_ShowerPowereds":
        return _ShowerPowereds(name)


ShowerPowereds: _ShowerPowereds = _ShowerPowereds()


class Sleeper(
    _BaseStructure, _Activate, _Error, _Lock, _Maximum, _Open, _Power, _Ratio, _SettingW
):
    _hash: int = -1467449329
    _prefab_name: int = "StructureSleeper"

    @property
    def EntityState(self) -> float:
        return _DeviceLogicType(self, _LT.EntityState)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Bed(self) -> _SlotTypeCommon:
        return self.slot0


class _Sleepers(
    _BaseStructures,
    _Activates,
    _Errors,
    _Locks,
    _Maximums,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
):
    _hash: int = -1467449329
    _prefab_name: int = "StructureSleeper"

    def __getitem__(self, name: str | int | float) -> "_Sleepers":
        return _Sleepers(name)

    @property
    def EntityState(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.EntityState)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Bed(self) -> _SlotTypeCommons:
        return self.slot0


Sleepers: _Sleepers = _Sleepers()


class SleeperLeft(
    _BaseStructure,
    _Activate,
    _Error,
    _Lock,
    _Maximum,
    _Mode,
    _Open,
    _Power,
    _Ratio,
    _SettingW,
):
    _hash: int = 1213495833
    _prefab_name: int = "StructureSleeperLeft"

    @property
    def EntityState(self) -> float:
        return _DeviceLogicType(self, _LT.EntityState)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Player(self) -> _SlotTypeCommon:
        return self.slot0


class _SleeperLefts(
    _BaseStructures,
    _Activates,
    _Errors,
    _Locks,
    _Maximums,
    _Modes,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
):
    _hash: int = 1213495833
    _prefab_name: int = "StructureSleeperLeft"

    def __getitem__(self, name: str | int | float) -> "_SleeperLefts":
        return _SleeperLefts(name)

    @property
    def EntityState(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.EntityState)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Player(self) -> _SlotTypeCommons:
        return self.slot0


SleeperLefts: _SleeperLefts = _SleeperLefts()


class SleeperRight(
    _BaseStructure,
    _Activate,
    _Error,
    _Lock,
    _Maximum,
    _Mode,
    _Open,
    _Power,
    _Ratio,
    _SettingW,
):
    _hash: int = -1812330717
    _prefab_name: int = "StructureSleeperRight"

    @property
    def EntityState(self) -> float:
        return _DeviceLogicType(self, _LT.EntityState)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Player(self) -> _SlotTypeCommon:
        return self.slot0


class _SleeperRights(
    _BaseStructures,
    _Activates,
    _Errors,
    _Locks,
    _Maximums,
    _Modes,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
):
    _hash: int = -1812330717
    _prefab_name: int = "StructureSleeperRight"

    def __getitem__(self, name: str | int | float) -> "_SleeperRights":
        return _SleeperRights(name)

    @property
    def EntityState(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.EntityState)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Player(self) -> _SlotTypeCommons:
        return self.slot0


SleeperRights: _SleeperRights = _SleeperRights()


class SleeperVertical(
    _BaseStructure,
    _Activate,
    _Error,
    _Lock,
    _Maximum,
    _Mode,
    _Open,
    _Power,
    _Ratio,
    _SettingW,
):
    _hash: int = -1300059018
    _prefab_name: int = "StructureSleeperVertical"

    @property
    def EntityState(self) -> float:
        return _DeviceLogicType(self, _LT.EntityState)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Player(self) -> _SlotTypeCommon:
        return self.slot0


class _SleeperVerticals(
    _BaseStructures,
    _Activates,
    _Errors,
    _Locks,
    _Maximums,
    _Modes,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
):
    _hash: int = -1300059018
    _prefab_name: int = "StructureSleeperVertical"

    def __getitem__(self, name: str | int | float) -> "_SleeperVerticals":
        return _SleeperVerticals(name)

    @property
    def EntityState(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.EntityState)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Player(self) -> _SlotTypeCommons:
        return self.slot0


SleeperVerticals: _SleeperVerticals = _SleeperVerticals()


class LogicSlotReader(_BaseStructure, _Error, _Power, _SettingR):
    _hash: int = -767867194
    _prefab_name: int = "StructureLogicSlotReader"


class _LogicSlotReaders(_BaseStructures, _Errors, _Powers, _SettingRs):
    _hash: int = -767867194
    _prefab_name: int = "StructureLogicSlotReader"

    def __getitem__(self, name: str | int | float) -> "_LogicSlotReaders":
        return _LogicSlotReaders(name)


LogicSlotReaders: _LogicSlotReaders = _LogicSlotReaders()


class SmallDirectHeatExchangeGastoGas(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 1310303582
    _prefab_name: int = "StructureSmallDirectHeatExchangeGastoGas"


class _SmallDirectHeatExchangeGastoGass(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = 1310303582
    _prefab_name: int = "StructureSmallDirectHeatExchangeGastoGas"

    def __getitem__(
        self, name: str | int | float
    ) -> "_SmallDirectHeatExchangeGastoGass":
        return _SmallDirectHeatExchangeGastoGass(name)


SmallDirectHeatExchangeGastoGass: _SmallDirectHeatExchangeGastoGass = (
    _SmallDirectHeatExchangeGastoGass()
)


class SmallDirectHeatExchangeLiquidtoGas(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 1825212016
    _prefab_name: int = "StructureSmallDirectHeatExchangeLiquidtoGas"


class _SmallDirectHeatExchangeLiquidtoGass(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = 1825212016
    _prefab_name: int = "StructureSmallDirectHeatExchangeLiquidtoGas"

    def __getitem__(
        self, name: str | int | float
    ) -> "_SmallDirectHeatExchangeLiquidtoGass":
        return _SmallDirectHeatExchangeLiquidtoGass(name)


SmallDirectHeatExchangeLiquidtoGass: _SmallDirectHeatExchangeLiquidtoGass = (
    _SmallDirectHeatExchangeLiquidtoGass()
)


class SmallDirectHeatExchangeLiquidtoLiquid(
    _BaseStructure, _Maximum, _Ratio, _SettingW
):
    _hash: int = -507770416
    _prefab_name: int = "StructureSmallDirectHeatExchangeLiquidtoLiquid"


class _SmallDirectHeatExchangeLiquidtoLiquids(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = -507770416
    _prefab_name: int = "StructureSmallDirectHeatExchangeLiquidtoLiquid"

    def __getitem__(
        self, name: str | int | float
    ) -> "_SmallDirectHeatExchangeLiquidtoLiquids":
        return _SmallDirectHeatExchangeLiquidtoLiquids(name)


SmallDirectHeatExchangeLiquidtoLiquids: _SmallDirectHeatExchangeLiquidtoLiquids = (
    _SmallDirectHeatExchangeLiquidtoLiquids()
)


class AirlockGate(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = 1736080881
    _prefab_name: int = "StructureAirlockGate"


class _AirlockGates(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = 1736080881
    _prefab_name: int = "StructureAirlockGate"

    def __getitem__(self, name: str | int | float) -> "_AirlockGates":
        return _AirlockGates(name)


AirlockGates: _AirlockGates = _AirlockGates()


class SmallSatelliteDish(
    _BaseStructure, _Activate, _Error, _Idle, _Power, _SettingW, _VerticalW
):
    _hash: int = -2138748650
    _prefab_name: int = "StructureSmallSatelliteDish"

    @property
    def BestContactFilter(self) -> float:
        return _DeviceLogicType(self, _LT.BestContactFilter)

    @BestContactFilter.setter
    def BestContactFilter(self, value: int | float):
        pass

    @property
    def ContactTypeId(self) -> float:
        return _DeviceLogicType(self, _LT.ContactTypeId)

    @property
    def InterrogationProgress(self) -> float:
        return _DeviceLogicType(self, _LT.InterrogationProgress)

    @property
    def MinimumWattsToContact(self) -> float:
        return _DeviceLogicType(self, _LT.MinimumWattsToContact)

    @property
    def SignalID(self) -> float:
        return _DeviceLogicType(self, _LT.SignalID)

    @property
    def SignalStrength(self) -> float:
        return _DeviceLogicType(self, _LT.SignalStrength)

    @property
    def SizeX(self) -> float:
        return _DeviceLogicType(self, _LT.SizeX)

    @property
    def SizeZ(self) -> float:
        return _DeviceLogicType(self, _LT.SizeZ)

    @property
    def TargetPadIndex(self) -> float:
        return _DeviceLogicType(self, _LT.TargetPadIndex)

    @TargetPadIndex.setter
    def TargetPadIndex(self, value: int | float):
        pass

    @property
    def WattsReachingContact(self) -> float:
        return _DeviceLogicType(self, _LT.WattsReachingContact)


class _SmallSatelliteDishs(
    _BaseStructures, _Activates, _Errors, _Idles, _Powers, _SettingWs, _VerticalWs
):
    _hash: int = -2138748650
    _prefab_name: int = "StructureSmallSatelliteDish"

    def __getitem__(self, name: str | int | float) -> "_SmallSatelliteDishs":
        return _SmallSatelliteDishs(name)

    @property
    def BestContactFilter(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.BestContactFilter)

    @BestContactFilter.setter
    def BestContactFilter(self, value: int | float):
        pass

    @property
    def ContactTypeId(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.ContactTypeId)

    @property
    def InterrogationProgress(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.InterrogationProgress)

    @property
    def MinimumWattsToContact(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.MinimumWattsToContact)

    @property
    def SignalID(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SignalID)

    @property
    def SignalStrength(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SignalStrength)

    @property
    def SizeX(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SizeX)

    @property
    def SizeZ(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SizeZ)

    @property
    def TargetPadIndex(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TargetPadIndex)

    @TargetPadIndex.setter
    def TargetPadIndex(self, value: int | float):
        pass

    @property
    def WattsReachingContact(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.WattsReachingContact)


SmallSatelliteDishs: _SmallSatelliteDishs = _SmallSatelliteDishs()


class TankSmall(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _Open,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = 1013514688
    _prefab_name: int = "StructureTankSmall"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _TankSmalls(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _Opens,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = 1013514688
    _prefab_name: int = "StructureTankSmall"

    def __getitem__(self, name: str | int | float) -> "_TankSmalls":
        return _TankSmalls(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


TankSmalls: _TankSmalls = _TankSmalls()


class TankSmallAir(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _Open,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = 955744474
    _prefab_name: int = "StructureTankSmallAir"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _TankSmallAirs(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _Opens,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = 955744474
    _prefab_name: int = "StructureTankSmallAir"

    def __getitem__(self, name: str | int | float) -> "_TankSmallAirs":
        return _TankSmallAirs(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


TankSmallAirs: _TankSmallAirs = _TankSmallAirs()


class TankSmallFuel(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _Open,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = 2102454415
    _prefab_name: int = "StructureTankSmallFuel"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _TankSmallFuels(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _Opens,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = 2102454415
    _prefab_name: int = "StructureTankSmallFuel"

    def __getitem__(self, name: str | int | float) -> "_TankSmallFuels":
        return _TankSmallFuels(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


TankSmallFuels: _TankSmallFuels = _TankSmallFuels()


class SolarPanel(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = -2045627372
    _prefab_name: int = "StructureSolarPanel"


class _SolarPanels(_BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs):
    _hash: int = -2045627372
    _prefab_name: int = "StructureSolarPanel"

    def __getitem__(self, name: str | int | float) -> "_SolarPanels":
        return _SolarPanels(name)


SolarPanels: _SolarPanels = _SolarPanels()


class SolarPanel45(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = -1554349863
    _prefab_name: int = "StructureSolarPanel45"


class _SolarPanel45s(_BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs):
    _hash: int = -1554349863
    _prefab_name: int = "StructureSolarPanel45"

    def __getitem__(self, name: str | int | float) -> "_SolarPanel45s":
        return _SolarPanel45s(name)


SolarPanel45s: _SolarPanel45s = _SolarPanel45s()


class SolarPanelDual(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = -539224550
    _prefab_name: int = "StructureSolarPanelDual"


class _SolarPanelDuals(_BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs):
    _hash: int = -539224550
    _prefab_name: int = "StructureSolarPanelDual"

    def __getitem__(self, name: str | int | float) -> "_SolarPanelDuals":
        return _SolarPanelDuals(name)


SolarPanelDuals: _SolarPanelDuals = _SolarPanelDuals()


class SolarPanelFlat(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = 1968102968
    _prefab_name: int = "StructureSolarPanelFlat"


class _SolarPanelFlats(_BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs):
    _hash: int = 1968102968
    _prefab_name: int = "StructureSolarPanelFlat"

    def __getitem__(self, name: str | int | float) -> "_SolarPanelFlats":
        return _SolarPanelFlats(name)


SolarPanelFlats: _SolarPanelFlats = _SolarPanelFlats()


class SolarPanel45Reinforced(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = 930865127
    _prefab_name: int = "StructureSolarPanel45Reinforced"


class _SolarPanel45Reinforceds(
    _BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs
):
    _hash: int = 930865127
    _prefab_name: int = "StructureSolarPanel45Reinforced"

    def __getitem__(self, name: str | int | float) -> "_SolarPanel45Reinforceds":
        return _SolarPanel45Reinforceds(name)


SolarPanel45Reinforceds: _SolarPanel45Reinforceds = _SolarPanel45Reinforceds()


class SolarPanelDualReinforced(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = -1545574413
    _prefab_name: int = "StructureSolarPanelDualReinforced"


class _SolarPanelDualReinforceds(
    _BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs
):
    _hash: int = -1545574413
    _prefab_name: int = "StructureSolarPanelDualReinforced"

    def __getitem__(self, name: str | int | float) -> "_SolarPanelDualReinforceds":
        return _SolarPanelDualReinforceds(name)


SolarPanelDualReinforceds: _SolarPanelDualReinforceds = _SolarPanelDualReinforceds()


class SolarPanelFlatReinforced(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = 1697196770
    _prefab_name: int = "StructureSolarPanelFlatReinforced"


class _SolarPanelFlatReinforceds(
    _BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs
):
    _hash: int = 1697196770
    _prefab_name: int = "StructureSolarPanelFlatReinforced"

    def __getitem__(self, name: str | int | float) -> "_SolarPanelFlatReinforceds":
        return _SolarPanelFlatReinforceds(name)


SolarPanelFlatReinforceds: _SolarPanelFlatReinforceds = _SolarPanelFlatReinforceds()


class SolarPanelReinforced(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = -934345724
    _prefab_name: int = "StructureSolarPanelReinforced"


class _SolarPanelReinforceds(
    _BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs
):
    _hash: int = -934345724
    _prefab_name: int = "StructureSolarPanelReinforced"

    def __getitem__(self, name: str | int | float) -> "_SolarPanelReinforceds":
        return _SolarPanelReinforceds(name)


SolarPanelReinforceds: _SolarPanelReinforceds = _SolarPanelReinforceds()


class Sorter(
    _BaseStructure,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Mode,
    _Power,
):
    _hash: int = -1009150565
    _prefab_name: int = "StructureSorter"

    @property
    def Output(self) -> float:
        return _DeviceLogicType(self, _LT.Output)

    @Output.setter
    def Output(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def Export2(self) -> _SlotTypeCommon:
        return self.slot2

    @property
    def slot3(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 3)

    @property
    def DataDisk(self) -> _SlotTypeCommon:
        return self.slot3


class _Sorters(
    _BaseStructures,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Modes,
    _Powers,
):
    _hash: int = -1009150565
    _prefab_name: int = "StructureSorter"

    def __getitem__(self, name: str | int | float) -> "_Sorters":
        return _Sorters(name)

    @property
    def Output(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Output)

    @Output.setter
    def Output(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def Export2(self) -> _SlotTypeCommons:
        return self.slot2

    @property
    def slot3(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 3)

    @property
    def DataDisk(self) -> _SlotTypeCommons:
        return self.slot3


Sorters: _Sorters = _Sorters()


class StackerReverse(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Mode,
    _Power,
    _SettingW,
):
    _hash: int = 1585641623
    _prefab_name: int = "StructureStackerReverse"

    @property
    def Output(self) -> float:
        return _DeviceLogicType(self, _LT.Output)

    @Output.setter
    def Output(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def Processing(self) -> _SlotTypeCommon:
        return self.slot2


class _StackerReverses(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Modes,
    _Powers,
    _SettingWs,
):
    _hash: int = 1585641623
    _prefab_name: int = "StructureStackerReverse"

    def __getitem__(self, name: str | int | float) -> "_StackerReverses":
        return _StackerReverses(name)

    @property
    def Output(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Output)

    @Output.setter
    def Output(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def Processing(self) -> _SlotTypeCommons:
        return self.slot2


StackerReverses: _StackerReverses = _StackerReverses()


class Stacker(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Mode,
    _Power,
    _SettingW,
):
    _hash: int = -2020231820
    _prefab_name: int = "StructureStacker"

    @property
    def Output(self) -> float:
        return _DeviceLogicType(self, _LT.Output)

    @Output.setter
    def Output(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def Processing(self) -> _SlotTypeCommon:
        return self.slot2


class _Stackers(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Modes,
    _Powers,
    _SettingWs,
):
    _hash: int = -2020231820
    _prefab_name: int = "StructureStacker"

    def __getitem__(self, name: str | int | float) -> "_Stackers":
        return _Stackers(name)

    @property
    def Output(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Output)

    @Output.setter
    def Output(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def Processing(self) -> _SlotTypeCommons:
        return self.slot2


Stackers: _Stackers = _Stackers()


class Battery(_BaseStructure, _Charge, _Error, _Lock, _Maximum, _ModeR, _On, _Ratio):
    _hash: int = -400115994
    _prefab_name: int = "StructureBattery"

    @property
    def Power(self) -> float:
        return _DeviceLogicType(self, _LT.Power)

    @property
    def PowerActual(self) -> float:
        return _DeviceLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> float:
        return _DeviceLogicType(self, _LT.PowerPotential)


class _Batterys(
    _BaseStructures, _Charges, _Errors, _Locks, _Maximums, _ModeRs, _Ons, _Ratios
):
    _hash: int = -400115994
    _prefab_name: int = "StructureBattery"

    def __getitem__(self, name: str | int | float) -> "_Batterys":
        return _Batterys(name)

    @property
    def Power(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Power)

    @property
    def PowerActual(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerPotential)


Batterys: _Batterys = _Batterys()


class BatteryLarge(
    _BaseStructure, _Charge, _Error, _Lock, _Maximum, _ModeR, _On, _Ratio
):
    _hash: int = -1388288459
    _prefab_name: int = "StructureBatteryLarge"

    @property
    def Power(self) -> float:
        return _DeviceLogicType(self, _LT.Power)

    @property
    def PowerActual(self) -> float:
        return _DeviceLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> float:
        return _DeviceLogicType(self, _LT.PowerPotential)


class _BatteryLarges(
    _BaseStructures, _Charges, _Errors, _Locks, _Maximums, _ModeRs, _Ons, _Ratios
):
    _hash: int = -1388288459
    _prefab_name: int = "StructureBatteryLarge"

    def __getitem__(self, name: str | int | float) -> "_BatteryLarges":
        return _BatteryLarges(name)

    @property
    def Power(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Power)

    @property
    def PowerActual(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerActual)

    @property
    def PowerPotential(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerPotential)


BatteryLarges: _BatteryLarges = _BatteryLarges()


class StirlingEngine(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Error,
    _Hydrogen,
    _Maximum,
    _PollWater,
    _Power,
    _Quantity,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = -260316435
    _prefab_name: int = "StructureStirlingEngine"

    @property
    def EnvironmentEfficiency(self) -> float:
        return _DeviceLogicType(self, _LT.EnvironmentEfficiency)

    @property
    def PowerGeneration(self) -> float:
        return _DeviceLogicType(self, _LT.PowerGeneration)

    @property
    def Volume(self) -> float:
        return _DeviceLogicType(self, _LT.Volume)

    @property
    def WorkingGasEfficiency(self) -> float:
        return _DeviceLogicType(self, _LT.WorkingGasEfficiency)

    @property
    def slot0(self) -> _SlotTypeGasCanister:
        return _SlotTypeGasCanister(self, 0)

    @property
    def GasCanister(self) -> _SlotTypeGasCanister:
        return self.slot0


class _StirlingEngines(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _Maximums,
    _PollWaters,
    _Powers,
    _Quantitys,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = -260316435
    _prefab_name: int = "StructureStirlingEngine"

    def __getitem__(self, name: str | int | float) -> "_StirlingEngines":
        return _StirlingEngines(name)

    @property
    def EnvironmentEfficiency(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.EnvironmentEfficiency)

    @property
    def PowerGeneration(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerGeneration)

    @property
    def Volume(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Volume)

    @property
    def WorkingGasEfficiency(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.WorkingGasEfficiency)

    @property
    def slot0(self) -> _SlotTypeGasCanisters:
        return _SlotTypeGasCanisters(self, 0)

    @property
    def GasCanister(self) -> _SlotTypeGasCanisters:
        return self.slot0


StirlingEngines: _StirlingEngines = _StirlingEngines()


class SuitStorage(_BaseStructure, _Error, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = 255034731
    _prefab_name: int = "StructureSuitStorage"

    @property
    def slot0(self) -> _SlotTypeHelmet:
        return _SlotTypeHelmet(self, 0)

    @property
    def Helmet(self) -> _SlotTypeHelmet:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeSuit:
        return _SlotTypeSuit(self, 1)

    @property
    def Suit(self) -> _SlotTypeSuit:
        return self.slot1

    @property
    def slot2(self) -> _SlotTypeBack:
        return _SlotTypeBack(self, 2)

    @property
    def Back(self) -> _SlotTypeBack:
        return self.slot2


class _SuitStorages(_BaseStructures, _Errors, _Maximums, _Powers, _Ratios, _SettingWs):
    _hash: int = 255034731
    _prefab_name: int = "StructureSuitStorage"

    def __getitem__(self, name: str | int | float) -> "_SuitStorages":
        return _SuitStorages(name)

    @property
    def slot0(self) -> _SlotTypeHelmets:
        return _SlotTypeHelmets(self, 0)

    @property
    def Helmet(self) -> _SlotTypeHelmets:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeSuits:
        return _SlotTypeSuits(self, 1)

    @property
    def Suit(self) -> _SlotTypeSuits:
        return self.slot1

    @property
    def slot2(self) -> _SlotTypeBacks:
        return _SlotTypeBacks(self, 2)

    @property
    def Back(self) -> _SlotTypeBacks:
        return self.slot2


SuitStorages: _SuitStorages = _SuitStorages()


class LogicSwitch2(_BaseStructure, _Lock, _Open, _SettingR):
    _hash: int = 321604921
    _prefab_name: int = "StructureLogicSwitch2"


class _LogicSwitch2s(_BaseStructures, _Locks, _Opens, _SettingRs):
    _hash: int = 321604921
    _prefab_name: int = "StructureLogicSwitch2"

    def __getitem__(self, name: str | int | float) -> "_LogicSwitch2s":
        return _LogicSwitch2s(name)


LogicSwitch2s: _LogicSwitch2s = _LogicSwitch2s()


class TankBigInsulated(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _Open,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = 1280378227
    _prefab_name: int = "StructureTankBigInsulated"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _TankBigInsulateds(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _Opens,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = 1280378227
    _prefab_name: int = "StructureTankBigInsulated"

    def __getitem__(self, name: str | int | float) -> "_TankBigInsulateds":
        return _TankBigInsulateds(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


TankBigInsulateds: _TankBigInsulateds = _TankBigInsulateds()


class TankSmallInsulated(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Hydrogen,
    _Maximum,
    _Open,
    _PollWater,
    _Ratio,
    _SettingW,
    _Temperature,
    _Volume,
):
    _hash: int = 272136332
    _prefab_name: int = "StructureTankSmallInsulated"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)


class _TankSmallInsulateds(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Hydrogens,
    _Maximums,
    _Opens,
    _PollWaters,
    _Ratios,
    _SettingWs,
    _Temperatures,
    _Volumes,
):
    _hash: int = 272136332
    _prefab_name: int = "StructureTankSmallInsulated"

    def __getitem__(self, name: str | int | float) -> "_TankSmallInsulateds":
        return _TankSmallInsulateds(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)


TankSmallInsulateds: _TankSmallInsulateds = _TankSmallInsulateds()


class GroundBasedTelescope(
    _BaseStructure, _Activate, _Error, _Lock, _Open, _Power, _VerticalW
):
    _hash: int = -619745681
    _prefab_name: int = "StructureGroundBasedTelescope"

    @property
    def AlignmentError(self) -> float:
        return _DeviceLogicType(self, _LT.AlignmentError)

    @property
    def CelestialHash(self) -> float:
        return _DeviceLogicType(self, _LT.CelestialHash)

    @property
    def CelestialParentHash(self) -> float:
        return _DeviceLogicType(self, _LT.CelestialParentHash)

    @property
    def DistanceAu(self) -> float:
        return _DeviceLogicType(self, _LT.DistanceAu)

    @property
    def DistanceKm(self) -> float:
        return _DeviceLogicType(self, _LT.DistanceKm)

    @property
    def Eccentricity(self) -> float:
        return _DeviceLogicType(self, _LT.Eccentricity)

    @property
    def HorizontalRatio(self) -> float:
        return _DeviceLogicType(self, _LT.HorizontalRatio)

    @HorizontalRatio.setter
    def HorizontalRatio(self, value: int | float):
        pass

    @property
    def Inclination(self) -> float:
        return _DeviceLogicType(self, _LT.Inclination)

    @property
    def OrbitPeriod(self) -> float:
        return _DeviceLogicType(self, _LT.OrbitPeriod)

    @property
    def SemiMajorAxis(self) -> float:
        return _DeviceLogicType(self, _LT.SemiMajorAxis)

    @property
    def TrueAnomaly(self) -> float:
        return _DeviceLogicType(self, _LT.TrueAnomaly)

    @property
    def VerticalRatio(self) -> float:
        return _DeviceLogicType(self, _LT.VerticalRatio)

    @VerticalRatio.setter
    def VerticalRatio(self, value: int | float):
        pass


class _GroundBasedTelescopes(
    _BaseStructures, _Activates, _Errors, _Locks, _Opens, _Powers, _VerticalWs
):
    _hash: int = -619745681
    _prefab_name: int = "StructureGroundBasedTelescope"

    def __getitem__(self, name: str | int | float) -> "_GroundBasedTelescopes":
        return _GroundBasedTelescopes(name)

    @property
    def AlignmentError(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.AlignmentError)

    @property
    def CelestialHash(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CelestialHash)

    @property
    def CelestialParentHash(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CelestialParentHash)

    @property
    def DistanceAu(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.DistanceAu)

    @property
    def DistanceKm(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.DistanceKm)

    @property
    def Eccentricity(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Eccentricity)

    @property
    def HorizontalRatio(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.HorizontalRatio)

    @HorizontalRatio.setter
    def HorizontalRatio(self, value: int | float):
        pass

    @property
    def Inclination(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Inclination)

    @property
    def OrbitPeriod(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.OrbitPeriod)

    @property
    def SemiMajorAxis(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.SemiMajorAxis)

    @property
    def TrueAnomaly(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TrueAnomaly)

    @property
    def VerticalRatio(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.VerticalRatio)

    @VerticalRatio.setter
    def VerticalRatio(self, value: int | float):
        pass


GroundBasedTelescopes: _GroundBasedTelescopes = _GroundBasedTelescopes()


class ToolManufactory(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Open,
    _Power,
    _Reagents,
    _RecipeHash,
):
    _hash: int = -465741100
    _prefab_name: int = "StructureToolManufactory"

    @property
    def CompletionRatio(self) -> float:
        return _DeviceLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> float:
        return _DeviceLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _ToolManufactorys(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Opens,
    _Powers,
    _Reagentss,
    _RecipeHashs,
):
    _hash: int = -465741100
    _prefab_name: int = "StructureToolManufactory"

    def __getitem__(self, name: str | int | float) -> "_ToolManufactorys":
        return _ToolManufactorys(name)

    @property
    def CompletionRatio(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CompletionRatio)

    @property
    def StackSize(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.StackSize)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


ToolManufactorys: _ToolManufactorys = _ToolManufactorys()


class TraderWaypoint(_BaseStructure, _Error, _Power):
    _hash: int = 1570931620
    _prefab_name: int = "StructureTraderWaypoint"


class _TraderWaypoints(_BaseStructures, _Errors, _Powers):
    _hash: int = 1570931620
    _prefab_name: int = "StructureTraderWaypoint"

    def __getitem__(self, name: str | int | float) -> "_TraderWaypoints":
        return _TraderWaypoints(name)


TraderWaypoints: _TraderWaypoints = _TraderWaypoints()


class Transformer(_BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = -1423212473
    _prefab_name: int = "StructureTransformer"


class _Transformers(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -1423212473
    _prefab_name: int = "StructureTransformer"

    def __getitem__(self, name: str | int | float) -> "_Transformers":
        return _Transformers(name)


Transformers: _Transformers = _Transformers()


class TransformerMedium(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = -1065725831
    _prefab_name: int = "StructureTransformerMedium"


class _TransformerMediums(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -1065725831
    _prefab_name: int = "StructureTransformerMedium"

    def __getitem__(self, name: str | int | float) -> "_TransformerMediums":
        return _TransformerMediums(name)


TransformerMediums: _TransformerMediums = _TransformerMediums()


class TransformerSmall(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = -890946730
    _prefab_name: int = "StructureTransformerSmall"


class _TransformerSmalls(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -890946730
    _prefab_name: int = "StructureTransformerSmall"

    def __getitem__(self, name: str | int | float) -> "_TransformerSmalls":
        return _TransformerSmalls(name)


TransformerSmalls: _TransformerSmalls = _TransformerSmalls()


class TransformerSmallReversed(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = 1054059374
    _prefab_name: int = "StructureTransformerSmallReversed"


class _TransformerSmallReverseds(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 1054059374
    _prefab_name: int = "StructureTransformerSmallReversed"

    def __getitem__(self, name: str | int | float) -> "_TransformerSmallReverseds":
        return _TransformerSmallReverseds(name)


TransformerSmallReverseds: _TransformerSmallReverseds = _TransformerSmallReverseds()


class RocketTransformerSmall(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = 518925193
    _prefab_name: int = "StructureRocketTransformerSmall"


class _RocketTransformerSmalls(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 518925193
    _prefab_name: int = "StructureRocketTransformerSmall"

    def __getitem__(self, name: str | int | float) -> "_RocketTransformerSmalls":
        return _RocketTransformerSmalls(name)


RocketTransformerSmalls: _RocketTransformerSmalls = _RocketTransformerSmalls()


class PressurePlateLarge(_BaseStructure, _SettingR):
    _hash: int = -2008706143
    _prefab_name: int = "StructurePressurePlateLarge"


class _PressurePlateLarges(_BaseStructures, _SettingRs):
    _hash: int = -2008706143
    _prefab_name: int = "StructurePressurePlateLarge"

    def __getitem__(self, name: str | int | float) -> "_PressurePlateLarges":
        return _PressurePlateLarges(name)


PressurePlateLarges: _PressurePlateLarges = _PressurePlateLarges()


class PressurePlateMedium(_BaseStructure, _SettingR):
    _hash: int = 1269458680
    _prefab_name: int = "StructurePressurePlateMedium"


class _PressurePlateMediums(_BaseStructures, _SettingRs):
    _hash: int = 1269458680
    _prefab_name: int = "StructurePressurePlateMedium"

    def __getitem__(self, name: str | int | float) -> "_PressurePlateMediums":
        return _PressurePlateMediums(name)


PressurePlateMediums: _PressurePlateMediums = _PressurePlateMediums()


class PressurePlateSmall(_BaseStructure, _SettingR):
    _hash: int = -1536471028
    _prefab_name: int = "StructurePressurePlateSmall"


class _PressurePlateSmalls(_BaseStructures, _SettingRs):
    _hash: int = -1536471028
    _prefab_name: int = "StructurePressurePlateSmall"

    def __getitem__(self, name: str | int | float) -> "_PressurePlateSmalls":
        return _PressurePlateSmalls(name)


PressurePlateSmalls: _PressurePlateSmalls = _PressurePlateSmalls()


class TurboVolumePump(
    _BaseStructure, _Error, _Lock, _Maximum, _Mode, _Power, _Ratio, _SettingW
):
    _hash: int = 1310794736
    _prefab_name: int = "StructureTurboVolumePump"


class _TurboVolumePumps(
    _BaseStructures, _Errors, _Locks, _Maximums, _Modes, _Powers, _Ratios, _SettingWs
):
    _hash: int = 1310794736
    _prefab_name: int = "StructureTurboVolumePump"

    def __getitem__(self, name: str | int | float) -> "_TurboVolumePumps":
        return _TurboVolumePumps(name)


TurboVolumePumps: _TurboVolumePumps = _TurboVolumePumps()


class LiquidTurboVolumePump(
    _BaseStructure, _Error, _Lock, _Maximum, _Mode, _Power, _Ratio, _SettingW
):
    _hash: int = -1051805505
    _prefab_name: int = "StructureLiquidTurboVolumePump"


class _LiquidTurboVolumePumps(
    _BaseStructures, _Errors, _Locks, _Maximums, _Modes, _Powers, _Ratios, _SettingWs
):
    _hash: int = -1051805505
    _prefab_name: int = "StructureLiquidTurboVolumePump"

    def __getitem__(self, name: str | int | float) -> "_LiquidTurboVolumePumps":
        return _LiquidTurboVolumePumps(name)


LiquidTurboVolumePumps: _LiquidTurboVolumePumps = _LiquidTurboVolumePumps()


class ChuteUmbilicalMale(_BaseStructure, _Error, _Lock, _ModeR, _Open, _Power):
    _hash: int = -958884053
    _prefab_name: int = "StructureChuteUmbilicalMale"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def TransportSlot(self) -> _SlotTypeCommon:
        return self.slot0


class _ChuteUmbilicalMales(_BaseStructures, _Errors, _Locks, _ModeRs, _Opens, _Powers):
    _hash: int = -958884053
    _prefab_name: int = "StructureChuteUmbilicalMale"

    def __getitem__(self, name: str | int | float) -> "_ChuteUmbilicalMales":
        return _ChuteUmbilicalMales(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def TransportSlot(self) -> _SlotTypeCommons:
        return self.slot0


ChuteUmbilicalMales: _ChuteUmbilicalMales = _ChuteUmbilicalMales()


class GasUmbilicalMale(
    _BaseStructure, _Error, _Lock, _Maximum, _ModeR, _Open, _Power, _Ratio, _SettingW
):
    _hash: int = -1814939203
    _prefab_name: int = "StructureGasUmbilicalMale"


class _GasUmbilicalMales(
    _BaseStructures,
    _Errors,
    _Locks,
    _Maximums,
    _ModeRs,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
):
    _hash: int = -1814939203
    _prefab_name: int = "StructureGasUmbilicalMale"

    def __getitem__(self, name: str | int | float) -> "_GasUmbilicalMales":
        return _GasUmbilicalMales(name)


GasUmbilicalMales: _GasUmbilicalMales = _GasUmbilicalMales()


class LiquidUmbilicalMale(
    _BaseStructure, _Error, _Lock, _Maximum, _ModeR, _Open, _Power, _Ratio, _SettingW
):
    _hash: int = -1798420047
    _prefab_name: int = "StructureLiquidUmbilicalMale"


class _LiquidUmbilicalMales(
    _BaseStructures,
    _Errors,
    _Locks,
    _Maximums,
    _ModeRs,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
):
    _hash: int = -1798420047
    _prefab_name: int = "StructureLiquidUmbilicalMale"

    def __getitem__(self, name: str | int | float) -> "_LiquidUmbilicalMales":
        return _LiquidUmbilicalMales(name)


LiquidUmbilicalMales: _LiquidUmbilicalMales = _LiquidUmbilicalMales()


class PowerUmbilicalMale(_BaseStructure, _Error, _Lock, _ModeR, _Open, _Power):
    _hash: int = 1529453938
    _prefab_name: int = "StructurePowerUmbilicalMale"


class _PowerUmbilicalMales(_BaseStructures, _Errors, _Locks, _ModeRs, _Opens, _Powers):
    _hash: int = 1529453938
    _prefab_name: int = "StructurePowerUmbilicalMale"

    def __getitem__(self, name: str | int | float) -> "_PowerUmbilicalMales":
        return _PowerUmbilicalMales(name)


PowerUmbilicalMales: _PowerUmbilicalMales = _PowerUmbilicalMales()


class GasUmbilicalFemale(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -1680477930
    _prefab_name: int = "StructureGasUmbilicalFemale"


class _GasUmbilicalFemales(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = -1680477930
    _prefab_name: int = "StructureGasUmbilicalFemale"

    def __getitem__(self, name: str | int | float) -> "_GasUmbilicalFemales":
        return _GasUmbilicalFemales(name)


GasUmbilicalFemales: _GasUmbilicalFemales = _GasUmbilicalFemales()


class LiquidUmbilicalFemale(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 1734723642
    _prefab_name: int = "StructureLiquidUmbilicalFemale"


class _LiquidUmbilicalFemales(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = 1734723642
    _prefab_name: int = "StructureLiquidUmbilicalFemale"

    def __getitem__(self, name: str | int | float) -> "_LiquidUmbilicalFemales":
        return _LiquidUmbilicalFemales(name)


LiquidUmbilicalFemales: _LiquidUmbilicalFemales = _LiquidUmbilicalFemales()


class GasUmbilicalFemaleSide(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -648683847
    _prefab_name: int = "StructureGasUmbilicalFemaleSide"


class _GasUmbilicalFemaleSides(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = -648683847
    _prefab_name: int = "StructureGasUmbilicalFemaleSide"

    def __getitem__(self, name: str | int | float) -> "_GasUmbilicalFemaleSides":
        return _GasUmbilicalFemaleSides(name)


GasUmbilicalFemaleSides: _GasUmbilicalFemaleSides = _GasUmbilicalFemaleSides()


class LiquidUmbilicalFemaleSide(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 1220870319
    _prefab_name: int = "StructureLiquidUmbilicalFemaleSide"


class _LiquidUmbilicalFemaleSides(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = 1220870319
    _prefab_name: int = "StructureLiquidUmbilicalFemaleSide"

    def __getitem__(self, name: str | int | float) -> "_LiquidUmbilicalFemaleSides":
        return _LiquidUmbilicalFemaleSides(name)


LiquidUmbilicalFemaleSides: _LiquidUmbilicalFemaleSides = _LiquidUmbilicalFemaleSides()


class Unloader(
    _BaseStructure,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Mode,
    _Power,
):
    _hash: int = 750118160
    _prefab_name: int = "StructureUnloader"

    @property
    def Output(self) -> float:
        return _DeviceLogicType(self, _LT.Output)

    @Output.setter
    def Output(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1


class _Unloaders(
    _BaseStructures,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Modes,
    _Powers,
):
    _hash: int = 750118160
    _prefab_name: int = "StructureUnloader"

    def __getitem__(self, name: str | int | float) -> "_Unloaders":
        return _Unloaders(name)

    @property
    def Output(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.Output)

    @Output.setter
    def Output(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1


Unloaders: _Unloaders = _Unloaders()


class UprightWindTurbine(_BaseStructure):
    _hash: int = 1622183451
    _prefab_name: int = "StructureUprightWindTurbine"

    @property
    def PowerGeneration(self) -> float:
        return _DeviceLogicType(self, _LT.PowerGeneration)


class _UprightWindTurbines(_BaseStructures):
    _hash: int = 1622183451
    _prefab_name: int = "StructureUprightWindTurbine"

    def __getitem__(self, name: str | int | float) -> "_UprightWindTurbines":
        return _UprightWindTurbines(name)

    @property
    def PowerGeneration(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerGeneration)


UprightWindTurbines: _UprightWindTurbines = _UprightWindTurbines()


class Valve(_BaseStructure, _Maximum, _On, _Ratio, _SettingW):
    _hash: int = -692036078
    _prefab_name: int = "StructureValve"


class _Valves(_BaseStructures, _Maximums, _Ons, _Ratios, _SettingWs):
    _hash: int = -692036078
    _prefab_name: int = "StructureValve"

    def __getitem__(self, name: str | int | float) -> "_Valves":
        return _Valves(name)


Valves: _Valves = _Valves()


class LiquidValve(_BaseStructure, _Maximum, _On, _Ratio, _SettingW):
    _hash: int = 1849974453
    _prefab_name: int = "StructureLiquidValve"


class _LiquidValves(_BaseStructures, _Maximums, _Ons, _Ratios, _SettingWs):
    _hash: int = 1849974453
    _prefab_name: int = "StructureLiquidValve"

    def __getitem__(self, name: str | int | float) -> "_LiquidValves":
        return _LiquidValves(name)


LiquidValves: _LiquidValves = _LiquidValves()


class VendingMachine(
    _BaseStructure,
    _Activate,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Power,
    _Quantity,
    _Ratio,
):
    _hash: int = -443130773
    _prefab_name: int = "StructureVendingMachine"

    @property
    def RequestHash(self) -> float:
        return _DeviceLogicType(self, _LT.RequestHash)

    @RequestHash.setter
    def RequestHash(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 1)

    @property
    def Export(self) -> _SlotTypeCommon:
        return self.slot1

    @property
    def slot10(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 10)

    @property
    def slot100(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 100)

    @property
    def slot101(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 101)

    @property
    def slot11(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 14)

    @property
    def slot15(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 15)

    @property
    def slot16(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 16)

    @property
    def slot17(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 17)

    @property
    def slot18(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 18)

    @property
    def slot19(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 19)

    @property
    def slot2(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 2)

    @property
    def slot20(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 20)

    @property
    def slot21(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 21)

    @property
    def slot22(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 22)

    @property
    def slot23(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 23)

    @property
    def slot24(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 24)

    @property
    def slot25(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 25)

    @property
    def slot26(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 26)

    @property
    def slot27(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 27)

    @property
    def slot28(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 28)

    @property
    def slot29(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 29)

    @property
    def slot3(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 3)

    @property
    def slot30(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 30)

    @property
    def slot31(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 31)

    @property
    def slot32(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 32)

    @property
    def slot33(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 33)

    @property
    def slot34(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 34)

    @property
    def slot35(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 35)

    @property
    def slot36(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 36)

    @property
    def slot37(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 37)

    @property
    def slot38(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 38)

    @property
    def slot39(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 39)

    @property
    def slot4(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 4)

    @property
    def slot40(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 40)

    @property
    def slot41(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 41)

    @property
    def slot42(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 42)

    @property
    def slot43(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 43)

    @property
    def slot44(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 44)

    @property
    def slot45(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 45)

    @property
    def slot46(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 46)

    @property
    def slot47(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 47)

    @property
    def slot48(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 48)

    @property
    def slot49(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 49)

    @property
    def slot5(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 5)

    @property
    def slot50(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 50)

    @property
    def slot51(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 51)

    @property
    def slot52(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 52)

    @property
    def slot53(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 53)

    @property
    def slot54(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 54)

    @property
    def slot55(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 55)

    @property
    def slot56(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 56)

    @property
    def slot57(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 57)

    @property
    def slot58(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 58)

    @property
    def slot59(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 59)

    @property
    def slot6(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 6)

    @property
    def slot60(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 60)

    @property
    def slot61(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 61)

    @property
    def slot62(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 62)

    @property
    def slot63(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 63)

    @property
    def slot64(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 64)

    @property
    def slot65(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 65)

    @property
    def slot66(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 66)

    @property
    def slot67(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 67)

    @property
    def slot68(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 68)

    @property
    def slot69(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 69)

    @property
    def slot7(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 7)

    @property
    def slot70(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 70)

    @property
    def slot71(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 71)

    @property
    def slot72(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 72)

    @property
    def slot73(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 73)

    @property
    def slot74(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 74)

    @property
    def slot75(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 75)

    @property
    def slot76(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 76)

    @property
    def slot77(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 77)

    @property
    def slot78(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 78)

    @property
    def slot79(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 79)

    @property
    def slot8(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 8)

    @property
    def slot80(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 80)

    @property
    def slot81(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 81)

    @property
    def slot82(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 82)

    @property
    def slot83(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 83)

    @property
    def slot84(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 84)

    @property
    def slot85(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 85)

    @property
    def slot86(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 86)

    @property
    def slot87(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 87)

    @property
    def slot88(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 88)

    @property
    def slot89(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 89)

    @property
    def slot9(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 9)

    @property
    def slot90(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 90)

    @property
    def slot91(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 91)

    @property
    def slot92(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 92)

    @property
    def slot93(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 93)

    @property
    def slot94(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 94)

    @property
    def slot95(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 95)

    @property
    def slot96(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 96)

    @property
    def slot97(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 97)

    @property
    def slot98(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 98)

    @property
    def slot99(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 99)


class _VendingMachines(
    _BaseStructures,
    _Activates,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Powers,
    _Quantitys,
    _Ratios,
):
    _hash: int = -443130773
    _prefab_name: int = "StructureVendingMachine"

    def __getitem__(self, name: str | int | float) -> "_VendingMachines":
        return _VendingMachines(name)

    @property
    def RequestHash(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RequestHash)

    @RequestHash.setter
    def RequestHash(self, value: int | float):
        pass

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0

    @property
    def slot1(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 1)

    @property
    def Export(self) -> _SlotTypeCommons:
        return self.slot1

    @property
    def slot10(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 10)

    @property
    def slot100(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 100)

    @property
    def slot101(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 101)

    @property
    def slot11(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 11)

    @property
    def slot12(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 12)

    @property
    def slot13(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 13)

    @property
    def slot14(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 14)

    @property
    def slot15(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 15)

    @property
    def slot16(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 16)

    @property
    def slot17(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 17)

    @property
    def slot18(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 18)

    @property
    def slot19(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 19)

    @property
    def slot2(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 2)

    @property
    def slot20(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 20)

    @property
    def slot21(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 21)

    @property
    def slot22(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 22)

    @property
    def slot23(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 23)

    @property
    def slot24(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 24)

    @property
    def slot25(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 25)

    @property
    def slot26(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 26)

    @property
    def slot27(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 27)

    @property
    def slot28(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 28)

    @property
    def slot29(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 29)

    @property
    def slot3(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 3)

    @property
    def slot30(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 30)

    @property
    def slot31(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 31)

    @property
    def slot32(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 32)

    @property
    def slot33(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 33)

    @property
    def slot34(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 34)

    @property
    def slot35(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 35)

    @property
    def slot36(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 36)

    @property
    def slot37(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 37)

    @property
    def slot38(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 38)

    @property
    def slot39(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 39)

    @property
    def slot4(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 4)

    @property
    def slot40(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 40)

    @property
    def slot41(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 41)

    @property
    def slot42(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 42)

    @property
    def slot43(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 43)

    @property
    def slot44(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 44)

    @property
    def slot45(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 45)

    @property
    def slot46(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 46)

    @property
    def slot47(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 47)

    @property
    def slot48(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 48)

    @property
    def slot49(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 49)

    @property
    def slot5(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 5)

    @property
    def slot50(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 50)

    @property
    def slot51(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 51)

    @property
    def slot52(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 52)

    @property
    def slot53(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 53)

    @property
    def slot54(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 54)

    @property
    def slot55(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 55)

    @property
    def slot56(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 56)

    @property
    def slot57(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 57)

    @property
    def slot58(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 58)

    @property
    def slot59(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 59)

    @property
    def slot6(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 6)

    @property
    def slot60(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 60)

    @property
    def slot61(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 61)

    @property
    def slot62(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 62)

    @property
    def slot63(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 63)

    @property
    def slot64(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 64)

    @property
    def slot65(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 65)

    @property
    def slot66(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 66)

    @property
    def slot67(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 67)

    @property
    def slot68(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 68)

    @property
    def slot69(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 69)

    @property
    def slot7(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 7)

    @property
    def slot70(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 70)

    @property
    def slot71(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 71)

    @property
    def slot72(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 72)

    @property
    def slot73(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 73)

    @property
    def slot74(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 74)

    @property
    def slot75(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 75)

    @property
    def slot76(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 76)

    @property
    def slot77(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 77)

    @property
    def slot78(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 78)

    @property
    def slot79(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 79)

    @property
    def slot8(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 8)

    @property
    def slot80(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 80)

    @property
    def slot81(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 81)

    @property
    def slot82(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 82)

    @property
    def slot83(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 83)

    @property
    def slot84(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 84)

    @property
    def slot85(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 85)

    @property
    def slot86(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 86)

    @property
    def slot87(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 87)

    @property
    def slot88(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 88)

    @property
    def slot89(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 89)

    @property
    def slot9(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 9)

    @property
    def slot90(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 90)

    @property
    def slot91(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 91)

    @property
    def slot92(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 92)

    @property
    def slot93(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 93)

    @property
    def slot94(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 94)

    @property
    def slot95(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 95)

    @property
    def slot96(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 96)

    @property
    def slot97(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 97)

    @property
    def slot98(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 98)

    @property
    def slot99(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 99)


VendingMachines: _VendingMachines = _VendingMachines()


class VolumePump(_BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = -321403609
    _prefab_name: int = "StructureVolumePump"


class _VolumePumps(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -321403609
    _prefab_name: int = "StructureVolumePump"

    def __getitem__(self, name: str | int | float) -> "_VolumePumps":
        return _VolumePumps(name)


VolumePumps: _VolumePumps = _VolumePumps()


class WallCooler(_BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = -739292323
    _prefab_name: int = "StructureWallCooler"

    @property
    def CombustionOutput(self) -> float:
        return _DeviceLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> float:
        return _DeviceLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> float:
        return _DeviceLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def DataDisk(self) -> _SlotTypeCommon:
        return self.slot0


class _WallCoolers(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -739292323
    _prefab_name: int = "StructureWallCooler"

    def __getitem__(self, name: str | int | float) -> "_WallCoolers":
        return _WallCoolers(name)

    @property
    def CombustionOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.CombustionOutput)

    @property
    def PressureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PressureOutput)

    @property
    def RatioCarbonDioxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioCarbonDioxideOutput)

    @property
    def RatioNitrogenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrogenOutput)

    @property
    def RatioNitrousOxideOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioNitrousOxideOutput)

    @property
    def RatioOxygenOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioOxygenOutput)

    @property
    def RatioPollutantOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioPollutantOutput)

    @property
    def RatioVolatilesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioVolatilesOutput)

    @property
    def RatioWaterOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.RatioWaterOutput)

    @property
    def TemperatureOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TemperatureOutput)

    @property
    def TotalMolesOutput(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.TotalMolesOutput)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def DataDisk(self) -> _SlotTypeCommons:
        return self.slot0


WallCoolers: _WallCoolers = _WallCoolers()


class WallHeater(_BaseStructure, _Error, _Lock, _Power):
    _hash: int = 24258244
    _prefab_name: int = "StructureWallHeater"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def DataDisk(self) -> _SlotTypeCommon:
        return self.slot0


class _WallHeaters(_BaseStructures, _Errors, _Locks, _Powers):
    _hash: int = 24258244
    _prefab_name: int = "StructureWallHeater"

    def __getitem__(self, name: str | int | float) -> "_WallHeaters":
        return _WallHeaters(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def DataDisk(self) -> _SlotTypeCommons:
        return self.slot0


WallHeaters: _WallHeaters = _WallHeaters()


class WallLight(_BaseStructure, _Lock, _Power):
    _hash: int = -1860064656
    _prefab_name: int = "StructureWallLight"


class _WallLights(_BaseStructures, _Locks, _Powers):
    _hash: int = -1860064656
    _prefab_name: int = "StructureWallLight"

    def __getitem__(self, name: str | int | float) -> "_WallLights":
        return _WallLights(name)


WallLights: _WallLights = _WallLights()


class WallLightBattery(_BaseStructure, _Lock, _Power):
    _hash: int = -1306415132
    _prefab_name: int = "StructureWallLightBattery"

    @property
    def slot0(self) -> _SlotTypeBattery:
        return _SlotTypeBattery(self, 0)

    @property
    def Battery(self) -> _SlotTypeBattery:
        return self.slot0


class _WallLightBatterys(_BaseStructures, _Locks, _Powers):
    _hash: int = -1306415132
    _prefab_name: int = "StructureWallLightBattery"

    def __getitem__(self, name: str | int | float) -> "_WallLightBatterys":
        return _WallLightBatterys(name)

    @property
    def slot0(self) -> _SlotTypeBatterys:
        return _SlotTypeBatterys(self, 0)

    @property
    def Battery(self) -> _SlotTypeBatterys:
        return self.slot0


WallLightBatterys: _WallLightBatterys = _WallLightBatterys()


class LightLongAngled(_BaseStructure, _Lock, _Power):
    _hash: int = 1847265835
    _prefab_name: int = "StructureLightLongAngled"


class _LightLongAngleds(_BaseStructures, _Locks, _Powers):
    _hash: int = 1847265835
    _prefab_name: int = "StructureLightLongAngled"

    def __getitem__(self, name: str | int | float) -> "_LightLongAngleds":
        return _LightLongAngleds(name)


LightLongAngleds: _LightLongAngleds = _LightLongAngleds()


class LightLongWide(_BaseStructure, _Lock, _Power):
    _hash: int = 555215790
    _prefab_name: int = "StructureLightLongWide"


class _LightLongWides(_BaseStructures, _Locks, _Powers):
    _hash: int = 555215790
    _prefab_name: int = "StructureLightLongWide"

    def __getitem__(self, name: str | int | float) -> "_LightLongWides":
        return _LightLongWides(name)


LightLongWides: _LightLongWides = _LightLongWides()


class LightLong(_BaseStructure, _Lock, _Power):
    _hash: int = 797794350
    _prefab_name: int = "StructureLightLong"


class _LightLongs(_BaseStructures, _Locks, _Powers):
    _hash: int = 797794350
    _prefab_name: int = "StructureLightLong"

    def __getitem__(self, name: str | int | float) -> "_LightLongs":
        return _LightLongs(name)


LightLongs: _LightLongs = _LightLongs()


class WaterPurifier(_BaseStructure, _ClearMemory, _Error, _ImportCount, _Lock, _Power):
    _hash: int = 887383294
    _prefab_name: int = "StructureWaterPurifier"

    @property
    def slot0(self) -> _SlotTypeCommon:
        return _SlotTypeCommon(self, 0)

    @property
    def Import(self) -> _SlotTypeCommon:
        return self.slot0


class _WaterPurifiers(
    _BaseStructures, _ClearMemorys, _Errors, _ImportCounts, _Locks, _Powers
):
    _hash: int = 887383294
    _prefab_name: int = "StructureWaterPurifier"

    def __getitem__(self, name: str | int | float) -> "_WaterPurifiers":
        return _WaterPurifiers(name)

    @property
    def slot0(self) -> _SlotTypeCommons:
        return _SlotTypeCommons(self, 0)

    @property
    def Import(self) -> _SlotTypeCommons:
        return self.slot0


WaterPurifiers: _WaterPurifiers = _WaterPurifiers()


class WaterBottleFillerPowered(_BaseStructure, _Activate, _Error, _Power):
    _hash: int = -756587791
    _prefab_name: int = "StructureWaterBottleFillerPowered"

    @property
    def slot0(self) -> _SlotTypeGasCanister:
        return _SlotTypeGasCanister(self, 0)

    @property
    def slot1(self) -> _SlotTypeGasCanister:
        return _SlotTypeGasCanister(self, 1)


class _WaterBottleFillerPowereds(_BaseStructures, _Activates, _Errors, _Powers):
    _hash: int = -756587791
    _prefab_name: int = "StructureWaterBottleFillerPowered"

    def __getitem__(self, name: str | int | float) -> "_WaterBottleFillerPowereds":
        return _WaterBottleFillerPowereds(name)

    @property
    def slot0(self) -> _SlotTypeGasCanisters:
        return _SlotTypeGasCanisters(self, 0)

    @property
    def slot1(self) -> _SlotTypeGasCanisters:
        return _SlotTypeGasCanisters(self, 1)


WaterBottleFillerPowereds: _WaterBottleFillerPowereds = _WaterBottleFillerPowereds()


class WaterBottleFillerPoweredBottom(_BaseStructure, _Activate, _Error, _Power):
    _hash: int = 1986658780
    _prefab_name: int = "StructureWaterBottleFillerPoweredBottom"

    @property
    def slot0(self) -> _SlotTypeGasCanister:
        return _SlotTypeGasCanister(self, 0)

    @property
    def slot1(self) -> _SlotTypeGasCanister:
        return _SlotTypeGasCanister(self, 1)


class _WaterBottleFillerPoweredBottoms(_BaseStructures, _Activates, _Errors, _Powers):
    _hash: int = 1986658780
    _prefab_name: int = "StructureWaterBottleFillerPoweredBottom"

    def __getitem__(
        self, name: str | int | float
    ) -> "_WaterBottleFillerPoweredBottoms":
        return _WaterBottleFillerPoweredBottoms(name)

    @property
    def slot0(self) -> _SlotTypeGasCanisters:
        return _SlotTypeGasCanisters(self, 0)

    @property
    def slot1(self) -> _SlotTypeGasCanisters:
        return _SlotTypeGasCanisters(self, 1)


WaterBottleFillerPoweredBottoms: _WaterBottleFillerPoweredBottoms = (
    _WaterBottleFillerPoweredBottoms()
)


class WeatherStation(_BaseStructure, _Activate, _Error, _Lock, _ModeR, _Power):
    _hash: int = 1997212478
    _prefab_name: int = "StructureWeatherStation"

    @property
    def NextWeatherEventTime(self) -> float:
        return _DeviceLogicType(self, _LT.NextWeatherEventTime)


class _WeatherStations(_BaseStructures, _Activates, _Errors, _Locks, _ModeRs, _Powers):
    _hash: int = 1997212478
    _prefab_name: int = "StructureWeatherStation"

    def __getitem__(self, name: str | int | float) -> "_WeatherStations":
        return _WeatherStations(name)

    @property
    def NextWeatherEventTime(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.NextWeatherEventTime)


WeatherStations: _WeatherStations = _WeatherStations()


class WindTurbine(_BaseStructure):
    _hash: int = -2082355173
    _prefab_name: int = "StructureWindTurbine"

    @property
    def PowerGeneration(self) -> float:
        return _DeviceLogicType(self, _LT.PowerGeneration)


class _WindTurbines(_BaseStructures):
    _hash: int = -2082355173
    _prefab_name: int = "StructureWindTurbine"

    def __getitem__(self, name: str | int | float) -> "_WindTurbines":
        return _WindTurbines(name)

    @property
    def PowerGeneration(self) -> _DevicesLogicType:
        return _DevicesLogicType(self, _LT.PowerGeneration)


WindTurbines: _WindTurbines = _WindTurbines()
