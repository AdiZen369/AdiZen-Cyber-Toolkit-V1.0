#!/usr/bin/env python3
"""
AdiZen Cracker
---------------
Basic password strength tester and brute-force demo.

Usage:
    python3 -m adizen_cyber_toolkit.adizencracker --password MyPass123!
"""

import argparse
import itertools
import string


def check_strength(password):
    """Evaluate password strength. Returns: Weak / Moderate / Strong / Very Strong."""
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([length >= 8, has_upper, has_digit, has_special])
    levels = ["Weak", "Moderate", "Strong", "Very Strong"]
    return levels[min(score, len(levels) - 1)]


def brute_force(target, max_len=4):
    """Brute-force demo for short lowercase passwords only (educational)."""
    chars = string.ascii_lowercase
    for length in range(1, max_len + 1):
        for attempt in itertools.product(chars, repeat=length):
            if "".join(attempt) == target:
                return f"Password cracked: {target}"
    return "Not cracked within search space"


def main():
    parser = argparse.ArgumentParser(description="AdiZen Cracker – Password Strength Tester")
    parser.add_argument("--password", required=True, help="Password to test")
    parser.add_argument("--bruteforce", action="store_true", help="Run brute-force demo (max 4 chars)")
    args = parser.parse_args()

    print(f"🔑 Password strength: {check_strength(args.password)}")

    if args.bruteforce:
        print(brute_force(args.password))


if __name__ == "__main__":
    main()
