import unittest
from adizen_cyber_toolkit import adizenfilter


class TestAdiZenFilter(unittest.TestCase):
    def test_removes_html_tags(self):
        dirty = "<p>Hello   world</p>"
        clean = adizenfilter.sanitize(dirty)
        self.assertEqual(clean, "Hello world")

    def test_normalises_whitespace(self):
        self.assertEqual(adizenfilter.sanitize("  hello   world  "), "hello world")

    def test_no_tags(self):
        self.assertEqual(adizenfilter.sanitize("plain text"), "plain text")


if __name__ == "__main__":
    unittest.main()
