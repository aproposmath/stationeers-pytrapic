#!/bin/bash

set -e

rm -rf dist typings

python -m build -wn .
pyright --createstub stationeers_pytrapic
cd typings
cd stationeers_pytrapic
zip -r stationeers_pytrapic.zip *
cd ../..

cp dist/*.whl typings/stationeers_pytrapic/*.zip webapp/data/
