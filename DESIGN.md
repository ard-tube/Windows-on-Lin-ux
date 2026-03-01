# Design Document

## Objective
To provide a lightweight, efficient bridge for running Windows applications on Linux with native NVIDIA GPU support.

## Component Breakdown
1. **Frontend (Python/Tkinter):** Provides a simple GUI for file selection and execution monitoring.
2. **Backend (Bash Script):** Handles environment variables and interacts with the Wine compatibility layer.
3. **Graphics Engine:** Utilizes NVIDIA PRIME offloading for RTX 2050 performance.

## Data Flow
User Interface -> .exe Path Capture -> Bash Wrapper -> Environment Variable Export -> Wine Execution.
