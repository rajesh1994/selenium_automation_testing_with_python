import pytest

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("\n\nI will run once before every test class")
    if browser == 'firefox':
        value = 10
        print("Running tests on FF")
    else:
        value = 20
        print("Running tests on chrome")

    if request.cls is not None:
        request.cls.value = value

    yield value
    print("\n\nI will run once after every test class")

@pytest.fixture()
def setUp():
    print("\nI will run once before every test function/method")
    yield
    print("\nI will run once after every test function/method")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")