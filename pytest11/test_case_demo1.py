import pytest

@pytest.fixture()
def setUp():
    print("\n\nI will run once before every test function/method")

def test_demo1_methodA(setUp):
    print("Running test method A")

def test_demo1_methodB(setUp):
    print("Running test method B")