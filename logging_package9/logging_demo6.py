import logging
import custom_logger5 as cl
import sys
import os # if you want this directory

try:
    sys.path.index(os.getcwd()) # Or os.getcwd() for this directory
except ValueError:
    sys.path.append(os.getcwd()) # Or os.getcwd() for this directory

class LoggingDemo2():
    log = cl.customLogger(logging.DEBUG)
    
    def method1(self):
        self.log.debug("Debug message")
        self.log.info("Info message")
        self.log.error("Error message")
        self.log.warning("Warning message")
        self.log.critical("Critical message")
    
    def method2(self):
        m2log = cl.customLogger(logging.INFO)
        m2log.debug("Debug message")
        m2log.info("Info message")
        m2log.error("Error message")
        m2log.warning("Warning message")
        m2log.critical("Critical message")
    
    def method3(self):
        m3log = cl.customLogger(logging.INFO)
        m3log.debug("Debug message")
        m3log.info("Info message")
        m3log.error("Error message")
        m3log.warning("Warning message")
        m3log.critical("Critical message")

demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()