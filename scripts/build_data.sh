#!/bin/bash

set -e

rm -rf dist typings webapp/data/*

python -m build -wn .
pyright --createstub stationeers_pytrapic
cd typings
cd stationeers_pytrapic
zip -r stationeers_pytrapic.zip *
cd ../..

cp typings/stationeers_pytrapic/*.zip webapp/data/
cp dist/*.whl webapp/data/stationeers_pytrapic-0.0.1-py3-none-any.whl
