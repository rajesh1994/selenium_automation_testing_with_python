from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
from selenium.common.exceptions import *
import sys
sys.path.append('/home/dxch075/environments/python_automation/selenium_automation_testing_with_python/utilities3')
from handy_wrappers3 import HandyWrappers

class ExplicitWaitType():
    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrappers(driver)
    
    def waitForElementToBeClickable(self, locator, locatorType='id',
                       timeout=10,pollFrequency=0.5):
        element = None
        try:
            byType = self.hw.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) + 
                  " :: seconds for element to clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(ec.element_to_be_clickable((byType, locator)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element

    def waitForElementToBePresent(self, locator, elementtext, 
                                  locatorType='id', timeout=10,pollFrequency=0.5):
        element = None
        try:
            byType = self.hw.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) + 
                  " :: seconds for element to present")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(ec.text_to_be_present_in_element((byType, locator), elementtext))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element