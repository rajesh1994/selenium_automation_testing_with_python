from lib2to3.pgen2 import driver
import os
from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://courses.letskodeit.com/practice"

class GetText():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        
        open_window_element = driver.find_element(By.ID, "openwindow")
        open_window_element_text = open_window_element.text
        print("Text on 'Open Window Element' is: " + open_window_element_text)
        time.sleep(3)
        driver.quit()
        
        
ff = GetText()
ff.test()