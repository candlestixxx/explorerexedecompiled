#!/bin/bash
while true; do
  if [ -f input/explorer.exe ]; then
    echo "Found explorer.exe! Triggering pipeline..."
    ./run_all.sh input/explorer.exe > pipeline_execution.log 2>&1
    echo "Pipeline complete. Triggering autonomous post-decompilation analysis..."
    ./scripts/post_analysis.py >> pipeline_execution.log 2>&1
    break
  fi
  sleep 5
done
