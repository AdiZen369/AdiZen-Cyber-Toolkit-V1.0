#!/usr/bin/env python3
"""
AdiZen Cracker
---------------
Basic password strength tester and brute-force demo.
"""

import argparse
import itertools
import string


def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([length >= 8, has_upper, has_digit, has_special])
    levels = ["Weak", "Moderate", "Strong", "Very Strong"]
    return levels[score] if score < len(levels) else "Excellent"


def brute_force(target, max_len=4):
    chars = string.ascii_lowercase
    for length in range(1, max_len + 1):
        for attempt in itertools.product(chars, repeat=length):
            if "".join(attempt) == target:
                return f"Password cracked: {target}"
    return "Not cracked"


def main():
    parser = argparse.ArgumentParser(description="AdiZen Cracker")
    parser.add_argument("--password", required=True, help="Password to test")
    parser.add_argument("--bruteforce", action="store_true", help="Run brute-force demo")
    args = parser.parse_args()

    print(f"🔑 Password strength: {check_strength(args.password)}")

    if args.bruteforce:
        print(brute_force(args.password))


if __name__ == "__main__":
    main()