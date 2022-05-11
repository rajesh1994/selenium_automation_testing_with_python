import unittest

class TestCaseDemo1(unittest.TestCase):
    def setUp(self):
        print("\n\nI will run once before every test function/method")
    
    def test_methodA(self):
        print("Test method A")
    
    def test_methodB(self):
        print("Test method B")
    
    def tearDown(self):
        print("I will run once after every test function\n")

if __name__ == '__main__':
    unittest.main(verbosity=2)