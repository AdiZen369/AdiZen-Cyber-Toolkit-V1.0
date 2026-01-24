import unittest
import tools.adizenhasher as h

class TestAdiZenHasher(unittest.TestCase):
    def test_generate_hash(self):
        result = h.generate_hash("hello", "md5")
        self.assertEqual(len(result), 32)  # MD5 hashes are 32 hex chars

if __name__ == "__main__":
    unittest.main()