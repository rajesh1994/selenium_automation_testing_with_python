from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://courses.letskodeit.com/"
class LoginTest():
    def test_valid_login(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.get(url)
        signin_field = driver.find_element(By.XPATH, "//a[@href='/login']")
        signin_field.click()
        email_field = driver.find_element(By.ID,"email")
        email_field.send_keys("test@email.com")
        pwd_field = driver.find_element(By.ID, "password")
        pwd_field.send_keys("abcabc")
        login_button = driver.find_element(By.XPATH, "//input[@value='Login']")
        login_button.click()

        user_icon = driver.find_element(By.XPATH,
                                        "//button[@id='dropdownMenu1']/span[text()='My Account']")
        if user_icon is not None:
            print("Login successfull")
        else:
            print("Login failed")
        
        driver.quit()

ff = LoginTest()
ff.test_valid_login()