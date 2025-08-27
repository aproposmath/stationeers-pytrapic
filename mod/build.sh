#! /bin/bash
set -e

export PYTRAPIC_VERSION=`./get_version.py`
export STATIONEERS_DLL_DIR=~/.sa/Stationeers/rocketstation_Data/Managed/
~/.local/share/nvim/mason/bin/csharpier format PyTrapIC.cs
xmllint --format PyTrapIC.csproj -o PyTrapIC.csproj
dotnet build -c Debug PyTrapIC.csproj
