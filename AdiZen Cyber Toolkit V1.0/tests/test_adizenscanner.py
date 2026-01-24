import unittest
import tools.adizenscanner as scanner

class TestAdiZenScanner(unittest.TestCase):
    def test_scan_ports(self):
        result = scanner.scan_ports("localhost", [22])
        self.assertIn(22, result)

if __name__ == "__main__":
    unittest.main()