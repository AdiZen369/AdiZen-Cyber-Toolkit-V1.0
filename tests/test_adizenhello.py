import unittest
from adizen_cyber_toolkit import adizenhello


class TestAdiZenHello(unittest.TestCase):
    def test_main_runs(self):
        # main() prints and returns None
        result = adizenhello.main()
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
