# C/C++ Coding Guidelines for AI Decompilation

## 1. Naming Conventions
- **Classes/Structs:** PascalCase (e.g., `ShellBrowserWindow`, `TaskbarController`).
- **Methods/Functions:** PascalCase for Win32/COM public APIs (e.g., `Initialize()`), camelCase for internal helpers (e.g., `calculateOffset()`).
- **Variables:** camelCase (e.g., `hwndMain`, `pidlRoot`). Prefix globals with `g_` and members with `m_`.
- **Constants/Macros:** UPPER_SNAKE_CASE (e.g., `MAX_PATH_LENGTH`).

## 2. Pointer Arithmetic and Casts
- **Avoid Raw Casts:** Do not use C-style casts (`(int)x`). Use modern C++ casts (`static_cast`, `reinterpret_cast`) exclusively.
- **Pointer Math:** Minimize manual pointer arithmetic. Where necessary, document the layout assumption explicitly.

## 3. Control Flow
- **De-flattening:** Eliminate `goto` statements resulting from compiler optimizations. Reconstruct logical `while`, `for`, and `if-else` blocks.
- **Early Returns:** Prefer early returns over deeply nested `if` blocks to improve readability.
