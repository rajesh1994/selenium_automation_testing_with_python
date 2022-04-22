import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://courses.letskodeit.com/practice"

class GetAttribute():
    def text(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        
        confirm_button_element = driver.find_element(By.ID, "confirmbtn")
        attribute = confirm_button_element.get_attribute("class")
        print("Value of the attribute is: " + attribute)
        
        time.sleep(3)
        driver.quit()

        
ff = GetAttribute()
ff.text()