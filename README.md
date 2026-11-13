# Explorer.exe Decompilation Pipeline

An automated 6-phase pipeline (Python, Jython, Docker, CMake, `libclang`)
intended to extract, decompile, refine, and restructure the Windows
`explorer.exe` executable into compilable C++.

## Status

**Experimental — blocked.** Per the repo's own status note, the pipeline
orchestrator reports `explorer.exe` as successfully decompiled, but the
actual output `.cpp` files are missing from the environment. Compilation
cannot proceed until decompiled files are placed in `src/` and `include/`.

Version: 1.2.33. Last activity: 2026-11-12 (merge of a Jules branch hardening
the build and decompilation pipeline). Recent work has focused on end-to-end
pipeline unblocking, the MinGW toolchain, and Ghidra typing refinement.

## What's working

- Pipeline scaffolding and scripts (`run_all.sh`, `run_tests.sh`,
  `sync.sh`, `scripts/`).
- Dockerized headless decompilation setup (Ghidra, OpenJDK 17).
- MinGW-w64 CMake cross-compile configuration
  (`CMakeToolchain-MinGW.cmake`).
- `test_frontend.html` — a visual interface that *simulates* the backend
  workflow; it is a mock, not the real pipeline.

## What's not working

- No decompiled `.cpp` output exists in the repo, so there is nothing to
  compile. The end-to-end path (binary in, compilable C++ out) is
  unverified.

## Pipeline Architecture

- Phase 1: Ingestion & symbol fetching (`pefile`, `urllib`)
- Phase 2: Dockerized headless decompilation (Ghidra, OpenJDK 17)
- Phase 3: Regex refinement and namespace segmentation
- Phase 4: CI verification and cross-compilation (MinGW-w64, CMake)
- Phase 5: AST flattening (libclang `GOTO_STMT` recovery)
- Phase 6: Block synthesis (rewriting goto to native while loops)

## Usage

Provide the binary:

```bash
./run_all.sh explorer.exe
```

Once decompiled files are placed in `src/` and `include/`, cross-compile
with the provided MinGW-w64 CMake configuration:

```bash
mkdir -p build && cd build
cmake .. -DCMAKE_TOOLCHAIN_FILE=../CMakeToolchain-MinGW.cmake
make
```

## Links

- Repo: https://github.com/candlestixxx/explorerexedecompiled
- Related docs in-repo: `BINARY_INTERFACE.md`, `CHANGELOG.md`,
  `ROADMAP.md`, `TODO.md`, `HANDOFF.md`
