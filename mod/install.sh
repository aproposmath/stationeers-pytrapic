#!/bin/bash

DIR=`pwd`
rm -f *.zip
set -e
./release.sh

cd ~/.sa/Stationeers/BepInEx/plugins/
rm -rf pytrapic
unzip $DIR/*.zip
