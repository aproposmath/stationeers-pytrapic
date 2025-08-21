#! /bin/bash
set -e

export STATIONEERS_DIR=~/.sa/Stationeers
 ~/.local/share/nvim/mason/bin/csharpier format PyTrapIC.cs
dotnet build -c Release PyTrapIC.csproj
