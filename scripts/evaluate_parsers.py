#!/usr/bin/env python3
import sys
import os
import clang.cindex
from clang.cindex import Index
import time

def evaluate_ast_parser(filepath):
    print(f"Evaluating libclang AST parsing capabilities on {os.path.basename(filepath)}...")
    if not os.path.exists(filepath):
        print(f"ERROR: File {filepath} not found.")
        return 1

    start_time = time.time()
    index = Index.create()

    # Try parsing the raw file directly.
    # Note: For real files, we'd normally pass include paths, but this is a raw pseudo-C evaluation
    tu = index.parse(filepath, args=['-x', 'c++', '-std=c++17'])

    parse_time = time.time() - start_time
    print(f"Initial Parse Time: {parse_time:.2f} seconds")

    if not tu:
        print("libclang failed to generate Translation Unit.")
        return 1

    diagnostics = list(tu.diagnostics)
    print(f"Number of parsing diagnostics (errors/warnings): {len(diagnostics)}")

    # Do a basic walk to measure traversal limits
    node_count = 0
    function_count = 0
    goto_count = 0

    def walk(node):
        nonlocal node_count, function_count, goto_count
        node_count += 1

        if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
            function_count += 1
        elif node.kind == clang.cindex.CursorKind.GOTO_STMT:
            goto_count += 1

        for child in node.get_children():
            walk(child)

    print("Walking AST...")
    walk_start = time.time()
    try:
        walk(tu.cursor)
        walk_time = time.time() - walk_start
        print(f"AST Walk completed successfully in {walk_time:.2f} seconds.")
        print(f"Total Nodes: {node_count}")
        print(f"Functions: {function_count}")
        print(f"Explicit GOTOs: {goto_count}")
    except Exception as e:
        print(f"AST Walk Failed! Recursion limit or OOM reached: {e}")
        return 1

    return 0

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "src/monolithic_output.c"
    sys.exit(evaluate_ast_parser(target))
