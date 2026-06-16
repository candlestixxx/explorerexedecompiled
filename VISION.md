# VISION

The primary objective of this repository is to autonomously decompile, restructure, and cross-compile the Windows 10 `explorer.exe` (Build 19045) binary into high-fidelity, compilable, and highly readable C++ source code.

This project uses an orchestrator pattern with 6 discrete phases encompassing heuristic extraction, headless Ghidra decompilation, regex refinement, AST-based control flow recovery (eliminating gotos), and finally Linux-based MinGW-w64 cross-compilation linking to Win32/COM libraries.
