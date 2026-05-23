# 🛡️ AdiZen-Cyber-Toolkit-V1.0

![Tests](https://github.com/AdiZen369/AdiZen-Cyber-Toolkit-V1.0/actions/workflows/tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/AdiZen369/AdiZen-Cyber-Toolkit-V1.0/branch/main/graph/badge.svg)](https://codecov.io/gh/AdiZen369/AdiZen-Cyber-Toolkit-V1.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

AdiZen-Cyber-Toolkit-V1.0 is a collection of lightweight Python-based cybersecurity utilities designed for auditing, inspection, and exploration.
The toolkit provides modular scripts that can be used individually or integrated into larger workflows for security testing and automation.

## ⚠️ Ethical Use Only
This toolkit is designed for **authorized security testing only**. Always obtain explicit written permission before testing systems you do not own.

## 📂 Tools Included

| Tool | Description |
|------|-------------|
| **adizenauditor.py** | System and configuration auditing utility |
| **adizencracker.py** | Password strength tester and brute-force demo |
| **adizenfilter.py** | Data filtering and sanitization helper |
| **adizenhasher.py** | Hash generator (MD5, SHA-256, etc.) |
| **adizenhello.py** | Environment check and welcome script |
| **adizeninspector.py** | File and process inspection utility |
| **adizenscanner.py** | Simple network and port scanner |
| **adizenspider.py** | Web spider for crawling and reconnaissance |

## 🚀 Getting Started

### Installation
```bash
git clone https://github.com/AdiZen369/AdiZen-Cyber-Toolkit-V1.0
cd AdiZen-Cyber-Toolkit-V1.0
pip install -r requirements.txt
```

### Usage
Run any tool as a Python module:
```bash
python3 -m adizen_cyber_toolkit.adizenscanner --target 192.168.1.1 --ports 22,80,443
python3 -m adizen_cyber_toolkit.adizenhasher --text "hello world" --algo sha256
python3 -m adizen_cyber_toolkit.adizenspider --url https://example.com
python3 -m adizen_cyber_toolkit.adizencracker --password MyPassword123
python3 -m adizen_cyber_toolkit.adizeninspector --file /etc/hosts
python3 -m adizen_cyber_toolkit.adizenauditor
```

### Run Tests
```bash
pip install pytest pytest-cov
pytest --cov=adizen_cyber_toolkit --cov-report=term-missing
```

## 📁 Project Structure
```
AdiZen-Cyber-Toolkit-V1.0/
├── adizen_cyber_toolkit/    # Source modules
│   ├── __init__.py
│   ├── adizenauditor.py
│   ├── adizencracker.py
│   ├── adizenfilter.py
│   ├── adizenhasher.py
│   ├── adizenhello.py
│   ├── adizeninspector.py
│   ├── adizenscanner.py
│   └── adizenspider.py
├── tests/                   # Unit tests
├── docs/                    # Documentation
├── .github/workflows/       # CI/CD
├── requirements.txt
├── setup.py
└── README.md
```

## 🗺️ Roadmap
- **v1.0** – Initial release (8 command-line utilities) ✅
- **v2.0** – Desktop GUI (Tkinter) + Web dashboard (Flask) + AI integration 🚀

## 📜 License
MIT License — see [LICENSE](LICENSE) for details.

## 🏢 About
**AdiZenWorks Inc.** — Securing Your Digital Future  
📧 Contact: security@adizenworks.com
