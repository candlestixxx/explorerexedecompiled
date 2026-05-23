# Changelog

All notable changes to this project will be documented in this file.

## [0.1.6] - Headless Disassembler Containerization
- Created a `Dockerfile` configuring OpenJDK 17 and Ghidra 11.0.
- Established the base environment for reproducible Phase 2 headless decompilation tasks.
- Updated `TODO.md` outlining the next steps for `scripts/decompile.py`.

## [0.1.5] - Phase 2 Transition
- Updated `TODO.md` to formally close out Phase 1 initialization.
- Added tasks for Phase 2: Dockerizing Ghidra/RetDec and implementing `scripts/decompile.py`.

## [0.1.4] - Phase 1 Pipeline Orchestration
- Created `scripts/orchestrate.py` to link `ingest_binary.py` and `fetch_pdb.py` into a cohesive Phase 1 workflow.
- Updated `TODO.md` to reflect the completed Phase 1 orchestration task.

## [0.1.3] - PE File Parsing & Binary Ingestion
- Implemented `pefile` integration in `scripts/ingest_binary.py` to extract CodeView Debug Directories.
- Script now computes SHA256 hashes and dynamically returns the GUID/Age string needed for PDB fetching.
- Added `requirements.txt` to track `pefile` and future Python dependencies.

## [0.1.2] - Microsoft Symbol Server Integration
- Implemented actual HTTP GET requests in `scripts/fetch_pdb.py` to retrieve PDBs from Microsoft Symbol Server using `urllib.request`.
- Updated `TODO.md` to reflect implementation status.
- Validated error handling against missing dummy PDB records.

## [0.1.1] - Scaffolding Pipeline
- Created `src/` and `include/` directories to establish the C++ project structure.
- Scaffolded pipeline python scripts under `scripts/` (`fetch_pdb.py`, `ingest_binary.py`, `decompile.py`).
- Added C/C++ decompilation coding guidelines to `C_CPP_GUIDELINES.md`.
- Updated `TODO.md` to specify targeting Windows 10 Build 19045 for the decompilation phase.

## [0.1.0] - Initial Setup
- Initialized core structural documentation (ROADMAP.md, TODO.md, VISION.md, MEMORY.md, DEPLOY.md, IDEAS.md, VERSION.md, HANDOFF.md).
- Prepared repository for AI agent workflow according to guidelines.