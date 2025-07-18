import os
import unittest

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(current_dir, "sweetshop_final", "tests")

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=tests_dir, pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
