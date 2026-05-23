import unittest
from adizen_cyber_toolkit import adizenhasher


class TestAdiZenHasher(unittest.TestCase):
    def test_md5_length(self):
        result = adizenhasher.generate_hash("hello", "md5")
        self.assertEqual(len(result), 32)

    def test_sha256_length(self):
        result = adizenhasher.generate_hash("hello", "sha256")
        self.assertEqual(len(result), 64)

    def test_sha512_length(self):
        result = adizenhasher.generate_hash("hello", "sha512")
        self.assertEqual(len(result), 128)

    def test_unsupported_algorithm(self):
        result = adizenhasher.generate_hash("hello", "fakealgo")
        self.assertIn("Unsupported", result)

    def test_consistent_hash(self):
        r1 = adizenhasher.generate_hash("hello", "sha256")
        r2 = adizenhasher.generate_hash("hello", "sha256")
        self.assertEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()
