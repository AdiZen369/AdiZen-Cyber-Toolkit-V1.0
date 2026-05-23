#!/usr/bin/env python3
"""
AdiZen Hello
---------------
Introductory script and environment check.
"""

import sys
import platform


def main():
    print("👋 Welcome to AdiZen-Cyber-Toolkit!")
    print(f"Python {sys.version.split()[0]} on {platform.system()}")
    print("Your environment is ready to run security utilities.")


if __name__ == "__main__":
    main()
