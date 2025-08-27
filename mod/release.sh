#! /bin/bash
set -e

export STATIONEERS_DLL_DIR=~/.sa/Stationeers/rocketstation_Data/Managed/
MOD_DIR=`pwd`

~/.local/share/nvim/mason/bin/csharpier format PyTrapIC.cs
xmllint --format PyTrapIC.csproj -o PyTrapIC.csproj
dotnet build -c Release PyTrapIC.csproj

rm -rf dist
mkdir -p dist/pytrapic

cp bin/Release/net46/PyTrapIC.dll dist/pytrapic/

rm -rf venv
python -m venv venv
source venv/bin/activate
pip install ..

cd venv/lib/python3*/site-packages
zip -r $MOD_DIR/dist/pytrapic/pytrapic_python_modules.zip antlr4 astroid luaparser multimethod stationeers_pytrapic
                
cd $MOD_DIR/dist/
zip -r PyTrapIC.zip pytrapic
rm -r $MOD_DIR/dist/pytrapic
