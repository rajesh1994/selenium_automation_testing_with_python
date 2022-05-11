import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *

url = "https://www.flipkart.com/"

class ExplicitWait():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        
        login_wizard_close = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")
        login_wizard_close.click()
     
        wait = WebDriverWait(driver, 20, 2, [NoSuchElementException,
                                             ElementNotVisibleException,
                                             ElementNotSelectableException])
        search_text = "Samsung Mobiles"
        search_field = wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@name='q']")))
        search_field.click()
        search_field.send_keys(search_text)
        
        search_button = driver.find_element(By.XPATH, "//button[@class='L0Z3Pu']")
        search_button.click()
        
        search_result_text = "results for "
        search_result = wait.until(ec.text_to_be_present_in_element(
            (By.XPATH, "//span[@class='_10Ermr']"), 'results for "Samsung Mobiles"'))
        
        sleep(5)
        driver.quit()

ff = ExplicitWait()
ff.test()