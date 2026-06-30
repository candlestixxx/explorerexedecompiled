#!/usr/bin/env python3
import os

def analyze_output(filepath):
    if not os.path.exists(filepath):
        return "CRITICAL ANOMALY: Output file missing."

    with open(filepath, 'r') as f:
        content = f.read()

    size = len(content)
    lines = content.count('\n') + 1

    report = f"## Post-Decompilation Output Analysis\n"
    report += f"- Target File: {filepath}\n"
    report += f"- Size: {size} bytes\n"
    report += f"- Lines: {lines}\n\n"

    # Anomaly detection logic
    if size < 500:
        report += "### FLAG: ANOMALY DETECTED\n"
        report += "The output file is unusually small (under 500 bytes).\n"
        if "int main() { return 0; }" in content:
            report += "Root Cause: The output perfectly matches the mock C stub. This indicates the pipeline processed a synthesized placeholder binary rather than the authentic explorer.exe.\n"
    else:
        report += "### SUCCESS: Genuine Output Detected\n"
        report += "The output file exceeds the mock threshold. Proceed with deep symbol recovery.\n"

    return report

def main():
    print("Initiating Post-Decompilation Analysis...")
    report_content = analyze_output("src/monolithic_output.c")

    with open("post_run_status.md", "w") as f:
        f.write("# Autonomous Pipeline Status Report\n\n")
        f.write(report_content)

    print("Analysis complete. Findings written to post_run_status.md")

if __name__ == "__main__":
    main()
