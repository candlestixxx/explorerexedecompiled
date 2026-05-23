#!/usr/bin/env python3
"""
segment_c.py

Phase 3 pipeline script. Parses the refined monolithic C pseudocode file
and segments it into logical C++ source files within the src/ directory based
on heuristic namespace prefixes or function groupings (e.g. CTaskbar_, CShellWindow_).

Usage:
  python segment_c.py <input_refined_c_file> <output_src_dir>
"""

import sys
import argparse
import logging
import re
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def segment_code(input_file, output_dir):
    if not os.path.exists(input_file):
        logger.error(f"Input file not found: {input_file}")
        return False

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    logger.info(f"Segmenting monolithic file: {input_file}")

    with open(input_file, 'r') as f:
        content = f.read()

    # Split the file by the function headers created by DumpC.py
    # e.g., "// ==========================================================\n// Function: Name\n..."

    sections = re.split(r'(// ==========================================================\n// Function: .*\n// Address:.*\n// ==========================================================\n)', content)

    # default bucket for functions that don't match a heuristic class
    modules = {"Unknown": ""}

    # Re-associate the split headers with their function bodies
    for i in range(1, len(sections), 2):
        header = sections[i]
        body = sections[i+1] if (i+1) < len(sections) else ""

        # Extract function name from header
        match = re.search(r'// Function:\s*([^\s]+)', header)
        if match:
            func_name = match.group(1)

            # Heuristic grouping based on standard COM/Win32 shell prefixes
            module_name = "Unknown"
            if func_name.startswith("CTaskbar_") or func_name.startswith("Taskbar"):
                module_name = "Taskbar"
            elif func_name.startswith("CShellBrowser") or func_name.startswith("ShellWindow"):
                module_name = "ShellWindow"
            elif func_name.startswith("CDesktop"):
                module_name = "Desktop"
            elif func_name.startswith("FileBrowser"):
                module_name = "FileBrowserHelpers"

            if module_name not in modules:
                modules[module_name] = ""

            modules[module_name] += header + body

    # Write modules to disk
    for mod_name, mod_content in modules.items():
        if not mod_content.strip():
            continue

        filename = f"{mod_name}.cpp" if mod_name != "Unknown" else "Misc.cpp"
        out_path = os.path.join(output_dir, filename)

        # Append mode so we don't overwrite if multiple passes occur, but for clean runs, we write.
        with open(out_path, 'w') as out_f:
            out_f.write(f"// Segmented Module: {filename}\n")
            out_f.write(mod_content)

        logger.info(f"Wrote module: {filename} ({len(mod_content.splitlines())} lines)")

    return True

def main():
    parser = argparse.ArgumentParser(description="Segment Refined Ghidra Pseudocode into Modules")
    parser.add_argument("input_file", help="The refined .c output from refine_c.py")
    parser.add_argument("output_dir", help="The src/ directory to write the .cpp files to")
    args = parser.parse_args()

    success = segment_code(args.input_file, args.output_dir)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
