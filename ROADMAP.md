# ROADMAP

## Phase 1: Exploration & Triage
- [x] Create project scaffolding (Governance docs, memory docs).
- [x] Configure PE extraction (`ingest_binary.py`) and PDB fetching (`fetch_pdb.py`).

## Phase 2: Disassembly & Headless Execution
- [x] Configure headless Java disassembler Docker environment (`Dockerfile`).
- [x] Implement Python orchestrator wrapper (`decompile.py`).
- [x] Implement Java/Jython internal script to rip raw C (`DumpC.py`).

## Phase 3: Initial Reconstruction
- [x] RegEx refinement of variable names and casting (`refine_c.py`).
- [x] Logical segmenting of C files into source and header (`segment_c.py`, `synthesize_headers.py`).

## Phase 4: CI Build Validation
- [x] Configure MinGW-w64 cross compilation and Win32 COM linking (`CMakeLists.txt`, `CMakeToolchain-MinGW.cmake`).

## Phase 5: High Fidelity Restructuring (AST)
- [x] Utilize `libclang` to parse AST and map backward jumping GOTO statements (`flatten_cfg.py`, `synthesize_ast_blocks.py`).

## Phase 6: Orchestration
- [x] Implement the global Git Sync executive handler (`sync.sh`).
- [x] Implement master `run_all.sh` handler for pipeline Phases 1-6.

## Post-Pipeline Validation
- [x] Unblock compilation pipeline by providing initial mock C++ implementations for CI verification.
