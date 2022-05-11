import sys
import os # if you want this directory
from selenium.webdriver.common.by import By
from pom.base.selenium_driver import SeleniumDriver

try:
    sys.path.index(os.getcwd()) # Or os.getcwd() for this directory
except ValueError:
    sys.path.append(os.getcwd()) # Or os.getcwd() for this directory


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    #Locators
    signin = "//a[@href='/login']"
    email = "email"
    password = "password"
    login_button = "//input[@value='Login']"
    
    def clickLoginLink(self):
        self.elementClick(self.signin, locatorType="xpath")
    
    def enterEmail(self, email):
        self.sendKeys(email, self.email)
    
    def enterPassword(self, password):
        self.sendKeys(password, self.password)
    
    def clickLoginButton(self):
        self.elementClick(self.login_button, locatorType='xpath')
    
    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
