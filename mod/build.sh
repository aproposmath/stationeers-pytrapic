#! /bin/bash
set -e

# ~/.local/share/nvim/mason/bin/csharpier format *.cs
# xmllint --format PyTrapIC.csproj -o PyTrapIC.csproj
# xmllint --format PyTrapIC.props -o PyTrapIC.props
dotnet build -c Debug PyTrapIC.csproj

cp bin/Debug/net46/PyTrapIC.dll ~/.sa/Stationeers/BepInEx/scripts/
