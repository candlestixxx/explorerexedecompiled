#!/bin/bash
echo "=== EXECUTING REPOSITORY SYNC PROTOCOL ==="
git fetch --all --tags
git submodule update --init --recursive
echo "Sync complete."
