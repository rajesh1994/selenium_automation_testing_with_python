import sys
import os # if you want this directory
from selenium.webdriver.common.by import By
from pom.base.selenium_driver import SeleniumDriver

try:
    sys.path.index(os.getcwd()) # Or os.getcwd() for this directory
except ValueError:
    sys.path.append(os.getcwd()) # Or os.getcwd() for this directory

class LoginPage():

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//a[@href='/login']"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"

    def clickLoginLink(self):
        self.element(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        self.waitForElement("//div[@id='navbar']//li[@class='dropdown']",
                                       locatorType="xpath")
        result = self.isElementPresent(locator="//div[@id='navbar']//li[@class='dropdown']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator="//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")