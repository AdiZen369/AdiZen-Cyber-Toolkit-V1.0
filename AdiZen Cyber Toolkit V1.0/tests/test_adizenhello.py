import unittest
import tools.adizenhello as hello

class TestAdiZenHello(unittest.TestCase):
    def test_main(self):
        result = hello.main()
        self.assertIsNone(result)  # main prints, returns None

if __name__ == "__main__":
    unittest.main()