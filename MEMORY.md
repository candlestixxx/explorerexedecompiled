# MEMORY

## Internal Architectural Observations
- **Current State**: Initial project setup phase. No code or binaries are present yet.
- **Project Structure**: Primarily driven by markdown files outlining strategy, vision, and roadmap for AI agents.
- **Target OS**: Windows, dealing intimately with OS subsystem dependencies like COM, Win32 API, and Shell APIs.
- **Key Challenges**:
  - Automatically downloading matching PDB files.
  - Converting procedural Win32 APIs into modern C++ paradigms.
  - Separating compiler boilerplate from actual logic.

## Design Preferences
- Heavy segmentation of the resulting codebase into logical modules (e.g., `TaskbarController.cpp`, `ShellWindow.cpp`).
- Extensive inline documentation.
- Using idiomatically modern C++ constructs instead of raw C-style pointer arithmetic where feasible.