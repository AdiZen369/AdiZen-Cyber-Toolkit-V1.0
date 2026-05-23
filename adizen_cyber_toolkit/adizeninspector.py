#!/usr/bin/env python3
"""
AdiZen Inspector
---------------
File and process inspection utility.

Usage:
    python3 -m adizen_cyber_toolkit.adizeninspector --file /etc/hosts
"""

import argparse
import os
import datetime


def inspect_file(path):
    """Return a dict of file metadata, or an error string if not found."""
    if not os.path.exists(path):
        return f"File not found: {path}"
    stats = os.stat(path)
    return {
        "Path": os.path.abspath(path),
        "Size (bytes)": stats.st_size,
        "Last Modified": datetime.datetime.fromtimestamp(stats.st_mtime).isoformat(),
        "Permissions (octal)": oct(stats.st_mode),
    }


def main():
    parser = argparse.ArgumentParser(description="AdiZen Inspector – File Inspector")
    parser.add_argument("--file", required=True, help="File path to inspect")
    args = parser.parse_args()

    print(f"🔍 Inspecting {args.file}...\n")
    result = inspect_file(args.file)
    if isinstance(result, dict):
        for k, v in result.items():
            print(f"{k}: {v}")
    else:
        print(result)


if __name__ == "__main__":
    main()
