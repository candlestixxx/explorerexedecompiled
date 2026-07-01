#!/usr/bin/env python3
import sys
import os
import clang.cindex

def print_ast(node, depth=0):
    indent = "  " * depth
    print(f"{indent}{node.kind}")
    for child in node.get_children():
        print_ast(child, depth + 1)

def find_functions(node):
    if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
        print(f"Found function: {node.spelling}")
        print_ast(node, depth=1)
    for child in node.get_children():
        find_functions(child)

def main(filepath="src/monolithic_output.c"):
    if not os.path.exists(filepath):
        print("Flattening CFG (AST)...")
        print(f"ERROR: {filepath} not found. Cannot analyze.")
        return 1

    print("Flattening CFG (AST)...")
    index = clang.cindex.Index.create()
    tu = index.parse(filepath)
    find_functions(tu.cursor)
    return 0

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "src/monolithic_output.c"
    sys.exit(main(filepath))
