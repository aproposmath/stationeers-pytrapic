#! /bin/bash
set -e


dotnet build -c Release PyTrapIC.csproj

rm -rf pytrapic PyTrapIC.zip
mkdir -p pytrapic

cp bin/Release/net48/PyTrapIC.dll pytrapic/
cp -r About pytrapic/
zip -r PyTrapIC.zip ./pytrapic
