import unittest
from adizen_cyber_toolkit import adizenscanner


class TestAdiZenScanner(unittest.TestCase):
    def test_scan_returns_dict(self):
        result = adizenscanner.scan_ports("localhost", [22, 80])
        self.assertIsInstance(result, dict)
        self.assertIn(22, result)
        self.assertIn(80, result)

    def test_port_status_values(self):
        result = adizenscanner.scan_ports("localhost", [22])
        self.assertIn(result[22], ["OPEN", "CLOSED", "ERROR"])


if __name__ == "__main__":
    unittest.main()
