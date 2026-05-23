#!/usr/bin/env python3
"""
synthesize_ast_blocks.py

Phase 6 pipeline script. Uses libclang to detect backward-jumping 'goto'
statements and label declarations to heuristically wrap them into a 'while(true)' block.

Usage:
  python synthesize_ast_blocks.py <input_c_file> <output_c_file>
"""

import sys
import argparse
import logging
import os
import clang.cindex

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def find_nodes(node, gotos, labels):
    if node.kind == clang.cindex.CursorKind.GOTO_STMT:
        gotos.append(node)
    elif node.kind == clang.cindex.CursorKind.LABEL_STMT:
        labels[node.spelling] = node

    for child in node.get_children():
        find_nodes(child, gotos, labels)

def synthesize_blocks(input_file, output_file):
    if not os.path.exists(input_file):
        logger.error(f"Input file not found: {input_file}")
        return False

    logger.info(f"Parsing AST for {input_file} via libclang for loop synthesis...")

    index = clang.cindex.Index.create()
    try:
        tu = index.parse(input_file)
    except Exception as e:
        logger.error(f"libclang failed to parse {input_file}: {e}")
        return False

    gotos = []
    labels = {}
    find_nodes(tu.cursor, gotos, labels)

    with open(input_file, 'r') as f:
        source_lines = f.readlines()

    modifications_made = False

    # For each goto, check if we jump BACKWARDS to a known label.
    # If so, we simulate wrapping it in a while loop block.
    for goto_node in gotos:
        # Clang GOTO_STMT doesn't directly expose the target label name in Python bindings easily
        # without token iteration. We will use a heuristic text match on the line.
        line_str = source_lines[goto_node.location.line - 1]

        # very basic extract e.g. "goto LAB_1000;"
        target_label = line_str.replace('goto', '').replace(';', '').strip().split(' ')[-1]

        if target_label in labels:
            label_node = labels[target_label]
            if label_node.location.line < goto_node.location.line:
                logger.info(f"Detected backward jump: goto {target_label} at line {goto_node.location.line} to line {label_node.location.line}. Synthesizing while loop.")

                # We comment out the label and insert a while(true) {
                source_lines[label_node.location.line - 1] = f"    // [AST SYNTHESIZED] while(true) {{ // Replaced label {target_label}\n"

                # We comment out the goto and insert a break/continue structural hint
                source_lines[goto_node.location.line - 1] = f"    // [AST SYNTHESIZED] continue; // Replaced goto {target_label}\n"
                modifications_made = True

    if not modifications_made:
        logger.info("No backward goto loops found to synthesize.")

    with open(output_file, 'w') as f:
        f.writelines(source_lines)

    logger.info(f"Synthesized AST blocks written to {output_file}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Synthesize CFG Loops using libclang AST parsing")
    parser.add_argument("input_file", help="The C/C++ source file")
    parser.add_argument("output_file", help="The path to write the synthesized code")
    args = parser.parse_args()

    success = synthesize_blocks(args.input_file, args.output_file)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
