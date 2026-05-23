cmake_minimum_required(VERSION 3.10)
project(ExplorerDecompiled VERSION 0.1.0 LANGUAGES CXX)

# Set C++ Standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# The goal is to verify compilability, so we define a static library
# target instead of an executable, since we don't have a full main()
# yet and just want to verify the syntax and linking of the decompiled files.

# Add the include directory
include_directories(include)

# Gather all auto-segmented C++ source files
file(GLOB SOURCES "src/*.cpp")

# Create a static library target
if(SOURCES)
    add_library(ExplorerDecompiledStatic STATIC ${SOURCES})

    # Ideally this would be compiled with MSVC targeting Windows,
    # but for baseline CI verification on Linux/WSL, we suppress missing
    # Windows-specific attributes if compiling with Clang/GCC
    if (NOT MSVC)
        target_compile_options(ExplorerDecompiledStatic PRIVATE -w)
    endif()
else()
    message(WARNING "No C++ source files found in src/ directory.")
endif()
