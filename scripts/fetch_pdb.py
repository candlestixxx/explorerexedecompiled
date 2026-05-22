#!/usr/bin/env python3
"""
fetch_pdb.py

Queries the Microsoft Symbol Server for a matching .pdb file given a
binary's GUID and Age hash.

Usage:
  python fetch_pdb.py <guid_age_hash> <output_dir>
"""

import os
import sys
import argparse
import logging
import urllib.request
import urllib.error

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SYMBOL_SERVER_URL = "https://msdl.microsoft.com/download/symbols"

def fetch_pdb(guid_age, pdb_name, output_dir):
    """
    Fetches a PDB from the Microsoft Symbol Server using the binary's PDB name and GUID/Age hash.
    """
    # Create the target output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # The URL format for the Microsoft Symbol Server is:
    # https://msdl.microsoft.com/download/symbols/<pdb_name>/<guid_age>/<pdb_name>
    target_url = f"{SYMBOL_SERVER_URL}/{pdb_name}/{guid_age}/{pdb_name}"
    output_path = os.path.join(output_dir, pdb_name)

    logger.info(f"Attempting to fetch PDB from: {target_url}")

    try:
        # We need a user-agent, otherwise the symbol server might reject the request
        req = urllib.request.Request(
            target_url,
            headers={'User-Agent': 'Microsoft-Symbol-Server/10.0.0.0'}
        )

        with urllib.request.urlopen(req) as response, open(output_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        logger.info(f"Successfully downloaded PDB to: {output_path}")
        return True

    except urllib.error.HTTPError as e:
        logger.error(f"HTTP Error fetching PDB: {e.code} - {e.reason}")
        return False
    except urllib.error.URLError as e:
        logger.error(f"URL Error fetching PDB: {e.reason}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error fetching PDB: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Fetch PDB from MS Symbol Server")
    parser.add_argument("guid_age", help="The GUID and Age string of the target binary (e.g., 33A27CE1BD48421FB16D5CD8C91348FF1)")
    parser.add_argument("pdb_name", help="The original name of the PDB file (e.g., explorer.pdb)")
    parser.add_argument("output_dir", help="Directory to save the downloaded PDB")
    args = parser.parse_args()

    success = fetch_pdb(args.guid_age, args.pdb_name, args.output_dir)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
