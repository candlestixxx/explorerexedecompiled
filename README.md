# Explorer.exe Decompilation Pipeline

An automated 6-phase pipeline utilizing Python, Jython, Docker, CMake, and `libclang` to autonomously extract, decompile, refine, and restructure the Windows `explorer.exe` executable into compilable high-fidelity C++.

## Project Status
**Currently blocked**: Awaiting human upload of `explorer.exe` (Windows 10 Build 19045).

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
