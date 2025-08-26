#! /bin/bash
set -e

export STATIONEERS_DLL_DIR=~/.sa/Stationeers/rocketstation_Data/Managed/
~/.local/share/nvim/mason/bin/csharpier format PyTrapIC.cs
xmllint --format PyTrapIC.csproj -o PyTrapIC.csproj
dotnet build -c Debug PyTrapIC.csproj
