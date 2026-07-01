#!/usr/bin/env python3
import os

def main():
    target_file = "src/monolithic_output.c"
    output_file = "post_run_status.md"

    status = []
    status.append("# Post-Run Analysis Status\n")

    if not os.path.exists(target_file):
        status.append(f"**Error**: {target_file} not found. Decompilation may have failed.")
    else:
        size = os.path.getsize(target_file)
        with open(target_file, "r") as f:
            content = f.read()

        is_mock = "// Decompiled output from Ghidra" in content
        is_small = size < 100

        if is_mock and is_small:
            status.append("**Warning**: Output appears to be a mock stub.")
        else:
            status.append("**Success**: Authentic decompilation output detected.")

        status.append(f"- File Size: {size} bytes")
        status.append(f"- Contains Mock Signature: {is_mock}")

    with open(output_file, "w") as f:
        f.write("\n".join(status))

    print(f"Post-analysis complete. Results logged to {output_file}.")

if __name__ == "__main__":
    main()
