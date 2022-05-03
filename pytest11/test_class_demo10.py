import pytest
from class_to_test8 import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestClassDemo():
    
    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.abc = SomeClassToTest(self.value)
    
    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running test method A")
    
    def test_methodB(self):
        print("Running test method B")