from selenium import webdriver
from utilities.handy_wrappers3 import HandyWrappers
import time
import os

url = "https://courses.letskodeit.com/practice"

class Wrappers():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        hw.driver.get(url)
                
        alert_text_field1 = hw.getElement("name")
        alert_text_field1.send_keys("Test")
        time.sleep(2)
        alert_text_field2 = hw.getElement("//input[@name='enter-name']", 'xpath')
        alert_text_field2.clear()
        hw.driver.quit()


ff = Wrappers()
ff.test()