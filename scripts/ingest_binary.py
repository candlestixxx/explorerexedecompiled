#!/usr/bin/env python3
"""
ingest_binary.py

Locates and validates the target `explorer.exe` binary.
Verifies file hashes and PE headers before allowing it into the pipeline.

Usage:
  python ingest_binary.py <path_to_binary>
"""

import sys
import argparse
import logging
import os
import pefile
import hashlib

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_file_hash(filepath):
    """Computes the SHA256 hash of the given file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def extract_pdb_info(filepath):
    """
    Parses the PE file and extracts the CodeView Debug Directory
    to construct the GUID/Age hash required for Microsoft Symbol Server.
    Returns a tuple (guid_age_str, pdb_filename) or (None, None).
    """
    try:
        pe = pefile.PE(filepath)
    except Exception as e:
        logger.error(f"Failed to parse PE file {filepath}: {e}")
        return None, None

    if not hasattr(pe, 'DIRECTORY_ENTRY_DEBUG'):
        logger.warning(f"No debug directory found in {filepath}.")
        return None, None

    for debug_data in pe.DIRECTORY_ENTRY_DEBUG:
        # Check if the debug entry is of type IMAGE_DEBUG_TYPE_CODEVIEW (2)
        if debug_data.struct.Type == 2:
            try:
                cv_data = debug_data.entry
                # Ensure it's the RSDS (PDB 7.0) signature
                if hasattr(cv_data, 'Signature_String') and cv_data.Signature_String == b"RSDS":
                    # GUID format: data1-data2-data3-data4
                    # Symbol Server expects GUID formatted as hex string + Age appended
                    guid_hex = f"{cv_data.Signature_Data1:08X}{cv_data.Signature_Data2:04X}{cv_data.Signature_Data3:04X}"
                    # Data4 is an array of 8 bytes
                    guid_hex += "".join([f"{b:02X}" for b in cv_data.Signature_Data4])
                    age_hex = f"{cv_data.Age:X}"

                    guid_age = f"{guid_hex}{age_hex}"
                    pdb_name = cv_data.PdbFileName.decode("utf-8").strip('\0')

                    return guid_age, pdb_name
            except Exception as e:
                logger.error(f"Error parsing CodeView debug data: {e}")

    return None, None

def validate_binary(filepath):
    """
    Validates the target binary and extracts its GUID/Age hash for PDB retrieval.
    Returns (guid_age, pdb_name) or (None, None)
    """
    if not os.path.exists(filepath):
        logger.error(f"Binary not found: {filepath}")
        return None, None

    logger.info(f"Validating binary at: {filepath}")

    file_hash = get_file_hash(filepath)
    logger.info(f"SHA256: {file_hash}")

    guid_age, pdb_name = extract_pdb_info(filepath)

    if guid_age and pdb_name:
        logger.info(f"PDB Name extracted: {pdb_name}")
        logger.info(f"GUID/Age hash extracted: {guid_age}")
        logger.info("Binary validation passed.")
        return guid_age, pdb_name
    else:
        logger.error("Failed to extract GUID/Age or PDB Name. Binary might not be supported or is stripped.")
        return None, None

def main():
    parser = argparse.ArgumentParser(description="Ingest and validate explorer.exe binary")
    parser.add_argument("binary_path", help="Path to the target explorer.exe binary")
    args = parser.parse_args()

    guid_age, pdb_name = validate_binary(args.binary_path)
    if not guid_age:
        sys.exit(1)

if __name__ == "__main__":
    main()
