cmake_minimum_required(VERSION 3.15)
project(ExplorerDecompiledStatic VERSION 1.2.3 LANGUAGES CXX C)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

include_directories(include)
file(GLOB_RECURSE SRC_FILES "src/*.cpp" "src/*.c")

if(NOT SRC_FILES)
    message(WARNING "No source files found in src/. Adding a mock file to prevent CMake error.")
    file(WRITE "${CMAKE_BINARY_DIR}/mock.cpp" "int main() { return 0; }")
    set(SRC_FILES "${CMAKE_BINARY_DIR}/mock.cpp")
endif()

add_library(ExplorerDecompiledStatic STATIC ${SRC_FILES})
set_target_properties(ExplorerDecompiledStatic PROPERTIES LINKER_LANGUAGE CXX)
target_link_libraries(ExplorerDecompiledStatic ole32 uuid)
