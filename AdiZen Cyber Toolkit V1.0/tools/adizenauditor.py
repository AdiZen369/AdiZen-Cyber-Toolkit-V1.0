#!/usr/bin/env python3
"""
AdiZen Auditor
---------------
System and configuration auditing utility for AdiZen-Cyber-Toolkit.

This script performs basic checks on the host system:
- OS information
- Python environment
- Installed packages
- Network connectivity

Usage:
    python3 tools/adizenauditor.py
"""

import platform
import sys
import socket
import pkg_resources


def system_info():
    """Collect basic system information."""
    return {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": sys.version.split()[0],
    }


def network_check(host="8.8.8.8", port=53, timeout=3):
    """Check basic network connectivity (default: Google DNS)."""
    try:
        socket.setdefaulttimeout(timeout)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.close()
        return True
    except Exception:
        return False


def installed_packages(limit=10):
    """List installed Python packages (limited for readability)."""
    packages = sorted([str(p) for p in pkg_resources.working_set])
    return packages[:limit]


def main():
    """Entry point for AdiZen Auditor."""
    print("🔍 AdiZen Auditor – System Audit Report\n")

    info = system_info()
    for key, value in info.items():
        print(f"{key}: {value}")

    print("\n📡 Network Connectivity:", "OK" if network_check() else "FAILED")

    print("\n📦 Installed Packages (sample):")
    for pkg in installed_packages():
        print(f" - {pkg}")

    return info


if __name__ == "__main__":
    main()