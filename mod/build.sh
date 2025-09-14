#! /bin/bash
set -e

export PYTRAPIC_VERSION=`./get_version.py`
export STATIONEERS_DLL_DIR=~/.sa/Stationeers/rocketstation_Data/Managed/
~/.local/share/nvim/mason/bin/csharpier format *.cs
xmllint --format PyTrapIC.csproj -o PyTrapIC.csproj
dotnet build -c Debug PyTrapIC.csproj

cp bin/Debug/net46/PyTrapIC.dll ~/.sa/Stationeers/BepInEx/plugins/pytrapic/
