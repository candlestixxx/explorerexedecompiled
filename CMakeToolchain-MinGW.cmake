# CMakeToolchain-MinGW.cmake
# Toolchain file for cross-compiling to Windows on a Linux host using MinGW-w64.

# Define the target system
set(CMAKE_SYSTEM_NAME Windows)
set(CMAKE_SYSTEM_PROCESSOR x86_64)

# Set compilers
set(CMAKE_C_COMPILER x86_64-w64-mingw32-gcc)
set(CMAKE_CXX_COMPILER x86_64-w64-mingw32-g++)

# Find programs on the host system
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)

# Search for headers and libraries only in the target environment
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
