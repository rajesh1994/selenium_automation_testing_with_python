import os
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://courses.letskodeit.com/practice"
class FindElementByClassCSSSelector():
    def test(self):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        
        class_element = driver.find_element(By.CLASS_NAME, "displayed-class")
        if class_element is not None:
            print("We found class element")
        
        tag_element = driver.find_element(By.CSS_SELECTOR, "h1")
        text = tag_element.text
        if tag_element is not None:
            print("We found tag element with text "+ text)
        
        driver.quit()
        
        
ff = FindElementByClassCSSSelector()
ff.test()