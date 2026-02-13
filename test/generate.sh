#!/bin/bash
set -e

python test_cases.py &
python test_libraries.py

wait
