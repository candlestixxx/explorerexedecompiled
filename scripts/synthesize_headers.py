#!/usr/bin/env python3
"""
synthesize_headers.py

Phase 3 pipeline script. Reads the segmented .cpp modules in the src/ directory
and generates corresponding .h header files in the include/ directory by heuristically
extracting function signatures.

Usage:
  python synthesize_headers.py <src_dir> <include_dir>
"""

import sys
import argparse
import logging
import re
import os
import glob

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def synthesize_header(cpp_path, include_dir):
    filename = os.path.basename(cpp_path)
    module_name, _ = os.path.splitext(filename)
    header_filename = f"{module_name}.h"
    header_path = os.path.join(include_dir, header_filename)

    with open(cpp_path, 'r') as f:
        content = f.read()

    # Heuristic regex to match simple C/C++ function definitions.
    # Looks for a return type, space, function name, and arguments inside parentheses
    # followed by an opening brace. (e.g. `void CTaskbar_Initialize(int a) {`)
    # Note: Very complex templates or multi-line macros may bypass this basic heuristic.

    signatures = re.findall(r'^([A-Za-z_][A-Za-z0-9_*\s]*\s+[A-Za-z_][A-Za-z0-9_]*\s*\([^)]*\))\s*\{', content, flags=re.MULTILINE)

    include_guard = f"{module_name.upper()}_H"

    with open(header_path, 'w') as out_f:
        out_f.write(f"// Auto-generated Header for {module_name}\n")
        out_f.write(f"#ifndef {include_guard}\n")
        out_f.write(f"#define {include_guard}\n\n")

        # We assume standard windows types might be used
        out_f.write("#include <windows.h>\n")
        out_f.write("#include <unknwn.h>\n\n")

        if not signatures:
            out_f.write("// No explicitly matched function signatures found.\n")
        else:
            for sig in signatures:
                # Strip trailing whitespace and append semicolon
                clean_sig = sig.strip()
                out_f.write(f"{clean_sig};\n")

        out_f.write(f"\n#endif // {include_guard}\n")

    logger.info(f"Synthesized header: {header_filename} with {len(signatures)} signatures.")
    return True

def process_directory(src_dir, include_dir):
    if not os.path.exists(src_dir):
        logger.error(f"Source directory not found: {src_dir}")
        return False

    if not os.path.exists(include_dir):
        os.makedirs(include_dir)

    cpp_files = glob.glob(os.path.join(src_dir, "*.cpp"))
    if not cpp_files:
        logger.warning(f"No .cpp files found in {src_dir}")
        return True

    for cpp_file in cpp_files:
        synthesize_header(cpp_file, include_dir)

    return True

def main():
    parser = argparse.ArgumentParser(description="Synthesize C++ headers from source files")
    parser.add_argument("src_dir", help="Directory containing the segmented .cpp files")
    parser.add_argument("include_dir", help="Directory to output the synthesized .h files")
    args = parser.parse_args()

    success = process_directory(args.src_dir, args.include_dir)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
