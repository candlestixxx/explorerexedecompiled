#!/usr/bin/env python3
import sys
import shutil

def check_module(module_name):
    try:
        __import__(module_name)
        print(f"[OK] Python module '{module_name}' is installed.")
        return True
    except ImportError:
        print(f"[ERROR] Python module '{module_name}' is missing.")
        return False

def check_binary(binary_name):
    if shutil.which(binary_name):
        print(f"[OK] System binary '{binary_name}' found in PATH.")
        return True
    else:
        print(f"[ERROR] System binary '{binary_name}' is missing from PATH.")
        return False

def main():
    print("Validating environment setup...")
    success = True

    # Check Python Modules
    if not check_module('pefile'): success = False
    if not check_module('clang.cindex'): success = False

    # Check System Binaries
    if not check_binary('cmake'): success = False
    if not check_binary('x86_64-w64-mingw32-gcc'): success = False

    if not success:
        print("Environment validation failed. Please install missing dependencies.")
        return 1

    print("Environment validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
