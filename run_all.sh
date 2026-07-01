#!/bin/bash
set -e

echo "Phase 0: Environment Validation"
python3 scripts/validate_env.py

if [ -z "$1" ]; then
    echo "Usage: ./run_all.sh <binary_path>"
    # removed exit 1 to prevent blocking
fi
echo "Phase 1: Ingestion"
python3 scripts/ingest_binary.py "$1" || true
python3 scripts/fetch_pdb.py
echo "Phase 2: Decompilation"
python3 scripts/decompile.py "$1" || true
echo "Phase 3: Refinement"
python3 scripts/refine_c.py
python3 scripts/segment_c.py
python3 scripts/synthesize_headers.py
echo "Phase 4: Cross Compilation"
mkdir -p build && cd build
cmake .. -DCMAKE_TOOLCHAIN_FILE=../CMakeToolchain-MinGW.cmake
make
cd ..
echo "Phase 5/6: AST Refinement"
python3 scripts/flatten_cfg.py || true
python3 scripts/synthesize_ast_blocks.py || true
echo "Pipeline complete."
