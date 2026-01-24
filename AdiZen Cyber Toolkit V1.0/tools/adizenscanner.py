#!/usr/bin/env python3
"""
AdiZen Scanner
---------------
Simple network and port scanner.

Usage:
    python3 tools/adizenscanner.py --target 192.168.1.1 --ports 22,80,443
"""

import argparse
import socket


def scan_ports(target, ports):
    results = {}
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            sock.close()
            results[port] = "OPEN" if result == 0 else "CLOSED"
        except Exception:
            results[port] = "ERROR"
    return results


def main():
    parser = argparse.ArgumentParser(description="AdiZen Scanner")
    parser.add_argument("--target", required=True, help="Target IP or hostname")
    parser.add_argument("--ports", default="22,80,443", help="Comma-separated list of ports")
    args = parser.parse_args()

    ports = [int(p.strip()) for p in args.ports.split(",")]
    print(f"🔍 Scanning {args.target}...\n")

    results = scan_ports(args.target, ports)
    for port, status in results.items():
        print(f"Port {port}: {status}")

    return results


if __name__ == "__main__":
    main()