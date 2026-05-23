#!/usr/bin/env python3
"""
refine_c.py

Phase 3 pipeline script. Parses the monolithic C pseudocode dumped by Ghidra
and applies heuristic regexes to refine variable names and flag compiler-optimized
gotos based on the rules in C_CPP_GUIDELINES.md.

Usage:
  python refine_c.py <input_c_file> <output_c_file>
"""

import sys
import argparse
import logging
import re
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def refine_pseudocode(input_file, output_file):
    if not os.path.exists(input_file):
        logger.error(f"Input file not found: {input_file}")
        return False

    logger.info(f"Refining pseudocode from {input_file}")

    with open(input_file, 'r') as f:
        content = f.read()

    # Rule: Variable Renaming (camelCase for internal variables)
    # Ghidra often outputs variables like uVar1, piVar2, ppcVar3.
    # We will simply append an underscore to flag them for manual/AI review
    # or apply a camelCase transformation. For now, we normalize basic prefixes.

    # Matches uVarX, iVarX, pcVarX etc.
    content = re.sub(r'\b([a-z]+)Var(\d+)\b', r'\1_var\2', content)

    # Rule: Flagging goto statements
    # C_CPP_GUIDELINES: Eliminate `goto` statements resulting from compiler optimizations.
    # We will inject a warning comment above any goto statement.
    content = re.sub(r'(\s*)(goto\s+\w+;)', r'\1// [WARNING: C_CPP_GUIDELINES] De-flattening required for goto statement\1\2', content)

    # Rule: Modern C++ casts (Heuristic representation for raw casts)
    # This is a very rudimentary regex to catch (int)x style casts and replace with static_cast.
    # Note: A true AST parser (like libclang) is required for 100% accuracy.
    content = re.sub(r'\(([A-Z][a-zA-Z0-9_]+ \*)\)([a-zA-Z0-9_]+)', r'reinterpret_cast<\1>(\2)', content)
    content = re.sub(r'\((int|char|short|long|unsigned int|DWORD|WORD|BYTE)\)([a-zA-Z0-9_]+)', r'static_cast<\1>(\2)', content)

    with open(output_file, 'w') as f:
        f.write(content)

    logger.info(f"Refined pseudocode written to {output_file}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Refine Ghidra C Pseudocode")
    parser.add_argument("input_file", help="The raw .c output from Ghidra DumpC.py")
    parser.add_argument("output_file", help="The path to write the refined .c file")
    args = parser.parse_args()

    success = refine_pseudocode(args.input_file, args.output_file)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
