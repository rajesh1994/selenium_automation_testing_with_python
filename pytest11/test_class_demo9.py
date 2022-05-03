import pytest
from selenium_automation_testing_with_python.pytest11.class_to_test8 import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():
    
    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.abc = SomeClassToTest(15)
    
    def test_methodA(self):
        result = self.abc.sumNumbers(5, 15)
        assert result == 35
        print("Running test method A")
    
    def test_methodB(self):
        print("Running test method B")