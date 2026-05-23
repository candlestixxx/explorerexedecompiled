# DumpC.py
# @author Jules
# @category Decompilation
# @keybinding
# @menupath
# @toolbar
#
# Dumps decompiled C pseudocode for all functions in the binary to an output file.
# Meant to be run headlessly via Ghidra analyzeHeadless.

import os
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

def dump_all_functions():
    # Setup decompiler interface
    decomplib = DecompInterface()
    decomplib.openProgram(currentProgram)

    monitor = ConsoleTaskMonitor()

    # Target output directory is mapped via Docker to /output
    output_dir = "/output"
    if not os.path.exists(output_dir):
        print("Output directory does not exist! Check Docker volume mounts.")
        return

    output_file = os.path.join(output_dir, currentProgram.getName() + "_decompiled.c")

    print("Starting decompilation dump to: " + output_file)

    with open(output_file, "w") as f:
        functionManager = currentProgram.getFunctionManager()
        functions = functionManager.getFunctions(True) # True means forward iterator

        for function in functions:
            f.write("// ==========================================================\n")
            f.write("// Function: " + function.getName() + "\n")
            f.write("// Address:  " + function.getEntryPoint().toString() + "\n")
            f.write("// ==========================================================\n")

            # Decompile the function
            results = decomplib.decompileFunction(function, 0, monitor)
            if results.decompileCompleted():
                markup = results.getCCodeMarkup()
                if markup:
                    f.write(markup.toString() + "\n\n")
                else:
                    f.write("// [Failed to get C Code Markup]\n\n")
            else:
                f.write("// [Decompilation failed or timed out]\n\n")

    print("Finished decompilation dump.")

if __name__ == "__main__":
    dump_all_functions()
