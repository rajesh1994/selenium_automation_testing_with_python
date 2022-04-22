from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import os

class RunFFTest():
    def test(self):
    #Initiate the web driver instance
        driver = webdriver.Firefox(service=Service(executable_path="/home/dxch075/Documents/python_selenium/browser_drivers/geckodriver"))

        driver.get("http://www.letskodeit.com")
        sleep(5)
        driver.quit()

ff = RunFFTest()
ff.test()