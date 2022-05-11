from unittest import result
import pytest
from class_to_test8 import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestClassDemo():
    
    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.abc = SomeClassToTest(10)
    
    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running test method A")
    
    def test_methodB(self):
        result = self.abc.sumNumbers(5, 5)
        assert result == 20
        print("Running test method B")
    
    def test_methodC(self):
        print("Running test method C")