#!/usr/bin/env python3
import sys
import os
import urllib.request

def main():
    if not os.path.exists("pdb_info.txt"):
        print("No PDB info found. Skipping PDB fetch.")
        return 0
    with open("pdb_info.txt", "r") as f:
        lines = f.readlines()
        if len(lines) < 2:
            print("Invalid PDB info format. Skipping PDB fetch.")
            return 0
        filename = lines[0].strip()
        guid_age = lines[1].strip()

    url = f"https://msdl.microsoft.com/download/symbols/{filename}/{guid_age}/{filename}"
    print(f"Fetching PDB from: {url}")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Failed to download PDB: {e}")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
