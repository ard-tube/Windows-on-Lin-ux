#!/bin/bash

# Arda-OS Windows Bridge v1.0

if ! command -v wine &> /dev/null; then
    sudo dpkg --add-architecture i386
    sudo apt update && sudo apt install -y wine64 wine32
fi

export __NV_PRIME_RENDER_OFFLOAD=1
export __GLX_VENDOR_LIBRARY_NAME=nvidia

if [ -z "$1" ]; then
    echo "Error: No .exe path specified."
    echo "Usage: ./run-windows.sh /path/to/file.exe"
else
    echo "Launching $1 with NVIDIA..."
    wine "$1"
fi
