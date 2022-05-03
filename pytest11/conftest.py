import pytest

@pytest.fixture(scope="class")
def oneTimeSetUp(browser, osType):
    print("\n\nI will run once before every test class/module")
    if browser == "firefox":
        print("Running test on firefox")
    else:
        print("Running test on chrome")
    yield
    print("\n\nI will run once after every test class/module")


@pytest.fixture()
def setUp():
    print("\nI will run once before every test function/method")
    yield
    print("\nI will run once after every test function/method")

def pytest_addoption(parser):
    parser.addoption("--browser", help="Type of browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("osType")