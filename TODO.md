# TODO

## Immediate Tasks
- [x] Determine the exact target build version of `explorer.exe` to reverse. (Target: Windows 10 Build 19045)
- [x] Set up the basic project structure for C++ output. (Created `src/` and `include/` directories)
- [x] Implement a script to query the Microsoft Symbol Server for PDB retrieval. (Implemented HTTP requests in `scripts/fetch_pdb.py`)
- [x] Select and configure the headless disassembler tooling (e.g., Ghidra or IDA Pro). (Deferred to Phase 2)
- [x] Write the first Python/Bash scripts for initial headless disassembly runs. (Implemented `scripts/ingest_binary.py` to extract PE hashes and `scripts/decompile.py` scaffold)
- [x] Create a master orchestrator script to link binary ingestion and PDB fetching into a Phase 1 pipeline. (Implemented `scripts/orchestrate.py`)
- [x] Phase 2: Containerize a headless disassembler (Ghidra/RetDec) via Docker to run `scripts/decompile.py` consistently. (Created `Dockerfile` for Ghidra)
- [x] Phase 2: Refactor `scripts/decompile.py` to execute headless analysis via Docker and dump Intermediate Representation (IR) / ASTs. (Implemented Docker invocation in `scripts/decompile.py` and `scripts/DumpC.py`)
- [x] Phase 3: Develop AST parsing logic to read the dumped C pseudocode from `scripts/DumpC.py` and refine variable naming. (Implemented heuristic regex parsing in `scripts/refine_c.py`)
- [x] Phase 3: Develop logic to split the monolithic C pseudocode into logical `src/` modules. (Implemented in `scripts/segment_c.py`)
- [x] Phase 3: Implement C++ structural synthesis (header generation) into `include/` based on inferred types from the decompiled logic. (Implemented in `scripts/synthesize_headers.py`)
- [x] Phase 4: Implement a build system (CMake/Makefile) to verify the compilability of the reconstructed C++ source code. (Created `CMakeLists.txt`)
- [x] Phase 4: Identify missing OS headers or libraries necessary to resolve `windows.h` and COM objects during the CI verification process. (Implemented MinGW toolchain linkage via `CMakeToolchain-MinGW.cmake`)
- [x] Draft coding guidelines for the generated C++ (naming conventions, documentation rules). (Created `C_CPP_GUIDELINES.md`)