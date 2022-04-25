import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://www.expedia.com"

class CalendarSelection():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(url)
        
        #Click the flights tab
        flights_tab = driver.find_element(By.XPATH, "//a[@class='uitk-tab-anchor']/span")
        flights_tab.click()
        
        # Click departing field
        departing_date = driver.find_element(By.ID, "d1-btn")
        departing_date.click()
        # Find the date to be selected
        departing_date_selection = driver.find_element(By.XPATH,
                             "//table[@class='uitk-date-picker-weeks'][position()=1]//button[contains(@aria-label,'May 30')]")
        driver.execute_script("arguments[0].click();", departing_date_selection)
        
        #Click the flights tab
        flights_tab = driver.find_element(By.XPATH, "//a[@class='uitk-tab-anchor']/span")
        flights_tab.click()
        sleep(5)
        
        # Find returning field
        returning_date = driver.find_element(By.ID, "d2-btn")
        returning_date.click()
        # Find the date to be selected
        returning_date_selection = driver.find_element(By.XPATH,
                             "//table[@class='uitk-date-picker-weeks'][position()=1]//button[contains(@aria-label,'Jun 15')]")
        driver.execute_script("arguments[0].click();", returning_date_selection)
        
        #Click the flights tab
        flights_tab = driver.find_element(By.XPATH, "//a[@class='uitk-tab-anchor']/span")
        flights_tab.click()
        
        sleep(5)
        driver.quit()

ff = CalendarSelection()
ff.test()