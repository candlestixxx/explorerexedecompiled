#!/usr/bin/env python3
"""
decompile.py

Invokes the headless disassembler (e.g., Ghidra or IDA Pro) on the target binary
to generate intermediate representation (IR) or ASTs.

Usage:
  python decompile.py <path_to_binary> <output_dir>
"""

import os
import sys
import argparse
import logging
import subprocess

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_headless_decompilation(binary_path, output_dir):
    """
    Invokes the containerized Ghidra headless analyzer to decompile the target binary.
    """
    if not os.path.exists(binary_path):
        logger.error(f"Target binary does not exist: {binary_path}")
        return False

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    binary_abs_path = os.path.abspath(binary_path)
    output_abs_dir = os.path.abspath(output_dir)
    binary_name = os.path.basename(binary_path)

    logger.info(f"Starting headless decompilation via Docker on: {binary_abs_path}")
    logger.info(f"Output will be saved to: {output_abs_dir}")

    # We mount the input binary and output directory into the container
    # The analyzeHeadless script requires a project directory (which we map to /workspace/proj)
    # and a project name. We use -import to pull the binary in.

    docker_cmd = [
        "docker", "run", "--rm",
        "-v", f"{binary_abs_path}:/input/{binary_name}:ro",
        "-v", f"{output_abs_dir}:/output:rw",
        "explorer-decompiler",
        "/workspace",       # Project path inside container
        "ExplorerProj",     # Project name
        "-import", f"/input/{binary_name}"
    ]

    logger.info(f"Executing: {' '.join(docker_cmd)}")

    try:
        # Run docker command, streaming output back to stdout
        process = subprocess.Popen(docker_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in iter(process.stdout.readline, ''):
            logger.info(f"[GHIDRA] {line.strip()}")

        process.stdout.close()
        process.wait()

        if process.returncode == 0:
            logger.info("Decompilation completed successfully.")
            return True
        else:
            logger.error(f"Ghidra analyzer failed with return code {process.returncode}")
            return False

    except subprocess.CalledProcessError as e:
        logger.error(f"Subprocess failed to launch Docker: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error during decompilation: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Run headless decompilation via Dockerized Ghidra")
    parser.add_argument("binary_path", help="Path to the target binary (e.g. explorer.exe)")
    parser.add_argument("output_dir", help="Directory to save the decompiled output")
    args = parser.parse_args()

    success = run_headless_decompilation(args.binary_path, args.output_dir)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
