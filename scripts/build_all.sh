#!/bin/bash

set -e

rm -rf dist typings

cd scripts
python build_enums.py
python ../src/stationeers_pytrapic/build_types.py Stationpedia.json
python build_intrinsics.py
cd ..

black src

python -m build -wn .
pyright --createstub stationeers_pytrapic
cd typings
cd stationeers_pytrapic
zip -r stationeers_pytrapic.zip *
cd ../..

cp dist/*.whl typings/stationeers_pytrapic/*.zip webapp/data/
