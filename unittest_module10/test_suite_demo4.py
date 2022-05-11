import unittest
from test_case_demo1 import TestCaseDemo1
from test_case_demo2 import TestCaseDemo2
import sys
import os # if you want this directory

try:
    sys.path.index(os.getcwd()) # Or os.getcwd() for this directory
except ValueError:
    sys.path.append(os.getcwd()) # Or os.getcwd() for this directory

#Get all tests from from TestCaseDemo1 & TestCaseDemo2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)

#Create a test suite combining TestCaseDemo1 & TestCaseDemo2
smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)