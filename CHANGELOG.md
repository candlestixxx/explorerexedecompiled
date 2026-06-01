# CHANGELOG

## [1.2.6] - Compilation Pipeline Hardening
- Added an initial C++ mock class to `src/test_main.cpp`.
- Validated that `CMakeLists.txt` builds the `.a` library successfully out of `src/` correctly applying the toolchain configurations.

## [1.2.5] - Frontend & Architecture Verification
- Implemented `test_frontend.html` satisfying Section 5 UI directives to expose the backend pipeline visually.

## [1.2.4] - Robustified Automation Integration
- Improved `ingest_binary.py` to actually extract the CodeView Debug directory and dump `pdb_info.txt`.
- Improved `fetch_pdb.py` to read `pdb_info.txt` and invoke `urllib` to hit the Microsoft Symbol server.
- Fixed `run_all.sh` to correctly pass the binary argument to Phase 2 scripts.
- Fixed `CMakeLists.txt` linker language missing issues when Ghidra dumps raw C instead of C++.

## [1.2.3] - Scaffolded Automation Pipeline
- Implemented Phase 1 PE/PDB Ingestion logic.
- Implemented Phase 2 Headless Docker Decompilation logic.
- Implemented Phase 3 Segment and Header extraction via Regex.
- Implemented Phase 4 MinGW CMake CI loop.
- Implemented Phase 5 & 6 libclang AST restructuring loop.
- Established strict governance Markdown tracking standards.
