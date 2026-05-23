import unittest
from adizen_cyber_toolkit import adizencracker


class TestAdiZenCracker(unittest.TestCase):
    def test_weak_password(self):
        self.assertEqual(adizencracker.check_strength("abc"), "Weak")

    def test_moderate_password(self):
        self.assertEqual(adizencracker.check_strength("abcdefgh"), "Moderate")

    def test_strong_password(self):
        result = adizencracker.check_strength("Abcdefg1!")
        self.assertIn(result, ["Strong", "Very Strong"])

    def test_bruteforce_found(self):
        result = adizencracker.brute_force("a", max_len=1)
        self.assertIn("Password cracked", result)

    def test_bruteforce_not_found(self):
        result = adizencracker.brute_force("zzz1", max_len=2)
        self.assertIn("Not cracked", result)


if __name__ == "__main__":
    unittest.main()
