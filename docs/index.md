# AdiZen-Cyber-Toolkit Documentation

Welcome to the AdiZen-Cyber-Toolkit docs.
Here you'll find usage examples, API references, and developer notes.

## Tools

### adizenauditor — System Auditor
```bash
python3 -m adizen_cyber_toolkit.adizenauditor
```

### adizenscanner — Port Scanner
```bash
python3 -m adizen_cyber_toolkit.adizenscanner --target 192.168.1.1 --ports 22,80,443
```

### adizenhasher — Hash Generator
```bash
python3 -m adizen_cyber_toolkit.adizenhasher --text "hello world" --algo sha256
python3 -m adizen_cyber_toolkit.adizenhasher --text "hello world" --algo md5
```

### adizenspider — Web Spider
```bash
python3 -m adizen_cyber_toolkit.adizenspider --url https://example.com --limit 20
```

### adizencracker — Password Strength
```bash
python3 -m adizen_cyber_toolkit.adizencracker --password "MyPassword123!"
python3 -m adizen_cyber_toolkit.adizencracker --password "abc" --bruteforce
```

### adizenfilter — Text Sanitizer
```bash
python3 -m adizen_cyber_toolkit.adizenfilter --text "<p>Hello <b>world</b></p>"
```

### adizeninspector — File Inspector
```bash
python3 -m adizen_cyber_toolkit.adizeninspector --file /etc/hosts
```

### adizenhello — Environment Check
```bash
python3 -m adizen_cyber_toolkit.adizenhello
```

## Using as a Library
```python
from adizen_cyber_toolkit import adizenscanner, adizenhasher

# Scan ports
results = adizenscanner.scan_ports("192.168.1.1", [22, 80, 443])
print(results)  # {22: 'OPEN', 80: 'OPEN', 443: 'CLOSED'}

# Generate hash
hash_val = adizenhasher.generate_hash("hello world", "sha256")
print(hash_val)
```
