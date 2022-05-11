import pytest

@pytest.fixture()
def setUp():
    print("\nI will run once before every test function/method")
    yield
    print("\nI will run once after every test function/method")

def test_demo2_methodA(setUp):
    print("Running test method A")

def test_demo2_methodB(setUp):
    print("Running test method B")