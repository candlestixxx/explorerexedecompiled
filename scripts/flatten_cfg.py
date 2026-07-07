#!/usr/bin/env python3
import sys
import os
import clang.cindex

def print_ast(node, depth=0):
    indent = "  " * depth
    print(f"{indent}{node.kind}")
    for child in node.get_children():
        print_ast(child, depth + 1)

def recursive_flatten(node):
    """
    Recursively walk the AST to find explicit goto statements and labels,
    preparing them for transformation into while loops or structured blocks.
    """
    # A true CFG flattener would analyze basic blocks, but here we just
    # recursively traverse to find control flow structures.
    if node.kind == clang.cindex.CursorKind.GOTO_STMT:
        print(f"  [Mock] Found GOTO at line {node.location.line}")
    elif node.kind == clang.cindex.CursorKind.LABEL_STMT:
        print(f"  [Mock] Found LABEL '{node.spelling}' at line {node.location.line}")

    for child in node.get_children():
        recursive_flatten(child)

def find_functions(node):
    if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
        print(f"Found function: {node.spelling}")
        # print_ast(node, depth=1) # Too noisy for production logs
        recursive_flatten(node)
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
