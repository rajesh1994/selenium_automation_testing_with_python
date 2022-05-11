from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
    
    def login(self, email, password):
        signin_field = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        signin_field.click()
        email_field = self.driver.find_element(By.ID,"email")
        email_field.send_keys(email)
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        login_button.click()
