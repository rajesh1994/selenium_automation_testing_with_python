from traceback import print_stack
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *

class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == 'plink':
            return By.PARTIAL_LINK_TEXT
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False
    
    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found with locator : "+ locator + " locatorType : " + locatorType)
        except:
            print("Element not found with locator : "+ locator + " locatorType : " + locatorType)
            return element
    
    def elementClick(self, locator, locatorType='id'):
        try:
            element = self.getElement(locatorType, locator)
            element.click()
            print("Clicked on element with locator : "+ locator + " locatorType : " + locatorType)
        except:
            print("Cannot clicked on element with locator : "+ locator + " locatorType : " + locatorType)
    
    def sendKeys(self, data, locator, locatorType='id'):
        try:
            element = self.getElement(locatorType, locator)
            element.send_keys(data)
            print("Sent data on element with locator : "+ locator + " locatorType : " + locatorType)
        except:
            print("Cannot sent data on element with locator : "+ locator + " locatorType : " + locatorType)
    
    def isElementPresent(self, locator, locatorType='id'):
        try:
            element = self.getElement(locatorType, locator)
            if element is not None:
                print("Element found!!!")
                return True
            else:
                return False
        except:
            print("Element not found!!!")
            return False
    
    def elementsPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Element found!!!")
                return True
            else:
                print("Element not found!!!")
                return False
        except:
            print("Element not found!!!")
            return False

    def waitForElementToBeClickable(self, locator, locatorType='id',
                       timeout=10,pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
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
            byType = self.getByType(locatorType)
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
