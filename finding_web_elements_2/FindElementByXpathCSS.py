import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By


url = "https://courses.letskodeit.com/practice"

class FindElementByXpathCSS():
    def test(self):
        driver = webdriver.Firefox(service=Service("/home/dxch075/Documents/python_selenium/browser_drivers/geckodriver"))
        driver.get(url)
        driver.maximize_window() # For maximizing window
        driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
        
        alert_field = driver.find_element(By.XPATH, "//fieldset/input[@id='name']")
        if alert_field is not None:
            print("We found an alert field by Xpath")
        
        hide_field = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if hide_field is not None:
            print("We found hide field by CSS Selector")
        
        driver.quit()
            
ff = FindElementByXpathCSS()
ff.test()