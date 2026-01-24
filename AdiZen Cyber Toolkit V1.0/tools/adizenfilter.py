#!/usr/bin/env python3
"""
AdiZen Filter
---------------
Data filtering and sanitization helper.
"""

import argparse
import re


def sanitize(text):
    # Remove HTML tags and extra spaces
    clean = re.sub(r"<.*?>", "", text)
    return " ".join(clean.split())


def main():
    parser = argparse.ArgumentParser(description="AdiZen Filter")
    parser.add_argument("--text", required=True, help="Text to sanitize")
    args = parser.parse_args()

    print("🧹 Sanitized text:\n")
    print(sanitize(args.text))


if __name__ == "__main__":
    main()