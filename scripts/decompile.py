#!/usr/bin/env python3
"""
Orchestrates Dockerized headless Ghidra decompilation.
Executes Ghidra within the ghidra-decompiler container to produce C pseudocode
at src/monolithic_output.c, ensuring universal read/write permissions for pipeline stages.
"""
import sys
import subprocess
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: decompile.py <binary_path>")
        return 1

    binary_path = sys.argv[1]
    if not os.path.exists(binary_path):
        print(f"File not found: {binary_path}")
        return 1

    print(f"Orchestrating Dockerized headless decompilation for {binary_path}...")

    os.makedirs("src", exist_ok=True)
    os.makedirs("project", exist_ok=True)

    # Command executes Ghidra headless analysis and then grants read/write permissions on the generated file
    container_cmd = (
        f"/opt/ghidra/support/analyzeHeadless /workspace/project Project "
        f"-import /workspace/{binary_path} -postScript /workspace/scripts/DumpC.py -deleteProject "
        f"&& chmod 666 /workspace/src/monolithic_output.c 2>/dev/null || true"
    )

    cmd = [
        "docker", "run", "--rm",
        "-v", f"{os.getcwd()}:/workspace",
        "ghidra-decompiler",
        "bash", "-c", container_cmd
    ]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)

    if result.returncode != 0:
        print("Decompilation failed!")
        return 1

    print("Decompilation complete. Output saved to src/monolithic_output.c")
    return 0

if __name__ == "__main__":
    sys.exit(main())
