#!/usr/bin/env python3
"""
AdiZen Hasher
---------------
Hash generator and validator (MD5, SHA-1, SHA-256, SHA-512).

Usage:
    python3 -m adizen_cyber_toolkit.adizenhasher --text "hello world" --algo sha256
"""

import argparse
import hashlib


SUPPORTED = ["md5", "sha1", "sha256", "sha512"]


def generate_hash(text, algo="sha256"):
    """Generate a hex digest for the given text using the specified algorithm."""
    if algo not in SUPPORTED:
        return f"Unsupported algorithm: {algo}. Choose from: {', '.join(SUPPORTED)}"
    h = hashlib.new(algo)
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description="AdiZen Hasher – Hash Generator")
    parser.add_argument("--text", required=True, help="Text to hash")
    parser.add_argument("--algo", default="sha256",
                        help=f"Hash algorithm ({', '.join(SUPPORTED)})")
    args = parser.parse_args()

    print(f"🔑 Hashing with {args.algo}...\n")
    result = generate_hash(args.text, args.algo)
    print(f"Result: {result}")
    return result


if __name__ == "__main__":
    main()
