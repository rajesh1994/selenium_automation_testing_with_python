from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time

url = "https://letskodeit.teachable.com/"

class Screenshot():
    def test(self):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(5)
        
        email_field = driver.find_element(By.LINK_TEXT, "Login")
        email_field.click()
        
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("abcabc@gmail.com")
        
        pwd_field = driver.find_element(By.NAME, "password")
        pwd_field.send_keys("password")
        
        login_button = driver.find_element(By.XPATH, "//input[@value='Login']")
        login_button.click()
        
        file_name = "login_screen_" + str(round(time.time())) + ".png"
        screenshot_directory = "/home/dxch075/Desktop/"
        destination = screenshot_directory + file_name
        
        try:
            driver.save_screenshot(destination)
            print("Screenshot saved to the directory -->> :: " + destination)
        except NotADirectoryError:
            print("Provided destination directory is not available")
        
        sleep(5)
        driver.quit()

ff = Screenshot()
ff.test()