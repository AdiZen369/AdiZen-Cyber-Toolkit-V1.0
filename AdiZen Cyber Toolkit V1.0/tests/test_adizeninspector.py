import unittest
import os
import tools.adizeninspector as inspector

class TestAdiZenInspector(unittest.TestCase):
    def test_inspect_file(self):
        # Create a temporary file
        tmpfile = "temp.txt"
        with open(tmpfile, "w") as f:
            f.write("test")
        result = inspector.inspect_file(tmpfile)
        self.assertIn("Size", result)
        os.remove(tmpfile)

if __name__ == "__main__":
    unittest.main()