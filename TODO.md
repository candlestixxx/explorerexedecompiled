# TODO

## Immediate Tasks
- [x] Determine the exact target build version of `explorer.exe` to reverse. (Target: Windows 10 Build 19045)
- [x] Set up the basic project structure for C++ output. (Created `src/` and `include/` directories)
- [x] Implement a script to query the Microsoft Symbol Server for PDB retrieval. (Implemented HTTP requests in `scripts/fetch_pdb.py`)
- [ ] Select and configure the headless disassembler tooling (e.g., Ghidra or IDA Pro).
- [x] Write the first Python/Bash scripts for initial headless disassembly runs. (Implemented `scripts/ingest_binary.py` to extract PE hashes and `scripts/decompile.py` scaffold)
- [ ] Investigate options for AST generation based on assembly output.
- [x] Draft coding guidelines for the generated C++ (naming conventions, documentation rules). (Created `C_CPP_GUIDELINES.md`)