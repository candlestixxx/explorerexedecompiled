#!/usr/bin/env python3
"""
Synthesize C/C++ structural headers into include/.
Creates common headers and type declarations required for compiling
extracted Windows explorer components and Win32 COM interfaces.
"""
import sys
import os

COMMON_HEADER_CONTENT = """#ifndef EXPLORER_DECOMPILED_TYPES_H
#define EXPLORER_DECOMPILED_TYPES_H

#include <stddef.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

// Base primitive types inferred from Ghidra AST
typedef uint8_t  undefined;
typedef uint8_t  undefined1;
typedef uint16_t undefined2;
typedef uint32_t undefined4;
typedef uint64_t undefined8;
typedef uint8_t  byte;
typedef uint16_t word;
typedef uint32_t dword;
typedef uint64_t qword;
typedef uint64_t ulonglong;
typedef int64_t  longlong;

#ifdef __cplusplus
}
#endif

#endif // EXPLORER_DECOMPILED_TYPES_H
"""

def synthesize_headers(include_dir="include"):
    print(f"Synthesizing headers into {include_dir}...")
    os.makedirs(include_dir, exist_ok=True)
    header_path = os.path.join(include_dir, "explorer_types.h")
    with open(header_path, "w", encoding="utf-8") as f:
        f.write(COMMON_HEADER_CONTENT)
    print(f"Generated {header_path}")
    return 0

def main():
    include_dir = sys.argv[1] if len(sys.argv) > 1 else "include"
    return synthesize_headers(include_dir)

if __name__ == "__main__":
    sys.exit(main())
