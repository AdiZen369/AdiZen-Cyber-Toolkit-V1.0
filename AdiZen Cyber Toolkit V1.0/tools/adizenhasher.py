#!/usr/bin/env python3
"""
AdiZen Hasher
---------------
Hash generator and validator (MD5, SHA256, etc.).

Usage:
    python3 tools/adizenhasher.py --text "hello world" --algo sha256
"""

import argparse
import hashlib


def generate_hash(text, algo="sha256"):
    try:
        h = hashlib.new(algo)
        h.update(text.encode("utf-8"))
        return h.hexdigest()
    except ValueError:
        return f"Unsupported algorithm: {algo}"


def main():
    parser = argparse.ArgumentParser(description="AdiZen Hasher")
    parser.add_argument("--text", required=True, help="Text to hash")
    parser.add_argument("--algo", default="sha256", help="Hash algorithm (md5, sha1, sha256, etc.)")
    args = parser.parse_args()

    print(f"🔑 Hashing text with {args.algo}...\n")
    result = generate_hash(args.text, args.algo)
    print(f"Result: {result}")

    return result


if __name__ == "__main__":
    main()