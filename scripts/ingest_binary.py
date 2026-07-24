#!/usr/bin/env python3
import sys, hashlib
try:
    import pefile
except ImportError:
    pefile = None

def get_pdb_info(pe):
    """Extracts the PDB GUID and Age from the CodeView Debug Directory."""
    if not hasattr(pe, 'DIRECTORY_ENTRY_DEBUG'):
        return None
    for debug in pe.DIRECTORY_ENTRY_DEBUG:
        if debug.struct.Type == 2: # IMAGE_DEBUG_TYPE_CODEVIEW
            cv = debug.entry
            if cv and cv.CvSignature == b'RSDS':
                if hasattr(cv, 'Signature_String'):
                    guid = cv.Signature_String[:-1]
                    return guid, cv.Age, cv.PdbFileName.decode('utf-8').strip('\x00')
                else:
                    data4 = cv.Signature_Data4
                    if isinstance(data4, int):
                        data4_hex = f"{data4:016X}"
                    else:
                        data4_hex = data4.hex().upper()
                    guid = f"{cv.Signature_Data1:08X}{cv.Signature_Data2:04X}{cv.Signature_Data3:04X}{data4_hex}"
                    return guid, cv.Age, cv.PdbFileName.decode('utf-8').strip('\x00')
    return None

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
            pdb_info = get_pdb_info(pe)
            if pdb_info:
                guid, age, filename = pdb_info
                print(f"PDB Info: {filename} {guid}{age:X}")
                # Save PDB info for fetch_pdb.py
                with open("pdb_info.txt", "w") as f:
                    f.write(f"{filename}\n{guid}{age:X}\n")
            return 0
    except Exception as e:
        print(f"Ingestion error: {e}")
    return 1

if __name__ == "__main__":
    sys.exit(main())
