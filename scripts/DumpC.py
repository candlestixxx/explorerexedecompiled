# Ghidra Headless Script
# Extracts decompiled C code from all functions
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor
import java.io.File

def dump_c():
    output_path = "/workspace/src/monolithic_output.c"
    print("Dumping C pseudocode to {}".format(output_path))

    decompInterface = DecompInterface()
    decompInterface.openProgram(currentProgram)
    monitor = ConsoleTaskMonitor()

    fm = currentProgram.getFunctionManager()
    funcs = fm.getFunctions(True)

    # Use io.open or specify encoding in Python 3. Jython 2.7 needs special handling for unicode.
    import codecs
    with codecs.open(output_path, "w", "utf-8") as f:
        f.write("// Auto-generated C output via Ghidra Decompiler\n")

        for func in funcs:
            if func.isExternal() or func.isThunk():
                continue

            res = decompInterface.decompileFunction(func, 0, monitor)
            if res.decompileCompleted():
                ccode = res.getDecompiledFunction().getC()
                f.write(ccode)
                f.write("\n")

dump_c()
