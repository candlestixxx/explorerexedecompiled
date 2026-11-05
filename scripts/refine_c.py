#!/usr/bin/env python3
"""
Refine Ghidra-generated C/C++ pseudocode.
Injects standard type definitions for Ghidra pseudocode primitives
(undefined, ulonglong, longlong, byte, bool, LOCK, etc.) into the monolithic
output file so that downstream libclang AST parsers and syntax analyzers
can load the translation unit cleanly without encountering unresolved symbol errors.
"""
import sys
import os

GHIDRA_PRIMITIVES_HEADER = """/* Standard Ghidra Decompiler Type Declarations & Primitives */
#ifndef GHIDRA_PRIMITIVES_H
#define GHIDRA_PRIMITIVES_H

#ifdef __cplusplus
extern "C" {
#endif

typedef unsigned char undefined;
typedef unsigned char undefined1;
typedef unsigned short undefined2;
typedef unsigned int undefined4;
typedef unsigned long long undefined8;
typedef unsigned char byte;
typedef unsigned short word;
typedef unsigned int dword;
typedef unsigned long long qword;
typedef unsigned long long ulonglong;
typedef long long longlong;
typedef unsigned int uint;
typedef unsigned short ushort;
typedef unsigned char uchar;
typedef void* LPTOP_LEVEL_EXCEPTION_FILTER;

#ifndef __cplusplus
#ifndef bool
typedef unsigned char bool;
#define true 1
#define false 0
#endif
#endif

#define LOCK() do {} while(0)

#ifdef __cplusplus
}
#endif

#endif /* GHIDRA_PRIMITIVES_H */
"""

def refine_monolithic_c(filepath="src/monolithic_output.c"):
    print("Refining C macros, types, and casts...")
    if not os.path.exists(filepath):
        print(f"File {filepath} not found. Skipping refinement.")
        return 0

    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        if "GHIDRA_PRIMITIVES_H" not in content:
            new_content = GHIDRA_PRIMITIVES_HEADER + "\n" + content
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Successfully injected Ghidra type definitions into {filepath}")
        else:
            print(f"Ghidra primitives already present in {filepath}")
        return 0
    except Exception as e:
        print(f"Error refining {filepath}: {e}")
        return 1

def main():
    filepath = sys.argv[1] if len(sys.argv) > 1 else "src/monolithic_output.c"
    return refine_monolithic_c(filepath)

if __name__ == "__main__":
    sys.exit(main())
