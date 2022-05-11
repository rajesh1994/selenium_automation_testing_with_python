import unittest
import sys
import os # if you want this directory
from selenium import webdriver
from selenium.webdriver.common.by import By
from pom.pages.home.login_page3 import LoginPage


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
        login_page = LoginPage(driver=driver)
        login_page.login("test@email.com", "abcabc")        
        driver.quit()