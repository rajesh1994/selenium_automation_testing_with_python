"""
https://docs.python.org/3/library/unittest.html#unittest.TestCase
"""
import unittest

class AssertDemo(unittest.TestCase):
    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is flase")
        b = False
        self.assertFalse(b, "b is true")
    
    def test_assertEqual(self):
        a = "Test"
        b = "Test "
        self.assertEqual(a, b, "a & b is not equal")

if __name__ == "__main__":
    unittest.main(verbosity=2)