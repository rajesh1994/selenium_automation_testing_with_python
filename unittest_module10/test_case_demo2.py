"""
Just follow this link to see how you can add PYTHONPATH to environment variable

Windows:
http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7

Mac/Linux:
http://stackoverflow.com/questions/3387695/add-to-python-path-mac-os-x
"""


import unittest

class TestCaseDemo2(unittest.TestCase):
    #Class level setUp
    @classmethod
    def setUpClass(cls):
        print("*" * 50)
        print("I will run only once before all tests funtions")
        print("*" * 50)
    
    #Function level setUp
    def setUp(self):
        print("\n\nI will run once before every test funtion")
    
    def test_methodA(self):
        print("Test method A")
    
    def test_methodB(self):
        print("Test method B")
    
    #Function level tearDown
    def tearDown(self):
        print("\nI will run once after every test funtion")
    
    #Class level tearDown
    @classmethod
    def tearDownClass(cls):
        print("*" * 50)
        print("I will run only once after all test functions")
        print("*" * 50)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)