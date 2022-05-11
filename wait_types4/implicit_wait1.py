import email
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://letskodeit.teachable.com"

class ImplicitWait():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(url)
        
        login_field = driver.find_element(By.XPATH, "//a[contains(text(),'Login')]")
        login_field.click()
        
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("test")
        driver.quit()

ff = ImplicitWait()
ff.test()