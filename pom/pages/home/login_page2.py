from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
    
    #Locators
    signin = "//a[@href='/login']"
    email = "email"
    password = "password"
    login_button = "//input[@value='Login']"
    
    def get_login_link(self):
        return self.driver.find_element(By.XPATH, self.signin)
    
    def get_email_field(self):
        return self.driver.find_element(By.XPATH, self.email)
    
    def get_password(self):
        return self.driver.find_element(By.XPATH, self.password)
    
    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self.login_button)
    
    def click_login_link(self):
        self.get_login_link().click()
    
    def enter_email(self, email):
        self.get_email_field().send_keys(email)
    
    def enter_password(self, password):
        self.get_password().send_keys(password)
    
    def click_login_button(self):
        self.get_login_button().click()
    
    def login(self, email, password):
        self.get_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
