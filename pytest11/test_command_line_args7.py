"""
Command to run pytest as command line arguments
py.test -s -v selenium_automation_testing_with_python/pytest11/test_command_line_args7.py --browser firefox

"""


def test_command_line_methodA(oneTimeSetUp, setUp):
    print("Running test method A")

def test_command_line_methodB(oneTimeSetUp, setUp):
    print("Running test method B")