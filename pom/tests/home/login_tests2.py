import unittest
import sys
import os # if you want this directory
from selenium import webdriver
from selenium.webdriver.common.by import By
from pom.pages.home.login_page2 import LoginPage


try:
    sys.path.index(os.getcwd()) # Or os.getcwd() for this directory
except ValueError:
    sys.path.append(os.getcwd()) # Or os.getcwd() for this directory

url = "https://courses.letskodeit.com/"
class LoginTest(unittest.TestCase):
    def test_valid_login(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.get(url)
        login_page = LoginPage(driver)
        login_page.login("test@email.com", "abcabc")

        user_icon = driver.find_element(By.XPATH,
                                        "//button[@id='dropdownMenu1']/span[text()='My Account']")
        if user_icon is not None:
            print("Login successfull")
        else:
            print("Login failed")
        
        driver.quit()