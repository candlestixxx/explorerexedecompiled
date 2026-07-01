#!/bin/bash
set -e
echo "Running Python Unit Tests..."
PYTHONPATH=scripts python3 -m unittest scripts/test_flatten_cfg.py
PYTHONPATH=scripts python3 -m unittest scripts/test_pipeline_mocks.py
echo "Unit tests passed."
