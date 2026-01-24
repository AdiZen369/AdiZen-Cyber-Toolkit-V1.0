import unittest
import tools.adizenfilter as f

class TestAdiZenFilter(unittest.TestCase):
    def test_sanitize(self):
        dirty = "<p>Hello   world</p>"
        clean = f.sanitize(dirty)
        self.assertEqual(clean, "Hello world")

if __name__ == "__main__":
    unittest.main()