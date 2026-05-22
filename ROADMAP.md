# ROADMAP

## Major Structural Milestones

### Phase 1: Environment Setup & Binary Ingestion
* Establish tools: headless disassembler, RetDec, or custom LLM decompilation pipelines.
* Retrieve target `explorer.exe` binary.
* Query Microsoft Symbol Server for `.pdb` file using GUID/Age hash.
* Apply symbols to recover original names, structures, and variables.

### Phase 2: Automated Disassembly & Control Flow Analysis
* Load binary into headless disassembler for static analysis.
* Map basic blocks, conditional jumps, and function boundaries (CFG Reconstruction).
* Isolate compiler-inserted boilerplate (security cookies, SEH, CRT).
* Document dynamically resolved APIs (GetProcAddress, Indirect Call Tables).

### Phase 3: Decompilation & Intermediate Representation (IR)
* Generate AST or C-like pseudocode.
* Infer complex Windows data types (LSTATUS, PIDLIST_ABSOLUTE, HRESULT) using PDB symbols.
* Infer local variable structures via offset access patterns.

### Phase 4: C++ Refactoring & Legibility Optimization
* Rename auto-generated variables contextually.
* Reconstruct idioms (loops, unflatten nested if-else).
* Convert procedural Win32 pointer arithmetic to modern C++ class-based structures (COM).
* Add high-level inline documentation.

### Phase 5: Artifact Generation & Structuring
* Segment decompiled output into logical modules (ShellWindow.cpp, FileBrowserHelpers.cpp).
* Synthesize header files (.h/.hpp) for structures, enums, and classes.
* Complete CI/CD and commit processes.