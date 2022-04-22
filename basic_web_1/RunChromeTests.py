from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

class RunChromeTest():
    def test(self):
    #Initiate the web driver instance
        driver = webdriver.Chrome(service=Service(executable_path="/home/dxch075/Documents/python_selenium/browser_drivers/chromedriver"))

        driver.get("http://www.letskodeit.com")
        sleep(5)
        driver.quit()

ff = RunChromeTest()
ff.test()