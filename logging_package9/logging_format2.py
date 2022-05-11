"""
Logging Format
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
"""

import logging

logging.basicConfig(filename="selenium_automation_testing_with_python/selenium_test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.DEBUG, filemode="w")
logging.info("Info Message")
logging.debug("Debug Message")
logging.error("Error Message")
logging.warning("Warning Message")
logging.critical("Critical Message")