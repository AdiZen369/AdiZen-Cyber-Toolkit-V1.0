#!/usr/bin/env python3
"""
AdiZen Auditor
---------------
System and configuration auditing utility for AdiZen-Cyber-Toolkit.

Usage:
    python3 -m adizen_cyber_toolkit.adizenauditor
"""

import platform
import sys
import socket

try:
    from importlib.metadata import packages_distributions
    def _get_packages(limit=10):
        pkgs = sorted(packages_distributions().keys())
        return pkgs[:limit]
except ImportError:
    import pkg_resources
    def _get_packages(limit=10):
        return sorted([str(p) for p in pkg_resources.working_set])[:limit]


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
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        sock.close()
        return True
    except Exception:
        return False


def installed_packages(limit=10):
    """List installed Python packages (limited for readability)."""
    return _get_packages(limit)


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
