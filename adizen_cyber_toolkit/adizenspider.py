#!/usr/bin/env python3
"""
AdiZen Spider
---------------
Basic web spider for crawling and link reconnaissance.

Usage:
    python3 -m adizen_cyber_toolkit.adizenspider --url https://example.com --limit 20
"""

import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def crawl(url, limit=10):
    """Crawl a URL and return up to `limit` links found on the page."""
    try:
        headers = {"User-Agent": "AdiZen-Spider/1.0 (Security Scanner)"}
        response = requests.get(url, timeout=5, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        links = []
        for a in soup.find_all("a", href=True):
            full_url = urljoin(url, a["href"])
            if urlparse(full_url).scheme in ("http", "https"):
                links.append(full_url)
        return links[:limit]
    except Exception as e:
        return [f"Error: {e}"]


def main():
    parser = argparse.ArgumentParser(description="AdiZen Spider – Web Crawler")
    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--limit", type=int, default=10, help="Max number of links to return")
    args = parser.parse_args()

    print(f"🕷️  Crawling {args.url}...\n")
    links = crawl(args.url, args.limit)
    for link in links:
        print(f" - {link}")

    return links


if __name__ == "__main__":
    main()
