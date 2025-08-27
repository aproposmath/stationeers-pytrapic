#! /bin/bash
set -e

export STATIONEERS_DLL_DIR=~/.sa/Stationeers/rocketstation_Data/Managed/
export PYTRAPIC_VERSION=`./get_version.py`
MOD_DIR=`pwd`
DIST_DIR=/tmp/pytrapic_dist

~/.local/share/nvim/mason/bin/csharpier format PyTrapIC.cs
xmllint --format PyTrapIC.csproj -o PyTrapIC.csproj
dotnet build -c Release PyTrapIC.csproj

rm -rf $DIST_DIR
mkdir -p $DIST_DIR/pytrapic

cp bin/Release/net46/PyTrapIC.dll $DIST_DIR/pytrapic/

cd $DIST_DIR

rm -rf venv
python -m venv venv
source venv/bin/activate
pip install $MOD_DIR/..

cd venv/lib/python3*/site-packages
zip -r $DIST_DIR/pytrapic/pytrapic_python_modules.zip antlr4 astroid luaparser multimethod stationeers_pytrapic
                
cd $DIST_DIR
echo $PYTRAPIC_VERSION > pytrapic/version.txt
zip -r PyTrapIC.zip pytrapic

cd $MOD_DIR
cp $DIST_DIR/PyTrapIC.zip PyTrapIC-$PYTRAPIC_VERSION.zip
