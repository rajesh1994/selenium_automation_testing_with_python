"""
    Python Logging Levels
        Notset = 0: This is the initial default setting of a log when it is created. It is not really relevant and most developers will not even take notice of this category. In many circles, it has already become nonessential. The root log is usually created with level WARNING.
            
        Debug = 10: This level gives detailed information, useful only when a problem is being diagnosed.
            
        Info = 20: This is used to confirm that everything is working as it should.
            
        Warning = 30: This level indicates that something unexpected has happened or some problem is about to happen in the near future.
            
        Error = 40: As it implies, an error has occurred. The software was unable to perform some function.
            
        Critical = 50: A serious error has occurred. The program itself may shut down or not be able to continue running properly.
"""

import logging

logging.basicConfig(filename="selenium_automation_testing_with_python/logging_package9/test.log", level=logging.DEBUG)
logging.warning("Warning message")
logging.info("Info message")
logging.error("Error message")