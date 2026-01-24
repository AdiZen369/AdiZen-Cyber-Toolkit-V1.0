import unittest
import tools.adizencracker as cracker

class TestAdiZenCracker(unittest.TestCase):
    def test_strength(self):
        self.assertEqual(cracker.check_strength("abc"), "Weak")
        self.assertIn(cracker.check_strength("Abc123!"), ["Strong","Very Strong","Excellent"])

    def test_bruteforce(self):
        result = cracker.brute_force("a", max_len=1)
        self.assertIn("Password cracked", result)

if __name__ == "__main__":
    unittest.main()