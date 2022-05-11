from lib2to3.pgen2 import driver
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrappers3 import HandyWrappers


url = "https://courses.letskodeit.com/practice"
class ElementPresenceCheck():
    
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        hw = HandyWrappers(driver)
        hw.driver.get(url)
        hw.driver.implicitly_wait(10)
        
        hideShowTextField = hw.isElementPresent("//input[@name='show-hide']", "xpath")
        print(str(hideShowTextField))
        
        openWindowField = hw.elementPresenceCheck("openwindow", "id")
        print(str(openWindowField))
        hw.driver.quit()
        
ff = ElementPresenceCheck()
ff.test()