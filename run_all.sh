#!/usr/bin/env bash

# run_all.sh
# Master Execution Pipeline for explorerexedecompiled

set -e

# Default directories and files
BINARY_PATH=$1
if [ -z "$BINARY_PATH" ]; then
    echo "Usage: ./run_all.sh <path_to_explorer_exe>"
    exit 1
fi

PDB_DIR="pdbs"
DECOMPILED_DIR="decompiled"
MONOLITHIC_C="$DECOMPILED_DIR/explorer.exe_decompiled.c"
REFINED_C="$DECOMPILED_DIR/explorer.exe_refined.c"
SRC_DIR="src"
INCLUDE_DIR="include"

# Ensure we're in the repository root
cd "$(dirname "$0")"
export PYTHONPATH=scripts

echo "=========================================="
echo " Starting Full Decompilation Pipeline"
echo " Target Binary: $BINARY_PATH"
echo "=========================================="

# PHASE 1: Ingest & Fetch PDB
echo ""
echo "[Phase 1] Ingesting Binary & Fetching PDB..."
python3 scripts/orchestrate.py "$BINARY_PATH" "$PDB_DIR"

# PHASE 2: Headless Decompilation (Requires Docker)
echo ""
echo "[Phase 2] Running Headless Decompilation via Ghidra Container..."
python3 scripts/decompile.py "$BINARY_PATH" "$DECOMPILED_DIR"

# PHASE 3: Pseudocode Refinement & Modular Segmentation
echo ""
echo "[Phase 3] Refining C Pseudocode..."
python3 scripts/refine_c.py "$MONOLITHIC_C" "$REFINED_C"

echo "[Phase 3] Segmenting into C++ Modules..."
python3 scripts/segment_c.py "$REFINED_C" "$SRC_DIR"

echo "[Phase 3] Synthesizing C++ Headers..."
python3 scripts/synthesize_headers.py "$SRC_DIR" "$INCLUDE_DIR"

# PHASE 4: Compilability & Verification
echo ""
echo "[Phase 4] Verifying Build Syntax via CMake..."
if [ -x "$(command -v x86_64-w64-mingw32-g++)" ]; then
    echo "Detected MinGW cross-compiler. Using CMakeToolchain-MinGW.cmake"
    cmake -DCMAKE_TOOLCHAIN_FILE=CMakeToolchain-MinGW.cmake .
else
    echo "Using default host compiler for baseline verification."
    cmake .
fi

make

echo ""
echo "=========================================="
echo " Pipeline Execution Completed Successfully!"
echo " Source artifacts are located in: ./$SRC_DIR and ./$INCLUDE_DIR"
echo "=========================================="
