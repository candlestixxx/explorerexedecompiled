#!/bin/bash
set -e
echo "Running Python Unit Tests..."
./run_tests.sh

echo "Checking for source files..."
if [ $(find src/ -name "*.cpp" | wc -l) -le 1 ]; then
    echo "ERROR: Decompiled source files are missing from the src/ directory!"
    echo "Only mock testing files exist. Aborting compilation."
else
    echo "Files found. Proceeding with compilation..."
    cd build
    make clean
    make
    echo "Compilation Successful."
fi
