# DEPLOY

## Environment Setup Instructions

### Prerequisites
- **OS**: Windows (preferred for native testing) or a Linux/macOS environment with appropriate cross-platform decompilation tools.
- **Disassembler**: IDA Pro or Ghidra installed and accessible in the system PATH.
- **Compiler**: MSVC (Microsoft Visual C++) via Visual Studio Build Tools, or Clang/GCC for testing compilability of the output C++ code.
- **Python**: Python 3.9+ for running automation and parsing scripts.
- **Git**: Ensure `git` is configured for committing artifacts.

### Workspace Initialization
1. Clone the repository and initialize submodules recursively:
   ```bash
   git clone --recursive <repository-url>
   cd explorerexedecompiled
   ```
2. Set up virtual environments for Python scripts (if any):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install Python dependencies (placeholder):
   ```bash
   # pip install -r requirements.txt
   ```

### Execution Pipeline
- To run the initial binary ingestion and PDB retrieval, execute `scripts/ingest_binary.py` (To be developed).
- Run `scripts/decompile.py` to initiate headless decompilation and AST generation (To be developed).