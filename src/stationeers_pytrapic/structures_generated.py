from stationeers_pytrapic.types import (
    DevicesLogicType,
    DeviceLogicType,
    _BaseStructure,
    _BaseStructures,
)


class _BaseGas:
    @property
    def RatioCarbonDioxide(self) -> float:
        return DeviceLogicType(self, self._id, "RatioCarbonDioxide")

    @property
    def RatioLiquidCarbonDioxide(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidCarbonDioxide")

    @property
    def RatioLiquidNitrogen(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidNitrogen")

    @property
    def RatioLiquidNitrousOxide(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidNitrousOxide")

    @property
    def RatioLiquidOxygen(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidOxygen")

    @property
    def RatioLiquidPollutant(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidPollutant")

    @property
    def RatioLiquidVolatiles(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidVolatiles")

    @property
    def RatioNitrogen(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrogen")

    @property
    def RatioNitrousOxide(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrousOxide")

    @property
    def RatioOxygen(self) -> float:
        return DeviceLogicType(self, self._id, "RatioOxygen")

    @property
    def RatioPollutant(self) -> float:
        return DeviceLogicType(self, self._id, "RatioPollutant")

    @property
    def RatioSteam(self) -> float:
        return DeviceLogicType(self, self._id, "RatioSteam")

    @property
    def RatioVolatiles(self) -> float:
        return DeviceLogicType(self, self._id, "RatioVolatiles")

    @property
    def RatioWater(self) -> float:
        return DeviceLogicType(self, self._id, "RatioWater")


class _BaseGass:
    @property
    def RatioCarbonDioxide(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioCarbonDioxide", self._name_hash)

    @property
    def RatioLiquidCarbonDioxide(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioLiquidCarbonDioxide", self._name_hash)

    @property
    def RatioLiquidNitrogen(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioLiquidNitrogen", self._name_hash)

    @property
    def RatioLiquidNitrousOxide(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioLiquidNitrousOxide", self._name_hash)

    @property
    def RatioLiquidOxygen(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioLiquidOxygen", self._name_hash)

    @property
    def RatioLiquidPollutant(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioLiquidPollutant", self._name_hash)

    @property
    def RatioLiquidVolatiles(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioLiquidVolatiles", self._name_hash)

    @property
    def RatioNitrogen(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrogen", self._name_hash)

    @property
    def RatioNitrousOxide(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrousOxide", self._name_hash)

    @property
    def RatioOxygen(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioOxygen", self._name_hash)

    @property
    def RatioPollutant(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioPollutant", self._name_hash)

    @property
    def RatioSteam(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioSteam", self._name_hash)

    @property
    def RatioVolatiles(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioVolatiles", self._name_hash)

    @property
    def RatioWater(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioWater", self._name_hash)


class _BaseGasInput:
    @property
    def RatioCarbonDioxideInput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioCarbonDioxideInput")

    @property
    def RatioLiquidCarbonDioxideInput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidCarbonDioxideInput")

    @property
    def RatioLiquidNitrogenInput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidNitrogenInput")

    @property
    def RatioLiquidNitrousOxideInput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidNitrousOxideInput")

    @property
    def RatioLiquidOxygenInput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidOxygenInput")

    @property
    def RatioLiquidPollutantInput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidPollutantInput")

    @property
    def RatioLiquidVolatilesInput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidVolatilesInput")

    @property
    def RatioNitrogenInput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrogenInput")

    @property
    def RatioNitrousOxideInput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrousOxideInput")

    @property
    def RatioOxygenInput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioOxygenInput")

    @property
    def RatioPollutantInput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioPollutantInput")

    @property
    def RatioSteamInput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioSteamInput")

    @property
    def RatioVolatilesInput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioVolatilesInput")

    @property
    def RatioWaterInput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioWaterInput")


class _BaseGasInputs:
    @property
    def RatioCarbonDioxideInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioCarbonDioxideInput", self._name_hash)

    @property
    def RatioLiquidCarbonDioxideInput(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidCarbonDioxideInput", self._name_hash
        )

    @property
    def RatioLiquidNitrogenInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioLiquidNitrogenInput", self._name_hash)

    @property
    def RatioLiquidNitrousOxideInput(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidNitrousOxideInput", self._name_hash
        )

    @property
    def RatioLiquidOxygenInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioLiquidOxygenInput", self._name_hash)

    @property
    def RatioLiquidPollutantInput(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidPollutantInput", self._name_hash
        )

    @property
    def RatioLiquidVolatilesInput(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidVolatilesInput", self._name_hash
        )

    @property
    def RatioNitrogenInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrogenInput", self._name_hash)

    @property
    def RatioNitrousOxideInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrousOxideInput", self._name_hash)

    @property
    def RatioOxygenInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioOxygenInput", self._name_hash)

    @property
    def RatioPollutantInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioPollutantInput", self._name_hash)

    @property
    def RatioSteamInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioSteamInput", self._name_hash)

    @property
    def RatioVolatilesInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioVolatilesInput", self._name_hash)

    @property
    def RatioWaterInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioWaterInput", self._name_hash)


class _BaseGasOutput:
    @property
    def RatioCarbonDioxideOutput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioCarbonDioxideOutput")

    @property
    def RatioLiquidCarbonDioxideOutput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidCarbonDioxideOutput")

    @property
    def RatioLiquidNitrogenOutput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidNitrogenOutput")

    @property
    def RatioLiquidNitrousOxideOutput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidNitrousOxideOutput")

    @property
    def RatioLiquidOxygenOutput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidOxygenOutput")

    @property
    def RatioLiquidPollutantOutput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidPollutantOutput")

    @property
    def RatioLiquidVolatilesOutput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidVolatilesOutput")

    @property
    def RatioNitrogenOutput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrogenOutput")

    @property
    def RatioNitrousOxideOutput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrousOxideOutput")

    @property
    def RatioOxygenOutput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioOxygenOutput")

    @property
    def RatioPollutantOutput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioPollutantOutput")

    @property
    def RatioSteamOutput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioSteamOutput")

    @property
    def RatioVolatilesOutput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioVolatilesOutput")

    @property
    def RatioWaterOutput(self) -> float:
        return DeviceLogicType(self, self._id, "RatioWaterOutput")


class _BaseGasOutputs:
    @property
    def RatioCarbonDioxideOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioCarbonDioxideOutput", self._name_hash)

    @property
    def RatioLiquidCarbonDioxideOutput(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidCarbonDioxideOutput", self._name_hash
        )

    @property
    def RatioLiquidNitrogenOutput(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidNitrogenOutput", self._name_hash
        )

    @property
    def RatioLiquidNitrousOxideOutput(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidNitrousOxideOutput", self._name_hash
        )

    @property
    def RatioLiquidOxygenOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioLiquidOxygenOutput", self._name_hash)

    @property
    def RatioLiquidPollutantOutput(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidPollutantOutput", self._name_hash
        )

    @property
    def RatioLiquidVolatilesOutput(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidVolatilesOutput", self._name_hash
        )

    @property
    def RatioNitrogenOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrogenOutput", self._name_hash)

    @property
    def RatioNitrousOxideOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrousOxideOutput", self._name_hash)

    @property
    def RatioOxygenOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioOxygenOutput", self._name_hash)

    @property
    def RatioPollutantOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioPollutantOutput", self._name_hash)

    @property
    def RatioSteamOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioSteamOutput", self._name_hash)

    @property
    def RatioVolatilesOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioVolatilesOutput", self._name_hash)

    @property
    def RatioWaterOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioWaterOutput", self._name_hash)


class _BaseGasOutput2:
    @property
    def RatioCarbonDioxideOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioCarbonDioxideOutput2")

    @property
    def RatioLiquidCarbonDioxideOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidCarbonDioxideOutput2")

    @property
    def RatioLiquidNitrogenOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidNitrogenOutput2")

    @property
    def RatioLiquidNitrousOxideOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidNitrousOxideOutput2")

    @property
    def RatioLiquidOxygenOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidOxygenOutput2")

    @property
    def RatioLiquidPollutantOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidPollutantOutput2")

    @property
    def RatioLiquidVolatilesOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidVolatilesOutput2")

    @property
    def RatioNitrogenOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrogenOutput2")

    @property
    def RatioNitrousOxideOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrousOxideOutput2")

    @property
    def RatioOxygenOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioOxygenOutput2")

    @property
    def RatioPollutantOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioPollutantOutput2")

    @property
    def RatioSteamOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioSteamOutput2")

    @property
    def RatioVolatilesOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioVolatilesOutput2")

    @property
    def RatioWaterOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioWaterOutput2")


class _BaseGasOutput2s:
    @property
    def RatioCarbonDioxideOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioCarbonDioxideOutput2", self._name_hash
        )

    @property
    def RatioLiquidCarbonDioxideOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidCarbonDioxideOutput2", self._name_hash
        )

    @property
    def RatioLiquidNitrogenOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidNitrogenOutput2", self._name_hash
        )

    @property
    def RatioLiquidNitrousOxideOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidNitrousOxideOutput2", self._name_hash
        )

    @property
    def RatioLiquidOxygenOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioLiquidOxygenOutput2", self._name_hash)

    @property
    def RatioLiquidPollutantOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidPollutantOutput2", self._name_hash
        )

    @property
    def RatioLiquidVolatilesOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidVolatilesOutput2", self._name_hash
        )

    @property
    def RatioNitrogenOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrogenOutput2", self._name_hash)

    @property
    def RatioNitrousOxideOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrousOxideOutput2", self._name_hash)

    @property
    def RatioOxygenOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioOxygenOutput2", self._name_hash)

    @property
    def RatioPollutantOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioPollutantOutput2", self._name_hash)

    @property
    def RatioSteamOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioSteamOutput2", self._name_hash)

    @property
    def RatioVolatilesOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioVolatilesOutput2", self._name_hash)

    @property
    def RatioWaterOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioWaterOutput2", self._name_hash)


class _Power:
    @property
    def On(self) -> float:
        return DeviceLogicType(self, self._id, "On")

    @On.setter
    def On(self, value: int | float):
        pass

    @property
    def Power(self) -> float:
        return DeviceLogicType(self, self._id, "Power")

    @property
    def RequiredPower(self) -> float:
        return DeviceLogicType(self, self._id, "RequiredPower")


class _Powers:
    @property
    def On(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "On", self._name_hash)

    @On.setter
    def On(self, value: int | float):
        pass

    @property
    def Power(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Power", self._name_hash)

    @property
    def RequiredPower(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RequiredPower", self._name_hash)


class _On:
    @property
    def On(self) -> float:
        return DeviceLogicType(self, self._id, "On")

    @On.setter
    def On(self, value: int | float):
        pass


class _Ons:
    @property
    def On(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "On", self._name_hash)

    @On.setter
    def On(self, value: int | float):
        pass


class _Activate:
    @property
    def Activate(self) -> float:
        return DeviceLogicType(self, self._id, "Activate")

    @Activate.setter
    def Activate(self, value: int | float):
        pass


class _Activates:
    @property
    def Activate(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Activate", self._name_hash)

    @Activate.setter
    def Activate(self, value: int | float):
        pass


class _Lock:
    @property
    def Lock(self) -> float:
        return DeviceLogicType(self, self._id, "Lock")

    @Lock.setter
    def Lock(self, value: int | float):
        pass


class _Locks:
    @property
    def Lock(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Lock", self._name_hash)

    @Lock.setter
    def Lock(self, value: int | float):
        pass


class _Open:
    @property
    def Open(self) -> float:
        return DeviceLogicType(self, self._id, "Open")

    @Open.setter
    def Open(self, value: int | float):
        pass


class _Opens:
    @property
    def Open(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Open", self._name_hash)

    @Open.setter
    def Open(self, value: int | float):
        pass


class _Error:
    @property
    def Error(self) -> float:
        return DeviceLogicType(self, self._id, "Error")


class _Errors:
    @property
    def Error(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Error", self._name_hash)


class _Ratio:
    @property
    def Ratio(self) -> float:
        return DeviceLogicType(self, self._id, "Ratio")


class _Ratios:
    @property
    def Ratio(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Ratio", self._name_hash)


class _Maximum:
    @property
    def Maximum(self) -> float:
        return DeviceLogicType(self, self._id, "Maximum")


class _Maximums:
    @property
    def Maximum(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Maximum", self._name_hash)


class _SettingW:
    @property
    def Setting(self) -> float:
        return DeviceLogicType(self, self._id, "Setting")

    @Setting.setter
    def Setting(self, value: int | float):
        pass


class _SettingWs:
    @property
    def Setting(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Setting", self._name_hash)

    @Setting.setter
    def Setting(self, value: int | float):
        pass


class _SettingR:
    @property
    def Setting(self) -> float:
        return DeviceLogicType(self, self._id, "Setting")


class _SettingRs:
    @property
    def Setting(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Setting", self._name_hash)


class _Mode:
    @property
    def Mode(self) -> float:
        return DeviceLogicType(self, self._id, "Mode")

    @Mode.setter
    def Mode(self, value: int | float):
        pass


class _Modes:
    @property
    def Mode(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Mode", self._name_hash)

    @Mode.setter
    def Mode(self, value: int | float):
        pass


class _ModeR:
    @property
    def Mode(self) -> float:
        return DeviceLogicType(self, self._id, "Mode")


class _ModeRs:
    @property
    def Mode(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Mode", self._name_hash)


class _Temperature:
    @property
    def Pressure(self) -> float:
        return DeviceLogicType(self, self._id, "Pressure")

    @property
    def Temperature(self) -> float:
        return DeviceLogicType(self, self._id, "Temperature")


class _Temperatures:
    @property
    def Pressure(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Pressure", self._name_hash)

    @property
    def Temperature(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Temperature", self._name_hash)


class _PollWater:
    @property
    def RatioPollutedWater(self) -> float:
        return DeviceLogicType(self, self._id, "RatioPollutedWater")


class _PollWaters:
    @property
    def RatioPollutedWater(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioPollutedWater", self._name_hash)


class _Combustion:
    @property
    def Combustion(self) -> float:
        return DeviceLogicType(self, self._id, "Combustion")

    @property
    def TotalMoles(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMoles")


class _Combustions:
    @property
    def Combustion(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Combustion", self._name_hash)

    @property
    def TotalMoles(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMoles", self._name_hash)


class _Idle:
    @property
    def Idle(self) -> float:
        return DeviceLogicType(self, self._id, "Idle")


class _Idles:
    @property
    def Idle(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Idle", self._name_hash)


class _ImportCount:
    @property
    def ImportCount(self) -> float:
        return DeviceLogicType(self, self._id, "ImportCount")

    @ImportCount.setter
    def ImportCount(self, value: int | float):
        pass


class _ImportCounts:
    @property
    def ImportCount(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ImportCount", self._name_hash)

    @ImportCount.setter
    def ImportCount(self, value: int | float):
        pass


class _ClearMemory:
    @property
    def ClearMemory(self) -> float:
        return DeviceLogicType(self, self._id, "ClearMemory")

    @ClearMemory.setter
    def ClearMemory(self, value: int | float):
        pass


class _ClearMemorys:
    @property
    def ClearMemory(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ClearMemory", self._name_hash)

    @ClearMemory.setter
    def ClearMemory(self, value: int | float):
        pass


class _Hydrogen:
    @property
    def RatioHydrogen(self) -> float:
        return DeviceLogicType(self, self._id, "RatioHydrogen")

    @property
    def RatioLiquidHydrogen(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidHydrogen")


class _Hydrogens:
    @property
    def RatioHydrogen(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioHydrogen", self._name_hash)

    @property
    def RatioLiquidHydrogen(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioLiquidHydrogen", self._name_hash)


class _ImportCount:
    @property
    def ImportCount(self) -> float:
        return DeviceLogicType(self, self._id, "ImportCount")


class _ImportCounts:
    @property
    def ImportCount(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ImportCount", self._name_hash)


class _ExportCount:
    @property
    def ExportCount(self) -> float:
        return DeviceLogicType(self, self._id, "ExportCount")


class _ExportCounts:
    @property
    def ExportCount(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ExportCount", self._name_hash)


class _Volume:
    @property
    def Volume(self) -> float:
        return DeviceLogicType(self, self._id, "Volume")

    @property
    def VolumeOfLiquid(self) -> float:
        return DeviceLogicType(self, self._id, "VolumeOfLiquid")


class _Volumes:
    @property
    def Volume(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Volume", self._name_hash)

    @property
    def VolumeOfLiquid(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "VolumeOfLiquid", self._name_hash)


class _Vertical:
    @property
    def Horizontal(self) -> float:
        return DeviceLogicType(self, self._id, "Horizontal")

    @property
    def Vertical(self) -> float:
        return DeviceLogicType(self, self._id, "Vertical")


class _Verticals:
    @property
    def Horizontal(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Horizontal", self._name_hash)

    @property
    def Vertical(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Vertical", self._name_hash)


class _VerticalW:
    @property
    def Horizontal(self) -> float:
        return DeviceLogicType(self, self._id, "Horizontal")

    @Horizontal.setter
    def Horizontal(self, value: int | float):
        pass

    @property
    def Vertical(self) -> float:
        return DeviceLogicType(self, self._id, "Vertical")

    @Vertical.setter
    def Vertical(self, value: int | float):
        pass


class _VerticalWs:
    @property
    def Horizontal(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Horizontal", self._name_hash)

    @Horizontal.setter
    def Horizontal(self, value: int | float):
        pass

    @property
    def Vertical(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Vertical", self._name_hash)

    @Vertical.setter
    def Vertical(self, value: int | float):
        pass


class _RecipeHash:
    @property
    def RecipeHash(self) -> float:
        return DeviceLogicType(self, self._id, "RecipeHash")

    @RecipeHash.setter
    def RecipeHash(self, value: int | float):
        pass


class _RecipeHashs:
    @property
    def RecipeHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RecipeHash", self._name_hash)

    @RecipeHash.setter
    def RecipeHash(self, value: int | float):
        pass


class _Charge:
    @property
    def Charge(self) -> float:
        return DeviceLogicType(self, self._id, "Charge")


class _Charges:
    @property
    def Charge(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Charge", self._name_hash)


class _Reagents:
    @property
    def Reagents(self) -> float:
        return DeviceLogicType(self, self._id, "Reagents")


class _Reagentss:
    @property
    def Reagents(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Reagents", self._name_hash)


class _Quantity:
    @property
    def Quantity(self) -> float:
        return DeviceLogicType(self, self._id, "Quantity")


class _Quantitys:
    @property
    def Quantity(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Quantity", self._name_hash)


class AccessBridge(_BaseStructure, _Activate, _Lock, _Open, _Power):
    _hash: int = 1298920475


class _AccessBridges(_BaseStructures, _Activates, _Locks, _Opens, _Powers):
    _hash: int = 1298920475

    def __getitem__(self, name: str | int) -> "_AccessBridges":
        return _AccessBridges(name)


AccessBridges: _AccessBridges = _AccessBridges()


class LiquidDrain(_BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = 1687692899


class _LiquidDrains(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 1687692899

    def __getitem__(self, name: str | int) -> "_LiquidDrains":
        return _LiquidDrains(name)


LiquidDrains: _LiquidDrains = _LiquidDrains()


class ActiveVent(
    _BaseStructure, _Error, _Lock, _Maximum, _Mode, _Open, _Power, _Ratio, _SettingW
):
    _hash: int = -1129453144

    @property
    def PressureExternal(self) -> float:
        return DeviceLogicType(self, self._id, "PressureExternal")

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass

    @property
    def PressureInternal(self) -> float:
        return DeviceLogicType(self, self._id, "PressureInternal")

    @PressureInternal.setter
    def PressureInternal(self, value: int | float):
        pass


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

    def __getitem__(self, name: str | int) -> "_ActiveVents":
        return _ActiveVents(name)

    @property
    def PressureExternal(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureExternal", self._name_hash)

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass

    @property
    def PressureInternal(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureInternal", self._name_hash)

    @PressureInternal.setter
    def PressureInternal(self, value: int | float):
        pass


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

    def __getitem__(self, name: str | int) -> "_AdvancedComposters":
        return _AdvancedComposters(name)


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

    @property
    def RecipeHash(self) -> float:
        return DeviceLogicType(self, self._id, "RecipeHash")

    @property
    def SettingInput(self) -> float:
        return DeviceLogicType(self, self._id, "SettingInput")

    @SettingInput.setter
    def SettingInput(self, value: int | float):
        pass

    @property
    def SettingOutput(self) -> float:
        return DeviceLogicType(self, self._id, "SettingOutput")

    @SettingOutput.setter
    def SettingOutput(self, value: int | float):
        pass


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

    def __getitem__(self, name: str | int) -> "_AdvancedFurnaces":
        return _AdvancedFurnaces(name)

    @property
    def RecipeHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RecipeHash", self._name_hash)

    @property
    def SettingInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SettingInput", self._name_hash)

    @SettingInput.setter
    def SettingInput(self, value: int | float):
        pass

    @property
    def SettingOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SettingOutput", self._name_hash)

    @SettingOutput.setter
    def SettingOutput(self, value: int | float):
        pass


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

    @property
    def CompletionRatio(self) -> float:
        return DeviceLogicType(self, self._id, "CompletionRatio")


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

    def __getitem__(self, name: str | int) -> "_AdvancedPackagingMachines":
        return _AdvancedPackagingMachines(name)

    @property
    def CompletionRatio(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CompletionRatio", self._name_hash)


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

    @property
    def CombustionInput(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionInput")

    @property
    def CombustionOutput(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionOutput")

    @property
    def CombustionOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionOutput2")

    @property
    def OperationalTemperatureEfficiency(self) -> float:
        return DeviceLogicType(self, self._id, "OperationalTemperatureEfficiency")

    @property
    def PressureEfficiency(self) -> float:
        return DeviceLogicType(self, self._id, "PressureEfficiency")

    @property
    def PressureInput(self) -> float:
        return DeviceLogicType(self, self._id, "PressureInput")

    @property
    def PressureOutput(self) -> float:
        return DeviceLogicType(self, self._id, "PressureOutput")

    @property
    def PressureOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "PressureOutput2")

    @property
    def TemperatureDifferentialEfficiency(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureDifferentialEfficiency")

    @property
    def TemperatureInput(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureInput")

    @property
    def TemperatureOutput(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureOutput")

    @property
    def TemperatureOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureOutput2")

    @property
    def TotalMolesInput(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesInput")

    @property
    def TotalMolesOutput(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesOutput")

    @property
    def TotalMolesOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesOutput2")


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

    def __getitem__(self, name: str | int) -> "_AirConditioners":
        return _AirConditioners(name)

    @property
    def CombustionInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionInput", self._name_hash)

    @property
    def CombustionOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionOutput", self._name_hash)

    @property
    def CombustionOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionOutput2", self._name_hash)

    @property
    def OperationalTemperatureEfficiency(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "OperationalTemperatureEfficiency", self._name_hash
        )

    @property
    def PressureEfficiency(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureEfficiency", self._name_hash)

    @property
    def PressureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureInput", self._name_hash)

    @property
    def PressureOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureOutput", self._name_hash)

    @property
    def PressureOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureOutput2", self._name_hash)

    @property
    def TemperatureDifferentialEfficiency(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "TemperatureDifferentialEfficiency", self._name_hash
        )

    @property
    def TemperatureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureInput", self._name_hash)

    @property
    def TemperatureOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureOutput", self._name_hash)

    @property
    def TemperatureOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureOutput2", self._name_hash)

    @property
    def TotalMolesInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesInput", self._name_hash)

    @property
    def TotalMolesOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesOutput", self._name_hash)

    @property
    def TotalMolesOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesOutput2", self._name_hash)


AirConditioners: _AirConditioners = _AirConditioners()


class Airlock(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = -2105052344


class _Airlocks(_BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs):
    _hash: int = -2105052344

    def __getitem__(self, name: str | int) -> "_Airlocks":
        return _Airlocks(name)


Airlocks: _Airlocks = _Airlocks()


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

    @property
    def RecipeHash(self) -> float:
        return DeviceLogicType(self, self._id, "RecipeHash")


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

    def __getitem__(self, name: str | int) -> "_ArcFurnaces":
        return _ArcFurnaces(name)

    @property
    def RecipeHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RecipeHash", self._name_hash)


ArcFurnaces: _ArcFurnaces = _ArcFurnaces()


class AreaPowerControl(
    _BaseStructure, _Charge, _Error, _Lock, _Maximum, _Mode, _Open, _Power, _Ratio
):
    _hash: int = 1999523701

    @property
    def PowerActual(self) -> float:
        return DeviceLogicType(self, self._id, "PowerActual")

    @property
    def PowerPotential(self) -> float:
        return DeviceLogicType(self, self._id, "PowerPotential")


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

    def __getitem__(self, name: str | int) -> "_AreaPowerControls":
        return _AreaPowerControls(name)

    @property
    def PowerActual(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerActual", self._name_hash)

    @property
    def PowerPotential(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerPotential", self._name_hash)


AreaPowerControls: _AreaPowerControls = _AreaPowerControls()


class AreaPowerControlReversed(
    _BaseStructure, _Charge, _Error, _Lock, _Maximum, _Mode, _Open, _Power, _Ratio
):
    _hash: int = -1032513487

    @property
    def PowerActual(self) -> float:
        return DeviceLogicType(self, self._id, "PowerActual")

    @property
    def PowerPotential(self) -> float:
        return DeviceLogicType(self, self._id, "PowerPotential")


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

    def __getitem__(self, name: str | int) -> "_AreaPowerControlReverseds":
        return _AreaPowerControlReverseds(name)

    @property
    def PowerActual(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerActual", self._name_hash)

    @property
    def PowerPotential(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerPotential", self._name_hash)


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

    @property
    def CompletionRatio(self) -> float:
        return DeviceLogicType(self, self._id, "CompletionRatio")


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

    def __getitem__(self, name: str | int) -> "_Autolathes":
        return _Autolathes(name)

    @property
    def CompletionRatio(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CompletionRatio", self._name_hash)


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

    @property
    def CompletionRatio(self) -> float:
        return DeviceLogicType(self, self._id, "CompletionRatio")


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

    def __getitem__(self, name: str | int) -> "_AutomatedOvens":
        return _AutomatedOvens(name)

    @property
    def CompletionRatio(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CompletionRatio", self._name_hash)


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

    def __getitem__(self, name: str | int) -> "_AutoMinerSmalls":
        return _AutoMinerSmalls(name)


AutoMinerSmalls: _AutoMinerSmalls = _AutoMinerSmalls()


class BatterySmall(_BaseStructure, _Charge, _Maximum, _ModeR, _On, _Ratio):
    _hash: int = -2123455080

    @property
    def Power(self) -> float:
        return DeviceLogicType(self, self._id, "Power")

    @property
    def PowerActual(self) -> float:
        return DeviceLogicType(self, self._id, "PowerActual")

    @property
    def PowerPotential(self) -> float:
        return DeviceLogicType(self, self._id, "PowerPotential")


class _BatterySmalls(_BaseStructures, _Charges, _Maximums, _ModeRs, _Ons, _Ratios):
    _hash: int = -2123455080

    def __getitem__(self, name: str | int) -> "_BatterySmalls":
        return _BatterySmalls(name)

    @property
    def Power(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Power", self._name_hash)

    @property
    def PowerActual(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerActual", self._name_hash)

    @property
    def PowerPotential(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerPotential", self._name_hash)


BatterySmalls: _BatterySmalls = _BatterySmalls()


class BackPressureRegulator(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = -1149857558


class _BackPressureRegulators(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -1149857558

    def __getitem__(self, name: str | int) -> "_BackPressureRegulators":
        return _BackPressureRegulators(name)


BackPressureRegulators: _BackPressureRegulators = _BackPressureRegulators()


class BasketHoop(_BaseStructure, _Lock, _Power, _SettingW):
    _hash: int = -1613497288


class _BasketHoops(_BaseStructures, _Locks, _Powers, _SettingWs):
    _hash: int = -1613497288

    def __getitem__(self, name: str | int) -> "_BasketHoops":
        return _BasketHoops(name)


BasketHoops: _BasketHoops = _BasketHoops()


class LogicBatchReader(_BaseStructure, _Error, _Power, _SettingR):
    _hash: int = 264413729


class _LogicBatchReaders(_BaseStructures, _Errors, _Powers, _SettingRs):
    _hash: int = 264413729

    def __getitem__(self, name: str | int) -> "_LogicBatchReaders":
        return _LogicBatchReaders(name)


LogicBatchReaders: _LogicBatchReaders = _LogicBatchReaders()


class LogicBatchSlotReader(_BaseStructure, _Error, _Power, _SettingR):
    _hash: int = 436888930


class _LogicBatchSlotReaders(_BaseStructures, _Errors, _Powers, _SettingRs):
    _hash: int = 436888930

    def __getitem__(self, name: str | int) -> "_LogicBatchSlotReaders":
        return _LogicBatchSlotReaders(name)


LogicBatchSlotReaders: _LogicBatchSlotReaders = _LogicBatchSlotReaders()


class LogicBatchWriter(_BaseStructure, _Error, _Power):
    _hash: int = 1415443359

    @property
    def ForceWrite(self) -> float:
        return DeviceLogicType(self, self._id, "ForceWrite")

    @ForceWrite.setter
    def ForceWrite(self, value: int | float):
        pass


class _LogicBatchWriters(_BaseStructures, _Errors, _Powers):
    _hash: int = 1415443359

    def __getitem__(self, name: str | int) -> "_LogicBatchWriters":
        return _LogicBatchWriters(name)

    @property
    def ForceWrite(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ForceWrite", self._name_hash)

    @ForceWrite.setter
    def ForceWrite(self, value: int | float):
        pass


LogicBatchWriters: _LogicBatchWriters = _LogicBatchWriters()


class BatteryMedium(_BaseStructure, _Charge, _Maximum, _ModeR, _On, _Ratio):
    _hash: int = -1125305264

    @property
    def Power(self) -> float:
        return DeviceLogicType(self, self._id, "Power")

    @property
    def PowerActual(self) -> float:
        return DeviceLogicType(self, self._id, "PowerActual")

    @property
    def PowerPotential(self) -> float:
        return DeviceLogicType(self, self._id, "PowerPotential")


class _BatteryMediums(_BaseStructures, _Charges, _Maximums, _ModeRs, _Ons, _Ratios):
    _hash: int = -1125305264

    def __getitem__(self, name: str | int) -> "_BatteryMediums":
        return _BatteryMediums(name)

    @property
    def Power(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Power", self._name_hash)

    @property
    def PowerActual(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerActual", self._name_hash)

    @property
    def PowerPotential(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerPotential", self._name_hash)


BatteryMediums: _BatteryMediums = _BatteryMediums()


class BatteryCharger(_BaseStructure, _Activate, _Error, _Power):
    _hash: int = 1945930022


class _BatteryChargers(_BaseStructures, _Activates, _Errors, _Powers):
    _hash: int = 1945930022

    def __getitem__(self, name: str | int) -> "_BatteryChargers":
        return _BatteryChargers(name)


BatteryChargers: _BatteryChargers = _BatteryChargers()


class BatteryChargerSmall(_BaseStructure, _Activate, _Error, _Power):
    _hash: int = -761772413


class _BatteryChargerSmalls(_BaseStructures, _Activates, _Errors, _Powers):
    _hash: int = -761772413

    def __getitem__(self, name: str | int) -> "_BatteryChargerSmalls":
        return _BatteryChargerSmalls(name)


BatteryChargerSmalls: _BatteryChargerSmalls = _BatteryChargerSmalls()


class Beacon(_BaseStructure, _Error, _Lock, _Power):
    _hash: int = -188177083

    @property
    def Color(self) -> float:
        return DeviceLogicType(self, self._id, "Color")

    @Color.setter
    def Color(self, value: int | float):
        pass


class _Beacons(_BaseStructures, _Errors, _Locks, _Powers):
    _hash: int = -188177083

    def __getitem__(self, name: str | int) -> "_Beacons":
        return _Beacons(name)

    @property
    def Color(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Color", self._name_hash)

    @Color.setter
    def Color(self, value: int | float):
        pass


Beacons: _Beacons = _Beacons()


class Bench1(_BaseStructure, _Error, _Power):
    _hash: int = 406745009


class _Bench1s(_BaseStructures, _Errors, _Powers):
    _hash: int = 406745009

    def __getitem__(self, name: str | int) -> "_Bench1s":
        return _Bench1s(name)


Bench1s: _Bench1s = _Bench1s()


class Bench3(_BaseStructure, _Error, _Power):
    _hash: int = -164622691


class _Bench3s(_BaseStructures, _Errors, _Powers):
    _hash: int = -164622691

    def __getitem__(self, name: str | int) -> "_Bench3s":
        return _Bench3s(name)


Bench3s: _Bench3s = _Bench3s()


class Bench2(_BaseStructure, _Error, _Power):
    _hash: int = -2127086069


class _Bench2s(_BaseStructures, _Errors, _Powers):
    _hash: int = -2127086069

    def __getitem__(self, name: str | int) -> "_Bench2s":
        return _Bench2s(name)


Bench2s: _Bench2s = _Bench2s()


class Bench4(_BaseStructure, _Error, _Power):
    _hash: int = 1750375230


class _Bench4s(_BaseStructures, _Errors, _Powers):
    _hash: int = 1750375230

    def __getitem__(self, name: str | int) -> "_Bench4s":
        return _Bench4s(name)


Bench4s: _Bench4s = _Bench4s()


class BlastDoor(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = 337416191


class _BlastDoors(_BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs):
    _hash: int = 337416191

    def __getitem__(self, name: str | int) -> "_BlastDoors":
        return _BlastDoors(name)


BlastDoors: _BlastDoors = _BlastDoors()


class BlockBed(_BaseStructure, _Activate, _Error, _Power):
    _hash: int = 697908419


class _BlockBeds(_BaseStructures, _Activates, _Errors, _Powers):
    _hash: int = 697908419

    def __getitem__(self, name: str | int) -> "_BlockBeds":
        return _BlockBeds(name)


BlockBeds: _BlockBeds = _BlockBeds()


class LogicButton(_BaseStructure, _Activate, _Lock, _SettingR):
    _hash: int = 491845673


class _LogicButtons(_BaseStructures, _Activates, _Locks, _SettingRs):
    _hash: int = 491845673

    def __getitem__(self, name: str | int) -> "_LogicButtons":
        return _LogicButtons(name)


LogicButtons: _LogicButtons = _LogicButtons()


class CableAnalysizer(_BaseStructure):
    _hash: int = 1036015121

    @property
    def PowerActual(self) -> float:
        return DeviceLogicType(self, self._id, "PowerActual")

    @property
    def PowerPotential(self) -> float:
        return DeviceLogicType(self, self._id, "PowerPotential")

    @property
    def PowerRequired(self) -> float:
        return DeviceLogicType(self, self._id, "PowerRequired")


class _CableAnalysizers(_BaseStructures):
    _hash: int = 1036015121

    def __getitem__(self, name: str | int) -> "_CableAnalysizers":
        return _CableAnalysizers(name)

    @property
    def PowerActual(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerActual", self._name_hash)

    @property
    def PowerPotential(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerPotential", self._name_hash)

    @property
    def PowerRequired(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerRequired", self._name_hash)


CableAnalysizers: _CableAnalysizers = _CableAnalysizers()


class Camera(_BaseStructure, _Mode, _On):
    _hash: int = -342072665


class _Cameras(_BaseStructures, _Modes, _Ons):
    _hash: int = -342072665

    def __getitem__(self, name: str | int) -> "_Cameras":
        return _Cameras(name)


Cameras: _Cameras = _Cameras()


class CarbonSequester(
    _BaseStructure,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Maximum,
    _Open,
    _Power,
    _Ratio,
    _SettingW,
):
    _hash: int = -865415211


class _CarbonSequesters(
    _BaseStructures,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Maximums,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
):
    _hash: int = -865415211

    def __getitem__(self, name: str | int) -> "_CarbonSequesters":
        return _CarbonSequesters(name)


CarbonSequesters: _CarbonSequesters = _CarbonSequesters()


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

    def __getitem__(self, name: str | int) -> "_CargoStorageMediums":
        return _CargoStorageMediums(name)


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

    def __getitem__(self, name: str | int) -> "_CargoStorageSmalls":
        return _CargoStorageSmalls(name)


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

    def __getitem__(self, name: str | int) -> "_Centrifuges":
        return _Centrifuges(name)


Centrifuges: _Centrifuges = _Centrifuges()


class ChuteDigitalFlipFlopSplitterLeft(_BaseStructure, _Mode, _Power, _SettingW):
    _hash: int = -810874728

    @property
    def Quantity(self) -> float:
        return DeviceLogicType(self, self._id, "Quantity")

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass

    @property
    def SettingOutput(self) -> float:
        return DeviceLogicType(self, self._id, "SettingOutput")

    @SettingOutput.setter
    def SettingOutput(self, value: int | float):
        pass


class _ChuteDigitalFlipFlopSplitterLefts(_BaseStructures, _Modes, _Powers, _SettingWs):
    _hash: int = -810874728

    def __getitem__(self, name: str | int) -> "_ChuteDigitalFlipFlopSplitterLefts":
        return _ChuteDigitalFlipFlopSplitterLefts(name)

    @property
    def Quantity(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Quantity", self._name_hash)

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass

    @property
    def SettingOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SettingOutput", self._name_hash)

    @SettingOutput.setter
    def SettingOutput(self, value: int | float):
        pass


ChuteDigitalFlipFlopSplitterLefts: _ChuteDigitalFlipFlopSplitterLefts = (
    _ChuteDigitalFlipFlopSplitterLefts()
)


class ChuteDigitalFlipFlopSplitterRight(_BaseStructure, _Mode, _Power, _SettingW):
    _hash: int = 163728359

    @property
    def Quantity(self) -> float:
        return DeviceLogicType(self, self._id, "Quantity")

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass

    @property
    def SettingOutput(self) -> float:
        return DeviceLogicType(self, self._id, "SettingOutput")

    @SettingOutput.setter
    def SettingOutput(self, value: int | float):
        pass


class _ChuteDigitalFlipFlopSplitterRights(_BaseStructures, _Modes, _Powers, _SettingWs):
    _hash: int = 163728359

    def __getitem__(self, name: str | int) -> "_ChuteDigitalFlipFlopSplitterRights":
        return _ChuteDigitalFlipFlopSplitterRights(name)

    @property
    def Quantity(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Quantity", self._name_hash)

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass

    @property
    def SettingOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SettingOutput", self._name_hash)

    @SettingOutput.setter
    def SettingOutput(self, value: int | float):
        pass


ChuteDigitalFlipFlopSplitterRights: _ChuteDigitalFlipFlopSplitterRights = (
    _ChuteDigitalFlipFlopSplitterRights()
)


class ChuteDigitalValveLeft(_BaseStructure, _Lock, _Open, _Power, _SettingW):
    _hash: int = 648608238

    @property
    def Quantity(self) -> float:
        return DeviceLogicType(self, self._id, "Quantity")

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass


class _ChuteDigitalValveLefts(_BaseStructures, _Locks, _Opens, _Powers, _SettingWs):
    _hash: int = 648608238

    def __getitem__(self, name: str | int) -> "_ChuteDigitalValveLefts":
        return _ChuteDigitalValveLefts(name)

    @property
    def Quantity(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Quantity", self._name_hash)

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass


ChuteDigitalValveLefts: _ChuteDigitalValveLefts = _ChuteDigitalValveLefts()


class ChuteDigitalValveRight(_BaseStructure, _Lock, _Open, _Power, _SettingW):
    _hash: int = -1337091041

    @property
    def Quantity(self) -> float:
        return DeviceLogicType(self, self._id, "Quantity")

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass


class _ChuteDigitalValveRights(_BaseStructures, _Locks, _Opens, _Powers, _SettingWs):
    _hash: int = -1337091041

    def __getitem__(self, name: str | int) -> "_ChuteDigitalValveRights":
        return _ChuteDigitalValveRights(name)

    @property
    def Quantity(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Quantity", self._name_hash)

    @Quantity.setter
    def Quantity(self, value: int | float):
        pass


ChuteDigitalValveRights: _ChuteDigitalValveRights = _ChuteDigitalValveRights()


class ChuteExportBin(_BaseStructure, _Error, _Lock, _Open, _Power):
    _hash: int = 1957571043


class _ChuteExportBins(_BaseStructures, _Errors, _Locks, _Opens, _Powers):
    _hash: int = 1957571043

    def __getitem__(self, name: str | int) -> "_ChuteExportBins":
        return _ChuteExportBins(name)


ChuteExportBins: _ChuteExportBins = _ChuteExportBins()


class ChuteBin(_BaseStructure, _Error, _Lock, _Open, _Power):
    _hash: int = -850484480


class _ChuteBins(_BaseStructures, _Errors, _Locks, _Opens, _Powers):
    _hash: int = -850484480

    def __getitem__(self, name: str | int) -> "_ChuteBins":
        return _ChuteBins(name)


ChuteBins: _ChuteBins = _ChuteBins()


class ChuteInlet(_BaseStructure, _ClearMemory, _ImportCount, _Lock):
    _hash: int = -1469588766


class _ChuteInlets(_BaseStructures, _ClearMemorys, _ImportCounts, _Locks):
    _hash: int = -1469588766

    def __getitem__(self, name: str | int) -> "_ChuteInlets":
        return _ChuteInlets(name)


ChuteInlets: _ChuteInlets = _ChuteInlets()


class ChuteOutlet(_BaseStructure, _ClearMemory, _ExportCount, _ImportCount, _Lock):
    _hash: int = -1022714809


class _ChuteOutlets(
    _BaseStructures, _ClearMemorys, _ExportCounts, _ImportCounts, _Locks
):
    _hash: int = -1022714809

    def __getitem__(self, name: str | int) -> "_ChuteOutlets":
        return _ChuteOutlets(name)


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

    @property
    def CombustionInput(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionInput")

    @property
    def CombustionLimiter(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionLimiter")

    @CombustionLimiter.setter
    def CombustionLimiter(self, value: int | float):
        pass

    @property
    def CombustionOutput(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionOutput")

    @property
    def PressureInput(self) -> float:
        return DeviceLogicType(self, self._id, "PressureInput")

    @property
    def PressureOutput(self) -> float:
        return DeviceLogicType(self, self._id, "PressureOutput")

    @property
    def Rpm(self) -> float:
        return DeviceLogicType(self, self._id, "Rpm")

    @property
    def Stress(self) -> float:
        return DeviceLogicType(self, self._id, "Stress")

    @property
    def TemperatureInput(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureInput")

    @property
    def TemperatureOutput(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureOutput")

    @property
    def Throttle(self) -> float:
        return DeviceLogicType(self, self._id, "Throttle")

    @Throttle.setter
    def Throttle(self, value: int | float):
        pass

    @property
    def TotalMolesInput(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesInput")

    @property
    def TotalMolesOutput(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesOutput")


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

    def __getitem__(self, name: str | int) -> "_CombustionCentrifuges":
        return _CombustionCentrifuges(name)

    @property
    def CombustionInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionInput", self._name_hash)

    @property
    def CombustionLimiter(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionLimiter", self._name_hash)

    @CombustionLimiter.setter
    def CombustionLimiter(self, value: int | float):
        pass

    @property
    def CombustionOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionOutput", self._name_hash)

    @property
    def PressureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureInput", self._name_hash)

    @property
    def PressureOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureOutput", self._name_hash)

    @property
    def Rpm(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Rpm", self._name_hash)

    @property
    def Stress(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Stress", self._name_hash)

    @property
    def TemperatureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureInput", self._name_hash)

    @property
    def TemperatureOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureOutput", self._name_hash)

    @property
    def Throttle(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Throttle", self._name_hash)

    @Throttle.setter
    def Throttle(self, value: int | float):
        pass

    @property
    def TotalMolesInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesInput", self._name_hash)

    @property
    def TotalMolesOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesOutput", self._name_hash)


CombustionCentrifuges: _CombustionCentrifuges = _CombustionCentrifuges()


class CompositeDoor(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = -793837322


class _CompositeDoors(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = -793837322

    def __getitem__(self, name: str | int) -> "_CompositeDoors":
        return _CompositeDoors(name)


CompositeDoors: _CompositeDoors = _CompositeDoors()


class CompositeWindowShutterController(_BaseStructure, _Error, _Lock, _Open, _Power):
    _hash: int = -2078371660


class _CompositeWindowShutterControllers(
    _BaseStructures, _Errors, _Locks, _Opens, _Powers
):
    _hash: int = -2078371660

    def __getitem__(self, name: str | int) -> "_CompositeWindowShutterControllers":
        return _CompositeWindowShutterControllers(name)


CompositeWindowShutterControllers: _CompositeWindowShutterControllers = (
    _CompositeWindowShutterControllers()
)


class Computer(_BaseStructure, _Error, _Lock, _Open, _Power):
    _hash: int = -626563514


class _Computers(_BaseStructures, _Errors, _Locks, _Opens, _Powers):
    _hash: int = -626563514

    def __getitem__(self, name: str | int) -> "_Computers":
        return _Computers(name)


Computers: _Computers = _Computers()


class ComputerUpright(_BaseStructure, _Error, _Lock, _Open, _Power):
    _hash: int = -405593895


class _ComputerUprights(_BaseStructures, _Errors, _Locks, _Opens, _Powers):
    _hash: int = -405593895

    def __getitem__(self, name: str | int) -> "_ComputerUprights":
        return _ComputerUprights(name)


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

    def __getitem__(self, name: str | int) -> "_CondensationChambers":
        return _CondensationChambers(name)


CondensationChambers: _CondensationChambers = _CondensationChambers()


class CondensationValve(_BaseStructure, _Maximum, _On, _Ratio, _SettingW):
    _hash: int = -965741795


class _CondensationValves(_BaseStructures, _Maximums, _Ons, _Ratios, _SettingWs):
    _hash: int = -965741795

    def __getitem__(self, name: str | int) -> "_CondensationValves":
        return _CondensationValves(name)


CondensationValves: _CondensationValves = _CondensationValves()


class Console(_BaseStructure, _Error, _Open, _Power, _SettingR):
    _hash: int = 235638270


class _Consoles(_BaseStructures, _Errors, _Opens, _Powers, _SettingRs):
    _hash: int = 235638270

    def __getitem__(self, name: str | int) -> "_Consoles":
        return _Consoles(name)


Consoles: _Consoles = _Consoles()


class ConsoleDual(_BaseStructure, _Error, _Open, _Power, _SettingR):
    _hash: int = -722284333


class _ConsoleDuals(_BaseStructures, _Errors, _Opens, _Powers, _SettingRs):
    _hash: int = -722284333

    def __getitem__(self, name: str | int) -> "_ConsoleDuals":
        return _ConsoleDuals(name)


ConsoleDuals: _ConsoleDuals = _ConsoleDuals()


class ConsoleMonitor(_BaseStructure, _Error, _Open, _Power, _SettingR):
    _hash: int = 801677497


class _ConsoleMonitors(_BaseStructures, _Errors, _Opens, _Powers, _SettingRs):
    _hash: int = 801677497

    def __getitem__(self, name: str | int) -> "_ConsoleMonitors":
        return _ConsoleMonitors(name)


ConsoleMonitors: _ConsoleMonitors = _ConsoleMonitors()


class ControlChair(
    _BaseStructure,
    _BaseGas,
    _Combustion,
    _Error,
    _Hydrogen,
    _Maximum,
    _Mode,
    _PollWater,
    _Power,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = -1961153710


class _ControlChairs(
    _BaseStructures,
    _BaseGass,
    _Combustions,
    _Errors,
    _Hydrogens,
    _Maximums,
    _Modes,
    _PollWaters,
    _Powers,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = -1961153710

    def __getitem__(self, name: str | int) -> "_ControlChairs":
        return _ControlChairs(name)


ControlChairs: _ControlChairs = _ControlChairs()


class CornerLocker(_BaseStructure, _Lock, _Open):
    _hash: int = -1968255729


class _CornerLockers(_BaseStructures, _Locks, _Opens):
    _hash: int = -1968255729

    def __getitem__(self, name: str | int) -> "_CornerLockers":
        return _CornerLockers(name)


CornerLockers: _CornerLockers = _CornerLockers()


class PassthroughHeatExchangerGasToGas(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -1674187440


class _PassthroughHeatExchangerGasToGass(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = -1674187440

    def __getitem__(self, name: str | int) -> "_PassthroughHeatExchangerGasToGass":
        return _PassthroughHeatExchangerGasToGass(name)


PassthroughHeatExchangerGasToGass: _PassthroughHeatExchangerGasToGass = (
    _PassthroughHeatExchangerGasToGass()
)


class PassthroughHeatExchangerGasToLiquid(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 1928991265


class _PassthroughHeatExchangerGasToLiquids(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = 1928991265

    def __getitem__(self, name: str | int) -> "_PassthroughHeatExchangerGasToLiquids":
        return _PassthroughHeatExchangerGasToLiquids(name)


PassthroughHeatExchangerGasToLiquids: _PassthroughHeatExchangerGasToLiquids = (
    _PassthroughHeatExchangerGasToLiquids()
)


class PassthroughHeatExchangerLiquidToLiquid(
    _BaseStructure, _Maximum, _Ratio, _SettingW
):
    _hash: int = -1472829583


class _PassthroughHeatExchangerLiquidToLiquids(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = -1472829583

    def __getitem__(
        self, name: str | int
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
    _Open,
    _Power,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = 1443059329

    @property
    def EntityState(self) -> float:
        return DeviceLogicType(self, self._id, "EntityState")


class _CryoTubeHorizontals(
    _BaseStructures,
    _Activates,
    _Errors,
    _Locks,
    _Maximums,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = 1443059329

    def __getitem__(self, name: str | int) -> "_CryoTubeHorizontals":
        return _CryoTubeHorizontals(name)

    @property
    def EntityState(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "EntityState", self._name_hash)


CryoTubeHorizontals: _CryoTubeHorizontals = _CryoTubeHorizontals()


class CryoTubeVertical(
    _BaseStructure,
    _Activate,
    _Error,
    _Lock,
    _Maximum,
    _Open,
    _Power,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = -1381321828

    @property
    def EntityState(self) -> float:
        return DeviceLogicType(self, self._id, "EntityState")


class _CryoTubeVerticals(
    _BaseStructures,
    _Activates,
    _Errors,
    _Locks,
    _Maximums,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = -1381321828

    def __getitem__(self, name: str | int) -> "_CryoTubeVerticals":
        return _CryoTubeVerticals(name)

    @property
    def EntityState(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "EntityState", self._name_hash)


CryoTubeVerticals: _CryoTubeVerticals = _CryoTubeVerticals()


class CryoTube(
    _BaseStructure,
    _Activate,
    _Error,
    _Lock,
    _Maximum,
    _Open,
    _Power,
    _Ratio,
    _SettingW,
    _Temperature,
):
    _hash: int = 1938254586

    @property
    def EntityState(self) -> float:
        return DeviceLogicType(self, self._id, "EntityState")


class _CryoTubes(
    _BaseStructures,
    _Activates,
    _Errors,
    _Locks,
    _Maximums,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
    _Temperatures,
):
    _hash: int = 1938254586

    def __getitem__(self, name: str | int) -> "_CryoTubes":
        return _CryoTubes(name)

    @property
    def EntityState(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "EntityState", self._name_hash)


CryoTubes: _CryoTubes = _CryoTubes()


class DaylightSensor(_BaseStructure, _Activate, _Mode, _On, _Vertical):
    _hash: int = 1076425094

    @property
    def SolarAngle(self) -> float:
        return DeviceLogicType(self, self._id, "SolarAngle")

    @property
    def SolarIrradiance(self) -> float:
        return DeviceLogicType(self, self._id, "SolarIrradiance")


class _DaylightSensors(_BaseStructures, _Activates, _Modes, _Ons, _Verticals):
    _hash: int = 1076425094

    def __getitem__(self, name: str | int) -> "_DaylightSensors":
        return _DaylightSensors(name)

    @property
    def SolarAngle(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SolarAngle", self._name_hash)

    @property
    def SolarIrradiance(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SolarIrradiance", self._name_hash)


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

    def __getitem__(self, name: str | int) -> "_DeepMiners":
        return _DeepMiners(name)


DeepMiners: _DeepMiners = _DeepMiners()


class LogicDial(_BaseStructure, _Mode, _Ratio, _SettingW):
    _hash: int = 554524804


class _LogicDials(_BaseStructures, _Modes, _Ratios, _SettingWs):
    _hash: int = 554524804

    def __getitem__(self, name: str | int) -> "_LogicDials":
        return _LogicDials(name)


LogicDials: _LogicDials = _LogicDials()


class DigitalValve(_BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = -1280984102


class _DigitalValves(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -1280984102

    def __getitem__(self, name: str | int) -> "_DigitalValves":
        return _DigitalValves(name)


DigitalValves: _DigitalValves = _DigitalValves()


class DiodeSlide(_BaseStructure, _Lock, _Power, _SettingW):
    _hash: int = 576516101


class _DiodeSlides(_BaseStructures, _Locks, _Powers, _SettingWs):
    _hash: int = 576516101

    def __getitem__(self, name: str | int) -> "_DiodeSlides":
        return _DiodeSlides(name)


DiodeSlides: _DiodeSlides = _DiodeSlides()


class DispersalTower(
    _BaseStructure,
    _BaseGasInput,
    _ClearMemory,
    _Error,
    _ExportCount,
    _ImportCount,
    _Lock,
    _Maximum,
    _Open,
    _Power,
    _Ratio,
    _SettingW,
):
    _hash: int = -1868831137

    @property
    def CombustionInput(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionInput")

    @property
    def PressureInput(self) -> float:
        return DeviceLogicType(self, self._id, "PressureInput")

    @property
    def TemperatureInput(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureInput")

    @property
    def TotalMolesInput(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesInput")


class _DispersalTowers(
    _BaseStructures,
    _BaseGasInputs,
    _ClearMemorys,
    _Errors,
    _ExportCounts,
    _ImportCounts,
    _Locks,
    _Maximums,
    _Opens,
    _Powers,
    _Ratios,
    _SettingWs,
):
    _hash: int = -1868831137

    def __getitem__(self, name: str | int) -> "_DispersalTowers":
        return _DispersalTowers(name)

    @property
    def CombustionInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionInput", self._name_hash)

    @property
    def PressureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureInput", self._name_hash)

    @property
    def TemperatureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureInput", self._name_hash)

    @property
    def TotalMolesInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesInput", self._name_hash)


DispersalTowers: _DispersalTowers = _DispersalTowers()


class DockPortSide(_BaseStructure, _Idle, _Lock, _Open, _Power, _SettingW):
    _hash: int = -137465079


class _DockPortSides(_BaseStructures, _Idles, _Locks, _Opens, _Powers, _SettingWs):
    _hash: int = -137465079

    def __getitem__(self, name: str | int) -> "_DockPortSides":
        return _DockPortSides(name)


DockPortSides: _DockPortSides = _DockPortSides()


class DrinkingFountain(_BaseStructure, _Error, _Power):
    _hash: int = 1968371847


class _DrinkingFountains(_BaseStructures, _Errors, _Powers):
    _hash: int = 1968371847

    def __getitem__(self, name: str | int) -> "_DrinkingFountains":
        return _DrinkingFountains(name)


DrinkingFountains: _DrinkingFountains = _DrinkingFountains()


class SleeperVerticalDroid(_BaseStructure, _Activate, _Error, _Lock, _Open, _Power):
    _hash: int = 1382098999


class _SleeperVerticalDroids(
    _BaseStructures, _Activates, _Errors, _Locks, _Opens, _Powers
):
    _hash: int = 1382098999

    def __getitem__(self, name: str | int) -> "_SleeperVerticalDroids":
        return _SleeperVerticalDroids(name)


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

    @property
    def CombustionInput(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionInput")

    @property
    def CombustionOutput(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionOutput")

    @property
    def PressureInput(self) -> float:
        return DeviceLogicType(self, self._id, "PressureInput")

    @property
    def PressureOutput(self) -> float:
        return DeviceLogicType(self, self._id, "PressureOutput")

    @property
    def TemperatureInput(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureInput")

    @property
    def TemperatureOutput(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureOutput")

    @property
    def TotalMolesInput(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesInput")

    @property
    def TotalMolesOutput(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesOutput")


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

    def __getitem__(self, name: str | int) -> "_Electrolyzers":
        return _Electrolyzers(name)

    @property
    def CombustionInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionInput", self._name_hash)

    @property
    def CombustionOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionOutput", self._name_hash)

    @property
    def PressureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureInput", self._name_hash)

    @property
    def PressureOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureOutput", self._name_hash)

    @property
    def TemperatureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureInput", self._name_hash)

    @property
    def TemperatureOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureOutput", self._name_hash)

    @property
    def TotalMolesInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesInput", self._name_hash)

    @property
    def TotalMolesOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesOutput", self._name_hash)


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

    @property
    def CompletionRatio(self) -> float:
        return DeviceLogicType(self, self._id, "CompletionRatio")


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

    def __getitem__(self, name: str | int) -> "_ElectronicsPrinters":
        return _ElectronicsPrinters(name)

    @property
    def CompletionRatio(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CompletionRatio", self._name_hash)


ElectronicsPrinters: _ElectronicsPrinters = _ElectronicsPrinters()


class ElevatorLevelIndustrial(_BaseStructure, _Activate, _Error, _Lock, _Open, _Power):
    _hash: int = 2060648791

    @property
    def ElevatorLevel(self) -> float:
        return DeviceLogicType(self, self._id, "ElevatorLevel")

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> float:
        return DeviceLogicType(self, self._id, "ElevatorSpeed")

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value: int | float):
        pass


class _ElevatorLevelIndustrials(
    _BaseStructures, _Activates, _Errors, _Locks, _Opens, _Powers
):
    _hash: int = 2060648791

    def __getitem__(self, name: str | int) -> "_ElevatorLevelIndustrials":
        return _ElevatorLevelIndustrials(name)

    @property
    def ElevatorLevel(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ElevatorLevel", self._name_hash)

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ElevatorSpeed", self._name_hash)

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value: int | float):
        pass


ElevatorLevelIndustrials: _ElevatorLevelIndustrials = _ElevatorLevelIndustrials()


class ElevatorLevelFront(_BaseStructure, _Activate, _Error, _Lock, _Open, _Power):
    _hash: int = -827912235

    @property
    def ElevatorLevel(self) -> float:
        return DeviceLogicType(self, self._id, "ElevatorLevel")

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> float:
        return DeviceLogicType(self, self._id, "ElevatorSpeed")

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value: int | float):
        pass


class _ElevatorLevelFronts(
    _BaseStructures, _Activates, _Errors, _Locks, _Opens, _Powers
):
    _hash: int = -827912235

    def __getitem__(self, name: str | int) -> "_ElevatorLevelFronts":
        return _ElevatorLevelFronts(name)

    @property
    def ElevatorLevel(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ElevatorLevel", self._name_hash)

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ElevatorSpeed", self._name_hash)

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value: int | float):
        pass


ElevatorLevelFronts: _ElevatorLevelFronts = _ElevatorLevelFronts()


class ElevatorShaftIndustrial(_BaseStructure):
    _hash: int = 1998354978

    @property
    def ElevatorLevel(self) -> float:
        return DeviceLogicType(self, self._id, "ElevatorLevel")

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> float:
        return DeviceLogicType(self, self._id, "ElevatorSpeed")

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value: int | float):
        pass


class _ElevatorShaftIndustrials(_BaseStructures):
    _hash: int = 1998354978

    def __getitem__(self, name: str | int) -> "_ElevatorShaftIndustrials":
        return _ElevatorShaftIndustrials(name)

    @property
    def ElevatorLevel(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ElevatorLevel", self._name_hash)

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ElevatorSpeed", self._name_hash)

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value: int | float):
        pass


ElevatorShaftIndustrials: _ElevatorShaftIndustrials = _ElevatorShaftIndustrials()


class ElevatorShaft(_BaseStructure, _Power):
    _hash: int = 826144419

    @property
    def ElevatorLevel(self) -> float:
        return DeviceLogicType(self, self._id, "ElevatorLevel")

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> float:
        return DeviceLogicType(self, self._id, "ElevatorSpeed")

    @ElevatorSpeed.setter
    def ElevatorSpeed(self, value: int | float):
        pass


class _ElevatorShafts(_BaseStructures, _Powers):
    _hash: int = 826144419

    def __getitem__(self, name: str | int) -> "_ElevatorShafts":
        return _ElevatorShafts(name)

    @property
    def ElevatorLevel(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ElevatorLevel", self._name_hash)

    @ElevatorLevel.setter
    def ElevatorLevel(self, value: int | float):
        pass

    @property
    def ElevatorSpeed(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ElevatorSpeed", self._name_hash)

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

    def __getitem__(self, name: str | int) -> "_EvaporationChambers":
        return _EvaporationChambers(name)


EvaporationChambers: _EvaporationChambers = _EvaporationChambers()


class ExpansionValve(_BaseStructure, _Maximum, _On, _Ratio, _SettingW):
    _hash: int = 195298587


class _ExpansionValves(_BaseStructures, _Maximums, _Ons, _Ratios, _SettingWs):
    _hash: int = 195298587

    def __getitem__(self, name: str | int) -> "_ExpansionValves":
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

    @property
    def CombustionInput(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionInput")

    @property
    def CombustionOutput(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionOutput")

    @property
    def CombustionOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionOutput2")

    @property
    def PressureInput(self) -> float:
        return DeviceLogicType(self, self._id, "PressureInput")

    @property
    def PressureOutput(self) -> float:
        return DeviceLogicType(self, self._id, "PressureOutput")

    @property
    def PressureOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "PressureOutput2")

    @property
    def TemperatureInput(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureInput")

    @property
    def TemperatureOutput(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureOutput")

    @property
    def TemperatureOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureOutput2")

    @property
    def TotalMolesInput(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesInput")

    @property
    def TotalMolesOutput(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesOutput")

    @property
    def TotalMolesOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesOutput2")


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

    def __getitem__(self, name: str | int) -> "_Filtrations":
        return _Filtrations(name)

    @property
    def CombustionInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionInput", self._name_hash)

    @property
    def CombustionOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionOutput", self._name_hash)

    @property
    def CombustionOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionOutput2", self._name_hash)

    @property
    def PressureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureInput", self._name_hash)

    @property
    def PressureOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureOutput", self._name_hash)

    @property
    def PressureOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureOutput2", self._name_hash)

    @property
    def TemperatureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureInput", self._name_hash)

    @property
    def TemperatureOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureOutput", self._name_hash)

    @property
    def TemperatureOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureOutput2", self._name_hash)

    @property
    def TotalMolesInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesInput", self._name_hash)

    @property
    def TotalMolesOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesOutput", self._name_hash)

    @property
    def TotalMolesOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesOutput2", self._name_hash)


Filtrations: _Filtrations = _Filtrations()


class FlashingLight(_BaseStructure, _Lock, _Power):
    _hash: int = -1535893860


class _FlashingLights(_BaseStructures, _Locks, _Powers):
    _hash: int = -1535893860

    def __getitem__(self, name: str | int) -> "_FlashingLights":
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

    def __getitem__(self, name: str | int) -> "_FridgeBigs":
        return _FridgeBigs(name)


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

    def __getitem__(self, name: str | int) -> "_FridgeSmalls":
        return _FridgeSmalls(name)


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

    @property
    def RecipeHash(self) -> float:
        return DeviceLogicType(self, self._id, "RecipeHash")


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

    def __getitem__(self, name: str | int) -> "_Furnaces":
        return _Furnaces(name)

    @property
    def RecipeHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RecipeHash", self._name_hash)


Furnaces: _Furnaces = _Furnaces()


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

    def __getitem__(self, name: str | int) -> "_MediumRocketGasFuelTanks":
        return _MediumRocketGasFuelTanks(name)


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

    def __getitem__(self, name: str | int) -> "_CapsuleTankGass":
        return _CapsuleTankGass(name)


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

    @property
    def PowerGeneration(self) -> float:
        return DeviceLogicType(self, self._id, "PowerGeneration")


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

    def __getitem__(self, name: str | int) -> "_GasGenerators":
        return _GasGenerators(name)

    @property
    def PowerGeneration(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerGeneration", self._name_hash)


GasGenerators: _GasGenerators = _GasGenerators()


class GasMixer(_BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = 2104106366


class _GasMixers(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 2104106366

    def __getitem__(self, name: str | int) -> "_GasMixers":
        return _GasMixers(name)


GasMixers: _GasMixers = _GasMixers()


class GasSensor(_BaseStructure, _BaseGas, _Hydrogen, _PollWater, _Temperature):
    _hash: int = -1252983604

    @property
    def Combustion(self) -> float:
        return DeviceLogicType(self, self._id, "Combustion")


class _GasSensors(_BaseStructures, _BaseGass, _Hydrogens, _PollWaters, _Temperatures):
    _hash: int = -1252983604

    def __getitem__(self, name: str | int) -> "_GasSensors":
        return _GasSensors(name)

    @property
    def Combustion(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Combustion", self._name_hash)


GasSensors: _GasSensors = _GasSensors()


class GasTankStorage(_BaseStructure, _Quantity, _Temperature):
    _hash: int = 1632165346

    @property
    def RatioCarbonDioxide(self) -> float:
        return DeviceLogicType(self, self._id, "RatioCarbonDioxide")

    @property
    def RatioNitrogen(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrogen")

    @property
    def RatioNitrousOxide(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrousOxide")

    @property
    def RatioOxygen(self) -> float:
        return DeviceLogicType(self, self._id, "RatioOxygen")

    @property
    def RatioPollutant(self) -> float:
        return DeviceLogicType(self, self._id, "RatioPollutant")

    @property
    def RatioVolatiles(self) -> float:
        return DeviceLogicType(self, self._id, "RatioVolatiles")

    @property
    def RatioWater(self) -> float:
        return DeviceLogicType(self, self._id, "RatioWater")


class _GasTankStorages(_BaseStructures, _Quantitys, _Temperatures):
    _hash: int = 1632165346

    def __getitem__(self, name: str | int) -> "_GasTankStorages":
        return _GasTankStorages(name)

    @property
    def RatioCarbonDioxide(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioCarbonDioxide", self._name_hash)

    @property
    def RatioNitrogen(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrogen", self._name_hash)

    @property
    def RatioNitrousOxide(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrousOxide", self._name_hash)

    @property
    def RatioOxygen(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioOxygen", self._name_hash)

    @property
    def RatioPollutant(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioPollutant", self._name_hash)

    @property
    def RatioVolatiles(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioVolatiles", self._name_hash)

    @property
    def RatioWater(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioWater", self._name_hash)


GasTankStorages: _GasTankStorages = _GasTankStorages()


class SolidFuelGenerator(_BaseStructure, _ClearMemory, _ImportCount, _Lock, _On):
    _hash: int = 813146305

    @property
    def PowerGeneration(self) -> float:
        return DeviceLogicType(self, self._id, "PowerGeneration")


class _SolidFuelGenerators(_BaseStructures, _ClearMemorys, _ImportCounts, _Locks, _Ons):
    _hash: int = 813146305

    def __getitem__(self, name: str | int) -> "_SolidFuelGenerators":
        return _SolidFuelGenerators(name)

    @property
    def PowerGeneration(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerGeneration", self._name_hash)


SolidFuelGenerators: _SolidFuelGenerators = _SolidFuelGenerators()


class GlassDoor(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = -324331872


class _GlassDoors(_BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs):
    _hash: int = -324331872

    def __getitem__(self, name: str | int) -> "_GlassDoors":
        return _GlassDoors(name)


GlassDoors: _GlassDoors = _GlassDoors()


class GrowLight(_BaseStructure, _Lock, _Power):
    _hash: int = -1758710260


class _GrowLights(_BaseStructures, _Locks, _Powers):
    _hash: int = -1758710260

    def __getitem__(self, name: str | int) -> "_GrowLights":
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

    @property
    def Harvest(self) -> float:
        return DeviceLogicType(self, self._id, "Harvest")

    @Harvest.setter
    def Harvest(self, value: int | float):
        pass

    @property
    def Plant(self) -> float:
        return DeviceLogicType(self, self._id, "Plant")

    @Plant.setter
    def Plant(self, value: int | float):
        pass


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

    def __getitem__(self, name: str | int) -> "_Harvies":
        return _Harvies(name)

    @property
    def Harvest(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Harvest", self._name_hash)

    @Harvest.setter
    def Harvest(self, value: int | float):
        pass

    @property
    def Plant(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Plant", self._name_hash)

    @Plant.setter
    def Plant(self, value: int | float):
        pass


Harvies: _Harvies = _Harvies()


class HeatExchangeLiquidtoGas(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 944685608


class _HeatExchangeLiquidtoGass(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = 944685608

    def __getitem__(self, name: str | int) -> "_HeatExchangeLiquidtoGass":
        return _HeatExchangeLiquidtoGass(name)


HeatExchangeLiquidtoGass: _HeatExchangeLiquidtoGass = _HeatExchangeLiquidtoGass()


class HeatExchangerGastoGas(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 21266291


class _HeatExchangerGastoGass(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = 21266291

    def __getitem__(self, name: str | int) -> "_HeatExchangerGastoGass":
        return _HeatExchangerGastoGass(name)


HeatExchangerGastoGass: _HeatExchangerGastoGass = _HeatExchangerGastoGass()


class HeatExchangerLiquidtoLiquid(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -613784254


class _HeatExchangerLiquidtoLiquids(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = -613784254

    def __getitem__(self, name: str | int) -> "_HeatExchangerLiquidtoLiquids":
        return _HeatExchangerLiquidtoLiquids(name)


HeatExchangerLiquidtoLiquids: _HeatExchangerLiquidtoLiquids = (
    _HeatExchangerLiquidtoLiquids()
)


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

    @property
    def CompletionRatio(self) -> float:
        return DeviceLogicType(self, self._id, "CompletionRatio")


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

    def __getitem__(self, name: str | int) -> "_HydraulicPipeBenders":
        return _HydraulicPipeBenders(name)

    @property
    def CompletionRatio(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CompletionRatio", self._name_hash)


HydraulicPipeBenders: _HydraulicPipeBenders = _HydraulicPipeBenders()


class HydroponicsTrayData(
    _BaseStructure, _BaseGas, _Combustion, _Hydrogen, _PollWater, _Temperature
):
    _hash: int = -1841632400


class _HydroponicsTrayDatas(
    _BaseStructures, _BaseGass, _Combustions, _Hydrogens, _PollWaters, _Temperatures
):
    _hash: int = -1841632400

    def __getitem__(self, name: str | int) -> "_HydroponicsTrayDatas":
        return _HydroponicsTrayDatas(name)


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

    def __getitem__(self, name: str | int) -> "_HydroponicsStations":
        return _HydroponicsStations(name)


HydroponicsStations: _HydroponicsStations = _HydroponicsStations()


class CircuitHousing(_BaseStructure, _Error, _Power, _SettingW):
    _hash: int = -128473777

    @property
    def LineNumber(self) -> float:
        return DeviceLogicType(self, self._id, "LineNumber")

    @LineNumber.setter
    def LineNumber(self, value: int | float):
        pass


class _CircuitHousings(_BaseStructures, _Errors, _Powers, _SettingWs):
    _hash: int = -128473777

    def __getitem__(self, name: str | int) -> "_CircuitHousings":
        return _CircuitHousings(name)

    @property
    def LineNumber(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "LineNumber", self._name_hash)

    @LineNumber.setter
    def LineNumber(self, value: int | float):
        pass


CircuitHousings: _CircuitHousings = _CircuitHousings()


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

    def __getitem__(self, name: str | int) -> "_IceCrushers":
        return _IceCrushers(name)


IceCrushers: _IceCrushers = _IceCrushers()


class Igniter(_BaseStructure, _On):
    _hash: int = 1005491513


class _Igniters(_BaseStructures, _Ons):
    _hash: int = 1005491513

    def __getitem__(self, name: str | int) -> "_Igniters":
        return _Igniters(name)


Igniters: _Igniters = _Igniters()


class EmergencyButton(
    _BaseStructure, _Activate, _Error, _Lock, _Open, _Power, _SettingR
):
    _hash: int = 1668452680


class _EmergencyButtons(
    _BaseStructures, _Activates, _Errors, _Locks, _Opens, _Powers, _SettingRs
):
    _hash: int = 1668452680

    def __getitem__(self, name: str | int) -> "_EmergencyButtons":
        return _EmergencyButtons(name)


EmergencyButtons: _EmergencyButtons = _EmergencyButtons()


class IndustrialBurner(
    _BaseStructure,
    _BaseGas,
    _ClearMemory,
    _Combustion,
    _Error,
    _ExportCount,
    _Hydrogen,
    _ImportCount,
    _Lock,
    _Maximum,
    _PollWater,
    _Power,
    _Ratio,
    _Reagents,
    _SettingW,
    _Temperature,
):
    _hash: int = 1493870235

    @property
    def Activate(self) -> float:
        return DeviceLogicType(self, self._id, "Activate")

    @Activate.setter
    def Activate(self, value: int | float):
        pass

    @property
    def RecipeHash(self) -> float:
        return DeviceLogicType(self, self._id, "RecipeHash")


class _IndustrialBurners(
    _BaseStructures,
    _BaseGass,
    _ClearMemorys,
    _Combustions,
    _Errors,
    _ExportCounts,
    _Hydrogens,
    _ImportCounts,
    _Locks,
    _Maximums,
    _PollWaters,
    _Powers,
    _Ratios,
    _Reagentss,
    _SettingWs,
    _Temperatures,
):
    _hash: int = 1493870235

    def __getitem__(self, name: str | int) -> "_IndustrialBurners":
        return _IndustrialBurners(name)

    @property
    def Activate(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Activate", self._name_hash)

    @Activate.setter
    def Activate(self, value: int | float):
        pass

    @property
    def RecipeHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RecipeHash", self._name_hash)


IndustrialBurners: _IndustrialBurners = _IndustrialBurners()


class IndustrialCombustor(
    _BaseStructure,
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
    _hash: int = -586072380

    @property
    def CombustionInput(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionInput")

    @property
    def CombustionInput2(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionInput2")

    @property
    def CombustionOutput(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionOutput")

    @property
    def PressureInput(self) -> float:
        return DeviceLogicType(self, self._id, "PressureInput")

    @property
    def PressureInput2(self) -> float:
        return DeviceLogicType(self, self._id, "PressureInput2")

    @property
    def PressureOutput(self) -> float:
        return DeviceLogicType(self, self._id, "PressureOutput")

    @property
    def RatioCarbonDioxideInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioCarbonDioxideInput2")

    @property
    def RatioLiquidCarbonDioxideInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidCarbonDioxideInput2")

    @property
    def RatioLiquidNitrogenInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidNitrogenInput2")

    @property
    def RatioLiquidNitrousOxideInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidNitrousOxideInput2")

    @property
    def RatioLiquidOxygenInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidOxygenInput2")

    @property
    def RatioLiquidPollutantInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidPollutantInput2")

    @property
    def RatioLiquidVolatilesInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidVolatilesInput2")

    @property
    def RatioNitrogenInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrogenInput2")

    @property
    def RatioNitrousOxideInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrousOxideInput2")

    @property
    def RatioOxygenInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioOxygenInput2")

    @property
    def RatioPollutantInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioPollutantInput2")

    @property
    def RatioSteamInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioSteamInput2")

    @property
    def RatioVolatilesInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioVolatilesInput2")

    @property
    def RatioWaterInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioWaterInput2")

    @property
    def TemperatureInput(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureInput")

    @property
    def TemperatureInput2(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureInput2")

    @property
    def TemperatureOutput(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureOutput")

    @property
    def TotalMolesInput(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesInput")

    @property
    def TotalMolesInput2(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesInput2")

    @property
    def TotalMolesOutput(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesOutput")


class _IndustrialCombustors(
    _BaseStructures,
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
    _hash: int = -586072380

    def __getitem__(self, name: str | int) -> "_IndustrialCombustors":
        return _IndustrialCombustors(name)

    @property
    def CombustionInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionInput", self._name_hash)

    @property
    def CombustionInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionInput2", self._name_hash)

    @property
    def CombustionOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionOutput", self._name_hash)

    @property
    def PressureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureInput", self._name_hash)

    @property
    def PressureInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureInput2", self._name_hash)

    @property
    def PressureOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureOutput", self._name_hash)

    @property
    def RatioCarbonDioxideInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioCarbonDioxideInput2", self._name_hash)

    @property
    def RatioLiquidCarbonDioxideInput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidCarbonDioxideInput2", self._name_hash
        )

    @property
    def RatioLiquidNitrogenInput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidNitrogenInput2", self._name_hash
        )

    @property
    def RatioLiquidNitrousOxideInput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidNitrousOxideInput2", self._name_hash
        )

    @property
    def RatioLiquidOxygenInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioLiquidOxygenInput2", self._name_hash)

    @property
    def RatioLiquidPollutantInput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidPollutantInput2", self._name_hash
        )

    @property
    def RatioLiquidVolatilesInput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidVolatilesInput2", self._name_hash
        )

    @property
    def RatioNitrogenInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrogenInput2", self._name_hash)

    @property
    def RatioNitrousOxideInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrousOxideInput2", self._name_hash)

    @property
    def RatioOxygenInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioOxygenInput2", self._name_hash)

    @property
    def RatioPollutantInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioPollutantInput2", self._name_hash)

    @property
    def RatioSteamInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioSteamInput2", self._name_hash)

    @property
    def RatioVolatilesInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioVolatilesInput2", self._name_hash)

    @property
    def RatioWaterInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioWaterInput2", self._name_hash)

    @property
    def TemperatureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureInput", self._name_hash)

    @property
    def TemperatureInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureInput2", self._name_hash)

    @property
    def TemperatureOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureOutput", self._name_hash)

    @property
    def TotalMolesInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesInput", self._name_hash)

    @property
    def TotalMolesInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesInput2", self._name_hash)

    @property
    def TotalMolesOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesOutput", self._name_hash)


IndustrialCombustors: _IndustrialCombustors = _IndustrialCombustors()


class IndustrialFiltration(
    _BaseStructure,
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
    _hash: int = 1167018773

    @property
    def CombustionOutput(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionOutput")

    @property
    def CombustionOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionOutput2")

    @property
    def PressureOutput(self) -> float:
        return DeviceLogicType(self, self._id, "PressureOutput")

    @property
    def PressureOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "PressureOutput2")

    @property
    def TemperatureOutput(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureOutput")

    @property
    def TemperatureOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureOutput2")

    @property
    def TotalMolesOutput(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesOutput")

    @property
    def TotalMolesOutput2(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesOutput2")


class _IndustrialFiltrations(
    _BaseStructures,
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
    _hash: int = 1167018773

    def __getitem__(self, name: str | int) -> "_IndustrialFiltrations":
        return _IndustrialFiltrations(name)

    @property
    def CombustionOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionOutput", self._name_hash)

    @property
    def CombustionOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionOutput2", self._name_hash)

    @property
    def PressureOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureOutput", self._name_hash)

    @property
    def PressureOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureOutput2", self._name_hash)

    @property
    def TemperatureOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureOutput", self._name_hash)

    @property
    def TemperatureOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureOutput2", self._name_hash)

    @property
    def TotalMolesOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesOutput", self._name_hash)

    @property
    def TotalMolesOutput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesOutput2", self._name_hash)


IndustrialFiltrations: _IndustrialFiltrations = _IndustrialFiltrations()


class InteriorDoorGlass(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = -2096421875


class _InteriorDoorGlasss(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = -2096421875

    def __getitem__(self, name: str | int) -> "_InteriorDoorGlasss":
        return _InteriorDoorGlasss(name)


InteriorDoorGlasss: _InteriorDoorGlasss = _InteriorDoorGlasss()


class InteriorDoorPadded(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = 847461335


class _InteriorDoorPaddeds(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = 847461335

    def __getitem__(self, name: str | int) -> "_InteriorDoorPaddeds":
        return _InteriorDoorPaddeds(name)


InteriorDoorPaddeds: _InteriorDoorPaddeds = _InteriorDoorPaddeds()


class InteriorDoorPaddedThin(
    _BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW
):
    _hash: int = 1981698201


class _InteriorDoorPaddedThins(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = 1981698201

    def __getitem__(self, name: str | int) -> "_InteriorDoorPaddedThins":
        return _InteriorDoorPaddedThins(name)


InteriorDoorPaddedThins: _InteriorDoorPaddedThins = _InteriorDoorPaddedThins()


class InteriorDoorTriangle(
    _BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW
):
    _hash: int = -1182923101


class _InteriorDoorTriangles(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = -1182923101

    def __getitem__(self, name: str | int) -> "_InteriorDoorTriangles":
        return _InteriorDoorTriangles(name)


InteriorDoorTriangles: _InteriorDoorTriangles = _InteriorDoorTriangles()


class Klaxon(_BaseStructure, _Mode, _Power):
    _hash: int = -828056979

    @property
    def SoundAlert(self) -> float:
        return DeviceLogicType(self, self._id, "SoundAlert")

    @SoundAlert.setter
    def SoundAlert(self, value: int | float):
        pass

    @property
    def Volume(self) -> float:
        return DeviceLogicType(self, self._id, "Volume")

    @Volume.setter
    def Volume(self, value: int | float):
        pass


class _Klaxons(_BaseStructures, _Modes, _Powers):
    _hash: int = -828056979

    def __getitem__(self, name: str | int) -> "_Klaxons":
        return _Klaxons(name)

    @property
    def SoundAlert(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SoundAlert", self._name_hash)

    @SoundAlert.setter
    def SoundAlert(self, value: int | float):
        pass

    @property
    def Volume(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Volume", self._name_hash)

    @Volume.setter
    def Volume(self, value: int | float):
        pass


Klaxons: _Klaxons = _Klaxons()


class RoboticArmDock(_BaseStructure, _Activate, _Error, _Idle, _Power, _SettingW):
    _hash: int = -1818718810

    @property
    def Extended(self) -> float:
        return DeviceLogicType(self, self._id, "Extended")

    @property
    def PositionX(self) -> float:
        return DeviceLogicType(self, self._id, "PositionX")


class _RoboticArmDocks(
    _BaseStructures, _Activates, _Errors, _Idles, _Powers, _SettingWs
):
    _hash: int = -1818718810

    def __getitem__(self, name: str | int) -> "_RoboticArmDocks":
        return _RoboticArmDocks(name)

    @property
    def Extended(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Extended", self._name_hash)

    @property
    def PositionX(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PositionX", self._name_hash)


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

    @property
    def CombustionInput(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionInput")

    @property
    def Extended(self) -> float:
        return DeviceLogicType(self, self._id, "Extended")

    @property
    def PositionX(self) -> float:
        return DeviceLogicType(self, self._id, "PositionX")

    @property
    def PressureExternal(self) -> float:
        return DeviceLogicType(self, self._id, "PressureExternal")

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass

    @property
    def PressureInput(self) -> float:
        return DeviceLogicType(self, self._id, "PressureInput")

    @property
    def PressureInternal(self) -> float:
        return DeviceLogicType(self, self._id, "PressureInternal")

    @PressureInternal.setter
    def PressureInternal(self, value: int | float):
        pass

    @property
    def TemperatureInput(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureInput")

    @property
    def TotalMolesInput(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesInput")


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

    def __getitem__(self, name: str | int) -> "_LarreDockAtmoss":
        return _LarreDockAtmoss(name)

    @property
    def CombustionInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionInput", self._name_hash)

    @property
    def Extended(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Extended", self._name_hash)

    @property
    def PositionX(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PositionX", self._name_hash)

    @property
    def PressureExternal(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureExternal", self._name_hash)

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass

    @property
    def PressureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureInput", self._name_hash)

    @property
    def PressureInternal(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureInternal", self._name_hash)

    @PressureInternal.setter
    def PressureInternal(self, value: int | float):
        pass

    @property
    def TemperatureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureInput", self._name_hash)

    @property
    def TotalMolesInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesInput", self._name_hash)


LarreDockAtmoss: _LarreDockAtmoss = _LarreDockAtmoss()


class LarreDockBypass(_BaseStructure, _Open, _Power):
    _hash: int = 1011275082


class _LarreDockBypasss(_BaseStructures, _Opens, _Powers):
    _hash: int = 1011275082

    def __getitem__(self, name: str | int) -> "_LarreDockBypasss":
        return _LarreDockBypasss(name)


LarreDockBypasss: _LarreDockBypasss = _LarreDockBypasss()


class LarreDockCargo(
    _BaseStructure, _Activate, _Error, _Idle, _Open, _Power, _SettingW
):
    _hash: int = -1555459562

    @property
    def Extended(self) -> float:
        return DeviceLogicType(self, self._id, "Extended")

    @property
    def PositionX(self) -> float:
        return DeviceLogicType(self, self._id, "PositionX")

    @property
    def TargetPrefabHash(self) -> float:
        return DeviceLogicType(self, self._id, "TargetPrefabHash")

    @property
    def TargetSlotIndex(self) -> float:
        return DeviceLogicType(self, self._id, "TargetSlotIndex")

    @TargetSlotIndex.setter
    def TargetSlotIndex(self, value: int | float):
        pass


class _LarreDockCargos(
    _BaseStructures, _Activates, _Errors, _Idles, _Opens, _Powers, _SettingWs
):
    _hash: int = -1555459562

    def __getitem__(self, name: str | int) -> "_LarreDockCargos":
        return _LarreDockCargos(name)

    @property
    def Extended(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Extended", self._name_hash)

    @property
    def PositionX(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PositionX", self._name_hash)

    @property
    def TargetPrefabHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TargetPrefabHash", self._name_hash)

    @property
    def TargetSlotIndex(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TargetSlotIndex", self._name_hash)

    @TargetSlotIndex.setter
    def TargetSlotIndex(self, value: int | float):
        pass


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

    @property
    def Extended(self) -> float:
        return DeviceLogicType(self, self._id, "Extended")

    @property
    def PositionX(self) -> float:
        return DeviceLogicType(self, self._id, "PositionX")


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

    def __getitem__(self, name: str | int) -> "_LarreDockCollectors":
        return _LarreDockCollectors(name)

    @property
    def Extended(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Extended", self._name_hash)

    @property
    def PositionX(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PositionX", self._name_hash)


LarreDockCollectors: _LarreDockCollectors = _LarreDockCollectors()


class LarreDockHydroponics(
    _BaseStructure, _Activate, _Error, _Idle, _Open, _Power, _SettingW
):
    _hash: int = 85133079

    @property
    def Extended(self) -> float:
        return DeviceLogicType(self, self._id, "Extended")

    @property
    def PositionX(self) -> float:
        return DeviceLogicType(self, self._id, "PositionX")

    @property
    def TargetPrefabHash(self) -> float:
        return DeviceLogicType(self, self._id, "TargetPrefabHash")

    @property
    def TargetSlotIndex(self) -> float:
        return DeviceLogicType(self, self._id, "TargetSlotIndex")


class _LarreDockHydroponicss(
    _BaseStructures, _Activates, _Errors, _Idles, _Opens, _Powers, _SettingWs
):
    _hash: int = 85133079

    def __getitem__(self, name: str | int) -> "_LarreDockHydroponicss":
        return _LarreDockHydroponicss(name)

    @property
    def Extended(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Extended", self._name_hash)

    @property
    def PositionX(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PositionX", self._name_hash)

    @property
    def TargetPrefabHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TargetPrefabHash", self._name_hash)

    @property
    def TargetSlotIndex(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TargetSlotIndex", self._name_hash)


LarreDockHydroponicss: _LarreDockHydroponicss = _LarreDockHydroponicss()


class Diode(_BaseStructure, _Lock, _Power):
    _hash: int = 1944485013

    @property
    def Color(self) -> float:
        return DeviceLogicType(self, self._id, "Color")

    @Color.setter
    def Color(self, value: int | float):
        pass


class _Diodes(_BaseStructures, _Locks, _Powers):
    _hash: int = 1944485013

    def __getitem__(self, name: str | int) -> "_Diodes":
        return _Diodes(name)

    @property
    def Color(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Color", self._name_hash)

    @Color.setter
    def Color(self, value: int | float):
        pass


Diodes: _Diodes = _Diodes()


class ConsoleLED1x3(_BaseStructure, _Error, _Mode, _Power, _SettingW):
    _hash: int = -1949054743

    @property
    def Color(self) -> float:
        return DeviceLogicType(self, self._id, "Color")

    @Color.setter
    def Color(self, value: int | float):
        pass


class _ConsoleLED1x3s(_BaseStructures, _Errors, _Modes, _Powers, _SettingWs):
    _hash: int = -1949054743

    def __getitem__(self, name: str | int) -> "_ConsoleLED1x3s":
        return _ConsoleLED1x3s(name)

    @property
    def Color(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Color", self._name_hash)

    @Color.setter
    def Color(self, value: int | float):
        pass


ConsoleLED1x3s: _ConsoleLED1x3s = _ConsoleLED1x3s()


class ConsoleLED1x2(_BaseStructure, _Error, _Mode, _Power, _SettingW):
    _hash: int = -53151617

    @property
    def Color(self) -> float:
        return DeviceLogicType(self, self._id, "Color")

    @Color.setter
    def Color(self, value: int | float):
        pass


class _ConsoleLED1x2s(_BaseStructures, _Errors, _Modes, _Powers, _SettingWs):
    _hash: int = -53151617

    def __getitem__(self, name: str | int) -> "_ConsoleLED1x2s":
        return _ConsoleLED1x2s(name)

    @property
    def Color(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Color", self._name_hash)

    @Color.setter
    def Color(self, value: int | float):
        pass


ConsoleLED1x2s: _ConsoleLED1x2s = _ConsoleLED1x2s()


class ConsoleLED5(_BaseStructure, _Error, _Mode, _Power, _SettingW):
    _hash: int = -815193061

    @property
    def Color(self) -> float:
        return DeviceLogicType(self, self._id, "Color")

    @Color.setter
    def Color(self, value: int | float):
        pass


class _ConsoleLED5s(_BaseStructures, _Errors, _Modes, _Powers, _SettingWs):
    _hash: int = -815193061

    def __getitem__(self, name: str | int) -> "_ConsoleLED5s":
        return _ConsoleLED5s(name)

    @property
    def Color(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Color", self._name_hash)

    @Color.setter
    def Color(self, value: int | float):
        pass


ConsoleLED5s: _ConsoleLED5s = _ConsoleLED5s()


class LargeDirectHeatExchangeLiquidtoLiquid(
    _BaseStructure, _Maximum, _Ratio, _SettingW
):
    _hash: int = 792686502


class _LargeDirectHeatExchangeLiquidtoLiquids(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = 792686502

    def __getitem__(self, name: str | int) -> "_LargeDirectHeatExchangeLiquidtoLiquids":
        return _LargeDirectHeatExchangeLiquidtoLiquids(name)


LargeDirectHeatExchangeLiquidtoLiquids: _LargeDirectHeatExchangeLiquidtoLiquids = (
    _LargeDirectHeatExchangeLiquidtoLiquids()
)


class LargeDirectHeatExchangeGastoGas(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -1230658883


class _LargeDirectHeatExchangeGastoGass(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = -1230658883

    def __getitem__(self, name: str | int) -> "_LargeDirectHeatExchangeGastoGass":
        return _LargeDirectHeatExchangeGastoGass(name)


LargeDirectHeatExchangeGastoGass: _LargeDirectHeatExchangeGastoGass = (
    _LargeDirectHeatExchangeGastoGass()
)


class LargeDirectHeatExchangeGastoLiquid(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 1412338038


class _LargeDirectHeatExchangeGastoLiquids(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = 1412338038

    def __getitem__(self, name: str | int) -> "_LargeDirectHeatExchangeGastoLiquids":
        return _LargeDirectHeatExchangeGastoLiquids(name)


LargeDirectHeatExchangeGastoLiquids: _LargeDirectHeatExchangeGastoLiquids = (
    _LargeDirectHeatExchangeGastoLiquids()
)


class LargeExtendableRadiator(
    _BaseStructure, _Lock, _Maximum, _Open, _Ratio, _SettingW
):
    _hash: int = -566775170

    @property
    def Horizontal(self) -> float:
        return DeviceLogicType(self, self._id, "Horizontal")

    @Horizontal.setter
    def Horizontal(self, value: int | float):
        pass


class _LargeExtendableRadiators(
    _BaseStructures, _Locks, _Maximums, _Opens, _Ratios, _SettingWs
):
    _hash: int = -566775170

    def __getitem__(self, name: str | int) -> "_LargeExtendableRadiators":
        return _LargeExtendableRadiators(name)

    @property
    def Horizontal(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Horizontal", self._name_hash)

    @Horizontal.setter
    def Horizontal(self, value: int | float):
        pass


LargeExtendableRadiators: _LargeExtendableRadiators = _LargeExtendableRadiators()


class LargeHangerDoor(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = -1351081801


class _LargeHangerDoors(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = -1351081801

    def __getitem__(self, name: str | int) -> "_LargeHangerDoors":
        return _LargeHangerDoors(name)


LargeHangerDoors: _LargeHangerDoors = _LargeHangerDoors()


class LargeSatelliteDish(
    _BaseStructure, _Activate, _Error, _Idle, _Power, _SettingW, _VerticalW
):
    _hash: int = 1913391845

    @property
    def BestContactFilter(self) -> float:
        return DeviceLogicType(self, self._id, "BestContactFilter")

    @BestContactFilter.setter
    def BestContactFilter(self, value: int | float):
        pass

    @property
    def ContactTypeId(self) -> float:
        return DeviceLogicType(self, self._id, "ContactTypeId")

    @property
    def InterrogationProgress(self) -> float:
        return DeviceLogicType(self, self._id, "InterrogationProgress")

    @property
    def MinimumWattsToContact(self) -> float:
        return DeviceLogicType(self, self._id, "MinimumWattsToContact")

    @property
    def SignalID(self) -> float:
        return DeviceLogicType(self, self._id, "SignalID")

    @property
    def SignalStrength(self) -> float:
        return DeviceLogicType(self, self._id, "SignalStrength")

    @property
    def SizeX(self) -> float:
        return DeviceLogicType(self, self._id, "SizeX")

    @property
    def SizeZ(self) -> float:
        return DeviceLogicType(self, self._id, "SizeZ")

    @property
    def TargetPadIndex(self) -> float:
        return DeviceLogicType(self, self._id, "TargetPadIndex")

    @TargetPadIndex.setter
    def TargetPadIndex(self, value: int | float):
        pass

    @property
    def WattsReachingContact(self) -> float:
        return DeviceLogicType(self, self._id, "WattsReachingContact")


class _LargeSatelliteDishs(
    _BaseStructures, _Activates, _Errors, _Idles, _Powers, _SettingWs, _VerticalWs
):
    _hash: int = 1913391845

    def __getitem__(self, name: str | int) -> "_LargeSatelliteDishs":
        return _LargeSatelliteDishs(name)

    @property
    def BestContactFilter(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "BestContactFilter", self._name_hash)

    @BestContactFilter.setter
    def BestContactFilter(self, value: int | float):
        pass

    @property
    def ContactTypeId(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ContactTypeId", self._name_hash)

    @property
    def InterrogationProgress(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "InterrogationProgress", self._name_hash)

    @property
    def MinimumWattsToContact(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "MinimumWattsToContact", self._name_hash)

    @property
    def SignalID(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SignalID", self._name_hash)

    @property
    def SignalStrength(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SignalStrength", self._name_hash)

    @property
    def SizeX(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SizeX", self._name_hash)

    @property
    def SizeZ(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SizeZ", self._name_hash)

    @property
    def TargetPadIndex(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TargetPadIndex", self._name_hash)

    @TargetPadIndex.setter
    def TargetPadIndex(self, value: int | float):
        pass

    @property
    def WattsReachingContact(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "WattsReachingContact", self._name_hash)


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

    def __getitem__(self, name: str | int) -> "_TankBigs":
        return _TankBigs(name)


TankBigs: _TankBigs = _TankBigs()


class LogicSwitch(_BaseStructure, _Lock, _Open, _SettingR):
    _hash: int = 1220484876


class _LogicSwitchs(_BaseStructures, _Locks, _Opens, _SettingRs):
    _hash: int = 1220484876

    def __getitem__(self, name: str | int) -> "_LogicSwitchs":
        return _LogicSwitchs(name)


LogicSwitchs: _LogicSwitchs = _LogicSwitchs()


class LightRound(_BaseStructure, _Lock, _Power):
    _hash: int = 1514476632


class _LightRounds(_BaseStructures, _Locks, _Powers):
    _hash: int = 1514476632

    def __getitem__(self, name: str | int) -> "_LightRounds":
        return _LightRounds(name)


LightRounds: _LightRounds = _LightRounds()


class LightRoundAngled(_BaseStructure, _Lock, _Power):
    _hash: int = 1592905386


class _LightRoundAngleds(_BaseStructures, _Locks, _Powers):
    _hash: int = 1592905386

    def __getitem__(self, name: str | int) -> "_LightRoundAngleds":
        return _LightRoundAngleds(name)


LightRoundAngleds: _LightRoundAngleds = _LightRoundAngleds()


class LightRoundSmall(_BaseStructure, _Lock, _Power):
    _hash: int = 1436121888


class _LightRoundSmalls(_BaseStructures, _Locks, _Powers):
    _hash: int = 1436121888

    def __getitem__(self, name: str | int) -> "_LightRoundSmalls":
        return _LightRoundSmalls(name)


LightRoundSmalls: _LightRoundSmalls = _LightRoundSmalls()


class RobotArmDoor(_BaseStructure, _Open):
    _hash: int = -2131782367

    @property
    def Power(self) -> float:
        return DeviceLogicType(self, self._id, "Power")

    @property
    def RequiredPower(self) -> float:
        return DeviceLogicType(self, self._id, "RequiredPower")


class _RobotArmDoors(_BaseStructures, _Opens):
    _hash: int = -2131782367

    def __getitem__(self, name: str | int) -> "_RobotArmDoors":
        return _RobotArmDoors(name)

    @property
    def Power(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Power", self._name_hash)

    @property
    def RequiredPower(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RequiredPower", self._name_hash)


RobotArmDoors: _RobotArmDoors = _RobotArmDoors()


class BackLiquidPressureRegulator(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = 2099900163


class _BackLiquidPressureRegulators(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 2099900163

    def __getitem__(self, name: str | int) -> "_BackLiquidPressureRegulators":
        return _BackLiquidPressureRegulators(name)


BackLiquidPressureRegulators: _BackLiquidPressureRegulators = (
    _BackLiquidPressureRegulators()
)


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

    def __getitem__(self, name: str | int) -> "_MediumRocketLiquidFuelTanks":
        return _MediumRocketLiquidFuelTanks(name)


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

    def __getitem__(self, name: str | int) -> "_CapsuleTankLiquids":
        return _CapsuleTankLiquids(name)


CapsuleTankLiquids: _CapsuleTankLiquids = _CapsuleTankLiquids()


class WaterDigitalValve(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = -517628750


class _WaterDigitalValves(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -517628750

    def __getitem__(self, name: str | int) -> "_WaterDigitalValves":
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

    def __getitem__(self, name: str | int) -> "_LiquidPipeAnalyzers":
        return _LiquidPipeAnalyzers(name)


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

    def __getitem__(self, name: str | int) -> "_LiquidTankBigs":
        return _LiquidTankBigs(name)


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

    def __getitem__(self, name: str | int) -> "_LiquidTankBigInsulateds":
        return _LiquidTankBigInsulateds(name)


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

    def __getitem__(self, name: str | int) -> "_LiquidTankSmalls":
        return _LiquidTankSmalls(name)


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

    def __getitem__(self, name: str | int) -> "_LiquidTankSmallInsulateds":
        return _LiquidTankSmallInsulateds(name)


LiquidTankSmallInsulateds: _LiquidTankSmallInsulateds = _LiquidTankSmallInsulateds()


class LiquidTankStorage(_BaseStructure, _Quantity, _Temperature):
    _hash: int = 1691898022

    @property
    def RatioCarbonDioxide(self) -> float:
        return DeviceLogicType(self, self._id, "RatioCarbonDioxide")

    @property
    def RatioNitrogen(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrogen")

    @property
    def RatioNitrousOxide(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrousOxide")

    @property
    def RatioOxygen(self) -> float:
        return DeviceLogicType(self, self._id, "RatioOxygen")

    @property
    def RatioPollutant(self) -> float:
        return DeviceLogicType(self, self._id, "RatioPollutant")

    @property
    def RatioVolatiles(self) -> float:
        return DeviceLogicType(self, self._id, "RatioVolatiles")

    @property
    def RatioWater(self) -> float:
        return DeviceLogicType(self, self._id, "RatioWater")


class _LiquidTankStorages(_BaseStructures, _Quantitys, _Temperatures):
    _hash: int = 1691898022

    def __getitem__(self, name: str | int) -> "_LiquidTankStorages":
        return _LiquidTankStorages(name)

    @property
    def RatioCarbonDioxide(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioCarbonDioxide", self._name_hash)

    @property
    def RatioNitrogen(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrogen", self._name_hash)

    @property
    def RatioNitrousOxide(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrousOxide", self._name_hash)

    @property
    def RatioOxygen(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioOxygen", self._name_hash)

    @property
    def RatioPollutant(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioPollutant", self._name_hash)

    @property
    def RatioVolatiles(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioVolatiles", self._name_hash)

    @property
    def RatioWater(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioWater", self._name_hash)


LiquidTankStorages: _LiquidTankStorages = _LiquidTankStorages()


class LiquidVolumePump(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = -454028979


class _LiquidVolumePumps(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -454028979

    def __getitem__(self, name: str | int) -> "_LiquidVolumePumps":
        return _LiquidVolumePumps(name)


LiquidVolumePumps: _LiquidVolumePumps = _LiquidVolumePumps()


class LiquidPressureRegulator(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = 482248766


class _LiquidPressureRegulators(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 482248766

    def __getitem__(self, name: str | int) -> "_LiquidPressureRegulators":
        return _LiquidPressureRegulators(name)


LiquidPressureRegulators: _LiquidPressureRegulators = _LiquidPressureRegulators()


class WaterWallCooler(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = -1369060582


class _WaterWallCoolers(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -1369060582

    def __getitem__(self, name: str | int) -> "_WaterWallCoolers":
        return _WaterWallCoolers(name)


WaterWallCoolers: _WaterWallCoolers = _WaterWallCoolers()


class StorageLocker(_BaseStructure, _Lock, _Open):
    _hash: int = -793623899


class _StorageLockers(_BaseStructures, _Locks, _Opens):
    _hash: int = -793623899

    def __getitem__(self, name: str | int) -> "_StorageLockers":
        return _StorageLockers(name)


StorageLockers: _StorageLockers = _StorageLockers()


class LockerSmall(_BaseStructure, _Lock, _Open):
    _hash: int = -647164662


class _LockerSmalls(_BaseStructures, _Locks, _Opens):
    _hash: int = -647164662

    def __getitem__(self, name: str | int) -> "_LockerSmalls":
        return _LockerSmalls(name)


LockerSmalls: _LockerSmalls = _LockerSmalls()


class LogicCompare(_BaseStructure, _Error, _Mode, _Power, _SettingR):
    _hash: int = -1489728908


class _LogicCompares(_BaseStructures, _Errors, _Modes, _Powers, _SettingRs):
    _hash: int = -1489728908

    def __getitem__(self, name: str | int) -> "_LogicCompares":
        return _LogicCompares(name)


LogicCompares: _LogicCompares = _LogicCompares()


class LogicGate(_BaseStructure, _Error, _Mode, _Power, _SettingR):
    _hash: int = 1942143074


class _LogicGates(_BaseStructures, _Errors, _Modes, _Powers, _SettingRs):
    _hash: int = 1942143074

    def __getitem__(self, name: str | int) -> "_LogicGates":
        return _LogicGates(name)


LogicGates: _LogicGates = _LogicGates()


class LogicHashGen(_BaseStructure, _SettingR):
    _hash: int = 2077593121


class _LogicHashGens(_BaseStructures, _SettingRs):
    _hash: int = 2077593121

    def __getitem__(self, name: str | int) -> "_LogicHashGens":
        return _LogicHashGens(name)


LogicHashGens: _LogicHashGens = _LogicHashGens()


class LogicMath(_BaseStructure, _Error, _Mode, _Power, _SettingR):
    _hash: int = 1657691323


class _LogicMaths(_BaseStructures, _Errors, _Modes, _Powers, _SettingRs):
    _hash: int = 1657691323

    def __getitem__(self, name: str | int) -> "_LogicMaths":
        return _LogicMaths(name)


LogicMaths: _LogicMaths = _LogicMaths()


class LogicMemory(_BaseStructure, _SettingW):
    _hash: int = -851746783


class _LogicMemorys(_BaseStructures, _SettingWs):
    _hash: int = -851746783

    def __getitem__(self, name: str | int) -> "_LogicMemorys":
        return _LogicMemorys(name)


LogicMemorys: _LogicMemorys = _LogicMemorys()


class LogicMinMax(_BaseStructure, _Error, _Mode, _Power, _SettingR):
    _hash: int = 929022276


class _LogicMinMaxs(_BaseStructures, _Errors, _Modes, _Powers, _SettingRs):
    _hash: int = 929022276

    def __getitem__(self, name: str | int) -> "_LogicMinMaxs":
        return _LogicMinMaxs(name)


LogicMinMaxs: _LogicMinMaxs = _LogicMinMaxs()


class LogicReader(_BaseStructure, _Error, _Power, _SettingR):
    _hash: int = -345383640


class _LogicReaders(_BaseStructures, _Errors, _Powers, _SettingRs):
    _hash: int = -345383640

    def __getitem__(self, name: str | int) -> "_LogicReaders":
        return _LogicReaders(name)


LogicReaders: _LogicReaders = _LogicReaders()


class LogicRocketDownlink(_BaseStructure):
    _hash: int = 876108549

    @property
    def Power(self) -> float:
        return DeviceLogicType(self, self._id, "Power")

    @property
    def RequiredPower(self) -> float:
        return DeviceLogicType(self, self._id, "RequiredPower")


class _LogicRocketDownlinks(_BaseStructures):
    _hash: int = 876108549

    def __getitem__(self, name: str | int) -> "_LogicRocketDownlinks":
        return _LogicRocketDownlinks(name)

    @property
    def Power(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Power", self._name_hash)

    @property
    def RequiredPower(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RequiredPower", self._name_hash)


LogicRocketDownlinks: _LogicRocketDownlinks = _LogicRocketDownlinks()


class LogicSelect(_BaseStructure, _Error, _Mode, _Power, _SettingR):
    _hash: int = 1822736084


class _LogicSelects(_BaseStructures, _Errors, _Modes, _Powers, _SettingRs):
    _hash: int = 1822736084

    def __getitem__(self, name: str | int) -> "_LogicSelects":
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

    def __getitem__(self, name: str | int) -> "_LogicSorters":
        return _LogicSorters(name)


LogicSorters: _LogicSorters = _LogicSorters()


class LogicRocketUplink(_BaseStructure, _Error, _Power):
    _hash: int = 546002924


class _LogicRocketUplinks(_BaseStructures, _Errors, _Powers):
    _hash: int = 546002924

    def __getitem__(self, name: str | int) -> "_LogicRocketUplinks":
        return _LogicRocketUplinks(name)


LogicRocketUplinks: _LogicRocketUplinks = _LogicRocketUplinks()


class LogicWriter(_BaseStructure, _Error, _Power):
    _hash: int = -1326019434

    @property
    def ForceWrite(self) -> float:
        return DeviceLogicType(self, self._id, "ForceWrite")

    @ForceWrite.setter
    def ForceWrite(self, value: int | float):
        pass


class _LogicWriters(_BaseStructures, _Errors, _Powers):
    _hash: int = -1326019434

    def __getitem__(self, name: str | int) -> "_LogicWriters":
        return _LogicWriters(name)

    @property
    def ForceWrite(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ForceWrite", self._name_hash)

    @ForceWrite.setter
    def ForceWrite(self, value: int | float):
        pass


LogicWriters: _LogicWriters = _LogicWriters()


class LogicWriterSwitch(_BaseStructure, _Activate, _Error, _Power):
    _hash: int = -1321250424

    @property
    def ForceWrite(self) -> float:
        return DeviceLogicType(self, self._id, "ForceWrite")

    @ForceWrite.setter
    def ForceWrite(self, value: int | float):
        pass


class _LogicWriterSwitchs(_BaseStructures, _Activates, _Errors, _Powers):
    _hash: int = -1321250424

    def __getitem__(self, name: str | int) -> "_LogicWriterSwitchs":
        return _LogicWriterSwitchs(name)

    @property
    def ForceWrite(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ForceWrite", self._name_hash)

    @ForceWrite.setter
    def ForceWrite(self, value: int | float):
        pass


LogicWriterSwitchs: _LogicWriterSwitchs = _LogicWriterSwitchs()


class ManualFloorHatch(_BaseStructure, _Idle, _Lock, _Open, _SettingW):
    _hash: int = 1435578852


class _ManualFloorHatchs(_BaseStructures, _Idles, _Locks, _Opens, _SettingWs):
    _hash: int = 1435578852

    def __getitem__(self, name: str | int) -> "_ManualFloorHatchs":
        return _ManualFloorHatchs(name)


ManualFloorHatchs: _ManualFloorHatchs = _ManualFloorHatchs()


class ManualHatch(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = -1808154199


class _ManualHatchs(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = -1808154199

    def __getitem__(self, name: str | int) -> "_ManualHatchs":
        return _ManualHatchs(name)


ManualHatchs: _ManualHatchs = _ManualHatchs()


class LogicMathUnary(_BaseStructure, _Error, _Mode, _Power, _SettingR):
    _hash: int = -1160020195


class _LogicMathUnarys(_BaseStructures, _Errors, _Modes, _Powers, _SettingRs):
    _hash: int = -1160020195

    def __getitem__(self, name: str | int) -> "_LogicMathUnarys":
        return _LogicMathUnarys(name)


LogicMathUnarys: _LogicMathUnarys = _LogicMathUnarys()


class MediumConvectionRadiator(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -1918215845


class _MediumConvectionRadiators(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = -1918215845

    def __getitem__(self, name: str | int) -> "_MediumConvectionRadiators":
        return _MediumConvectionRadiators(name)


MediumConvectionRadiators: _MediumConvectionRadiators = _MediumConvectionRadiators()


class PassiveLargeRadiatorGas(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 2066977095


class _PassiveLargeRadiatorGass(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = 2066977095

    def __getitem__(self, name: str | int) -> "_PassiveLargeRadiatorGass":
        return _PassiveLargeRadiatorGass(name)


PassiveLargeRadiatorGass: _PassiveLargeRadiatorGass = _PassiveLargeRadiatorGass()


class MediumConvectionRadiatorLiquid(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -1169014183


class _MediumConvectionRadiatorLiquids(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = -1169014183

    def __getitem__(self, name: str | int) -> "_MediumConvectionRadiatorLiquids":
        return _MediumConvectionRadiatorLiquids(name)


MediumConvectionRadiatorLiquids: _MediumConvectionRadiatorLiquids = (
    _MediumConvectionRadiatorLiquids()
)


class PassiveLargeRadiatorLiquid(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 24786172


class _PassiveLargeRadiatorLiquids(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = 24786172

    def __getitem__(self, name: str | int) -> "_PassiveLargeRadiatorLiquids":
        return _PassiveLargeRadiatorLiquids(name)


PassiveLargeRadiatorLiquids: _PassiveLargeRadiatorLiquids = (
    _PassiveLargeRadiatorLiquids()
)


class MediumHangerDoor(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = -566348148


class _MediumHangerDoors(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = -566348148

    def __getitem__(self, name: str | int) -> "_MediumHangerDoors":
        return _MediumHangerDoors(name)


MediumHangerDoors: _MediumHangerDoors = _MediumHangerDoors()


class MediumRadiator(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -975966237


class _MediumRadiators(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = -975966237

    def __getitem__(self, name: str | int) -> "_MediumRadiators":
        return _MediumRadiators(name)


MediumRadiators: _MediumRadiators = _MediumRadiators()


class MediumRadiatorLiquid(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -1141760613


class _MediumRadiatorLiquids(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = -1141760613

    def __getitem__(self, name: str | int) -> "_MediumRadiatorLiquids":
        return _MediumRadiatorLiquids(name)


MediumRadiatorLiquids: _MediumRadiatorLiquids = _MediumRadiatorLiquids()


class SatelliteDish(
    _BaseStructure, _Activate, _Error, _Idle, _Power, _SettingW, _VerticalW
):
    _hash: int = 439026183

    @property
    def BestContactFilter(self) -> float:
        return DeviceLogicType(self, self._id, "BestContactFilter")

    @BestContactFilter.setter
    def BestContactFilter(self, value: int | float):
        pass

    @property
    def ContactTypeId(self) -> float:
        return DeviceLogicType(self, self._id, "ContactTypeId")

    @property
    def InterrogationProgress(self) -> float:
        return DeviceLogicType(self, self._id, "InterrogationProgress")

    @property
    def MinimumWattsToContact(self) -> float:
        return DeviceLogicType(self, self._id, "MinimumWattsToContact")

    @property
    def SignalID(self) -> float:
        return DeviceLogicType(self, self._id, "SignalID")

    @property
    def SignalStrength(self) -> float:
        return DeviceLogicType(self, self._id, "SignalStrength")

    @property
    def SizeX(self) -> float:
        return DeviceLogicType(self, self._id, "SizeX")

    @property
    def SizeZ(self) -> float:
        return DeviceLogicType(self, self._id, "SizeZ")

    @property
    def TargetPadIndex(self) -> float:
        return DeviceLogicType(self, self._id, "TargetPadIndex")

    @TargetPadIndex.setter
    def TargetPadIndex(self, value: int | float):
        pass

    @property
    def WattsReachingContact(self) -> float:
        return DeviceLogicType(self, self._id, "WattsReachingContact")


class _SatelliteDishs(
    _BaseStructures, _Activates, _Errors, _Idles, _Powers, _SettingWs, _VerticalWs
):
    _hash: int = 439026183

    def __getitem__(self, name: str | int) -> "_SatelliteDishs":
        return _SatelliteDishs(name)

    @property
    def BestContactFilter(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "BestContactFilter", self._name_hash)

    @BestContactFilter.setter
    def BestContactFilter(self, value: int | float):
        pass

    @property
    def ContactTypeId(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ContactTypeId", self._name_hash)

    @property
    def InterrogationProgress(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "InterrogationProgress", self._name_hash)

    @property
    def MinimumWattsToContact(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "MinimumWattsToContact", self._name_hash)

    @property
    def SignalID(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SignalID", self._name_hash)

    @property
    def SignalStrength(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SignalStrength", self._name_hash)

    @property
    def SizeX(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SizeX", self._name_hash)

    @property
    def SizeZ(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SizeZ", self._name_hash)

    @property
    def TargetPadIndex(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TargetPadIndex", self._name_hash)

    @TargetPadIndex.setter
    def TargetPadIndex(self, value: int | float):
        pass

    @property
    def WattsReachingContact(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "WattsReachingContact", self._name_hash)


SatelliteDishs: _SatelliteDishs = _SatelliteDishs()


class PowerTransmitterReceiver(
    _BaseStructure, _Charge, _Error, _ModeR, _Power, _VerticalW
):
    _hash: int = 1195820278

    @property
    def PositionX(self) -> float:
        return DeviceLogicType(self, self._id, "PositionX")

    @property
    def PositionY(self) -> float:
        return DeviceLogicType(self, self._id, "PositionY")

    @property
    def PositionZ(self) -> float:
        return DeviceLogicType(self, self._id, "PositionZ")

    @property
    def PowerActual(self) -> float:
        return DeviceLogicType(self, self._id, "PowerActual")

    @property
    def PowerPotential(self) -> float:
        return DeviceLogicType(self, self._id, "PowerPotential")


class _PowerTransmitterReceivers(
    _BaseStructures, _Charges, _Errors, _ModeRs, _Powers, _VerticalWs
):
    _hash: int = 1195820278

    def __getitem__(self, name: str | int) -> "_PowerTransmitterReceivers":
        return _PowerTransmitterReceivers(name)

    @property
    def PositionX(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PositionX", self._name_hash)

    @property
    def PositionY(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PositionY", self._name_hash)

    @property
    def PositionZ(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PositionZ", self._name_hash)

    @property
    def PowerActual(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerActual", self._name_hash)

    @property
    def PowerPotential(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerPotential", self._name_hash)


PowerTransmitterReceivers: _PowerTransmitterReceivers = _PowerTransmitterReceivers()


class PowerTransmitter(_BaseStructure, _Charge, _Error, _ModeR, _Power, _VerticalW):
    _hash: int = -65087121

    @property
    def PositionX(self) -> float:
        return DeviceLogicType(self, self._id, "PositionX")

    @property
    def PositionY(self) -> float:
        return DeviceLogicType(self, self._id, "PositionY")

    @property
    def PositionZ(self) -> float:
        return DeviceLogicType(self, self._id, "PositionZ")

    @property
    def PowerActual(self) -> float:
        return DeviceLogicType(self, self._id, "PowerActual")

    @property
    def PowerPotential(self) -> float:
        return DeviceLogicType(self, self._id, "PowerPotential")


class _PowerTransmitters(
    _BaseStructures, _Charges, _Errors, _ModeRs, _Powers, _VerticalWs
):
    _hash: int = -65087121

    def __getitem__(self, name: str | int) -> "_PowerTransmitters":
        return _PowerTransmitters(name)

    @property
    def PositionX(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PositionX", self._name_hash)

    @property
    def PositionY(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PositionY", self._name_hash)

    @property
    def PositionZ(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PositionZ", self._name_hash)

    @property
    def PowerActual(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerActual", self._name_hash)

    @property
    def PowerPotential(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerPotential", self._name_hash)


PowerTransmitters: _PowerTransmitters = _PowerTransmitters()


class MotionSensor(_BaseStructure, _Activate, _On, _Quantity):
    _hash: int = -1713470563


class _MotionSensors(_BaseStructures, _Activates, _Ons, _Quantitys):
    _hash: int = -1713470563

    def __getitem__(self, name: str | int) -> "_MotionSensors":
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

    @property
    def CombustionInput(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionInput")

    @property
    def CombustionInput2(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionInput2")

    @property
    def CombustionOutput(self) -> float:
        return DeviceLogicType(self, self._id, "CombustionOutput")

    @property
    def PressureInput(self) -> float:
        return DeviceLogicType(self, self._id, "PressureInput")

    @property
    def PressureInput2(self) -> float:
        return DeviceLogicType(self, self._id, "PressureInput2")

    @property
    def PressureOutput(self) -> float:
        return DeviceLogicType(self, self._id, "PressureOutput")

    @property
    def RatioCarbonDioxideInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioCarbonDioxideInput2")

    @property
    def RatioLiquidCarbonDioxideInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidCarbonDioxideInput2")

    @property
    def RatioLiquidNitrogenInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidNitrogenInput2")

    @property
    def RatioLiquidNitrousOxideInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidNitrousOxideInput2")

    @property
    def RatioLiquidOxygenInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidOxygenInput2")

    @property
    def RatioLiquidPollutantInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidPollutantInput2")

    @property
    def RatioLiquidVolatilesInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioLiquidVolatilesInput2")

    @property
    def RatioNitrogenInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrogenInput2")

    @property
    def RatioNitrousOxideInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioNitrousOxideInput2")

    @property
    def RatioOxygenInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioOxygenInput2")

    @property
    def RatioPollutantInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioPollutantInput2")

    @property
    def RatioSteamInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioSteamInput2")

    @property
    def RatioVolatilesInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioVolatilesInput2")

    @property
    def RatioWaterInput2(self) -> float:
        return DeviceLogicType(self, self._id, "RatioWaterInput2")

    @property
    def TemperatureInput(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureInput")

    @property
    def TemperatureInput2(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureInput2")

    @property
    def TemperatureOutput(self) -> float:
        return DeviceLogicType(self, self._id, "TemperatureOutput")

    @property
    def TotalMolesInput(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesInput")

    @property
    def TotalMolesInput2(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesInput2")

    @property
    def TotalMolesOutput(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMolesOutput")


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

    def __getitem__(self, name: str | int) -> "_Nitrolyzers":
        return _Nitrolyzers(name)

    @property
    def CombustionInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionInput", self._name_hash)

    @property
    def CombustionInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionInput2", self._name_hash)

    @property
    def CombustionOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CombustionOutput", self._name_hash)

    @property
    def PressureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureInput", self._name_hash)

    @property
    def PressureInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureInput2", self._name_hash)

    @property
    def PressureOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureOutput", self._name_hash)

    @property
    def RatioCarbonDioxideInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioCarbonDioxideInput2", self._name_hash)

    @property
    def RatioLiquidCarbonDioxideInput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidCarbonDioxideInput2", self._name_hash
        )

    @property
    def RatioLiquidNitrogenInput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidNitrogenInput2", self._name_hash
        )

    @property
    def RatioLiquidNitrousOxideInput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidNitrousOxideInput2", self._name_hash
        )

    @property
    def RatioLiquidOxygenInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioLiquidOxygenInput2", self._name_hash)

    @property
    def RatioLiquidPollutantInput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidPollutantInput2", self._name_hash
        )

    @property
    def RatioLiquidVolatilesInput2(self) -> DevicesLogicType:
        return DevicesLogicType(
            self._hash, "RatioLiquidVolatilesInput2", self._name_hash
        )

    @property
    def RatioNitrogenInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrogenInput2", self._name_hash)

    @property
    def RatioNitrousOxideInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioNitrousOxideInput2", self._name_hash)

    @property
    def RatioOxygenInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioOxygenInput2", self._name_hash)

    @property
    def RatioPollutantInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioPollutantInput2", self._name_hash)

    @property
    def RatioSteamInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioSteamInput2", self._name_hash)

    @property
    def RatioVolatilesInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioVolatilesInput2", self._name_hash)

    @property
    def RatioWaterInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RatioWaterInput2", self._name_hash)

    @property
    def TemperatureInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureInput", self._name_hash)

    @property
    def TemperatureInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureInput2", self._name_hash)

    @property
    def TemperatureOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TemperatureOutput", self._name_hash)

    @property
    def TotalMolesInput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesInput", self._name_hash)

    @property
    def TotalMolesInput2(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesInput2", self._name_hash)

    @property
    def TotalMolesOutput(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMolesOutput", self._name_hash)


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

    def __getitem__(self, name: str | int) -> "_HorizontalAutoMiners":
        return _HorizontalAutoMiners(name)


HorizontalAutoMiners: _HorizontalAutoMiners = _HorizontalAutoMiners()


class OccupancySensor(_BaseStructure, _Quantity):
    _hash: int = 322782515

    @property
    def Activate(self) -> float:
        return DeviceLogicType(self, self._id, "Activate")


class _OccupancySensors(_BaseStructures, _Quantitys):
    _hash: int = 322782515

    def __getitem__(self, name: str | int) -> "_OccupancySensors":
        return _OccupancySensors(name)

    @property
    def Activate(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Activate", self._name_hash)


OccupancySensors: _OccupancySensors = _OccupancySensors()


class PipeOneWayValveLever(_BaseStructure, _Maximum, _On, _Ratio, _SettingW):
    _hash: int = 1289581593


class _PipeOneWayValveLevers(_BaseStructures, _Maximums, _Ons, _Ratios, _SettingWs):
    _hash: int = 1289581593

    def __getitem__(self, name: str | int) -> "_PipeOneWayValveLevers":
        return _PipeOneWayValveLevers(name)


PipeOneWayValveLevers: _PipeOneWayValveLevers = _PipeOneWayValveLevers()


class PipeLiquidOneWayValveLever(_BaseStructure, _Maximum, _On, _Ratio, _SettingW):
    _hash: int = -523832822


class _PipeLiquidOneWayValveLevers(
    _BaseStructures, _Maximums, _Ons, _Ratios, _SettingWs
):
    _hash: int = -523832822

    def __getitem__(self, name: str | int) -> "_PipeLiquidOneWayValveLevers":
        return _PipeLiquidOneWayValveLevers(name)


PipeLiquidOneWayValveLevers: _PipeLiquidOneWayValveLevers = (
    _PipeLiquidOneWayValveLevers()
)


class OverheadShortCornerLocker(_BaseStructure, _Lock, _Open):
    _hash: int = -1794932560


class _OverheadShortCornerLockers(_BaseStructures, _Locks, _Opens):
    _hash: int = -1794932560

    def __getitem__(self, name: str | int) -> "_OverheadShortCornerLockers":
        return _OverheadShortCornerLockers(name)


OverheadShortCornerLockers: _OverheadShortCornerLockers = _OverheadShortCornerLockers()


class OverheadShortLocker(_BaseStructure, _Lock, _Open):
    _hash: int = 1468249454


class _OverheadShortLockers(_BaseStructures, _Locks, _Opens):
    _hash: int = 1468249454

    def __getitem__(self, name: str | int) -> "_OverheadShortLockers":
        return _OverheadShortLockers(name)


OverheadShortLockers: _OverheadShortLockers = _OverheadShortLockers()


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

    def __getitem__(self, name: str | int) -> "_PipeAnalysizers":
        return _PipeAnalysizers(name)


PipeAnalysizers: _PipeAnalysizers = _PipeAnalysizers()


class PipeHeater(_BaseStructure, _Error, _Lock, _Power):
    _hash: int = -419758574


class _PipeHeaters(_BaseStructures, _Errors, _Locks, _Powers):
    _hash: int = -419758574

    def __getitem__(self, name: str | int) -> "_PipeHeaters":
        return _PipeHeaters(name)


PipeHeaters: _PipeHeaters = _PipeHeaters()


class LiquidPipeHeater(_BaseStructure, _Error, _Lock, _Power):
    _hash: int = -287495560


class _LiquidPipeHeaters(_BaseStructures, _Errors, _Locks, _Powers):
    _hash: int = -287495560

    def __getitem__(self, name: str | int) -> "_LiquidPipeHeaters":
        return _LiquidPipeHeaters(name)


LiquidPipeHeaters: _LiquidPipeHeaters = _LiquidPipeHeaters()


class PipeIgniter(_BaseStructure, _Activate, _Error):
    _hash: int = 1286441942

    @property
    def Power(self) -> float:
        return DeviceLogicType(self, self._id, "Power")

    @property
    def RequiredPower(self) -> float:
        return DeviceLogicType(self, self._id, "RequiredPower")


class _PipeIgniters(_BaseStructures, _Activates, _Errors):
    _hash: int = 1286441942

    def __getitem__(self, name: str | int) -> "_PipeIgniters":
        return _PipeIgniters(name)

    @property
    def Power(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Power", self._name_hash)

    @property
    def RequiredPower(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RequiredPower", self._name_hash)


PipeIgniters: _PipeIgniters = _PipeIgniters()


class PortablesConnector(_BaseStructure, _Maximum, _Open, _Ratio, _SettingW):
    _hash: int = -899013427


class _PortablesConnectors(_BaseStructures, _Maximums, _Opens, _Ratios, _SettingWs):
    _hash: int = -899013427

    def __getitem__(self, name: str | int) -> "_PortablesConnectors":
        return _PortablesConnectors(name)


PortablesConnectors: _PortablesConnectors = _PortablesConnectors()


class PowerConnector(_BaseStructure, _Open):
    _hash: int = -782951720


class _PowerConnectors(_BaseStructures, _Opens):
    _hash: int = -782951720

    def __getitem__(self, name: str | int) -> "_PowerConnectors":
        return _PowerConnectors(name)


PowerConnectors: _PowerConnectors = _PowerConnectors()


class PowerTransmitterOmni(_BaseStructure, _Error, _Power):
    _hash: int = -327468845


class _PowerTransmitterOmnis(_BaseStructures, _Errors, _Powers):
    _hash: int = -327468845

    def __getitem__(self, name: str | int) -> "_PowerTransmitterOmnis":
        return _PowerTransmitterOmnis(name)


PowerTransmitterOmnis: _PowerTransmitterOmnis = _PowerTransmitterOmnis()


class Bench(_BaseStructure, _Error, _Power):
    _hash: int = -2042448192


class _Benchs(_BaseStructures, _Errors, _Powers):
    _hash: int = -2042448192

    def __getitem__(self, name: str | int) -> "_Benchs":
        return _Benchs(name)


Benchs: _Benchs = _Benchs()


class PoweredVent(_BaseStructure, _Error, _Lock, _Mode, _Power):
    _hash: int = 938836756

    @property
    def PressureExternal(self) -> float:
        return DeviceLogicType(self, self._id, "PressureExternal")

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass


class _PoweredVents(_BaseStructures, _Errors, _Locks, _Modes, _Powers):
    _hash: int = 938836756

    def __getitem__(self, name: str | int) -> "_PoweredVents":
        return _PoweredVents(name)

    @property
    def PressureExternal(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureExternal", self._name_hash)

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass


PoweredVents: _PoweredVents = _PoweredVents()


class PoweredVentLarge(_BaseStructure, _Error, _Lock, _Mode, _Power):
    _hash: int = -785498334

    @property
    def PressureExternal(self) -> float:
        return DeviceLogicType(self, self._id, "PressureExternal")

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass


class _PoweredVentLarges(_BaseStructures, _Errors, _Locks, _Modes, _Powers):
    _hash: int = -785498334

    def __getitem__(self, name: str | int) -> "_PoweredVentLarges":
        return _PoweredVentLarges(name)

    @property
    def PressureExternal(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PressureExternal", self._name_hash)

    @PressureExternal.setter
    def PressureExternal(self, value: int | float):
        pass


PoweredVentLarges: _PoweredVentLarges = _PoweredVentLarges()


class PressurantValve(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = 23052817


class _PressurantValves(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 23052817

    def __getitem__(self, name: str | int) -> "_PressurantValves":
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

    @property
    def PassedMoles(self) -> float:
        return DeviceLogicType(self, self._id, "PassedMoles")

    @property
    def Throttle(self) -> float:
        return DeviceLogicType(self, self._id, "Throttle")

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

    def __getitem__(self, name: str | int) -> "_PressureFedGasEngines":
        return _PressureFedGasEngines(name)

    @property
    def PassedMoles(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PassedMoles", self._name_hash)

    @property
    def Throttle(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Throttle", self._name_hash)

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

    @property
    def PassedMoles(self) -> float:
        return DeviceLogicType(self, self._id, "PassedMoles")

    @property
    def Throttle(self) -> float:
        return DeviceLogicType(self, self._id, "Throttle")

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

    def __getitem__(self, name: str | int) -> "_PressureFedLiquidEngines":
        return _PressureFedLiquidEngines(name)

    @property
    def PassedMoles(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PassedMoles", self._name_hash)

    @property
    def Throttle(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Throttle", self._name_hash)

    @Throttle.setter
    def Throttle(self, value: int | float):
        pass


PressureFedLiquidEngines: _PressureFedLiquidEngines = _PressureFedLiquidEngines()


class PressureRegulator(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = 209854039


class _PressureRegulators(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 209854039

    def __getitem__(self, name: str | int) -> "_PressureRegulators":
        return _PressureRegulators(name)


PressureRegulators: _PressureRegulators = _PressureRegulators()


class ProximitySensor(_BaseStructure, _Quantity, _SettingW):
    _hash: int = 568800213

    @property
    def Activate(self) -> float:
        return DeviceLogicType(self, self._id, "Activate")


class _ProximitySensors(_BaseStructures, _Quantitys, _SettingWs):
    _hash: int = 568800213

    def __getitem__(self, name: str | int) -> "_ProximitySensors":
        return _ProximitySensors(name)

    @property
    def Activate(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Activate", self._name_hash)


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

    @property
    def PassedMoles(self) -> float:
        return DeviceLogicType(self, self._id, "PassedMoles")

    @property
    def Throttle(self) -> float:
        return DeviceLogicType(self, self._id, "Throttle")

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

    def __getitem__(self, name: str | int) -> "_GovernedGasEngines":
        return _GovernedGasEngines(name)

    @property
    def PassedMoles(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PassedMoles", self._name_hash)

    @property
    def Throttle(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Throttle", self._name_hash)

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

    @property
    def PassedMoles(self) -> float:
        return DeviceLogicType(self, self._id, "PassedMoles")

    @property
    def Throttle(self) -> float:
        return DeviceLogicType(self, self._id, "Throttle")

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

    def __getitem__(self, name: str | int) -> "_PumpedLiquidEngines":
        return _PumpedLiquidEngines(name)

    @property
    def PassedMoles(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PassedMoles", self._name_hash)

    @property
    def Throttle(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Throttle", self._name_hash)

    @Throttle.setter
    def Throttle(self, value: int | float):
        pass


PumpedLiquidEngines: _PumpedLiquidEngines = _PumpedLiquidEngines()


class PurgeValve(_BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = -737232128


class _PurgeValves(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -737232128

    def __getitem__(self, name: str | int) -> "_PurgeValves":
        return _PurgeValves(name)


PurgeValves: _PurgeValves = _PurgeValves()


class LogicReagentReader(_BaseStructure, _Error, _Power, _SettingR):
    _hash: int = -124308857


class _LogicReagentReaders(_BaseStructures, _Errors, _Powers, _SettingRs):
    _hash: int = -124308857

    def __getitem__(self, name: str | int) -> "_LogicReagentReaders":
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

    def __getitem__(self, name: str | int) -> "_Recyclers":
        return _Recyclers(name)


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

    @property
    def RequestHash(self) -> float:
        return DeviceLogicType(self, self._id, "RequestHash")

    @RequestHash.setter
    def RequestHash(self, value: int | float):
        pass


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

    def __getitem__(self, name: str | int) -> "_RefrigeratedVendingMachines":
        return _RefrigeratedVendingMachines(name)

    @property
    def RequestHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RequestHash", self._name_hash)

    @RequestHash.setter
    def RequestHash(self, value: int | float):
        pass


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

    @property
    def Acceleration(self) -> float:
        return DeviceLogicType(self, self._id, "Acceleration")

    @property
    def Altitude(self) -> float:
        return DeviceLogicType(self, self._id, "Altitude")

    @property
    def Apex(self) -> float:
        return DeviceLogicType(self, self._id, "Apex")

    @property
    def AutoLand(self) -> float:
        return DeviceLogicType(self, self._id, "AutoLand")

    @AutoLand.setter
    def AutoLand(self, value: int | float):
        pass

    @property
    def AutoShutOff(self) -> float:
        return DeviceLogicType(self, self._id, "AutoShutOff")

    @AutoShutOff.setter
    def AutoShutOff(self, value: int | float):
        pass

    @property
    def BurnTimeRemaining(self) -> float:
        return DeviceLogicType(self, self._id, "BurnTimeRemaining")

    @property
    def Chart(self) -> float:
        return DeviceLogicType(self, self._id, "Chart")

    @property
    def ChartedNavPoints(self) -> float:
        return DeviceLogicType(self, self._id, "ChartedNavPoints")

    @property
    def CurrentCode(self) -> float:
        return DeviceLogicType(self, self._id, "CurrentCode")

    @property
    def Density(self) -> float:
        return DeviceLogicType(self, self._id, "Density")

    @property
    def DestinationCode(self) -> float:
        return DeviceLogicType(self, self._id, "DestinationCode")

    @DestinationCode.setter
    def DestinationCode(self, value: int | float):
        pass

    @property
    def Discover(self) -> float:
        return DeviceLogicType(self, self._id, "Discover")

    @property
    def DryMass(self) -> float:
        return DeviceLogicType(self, self._id, "DryMass")

    @property
    def FlightControlRule(self) -> float:
        return DeviceLogicType(self, self._id, "FlightControlRule")

    @property
    def Mass(self) -> float:
        return DeviceLogicType(self, self._id, "Mass")

    @property
    def MinedQuantity(self) -> float:
        return DeviceLogicType(self, self._id, "MinedQuantity")

    @property
    def NavPoints(self) -> float:
        return DeviceLogicType(self, self._id, "NavPoints")

    @property
    def Progress(self) -> float:
        return DeviceLogicType(self, self._id, "Progress")

    @property
    def ReEntryAltitude(self) -> float:
        return DeviceLogicType(self, self._id, "ReEntryAltitude")

    @property
    def Richness(self) -> float:
        return DeviceLogicType(self, self._id, "Richness")

    @property
    def Sites(self) -> float:
        return DeviceLogicType(self, self._id, "Sites")

    @property
    def Size(self) -> float:
        return DeviceLogicType(self, self._id, "Size")

    @property
    def Survey(self) -> float:
        return DeviceLogicType(self, self._id, "Survey")

    @property
    def Temperature(self) -> float:
        return DeviceLogicType(self, self._id, "Temperature")

    @property
    def Thrust(self) -> float:
        return DeviceLogicType(self, self._id, "Thrust")

    @property
    def ThrustToWeight(self) -> float:
        return DeviceLogicType(self, self._id, "ThrustToWeight")

    @property
    def TimeToDestination(self) -> float:
        return DeviceLogicType(self, self._id, "TimeToDestination")

    @property
    def TotalMoles(self) -> float:
        return DeviceLogicType(self, self._id, "TotalMoles")

    @property
    def TotalQuantity(self) -> float:
        return DeviceLogicType(self, self._id, "TotalQuantity")

    @property
    def VelocityRelativeY(self) -> float:
        return DeviceLogicType(self, self._id, "VelocityRelativeY")

    @property
    def Weight(self) -> float:
        return DeviceLogicType(self, self._id, "Weight")


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

    def __getitem__(self, name: str | int) -> "_RocketAvionicss":
        return _RocketAvionicss(name)

    @property
    def Acceleration(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Acceleration", self._name_hash)

    @property
    def Altitude(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Altitude", self._name_hash)

    @property
    def Apex(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Apex", self._name_hash)

    @property
    def AutoLand(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "AutoLand", self._name_hash)

    @AutoLand.setter
    def AutoLand(self, value: int | float):
        pass

    @property
    def AutoShutOff(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "AutoShutOff", self._name_hash)

    @AutoShutOff.setter
    def AutoShutOff(self, value: int | float):
        pass

    @property
    def BurnTimeRemaining(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "BurnTimeRemaining", self._name_hash)

    @property
    def Chart(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Chart", self._name_hash)

    @property
    def ChartedNavPoints(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ChartedNavPoints", self._name_hash)

    @property
    def CurrentCode(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CurrentCode", self._name_hash)

    @property
    def Density(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Density", self._name_hash)

    @property
    def DestinationCode(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "DestinationCode", self._name_hash)

    @DestinationCode.setter
    def DestinationCode(self, value: int | float):
        pass

    @property
    def Discover(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Discover", self._name_hash)

    @property
    def DryMass(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "DryMass", self._name_hash)

    @property
    def FlightControlRule(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "FlightControlRule", self._name_hash)

    @property
    def Mass(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Mass", self._name_hash)

    @property
    def MinedQuantity(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "MinedQuantity", self._name_hash)

    @property
    def NavPoints(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "NavPoints", self._name_hash)

    @property
    def Progress(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Progress", self._name_hash)

    @property
    def ReEntryAltitude(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ReEntryAltitude", self._name_hash)

    @property
    def Richness(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Richness", self._name_hash)

    @property
    def Sites(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Sites", self._name_hash)

    @property
    def Size(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Size", self._name_hash)

    @property
    def Survey(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Survey", self._name_hash)

    @property
    def Temperature(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Temperature", self._name_hash)

    @property
    def Thrust(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Thrust", self._name_hash)

    @property
    def ThrustToWeight(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ThrustToWeight", self._name_hash)

    @property
    def TimeToDestination(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TimeToDestination", self._name_hash)

    @property
    def TotalMoles(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalMoles", self._name_hash)

    @property
    def TotalQuantity(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TotalQuantity", self._name_hash)

    @property
    def VelocityRelativeY(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "VelocityRelativeY", self._name_hash)

    @property
    def Weight(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Weight", self._name_hash)


RocketAvionicss: _RocketAvionicss = _RocketAvionicss()


class RocketCargoBay(_BaseStructure, _Error, _Lock, _Power):
    _hash: int = -682274666


class _RocketCargoBays(_BaseStructures, _Errors, _Locks, _Powers):
    _hash: int = -682274666

    def __getitem__(self, name: str | int) -> "_RocketCargoBays":
        return _RocketCargoBays(name)


RocketCargoBays: _RocketCargoBays = _RocketCargoBays()


class RocketCelestialTracker(_BaseStructure, _Error, _Power, _Vertical):
    _hash: int = 997453927

    @property
    def CelestialHash(self) -> float:
        return DeviceLogicType(self, self._id, "CelestialHash")

    @property
    def Index(self) -> float:
        return DeviceLogicType(self, self._id, "Index")

    @Index.setter
    def Index(self, value: int | float):
        pass


class _RocketCelestialTrackers(_BaseStructures, _Errors, _Powers, _Verticals):
    _hash: int = 997453927

    def __getitem__(self, name: str | int) -> "_RocketCelestialTrackers":
        return _RocketCelestialTrackers(name)

    @property
    def CelestialHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CelestialHash", self._name_hash)

    @property
    def Index(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Index", self._name_hash)

    @Index.setter
    def Index(self, value: int | float):
        pass


RocketCelestialTrackers: _RocketCelestialTrackers = _RocketCelestialTrackers()


class RocketCircuitHousing(_BaseStructure, _Error, _Power, _SettingW):
    _hash: int = 150135861

    @property
    def LineNumber(self) -> float:
        return DeviceLogicType(self, self._id, "LineNumber")

    @LineNumber.setter
    def LineNumber(self, value: int | float):
        pass


class _RocketCircuitHousings(_BaseStructures, _Errors, _Powers, _SettingWs):
    _hash: int = 150135861

    def __getitem__(self, name: str | int) -> "_RocketCircuitHousings":
        return _RocketCircuitHousings(name)

    @property
    def LineNumber(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "LineNumber", self._name_hash)

    @LineNumber.setter
    def LineNumber(self, value: int | float):
        pass


RocketCircuitHousings: _RocketCircuitHousings = _RocketCircuitHousings()


class RocketEngineTiny(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = 178472613


class _RocketEngineTinys(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 178472613

    def __getitem__(self, name: str | int) -> "_RocketEngineTinys":
        return _RocketEngineTinys(name)


RocketEngineTinys: _RocketEngineTinys = _RocketEngineTinys()


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

    @property
    def CompletionRatio(self) -> float:
        return DeviceLogicType(self, self._id, "CompletionRatio")


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

    def __getitem__(self, name: str | int) -> "_RocketManufactorys":
        return _RocketManufactorys(name)

    @property
    def CompletionRatio(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CompletionRatio", self._name_hash)


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

    @property
    def DrillCondition(self) -> float:
        return DeviceLogicType(self, self._id, "DrillCondition")


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

    def __getitem__(self, name: str | int) -> "_RocketMiners":
        return _RocketMiners(name)

    @property
    def DrillCondition(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "DrillCondition", self._name_hash)


RocketMiners: _RocketMiners = _RocketMiners()


class RocketScanner(_BaseStructure, _Error, _Lock, _Power):
    _hash: int = 2014252591


class _RocketScanners(_BaseStructures, _Errors, _Locks, _Powers):
    _hash: int = 2014252591

    def __getitem__(self, name: str | int) -> "_RocketScanners":
        return _RocketScanners(name)


RocketScanners: _RocketScanners = _RocketScanners()


class SDBHopper(_BaseStructure, _ClearMemory, _ImportCount, _Open):
    _hash: int = -1875856925


class _SDBHoppers(_BaseStructures, _ClearMemorys, _ImportCounts, _Opens):
    _hash: int = -1875856925

    def __getitem__(self, name: str | int) -> "_SDBHoppers":
        return _SDBHoppers(name)


SDBHoppers: _SDBHoppers = _SDBHoppers()


class SDBHopperAdvanced(_BaseStructure, _ClearMemory, _ImportCount, _Lock, _Open):
    _hash: int = 467225612


class _SDBHopperAdvanceds(
    _BaseStructures, _ClearMemorys, _ImportCounts, _Locks, _Opens
):
    _hash: int = 467225612

    def __getitem__(self, name: str | int) -> "_SDBHopperAdvanceds":
        return _SDBHopperAdvanceds(name)


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

    def __getitem__(self, name: str | int) -> "_SDBSilos":
        return _SDBSilos(name)


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

    @property
    def CompletionRatio(self) -> float:
        return DeviceLogicType(self, self._id, "CompletionRatio")


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

    def __getitem__(self, name: str | int) -> "_SecurityPrinters":
        return _SecurityPrinters(name)

    @property
    def CompletionRatio(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CompletionRatio", self._name_hash)


SecurityPrinters: _SecurityPrinters = _SecurityPrinters()


class ShelfMedium(_BaseStructure, _Open):
    _hash: int = 182006674


class _ShelfMediums(_BaseStructures, _Opens):
    _hash: int = 182006674

    def __getitem__(self, name: str | int) -> "_ShelfMediums":
        return _ShelfMediums(name)


ShelfMediums: _ShelfMediums = _ShelfMediums()


class ShortCornerLocker(_BaseStructure, _Lock, _Open):
    _hash: int = 1330754486


class _ShortCornerLockers(_BaseStructures, _Locks, _Opens):
    _hash: int = 1330754486

    def __getitem__(self, name: str | int) -> "_ShortCornerLockers":
        return _ShortCornerLockers(name)


ShortCornerLockers: _ShortCornerLockers = _ShortCornerLockers()


class ShortLocker(_BaseStructure, _Lock, _Open):
    _hash: int = -554553467


class _ShortLockers(_BaseStructures, _Locks, _Opens):
    _hash: int = -554553467

    def __getitem__(self, name: str | int) -> "_ShortLockers":
        return _ShortLockers(name)


ShortLockers: _ShortLockers = _ShortLockers()


class Shower(_BaseStructure, _Activate, _Maximum, _Open, _Ratio, _SettingW):
    _hash: int = -775128944


class _Showers(_BaseStructures, _Activates, _Maximums, _Opens, _Ratios, _SettingWs):
    _hash: int = -775128944

    def __getitem__(self, name: str | int) -> "_Showers":
        return _Showers(name)


Showers: _Showers = _Showers()


class ShowerPowered(_BaseStructure, _Error, _Open, _Power):
    _hash: int = -1081797501


class _ShowerPowereds(_BaseStructures, _Errors, _Opens, _Powers):
    _hash: int = -1081797501

    def __getitem__(self, name: str | int) -> "_ShowerPowereds":
        return _ShowerPowereds(name)


ShowerPowereds: _ShowerPowereds = _ShowerPowereds()


class Sleeper(
    _BaseStructure, _Activate, _Error, _Lock, _Maximum, _Open, _Power, _Ratio, _SettingW
):
    _hash: int = -1467449329

    @property
    def EntityState(self) -> float:
        return DeviceLogicType(self, self._id, "EntityState")


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

    def __getitem__(self, name: str | int) -> "_Sleepers":
        return _Sleepers(name)

    @property
    def EntityState(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "EntityState", self._name_hash)


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

    @property
    def EntityState(self) -> float:
        return DeviceLogicType(self, self._id, "EntityState")


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

    def __getitem__(self, name: str | int) -> "_SleeperLefts":
        return _SleeperLefts(name)

    @property
    def EntityState(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "EntityState", self._name_hash)


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

    @property
    def EntityState(self) -> float:
        return DeviceLogicType(self, self._id, "EntityState")


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

    def __getitem__(self, name: str | int) -> "_SleeperRights":
        return _SleeperRights(name)

    @property
    def EntityState(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "EntityState", self._name_hash)


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

    @property
    def EntityState(self) -> float:
        return DeviceLogicType(self, self._id, "EntityState")


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

    def __getitem__(self, name: str | int) -> "_SleeperVerticals":
        return _SleeperVerticals(name)

    @property
    def EntityState(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "EntityState", self._name_hash)


SleeperVerticals: _SleeperVerticals = _SleeperVerticals()


class LogicSlotReader(_BaseStructure, _Error, _Power, _SettingR):
    _hash: int = -767867194


class _LogicSlotReaders(_BaseStructures, _Errors, _Powers, _SettingRs):
    _hash: int = -767867194

    def __getitem__(self, name: str | int) -> "_LogicSlotReaders":
        return _LogicSlotReaders(name)


LogicSlotReaders: _LogicSlotReaders = _LogicSlotReaders()


class SmallDirectHeatExchangeGastoGas(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 1310303582


class _SmallDirectHeatExchangeGastoGass(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = 1310303582

    def __getitem__(self, name: str | int) -> "_SmallDirectHeatExchangeGastoGass":
        return _SmallDirectHeatExchangeGastoGass(name)


SmallDirectHeatExchangeGastoGass: _SmallDirectHeatExchangeGastoGass = (
    _SmallDirectHeatExchangeGastoGass()
)


class SmallDirectHeatExchangeLiquidtoGas(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 1825212016


class _SmallDirectHeatExchangeLiquidtoGass(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = 1825212016

    def __getitem__(self, name: str | int) -> "_SmallDirectHeatExchangeLiquidtoGass":
        return _SmallDirectHeatExchangeLiquidtoGass(name)


SmallDirectHeatExchangeLiquidtoGass: _SmallDirectHeatExchangeLiquidtoGass = (
    _SmallDirectHeatExchangeLiquidtoGass()
)


class SmallDirectHeatExchangeLiquidtoLiquid(
    _BaseStructure, _Maximum, _Ratio, _SettingW
):
    _hash: int = -507770416


class _SmallDirectHeatExchangeLiquidtoLiquids(
    _BaseStructures, _Maximums, _Ratios, _SettingWs
):
    _hash: int = -507770416

    def __getitem__(self, name: str | int) -> "_SmallDirectHeatExchangeLiquidtoLiquids":
        return _SmallDirectHeatExchangeLiquidtoLiquids(name)


SmallDirectHeatExchangeLiquidtoLiquids: _SmallDirectHeatExchangeLiquidtoLiquids = (
    _SmallDirectHeatExchangeLiquidtoLiquids()
)


class AirlockGate(_BaseStructure, _Idle, _Lock, _Mode, _Open, _Power, _SettingW):
    _hash: int = 1736080881


class _AirlockGates(
    _BaseStructures, _Idles, _Locks, _Modes, _Opens, _Powers, _SettingWs
):
    _hash: int = 1736080881

    def __getitem__(self, name: str | int) -> "_AirlockGates":
        return _AirlockGates(name)


AirlockGates: _AirlockGates = _AirlockGates()


class SmallSatelliteDish(
    _BaseStructure, _Activate, _Error, _Idle, _Power, _SettingW, _VerticalW
):
    _hash: int = -2138748650

    @property
    def BestContactFilter(self) -> float:
        return DeviceLogicType(self, self._id, "BestContactFilter")

    @BestContactFilter.setter
    def BestContactFilter(self, value: int | float):
        pass

    @property
    def ContactTypeId(self) -> float:
        return DeviceLogicType(self, self._id, "ContactTypeId")

    @property
    def InterrogationProgress(self) -> float:
        return DeviceLogicType(self, self._id, "InterrogationProgress")

    @property
    def MinimumWattsToContact(self) -> float:
        return DeviceLogicType(self, self._id, "MinimumWattsToContact")

    @property
    def SignalID(self) -> float:
        return DeviceLogicType(self, self._id, "SignalID")

    @property
    def SignalStrength(self) -> float:
        return DeviceLogicType(self, self._id, "SignalStrength")

    @property
    def SizeX(self) -> float:
        return DeviceLogicType(self, self._id, "SizeX")

    @property
    def SizeZ(self) -> float:
        return DeviceLogicType(self, self._id, "SizeZ")

    @property
    def TargetPadIndex(self) -> float:
        return DeviceLogicType(self, self._id, "TargetPadIndex")

    @TargetPadIndex.setter
    def TargetPadIndex(self, value: int | float):
        pass

    @property
    def WattsReachingContact(self) -> float:
        return DeviceLogicType(self, self._id, "WattsReachingContact")


class _SmallSatelliteDishs(
    _BaseStructures, _Activates, _Errors, _Idles, _Powers, _SettingWs, _VerticalWs
):
    _hash: int = -2138748650

    def __getitem__(self, name: str | int) -> "_SmallSatelliteDishs":
        return _SmallSatelliteDishs(name)

    @property
    def BestContactFilter(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "BestContactFilter", self._name_hash)

    @BestContactFilter.setter
    def BestContactFilter(self, value: int | float):
        pass

    @property
    def ContactTypeId(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "ContactTypeId", self._name_hash)

    @property
    def InterrogationProgress(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "InterrogationProgress", self._name_hash)

    @property
    def MinimumWattsToContact(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "MinimumWattsToContact", self._name_hash)

    @property
    def SignalID(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SignalID", self._name_hash)

    @property
    def SignalStrength(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SignalStrength", self._name_hash)

    @property
    def SizeX(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SizeX", self._name_hash)

    @property
    def SizeZ(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SizeZ", self._name_hash)

    @property
    def TargetPadIndex(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TargetPadIndex", self._name_hash)

    @TargetPadIndex.setter
    def TargetPadIndex(self, value: int | float):
        pass

    @property
    def WattsReachingContact(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "WattsReachingContact", self._name_hash)


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

    def __getitem__(self, name: str | int) -> "_TankSmalls":
        return _TankSmalls(name)


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

    def __getitem__(self, name: str | int) -> "_TankSmallAirs":
        return _TankSmallAirs(name)


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

    def __getitem__(self, name: str | int) -> "_TankSmallFuels":
        return _TankSmallFuels(name)


TankSmallFuels: _TankSmallFuels = _TankSmallFuels()


class SolarPanel(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = -2045627372


class _SolarPanels(_BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs):
    _hash: int = -2045627372

    def __getitem__(self, name: str | int) -> "_SolarPanels":
        return _SolarPanels(name)


SolarPanels: _SolarPanels = _SolarPanels()


class SolarPanel45(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = -1554349863


class _SolarPanel45s(_BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs):
    _hash: int = -1554349863

    def __getitem__(self, name: str | int) -> "_SolarPanel45s":
        return _SolarPanel45s(name)


SolarPanel45s: _SolarPanel45s = _SolarPanel45s()


class SolarPanelDual(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = -539224550


class _SolarPanelDuals(_BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs):
    _hash: int = -539224550

    def __getitem__(self, name: str | int) -> "_SolarPanelDuals":
        return _SolarPanelDuals(name)


SolarPanelDuals: _SolarPanelDuals = _SolarPanelDuals()


class SolarPanelFlat(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = 1968102968


class _SolarPanelFlats(_BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs):
    _hash: int = 1968102968

    def __getitem__(self, name: str | int) -> "_SolarPanelFlats":
        return _SolarPanelFlats(name)


SolarPanelFlats: _SolarPanelFlats = _SolarPanelFlats()


class SolarPanel45Reinforced(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = 930865127


class _SolarPanel45Reinforceds(
    _BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs
):
    _hash: int = 930865127

    def __getitem__(self, name: str | int) -> "_SolarPanel45Reinforceds":
        return _SolarPanel45Reinforceds(name)


SolarPanel45Reinforceds: _SolarPanel45Reinforceds = _SolarPanel45Reinforceds()


class SolarPanelDualReinforced(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = -1545574413


class _SolarPanelDualReinforceds(
    _BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs
):
    _hash: int = -1545574413

    def __getitem__(self, name: str | int) -> "_SolarPanelDualReinforceds":
        return _SolarPanelDualReinforceds(name)


SolarPanelDualReinforceds: _SolarPanelDualReinforceds = _SolarPanelDualReinforceds()


class SolarPanelFlatReinforced(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = 1697196770


class _SolarPanelFlatReinforceds(
    _BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs
):
    _hash: int = 1697196770

    def __getitem__(self, name: str | int) -> "_SolarPanelFlatReinforceds":
        return _SolarPanelFlatReinforceds(name)


SolarPanelFlatReinforceds: _SolarPanelFlatReinforceds = _SolarPanelFlatReinforceds()


class SolarPanelReinforced(_BaseStructure, _Charge, _Maximum, _Ratio, _VerticalW):
    _hash: int = -934345724


class _SolarPanelReinforceds(
    _BaseStructures, _Charges, _Maximums, _Ratios, _VerticalWs
):
    _hash: int = -934345724

    def __getitem__(self, name: str | int) -> "_SolarPanelReinforceds":
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

    @property
    def Output(self) -> float:
        return DeviceLogicType(self, self._id, "Output")

    @Output.setter
    def Output(self, value: int | float):
        pass


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

    def __getitem__(self, name: str | int) -> "_Sorters":
        return _Sorters(name)

    @property
    def Output(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Output", self._name_hash)

    @Output.setter
    def Output(self, value: int | float):
        pass


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

    @property
    def Output(self) -> float:
        return DeviceLogicType(self, self._id, "Output")

    @Output.setter
    def Output(self, value: int | float):
        pass


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

    def __getitem__(self, name: str | int) -> "_StackerReverses":
        return _StackerReverses(name)

    @property
    def Output(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Output", self._name_hash)

    @Output.setter
    def Output(self, value: int | float):
        pass


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

    @property
    def Output(self) -> float:
        return DeviceLogicType(self, self._id, "Output")

    @Output.setter
    def Output(self, value: int | float):
        pass


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

    def __getitem__(self, name: str | int) -> "_Stackers":
        return _Stackers(name)

    @property
    def Output(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Output", self._name_hash)

    @Output.setter
    def Output(self, value: int | float):
        pass


Stackers: _Stackers = _Stackers()


class Battery(_BaseStructure, _Charge, _Error, _Lock, _Maximum, _ModeR, _On, _Ratio):
    _hash: int = -400115994

    @property
    def Power(self) -> float:
        return DeviceLogicType(self, self._id, "Power")

    @property
    def PowerActual(self) -> float:
        return DeviceLogicType(self, self._id, "PowerActual")

    @property
    def PowerPotential(self) -> float:
        return DeviceLogicType(self, self._id, "PowerPotential")


class _Batterys(
    _BaseStructures, _Charges, _Errors, _Locks, _Maximums, _ModeRs, _Ons, _Ratios
):
    _hash: int = -400115994

    def __getitem__(self, name: str | int) -> "_Batterys":
        return _Batterys(name)

    @property
    def Power(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Power", self._name_hash)

    @property
    def PowerActual(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerActual", self._name_hash)

    @property
    def PowerPotential(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerPotential", self._name_hash)


Batterys: _Batterys = _Batterys()


class BatteryLarge(
    _BaseStructure, _Charge, _Error, _Lock, _Maximum, _ModeR, _On, _Ratio
):
    _hash: int = -1388288459

    @property
    def Power(self) -> float:
        return DeviceLogicType(self, self._id, "Power")

    @property
    def PowerActual(self) -> float:
        return DeviceLogicType(self, self._id, "PowerActual")

    @property
    def PowerPotential(self) -> float:
        return DeviceLogicType(self, self._id, "PowerPotential")


class _BatteryLarges(
    _BaseStructures, _Charges, _Errors, _Locks, _Maximums, _ModeRs, _Ons, _Ratios
):
    _hash: int = -1388288459

    def __getitem__(self, name: str | int) -> "_BatteryLarges":
        return _BatteryLarges(name)

    @property
    def Power(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Power", self._name_hash)

    @property
    def PowerActual(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerActual", self._name_hash)

    @property
    def PowerPotential(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerPotential", self._name_hash)


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

    @property
    def EnvironmentEfficiency(self) -> float:
        return DeviceLogicType(self, self._id, "EnvironmentEfficiency")

    @property
    def PowerGeneration(self) -> float:
        return DeviceLogicType(self, self._id, "PowerGeneration")

    @property
    def Volume(self) -> float:
        return DeviceLogicType(self, self._id, "Volume")

    @property
    def WorkingGasEfficiency(self) -> float:
        return DeviceLogicType(self, self._id, "WorkingGasEfficiency")


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

    def __getitem__(self, name: str | int) -> "_StirlingEngines":
        return _StirlingEngines(name)

    @property
    def EnvironmentEfficiency(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "EnvironmentEfficiency", self._name_hash)

    @property
    def PowerGeneration(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerGeneration", self._name_hash)

    @property
    def Volume(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Volume", self._name_hash)

    @property
    def WorkingGasEfficiency(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "WorkingGasEfficiency", self._name_hash)


StirlingEngines: _StirlingEngines = _StirlingEngines()


class SuitStorage(_BaseStructure, _Error, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = 255034731


class _SuitStorages(_BaseStructures, _Errors, _Maximums, _Powers, _Ratios, _SettingWs):
    _hash: int = 255034731

    def __getitem__(self, name: str | int) -> "_SuitStorages":
        return _SuitStorages(name)


SuitStorages: _SuitStorages = _SuitStorages()


class LogicSwitch2(_BaseStructure, _Lock, _Open, _SettingR):
    _hash: int = 321604921


class _LogicSwitch2s(_BaseStructures, _Locks, _Opens, _SettingRs):
    _hash: int = 321604921

    def __getitem__(self, name: str | int) -> "_LogicSwitch2s":
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

    def __getitem__(self, name: str | int) -> "_TankBigInsulateds":
        return _TankBigInsulateds(name)


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

    def __getitem__(self, name: str | int) -> "_TankSmallInsulateds":
        return _TankSmallInsulateds(name)


TankSmallInsulateds: _TankSmallInsulateds = _TankSmallInsulateds()


class GroundBasedTelescope(
    _BaseStructure, _Activate, _Error, _Lock, _Open, _Power, _VerticalW
):
    _hash: int = -619745681

    @property
    def AlignmentError(self) -> float:
        return DeviceLogicType(self, self._id, "AlignmentError")

    @property
    def CelestialHash(self) -> float:
        return DeviceLogicType(self, self._id, "CelestialHash")

    @property
    def CelestialParentHash(self) -> float:
        return DeviceLogicType(self, self._id, "CelestialParentHash")

    @property
    def DistanceAu(self) -> float:
        return DeviceLogicType(self, self._id, "DistanceAu")

    @property
    def DistanceKm(self) -> float:
        return DeviceLogicType(self, self._id, "DistanceKm")

    @property
    def Eccentricity(self) -> float:
        return DeviceLogicType(self, self._id, "Eccentricity")

    @property
    def HorizontalRatio(self) -> float:
        return DeviceLogicType(self, self._id, "HorizontalRatio")

    @HorizontalRatio.setter
    def HorizontalRatio(self, value: int | float):
        pass

    @property
    def Inclination(self) -> float:
        return DeviceLogicType(self, self._id, "Inclination")

    @property
    def OrbitPeriod(self) -> float:
        return DeviceLogicType(self, self._id, "OrbitPeriod")

    @property
    def SemiMajorAxis(self) -> float:
        return DeviceLogicType(self, self._id, "SemiMajorAxis")

    @property
    def TrueAnomaly(self) -> float:
        return DeviceLogicType(self, self._id, "TrueAnomaly")

    @property
    def VerticalRatio(self) -> float:
        return DeviceLogicType(self, self._id, "VerticalRatio")

    @VerticalRatio.setter
    def VerticalRatio(self, value: int | float):
        pass


class _GroundBasedTelescopes(
    _BaseStructures, _Activates, _Errors, _Locks, _Opens, _Powers, _VerticalWs
):
    _hash: int = -619745681

    def __getitem__(self, name: str | int) -> "_GroundBasedTelescopes":
        return _GroundBasedTelescopes(name)

    @property
    def AlignmentError(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "AlignmentError", self._name_hash)

    @property
    def CelestialHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CelestialHash", self._name_hash)

    @property
    def CelestialParentHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CelestialParentHash", self._name_hash)

    @property
    def DistanceAu(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "DistanceAu", self._name_hash)

    @property
    def DistanceKm(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "DistanceKm", self._name_hash)

    @property
    def Eccentricity(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Eccentricity", self._name_hash)

    @property
    def HorizontalRatio(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "HorizontalRatio", self._name_hash)

    @HorizontalRatio.setter
    def HorizontalRatio(self, value: int | float):
        pass

    @property
    def Inclination(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Inclination", self._name_hash)

    @property
    def OrbitPeriod(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "OrbitPeriod", self._name_hash)

    @property
    def SemiMajorAxis(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "SemiMajorAxis", self._name_hash)

    @property
    def TrueAnomaly(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "TrueAnomaly", self._name_hash)

    @property
    def VerticalRatio(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "VerticalRatio", self._name_hash)

    @VerticalRatio.setter
    def VerticalRatio(self, value: int | float):
        pass


GroundBasedTelescopes: _GroundBasedTelescopes = _GroundBasedTelescopes()


class TerraformingManufactory(
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
    _hash: int = 1549873866

    @property
    def CompletionRatio(self) -> float:
        return DeviceLogicType(self, self._id, "CompletionRatio")


class _TerraformingManufactorys(
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
    _hash: int = 1549873866

    def __getitem__(self, name: str | int) -> "_TerraformingManufactorys":
        return _TerraformingManufactorys(name)

    @property
    def CompletionRatio(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CompletionRatio", self._name_hash)


TerraformingManufactorys: _TerraformingManufactorys = _TerraformingManufactorys()


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

    @property
    def CompletionRatio(self) -> float:
        return DeviceLogicType(self, self._id, "CompletionRatio")


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

    def __getitem__(self, name: str | int) -> "_ToolManufactorys":
        return _ToolManufactorys(name)

    @property
    def CompletionRatio(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "CompletionRatio", self._name_hash)


ToolManufactorys: _ToolManufactorys = _ToolManufactorys()


class TraderWaypoint(_BaseStructure, _Error, _Power):
    _hash: int = 1570931620


class _TraderWaypoints(_BaseStructures, _Errors, _Powers):
    _hash: int = 1570931620

    def __getitem__(self, name: str | int) -> "_TraderWaypoints":
        return _TraderWaypoints(name)


TraderWaypoints: _TraderWaypoints = _TraderWaypoints()


class Transformer(_BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = -1423212473


class _Transformers(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -1423212473

    def __getitem__(self, name: str | int) -> "_Transformers":
        return _Transformers(name)


Transformers: _Transformers = _Transformers()


class TransformerMedium(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = -1065725831


class _TransformerMediums(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -1065725831

    def __getitem__(self, name: str | int) -> "_TransformerMediums":
        return _TransformerMediums(name)


TransformerMediums: _TransformerMediums = _TransformerMediums()


class TransformerSmall(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = -890946730


class _TransformerSmalls(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -890946730

    def __getitem__(self, name: str | int) -> "_TransformerSmalls":
        return _TransformerSmalls(name)


TransformerSmalls: _TransformerSmalls = _TransformerSmalls()


class TransformerMediumReversed(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = 833912764


class _TransformerMediumReverseds(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 833912764

    def __getitem__(self, name: str | int) -> "_TransformerMediumReverseds":
        return _TransformerMediumReverseds(name)


TransformerMediumReverseds: _TransformerMediumReverseds = _TransformerMediumReverseds()


class TransformerSmallReversed(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = 1054059374


class _TransformerSmallReverseds(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 1054059374

    def __getitem__(self, name: str | int) -> "_TransformerSmallReverseds":
        return _TransformerSmallReverseds(name)


TransformerSmallReverseds: _TransformerSmallReverseds = _TransformerSmallReverseds()


class RocketTransformerSmall(
    _BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW
):
    _hash: int = 518925193


class _RocketTransformerSmalls(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = 518925193

    def __getitem__(self, name: str | int) -> "_RocketTransformerSmalls":
        return _RocketTransformerSmalls(name)


RocketTransformerSmalls: _RocketTransformerSmalls = _RocketTransformerSmalls()


class PressurePlateLarge(_BaseStructure, _SettingR):
    _hash: int = -2008706143


class _PressurePlateLarges(_BaseStructures, _SettingRs):
    _hash: int = -2008706143

    def __getitem__(self, name: str | int) -> "_PressurePlateLarges":
        return _PressurePlateLarges(name)


PressurePlateLarges: _PressurePlateLarges = _PressurePlateLarges()


class PressurePlateMedium(_BaseStructure, _SettingR):
    _hash: int = 1269458680


class _PressurePlateMediums(_BaseStructures, _SettingRs):
    _hash: int = 1269458680

    def __getitem__(self, name: str | int) -> "_PressurePlateMediums":
        return _PressurePlateMediums(name)


PressurePlateMediums: _PressurePlateMediums = _PressurePlateMediums()


class PressurePlateSmall(_BaseStructure, _SettingR):
    _hash: int = -1536471028


class _PressurePlateSmalls(_BaseStructures, _SettingRs):
    _hash: int = -1536471028

    def __getitem__(self, name: str | int) -> "_PressurePlateSmalls":
        return _PressurePlateSmalls(name)


PressurePlateSmalls: _PressurePlateSmalls = _PressurePlateSmalls()


class TurbineGenerator(_BaseStructure):
    _hash: int = 1282191063

    @property
    def PowerGeneration(self) -> float:
        return DeviceLogicType(self, self._id, "PowerGeneration")


class _TurbineGenerators(_BaseStructures):
    _hash: int = 1282191063

    def __getitem__(self, name: str | int) -> "_TurbineGenerators":
        return _TurbineGenerators(name)

    @property
    def PowerGeneration(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerGeneration", self._name_hash)


TurbineGenerators: _TurbineGenerators = _TurbineGenerators()


class TurboVolumePump(
    _BaseStructure, _Error, _Lock, _Maximum, _Mode, _Power, _Ratio, _SettingW
):
    _hash: int = 1310794736


class _TurboVolumePumps(
    _BaseStructures, _Errors, _Locks, _Maximums, _Modes, _Powers, _Ratios, _SettingWs
):
    _hash: int = 1310794736

    def __getitem__(self, name: str | int) -> "_TurboVolumePumps":
        return _TurboVolumePumps(name)


TurboVolumePumps: _TurboVolumePumps = _TurboVolumePumps()


class LiquidTurboVolumePump(
    _BaseStructure, _Error, _Lock, _Maximum, _Mode, _Power, _Ratio, _SettingW
):
    _hash: int = -1051805505


class _LiquidTurboVolumePumps(
    _BaseStructures, _Errors, _Locks, _Maximums, _Modes, _Powers, _Ratios, _SettingWs
):
    _hash: int = -1051805505

    def __getitem__(self, name: str | int) -> "_LiquidTurboVolumePumps":
        return _LiquidTurboVolumePumps(name)


LiquidTurboVolumePumps: _LiquidTurboVolumePumps = _LiquidTurboVolumePumps()


class ChuteUmbilicalMale(_BaseStructure, _Error, _Lock, _ModeR, _Open, _Power):
    _hash: int = -958884053


class _ChuteUmbilicalMales(_BaseStructures, _Errors, _Locks, _ModeRs, _Opens, _Powers):
    _hash: int = -958884053

    def __getitem__(self, name: str | int) -> "_ChuteUmbilicalMales":
        return _ChuteUmbilicalMales(name)


ChuteUmbilicalMales: _ChuteUmbilicalMales = _ChuteUmbilicalMales()


class GasUmbilicalMale(
    _BaseStructure, _Error, _Lock, _Maximum, _ModeR, _Open, _Power, _Ratio, _SettingW
):
    _hash: int = -1814939203


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

    def __getitem__(self, name: str | int) -> "_GasUmbilicalMales":
        return _GasUmbilicalMales(name)


GasUmbilicalMales: _GasUmbilicalMales = _GasUmbilicalMales()


class LiquidUmbilicalMale(
    _BaseStructure, _Error, _Lock, _Maximum, _ModeR, _Open, _Power, _Ratio, _SettingW
):
    _hash: int = -1798420047


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

    def __getitem__(self, name: str | int) -> "_LiquidUmbilicalMales":
        return _LiquidUmbilicalMales(name)


LiquidUmbilicalMales: _LiquidUmbilicalMales = _LiquidUmbilicalMales()


class PowerUmbilicalMale(_BaseStructure, _Error, _Lock, _ModeR, _Open, _Power):
    _hash: int = 1529453938


class _PowerUmbilicalMales(_BaseStructures, _Errors, _Locks, _ModeRs, _Opens, _Powers):
    _hash: int = 1529453938

    def __getitem__(self, name: str | int) -> "_PowerUmbilicalMales":
        return _PowerUmbilicalMales(name)


PowerUmbilicalMales: _PowerUmbilicalMales = _PowerUmbilicalMales()


class GasUmbilicalFemale(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -1680477930


class _GasUmbilicalFemales(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = -1680477930

    def __getitem__(self, name: str | int) -> "_GasUmbilicalFemales":
        return _GasUmbilicalFemales(name)


GasUmbilicalFemales: _GasUmbilicalFemales = _GasUmbilicalFemales()


class LiquidUmbilicalFemale(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 1734723642


class _LiquidUmbilicalFemales(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = 1734723642

    def __getitem__(self, name: str | int) -> "_LiquidUmbilicalFemales":
        return _LiquidUmbilicalFemales(name)


LiquidUmbilicalFemales: _LiquidUmbilicalFemales = _LiquidUmbilicalFemales()


class GasUmbilicalFemaleSide(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = -648683847


class _GasUmbilicalFemaleSides(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = -648683847

    def __getitem__(self, name: str | int) -> "_GasUmbilicalFemaleSides":
        return _GasUmbilicalFemaleSides(name)


GasUmbilicalFemaleSides: _GasUmbilicalFemaleSides = _GasUmbilicalFemaleSides()


class LiquidUmbilicalFemaleSide(_BaseStructure, _Maximum, _Ratio, _SettingW):
    _hash: int = 1220870319


class _LiquidUmbilicalFemaleSides(_BaseStructures, _Maximums, _Ratios, _SettingWs):
    _hash: int = 1220870319

    def __getitem__(self, name: str | int) -> "_LiquidUmbilicalFemaleSides":
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

    @property
    def Output(self) -> float:
        return DeviceLogicType(self, self._id, "Output")

    @Output.setter
    def Output(self, value: int | float):
        pass


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

    def __getitem__(self, name: str | int) -> "_Unloaders":
        return _Unloaders(name)

    @property
    def Output(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "Output", self._name_hash)

    @Output.setter
    def Output(self, value: int | float):
        pass


Unloaders: _Unloaders = _Unloaders()


class UprightWindTurbine(_BaseStructure):
    _hash: int = 1622183451

    @property
    def PowerGeneration(self) -> float:
        return DeviceLogicType(self, self._id, "PowerGeneration")


class _UprightWindTurbines(_BaseStructures):
    _hash: int = 1622183451

    def __getitem__(self, name: str | int) -> "_UprightWindTurbines":
        return _UprightWindTurbines(name)

    @property
    def PowerGeneration(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerGeneration", self._name_hash)


UprightWindTurbines: _UprightWindTurbines = _UprightWindTurbines()


class Valve(_BaseStructure, _Maximum, _On, _Ratio, _SettingW):
    _hash: int = -692036078


class _Valves(_BaseStructures, _Maximums, _Ons, _Ratios, _SettingWs):
    _hash: int = -692036078

    def __getitem__(self, name: str | int) -> "_Valves":
        return _Valves(name)


Valves: _Valves = _Valves()


class LiquidValve(_BaseStructure, _Maximum, _On, _Ratio, _SettingW):
    _hash: int = 1849974453


class _LiquidValves(_BaseStructures, _Maximums, _Ons, _Ratios, _SettingWs):
    _hash: int = 1849974453

    def __getitem__(self, name: str | int) -> "_LiquidValves":
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

    @property
    def RequestHash(self) -> float:
        return DeviceLogicType(self, self._id, "RequestHash")

    @RequestHash.setter
    def RequestHash(self, value: int | float):
        pass


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

    def __getitem__(self, name: str | int) -> "_VendingMachines":
        return _VendingMachines(name)

    @property
    def RequestHash(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "RequestHash", self._name_hash)

    @RequestHash.setter
    def RequestHash(self, value: int | float):
        pass


VendingMachines: _VendingMachines = _VendingMachines()


class VolumePump(_BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = -321403609


class _VolumePumps(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -321403609

    def __getitem__(self, name: str | int) -> "_VolumePumps":
        return _VolumePumps(name)


VolumePumps: _VolumePumps = _VolumePumps()


class WallCooler(_BaseStructure, _Error, _Lock, _Maximum, _Power, _Ratio, _SettingW):
    _hash: int = -739292323


class _WallCoolers(
    _BaseStructures, _Errors, _Locks, _Maximums, _Powers, _Ratios, _SettingWs
):
    _hash: int = -739292323

    def __getitem__(self, name: str | int) -> "_WallCoolers":
        return _WallCoolers(name)


WallCoolers: _WallCoolers = _WallCoolers()


class WallHeater(_BaseStructure, _Error, _Lock, _Power):
    _hash: int = 24258244


class _WallHeaters(_BaseStructures, _Errors, _Locks, _Powers):
    _hash: int = 24258244

    def __getitem__(self, name: str | int) -> "_WallHeaters":
        return _WallHeaters(name)


WallHeaters: _WallHeaters = _WallHeaters()


class WallLight(_BaseStructure, _Lock, _Power):
    _hash: int = -1860064656


class _WallLights(_BaseStructures, _Locks, _Powers):
    _hash: int = -1860064656

    def __getitem__(self, name: str | int) -> "_WallLights":
        return _WallLights(name)


WallLights: _WallLights = _WallLights()


class WallLightBattery(_BaseStructure, _Lock, _Power):
    _hash: int = -1306415132


class _WallLightBatterys(_BaseStructures, _Locks, _Powers):
    _hash: int = -1306415132

    def __getitem__(self, name: str | int) -> "_WallLightBatterys":
        return _WallLightBatterys(name)


WallLightBatterys: _WallLightBatterys = _WallLightBatterys()


class LightLongAngled(_BaseStructure, _Lock, _Power):
    _hash: int = 1847265835


class _LightLongAngleds(_BaseStructures, _Locks, _Powers):
    _hash: int = 1847265835

    def __getitem__(self, name: str | int) -> "_LightLongAngleds":
        return _LightLongAngleds(name)


LightLongAngleds: _LightLongAngleds = _LightLongAngleds()


class LightLongWide(_BaseStructure, _Lock, _Power):
    _hash: int = 555215790


class _LightLongWides(_BaseStructures, _Locks, _Powers):
    _hash: int = 555215790

    def __getitem__(self, name: str | int) -> "_LightLongWides":
        return _LightLongWides(name)


LightLongWides: _LightLongWides = _LightLongWides()


class LightLong(_BaseStructure, _Lock, _Power):
    _hash: int = 797794350


class _LightLongs(_BaseStructures, _Locks, _Powers):
    _hash: int = 797794350

    def __getitem__(self, name: str | int) -> "_LightLongs":
        return _LightLongs(name)


LightLongs: _LightLongs = _LightLongs()


class WaterBottleFiller(_BaseStructure, _Activate, _Error):
    _hash: int = -1178961954


class _WaterBottleFillers(_BaseStructures, _Activates, _Errors):
    _hash: int = -1178961954

    def __getitem__(self, name: str | int) -> "_WaterBottleFillers":
        return _WaterBottleFillers(name)


WaterBottleFillers: _WaterBottleFillers = _WaterBottleFillers()


class WaterBottleFillerBottom(_BaseStructure, _Activate, _Error):
    _hash: int = 1433754995


class _WaterBottleFillerBottoms(_BaseStructures, _Activates, _Errors):
    _hash: int = 1433754995

    def __getitem__(self, name: str | int) -> "_WaterBottleFillerBottoms":
        return _WaterBottleFillerBottoms(name)


WaterBottleFillerBottoms: _WaterBottleFillerBottoms = _WaterBottleFillerBottoms()


class WaterPurifier(_BaseStructure, _ClearMemory, _Error, _ImportCount, _Lock, _Power):
    _hash: int = 887383294


class _WaterPurifiers(
    _BaseStructures, _ClearMemorys, _Errors, _ImportCounts, _Locks, _Powers
):
    _hash: int = 887383294

    def __getitem__(self, name: str | int) -> "_WaterPurifiers":
        return _WaterPurifiers(name)


WaterPurifiers: _WaterPurifiers = _WaterPurifiers()


class WaterBottleFillerPoweredBottom(_BaseStructure, _Activate, _Error, _Power):
    _hash: int = 1986658780


class _WaterBottleFillerPoweredBottoms(_BaseStructures, _Activates, _Errors, _Powers):
    _hash: int = 1986658780

    def __getitem__(self, name: str | int) -> "_WaterBottleFillerPoweredBottoms":
        return _WaterBottleFillerPoweredBottoms(name)


WaterBottleFillerPoweredBottoms: _WaterBottleFillerPoweredBottoms = (
    _WaterBottleFillerPoweredBottoms()
)


class WaterBottleFillerPowered(_BaseStructure, _Activate, _Error, _Power):
    _hash: int = -756587791


class _WaterBottleFillerPowereds(_BaseStructures, _Activates, _Errors, _Powers):
    _hash: int = -756587791

    def __getitem__(self, name: str | int) -> "_WaterBottleFillerPowereds":
        return _WaterBottleFillerPowereds(name)


WaterBottleFillerPowereds: _WaterBottleFillerPowereds = _WaterBottleFillerPowereds()


class WeatherStation(_BaseStructure, _Activate, _Error, _Lock, _ModeR, _Power):
    _hash: int = 1997212478

    @property
    def NextWeatherEventTime(self) -> float:
        return DeviceLogicType(self, self._id, "NextWeatherEventTime")


class _WeatherStations(_BaseStructures, _Activates, _Errors, _Locks, _ModeRs, _Powers):
    _hash: int = 1997212478

    def __getitem__(self, name: str | int) -> "_WeatherStations":
        return _WeatherStations(name)

    @property
    def NextWeatherEventTime(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "NextWeatherEventTime", self._name_hash)


WeatherStations: _WeatherStations = _WeatherStations()


class WindTurbine(_BaseStructure):
    _hash: int = -2082355173

    @property
    def PowerGeneration(self) -> float:
        return DeviceLogicType(self, self._id, "PowerGeneration")


class _WindTurbines(_BaseStructures):
    _hash: int = -2082355173

    def __getitem__(self, name: str | int) -> "_WindTurbines":
        return _WindTurbines(name)

    @property
    def PowerGeneration(self) -> DevicesLogicType:
        return DevicesLogicType(self._hash, "PowerGeneration", self._name_hash)


WindTurbines: _WindTurbines = _WindTurbines()
