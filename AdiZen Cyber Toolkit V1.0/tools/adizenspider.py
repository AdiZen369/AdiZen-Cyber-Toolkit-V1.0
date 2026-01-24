#!/usr/bin/env python3
"""
AdiZen Spider
---------------
Basic web spider for crawling and reconnaissance.

Usage:
    python3 tools/adizenspider.py --url https://example.com
"""

import argparse
import requests
from bs4 import BeautifulSoup


def crawl(url, limit=10):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        links = [a.get("href") for a in soup.find_all("a", href=True)]
        return links[:limit]
    except Exception as e:
        return [f"Error: {e}"]


def main():
    parser = argparse.ArgumentParser(description="AdiZen Spider")
    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--limit", type=int, default=10, help="Limit number of links")
    args = parser.parse_args()

    print(f"🕷️ Crawling {args.url}...\n")
    links = crawl(args.url, args.limit)
    for link in links:
        print(f" - {link}")

    return links


if __name__ == "__main__":
    main()