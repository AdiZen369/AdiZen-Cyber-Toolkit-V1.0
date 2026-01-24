#!/usr/bin/env python3
"""
AdiZen Inspector
---------------
File and process inspection utility.
"""

import argparse
import os


def inspect_file(path):
    if not os.path.exists(path):
        return f"File not found: {path}"
    stats = os.stat(path)
    return {
        "Size": stats.st_size,
        "Last Modified": stats.st_mtime,
        "Permissions": stats.st_mode,
    }


def main():
    parser = argparse.ArgumentParser(description="AdiZen Inspector")
    parser.add_argument("--file", required=True, help="File path to inspect")
    args = parser.parse_args()

    print(f"🔍 Inspecting {args.file}...\n")
    result = inspect_file(args.file)
    print(result)


if __name__ == "__main__":
    main()