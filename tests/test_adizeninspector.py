import unittest
import os
import tempfile
from adizen_cyber_toolkit import adizeninspector


class TestAdiZenInspector(unittest.TestCase):
    def test_inspect_existing_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(b"test content")
            tmppath = f.name
        try:
            result = adizeninspector.inspect_file(tmppath)
            self.assertIsInstance(result, dict)
            self.assertIn("Size (bytes)", result)
            self.assertEqual(result["Size (bytes)"], 12)
        finally:
            os.remove(tmppath)

    def test_inspect_missing_file(self):
        result = adizeninspector.inspect_file("/nonexistent/path/file.txt")
        self.assertIsInstance(result, str)
        self.assertIn("not found", result)


if __name__ == "__main__":
    unittest.main()
