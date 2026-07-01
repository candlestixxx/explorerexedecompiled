#!/bin/bash
mkdir -p input
echo "Monitoring input/ directory for target binaries..."
while true; do
    for file in input/*; do
        if [ -f "$file" ]; then
            echo "Found file: $file. Executing pipeline..."
            ./run_all.sh "$file"
            python3 scripts/post_analysis.py
            # Remove the file to prevent continuous loop
            rm "$file"
            echo "Pipeline run complete. Resuming monitoring..."
        fi
    done
    sleep 5
done
