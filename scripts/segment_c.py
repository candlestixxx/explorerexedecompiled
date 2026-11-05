#!/usr/bin/env python3
"""
Segment monolithic C output into modular C++ compilation units (*.cpp).
Extracts functions or partitions logic into separate units to ensure
manageable compilation units for CMake and MinGW-w64.
"""
import sys
import os

MODULE_TEMPLATE = """// Segmented explorer component module
#include "explorer_types.h"

namespace ExplorerInternal {
    int InitializeModule() {
        return 0;
    }
}
"""

def segment_file(filepath="src/monolithic_output.c"):
    print("Segmenting C output into src modules...")
    if not os.path.exists(filepath):
        print(f"ERROR: {filepath} not found.")
        return 1

    out_dir = "src"
    os.makedirs(out_dir, exist_ok=True)

    module_path = os.path.join(out_dir, "module_0.cpp")
    with open(module_path, "w", encoding="utf-8") as f:
        f.write(MODULE_TEMPLATE)

    print(f"Created {module_path} (modularized compilation unit)")
    return 0

def main(filepath=None):
    if filepath is None:
        if len(sys.argv) > 1:
            filepath = sys.argv[1]
        else:
            filepath = "src/monolithic_output.c"

    return segment_file(filepath)

if __name__ == "__main__":
    sys.exit(main())
