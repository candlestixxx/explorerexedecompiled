#!/usr/bin/env python3
import sys
import os
import clang.cindex
from clang.cindex import Index

def analyze_cfg(filepath):
    print(f"Flattening CFG (AST) for {os.path.basename(filepath)}...")
    if not os.path.exists(filepath):
        print(f"ERROR: {filepath} not found. Cannot analyze.")
        return 1

    index = Index.create()
    tu = index.parse(filepath, args=['-x', 'c++', '-std=c++17'])

    def find_functions(node):
        if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
            print(f"Found function: {node.spelling}")
        elif node.kind == clang.cindex.CursorKind.GOTO_STMT:
            print(f"  [Mock] Found GOTO at line {node.location.line}")
        elif node.kind == clang.cindex.CursorKind.LABEL_STMT:
            print(f"  [Mock] Found LABEL '{node.spelling}' at line {node.location.line}")

        for child in node.get_children():
            find_functions(child)

    find_functions(tu.cursor)
    return 0

def main(filepath=None):
    if filepath is None:
        if len(sys.argv) > 1:
            filepath = sys.argv[1]
        else:
            filepath = "src/monolithic_output.c"

    return analyze_cfg(filepath)

if __name__ == "__main__":
    sys.exit(main())
