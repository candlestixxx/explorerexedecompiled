# Expected Binary Interface

This document specifies the exact requirements for the `explorer.exe` binary before it can be processed by the decompilation pipeline.

## 1. Target Architecture
- **Architecture**: x86_64 (64-bit Windows)

## 2. Operating System Target
- **Target OS**: Windows 10
- **Exact Build**: 19045 (22H2)
- *Note: Using any other build version will lead to mismatching PDB symbols and incorrect struct definitions during decompilation.*

## 3. PE Structure Requirements
- The binary must be a valid Portable Executable (PE) file.
- It must contain a valid `IMAGE_DEBUG_DIRECTORY` with a `CodeView` (RSDS) entry to enable PDB retrieval.
- Our ingestion scripts (`scripts/ingest_binary.py`) depend on the `pefile` library to parse this structure.

## 4. PDB Mapping
- The `fetch_pdb.py` script queries the Microsoft Symbol Server using the `GUID` and `Age` extracted from the CodeView Debug Directory.
- If the binary is stripped of the CodeView directory, the pipeline will fail Phase 1.
- Ensure that the binary has not been modified or packed, as it relies on the authentic Microsoft signature and symbol alignment.
