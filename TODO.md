# TODO

## Immediate Tasks
- [x] Determine the exact target build version of `explorer.exe` to reverse. (Target: Windows 10 Build 19045)
- [x] Set up the basic project structure for C++ output. (Created `src/` and `include/` directories)
- [x] Implement a script to query the Microsoft Symbol Server for PDB retrieval. (Implemented HTTP requests in `scripts/fetch_pdb.py`)
- [x] Select and configure the headless disassembler tooling (e.g., Ghidra or IDA Pro). (Deferred to Phase 2)
- [x] Write the first Python/Bash scripts for initial headless disassembly runs. (Implemented `scripts/ingest_binary.py` to extract PE hashes and `scripts/decompile.py` scaffold)
- [x] Create a master orchestrator script to link binary ingestion and PDB fetching into a Phase 1 pipeline. (Implemented `scripts/orchestrate.py`)
- [ ] Phase 2: Containerize a headless disassembler (Ghidra/RetDec) via Docker to run `scripts/decompile.py` consistently.
- [ ] Phase 2: Refactor `scripts/decompile.py` to execute analysis and dump Intermediate Representation (IR) / ASTs.
- [x] Draft coding guidelines for the generated C++ (naming conventions, documentation rules). (Created `C_CPP_GUIDELINES.md`)