
---

## 📂 `tests/test_adizenauditor.py`
```python
import unittest
import tools.adizenauditor as auditor

class TestAdiZenAuditor(unittest.TestCase):
    def test_run(self):
        result = auditor.main()
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()