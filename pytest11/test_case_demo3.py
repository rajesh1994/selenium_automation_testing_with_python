"""
file name should start with test
test method name should start with test

py.test test_mod.py                     # run tests in module
py.test somepath                        # run all tests below somepath
py.test test_module.py::test_method     # only run test_method in test_module
py.test test_case*.py                   # run similar files starts with same file name by using     wildcard symbol

-s to print statements
-v verbose
"""


import pytest

@pytest.fixture()
def setUp():
    print("\nI will run once before every test function/method")
    yield
    print("\nI will run once after every test function/method")

def test_demo3_methodA(setUp):
    print("Running test method A")

def test_demo3_methodB(setUp):
    print("Running test method B")