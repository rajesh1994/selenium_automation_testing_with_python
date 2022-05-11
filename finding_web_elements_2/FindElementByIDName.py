import os
from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

url = "https://courses.letskodeit.com/practice"
class FindByIDName():
    def test(self):
        driver = webdriver.Firefox(service=Service("/home/dxch075/Documents/python_selenium/browser_drivers/geckodriver"))
        driver.get(url)
        driver.maximize_window() # For maximizing window
        driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
        
        alert_field = driver.find_element(By.ID, "name")
        if alert_field is not None:
            print("We found alert field element by ID")
        
        hide_field = driver.find_element(By.NAME, "show-hide")
        if hide_field is not None:
            print("We found hide field element by name")
        
        driver.quit()

ff = FindByIDName()
ff.test()