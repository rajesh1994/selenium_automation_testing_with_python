from selenium import webdriver
from selenium.webdriver.common.by import By
from explicit_wait_type_wrapper2 import ExplicitWaitType
from time import sleep
import os

url = "https://www.flipkart.com/"

class ExplicitWait():
    def test(self):
        driver = webdriver.Firefox()
        print(os.getcwd())
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        wait = ExplicitWaitType(driver)
        
        login_wizard_close = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")
        login_wizard_close.click()
     
        search_text = "Samsung Mobiles"
        search_field = wait.waitForElementToBeClickable("//input[@name='q']", By.XPATH)
        #search_field = wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@name='q']")))
        search_field.click()
        search_field.send_keys(search_text)
        
        search_button = driver.find_element(By.XPATH, "//button[@class='L0Z3Pu']")
        search_button.click()
        
        search_result = wait.waitForElementToBePresent("//input[@name='q']", By.XPATH)
        search_result = wait.waitForElementToBePresent("//span[@class='_10Ermr']",
                                                       'results for "Samsung Mobiles"', By.XPATH)
        
        sleep(5)
        driver.quit()
        
"""         search_result = wait.until(ec.text_to_be_present_in_element(
            (By.XPATH, "//span[@class='_10Ermr']"), 'results for "Samsung Mobiles"')) """

ff = ExplicitWait()
ff.test()