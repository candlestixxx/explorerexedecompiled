# Changelog

All notable changes to this project will be documented in this file.

## [0.1.12] - Phase 4 CMake Build System
- Implemented `CMakeLists.txt` at the root of the repository to establish the Phase 4 build system.
- Configured CMake to compile the auto-segmented `src/` and `include/` files into a static library for syntax and linking verification.
- Updated `TODO.md` to track build system completion.

## [0.1.11] - Phase 3 Header Synthesis and Closure
- Implemented `scripts/synthesize_headers.py` to auto-generate `.h` files from segmented C++ source code.
- Successfully closed out all Phase 3 tasks.
- Updated `TODO.md` to map out Phase 4 requirements involving build systems and compilation verification.

## [0.1.10] - Phase 3 Modular Segmentation
- Implemented `scripts/segment_c.py` to logically split the refined monolithic C output into domain-specific C++ files within the `src/` directory.
- Updated `TODO.md` to define the final objective of Phase 3 (Header Synthesis).

## [0.1.9] - Phase 3 Pseudocode Refinement
- Added `scripts/refine_c.py` to post-process Ghidra's monolithic C output using heuristic regex parsing.
- Refinement enforces modern C++ casts, normalizes auto-generated variable names, and explicitly flags un-flattened `goto` statements.

## [0.1.8] - Ghidra IR Extraction Script
- Authored `scripts/DumpC.py`, a Jython script utilizing Ghidra's `DecompInterface` to extract C pseudocode.
- Updated `scripts/decompile.py` to dynamically mount the script directory and invoke `DumpC.py` post-analysis.
- Marked Phase 2 as complete in `TODO.md` and transitioned focus to Phase 3 goals.

## [0.1.7] - Containerized Decompilation Invocation
- Refactored `scripts/decompile.py` to invoke the `explorer-decompiler` Docker container via Python's `subprocess`.
- Added logic to map binary paths to Docker volumes for seamless analysis.
- Updated `TODO.md` to reflect completion of the decompilation invocation setup.

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