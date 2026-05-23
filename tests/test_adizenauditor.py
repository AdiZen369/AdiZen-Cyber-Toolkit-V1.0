import unittest
from adizen_cyber_toolkit import adizenauditor


class TestAdiZenAuditor(unittest.TestCase):
    def test_system_info(self):
        info = adizenauditor.system_info()
        self.assertIn("OS", info)
        self.assertIn("Python Version", info)

    def test_network_check_returns_bool(self):
        result = adizenauditor.network_check()
        self.assertIsInstance(result, bool)

    def test_installed_packages(self):
        pkgs = adizenauditor.installed_packages(limit=5)
        self.assertIsInstance(pkgs, list)

    def test_main(self):
        result = adizenauditor.main()
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
