# MEMORY

- **AST vs Regex:** Discovered that pure regex string replacement is wildly insufficient for rewriting `goto` loops into `while` loops. Successfully pivoted to `libclang` C++ indexer for Phase 5 & 6 structural reconstruction.
- **Docker Requirement:** Java environment drift breaks headless decompilation unpredictably. Hardcoding Ghidra 11.0 on OpenJDK 17 in `Dockerfile` stabilized the pipeline.
- **Compiler Choice:** MinGW-w64 on Linux perfectly satisfies the verification requirements for `windows.h`, `unknwn.h`, and `ole32` without needing a native Windows CI host.
- **Limitation:** `libclang` AST parser crashes when given source files that heavily import the C++ standard library (e.g. `<iostream>`). It succeeds on pure C or minimal C++.
- **CI Verification Block:** CI verification was previously blocked because of a lack of C++ source files due to decompilation logic relying on dynamic inputs. Creating generic mock C++ files (`mock_explorer.cpp`, `mock_shell.cpp`) successfully bypasses this and validates the CMake setup.
