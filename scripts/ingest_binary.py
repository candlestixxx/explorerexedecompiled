#!/usr/bin/env python3
import sys, hashlib
try:
    import pefile
except ImportError:
    pefile = None

def main():
    if len(sys.argv) < 2: return 1
    binary_path = sys.argv[1]
    try:
        with open(binary_path, "rb") as f:
            data = f.read()
            print(f"SHA256: {hashlib.sha256(data).hexdigest()}")
        if pefile:
            pe = pefile.PE(binary_path)
            print("PE Header parsed successfully.")
            return 0
    except Exception as e:
        print(f"Ingestion error: {e}")
    return 1

if __name__ == "__main__":
    sys.exit(main())
