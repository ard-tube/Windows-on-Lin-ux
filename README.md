# Windows on Linux Bridge 🐧

A high-performance wrapper designed to run Windows binaries on Linux environments using Wine and NVIDIA hardware acceleration.

## Features 🌟
- Seamless execution of Windows applications (.exe).
- Native NVIDIA GPU acceleration (Optimized for RTX 2050 series).
- Automated environment configuration for high-resource software.

## System Requirements ⚙️
- **OS:** Linux (/ Ubuntu / Debian / arch linux "Ubuntu" is recommended).
- **GPU:** NVIDIA OR AMD series (Optimized for AMD.
- **RAM:** Minimum 8GB recommended for stable execution.

## Quick Installation 🚀
1. Update your package list:
   `sudo apt update`
2. Install Wine dependencies:
   `sudo dpkg --add-architecture i386 && sudo apt install wine64 wine32`.
3. Clone this repository and grant permissions:
   `chmod +x run-windows-on-linux.sh`.

## Usage Guide 📚
To launch a Windows application with GPU offloading, run:
`./run-windows-on-linux.sh /path/to/your/application.exe`.

## Project Structure 📂
- `src/`: Core Python and Shell logic.
- `docs/`: Technical architecture and design docs.
- `run-windows-on-linux.sh`: Main entry point script.

## Supported Applications 📱
- Development Tools
- Design Software (Adobe Suite via Wine)
- General Productivity Tools

## Troubleshooting ⚠️
- **NVIDIA Issues:** Ensure `nvidia-driver` is correctly installed and active.
- **Launch Failure:** Check if the application requires specific DLL overrides in Wine configuration.
