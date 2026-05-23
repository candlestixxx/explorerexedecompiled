#!/usr/bin/env python3
"""
orchestrate.py

Master pipeline script for Phase 1.
1. Validates and extracts GUID/Age from the target binary using ingest_binary.
2. Fetches the matching PDB from the Microsoft Symbol Server using fetch_pdb.

Usage:
  python orchestrate.py <path_to_binary> <pdb_output_dir>
"""

import sys
import argparse
import logging
import ingest_binary
import fetch_pdb

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_phase_1(binary_path, pdb_output_dir):
    logger.info("=== Starting Phase 1: Binary Ingestion & PDB Retrieval ===")

    # Step 1: Validate and extract info
    logger.info("--- Step 1: Ingesting Binary ---")
    guid_age, pdb_name = ingest_binary.validate_binary(binary_path)
    if not guid_age or not pdb_name:
        logger.error("Binary validation failed or PDB info missing. Halting pipeline.")
        return False

    # Step 2: Fetch PDB
    logger.info("--- Step 2: Fetching PDB ---")
    if not fetch_pdb.fetch_pdb(guid_age, pdb_name, pdb_output_dir):
        logger.error("Failed to fetch PDB from Symbol Server. Halting pipeline.")
        return False

    logger.info("=== Phase 1 Completed Successfully ===")
    return True

def main():
    parser = argparse.ArgumentParser(description="Master orchestrator for Phase 1 pipeline")
    parser.add_argument("binary_path", help="Path to the target executable (e.g., explorer.exe)")
    parser.add_argument("pdb_output_dir", help="Directory to save the downloaded PDB")
    args = parser.parse_args()

    success = run_phase_1(args.binary_path, args.pdb_output_dir)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
