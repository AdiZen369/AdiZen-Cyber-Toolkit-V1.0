#!/usr/bin/env bash
# AdiZenWorks Cybersecurity Toolkit V1 — Launch Desktop GUI
set -e
cd "$(dirname "$0")"
python3 desktop/main.py "$@"
