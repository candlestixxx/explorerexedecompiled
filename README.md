# Explorer.exe Decompilation Pipeline

An automated 6-phase pipeline utilizing Python, Jython, Docker, CMake, and `libclang` to autonomously extract, decompile, refine, and restructure the Windows `explorer.exe` executable into compilable high-fidelity C++.

## Project Status
**Currently blocked**: The pipeline orchestrator believes that `explorer.exe` has been successfully decompiled, but the actual output `.cpp` files are completely missing from the environment. Compilation cannot proceed until they are uploaded.

## Compilation Instructions
Once the decompiled files are placed in `src/` and `include/`, you can cross-compile them using the provided MinGW-w64 CMake configuration:

```bash
mkdir -p build && cd build
cmake .. -DCMAKE_TOOLCHAIN_FILE=../CMakeToolchain-MinGW.cmake
make
```

## Pipeline Architecture
- Phase 1: Ingestion & Symbol Fetching (`pefile`, `urllib`)
- Phase 2: Dockerized Headless Decompilation (Ghidra, OpenJDK 17)
- Phase 3: Regex Refinement and Namespace Segmentation
- Phase 4: CI Verification and Cross-Compilation (MinGW-w64, CMake)
- Phase 5: AST Flatting (libclang `GOTO_STMT` recovery)
- Phase 6: Block Synthesis (Rewriting goto to native while loops)

## Usage
Provide the binary:
`./run_all.sh explorer.exe`

A visual interface simulating the backend workflow is available in `test_frontend.html`.
