import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://courses.letskodeit.com/practice"


class FindElementsByLinkText():
    def test(self):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window() # For maximizing window
        driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
        
        link_text = driver.find_element(By.LINK_TEXT, "ALL COURSES")
        if link_text is not None:
            print("We found link text element")
        link_text.click()
        sleep(5)
        driver.back()
        
        partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign")
        if partial_link_text is not None:
            print("We found partial link text element") 
        partial_link_text.click()
        sleep(5)
        driver.back()
        
        driver.quit()
        
ff = FindElementsByLinkText()
ff.test()