#!/usr/bin/env python3
"""
AdiZen Filter
---------------
Data filtering and sanitization helper.

Usage:
    python3 -m adizen_cyber_toolkit.adizenfilter --text "<p>Hello world</p>"
"""

import argparse
import re


def sanitize(text):
    """Remove HTML tags and normalise whitespace."""
    clean = re.sub(r"<.*?>", "", text)
    return " ".join(clean.split())


def main():
    parser = argparse.ArgumentParser(description="AdiZen Filter – Text Sanitizer")
    parser.add_argument("--text", required=True, help="Text to sanitize")
    args = parser.parse_args()

    print("🧹 Sanitized text:\n")
    print(sanitize(args.text))


if __name__ == "__main__":
    main()
